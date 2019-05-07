# py_ctp

上期技术期货交易api之python封装，实现接口调用。支持windows(x86/x64) linux(x64).

#### 示例

```python
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
    def __init__(self, addr: str, broker: str, investor: str, pwd: str, appid: str, auth_code: str, proc: str):
        self.front = addr
        self.broker = broker
        self.investor = investor
        self.pwd = pwd
        self.appid = appid
        self.authcode = auth_code
        self.proc = proc

        self.t = CtpTrade()
        self.t.OnConnected = self.on_connect
        self.t.OnUserLogin = lambda o, x: print('Trade logon:', x)
        self.t.OnDisConnected = lambda o, x: print(x)
        self.t.OnRtnNotice = lambda obj, time, msg: print(f'OnNotice: {time}:{msg}')
        self.t.OnErrRtnQuote = lambda obj, quote, info: None
        self.t.OnErrRtnQuoteInsert = lambda obj, o: None
        self.t.OnOrder = lambda obj, o: None
        self.t.OnErrOrder = lambda obj, f, info: None
        self.t.OnTrade = lambda obj, o: None
        self.t.OnInstrumentStatus = lambda obj, inst, stat: None

    def on_connect(self, obj):
        self.t.ReqUserLogin(self.investor, self.pwd, self.broker, self.proc, self.appid, self.authcode)

    def run(self):
        self.t.ReqConnect(self.front)
        # self.t.ReqConnect('tcp://192.168.52.4:41205')

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
        self.q.OnConnected = lambda x: self.q.ReqUserLogin(self.investor, self.pwd, self.broker)
        self.q.OnUserLogin = lambda o, i: self.q.ReqSubscribeMarketData('rb1910')

    def run(self):
        self.q.ReqConnect(self.front)

    def release(self):
        self.q.ReqUserLogout()


if __name__ == "__main__":
    front_trade = 'tcp://180.168.146.187:13030'
    front_quote = 'tcp://180.168.146.187:13040'
    broker = '9999'
    investor = ''
    pwd = ''
    appid = ''
    auth_code = ''
    proc = ''
    if investor == '':
        investor = input('invesotr:')
        pwd = input('password:')
        appid = input('appid:')
        auth_code = input('auth code:')
        proc = input('product info:')
    tt = TestTrade(front_trade, broker, investor, pwd, appid, auth_code, proc)
    tt.run()
    time.sleep(5)
    # tt.t.ReqOrderInsert('j1905', DirectType.Buy, OffsetType.Open, 2060, 3)

    time.sleep(3)
    qq = TestQuote(front_quote, broker, investor, pwd)
    qq.run()

    # time.sleep(6)
    # for inst in tt.t.instruments.values():
    #     print(inst)
    input()
    tt.release()
    qq.release()
    input()

```