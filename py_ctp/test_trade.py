#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = ''

from py_ctp.trade import CtpTrade
import time


class TestTrade(object):
    def __init__(self):
        self.t = CtpTrade()
        self.t.OnConnected = self.connected
        self.t.OnUserLogin = self.logined
        self.t.OnDisConnected = self.disconnected

    def run(self):
        self.t.ReqConnect('tcp://180.168.146.187:10000')
        # self.t.ReqConnect('tcp://192.168.52.4:41205')

    def release(self):
        self.t.ReqUserLogout()

    def connected(self, obj):
        print('connected')
        self.t.ReqUserLogin('008105', '1', '9999')
        # if not self.t.logged:
        #     self.t.ReqUserLogin('111', 'jykf1234', '6000')

    def logined(self, obj, info):
        print(info)
        print(self.t.account.__dict__)
        # self.t.ReqOrderInsert('rb1810', DirectType.Buy, OffsetType.Open, 4100.0, 1)

    def disconnected(self, obj, reason):
        print('disconnected:' + str(reason))


tt = TestTrade()
# t.OnConnected = t.ReqUserLogin('008105', '1', '9999')
# t.ReqConnect('tcp://180.168.146.187:10000')
tt.run()

time.sleep(6)
for inst in tt.t.instruments.values():
    print(inst)
input()
tt.release()
