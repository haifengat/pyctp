#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/22'
"""

import threading
import itertools
import time
import os
import platform
from time import sleep

from .enums import OrderType, InstrumentStatus, DirectType, OffsetType, HedgeType, TradeTypeType
from .structs import InfoField, InstrumentField, OrderField, OrderStatus, PositionField, TradeField, TradingAccount, PositionDetail
from .ctp_trade import Trade
from .ctp_struct import CThostFtdcInputOrderActionField, CThostFtdcInputOrderField, CThostFtdcInstrumentField, CThostFtdcInstrumentStatusField, CThostFtdcInvestorPositionField, CThostFtdcOrderField, CThostFtdcRspInfoField, CThostFtdcRspUserLoginField, CThostFtdcSettlementInfoConfirmField, CThostFtdcTradingAccountField, CThostFtdcTradingNoticeInfoField, CThostFtdcQuoteField, CThostFtdcInputQuoteField, CThostFtdcInputForQuoteField, CThostFtdcInvestorPositionDetailField, CThostFtdcRspAuthenticateField
from .ctp_enum import TThostFtdcActionFlagType, TThostFtdcContingentConditionType, TThostFtdcDirectionType, TThostFtdcOffsetFlagType, TThostFtdcForceCloseReasonType, TThostFtdcHedgeFlagType, TThostFtdcOrderPriceTypeType, TThostFtdcPosiDirectionType, TThostFtdcTimeConditionType, TThostFtdcVolumeConditionType, TThostFtdcOrderStatusType, TThostFtdcInstrumentStatusType, TThostFtdcTradeTypeType, TThostFtdcAppTypeType


class CtpTrade():
    """"""

    def __init__(self):
        self.front_address = ''
        self.investor = ''
        self.password = ''
        self.broker = ''
        self.pub_ip = ''
        '''公网IP'''
        self.port = ''
        '''公网端口'''
        self.logined = False
        self.tradingday = ''

        self.instruments = {}
        self.orders = {}
        self.trades = {}
        self.account: TradingAccount = None
        self.positions = {}
        self.instrument_status = {}

        self._req = 0
        self._session = ''
        self._orderid_sysid = {}
        self._posi = []

        self.t = Trade()

    def _OnFrontConnected(self):
        threading.Thread(target=self.OnConnected, args=(self,)).start()

    def _OnFrontDisconnected(self, nReason):
        self.logined = False
        print(nReason)
        # 下午收盘后会不停断开再连接 4097错误
        if nReason == 4097 or nReason == 4098:
            threading.Thread(target=self._reconnect).start()
        else:
            threading.Thread(target=self.OnDisConnected, args=(self, nReason)).start()

    def _reconnect(self):
        if sum([1 if stat == 'Continous' else 0 for exc, stat in self.instrument_status.items()]) == 0:
            print(time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
            self.t.Release()
            time.sleep(600)
            self.ReqConnect(self.front_address)

    # def _OnRspUserLogout(self, pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
    #     pass

    def _OnRspAuthenticate(self, pRspAuthenticateField: CThostFtdcRspAuthenticateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        if pRspInfo.getErrorID() == 0:
            if pRspAuthenticateField.getAppType() == TThostFtdcAppTypeType.THOST_FTDC_APP_TYPE_InvestorRelay:
                self.t.RegisterUserSystemInfo(self.broker, self.investor, 0, '', self.pub_ip, self.port, time.strftime('%H:%M:%S', time.localtime()))
            elif pRspAuthenticateField.getAppType() == TThostFtdcAppTypeType.THOST_FTDC_APP_TYPE_OperatorRelay:
                self.t.SubmitUserSystemInfo(self.broker, self.investor, 0, '', self.pub_ip, self.port, time.strftime('%H:%M:%S', time.localtime()))
            self.t.ReqUserLogin(BrokerID=self.broker, UserID=self.investor, Password=self.password, UserProductInfo=pRspAuthenticateField.getUserProductInfo())
        else:
            info = InfoField()
            info.ErrorID = pRspInfo.getErrorID()
            info.ErrorMsg = f'认证错误:{pRspInfo.getErrorMsg()}'
            threading.Thread(target=self.OnUserLogin, args=(self, info)).start()

    def _OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField(), pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if pRspInfo.getErrorID() == 0:
            self.session = pRspUserLogin.getSessionID()
            self.tradingday = pRspUserLogin.getTradingDay()
            self.t.ReqSettlementInfoConfirm(self.broker, self.investor)
        elif self.logined:
            threading.Thread(target=self._relogin).start()
        else:
            info = InfoField()
            info.ErrorID = pRspInfo.getErrorID()
            info.ErrorMsg = pRspInfo.getErrorMsg()
            threading.Thread(target=self.OnUserLogin, args=(self, info)).start()

    def _relogin(self):
        # 隔夜重连=>处理'初始化'错误
        time.sleep(60 * 10)
        self.t.ReqUserLogin(
            BrokerID=self.broker,
            UserID=self.investor,
            Password=self.password,
            UserProductInfo='@haifeng')

    def _OnRspSettlementInfoConfirm(
            self,
            pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField,
            pRspInfo: CThostFtdcRspInfoField,
            nRequestID: int,
            bIsLast: bool):
        if not self.logined:
            time.sleep(0.5)
            if self.broker == '9999':
                print("qry instrument")
                self.t.ReqQryInstrument()
            else:
                print("qry classified instrument")
                self.t.ReqQryClassifiedInstrument()

    def _qry(self):
        """查询帐号相关信息"""
        # restart 模式, 待rtnorder 处理完毕后再进行查询,否则会造成position混乱
        ord_cnt = 0
        trd_cnt = 0
        while True:
            time.sleep(0.5)
            if len(self.orders) == ord_cnt and len(self.trades) == trd_cnt:
                break
            ord_cnt = len(self.orders)
            trd_cnt = len(self.trades)
        time.sleep(1.1)
        self.t.ReqQryInvestorPosition(self.broker, self.investor)
        time.sleep(1.1)
        self.t.ReqQryTradingAccount(self.broker, self.investor)
        time.sleep(1.1)

        print('logged')
        self.logined = True
        info = InfoField()
        info.ErrorID = 0
        info.ErrorMsg = '正确'
        threading.Thread(target=self.OnUserLogin, args=(self, info)).start()
        # 调用Release后程序异常退出,但不报错误:接口断开了仍然调用了查询指令
        # while self.logined:
        """查询持仓与权益"""
        self.t.ReqQryInvestorPosition(self.broker, self.investor)

    def _OnRtnInstrumentStatus(self, pInstrumentStatus: CThostFtdcInstrumentStatusField):
        if pInstrumentStatus.getInstrumentID() == '':
            return
        status = InstrumentStatus.Continous
        if pInstrumentStatus.getInstrumentStatus() == TThostFtdcInstrumentStatusType.THOST_FTDC_IS_Continous:
            status = InstrumentStatus.Continous
        elif pInstrumentStatus.getInstrumentStatus() == TThostFtdcInstrumentStatusType.THOST_FTDC_IS_Closed:
            status = InstrumentStatus.Closed
        elif str(pInstrumentStatus.getInstrumentStatus()).startswith('Auction'):
            status = InstrumentStatus.Auction
        else:
            status = InstrumentStatus.NoTrading
        self.instrument_status[pInstrumentStatus.getInstrumentID()] = status
        self.OnInstrumentStatus(self, pInstrumentStatus.getInstrumentID(), status)

    def _OnRspQryInstrument(self, pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        inst = InstrumentField()
        inst.InstrumentID = pInstrument.getInstrumentID()
        inst.InstrumentName = pInstrument.getInstrumentName()
        inst.ProductID = pInstrument.getProductID()
        inst.ExchangeID = pInstrument.getExchangeID()
        inst.VolumeMultiple = pInstrument.getVolumeMultiple()
        inst.PriceTick = pInstrument.getPriceTick()
        inst.MaxOrderVolume = pInstrument.getMaxLimitOrderVolume()
        inst.ProductType = pInstrument.getProductClass().name  # ProductClassType.Futures -> Futures
        self.instruments[inst.InstrumentID] = inst
        if bIsLast:
            sleep(1.1)
            """查询合约/持仓/权益"""
            print('start qry thread')
            threading.Thread(target=self._qry).start()  # 开启查询

    def _OnRspQryClassifiedInstrument(self, pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        self._OnRspQryInstrument(pInstrument, pRspInfo, nRequestID, bIsLast)
        

    def _OnRspQryPosition(self, pInvestorPosition: CThostFtdcInvestorPositionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if pInvestorPosition.getInstrumentID() != '':  # 偶尔出现NULL的数据导致数据转换错误
            if pInvestorPosition.getInstrumentID() in self.instruments: # 解决交易所自主合成某些不可交易的套利合约的问题如 SPC y2005&p2001
                self._posi.append(pInvestorPosition)  # Struct(**f.__dict__)) #dict -> object

        if bIsLast:
            # 先排序再group才有效
            self._posi = sorted(self._posi, key=lambda c: '{0}_{1}'.format(c.getInstrumentID(), DirectType.Buy if c.getPosiDirection() == TThostFtdcPosiDirectionType.THOST_FTDC_PD_Long else DirectType.Sell))
            # direction需从posidiction转换为dictiontype
            for key, group in itertools.groupby(self._posi, lambda c: '{0}_{1}'.format(c.getInstrumentID(), 'Buy' if c.getPosiDirection() == TThostFtdcPosiDirectionType.THOST_FTDC_PD_Long else 'Sell')):
                pf = self.positions.get(key)
                if not pf:
                    pf = PositionField()
                    self.positions[key] = pf
                pf.Position = 0
                pf.TdPosition = 0
                pf.YdPosition = 0
                pf.CloseProfit = 0
                pf.PositionProfit = 0
                pf.Commission = 0
                pf.Margin = 0
                pf.Price = 0
                cost = 0.0
                for g in group:
                    if not pf.InstrumentID:
                        pf.InstrumentID = g.getInstrumentID()
                        pf.Direction = DirectType.Buy if g.getPosiDirection() == TThostFtdcPosiDirectionType.THOST_FTDC_PD_Long else DirectType.Sell
                    pf.Position += g.getPosition()
                    pf.TdPosition += g.getTodayPosition()
                    pf.YdPosition = pf.Position - pf.TdPosition
                    pf.CloseProfit += g.getCloseProfit()
                    pf.PositionProfit += g.getPositionProfit()
                    pf.Commission += g.getCommission()
                    pf.Margin += g.getUseMargin()
                    cost += g.OpenCost
                # pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
                if pf.InstrumentID in self.instruments:
                    vm = self.instruments[pf.InstrumentID].VolumeMultiple
                    pf.Price = 0 if pf.Position <= 0 else (cost / (vm if vm > 0 else 1) / pf.Position)
            self._posi.clear()

            """查询持仓与权益"""
            if not self.logined:
                return
            time.sleep(1.1)
            self.t.ReqQryTradingAccount(self.broker, self.investor)

    def _OnRspQryPositionDetail(self, pInvestorPositionDetail: CThostFtdcInvestorPositionDetailField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """持仓明细"""
        if pInvestorPositionDetail.getInstrumentID() == '':
            return
        detail = PositionDetail()
        detail.Instrument = pInvestorPositionDetail.getInstrumentID()
        detail.CloseProfit = pInvestorPositionDetail.getCloseProfitByTrade()
        detail.Direction = DirectType.Buy if pInvestorPositionDetail.getDirection() == TThostFtdcDirectionType.THOST_FTDC_D_Buy else DirectType.Sell
        detail.HedgeFlag = HedgeType(list(TThostFtdcHedgeFlagType).index(pInvestorPositionDetail.getHedgeFlag()))
        detail.OpenDate = pInvestorPositionDetail.getOpenDate()
        detail.PositionProfit = pInvestorPositionDetail.getPositionProfitByTrade()
        detail.OpenPrice = pInvestorPositionDetail.getOpenPrice()
        detail.TradeType = TradeTypeType(list(TThostFtdcTradeTypeType).index(pInvestorPositionDetail.getTradeType()))
        detail.Volume = pInvestorPositionDetail.getVolume()
        self.position_details[pInvestorPositionDetail.getTradeID()] = detail

    def _OnRspQryAccount(self, pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if not self.account:
            self.account = TradingAccount()
        self.account.Available = pTradingAccount.getAvailable()
        self.account.CloseProfit = pTradingAccount.getCloseProfit()
        self.account.Commission = pTradingAccount.getCommission()
        self.account.CurrMargin = pTradingAccount.getCurrMargin()
        self.account.FrozenCash = pTradingAccount.getFrozenCash()
        self.account.PositionProfit = pTradingAccount.getPositionProfit()
        self.account.PreBalance = pTradingAccount.getPreBalance() + pTradingAccount.getDeposit() + pTradingAccount.getWithdraw()
        self.account.Fund = self.account.PreBalance + pTradingAccount.getCloseProfit() + pTradingAccount.getPositionProfit() - pTradingAccount.getCommission()
        self.account.Risk = 0 if self.account.Fund == 0 else self.account.CurrMargin / self.account.Fund
        if bIsLast:
            """查询持仓与权益"""
            if not self.logined:
                return
            time.sleep(1.1)
            self.t.ReqQryInvestorPosition(self.broker, self.investor)

    def _OnRtnOrder(self, pOrder: CThostFtdcOrderField):
        """"""
        id = '{0}|{1}|{2}'.format(pOrder.getSessionID(), pOrder.getFrontID(), pOrder.getOrderRef())
        of = self.orders.get(id)
        if not of:
            of = OrderField()
            if pOrder.getOrderRef().isdigit():
                of.Custom = int(pOrder.getOrderRef()) % 1000000
            of.InstrumentID = pOrder.getInstrumentID()
            of.ExchangeID = pOrder.getExchangeID()
            of.InsertTime = pOrder.getInsertTime()
            of.Direction = DirectType.Buy if pOrder.getDirection() == TThostFtdcDirectionType.THOST_FTDC_D_Buy else DirectType.Sell
            ot = TThostFtdcOffsetFlagType(ord(pOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open else OffsetType.CloseToday if ot == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday else OffsetType.Close
            of.Status = OrderStatus.Normal
            of.StatusMsg = pOrder.getStatusMsg()
            of.IsLocal = pOrder.getSessionID() == self.session
            of.LimitPrice = pOrder.getLimitPrice()
            of.OrderID = id
            of.Volume = pOrder.getVolumeTotalOriginal()
            of.VolumeLeft = of.Volume
            self.orders[id] = of
            threading.Thread(target=self.OnOrder, args=(self, of)).start()
        elif pOrder.getOrderStatus() == TThostFtdcOrderStatusType.THOST_FTDC_OST_Canceled:
            of.Status = OrderStatus.Canceled
            of.StatusMsg = pOrder.getStatusMsg()

            if of.StatusMsg.find('被拒绝') >= 0:
                info = InfoField()
                info.ErrorID = -1
                info.ErrorMsg = of.StatusMsg
                threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()
            else:
                threading.Thread(target=self.OnCancel, args=(self, of)).start()
        else:
            if pOrder.getOrderSysID():
                of.SysID = pOrder.getOrderSysID()
                self._orderid_sysid[pOrder.getOrderSysID()] = id  # 记录sysid与orderid关联,方便Trade时查找处理

    def _OnRtnTrade(self, f):
        """"""
        tf = TradeField()
        tf.Direction = DirectType.Buy if f.getDirection() == TThostFtdcDirectionType.THOST_FTDC_D_Buy else DirectType.Sell
        tf.ExchangeID = f.getExchangeID()
        tf.InstrumentID = f.getInstrumentID()
        tf.Offset = OffsetType.Open if f.getOffsetFlag() == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open else OffsetType.Close if f.getOffsetFlag() == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Close else OffsetType.CloseToday
        tf.Price = f.getPrice()
        tf.SysID = f.getOrderSysID()
        tf.TradeID = f.getTradeID()
        tf.TradeTime = f.getTradeTime()
        tf.TradingDay = f.getTradingDay()
        tf.Volume = f.getVolume()

        self.trades[f'{tf.TradeID}{tf.Direction.value}'] = tf

        id = self._orderid_sysid[tf.SysID]
        of = self.orders[id]
        tf.OrderID = id  # tradeid 与 orderid 关联
        of.TradeTime = tf.TradeTime
        of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + tf.Price *
                       tf.Volume) / (of.Volume - of.VolumeLeft + tf.Volume)
        of.TradeVolume = tf.Volume
        of.VolumeLeft -= tf.Volume
        if of.VolumeLeft == 0:
            of.Status = OrderStatus.Filled
            of.StatusMsg = '全部成交'
        else:
            of.Status = OrderStatus.Partial
            of.StatusMsg = '部分成交'
        # 更新持仓 *****
        if tf.Offset == OffsetType.Open:
            key = '{0}_{1}'.format(tf.InstrumentID, 'Buy' if tf.Direction == DirectType.Buy else 'Sell')
            pf = self.positions.get(key)
            if not pf:
                pf = PositionField()
                self.positions[key] = pf
            pf.InstrumentID = tf.InstrumentID
            pf.Direction = tf.Direction
            pf.Price = (pf.Price * pf.Position + tf.Price * tf.Volume) / (pf.Position + tf.Volume)
            pf.TdPosition += tf.Volume
            pf.Position += tf.Volume
        else:
            key = '{0}_{1}'.format(tf.InstrumentID, 'Sell' if tf.Direction == DirectType.Buy else 'Buy')
            pf: PositionField = self.positions.get(key)
            if pf:  # 有可能出现无持仓的情况
                if tf.Offset == OffsetType.CloseToday:
                    pf.TdPosition -= tf.Volume
                else:
                    ydclose = min(pf.YdPosition, tf.Volume)
                    if pf.YdPosition > 0:
                        pf.YdPosition -= ydclose
                    pf.TdPosition -= max(0, tf.Volume - ydclose)
                pf.Position -= tf.Volume
        threading.Thread(target=self._onRtn, args=(of, tf)).start()

    def _onRtn(self, of, tf):
        self.OnOrder(self, of)
        self.OnTrade(self, tf)

    def _OnRspOrder(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        id = '{0}|{1}|{2}'.format(self.session, '0', pInputOrder.getOrderRef())
        of = self.orders.get(id)
        if not of:
            of = OrderField()
            l = int(pInputOrder.getOrderRef())
            of.Custom = l % 1000000
            of.InstrumentID = pInputOrder.getInstrumentID()
            of.InsertTime = time.strftime('%H:%M:%S', time.localtime())
            # 对direction需特别处理（具体见ctp_struct）
            of.Direction = DirectType.Buy if pInputOrder.getDirection() == TThostFtdcDirectionType.THOST_FTDC_D_Buy else DirectType.Sell
            ot = TThostFtdcOffsetFlagType(ord(pInputOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open else OffsetType.CloseToday if ot == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday else OffsetType.Close
            # of.Status = OrderStatus.Normal
            # of.StatusMsg = f.getStatusMsg()
            of.IsLocal = True
            of.LimitPrice = pInputOrder.getLimitPrice()
            of.OrderID = id
            of.Volume = pInputOrder.getVolumeTotalOriginal()
            of.VolumeLeft = of.Volume
            self.orders[id] = of

        of.Status = OrderStatus.Error
        of.StatusMsg = '{0}:{1}'.format(info.ErrorID, info.ErrorMsg)
        threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()

    def _OnErrOrder(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField):
        """"""
        id = '{0}|{1}|{2}'.format(self.session, '0', pInputOrder.getOrderRef())
        of = self.orders.get(id)

        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        if of and of.IsLocal:
            of.Status = OrderStatus.Error
            of.StatusMsg = '{0}:{1}'.format(pRspInfo.getErrorID(), pRspInfo.getErrorMsg())
            threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()

    def _OnRspOrderAction(self, pInputOrderAction: CThostFtdcInputOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        id = "{0}|{1}|{2}".format(pInputOrderAction.getSessionID(), pInputOrderAction.getFrontID(), pInputOrderAction.getOrderRef())
        if self.logined and id in self.orders:
            info = InfoField()
            info.ErrorID = pRspInfo.ErrorID
            info.ErrorMsg = pRspInfo.ErrorMsg
            threading.Thread(target=self.OnErrCancel, args=(self, self.orders[id], info)).start()

    def _OnRtnNotice(self, pTradingNoticeInfo: CThostFtdcTradingNoticeInfoField):
        '''交易提醒'''
        msg = pTradingNoticeInfo.getFieldContent()
        if len(msg) > 0:
            threading.Thread(target=self.OnRtnNotice, args=(self, pTradingNoticeInfo.getSendTime(), msg)).start()

    def _OnRtnQuote(self, pQuote: CThostFtdcQuoteField):
        threading.Thread(target=self.OnRtnQuote, args=(self, pQuote)).start()

    def _OnErrRtnQuote(self, pInputQuote: CThostFtdcInputQuoteField, pRspInfo: CThostFtdcRspInfoField):
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()
        threading.Thread(target=self.OnErrRtnQuote, args=(self, pInputQuote, info)).start()

    def _OnErrForQuoteInsert(self, pInputForQuote: CThostFtdcInputForQuoteField, pRspInfo: CThostFtdcRspInfoField):
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()
        threading.Thread(target=self.OnErrRtnForQuoteInsert, args=(self, pInputForQuote, info)).start()

    def _OnRspError(self, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()
        threading.Thread(target=self.OnRspError, args=(self, info)).start()

    def GetVersion(self):
        return self.t.GetVersion()

    def ReqConnect(self, front: str):
        """连接交易前置

        :param front:
        """
        self.t.CreateApi()
        spi = self.t.CreateSpi()
        self.t.RegisterSpi(spi)

        self.t.OnFrontConnected = self._OnFrontConnected
        self.t.OnRspUserLogin = self._OnRspUserLogin
        self.t.OnRspAuthenticate = self._OnRspAuthenticate
        self.t.OnFrontDisconnected = self._OnFrontDisconnected
        # self.t.OnRspUserLogout = self._OnRspUserLogout
        self.t.OnRspSettlementInfoConfirm = self._OnRspSettlementInfoConfirm
        self.t.OnRtnOrder = self._OnRtnOrder
        self.t.OnRtnTrade = self._OnRtnTrade
        self.t.OnRspOrderInsert = self._OnRspOrder
        self.t.OnErrRtnOrderInsert = self._OnErrOrder
        self.t.OnRspOrderAction = self._OnRspOrderAction
        self.t.OnRtnInstrumentStatus = self._OnRtnInstrumentStatus
        self.t.OnRspQryInstrument = self._OnRspQryInstrument
        self.t.OnRspClassifiedInstrument = self._OnRspQryClassifiedInstrument
        self.t.OnRspQryTradingAccount = self._OnRspQryAccount
        self.t.OnRspQryInvestorPosition = self._OnRspQryPosition
        self.t.OnRspQryInvestorPositionDetail = self._OnRspQryPositionDetail
        self.t.OnRtnTradingNotice = self._OnRtnNotice
        self.t.OnRtnQuote = self._OnRtnQuote
        self.t.OnErrRtnQuoteInsert = self._OnErrRtnQuote
        self.t.OnErrRtnForQuoteInsert = self._OnErrForQuoteInsert
        self.t.OnRspError = self._OnRspError

        self.front_address = front
        self.t.RegCB()
        self.t.RegisterFront(front)
        self.t.SubscribePrivateTopic(0)  # restart 同步处理order trade
        self.t.SubscribePublicTopic(0)
        self.t.Init()
        # self.t.Join()

    def ReqUserLogin(self, user: str, pwd: str, broker: str, proc_info: str, appid: str, auth_code: str):
        """登录

        :param user:
        :param pwd:
        :param broker:
        """
        self.broker = broker
        self.investor = user
        self.password = pwd
        self.t.ReqAuthenticate(broker, user, proc_info, auth_code, appid)

    def ReqOrderInsert(self, pInstrument: str, pDirection: DirectType, pOffset: OffsetType, pPrice: float = 0.0, pVolume: int = 1, pType: OrderType = OrderType.Limit, pCustom: int = 0):
        """委托

        :param pInstrument:
        :param pDirection:
        :param pOffset:
        :param pPrice:
        :param pVolume:
        :param pType:
        :param pCustom:
        :return:
        """
        OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice
        TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC
        LimitPrice = 0.0
        VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV

        if pType == OrderType.Market:  # 市价
            OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice
            TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC
            LimitPrice = 0.0
            VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV
        elif pType == OrderType.Limit:  # 限价
            OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice
            TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_GFD
            LimitPrice = pPrice
            VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV
        elif pType == OrderType.FAK:  # FAK
            OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice
            TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC
            LimitPrice = pPrice
            VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV
        elif pType == OrderType.FOK:  # FOK
            OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice
            TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC
            LimitPrice = pPrice
            VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_CV  # 全部数量

        self._req += 1
        self.t.ReqOrderInsert(
            BrokerID=self.broker,
            InvestorID=self.investor,
            InstrumentID=pInstrument,
            OrderRef="%06d%06d" % (self._req, pCustom % 1000000),
            UserID=self.investor,
            ExchangeID=self.instruments[pInstrument].ExchangeID,
            # 此处ctp_enum与at_struct名称冲突
            Direction=TThostFtdcDirectionType.THOST_FTDC_D_Buy if pDirection == DirectType.Buy else TThostFtdcDirectionType.THOST_FTDC_D_Sell,
            CombOffsetFlag=chr(TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open.value if pOffset == OffsetType.Open else TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday.value if pOffset == OffsetType.CloseToday else TThostFtdcOffsetFlagType.THOST_FTDC_OF_Close.value),
            CombHedgeFlag=chr(TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation.value),
            IsAutoSuspend=0,
            ForceCloseReason=TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,
            IsSwapOrder=0,
            ContingentCondition=TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,
            VolumeCondition=VolumeCondition,
            MinVolume=1,
            VolumeTotalOriginal=pVolume,
            OrderPriceType=OrderPriceType,
            TimeCondition=TimeCondition,
            LimitPrice=LimitPrice,
        )

    def ReqOrderAction(self, OrderID: str):
        """撤单

        :param OrderID:
        """
        of = self.orders[OrderID]

        if not of:
            return -1
        else:
            pOrderId = of.OrderID
            return self.t.ReqOrderAction(
                self.broker,
                self.investor,
                OrderRef=pOrderId.split('|')[2],
                FrontID=int(pOrderId.split('|')[1]),
                SessionID=int(pOrderId.split('|')[0]),
                InstrumentID=of.InstrumentID,
                ExchangeID=of.ExchangeID,
                ActionFlag=TThostFtdcActionFlagType.THOST_FTDC_AF_Delete)

    def ReqUserLogout(self):
        """退出接口"""
        self.logined = False
        time.sleep(3)
        self.t.ReqUserLogout(BrokerID=self.broker, UserID=self.investor)
        self.t.RegisterSpi(None)
        self.t.Release()
        threading.Thread(target=self.OnDisConnected, args=(self, 0)).start()

    def OnConnected(self, obj):
        """接口连接

        :param obj:
        """
        print('=== [TRADE] OnConnected ==='.format(''))

    def OnDisConnected(self, obj, reason: int):
        """接口断开

        :param obj:
        :param reason:
        """
        print('=== [TRADE] OnDisConnected === \nreason: {0}'.format(reason))

    def OnUserLogin(self, obj, info: InfoField):
        """登录响应

        :param obj:
        :param info:
        """
        print('=== [TRADE] OnUserLogin === \n{0}'.format(info))

    def OnOrder(self, obj, f: OrderField):
        """委托响应

        :param obj:
        :param f:
        """
        print('=== [TRADE] OnOrder === \n{0}'.format(f.__dict__))

    def OnTrade(self, obj, f: TradeField):
        """成交响应

        :param obj:
        :param f:
        """
        print('=== [TRADE] OnTrade === \n{0}'.format(f.__dict__))

    def OnCancel(self, obj, f: OrderField):
        """
        撤单响应
            :param self:
            :param obj:
            :param f:OrderField:
        """
        print('=== [TRADE] OnCancel === \n{0}'.format(f.__dict__))

    def OnErrCancel(self, obj, f: OrderField, info: InfoField):
        """
        撤单失败
            :param self:
            :param obj:
            :param f:OrderField:
            :param info:InfoField:
        """
        print('=== [TRADE] OnErrCancel ===\n{0}'.format(f.__dict__))
        print(info)


    def OnRspError(self, obj, info: InfoField):
        """
        撤单失败
            :param self:
            :param obj:
            :param f:OrderField:
            :param info:InfoField:
        """
        print('=== [TRADE] OnRspError ===\n{0}'.format(info.__dict__))

    def OnErrOrder(self, obj, f: OrderField, info: InfoField):
        """
        委托错误
            :param self:
            :param obj:
            :param f:OrderField:
            :param info:InfoField:
        """
        print('=== [TRADE] OnErrOrder ===\n{0}'.format(f.__dict__))
        print(info)

    def OnInstrumentStatus(self, obj, inst: str, status: InstrumentStatus):
        """
        交易状态
            :param self:
            :param obj:
            :param inst:str:
            :param status:InstrumentStatus:
        """
        print('{}:{}'.format(inst, str(status).strip().split('.')[-1]))

    def OnRtnNotice(self, obj, time: str, msg: str):
        """交易提醒

        :param obj:
        :param time:
        :param msg:
        :return:
        """
        print(f'=== OnRtnNotice===\n {time}:{msg}')

    def OnRtnQuote(self, obj, quote: CThostFtdcQuoteField):
        """报价通知

        :param obj:
        :param quote:
        :return:
        """
        print('=== [TRADE] OnRtnQuote ===\n{0}'.format(quote.__dict__))

    def OnErrRtnQuote(self, obj, quote: CThostFtdcInputQuoteField, info: InfoField):
        """

        :param obj:
        :param quote:
        :return:
        """
        print('=== [TRADE] OnErrRtnQuote ===\n{0}'.format(quote.__dict__))
        print(info)

    def OnErrRtnForQuoteInsert(self, obj, quote: CThostFtdcInputQuoteField, info: InfoField):
        """询价录入错误回报

        :param obj:
        :param quote:
        :return:
        """
        print('=== [TRADE] OnErrRtnForQuoteInsert ===\n{0}'.format(quote.__dict__))
        print(info)
