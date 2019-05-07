#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import _thread
from .ctp_trade import Trade
from .ctp_quote import Quote
from .ctp_struct import *

"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""
import sys
import os
import platform

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


class Test:

    def __init__(self):
        self.front_addr = self.investor = self.pwd = self.broker = self.product_info = self.app_id = self.auth_code = ''
        self.Session = ''
        self.q = Quote()
        self.t = Trade()
        self.req = 0
        self.ordered = False
        self.RelogEnable = True

    def q_OnFrontConnected(self):
        print('connected')
        self.q.ReqUserLogin(BrokerID=self.broker, UserID=self.investor, Password=self.pwd)

    def q_OnRspUserLogin(self, rsp: CThostFtdcRspUserLoginField, info: CThostFtdcRspInfoField, req: int, last: bool):
        print(info.__str__)
        self.q.SubscribeMarketData('rb1905')

    def q_OnTick(self, tick: CThostFtdcMarketDataField):
        f = tick
        # print(tick)

        if not self.ordered:
            _thread.start_new_thread(self.Order, (f,))
            self.ordered = True

    def Order(self, f: CThostFtdcMarketDataField):
        print("报单")
        self.req += 1
        self.t.ReqOrderInsert(
            BrokerID=self.broker,
            InvestorID=self.investor,
            InstrumentID=f.getInstrumentID(),
            OrderRef='{0:>12}'.format(self.req),
            UserID=self.investor,
            OrderPriceType=TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice,
            Direction=TThostFtdcDirectionType.THOST_FTDC_D_Buy,
            CombOffsetFlag=chr(TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open.value),
            CombHedgeFlag=chr(TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation.value),
            LimitPrice=f.getLastPrice() - 50,
            VolumeTotalOriginal=1,
            TimeCondition=TThostFtdcTimeConditionType.THOST_FTDC_TC_GFD,
            # GTDDate=''
            VolumeCondition=TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV,
            MinVolume=1,
            ContingentCondition=TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,
            StopPrice=0,
            ForceCloseReason=TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,
            IsAutoSuspend=0,
            IsSwapOrder=0,
            UserForceClose=0)

    def OnFrontConnected(self):
        if not self.RelogEnable:
            return
        print('connected')
        self.t.ReqAuthenticate(self.broker, self.investor, self.product_info, self.app_id, self.auth_code)

    def OnFrontDisconnected(self, reason: int):
        print(reason)

    def OnRspAuthenticate(self, pRspAuthenticateField: CThostFtdcRspAuthenticateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('auth：{0}:{1}'.format(pRspInfo.getErrorID(), pRspInfo.getErrorMsg()))
        self.t.ReqUserLogin(BrokerID=self.broker, UserID=self.investor, Password=self.pwd, UserProductInfo='@haifeng')

    def OnRspUserLogin(self, rsp: CThostFtdcRspUserLoginField, info: CThostFtdcRspInfoField, req: int, last: bool):
        print(info.getErrorMsg())

        if info.getErrorID() == 0:
            self.Session = rsp.getSessionID()
            self.t.ReqSettlementInfoConfirm(BrokerID=self.broker, InvestorID=self.investor)
        else:
            self.RelogEnable = False

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        # print(pSettlementInfoConfirm)
        _thread.start_new_thread(self.StartQuote, ())

    def StartQuote(self):
        self.q.CreateApi()
        spi = self.q.CreateSpi()
        self.q.RegisterSpi(spi)

        self.q.OnFrontConnected = self.q_OnFrontConnected
        self.q.OnRspUserLogin = self.q_OnRspUserLogin
        self.q.OnRtnDepthMarketData = self.q_OnTick

        self.q.RegCB()

        self.q.RegisterFront(self.front_addr.split(',')[1])
        self.q.Init()
        # self.q.Join()

    def Qry(self):
        sleep(1.1)
        self.t.ReqQryInstrument()
        while True:
            sleep(1.1)
            self.t.ReqQryTradingAccount(self.broker, self.investor)
            sleep(1.1)
            self.t.ReqQryInvestorPosition(self.broker, self.investor)
            return

    def OnRtnInstrumentStatus(self, pInstrumentStatus: CThostFtdcInstrumentStatusField):
        print(pInstrumentStatus.getInstrumentStatus())

    def OnRspOrderInsert(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('OnRspOrderInsert')
        print(pRspInfo)
        print(pInputOrder)

    def OnRtnOrder(self, pOrder: CThostFtdcOrderField):
        print(pOrder)
        if pOrder.getSessionID() == self.Session and pOrder.getOrderStatus() == TThostFtdcOrderStatusType.THOST_FTDC_OST_NoTradeNotQueueing:
            print("撤单")
            self.t.ReqOrderAction(
                self.broker, self.investor,
                InstrumentID=pOrder.getInstrumentID(),
                OrderRef=pOrder.getOrderRef(),
                FrontID=pOrder.getFrontID(),
                SessionID=pOrder.getSessionID(),
                ActionFlag=ActionFlagType.Delete)

    def Run(self):
        # CreateApi时会用到log目录,需要在程序目录下创建**而非dll下**
        self.t.CreateApi()
        spi = self.t.CreateSpi()
        self.t.RegisterSpi(spi)

        self.t.OnFrontConnected = self.OnFrontConnected
        self.t.OnFrontDisconnected = self.OnFrontDisconnected
        self.t.OnRspUserLogin = self.OnRspUserLogin
        self.t.OnRspSettlementInfoConfirm = self.OnRspSettlementInfoConfirm
        self.t.OnRspAuthenticate = self.OnRspAuthenticate
        self.t.OnRtnInstrumentStatus = self.OnRtnInstrumentStatus
        self.t.OnRspOrderInsert = self.OnRspOrderInsert
        self.t.OnRtnOrder = self.OnRtnOrder
        # _thread.start_new_thread(self.Qry, ())
        self.t.RegCB()

        # 配置帐号信息
        self.front_addr = 'tcp://180.168.146.187:13030,tcp://180.168.146.187:13040'
        self.broker = '9999'
        self.investor = ''
        self.pwd = ''
        self.product_info = ''
        self.app_id = ''
        self.auth_code = ''

        self.t.RegisterFront(self.front_addr.split(',')[0])
        self.t.SubscribePrivateTopic(nResumeType=2)  # quick
        self.t.SubscribePrivateTopic(nResumeType=2)
        self.t.Init()
        # self.t.Join()


if __name__ == '__main__':
    t = Test()
    t.Run()
    input()
    t.t.Release()
    input()
