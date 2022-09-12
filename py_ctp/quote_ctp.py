#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2022/09/11


import os
import sys
import platform
import ctypes
import copy
from .struct import *


class Quote:

    def __init__(self):
        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lib64")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_quote.dll' if 'Windows' in platform.system() else 'libctp_quote.so')
        if not os.path.exists(absolute_dllfile_path):
            print('缺少DLL接口文件')
            return

        # make log dir for api log
        logdir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(logdir):
            os.mkdir(logdir)
 
        dlldir = os.path.split(absolute_dllfile_path)[0]
        # change work directory
        cur_path = os.getcwd()
        os.chdir(dlldir)

        self.h = CDLL(absolute_dllfile_path)

        self.h.qCreateApi.argtypes = []
        self.h.qCreateApi.restype = c_void_p

        self.h.qCreateSpi.argtypes = []
        self.h.qCreateSpi.restype = c_void_p

        self.api = None
        self.spi = None

        #################### 请求函数 #######################
        # 创建MdApi
        self.h.qRelease.argtypes = [c_void_p]
        self.h.qRelease.restype = c_void_p
        # 初始化
        self.h.qInit.argtypes = [c_void_p]
        self.h.qInit.restype = c_void_p
        # 等待接口线程结束运行
        self.h.qJoin.argtypes = [c_void_p]
        self.h.qJoin.restype = c_void_p
        # 注册前置机网络地址
        self.h.qRegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterFront.restype = c_void_p
        # @remark RegisterNameServer优先于RegisterFront
        self.h.qRegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterNameServer.restype = c_void_p
        # 注册名字服务器用户信息
        self.h.qRegisterFensUserInfo.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterFensUserInfo.restype = c_void_p
        # 注册回调接口
        self.h.qRegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterSpi.restype = c_void_p
        # 订阅行情。
        self.h.qSubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qSubscribeMarketData.restype = c_void_p
        # 退订行情。
        self.h.qUnSubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qUnSubscribeMarketData.restype = c_void_p
        # 订阅询价。
        self.h.qSubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qSubscribeForQuoteRsp.restype = c_void_p
        # 退订询价。
        self.h.qUnSubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qUnSubscribeForQuoteRsp.restype = c_void_p
        # 用户登录请求
        self.h.qReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqUserLogin.restype = c_void_p
        # 登出请求
        self.h.qReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqUserLogout.restype = c_void_p
        # 请求查询组播合约
        self.h.qReqQryMulticastInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqQryMulticastInstrument.restype = c_void_p
        
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.qCreateApi()
        return self.api

    def CreateSpi(self):
        self.spi = self.h.qCreateSpi()
        #################### 响应函数 #########################
        # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        self.h.qSetOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnFrontConnected.restype = None
        self.evOnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.qSetOnFrontConnected(self.spi, self.evOnFrontConnected)
        # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        self.h.qSetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnFrontDisconnected.restype = None
        self.evOnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.qSetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)
        # 心跳超时警告。当长时间未收到报文时，该方法被调用。
        self.h.qSetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnHeartBeatWarning.restype = None
        self.evOnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.qSetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)
        # 登录请求响应
        self.h.qSetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspUserLogin.restype = None
        self.evOnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.qSetOnRspUserLogin(self.spi, self.evOnRspUserLogin)
        # 登出请求响应
        self.h.qSetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspUserLogout.restype = None
        self.evOnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.qSetOnRspUserLogout(self.spi, self.evOnRspUserLogout)
        # 请求查询组播合约响应
        self.h.qSetOnRspQryMulticastInstrument.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspQryMulticastInstrument.restype = None
        self.evOnRspQryMulticastInstrument = CFUNCTYPE(None, POINTER(CThostFtdcMulticastInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMulticastInstrument)
        self.h.qSetOnRspQryMulticastInstrument(self.spi, self.evOnRspQryMulticastInstrument)
        # 错误应答
        self.h.qSetOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspError.restype = None
        self.evOnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.qSetOnRspError(self.spi, self.evOnRspError)
        # 订阅行情应答
        self.h.qSetOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspSubMarketData.restype = None
        self.evOnRspSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
        self.h.qSetOnRspSubMarketData(self.spi, self.evOnRspSubMarketData)
        # 取消订阅行情应答
        self.h.qSetOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspUnSubMarketData.restype = None
        self.evOnRspUnSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
        self.h.qSetOnRspUnSubMarketData(self.spi, self.evOnRspUnSubMarketData)
        # 订阅询价应答
        self.h.qSetOnRspSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspSubForQuoteRsp.restype = None
        self.evOnRspSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubForQuoteRsp)
        self.h.qSetOnRspSubForQuoteRsp(self.spi, self.evOnRspSubForQuoteRsp)
        # 取消订阅询价应答
        self.h.qSetOnRspUnSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRspUnSubForQuoteRsp.restype = None
        self.evOnRspUnSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubForQuoteRsp)
        self.h.qSetOnRspUnSubForQuoteRsp(self.spi, self.evOnRspUnSubForQuoteRsp)
        # 深度行情通知
        self.h.qSetOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRtnDepthMarketData.restype = None
        self.evOnRtnDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
        self.h.qSetOnRtnDepthMarketData(self.spi, self.evOnRtnDepthMarketData)
        # 询价通知
        self.h.qSetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qSetOnRtnForQuoteRsp.restype = None
        self.evOnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.qSetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)
        
        return self.spi

    #################### 请求函数 #######################
    
    def Release(self):
        """ 创建MdApi """
        self.h.qRelease(self.api)
    
    def Init(self):
        """ 初始化 """
        self.h.qInit(self.api)
    
    def Join(self):
        """ 等待接口线程结束运行 """
        self.h.qJoin(self.api)
    
    def RegisterFront(self, pszFrontAddress:str):
        """ 注册前置机网络地址 """
        self.h.qRegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))
    
    def RegisterNameServer(self, pszNsAddress:str):
        """ @remark RegisterNameServer优先于RegisterFront """
        self.h.qRegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))
    
    def RegisterFensUserInfo(self,  pFensUserInfo:CThostFtdcFensUserInfoField):
        """ 注册名字服务器用户信息 """
        self.h.qRegisterFensUserInfo(self.api, byref( pFensUserInfo))
    
    def RegisterSpi(self, pSpi:c_void_p):
        """ 注册回调接口 """
        self.h.qRegisterSpi(self.api, pSpi)
    
    def SubscribeMarketData(self, ppInstrumentID:str, nCount:int):
        """ 订阅行情。 """
        self.h.qSubscribeMarketData(self.api, ppInstrumentID, nCount)
    
    def UnSubscribeMarketData(self, ppInstrumentID:str, nCount:int):
        """ 退订行情。 """
        self.h.qUnSubscribeMarketData(self.api, ppInstrumentID, nCount)
    
    def SubscribeForQuoteRsp(self, ppInstrumentID:str, nCount:int):
        """ 订阅询价。 """
        self.h.qSubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)
    
    def UnSubscribeForQuoteRsp(self, ppInstrumentID:str, nCount:int):
        """ 退订询价。 """
        self.h.qUnSubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)
    
    def ReqUserLogin(self, pReqUserLoginField:CThostFtdcReqUserLoginField, nRequestID:int):
        """ 用户登录请求 """
        self.h.qReqUserLogin(self.api, byref(pReqUserLoginField), nRequestID)
    
    def ReqUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, nRequestID:int):
        """ 登出请求 """
        self.h.qReqUserLogout(self.api, byref(pUserLogout), nRequestID)
    
    def ReqQryMulticastInstrument(self, pQryMulticastInstrument:CThostFtdcQryMulticastInstrumentField, nRequestID:int):
        """ 请求查询组播合约 """
        self.h.qReqQryMulticastInstrument(self.api, byref(pQryMulticastInstrument), nRequestID)
    
    #################### 响应函数 #########################
    
    def __OnFrontConnected(self):
        self.OnFrontConnected()
    def OnFrontConnected(self):
        """ 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。 """
        print('===OnFrontConnected===:')
    
    def __OnFrontDisconnected(self, nReason:int):
        self.OnFrontDisconnected(nReason)
    def OnFrontDisconnected(self, nReason:int):
        """ 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。 """
        print('===OnFrontDisconnected===:nReason:int')
    
    def __OnHeartBeatWarning(self, nTimeLapse:int):
        self.OnHeartBeatWarning(nTimeLapse)
    def OnHeartBeatWarning(self, nTimeLapse:int):
        """ 心跳超时警告。当长时间未收到报文时，该方法被调用。 """
        print('===OnHeartBeatWarning===:nTimeLapse:int')
    
    def __OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents) if pRspUserLogin else CThostFtdcRspUserLoginField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登录请求响应 """
        print('===OnRspUserLogin===:pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents) if pUserLogout else CThostFtdcUserLogoutField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登出请求响应 """
        print('===OnRspUserLogout===:pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMulticastInstrument(self, pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMulticastInstrument(copy.deepcopy(POINTER(CThostFtdcMulticastInstrumentField).from_param(pMulticastInstrument).contents) if pMulticastInstrument else CThostFtdcMulticastInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMulticastInstrument(self, pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询组播合约响应 """
        print('===OnRspQryMulticastInstrument===:pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 错误应答 """
        print('===OnRspError===:pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 订阅行情应答 """
        print('===OnRspSubMarketData===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUnSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUnSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUnSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 取消订阅行情应答 """
        print('===OnRspUnSubMarketData===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 订阅询价应答 """
        print('===OnRspSubForQuoteRsp===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUnSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUnSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 取消订阅询价应答 """
        print('===OnRspUnSubForQuoteRsp===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField):
        self.OnRtnDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents) if pDepthMarketData else CThostFtdcDepthMarketDataField())
    def OnRtnDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField):
        """ 深度行情通知 """
        print('===OnRtnDepthMarketData===:pDepthMarketData:CThostFtdcDepthMarketDataField')
    
    def __OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents) if pForQuoteRsp else CThostFtdcForQuoteRspField())
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        """ 询价通知 """
        print('===OnRtnForQuoteRsp===:pForQuoteRsp:CThostFtdcForQuoteRspField')
    