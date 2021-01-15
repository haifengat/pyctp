#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/10


import os
import sys
import platform
import ctypes
import copy
from .ctp_struct import *


class Quote:

    def __init__(self):

        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"lib{'64' if sys.maxsize > 2**32 else '32'}")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_quote.' + ('dll' if 'Windows' in platform.system() else 'so'))
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

        self.h.CreateApi.argtypes = []
        self.h.CreateApi.restype = c_void_p

        self.h.CreateSpi.argtypes = []
        self.h.CreateSpi.restype = c_void_p

        self.api = None
        self.spi = None
        self.nRequestID = 0
        self.h.Release.argtypes = [c_void_p]
        self.h.Release.restype = c_void_p

        self.h.Init.argtypes = [c_void_p]
        self.h.Init.restype = c_void_p

        self.h.Join.argtypes = [c_void_p]
        self.h.Join.restype = c_void_p

        self.h.RegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.RegisterFront.restype = c_void_p

        self.h.RegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.RegisterNameServer.restype = c_void_p

        self.h.RegisterFensUserInfo.argtypes = [c_void_p, c_void_p]
        self.h.RegisterFensUserInfo.restype = c_void_p

        self.h.RegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.RegisterSpi.restype = c_void_p

        self.h.SubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.SubscribeMarketData.restype = c_void_p

        self.h.UnSubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.UnSubscribeMarketData.restype = c_void_p

        self.h.SubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.SubscribeForQuoteRsp.restype = c_void_p

        self.h.UnSubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.UnSubscribeForQuoteRsp.restype = c_void_p

        self.h.ReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogin.restype = c_void_p

        self.h.ReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogout.restype = c_void_p

        self.h.ReqQryMulticastInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryMulticastInstrument.restype = c_void_p
        os.chdir(cur_path)


    def CreateApi(self):
        self.api = self.h.CreateApi()
        return self.api
        
    def CreateSpi(self):
        self.spi = self.h.CreateSpi()
        return self.spi


    def Release(self):
        self.h.Release(self.api)

    def Init(self):
        self.h.Init(self.api)

    def Join(self):
        self.h.Join(self.api)

    def RegisterFront(self, pszFrontAddress: str):
        self.h.RegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))

    def RegisterNameServer(self, pszNsAddress: str):
        self.h.RegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))

    def RegisterFensUserInfo(self, BrokerID: str = '', UserID: str = '', LoginMode: TThostFtdcLoginModeType = list(TThostFtdcLoginModeType)[0]):
        pFensUserInfo = CThostFtdcFensUserInfoField()
        pFensUserInfo.BrokerID = bytes(BrokerID, encoding='ascii')
        pFensUserInfo.UserID = bytes(UserID, encoding='ascii')
        pFensUserInfo.LoginMode = LoginMode.value
        self.h.RegisterFensUserInfo(self.api, byref(pFensUserInfo))

    def RegisterSpi(self, pSpi):
        self.h.RegisterSpi(self.api, pSpi)

    def SubscribeMarketData(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.SubscribeMarketData(self.api, ca1, nCount)

    def UnSubscribeMarketData(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.UnSubscribeMarketData(self.api, ca1, nCount)

    def SubscribeForQuoteRsp(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.SubscribeForQuoteRsp(self.api, ca1, nCount)

    def UnSubscribeForQuoteRsp(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.UnSubscribeForQuoteRsp(self.api, ca1, nCount)

    def ReqUserLogin(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '', MacAddress: str = '', OneTimePassword: str = '', reserve1: str = '', LoginRemark: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        pReqUserLoginField = CThostFtdcReqUserLoginField()
        pReqUserLoginField.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserLoginField.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLoginField.UserID = bytes(UserID, encoding='ascii')
        pReqUserLoginField.Password = bytes(Password, encoding='ascii')
        pReqUserLoginField.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqUserLoginField.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
        pReqUserLoginField.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
        pReqUserLoginField.MacAddress = bytes(MacAddress, encoding='ascii')
        pReqUserLoginField.OneTimePassword = bytes(OneTimePassword, encoding='ascii')
        pReqUserLoginField.reserve1 = bytes(reserve1, encoding='ascii')
        pReqUserLoginField.LoginRemark = bytes(LoginRemark, encoding='ascii')
        pReqUserLoginField.ClientIPPort = ClientIPPort
        pReqUserLoginField.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLogin(self.api, byref(pReqUserLoginField), self.nRequestID)

    def ReqUserLogout(self, BrokerID: str = '', UserID: str = ''):
        pUserLogout = CThostFtdcUserLogoutField()
        pUserLogout.BrokerID = bytes(BrokerID, encoding='ascii')
        pUserLogout.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLogout(self.api, byref(pUserLogout), self.nRequestID)

    def ReqQryMulticastInstrument(self, TopicID: int = 0, reserve1: str = '', InstrumentID: str = ''):
        pQryMulticastInstrument = CThostFtdcQryMulticastInstrumentField()
        pQryMulticastInstrument.TopicID = TopicID
        pQryMulticastInstrument.reserve1 = bytes(reserve1, encoding='ascii')
        pQryMulticastInstrument.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryMulticastInstrument(self.api, byref(pQryMulticastInstrument), self.nRequestID)

    def RegCB(self):
        self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontConnected.restype = None
        self.evOnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

        self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontDisconnected.restype = None
        self.evOnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

        self.h.SetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.SetOnHeartBeatWarning.restype = None
        self.evOnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.SetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)

        self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogin.restype = None
        self.evOnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

        self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogout.restype = None
        self.evOnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

        self.h.SetOnRspQryMulticastInstrument.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryMulticastInstrument.restype = None
        self.evOnRspQryMulticastInstrument = CFUNCTYPE(None, POINTER(CThostFtdcMulticastInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMulticastInstrument)
        self.h.SetOnRspQryMulticastInstrument(self.spi, self.evOnRspQryMulticastInstrument)

        self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspError.restype = None
        self.evOnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.SetOnRspError(self.spi, self.evOnRspError)

        self.h.SetOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspSubMarketData.restype = None
        self.evOnRspSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
        self.h.SetOnRspSubMarketData(self.spi, self.evOnRspSubMarketData)

        self.h.SetOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUnSubMarketData.restype = None
        self.evOnRspUnSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
        self.h.SetOnRspUnSubMarketData(self.spi, self.evOnRspUnSubMarketData)

        self.h.SetOnRspSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspSubForQuoteRsp.restype = None
        self.evOnRspSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubForQuoteRsp)
        self.h.SetOnRspSubForQuoteRsp(self.spi, self.evOnRspSubForQuoteRsp)

        self.h.SetOnRspUnSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUnSubForQuoteRsp.restype = None
        self.evOnRspUnSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubForQuoteRsp)
        self.h.SetOnRspUnSubForQuoteRsp(self.spi, self.evOnRspUnSubForQuoteRsp)

        self.h.SetOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnDepthMarketData.restype = None
        self.evOnRtnDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
        self.h.SetOnRtnDepthMarketData(self.spi, self.evOnRtnDepthMarketData)

        self.h.SetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnForQuoteRsp.restype = None
        self.evOnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.SetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)

    def __OnFrontConnected(self):
        self.OnFrontConnected()

    def __OnFrontDisconnected(self, nReason):
        self.OnFrontDisconnected(nReason)

    def __OnHeartBeatWarning(self, nTimeLapse):
        self.OnHeartBeatWarning(nTimeLapse)

    def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryMulticastInstrument(self, pMulticastInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryMulticastInstrument(copy.deepcopy(POINTER(CThostFtdcMulticastInstrumentField).from_param(pMulticastInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspUnSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspUnSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnDepthMarketData(self, pDepthMarketData):
        self.OnRtnDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents))

    def __OnRtnForQuoteRsp(self, pForQuoteRsp):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents))

    def OnFrontConnected(self, ):
        print('===OnFrontConnected===: ')

    def OnFrontDisconnected(self, nReason: int):
        print('===OnFrontDisconnected===: nReason: int')

    def OnHeartBeatWarning(self, nTimeLapse: int):
        print('===OnHeartBeatWarning===: nTimeLapse: int')

    def OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogin===: pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserLogout(self, pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogout===: pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryMulticastInstrument(self, pMulticastInstrument: CThostFtdcMulticastInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryMulticastInstrument===: pMulticastInstrument: CThostFtdcMulticastInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspError(self, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspError===: pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspSubMarketData(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspSubMarketData===: pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUnSubMarketData(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUnSubMarketData===: pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspSubForQuoteRsp(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspSubForQuoteRsp===: pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUnSubForQuoteRsp===: pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField):
        print('===OnRtnDepthMarketData===: pDepthMarketData: CThostFtdcDepthMarketDataField')

    def OnRtnForQuoteRsp(self, pForQuoteRsp: CThostFtdcForQuoteRspField):
        print('===OnRtnForQuoteRsp===: pForQuoteRsp: CThostFtdcForQuoteRspField')