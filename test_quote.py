#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'test py ctp of se'
__author__ = 'HaiFeng'
__mtime__ = '2022/09/11'

from py_ctp.quote import CtpQuote
from py_ctp.enums import *

def onLogin(obj, info):
    print(info)
    obj.ReqSubscribeMarketData(["rb2210","rb2301"])

def main():
    q = CtpQuote()
    q.OnConnected = lambda obj: q.ReqUserLogin("008105", "1", "9999")
    q.OnUserLogin = onLogin
    q.OnTick = lambda obj, t : print(t)
    q.ReqConnect('tcp://180.168.146.187:10131')

    input()
    q.Release()
    input()


if __name__ == '__main__':
    main()