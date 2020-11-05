#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""

import threading
import platform
import os

from .structs import InfoField, Tick
from .ctp_quote import Quote
from .ctp_struct import CThostFtdcRspUserLoginField, CThostFtdcRspInfoField, CThostFtdcDepthMarketDataField, CThostFtdcSpecificInstrumentField


class CtpQuote(object):
    """"""

    def __init__(self):
        self.q = Quote()
        self.inst_tick = {}
        self.logined = False

    def ReqConnect(self, pAddress: str):
        """连接行情前置

        :param pAddress:
        """
        self.q.CreateApi()
        spi = self.q.CreateSpi()
        self.q.RegisterSpi(spi)

        self.q.OnFrontConnected = self._OnFrontConnected
        self.q.OnFrontDisconnected = self._OnFrontDisConnected
        self.q.OnRspUserLogin = self._OnRspUserLogin
        self.q.OnRtnDepthMarketData = self._OnRtnDepthMarketData
        self.q.OnRspSubMarketData = self._OnRspSubMarketData

        self.q.RegCB()

        self.q.RegisterFront(pAddress)
        self.q.Init()

    def ReqUserLogin(self, user: str, pwd: str, broker: str):
        """登录

        :param user:
        :param pwd:
        :param broker:
        """
        self.q.ReqUserLogin(BrokerID=broker, UserID=user, Password=pwd)

    def ReqSubscribeMarketData(self, pInstrument: str):
        """订阅合约行情

        :param pInstrument:
        """
        self.q.SubscribeMarketData(pInstrument)

    def ReqUserLogout(self):
        """退出接口(正常退出,不会触发OnFrontDisconnected)"""

        self.q.Release()
        # 确保隔夜或重新登录时的第1个tick不被发送到客户端
        self.inst_tick.clear()
        self.logined = False
        threading.Thread(target=self.OnDisConnected, args=(self, 0)).start()

    def _OnFrontConnected(self):
        """"""
        threading.Thread(target=self.OnConnected, args=(self,)).start()

    def _OnFrontDisConnected(self, reason: int):
        """"""
        # 确保隔夜或重新登录时的第1个tick不被发送到客户端
        self.inst_tick.clear()
        self.logined = False
        threading.Thread(target=self.OnDisConnected, args=(self, reason)).start()

    def _OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()
        self.logined = True
        threading.Thread(target=self.OnUserLogin, args=(self, info)).start()

    def _OnRspSubMarketData(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        pass

    def _OnRtnDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField):
        """"""
        tick: Tick = None
        # 这个逻辑交由应用端处理更合理 ==> 第一个tick不送给客户端(以处理隔夜早盘时收到夜盘的数据的问题)
        inst = pDepthMarketData.getInstrumentID()
        if inst not in self.inst_tick:
            tick = Tick()
            self.inst_tick[inst] = tick
        else:
            tick = self.inst_tick[inst]

        tick.AskPrice = pDepthMarketData.getAskPrice1()
        tick.AskVolume = pDepthMarketData.getAskVolume1()
        tick.AveragePrice = pDepthMarketData.getAveragePrice()
        tick.BidPrice = pDepthMarketData.getBidPrice1()
        tick.BidVolume = pDepthMarketData.getBidVolume1()
        tick.Instrument = pDepthMarketData.getInstrumentID()
        tick.LastPrice = pDepthMarketData.getLastPrice()
        tick.OpenInterest = pDepthMarketData.getOpenInterest()
        tick.Volume = pDepthMarketData.getVolume()

        # 用tradingday替代Actionday不可取
        # day = pDepthMarketData.getTradingDay()
        # str = day + ' ' + pDepthMarketData.getUpdateTime()
        # if day is None or day == ' ':
        #     str = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
        # tick.UpdateTime = str  # time.strptime(str, '%Y%m%d %H:%M:%S')

        tick.UpdateTime = pDepthMarketData.getUpdateTime()
        tick.UpdateMillisec = pDepthMarketData.getUpdateMillisec()
        tick.UpperLimitPrice = pDepthMarketData.getUpperLimitPrice()
        tick.LowerLimitPrice = pDepthMarketData.getLowerLimitPrice()
        tick.PreOpenInterest = pDepthMarketData.getPreOpenInterest()

        # 用线程会导入多数据入库时报错
        # threading.Thread(target=self.OnTick, args=(self, tick))
        self.OnTick(self, tick)

    def OnDisConnected(self, obj, error: int):
        """"""
        print(f'=== [QUOTE] OnDisConnected===\nerror: {str(error)}')

    def OnConnected(self, obj):
        """"""
        print('=== [QUOTE] OnConnected ===')

    def OnUserLogin(self, obj, info: InfoField):
        """"""
        print(f'=== [QUOTE] OnUserLogin ===\n{info}')

    def OnTick(self, obj, f: Tick):
        """"""
        print(f'=== [QUOTE] OnTick ===\n{f.__dict__}')


def connected(obj):
    print('connected')
    obj.ReqUserLogin('008105', '1', '9999')


def logged(obj, info):
    print(info)


def main():
    q = CtpQuote()
    q.OnConnected = connected
    q.OnUserLogin = logged
    q.ReqConnect('tcp://180.168.146.187:10010')

    input()
    q.Release()
    input()


if __name__ == '__main__':
    main()
