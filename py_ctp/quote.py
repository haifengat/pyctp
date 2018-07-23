#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/23'
"""

import _thread
from time import time
import platform
import os

import sys
sys.path.append('.')
from py_ctp.structs import InfoField, Tick
from py_ctp.ctp_quote import Quote
from py_ctp.ctp_struct import CThostFtdcRspUserLoginField, CThostFtdcRspInfoField, CThostFtdcDepthMarketDataField


class CtpQuote(object):
    """"""

    def __init__(self):
        dllpath = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..', 'dll')
        self.q = Quote(os.path.join(dllpath, 'ctp_quote.' + ('dll' if 'Windows' in platform.system() else 'so')))
        self.inst_tick = {}

    def ReqConnect(self, pAddress: str):
        self.q.CreateApi()
        spi = self.q.CreateSpi()
        self.q.RegisterSpi(spi)

        self.q.OnFrontConnected = self._OnFrontConnected
        self.q.OnFrontDisconnected = self._OnFrontDisConnected
        self.q.OnRspUserLogin = self._OnRspUserLogin
        self.q.OnRtnDepthMarketData = self._OnRtnDepthMarketData

        self.q.RegCB()

        self.q.RegisterFront(pAddress)
        self.q.Init()

    def ReqUserLogin(self, user: str, pwd: str, broker: str):
        self.q.ReqUserLogin(BrokerID=broker, UserID=user, Password=pwd)

    def ReqSubscribeMarketData(self, pInstrument: str):
        self.q.SubscribeMarketData(pInstrument)

    def Release(self):
        self.q.Release()
        _thread.start_new_thread(self.OnDisConnected, (self, 0))

    def _OnFrontConnected(self):
        """"""
        _thread.start_new_thread(self.OnConnected, (self,))

    def _OnFrontDisConnected(self, reason: int):
        """"""
        _thread.start_new_thread(self.OnDisConnected, (self, reason))

    def _OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()
        self.IsLogin = True
        _thread.start_new_thread(self.OnUserLogin, (self, info))

    def _OnRtnDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField):
        """"""
        tick = Tick()
        tick.AskPrice = pDepthMarketData.getAskPrice1()
        tick.AskVolume = pDepthMarketData.getAskVolume1()
        tick.AveragePrice = pDepthMarketData.getAveragePrice()
        tick.BidPrice = pDepthMarketData.getBidPrice1()
        tick.BidVolume = pDepthMarketData.getBidVolume1()
        tick.Instrument = pDepthMarketData.getInstrumentID()
        tick.LastPrice = pDepthMarketData.getLastPrice()
        tick.OpenInterest = pDepthMarketData.getOpenInterest()
        tick.Volume = pDepthMarketData.getVolume()

        day = pDepthMarketData.getTradingDay()
        str = day + ' ' + pDepthMarketData.getUpdateTime()
        if day is None or day == ' ':
            str = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
        tick.UpdateTime = str  # time.strptime(str, '%Y%m%d %H:%M:%S')
        self.inst_tick[tick.Instrument] = tick
        _thread.start_new_thread(self.OnTick, (self, tick))
        # self.OnRtnTick(tick)

    def OnDisConnected(self, obj, error: int):
        """"""
        print('disconnected: ' + str(error))

    def OnConnected(self, obj):
        """"""
        print('connected')

    def OnUserLogin(self, obj, info: InfoField):
        """"""
        print(info)

    def OnTick(self, obj, f: Tick):
        """"""
        print(f.__dict__)


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
