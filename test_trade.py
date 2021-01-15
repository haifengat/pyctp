#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'test py ctp of se'
__author__ = 'HaiFeng'
__mtime__ = '20190506'

from py_ctp.trade import CtpTrade
from py_ctp.quote import CtpQuote
from py_ctp.enums import *
import time


class TestTrade(object):
    def __init__(self, addr: str, broker: str, investor: str, pwd: str, appid: str, auth_code: str):
        self.front = addr
        self.broker = broker
        self.investor = investor
        self.pwd = pwd
        self.appid = appid
        self.authcode = auth_code
        self.proc = '@haifeng'

        self.t = CtpTrade()
        self.t.OnConnected = self.on_connect
        self.t.OnUserLogin = lambda o, x: print('Trade logon:', x)
        self.t.OnDisConnected = lambda o, x: print(x)
        self.t.OnRtnNotice = lambda obj, time, msg: print(f'OnNotice: {time}:{msg}')
        self.t.OnErrRtnQuote = lambda obj, quote, info: None
        self.t.OnErrRtnQuoteInsert = lambda obj, o: None
        self.t.OnOrder = lambda obj, o: None
        self.t.OnErrOrder = lambda obj, f, info: None # print(info)
        self.t.OnTrade = lambda obj, o: None
        self.t.OnCancel = lambda obj, o: None
        self.t.OnInstrumentStatus = lambda obj, inst, stat: None
        self.t.OnRspError = lambda obj, info: print(info)
        

    def on_connect(self, obj):
        self.t.ReqUserLogin(self.investor, self.pwd, self.broker, self.proc, self.appid, self.authcode)

    def run(self):
        print(self.t.GetVersion())
        print('trade connect...')
        self.t.ReqConnect(self.front)

    def release(self):
        self.t.ReqUserLogout()


class TestQuote(object):
    """TestQuote"""

    def __init__(self, addr: str, broker: str, investor: str, pwd: str):
        """"""
        self.front = addr
        self.broker = broker
        self.investor = investor
        self.pwd = pwd

        self.q = CtpQuote()
        self.q.OnTick = lambda o, x: print(x)
        self.q.OnConnected = lambda x: self.q.ReqUserLogin(self.investor, self.pwd, self.broker)
        self.q.OnUserLogin = lambda o, i: self.q.ReqSubscribeMarketData('rb2101')

    def run(self):
        print('quote connecting...')
        self.q.ReqConnect(self.front)

    def release(self):
        self.q.ReqUserLogout()


if __name__ == "__main__":
    front_trade = 'tcp://180.168.146.187:10101'
    front_quote = 'tcp://180.168.146.187:10111'
    broker = '9999'
    investor = '008107'
    pwd = '1'
    appid = 'simnow_client_test'
    auth_code = '0000000000000000'
    
    tt = TestTrade(front_trade, broker, investor, pwd, appid, auth_code)
    tt.run()
    while not tt.t.logined:
        time.sleep(3)
    print('account info')
    print(tt.t.account)
    print(len(tt.t.instruments))
    # tt.t.ReqOrderInsert('rb2101', DirectType.Buy, OffsetType.Open, 4000, 3)

    qq = TestQuote(front_quote, broker, investor, pwd)
    qq.run()
    
    time.sleep(5)
    print('press ENTER key to release')
    input()
    # for inst in tt.t.instruments.values():
    #     print(inst)
    print('trade release')
    tt.release()
    print('quote release')
    qq.release()
