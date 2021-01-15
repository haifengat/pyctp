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


class Trade:

    def __init__(self):

        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"lib{'64' if sys.maxsize > 2**32 else '32'}")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_trade.' + ('dll' if 'Windows' in platform.system() else 'so'))
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
        self.h.GetVersion.argtypes = []
        self.h.GetVersion.restype = c_char_p
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

        self.h.SubscribePrivateTopic.argtypes = [c_void_p, c_void_p]
        self.h.SubscribePrivateTopic.restype = c_void_p

        self.h.SubscribePublicTopic.argtypes = [c_void_p, c_void_p]
        self.h.SubscribePublicTopic.restype = c_void_p

        self.h.ReqAuthenticate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqAuthenticate.restype = c_void_p

        self.h.RegisterUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.RegisterUserSystemInfo.restype = c_void_p

        self.h.SubmitUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.SubmitUserSystemInfo.restype = c_void_p

        self.h.ReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogin.restype = c_void_p

        self.h.ReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogout.restype = c_void_p

        self.h.ReqUserPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserPasswordUpdate.restype = c_void_p

        self.h.ReqTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqTradingAccountPasswordUpdate.restype = c_void_p

        self.h.ReqUserAuthMethod.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserAuthMethod.restype = c_void_p

        self.h.ReqGenUserCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqGenUserCaptcha.restype = c_void_p

        self.h.ReqGenUserText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqGenUserText.restype = c_void_p

        self.h.ReqUserLoginWithCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLoginWithCaptcha.restype = c_void_p

        self.h.ReqUserLoginWithText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLoginWithText.restype = c_void_p

        self.h.ReqUserLoginWithOTP.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLoginWithOTP.restype = c_void_p

        self.h.ReqOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOrderInsert.restype = c_void_p

        self.h.ReqParkedOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqParkedOrderInsert.restype = c_void_p

        self.h.ReqParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqParkedOrderAction.restype = c_void_p

        self.h.ReqOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOrderAction.restype = c_void_p

        self.h.ReqQryMaxOrderVolume.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryMaxOrderVolume.restype = c_void_p

        self.h.ReqSettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqSettlementInfoConfirm.restype = c_void_p

        self.h.ReqRemoveParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqRemoveParkedOrder.restype = c_void_p

        self.h.ReqRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqRemoveParkedOrderAction.restype = c_void_p

        self.h.ReqExecOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqExecOrderInsert.restype = c_void_p

        self.h.ReqExecOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqExecOrderAction.restype = c_void_p

        self.h.ReqForQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqForQuoteInsert.restype = c_void_p

        self.h.ReqQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQuoteInsert.restype = c_void_p

        self.h.ReqQuoteAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQuoteAction.restype = c_void_p

        self.h.ReqBatchOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqBatchOrderAction.restype = c_void_p

        self.h.ReqOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOptionSelfCloseInsert.restype = c_void_p

        self.h.ReqOptionSelfCloseAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOptionSelfCloseAction.restype = c_void_p

        self.h.ReqCombActionInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqCombActionInsert.restype = c_void_p

        self.h.ReqQryOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryOrder.restype = c_void_p

        self.h.ReqQryTrade.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTrade.restype = c_void_p

        self.h.ReqQryInvestorPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorPosition.restype = c_void_p

        self.h.ReqQryTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTradingAccount.restype = c_void_p

        self.h.ReqQryInvestor.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestor.restype = c_void_p

        self.h.ReqQryTradingCode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTradingCode.restype = c_void_p

        self.h.ReqQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrumentMarginRate.restype = c_void_p

        self.h.ReqQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrumentCommissionRate.restype = c_void_p

        self.h.ReqQryExchange.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExchange.restype = c_void_p

        self.h.ReqQryProduct.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryProduct.restype = c_void_p

        self.h.ReqQryInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrument.restype = c_void_p

        self.h.ReqQryDepthMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryDepthMarketData.restype = c_void_p

        self.h.ReqQrySettlementInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySettlementInfo.restype = c_void_p

        self.h.ReqQryTransferBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTransferBank.restype = c_void_p

        self.h.ReqQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorPositionDetail.restype = c_void_p

        self.h.ReqQryNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryNotice.restype = c_void_p

        self.h.ReqQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySettlementInfoConfirm.restype = c_void_p

        self.h.ReqQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorPositionCombineDetail.restype = c_void_p

        self.h.ReqQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryCFMMCTradingAccountKey.restype = c_void_p

        self.h.ReqQryEWarrantOffset.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryEWarrantOffset.restype = c_void_p

        self.h.ReqQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorProductGroupMargin.restype = c_void_p

        self.h.ReqQryExchangeMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExchangeMarginRate.restype = c_void_p

        self.h.ReqQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExchangeMarginRateAdjust.restype = c_void_p

        self.h.ReqQryExchangeRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExchangeRate.restype = c_void_p

        self.h.ReqQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySecAgentACIDMap.restype = c_void_p

        self.h.ReqQryProductExchRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryProductExchRate.restype = c_void_p

        self.h.ReqQryProductGroup.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryProductGroup.restype = c_void_p

        self.h.ReqQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryMMInstrumentCommissionRate.restype = c_void_p

        self.h.ReqQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryMMOptionInstrCommRate.restype = c_void_p

        self.h.ReqQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrumentOrderCommRate.restype = c_void_p

        self.h.ReqQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySecAgentTradingAccount.restype = c_void_p

        self.h.ReqQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySecAgentCheckMode.restype = c_void_p

        self.h.ReqQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySecAgentTradeInfo.restype = c_void_p

        self.h.ReqQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryOptionInstrTradeCost.restype = c_void_p

        self.h.ReqQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryOptionInstrCommRate.restype = c_void_p

        self.h.ReqQryExecOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExecOrder.restype = c_void_p

        self.h.ReqQryForQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryForQuote.restype = c_void_p

        self.h.ReqQryQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryQuote.restype = c_void_p

        self.h.ReqQryOptionSelfClose.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryOptionSelfClose.restype = c_void_p

        self.h.ReqQryInvestUnit.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestUnit.restype = c_void_p

        self.h.ReqQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryCombInstrumentGuard.restype = c_void_p

        self.h.ReqQryCombAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryCombAction.restype = c_void_p

        self.h.ReqQryTransferSerial.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTransferSerial.restype = c_void_p

        self.h.ReqQryAccountregister.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryAccountregister.restype = c_void_p

        self.h.ReqQryContractBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryContractBank.restype = c_void_p

        self.h.ReqQryParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryParkedOrder.restype = c_void_p

        self.h.ReqQryParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryParkedOrderAction.restype = c_void_p

        self.h.ReqQryTradingNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTradingNotice.restype = c_void_p

        self.h.ReqQryBrokerTradingParams.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryBrokerTradingParams.restype = c_void_p

        self.h.ReqQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryBrokerTradingAlgos.restype = c_void_p

        self.h.ReqQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQueryCFMMCTradingAccountToken.restype = c_void_p

        self.h.ReqFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqFromBankToFutureByFuture.restype = c_void_p

        self.h.ReqFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqFromFutureToBankByFuture.restype = c_void_p

        self.h.ReqQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQueryBankAccountMoneyByFuture.restype = c_void_p

        self.h.ReqQryClassifiedInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryClassifiedInstrument.restype = c_void_p

        self.h.ReqQryCombPromotionParam.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryCombPromotionParam.restype = c_void_p
        os.chdir(cur_path)


    def CreateApi(self):
        self.api = self.h.CreateApi()
        return self.api
        
    def CreateSpi(self):
        self.spi = self.h.CreateSpi()
        return self.spi


    def GetVersion(self):
        v = str(self.h.GetVersion(), encoding='ascii')
        return str(v)


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

    def SubscribePrivateTopic(self, nResumeType: THOST_TE_RESUME_TYPE = 1):
        self.h.SubscribePrivateTopic(self.api, nResumeType)

    def SubscribePublicTopic(self, nResumeType: THOST_TE_RESUME_TYPE = 1):
        self.h.SubscribePublicTopic(self.api, nResumeType)

    def ReqAuthenticate(self, BrokerID: str = '', UserID: str = '', UserProductInfo: str = '', AuthCode: str = '', AppID: str = ''):
        pReqAuthenticateField = CThostFtdcReqAuthenticateField()
        pReqAuthenticateField.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqAuthenticateField.UserID = bytes(UserID, encoding='ascii')
        pReqAuthenticateField.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqAuthenticateField.AuthCode = bytes(AuthCode, encoding='ascii')
        pReqAuthenticateField.AppID = bytes(AppID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqAuthenticate(self.api, byref(pReqAuthenticateField), self.nRequestID)

    def RegisterUserSystemInfo(self, BrokerID: str = '', UserID: str = '', ClientSystemInfoLen: int = 0, ClientSystemInfo: str = '', reserve1: str = '', ClientIPPort: int = 0, ClientLoginTime: str = '', ClientAppID: str = '', ClientPublicIP: str = ''):
        pUserSystemInfo = CThostFtdcUserSystemInfoField()
        pUserSystemInfo.BrokerID = bytes(BrokerID, encoding='ascii')
        pUserSystemInfo.UserID = bytes(UserID, encoding='ascii')
        pUserSystemInfo.ClientSystemInfoLen = ClientSystemInfoLen
        pUserSystemInfo.ClientSystemInfo = bytes(ClientSystemInfo, encoding='ascii')
        pUserSystemInfo.reserve1 = bytes(reserve1, encoding='ascii')
        pUserSystemInfo.ClientIPPort = ClientIPPort
        pUserSystemInfo.ClientLoginTime = bytes(ClientLoginTime, encoding='ascii')
        pUserSystemInfo.ClientAppID = bytes(ClientAppID, encoding='ascii')
        pUserSystemInfo.ClientPublicIP = bytes(ClientPublicIP, encoding='ascii')
        self.h.RegisterUserSystemInfo(self.api, byref(pUserSystemInfo))

    def SubmitUserSystemInfo(self, BrokerID: str = '', UserID: str = '', ClientSystemInfoLen: int = 0, ClientSystemInfo: str = '', reserve1: str = '', ClientIPPort: int = 0, ClientLoginTime: str = '', ClientAppID: str = '', ClientPublicIP: str = ''):
        pUserSystemInfo = CThostFtdcUserSystemInfoField()
        pUserSystemInfo.BrokerID = bytes(BrokerID, encoding='ascii')
        pUserSystemInfo.UserID = bytes(UserID, encoding='ascii')
        pUserSystemInfo.ClientSystemInfoLen = ClientSystemInfoLen
        pUserSystemInfo.ClientSystemInfo = bytes(ClientSystemInfo, encoding='ascii')
        pUserSystemInfo.reserve1 = bytes(reserve1, encoding='ascii')
        pUserSystemInfo.ClientIPPort = ClientIPPort
        pUserSystemInfo.ClientLoginTime = bytes(ClientLoginTime, encoding='ascii')
        pUserSystemInfo.ClientAppID = bytes(ClientAppID, encoding='ascii')
        pUserSystemInfo.ClientPublicIP = bytes(ClientPublicIP, encoding='ascii')
        self.h.SubmitUserSystemInfo(self.api, byref(pUserSystemInfo))

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

    def ReqUserPasswordUpdate(self, BrokerID: str = '', UserID: str = '', OldPassword: str = '', NewPassword: str = ''):
        pUserPasswordUpdate = CThostFtdcUserPasswordUpdateField()
        pUserPasswordUpdate.BrokerID = bytes(BrokerID, encoding='ascii')
        pUserPasswordUpdate.UserID = bytes(UserID, encoding='ascii')
        pUserPasswordUpdate.OldPassword = bytes(OldPassword, encoding='ascii')
        pUserPasswordUpdate.NewPassword = bytes(NewPassword, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserPasswordUpdate(self.api, byref(pUserPasswordUpdate), self.nRequestID)

    def ReqTradingAccountPasswordUpdate(self, BrokerID: str = '', AccountID: str = '', OldPassword: str = '', NewPassword: str = '', CurrencyID: str = ''):
        pTradingAccountPasswordUpdate = CThostFtdcTradingAccountPasswordUpdateField()
        pTradingAccountPasswordUpdate.BrokerID = bytes(BrokerID, encoding='ascii')
        pTradingAccountPasswordUpdate.AccountID = bytes(AccountID, encoding='ascii')
        pTradingAccountPasswordUpdate.OldPassword = bytes(OldPassword, encoding='ascii')
        pTradingAccountPasswordUpdate.NewPassword = bytes(NewPassword, encoding='ascii')
        pTradingAccountPasswordUpdate.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqTradingAccountPasswordUpdate(self.api, byref(pTradingAccountPasswordUpdate), self.nRequestID)

    def ReqUserAuthMethod(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        pReqUserAuthMethod = CThostFtdcReqUserAuthMethodField()
        pReqUserAuthMethod.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserAuthMethod.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserAuthMethod.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserAuthMethod(self.api, byref(pReqUserAuthMethod), self.nRequestID)

    def ReqGenUserCaptcha(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        pReqGenUserCaptcha = CThostFtdcReqGenUserCaptchaField()
        pReqGenUserCaptcha.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqGenUserCaptcha.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqGenUserCaptcha.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqGenUserCaptcha(self.api, byref(pReqGenUserCaptcha), self.nRequestID)

    def ReqGenUserText(self, TradingDay: str = '', BrokerID: str = '', UserID: str = ''):
        pReqGenUserText = CThostFtdcReqGenUserTextField()
        pReqGenUserText.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqGenUserText.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqGenUserText.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqGenUserText(self.api, byref(pReqGenUserText), self.nRequestID)

    def ReqUserLoginWithCaptcha(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '', MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', Captcha: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        pReqUserLoginWithCaptcha = CThostFtdcReqUserLoginWithCaptchaField()
        pReqUserLoginWithCaptcha.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserLoginWithCaptcha.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLoginWithCaptcha.UserID = bytes(UserID, encoding='ascii')
        pReqUserLoginWithCaptcha.Password = bytes(Password, encoding='ascii')
        pReqUserLoginWithCaptcha.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqUserLoginWithCaptcha.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
        pReqUserLoginWithCaptcha.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
        pReqUserLoginWithCaptcha.MacAddress = bytes(MacAddress, encoding='ascii')
        pReqUserLoginWithCaptcha.reserve1 = bytes(reserve1, encoding='ascii')
        pReqUserLoginWithCaptcha.LoginRemark = bytes(LoginRemark, encoding='ascii')
        pReqUserLoginWithCaptcha.Captcha = bytes(Captcha, encoding='ascii')
        pReqUserLoginWithCaptcha.ClientIPPort = ClientIPPort
        pReqUserLoginWithCaptcha.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLoginWithCaptcha(self.api, byref(pReqUserLoginWithCaptcha), self.nRequestID)

    def ReqUserLoginWithText(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '', MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', Text: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        pReqUserLoginWithText = CThostFtdcReqUserLoginWithTextField()
        pReqUserLoginWithText.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserLoginWithText.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLoginWithText.UserID = bytes(UserID, encoding='ascii')
        pReqUserLoginWithText.Password = bytes(Password, encoding='ascii')
        pReqUserLoginWithText.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqUserLoginWithText.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
        pReqUserLoginWithText.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
        pReqUserLoginWithText.MacAddress = bytes(MacAddress, encoding='ascii')
        pReqUserLoginWithText.reserve1 = bytes(reserve1, encoding='ascii')
        pReqUserLoginWithText.LoginRemark = bytes(LoginRemark, encoding='ascii')
        pReqUserLoginWithText.Text = bytes(Text, encoding='ascii')
        pReqUserLoginWithText.ClientIPPort = ClientIPPort
        pReqUserLoginWithText.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLoginWithText(self.api, byref(pReqUserLoginWithText), self.nRequestID)

    def ReqUserLoginWithOTP(self, TradingDay: str = '', BrokerID: str = '', UserID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '', MacAddress: str = '', reserve1: str = '', LoginRemark: str = '', OTPPassword: str = '', ClientIPPort: int = 0, ClientIPAddress: str = ''):
        pReqUserLoginWithOTP = CThostFtdcReqUserLoginWithOTPField()
        pReqUserLoginWithOTP.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserLoginWithOTP.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLoginWithOTP.UserID = bytes(UserID, encoding='ascii')
        pReqUserLoginWithOTP.Password = bytes(Password, encoding='ascii')
        pReqUserLoginWithOTP.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqUserLoginWithOTP.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
        pReqUserLoginWithOTP.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
        pReqUserLoginWithOTP.MacAddress = bytes(MacAddress, encoding='ascii')
        pReqUserLoginWithOTP.reserve1 = bytes(reserve1, encoding='ascii')
        pReqUserLoginWithOTP.LoginRemark = bytes(LoginRemark, encoding='ascii')
        pReqUserLoginWithOTP.OTPPassword = bytes(OTPPassword, encoding='ascii')
        pReqUserLoginWithOTP.ClientIPPort = ClientIPPort
        pReqUserLoginWithOTP.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLoginWithOTP(self.api, byref(pReqUserLoginWithOTP), self.nRequestID)

    def ReqOrderInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: TThostFtdcOrderPriceTypeType = list(TThostFtdcOrderPriceTypeType)[0], Direction: TThostFtdcDirectionType = list(TThostFtdcDirectionType)[0], CombOffsetFlag: str = '', CombHedgeFlag: str = '', LimitPrice: float = .0, VolumeTotalOriginal: int = 0, TimeCondition: TThostFtdcTimeConditionType = list(TThostFtdcTimeConditionType)[0], GTDDate: str = '', VolumeCondition: TThostFtdcVolumeConditionType = list(TThostFtdcVolumeConditionType)[0], MinVolume: int = 0, ContingentCondition: TThostFtdcContingentConditionType = list(TThostFtdcContingentConditionType)[0], StopPrice: float = .0, ForceCloseReason: TThostFtdcForceCloseReasonType = list(TThostFtdcForceCloseReasonType)[0], IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, UserForceClose: int = 0, IsSwapOrder: int = 0, ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputOrder = CThostFtdcInputOrderField()
        pInputOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pInputOrder.OrderRef = bytes(OrderRef, encoding='ascii')
        pInputOrder.UserID = bytes(UserID, encoding='ascii')
        pInputOrder.OrderPriceType = OrderPriceType.value
        pInputOrder.Direction = Direction.value
        pInputOrder.CombOffsetFlag = bytes(CombOffsetFlag, encoding='ascii')
        pInputOrder.CombHedgeFlag = bytes(CombHedgeFlag, encoding='ascii')
        pInputOrder.LimitPrice = LimitPrice
        pInputOrder.VolumeTotalOriginal = VolumeTotalOriginal
        pInputOrder.TimeCondition = TimeCondition.value
        pInputOrder.GTDDate = bytes(GTDDate, encoding='ascii')
        pInputOrder.VolumeCondition = VolumeCondition.value
        pInputOrder.MinVolume = MinVolume
        pInputOrder.ContingentCondition = ContingentCondition.value
        pInputOrder.StopPrice = StopPrice
        pInputOrder.ForceCloseReason = ForceCloseReason.value
        pInputOrder.IsAutoSuspend = IsAutoSuspend
        pInputOrder.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputOrder.RequestID = RequestID
        pInputOrder.UserForceClose = UserForceClose
        pInputOrder.IsSwapOrder = IsSwapOrder
        pInputOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputOrder.AccountID = bytes(AccountID, encoding='ascii')
        pInputOrder.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pInputOrder.ClientID = bytes(ClientID, encoding='ascii')
        pInputOrder.reserve2 = bytes(reserve2, encoding='ascii')
        pInputOrder.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputOrder.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOrderInsert(self.api, byref(pInputOrder), self.nRequestID)

    def ReqParkedOrderInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OrderRef: str = '', UserID: str = '', OrderPriceType: TThostFtdcOrderPriceTypeType = list(TThostFtdcOrderPriceTypeType)[0], Direction: TThostFtdcDirectionType = list(TThostFtdcDirectionType)[0], CombOffsetFlag: str = '', CombHedgeFlag: str = '', LimitPrice: float = .0, VolumeTotalOriginal: int = 0, TimeCondition: TThostFtdcTimeConditionType = list(TThostFtdcTimeConditionType)[0], GTDDate: str = '', VolumeCondition: TThostFtdcVolumeConditionType = list(TThostFtdcVolumeConditionType)[0], MinVolume: int = 0, ContingentCondition: TThostFtdcContingentConditionType = list(TThostFtdcContingentConditionType)[0], StopPrice: float = .0, ForceCloseReason: TThostFtdcForceCloseReasonType = list(TThostFtdcForceCloseReasonType)[0], IsAutoSuspend: int = 0, BusinessUnit: str = '', RequestID: int = 0, UserForceClose: int = 0, ExchangeID: str = '', ParkedOrderID: str = '', UserType: TThostFtdcUserTypeType = list(TThostFtdcUserTypeType)[0], Status: TThostFtdcParkedOrderStatusType = list(TThostFtdcParkedOrderStatusType)[0], ErrorID: int = 0, ErrorMsg: str = '', IsSwapOrder: int = 0, AccountID: str = '', CurrencyID: str = '', ClientID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pParkedOrder = CThostFtdcParkedOrderField()
        pParkedOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pParkedOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pParkedOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pParkedOrder.OrderRef = bytes(OrderRef, encoding='ascii')
        pParkedOrder.UserID = bytes(UserID, encoding='ascii')
        pParkedOrder.OrderPriceType = OrderPriceType.value
        pParkedOrder.Direction = Direction.value
        pParkedOrder.CombOffsetFlag = bytes(CombOffsetFlag, encoding='ascii')
        pParkedOrder.CombHedgeFlag = bytes(CombHedgeFlag, encoding='ascii')
        pParkedOrder.LimitPrice = LimitPrice
        pParkedOrder.VolumeTotalOriginal = VolumeTotalOriginal
        pParkedOrder.TimeCondition = TimeCondition.value
        pParkedOrder.GTDDate = bytes(GTDDate, encoding='ascii')
        pParkedOrder.VolumeCondition = VolumeCondition.value
        pParkedOrder.MinVolume = MinVolume
        pParkedOrder.ContingentCondition = ContingentCondition.value
        pParkedOrder.StopPrice = StopPrice
        pParkedOrder.ForceCloseReason = ForceCloseReason.value
        pParkedOrder.IsAutoSuspend = IsAutoSuspend
        pParkedOrder.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pParkedOrder.RequestID = RequestID
        pParkedOrder.UserForceClose = UserForceClose
        pParkedOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pParkedOrder.ParkedOrderID = bytes(ParkedOrderID, encoding='ascii')
        pParkedOrder.UserType = UserType.value
        pParkedOrder.Status = Status.value
        pParkedOrder.ErrorID = ErrorID
        pParkedOrder.ErrorMsg = bytes(ErrorMsg, encoding='ascii')
        pParkedOrder.IsSwapOrder = IsSwapOrder
        pParkedOrder.AccountID = bytes(AccountID, encoding='ascii')
        pParkedOrder.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pParkedOrder.ClientID = bytes(ClientID, encoding='ascii')
        pParkedOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pParkedOrder.reserve2 = bytes(reserve2, encoding='ascii')
        pParkedOrder.MacAddress = bytes(MacAddress, encoding='ascii')
        pParkedOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pParkedOrder.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqParkedOrderInsert(self.api, byref(pParkedOrder), self.nRequestID)

    def ReqParkedOrderAction(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', OrderSysID: str = '', ActionFlag: TThostFtdcActionFlagType = list(TThostFtdcActionFlagType)[0], LimitPrice: float = .0, VolumeChange: int = 0, UserID: str = '', reserve1: str = '', ParkedOrderActionID: str = '', UserType: TThostFtdcUserTypeType = list(TThostFtdcUserTypeType)[0], Status: TThostFtdcParkedOrderStatusType = list(TThostFtdcParkedOrderStatusType)[0], ErrorID: int = 0, ErrorMsg: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pParkedOrderAction = CThostFtdcParkedOrderActionField()
        pParkedOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pParkedOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pParkedOrderAction.OrderActionRef = OrderActionRef
        pParkedOrderAction.OrderRef = bytes(OrderRef, encoding='ascii')
        pParkedOrderAction.RequestID = RequestID
        pParkedOrderAction.FrontID = FrontID
        pParkedOrderAction.SessionID = SessionID
        pParkedOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pParkedOrderAction.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pParkedOrderAction.ActionFlag = ActionFlag.value
        pParkedOrderAction.LimitPrice = LimitPrice
        pParkedOrderAction.VolumeChange = VolumeChange
        pParkedOrderAction.UserID = bytes(UserID, encoding='ascii')
        pParkedOrderAction.reserve1 = bytes(reserve1, encoding='ascii')
        pParkedOrderAction.ParkedOrderActionID = bytes(ParkedOrderActionID, encoding='ascii')
        pParkedOrderAction.UserType = UserType.value
        pParkedOrderAction.Status = Status.value
        pParkedOrderAction.ErrorID = ErrorID
        pParkedOrderAction.ErrorMsg = bytes(ErrorMsg, encoding='ascii')
        pParkedOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pParkedOrderAction.reserve2 = bytes(reserve2, encoding='ascii')
        pParkedOrderAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pParkedOrderAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pParkedOrderAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqParkedOrderAction(self.api, byref(pParkedOrderAction), self.nRequestID)

    def ReqOrderAction(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, OrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', OrderSysID: str = '', ActionFlag: TThostFtdcActionFlagType = list(TThostFtdcActionFlagType)[0], LimitPrice: float = .0, VolumeChange: int = 0, UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputOrderAction = CThostFtdcInputOrderActionField()
        pInputOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputOrderAction.OrderActionRef = OrderActionRef
        pInputOrderAction.OrderRef = bytes(OrderRef, encoding='ascii')
        pInputOrderAction.RequestID = RequestID
        pInputOrderAction.FrontID = FrontID
        pInputOrderAction.SessionID = SessionID
        pInputOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputOrderAction.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pInputOrderAction.ActionFlag = ActionFlag.value
        pInputOrderAction.LimitPrice = LimitPrice
        pInputOrderAction.VolumeChange = VolumeChange
        pInputOrderAction.UserID = bytes(UserID, encoding='ascii')
        pInputOrderAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputOrderAction.reserve2 = bytes(reserve2, encoding='ascii')
        pInputOrderAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputOrderAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputOrderAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOrderAction(self.api, byref(pInputOrderAction), self.nRequestID)

    def ReqQryMaxOrderVolume(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', Direction: TThostFtdcDirectionType = list(TThostFtdcDirectionType)[0], OffsetFlag: TThostFtdcOffsetFlagType = list(TThostFtdcOffsetFlagType)[0], HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], MaxVolume: int = 0, ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryMaxOrderVolume = CThostFtdcQryMaxOrderVolumeField()
        pQryMaxOrderVolume.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryMaxOrderVolume.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryMaxOrderVolume.reserve1 = bytes(reserve1, encoding='ascii')
        pQryMaxOrderVolume.Direction = Direction.value
        pQryMaxOrderVolume.OffsetFlag = OffsetFlag.value
        pQryMaxOrderVolume.HedgeFlag = HedgeFlag.value
        pQryMaxOrderVolume.MaxVolume = MaxVolume
        pQryMaxOrderVolume.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryMaxOrderVolume.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryMaxOrderVolume.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryMaxOrderVolume(self.api, byref(pQryMaxOrderVolume), self.nRequestID)

    def ReqSettlementInfoConfirm(self, BrokerID: str = '', InvestorID: str = '', ConfirmDate: str = '', ConfirmTime: str = '', SettlementID: int = 0, AccountID: str = '', CurrencyID: str = ''):
        pSettlementInfoConfirm = CThostFtdcSettlementInfoConfirmField()
        pSettlementInfoConfirm.BrokerID = bytes(BrokerID, encoding='ascii')
        pSettlementInfoConfirm.InvestorID = bytes(InvestorID, encoding='ascii')
        pSettlementInfoConfirm.ConfirmDate = bytes(ConfirmDate, encoding='ascii')
        pSettlementInfoConfirm.ConfirmTime = bytes(ConfirmTime, encoding='ascii')
        pSettlementInfoConfirm.SettlementID = SettlementID
        pSettlementInfoConfirm.AccountID = bytes(AccountID, encoding='ascii')
        pSettlementInfoConfirm.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqSettlementInfoConfirm(self.api, byref(pSettlementInfoConfirm), self.nRequestID)

    def ReqRemoveParkedOrder(self, BrokerID: str = '', InvestorID: str = '', ParkedOrderID: str = '', InvestUnitID: str = ''):
        pRemoveParkedOrder = CThostFtdcRemoveParkedOrderField()
        pRemoveParkedOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pRemoveParkedOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pRemoveParkedOrder.ParkedOrderID = bytes(ParkedOrderID, encoding='ascii')
        pRemoveParkedOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqRemoveParkedOrder(self.api, byref(pRemoveParkedOrder), self.nRequestID)

    def ReqRemoveParkedOrderAction(self, BrokerID: str = '', InvestorID: str = '', ParkedOrderActionID: str = '', InvestUnitID: str = ''):
        pRemoveParkedOrderAction = CThostFtdcRemoveParkedOrderActionField()
        pRemoveParkedOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pRemoveParkedOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pRemoveParkedOrderAction.ParkedOrderActionID = bytes(ParkedOrderActionID, encoding='ascii')
        pRemoveParkedOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqRemoveParkedOrderAction(self.api, byref(pRemoveParkedOrderAction), self.nRequestID)

    def ReqExecOrderInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExecOrderRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '', OffsetFlag: TThostFtdcOffsetFlagType = list(TThostFtdcOffsetFlagType)[0], HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], ActionType: TThostFtdcActionTypeType = list(TThostFtdcActionTypeType)[0], PosiDirection: TThostFtdcPosiDirectionType = list(TThostFtdcPosiDirectionType)[0], ReservePositionFlag: TThostFtdcExecOrderPositionFlagType = list(TThostFtdcExecOrderPositionFlagType)[0], CloseFlag: TThostFtdcExecOrderCloseFlagType = list(TThostFtdcExecOrderCloseFlagType)[0], ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputExecOrder = CThostFtdcInputExecOrderField()
        pInputExecOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputExecOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputExecOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pInputExecOrder.ExecOrderRef = bytes(ExecOrderRef, encoding='ascii')
        pInputExecOrder.UserID = bytes(UserID, encoding='ascii')
        pInputExecOrder.Volume = Volume
        pInputExecOrder.RequestID = RequestID
        pInputExecOrder.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputExecOrder.OffsetFlag = OffsetFlag.value
        pInputExecOrder.HedgeFlag = HedgeFlag.value
        pInputExecOrder.ActionType = ActionType.value
        pInputExecOrder.PosiDirection = PosiDirection.value
        pInputExecOrder.ReservePositionFlag = ReservePositionFlag.value
        pInputExecOrder.CloseFlag = CloseFlag.value
        pInputExecOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputExecOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputExecOrder.AccountID = bytes(AccountID, encoding='ascii')
        pInputExecOrder.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pInputExecOrder.ClientID = bytes(ClientID, encoding='ascii')
        pInputExecOrder.reserve2 = bytes(reserve2, encoding='ascii')
        pInputExecOrder.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputExecOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputExecOrder.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqExecOrderInsert(self.api, byref(pInputExecOrder), self.nRequestID)

    def ReqExecOrderAction(self, BrokerID: str = '', InvestorID: str = '', ExecOrderActionRef: int = 0, ExecOrderRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', ExecOrderSysID: str = '', ActionFlag: TThostFtdcActionFlagType = list(TThostFtdcActionFlagType)[0], UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputExecOrderAction = CThostFtdcInputExecOrderActionField()
        pInputExecOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputExecOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputExecOrderAction.ExecOrderActionRef = ExecOrderActionRef
        pInputExecOrderAction.ExecOrderRef = bytes(ExecOrderRef, encoding='ascii')
        pInputExecOrderAction.RequestID = RequestID
        pInputExecOrderAction.FrontID = FrontID
        pInputExecOrderAction.SessionID = SessionID
        pInputExecOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputExecOrderAction.ExecOrderSysID = bytes(ExecOrderSysID, encoding='ascii')
        pInputExecOrderAction.ActionFlag = ActionFlag.value
        pInputExecOrderAction.UserID = bytes(UserID, encoding='ascii')
        pInputExecOrderAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputExecOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputExecOrderAction.reserve2 = bytes(reserve2, encoding='ascii')
        pInputExecOrderAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputExecOrderAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputExecOrderAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqExecOrderAction(self.api, byref(pInputExecOrderAction), self.nRequestID)

    def ReqForQuoteInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ForQuoteRef: str = '', UserID: str = '', ExchangeID: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputForQuote = CThostFtdcInputForQuoteField()
        pInputForQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputForQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputForQuote.reserve1 = bytes(reserve1, encoding='ascii')
        pInputForQuote.ForQuoteRef = bytes(ForQuoteRef, encoding='ascii')
        pInputForQuote.UserID = bytes(UserID, encoding='ascii')
        pInputForQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputForQuote.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputForQuote.reserve2 = bytes(reserve2, encoding='ascii')
        pInputForQuote.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputForQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputForQuote.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqForQuoteInsert(self.api, byref(pInputForQuote), self.nRequestID)

    def ReqQuoteInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', QuoteRef: str = '', UserID: str = '', AskPrice: float = .0, BidPrice: float = .0, AskVolume: int = 0, BidVolume: int = 0, RequestID: int = 0, BusinessUnit: str = '', AskOffsetFlag: TThostFtdcOffsetFlagType = list(TThostFtdcOffsetFlagType)[0], BidOffsetFlag: TThostFtdcOffsetFlagType = list(TThostFtdcOffsetFlagType)[0], AskHedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], BidHedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], AskOrderRef: str = '', BidOrderRef: str = '', ForQuoteSysID: str = '', ExchangeID: str = '', InvestUnitID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputQuote = CThostFtdcInputQuoteField()
        pInputQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputQuote.reserve1 = bytes(reserve1, encoding='ascii')
        pInputQuote.QuoteRef = bytes(QuoteRef, encoding='ascii')
        pInputQuote.UserID = bytes(UserID, encoding='ascii')
        pInputQuote.AskPrice = AskPrice
        pInputQuote.BidPrice = BidPrice
        pInputQuote.AskVolume = AskVolume
        pInputQuote.BidVolume = BidVolume
        pInputQuote.RequestID = RequestID
        pInputQuote.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputQuote.AskOffsetFlag = AskOffsetFlag.value
        pInputQuote.BidOffsetFlag = BidOffsetFlag.value
        pInputQuote.AskHedgeFlag = AskHedgeFlag.value
        pInputQuote.BidHedgeFlag = BidHedgeFlag.value
        pInputQuote.AskOrderRef = bytes(AskOrderRef, encoding='ascii')
        pInputQuote.BidOrderRef = bytes(BidOrderRef, encoding='ascii')
        pInputQuote.ForQuoteSysID = bytes(ForQuoteSysID, encoding='ascii')
        pInputQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputQuote.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputQuote.ClientID = bytes(ClientID, encoding='ascii')
        pInputQuote.reserve2 = bytes(reserve2, encoding='ascii')
        pInputQuote.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputQuote.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQuoteInsert(self.api, byref(pInputQuote), self.nRequestID)

    def ReqQuoteAction(self, BrokerID: str = '', InvestorID: str = '', QuoteActionRef: int = 0, QuoteRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', QuoteSysID: str = '', ActionFlag: TThostFtdcActionFlagType = list(TThostFtdcActionFlagType)[0], UserID: str = '', reserve1: str = '', InvestUnitID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputQuoteAction = CThostFtdcInputQuoteActionField()
        pInputQuoteAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputQuoteAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputQuoteAction.QuoteActionRef = QuoteActionRef
        pInputQuoteAction.QuoteRef = bytes(QuoteRef, encoding='ascii')
        pInputQuoteAction.RequestID = RequestID
        pInputQuoteAction.FrontID = FrontID
        pInputQuoteAction.SessionID = SessionID
        pInputQuoteAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputQuoteAction.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
        pInputQuoteAction.ActionFlag = ActionFlag.value
        pInputQuoteAction.UserID = bytes(UserID, encoding='ascii')
        pInputQuoteAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputQuoteAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputQuoteAction.ClientID = bytes(ClientID, encoding='ascii')
        pInputQuoteAction.reserve2 = bytes(reserve2, encoding='ascii')
        pInputQuoteAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputQuoteAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputQuoteAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQuoteAction(self.api, byref(pInputQuoteAction), self.nRequestID)

    def ReqBatchOrderAction(self, BrokerID: str = '', InvestorID: str = '', OrderActionRef: int = 0, RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', UserID: str = '', InvestUnitID: str = '', reserve1: str = '', MacAddress: str = '', IPAddress: str = ''):
        pInputBatchOrderAction = CThostFtdcInputBatchOrderActionField()
        pInputBatchOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputBatchOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputBatchOrderAction.OrderActionRef = OrderActionRef
        pInputBatchOrderAction.RequestID = RequestID
        pInputBatchOrderAction.FrontID = FrontID
        pInputBatchOrderAction.SessionID = SessionID
        pInputBatchOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputBatchOrderAction.UserID = bytes(UserID, encoding='ascii')
        pInputBatchOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputBatchOrderAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputBatchOrderAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputBatchOrderAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqBatchOrderAction(self.api, byref(pInputBatchOrderAction), self.nRequestID)

    def ReqOptionSelfCloseInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', OptionSelfCloseRef: str = '', UserID: str = '', Volume: int = 0, RequestID: int = 0, BusinessUnit: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], OptSelfCloseFlag: TThostFtdcOptSelfCloseFlagType = list(TThostFtdcOptSelfCloseFlagType)[0], ExchangeID: str = '', InvestUnitID: str = '', AccountID: str = '', CurrencyID: str = '', ClientID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputOptionSelfClose = CThostFtdcInputOptionSelfCloseField()
        pInputOptionSelfClose.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputOptionSelfClose.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputOptionSelfClose.reserve1 = bytes(reserve1, encoding='ascii')
        pInputOptionSelfClose.OptionSelfCloseRef = bytes(OptionSelfCloseRef, encoding='ascii')
        pInputOptionSelfClose.UserID = bytes(UserID, encoding='ascii')
        pInputOptionSelfClose.Volume = Volume
        pInputOptionSelfClose.RequestID = RequestID
        pInputOptionSelfClose.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputOptionSelfClose.HedgeFlag = HedgeFlag.value
        pInputOptionSelfClose.OptSelfCloseFlag = OptSelfCloseFlag.value
        pInputOptionSelfClose.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputOptionSelfClose.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputOptionSelfClose.AccountID = bytes(AccountID, encoding='ascii')
        pInputOptionSelfClose.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pInputOptionSelfClose.ClientID = bytes(ClientID, encoding='ascii')
        pInputOptionSelfClose.reserve2 = bytes(reserve2, encoding='ascii')
        pInputOptionSelfClose.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputOptionSelfClose.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputOptionSelfClose.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOptionSelfCloseInsert(self.api, byref(pInputOptionSelfClose), self.nRequestID)

    def ReqOptionSelfCloseAction(self, BrokerID: str = '', InvestorID: str = '', OptionSelfCloseActionRef: int = 0, OptionSelfCloseRef: str = '', RequestID: int = 0, FrontID: int = 0, SessionID: int = 0, ExchangeID: str = '', OptionSelfCloseSysID: str = '', ActionFlag: TThostFtdcActionFlagType = list(TThostFtdcActionFlagType)[0], UserID: str = '', reserve1: str = '', InvestUnitID: str = '', reserve2: str = '', MacAddress: str = '', InstrumentID: str = '', IPAddress: str = ''):
        pInputOptionSelfCloseAction = CThostFtdcInputOptionSelfCloseActionField()
        pInputOptionSelfCloseAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputOptionSelfCloseAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputOptionSelfCloseAction.OptionSelfCloseActionRef = OptionSelfCloseActionRef
        pInputOptionSelfCloseAction.OptionSelfCloseRef = bytes(OptionSelfCloseRef, encoding='ascii')
        pInputOptionSelfCloseAction.RequestID = RequestID
        pInputOptionSelfCloseAction.FrontID = FrontID
        pInputOptionSelfCloseAction.SessionID = SessionID
        pInputOptionSelfCloseAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputOptionSelfCloseAction.OptionSelfCloseSysID = bytes(OptionSelfCloseSysID, encoding='ascii')
        pInputOptionSelfCloseAction.ActionFlag = ActionFlag.value
        pInputOptionSelfCloseAction.UserID = bytes(UserID, encoding='ascii')
        pInputOptionSelfCloseAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputOptionSelfCloseAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputOptionSelfCloseAction.reserve2 = bytes(reserve2, encoding='ascii')
        pInputOptionSelfCloseAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputOptionSelfCloseAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputOptionSelfCloseAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOptionSelfCloseAction(self.api, byref(pInputOptionSelfCloseAction), self.nRequestID)

    def ReqCombActionInsert(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', CombActionRef: str = '', UserID: str = '', Direction: TThostFtdcDirectionType = list(TThostFtdcDirectionType)[0], Volume: int = 0, CombDirection: TThostFtdcCombDirectionType = list(TThostFtdcCombDirectionType)[0], HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], ExchangeID: str = '', reserve2: str = '', MacAddress: str = '', InvestUnitID: str = '', FrontID: int = 0, SessionID: int = 0, InstrumentID: str = '', IPAddress: str = ''):
        pInputCombAction = CThostFtdcInputCombActionField()
        pInputCombAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputCombAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputCombAction.reserve1 = bytes(reserve1, encoding='ascii')
        pInputCombAction.CombActionRef = bytes(CombActionRef, encoding='ascii')
        pInputCombAction.UserID = bytes(UserID, encoding='ascii')
        pInputCombAction.Direction = Direction.value
        pInputCombAction.Volume = Volume
        pInputCombAction.CombDirection = CombDirection.value
        pInputCombAction.HedgeFlag = HedgeFlag.value
        pInputCombAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputCombAction.reserve2 = bytes(reserve2, encoding='ascii')
        pInputCombAction.MacAddress = bytes(MacAddress, encoding='ascii')
        pInputCombAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pInputCombAction.FrontID = FrontID
        pInputCombAction.SessionID = SessionID
        pInputCombAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputCombAction.IPAddress = bytes(IPAddress, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqCombActionInsert(self.api, byref(pInputCombAction), self.nRequestID)

    def ReqQryOrder(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', OrderSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryOrder = CThostFtdcQryOrderField()
        pQryOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pQryOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryOrder.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pQryOrder.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
        pQryOrder.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')
        pQryOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryOrder(self.api, byref(pQryOrder), self.nRequestID)

    def ReqQryTrade(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', TradeID: str = '', TradeTimeStart: str = '', TradeTimeEnd: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryTrade = CThostFtdcQryTradeField()
        pQryTrade.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTrade.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTrade.reserve1 = bytes(reserve1, encoding='ascii')
        pQryTrade.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryTrade.TradeID = bytes(TradeID, encoding='ascii')
        pQryTrade.TradeTimeStart = bytes(TradeTimeStart, encoding='ascii')
        pQryTrade.TradeTimeEnd = bytes(TradeTimeEnd, encoding='ascii')
        pQryTrade.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryTrade.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTrade(self.api, byref(pQryTrade), self.nRequestID)

    def ReqQryInvestorPosition(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryInvestorPosition = CThostFtdcQryInvestorPositionField()
        pQryInvestorPosition.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorPosition.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorPosition.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInvestorPosition.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorPosition.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInvestorPosition.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorPosition(self.api, byref(pQryInvestorPosition), self.nRequestID)

    def ReqQryTradingAccount(self, BrokerID: str = '', InvestorID: str = '', CurrencyID: str = '', BizType: TThostFtdcBizTypeType = list(TThostFtdcBizTypeType)[0], AccountID: str = ''):
        pQryTradingAccount = CThostFtdcQryTradingAccountField()
        pQryTradingAccount.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTradingAccount.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTradingAccount.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pQryTradingAccount.BizType = BizType.value
        pQryTradingAccount.AccountID = bytes(AccountID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTradingAccount(self.api, byref(pQryTradingAccount), self.nRequestID)

    def ReqQryInvestor(self, BrokerID: str = '', InvestorID: str = ''):
        pQryInvestor = CThostFtdcQryInvestorField()
        pQryInvestor.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestor.InvestorID = bytes(InvestorID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestor(self.api, byref(pQryInvestor), self.nRequestID)

    def ReqQryTradingCode(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', ClientID: str = '', ClientIDType: TThostFtdcClientIDTypeType = list(TThostFtdcClientIDTypeType)[0], InvestUnitID: str = ''):
        pQryTradingCode = CThostFtdcQryTradingCodeField()
        pQryTradingCode.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTradingCode.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTradingCode.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryTradingCode.ClientID = bytes(ClientID, encoding='ascii')
        pQryTradingCode.ClientIDType = ClientIDType.value
        pQryTradingCode.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTradingCode(self.api, byref(pQryTradingCode), self.nRequestID)

    def ReqQryInstrumentMarginRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryInstrumentMarginRate = CThostFtdcQryInstrumentMarginRateField()
        pQryInstrumentMarginRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInstrumentMarginRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInstrumentMarginRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInstrumentMarginRate.HedgeFlag = HedgeFlag.value
        pQryInstrumentMarginRate.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInstrumentMarginRate.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInstrumentMarginRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrumentMarginRate(self.api, byref(pQryInstrumentMarginRate), self.nRequestID)

    def ReqQryInstrumentCommissionRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryInstrumentCommissionRate = CThostFtdcQryInstrumentCommissionRateField()
        pQryInstrumentCommissionRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInstrumentCommissionRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInstrumentCommissionRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInstrumentCommissionRate.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInstrumentCommissionRate.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInstrumentCommissionRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrumentCommissionRate(self.api, byref(pQryInstrumentCommissionRate), self.nRequestID)

    def ReqQryExchange(self, ExchangeID: str = ''):
        pQryExchange = CThostFtdcQryExchangeField()
        pQryExchange.ExchangeID = bytes(ExchangeID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExchange(self.api, byref(pQryExchange), self.nRequestID)

    def ReqQryProduct(self, reserve1: str = '', ProductClass: TThostFtdcProductClassType = list(TThostFtdcProductClassType)[0], ExchangeID: str = '', ProductID: str = ''):
        pQryProduct = CThostFtdcQryProductField()
        pQryProduct.reserve1 = bytes(reserve1, encoding='ascii')
        pQryProduct.ProductClass = ProductClass.value
        pQryProduct.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryProduct.ProductID = bytes(ProductID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryProduct(self.api, byref(pQryProduct), self.nRequestID)

    def ReqQryInstrument(self, reserve1: str = '', ExchangeID: str = '', reserve2: str = '', reserve3: str = '', InstrumentID: str = '', ExchangeInstID: str = '', ProductID: str = ''):
        pQryInstrument = CThostFtdcQryInstrumentField()
        pQryInstrument.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInstrument.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInstrument.reserve2 = bytes(reserve2, encoding='ascii')
        pQryInstrument.reserve3 = bytes(reserve3, encoding='ascii')
        pQryInstrument.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pQryInstrument.ExchangeInstID = bytes(ExchangeInstID, encoding='ascii')
        pQryInstrument.ProductID = bytes(ProductID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrument(self.api, byref(pQryInstrument), self.nRequestID)

    def ReqQryDepthMarketData(self, reserve1: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        pQryDepthMarketData = CThostFtdcQryDepthMarketDataField()
        pQryDepthMarketData.reserve1 = bytes(reserve1, encoding='ascii')
        pQryDepthMarketData.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryDepthMarketData.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryDepthMarketData(self.api, byref(pQryDepthMarketData), self.nRequestID)

    def ReqQrySettlementInfo(self, BrokerID: str = '', InvestorID: str = '', TradingDay: str = '', AccountID: str = '', CurrencyID: str = ''):
        pQrySettlementInfo = CThostFtdcQrySettlementInfoField()
        pQrySettlementInfo.BrokerID = bytes(BrokerID, encoding='ascii')
        pQrySettlementInfo.InvestorID = bytes(InvestorID, encoding='ascii')
        pQrySettlementInfo.TradingDay = bytes(TradingDay, encoding='ascii')
        pQrySettlementInfo.AccountID = bytes(AccountID, encoding='ascii')
        pQrySettlementInfo.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySettlementInfo(self.api, byref(pQrySettlementInfo), self.nRequestID)

    def ReqQryTransferBank(self, BankID: str = '', BankBrchID: str = ''):
        pQryTransferBank = CThostFtdcQryTransferBankField()
        pQryTransferBank.BankID = bytes(BankID, encoding='ascii')
        pQryTransferBank.BankBrchID = bytes(BankBrchID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTransferBank(self.api, byref(pQryTransferBank), self.nRequestID)

    def ReqQryInvestorPositionDetail(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryInvestorPositionDetail = CThostFtdcQryInvestorPositionDetailField()
        pQryInvestorPositionDetail.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorPositionDetail.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorPositionDetail.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInvestorPositionDetail.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorPositionDetail.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInvestorPositionDetail.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorPositionDetail(self.api, byref(pQryInvestorPositionDetail), self.nRequestID)

    def ReqQryNotice(self, BrokerID: str = ''):
        pQryNotice = CThostFtdcQryNoticeField()
        pQryNotice.BrokerID = bytes(BrokerID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryNotice(self.api, byref(pQryNotice), self.nRequestID)

    def ReqQrySettlementInfoConfirm(self, BrokerID: str = '', InvestorID: str = '', AccountID: str = '', CurrencyID: str = ''):
        pQrySettlementInfoConfirm = CThostFtdcQrySettlementInfoConfirmField()
        pQrySettlementInfoConfirm.BrokerID = bytes(BrokerID, encoding='ascii')
        pQrySettlementInfoConfirm.InvestorID = bytes(InvestorID, encoding='ascii')
        pQrySettlementInfoConfirm.AccountID = bytes(AccountID, encoding='ascii')
        pQrySettlementInfoConfirm.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySettlementInfoConfirm(self.api, byref(pQrySettlementInfoConfirm), self.nRequestID)

    def ReqQryInvestorPositionCombineDetail(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', CombInstrumentID: str = ''):
        pQryInvestorPositionCombineDetail = CThostFtdcQryInvestorPositionCombineDetailField()
        pQryInvestorPositionCombineDetail.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorPositionCombineDetail.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorPositionCombineDetail.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInvestorPositionCombineDetail.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorPositionCombineDetail.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInvestorPositionCombineDetail.CombInstrumentID = bytes(CombInstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorPositionCombineDetail(self.api, byref(pQryInvestorPositionCombineDetail), self.nRequestID)

    def ReqQryCFMMCTradingAccountKey(self, BrokerID: str = '', InvestorID: str = ''):
        pQryCFMMCTradingAccountKey = CThostFtdcQryCFMMCTradingAccountKeyField()
        pQryCFMMCTradingAccountKey.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryCFMMCTradingAccountKey.InvestorID = bytes(InvestorID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryCFMMCTradingAccountKey(self.api, byref(pQryCFMMCTradingAccountKey), self.nRequestID)

    def ReqQryEWarrantOffset(self, BrokerID: str = '', InvestorID: str = '', ExchangeID: str = '', reserve1: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryEWarrantOffset = CThostFtdcQryEWarrantOffsetField()
        pQryEWarrantOffset.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryEWarrantOffset.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryEWarrantOffset.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryEWarrantOffset.reserve1 = bytes(reserve1, encoding='ascii')
        pQryEWarrantOffset.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryEWarrantOffset.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryEWarrantOffset(self.api, byref(pQryEWarrantOffset), self.nRequestID)

    def ReqQryInvestorProductGroupMargin(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], ExchangeID: str = '', InvestUnitID: str = '', ProductGroupID: str = ''):
        pQryInvestorProductGroupMargin = CThostFtdcQryInvestorProductGroupMarginField()
        pQryInvestorProductGroupMargin.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorProductGroupMargin.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorProductGroupMargin.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInvestorProductGroupMargin.HedgeFlag = HedgeFlag.value
        pQryInvestorProductGroupMargin.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorProductGroupMargin.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryInvestorProductGroupMargin.ProductGroupID = bytes(ProductGroupID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorProductGroupMargin(self.api, byref(pQryInvestorProductGroupMargin), self.nRequestID)

    def ReqQryExchangeMarginRate(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], ExchangeID: str = '', InstrumentID: str = ''):
        pQryExchangeMarginRate = CThostFtdcQryExchangeMarginRateField()
        pQryExchangeMarginRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryExchangeMarginRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryExchangeMarginRate.HedgeFlag = HedgeFlag.value
        pQryExchangeMarginRate.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryExchangeMarginRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExchangeMarginRate(self.api, byref(pQryExchangeMarginRate), self.nRequestID)

    def ReqQryExchangeMarginRateAdjust(self, BrokerID: str = '', reserve1: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], InstrumentID: str = ''):
        pQryExchangeMarginRateAdjust = CThostFtdcQryExchangeMarginRateAdjustField()
        pQryExchangeMarginRateAdjust.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryExchangeMarginRateAdjust.reserve1 = bytes(reserve1, encoding='ascii')
        pQryExchangeMarginRateAdjust.HedgeFlag = HedgeFlag.value
        pQryExchangeMarginRateAdjust.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExchangeMarginRateAdjust(self.api, byref(pQryExchangeMarginRateAdjust), self.nRequestID)

    def ReqQryExchangeRate(self, BrokerID: str = '', FromCurrencyID: str = '', ToCurrencyID: str = ''):
        pQryExchangeRate = CThostFtdcQryExchangeRateField()
        pQryExchangeRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryExchangeRate.FromCurrencyID = bytes(FromCurrencyID, encoding='ascii')
        pQryExchangeRate.ToCurrencyID = bytes(ToCurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExchangeRate(self.api, byref(pQryExchangeRate), self.nRequestID)

    def ReqQrySecAgentACIDMap(self, BrokerID: str = '', UserID: str = '', AccountID: str = '', CurrencyID: str = ''):
        pQrySecAgentACIDMap = CThostFtdcQrySecAgentACIDMapField()
        pQrySecAgentACIDMap.BrokerID = bytes(BrokerID, encoding='ascii')
        pQrySecAgentACIDMap.UserID = bytes(UserID, encoding='ascii')
        pQrySecAgentACIDMap.AccountID = bytes(AccountID, encoding='ascii')
        pQrySecAgentACIDMap.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySecAgentACIDMap(self.api, byref(pQrySecAgentACIDMap), self.nRequestID)

    def ReqQryProductExchRate(self, reserve1: str = '', ExchangeID: str = '', ProductID: str = ''):
        pQryProductExchRate = CThostFtdcQryProductExchRateField()
        pQryProductExchRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryProductExchRate.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryProductExchRate.ProductID = bytes(ProductID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryProductExchRate(self.api, byref(pQryProductExchRate), self.nRequestID)

    def ReqQryProductGroup(self, reserve1: str = '', ExchangeID: str = '', ProductID: str = ''):
        pQryProductGroup = CThostFtdcQryProductGroupField()
        pQryProductGroup.reserve1 = bytes(reserve1, encoding='ascii')
        pQryProductGroup.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryProductGroup.ProductID = bytes(ProductID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryProductGroup(self.api, byref(pQryProductGroup), self.nRequestID)

    def ReqQryMMInstrumentCommissionRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        pQryMMInstrumentCommissionRate = CThostFtdcQryMMInstrumentCommissionRateField()
        pQryMMInstrumentCommissionRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryMMInstrumentCommissionRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryMMInstrumentCommissionRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryMMInstrumentCommissionRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryMMInstrumentCommissionRate(self.api, byref(pQryMMInstrumentCommissionRate), self.nRequestID)

    def ReqQryMMOptionInstrCommRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        pQryMMOptionInstrCommRate = CThostFtdcQryMMOptionInstrCommRateField()
        pQryMMOptionInstrCommRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryMMOptionInstrCommRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryMMOptionInstrCommRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryMMOptionInstrCommRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryMMOptionInstrCommRate(self.api, byref(pQryMMOptionInstrCommRate), self.nRequestID)

    def ReqQryInstrumentOrderCommRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', InstrumentID: str = ''):
        pQryInstrumentOrderCommRate = CThostFtdcQryInstrumentOrderCommRateField()
        pQryInstrumentOrderCommRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInstrumentOrderCommRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInstrumentOrderCommRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryInstrumentOrderCommRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrumentOrderCommRate(self.api, byref(pQryInstrumentOrderCommRate), self.nRequestID)

    def ReqQrySecAgentTradingAccount(self, BrokerID: str = '', InvestorID: str = '', CurrencyID: str = '', BizType: TThostFtdcBizTypeType = list(TThostFtdcBizTypeType)[0], AccountID: str = ''):
        pQryTradingAccount = CThostFtdcQryTradingAccountField()
        pQryTradingAccount.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTradingAccount.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTradingAccount.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pQryTradingAccount.BizType = BizType.value
        pQryTradingAccount.AccountID = bytes(AccountID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySecAgentTradingAccount(self.api, byref(pQryTradingAccount), self.nRequestID)

    def ReqQrySecAgentCheckMode(self, BrokerID: str = '', InvestorID: str = ''):
        pQrySecAgentCheckMode = CThostFtdcQrySecAgentCheckModeField()
        pQrySecAgentCheckMode.BrokerID = bytes(BrokerID, encoding='ascii')
        pQrySecAgentCheckMode.InvestorID = bytes(InvestorID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySecAgentCheckMode(self.api, byref(pQrySecAgentCheckMode), self.nRequestID)

    def ReqQrySecAgentTradeInfo(self, BrokerID: str = '', BrokerSecAgentID: str = ''):
        pQrySecAgentTradeInfo = CThostFtdcQrySecAgentTradeInfoField()
        pQrySecAgentTradeInfo.BrokerID = bytes(BrokerID, encoding='ascii')
        pQrySecAgentTradeInfo.BrokerSecAgentID = bytes(BrokerSecAgentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySecAgentTradeInfo(self.api, byref(pQrySecAgentTradeInfo), self.nRequestID)

    def ReqQryOptionInstrTradeCost(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', HedgeFlag: TThostFtdcHedgeFlagType = list(TThostFtdcHedgeFlagType)[0], InputPrice: float = .0, UnderlyingPrice: float = .0, ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryOptionInstrTradeCost = CThostFtdcQryOptionInstrTradeCostField()
        pQryOptionInstrTradeCost.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryOptionInstrTradeCost.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryOptionInstrTradeCost.reserve1 = bytes(reserve1, encoding='ascii')
        pQryOptionInstrTradeCost.HedgeFlag = HedgeFlag.value
        pQryOptionInstrTradeCost.InputPrice = InputPrice
        pQryOptionInstrTradeCost.UnderlyingPrice = UnderlyingPrice
        pQryOptionInstrTradeCost.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryOptionInstrTradeCost.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryOptionInstrTradeCost.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryOptionInstrTradeCost(self.api, byref(pQryOptionInstrTradeCost), self.nRequestID)

    def ReqQryOptionInstrCommRate(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryOptionInstrCommRate = CThostFtdcQryOptionInstrCommRateField()
        pQryOptionInstrCommRate.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryOptionInstrCommRate.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryOptionInstrCommRate.reserve1 = bytes(reserve1, encoding='ascii')
        pQryOptionInstrCommRate.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryOptionInstrCommRate.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryOptionInstrCommRate.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryOptionInstrCommRate(self.api, byref(pQryOptionInstrCommRate), self.nRequestID)

    def ReqQryExecOrder(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', ExecOrderSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InstrumentID: str = ''):
        pQryExecOrder = CThostFtdcQryExecOrderField()
        pQryExecOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryExecOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryExecOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pQryExecOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryExecOrder.ExecOrderSysID = bytes(ExecOrderSysID, encoding='ascii')
        pQryExecOrder.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
        pQryExecOrder.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')
        pQryExecOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExecOrder(self.api, byref(pQryExecOrder), self.nRequestID)

    def ReqQryForQuote(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryForQuote = CThostFtdcQryForQuoteField()
        pQryForQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryForQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryForQuote.reserve1 = bytes(reserve1, encoding='ascii')
        pQryForQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryForQuote.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
        pQryForQuote.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')
        pQryForQuote.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryForQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryForQuote(self.api, byref(pQryForQuote), self.nRequestID)

    def ReqQryQuote(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', QuoteSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryQuote = CThostFtdcQryQuoteField()
        pQryQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryQuote.reserve1 = bytes(reserve1, encoding='ascii')
        pQryQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryQuote.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
        pQryQuote.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
        pQryQuote.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')
        pQryQuote.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryQuote(self.api, byref(pQryQuote), self.nRequestID)

    def ReqQryOptionSelfClose(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', OptionSelfCloseSysID: str = '', InsertTimeStart: str = '', InsertTimeEnd: str = '', InstrumentID: str = ''):
        pQryOptionSelfClose = CThostFtdcQryOptionSelfCloseField()
        pQryOptionSelfClose.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryOptionSelfClose.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryOptionSelfClose.reserve1 = bytes(reserve1, encoding='ascii')
        pQryOptionSelfClose.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryOptionSelfClose.OptionSelfCloseSysID = bytes(OptionSelfCloseSysID, encoding='ascii')
        pQryOptionSelfClose.InsertTimeStart = bytes(InsertTimeStart, encoding='ascii')
        pQryOptionSelfClose.InsertTimeEnd = bytes(InsertTimeEnd, encoding='ascii')
        pQryOptionSelfClose.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryOptionSelfClose(self.api, byref(pQryOptionSelfClose), self.nRequestID)

    def ReqQryInvestUnit(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        pQryInvestUnit = CThostFtdcQryInvestUnitField()
        pQryInvestUnit.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestUnit.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestUnit.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestUnit(self.api, byref(pQryInvestUnit), self.nRequestID)

    def ReqQryCombInstrumentGuard(self, BrokerID: str = '', reserve1: str = '', ExchangeID: str = '', InstrumentID: str = ''):
        pQryCombInstrumentGuard = CThostFtdcQryCombInstrumentGuardField()
        pQryCombInstrumentGuard.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryCombInstrumentGuard.reserve1 = bytes(reserve1, encoding='ascii')
        pQryCombInstrumentGuard.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryCombInstrumentGuard.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryCombInstrumentGuard(self.api, byref(pQryCombInstrumentGuard), self.nRequestID)

    def ReqQryCombAction(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryCombAction = CThostFtdcQryCombActionField()
        pQryCombAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryCombAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryCombAction.reserve1 = bytes(reserve1, encoding='ascii')
        pQryCombAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryCombAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryCombAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryCombAction(self.api, byref(pQryCombAction), self.nRequestID)

    def ReqQryTransferSerial(self, BrokerID: str = '', AccountID: str = '', BankID: str = '', CurrencyID: str = ''):
        pQryTransferSerial = CThostFtdcQryTransferSerialField()
        pQryTransferSerial.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTransferSerial.AccountID = bytes(AccountID, encoding='ascii')
        pQryTransferSerial.BankID = bytes(BankID, encoding='ascii')
        pQryTransferSerial.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTransferSerial(self.api, byref(pQryTransferSerial), self.nRequestID)

    def ReqQryAccountregister(self, BrokerID: str = '', AccountID: str = '', BankID: str = '', BankBranchID: str = '', CurrencyID: str = ''):
        pQryAccountregister = CThostFtdcQryAccountregisterField()
        pQryAccountregister.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryAccountregister.AccountID = bytes(AccountID, encoding='ascii')
        pQryAccountregister.BankID = bytes(BankID, encoding='ascii')
        pQryAccountregister.BankBranchID = bytes(BankBranchID, encoding='ascii')
        pQryAccountregister.CurrencyID = bytes(CurrencyID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryAccountregister(self.api, byref(pQryAccountregister), self.nRequestID)

    def ReqQryContractBank(self, BrokerID: str = '', BankID: str = '', BankBrchID: str = ''):
        pQryContractBank = CThostFtdcQryContractBankField()
        pQryContractBank.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryContractBank.BankID = bytes(BankID, encoding='ascii')
        pQryContractBank.BankBrchID = bytes(BankBrchID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryContractBank(self.api, byref(pQryContractBank), self.nRequestID)

    def ReqQryParkedOrder(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryParkedOrder = CThostFtdcQryParkedOrderField()
        pQryParkedOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryParkedOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryParkedOrder.reserve1 = bytes(reserve1, encoding='ascii')
        pQryParkedOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryParkedOrder.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryParkedOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryParkedOrder(self.api, byref(pQryParkedOrder), self.nRequestID)

    def ReqQryParkedOrderAction(self, BrokerID: str = '', InvestorID: str = '', reserve1: str = '', ExchangeID: str = '', InvestUnitID: str = '', InstrumentID: str = ''):
        pQryParkedOrderAction = CThostFtdcQryParkedOrderActionField()
        pQryParkedOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryParkedOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryParkedOrderAction.reserve1 = bytes(reserve1, encoding='ascii')
        pQryParkedOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryParkedOrderAction.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        pQryParkedOrderAction.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryParkedOrderAction(self.api, byref(pQryParkedOrderAction), self.nRequestID)

    def ReqQryTradingNotice(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        pQryTradingNotice = CThostFtdcQryTradingNoticeField()
        pQryTradingNotice.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTradingNotice.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTradingNotice.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTradingNotice(self.api, byref(pQryTradingNotice), self.nRequestID)

    def ReqQryBrokerTradingParams(self, BrokerID: str = '', InvestorID: str = '', CurrencyID: str = '', AccountID: str = ''):
        pQryBrokerTradingParams = CThostFtdcQryBrokerTradingParamsField()
        pQryBrokerTradingParams.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryBrokerTradingParams.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryBrokerTradingParams.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pQryBrokerTradingParams.AccountID = bytes(AccountID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryBrokerTradingParams(self.api, byref(pQryBrokerTradingParams), self.nRequestID)

    def ReqQryBrokerTradingAlgos(self, BrokerID: str = '', ExchangeID: str = '', reserve1: str = '', InstrumentID: str = ''):
        pQryBrokerTradingAlgos = CThostFtdcQryBrokerTradingAlgosField()
        pQryBrokerTradingAlgos.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryBrokerTradingAlgos.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryBrokerTradingAlgos.reserve1 = bytes(reserve1, encoding='ascii')
        pQryBrokerTradingAlgos.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryBrokerTradingAlgos(self.api, byref(pQryBrokerTradingAlgos), self.nRequestID)

    def ReqQueryCFMMCTradingAccountToken(self, BrokerID: str = '', InvestorID: str = '', InvestUnitID: str = ''):
        pQueryCFMMCTradingAccountToken = CThostFtdcQueryCFMMCTradingAccountTokenField()
        pQueryCFMMCTradingAccountToken.BrokerID = bytes(BrokerID, encoding='ascii')
        pQueryCFMMCTradingAccountToken.InvestorID = bytes(InvestorID, encoding='ascii')
        pQueryCFMMCTradingAccountToken.InvestUnitID = bytes(InvestUnitID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQueryCFMMCTradingAccountToken(self.api, byref(pQueryCFMMCTradingAccountToken), self.nRequestID)

    def ReqFromBankToFutureByFuture(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '', TradingDay: str = '', PlateSerial: int = 0, LastFragment: TThostFtdcLastFragmentType = list(TThostFtdcLastFragmentType)[0], SessionID: int = 0, CustomerName: str = '', IdCardType: TThostFtdcIdCardTypeType = list(TThostFtdcIdCardTypeType)[0], IdentifiedCardNo: str = '', CustType: TThostFtdcCustTypeType = list(TThostFtdcCustTypeType)[0], BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '', VerifyCertNoFlag: TThostFtdcYesNoIndicatorType = list(TThostFtdcYesNoIndicatorType)[0], CurrencyID: str = '', TradeAmount: float = .0, FutureFetchAmount: float = .0, FeePayFlag: TThostFtdcFeePayFlagType = list(TThostFtdcFeePayFlagType)[0], CustFee: float = .0, BrokerFee: float = .0, Message: str = '', Digest: str = '', BankAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], DeviceID: str = '', BankSecuAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], SecuPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: TThostFtdcTransferStatusType = list(TThostFtdcTransferStatusType)[0], LongCustomerName: str = ''):
        pReqTransfer = CThostFtdcReqTransferField()
        pReqTransfer.TradeCode = bytes(TradeCode, encoding='ascii')
        pReqTransfer.BankID = bytes(BankID, encoding='ascii')
        pReqTransfer.BankBranchID = bytes(BankBranchID, encoding='ascii')
        pReqTransfer.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqTransfer.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
        pReqTransfer.TradeDate = bytes(TradeDate, encoding='ascii')
        pReqTransfer.TradeTime = bytes(TradeTime, encoding='ascii')
        pReqTransfer.BankSerial = bytes(BankSerial, encoding='ascii')
        pReqTransfer.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqTransfer.PlateSerial = PlateSerial
        pReqTransfer.LastFragment = LastFragment.value
        pReqTransfer.SessionID = SessionID
        pReqTransfer.CustomerName = bytes(CustomerName, encoding='ascii')
        pReqTransfer.IdCardType = IdCardType.value
        pReqTransfer.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
        pReqTransfer.CustType = CustType.value
        pReqTransfer.BankAccount = bytes(BankAccount, encoding='ascii')
        pReqTransfer.BankPassWord = bytes(BankPassWord, encoding='ascii')
        pReqTransfer.AccountID = bytes(AccountID, encoding='ascii')
        pReqTransfer.Password = bytes(Password, encoding='ascii')
        pReqTransfer.InstallID = InstallID
        pReqTransfer.FutureSerial = FutureSerial
        pReqTransfer.UserID = bytes(UserID, encoding='ascii')
        pReqTransfer.VerifyCertNoFlag = VerifyCertNoFlag.value
        pReqTransfer.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pReqTransfer.TradeAmount = TradeAmount
        pReqTransfer.FutureFetchAmount = FutureFetchAmount
        pReqTransfer.FeePayFlag = FeePayFlag.value
        pReqTransfer.CustFee = CustFee
        pReqTransfer.BrokerFee = BrokerFee
        pReqTransfer.Message = bytes(Message, encoding='ascii')
        pReqTransfer.Digest = bytes(Digest, encoding='ascii')
        pReqTransfer.BankAccType = BankAccType.value
        pReqTransfer.DeviceID = bytes(DeviceID, encoding='ascii')
        pReqTransfer.BankSecuAccType = BankSecuAccType.value
        pReqTransfer.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
        pReqTransfer.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
        pReqTransfer.BankPwdFlag = BankPwdFlag.value
        pReqTransfer.SecuPwdFlag = SecuPwdFlag.value
        pReqTransfer.OperNo = bytes(OperNo, encoding='ascii')
        pReqTransfer.RequestID = RequestID
        pReqTransfer.TID = TID
        pReqTransfer.TransferStatus = TransferStatus.value
        pReqTransfer.LongCustomerName = bytes(LongCustomerName, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqFromBankToFutureByFuture(self.api, byref(pReqTransfer), self.nRequestID)

    def ReqFromFutureToBankByFuture(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '', TradingDay: str = '', PlateSerial: int = 0, LastFragment: TThostFtdcLastFragmentType = list(TThostFtdcLastFragmentType)[0], SessionID: int = 0, CustomerName: str = '', IdCardType: TThostFtdcIdCardTypeType = list(TThostFtdcIdCardTypeType)[0], IdentifiedCardNo: str = '', CustType: TThostFtdcCustTypeType = list(TThostFtdcCustTypeType)[0], BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', InstallID: int = 0, FutureSerial: int = 0, UserID: str = '', VerifyCertNoFlag: TThostFtdcYesNoIndicatorType = list(TThostFtdcYesNoIndicatorType)[0], CurrencyID: str = '', TradeAmount: float = .0, FutureFetchAmount: float = .0, FeePayFlag: TThostFtdcFeePayFlagType = list(TThostFtdcFeePayFlagType)[0], CustFee: float = .0, BrokerFee: float = .0, Message: str = '', Digest: str = '', BankAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], DeviceID: str = '', BankSecuAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], SecuPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], OperNo: str = '', RequestID: int = 0, TID: int = 0, TransferStatus: TThostFtdcTransferStatusType = list(TThostFtdcTransferStatusType)[0], LongCustomerName: str = ''):
        pReqTransfer = CThostFtdcReqTransferField()
        pReqTransfer.TradeCode = bytes(TradeCode, encoding='ascii')
        pReqTransfer.BankID = bytes(BankID, encoding='ascii')
        pReqTransfer.BankBranchID = bytes(BankBranchID, encoding='ascii')
        pReqTransfer.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqTransfer.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
        pReqTransfer.TradeDate = bytes(TradeDate, encoding='ascii')
        pReqTransfer.TradeTime = bytes(TradeTime, encoding='ascii')
        pReqTransfer.BankSerial = bytes(BankSerial, encoding='ascii')
        pReqTransfer.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqTransfer.PlateSerial = PlateSerial
        pReqTransfer.LastFragment = LastFragment.value
        pReqTransfer.SessionID = SessionID
        pReqTransfer.CustomerName = bytes(CustomerName, encoding='ascii')
        pReqTransfer.IdCardType = IdCardType.value
        pReqTransfer.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
        pReqTransfer.CustType = CustType.value
        pReqTransfer.BankAccount = bytes(BankAccount, encoding='ascii')
        pReqTransfer.BankPassWord = bytes(BankPassWord, encoding='ascii')
        pReqTransfer.AccountID = bytes(AccountID, encoding='ascii')
        pReqTransfer.Password = bytes(Password, encoding='ascii')
        pReqTransfer.InstallID = InstallID
        pReqTransfer.FutureSerial = FutureSerial
        pReqTransfer.UserID = bytes(UserID, encoding='ascii')
        pReqTransfer.VerifyCertNoFlag = VerifyCertNoFlag.value
        pReqTransfer.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pReqTransfer.TradeAmount = TradeAmount
        pReqTransfer.FutureFetchAmount = FutureFetchAmount
        pReqTransfer.FeePayFlag = FeePayFlag.value
        pReqTransfer.CustFee = CustFee
        pReqTransfer.BrokerFee = BrokerFee
        pReqTransfer.Message = bytes(Message, encoding='ascii')
        pReqTransfer.Digest = bytes(Digest, encoding='ascii')
        pReqTransfer.BankAccType = BankAccType.value
        pReqTransfer.DeviceID = bytes(DeviceID, encoding='ascii')
        pReqTransfer.BankSecuAccType = BankSecuAccType.value
        pReqTransfer.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
        pReqTransfer.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
        pReqTransfer.BankPwdFlag = BankPwdFlag.value
        pReqTransfer.SecuPwdFlag = SecuPwdFlag.value
        pReqTransfer.OperNo = bytes(OperNo, encoding='ascii')
        pReqTransfer.RequestID = RequestID
        pReqTransfer.TID = TID
        pReqTransfer.TransferStatus = TransferStatus.value
        pReqTransfer.LongCustomerName = bytes(LongCustomerName, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqFromFutureToBankByFuture(self.api, byref(pReqTransfer), self.nRequestID)

    def ReqQueryBankAccountMoneyByFuture(self, TradeCode: str = '', BankID: str = '', BankBranchID: str = '', BrokerID: str = '', BrokerBranchID: str = '', TradeDate: str = '', TradeTime: str = '', BankSerial: str = '', TradingDay: str = '', PlateSerial: int = 0, LastFragment: TThostFtdcLastFragmentType = list(TThostFtdcLastFragmentType)[0], SessionID: int = 0, CustomerName: str = '', IdCardType: TThostFtdcIdCardTypeType = list(TThostFtdcIdCardTypeType)[0], IdentifiedCardNo: str = '', CustType: TThostFtdcCustTypeType = list(TThostFtdcCustTypeType)[0], BankAccount: str = '', BankPassWord: str = '', AccountID: str = '', Password: str = '', FutureSerial: int = 0, InstallID: int = 0, UserID: str = '', VerifyCertNoFlag: TThostFtdcYesNoIndicatorType = list(TThostFtdcYesNoIndicatorType)[0], CurrencyID: str = '', Digest: str = '', BankAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], DeviceID: str = '', BankSecuAccType: TThostFtdcBankAccTypeType = list(TThostFtdcBankAccTypeType)[0], BrokerIDByBank: str = '', BankSecuAcc: str = '', BankPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], SecuPwdFlag: TThostFtdcPwdFlagType = list(TThostFtdcPwdFlagType)[0], OperNo: str = '', RequestID: int = 0, TID: int = 0, LongCustomerName: str = ''):
        pReqQueryAccount = CThostFtdcReqQueryAccountField()
        pReqQueryAccount.TradeCode = bytes(TradeCode, encoding='ascii')
        pReqQueryAccount.BankID = bytes(BankID, encoding='ascii')
        pReqQueryAccount.BankBranchID = bytes(BankBranchID, encoding='ascii')
        pReqQueryAccount.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqQueryAccount.BrokerBranchID = bytes(BrokerBranchID, encoding='ascii')
        pReqQueryAccount.TradeDate = bytes(TradeDate, encoding='ascii')
        pReqQueryAccount.TradeTime = bytes(TradeTime, encoding='ascii')
        pReqQueryAccount.BankSerial = bytes(BankSerial, encoding='ascii')
        pReqQueryAccount.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqQueryAccount.PlateSerial = PlateSerial
        pReqQueryAccount.LastFragment = LastFragment.value
        pReqQueryAccount.SessionID = SessionID
        pReqQueryAccount.CustomerName = bytes(CustomerName, encoding='ascii')
        pReqQueryAccount.IdCardType = IdCardType.value
        pReqQueryAccount.IdentifiedCardNo = bytes(IdentifiedCardNo, encoding='ascii')
        pReqQueryAccount.CustType = CustType.value
        pReqQueryAccount.BankAccount = bytes(BankAccount, encoding='ascii')
        pReqQueryAccount.BankPassWord = bytes(BankPassWord, encoding='ascii')
        pReqQueryAccount.AccountID = bytes(AccountID, encoding='ascii')
        pReqQueryAccount.Password = bytes(Password, encoding='ascii')
        pReqQueryAccount.FutureSerial = FutureSerial
        pReqQueryAccount.InstallID = InstallID
        pReqQueryAccount.UserID = bytes(UserID, encoding='ascii')
        pReqQueryAccount.VerifyCertNoFlag = VerifyCertNoFlag.value
        pReqQueryAccount.CurrencyID = bytes(CurrencyID, encoding='ascii')
        pReqQueryAccount.Digest = bytes(Digest, encoding='ascii')
        pReqQueryAccount.BankAccType = BankAccType.value
        pReqQueryAccount.DeviceID = bytes(DeviceID, encoding='ascii')
        pReqQueryAccount.BankSecuAccType = BankSecuAccType.value
        pReqQueryAccount.BrokerIDByBank = bytes(BrokerIDByBank, encoding='ascii')
        pReqQueryAccount.BankSecuAcc = bytes(BankSecuAcc, encoding='ascii')
        pReqQueryAccount.BankPwdFlag = BankPwdFlag.value
        pReqQueryAccount.SecuPwdFlag = SecuPwdFlag.value
        pReqQueryAccount.OperNo = bytes(OperNo, encoding='ascii')
        pReqQueryAccount.RequestID = RequestID
        pReqQueryAccount.TID = TID
        pReqQueryAccount.LongCustomerName = bytes(LongCustomerName, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQueryBankAccountMoneyByFuture(self.api, byref(pReqQueryAccount), self.nRequestID)

    def ReqQryClassifiedInstrument(self, InstrumentID: str = '', ExchangeID: str = '', ExchangeInstID: str = '', ProductID: str = '', TradingType: TThostFtdcTradingTypeType = list(TThostFtdcTradingTypeType)[0], ClassType: TThostFtdcClassTypeType = list(TThostFtdcClassTypeType)[0]):
        pQryClassifiedInstrument = CThostFtdcQryClassifiedInstrumentField()
        # pQryClassifiedInstrument.InstrumentID = bytes(InstrumentID, encoding='ascii')
        # pQryClassifiedInstrument.ExchangeID = bytes(ExchangeID, encoding='ascii')
        # pQryClassifiedInstrument.ExchangeInstID = bytes(ExchangeInstID, encoding='ascii')
        # pQryClassifiedInstrument.ProductID = bytes(ProductID, encoding='ascii')
        # pQryClassifiedInstrument.TradingType = TradingType.value
        # pQryClassifiedInstrument.ClassType = ClassType.value
        self.nRequestID += 1
        self.h.ReqQryClassifiedInstrument(self.api, byref(pQryClassifiedInstrument), self.nRequestID)

    def ReqQryCombPromotionParam(self, ExchangeID: str = '', InstrumentID: str = ''):
        pQryCombPromotionParam = CThostFtdcQryCombPromotionParamField()
        pQryCombPromotionParam.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryCombPromotionParam.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryCombPromotionParam(self.api, byref(pQryCombPromotionParam), self.nRequestID)

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

        self.h.SetOnRspAuthenticate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspAuthenticate.restype = None
        self.evOnRspAuthenticate = CFUNCTYPE(None, POINTER(CThostFtdcRspAuthenticateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspAuthenticate)
        self.h.SetOnRspAuthenticate(self.spi, self.evOnRspAuthenticate)

        self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogin.restype = None
        self.evOnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

        self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogout.restype = None
        self.evOnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

        self.h.SetOnRspUserPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserPasswordUpdate.restype = None
        self.evOnRspUserPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcUserPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserPasswordUpdate)
        self.h.SetOnRspUserPasswordUpdate(self.spi, self.evOnRspUserPasswordUpdate)

        self.h.SetOnRspTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspTradingAccountPasswordUpdate.restype = None
        self.evOnRspTradingAccountPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspTradingAccountPasswordUpdate)
        self.h.SetOnRspTradingAccountPasswordUpdate(self.spi, self.evOnRspTradingAccountPasswordUpdate)

        self.h.SetOnRspUserAuthMethod.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserAuthMethod.restype = None
        self.evOnRspUserAuthMethod = CFUNCTYPE(None, POINTER(CThostFtdcRspUserAuthMethodField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserAuthMethod)
        self.h.SetOnRspUserAuthMethod(self.spi, self.evOnRspUserAuthMethod)

        self.h.SetOnRspGenUserCaptcha.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspGenUserCaptcha.restype = None
        self.evOnRspGenUserCaptcha = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserCaptchaField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserCaptcha)
        self.h.SetOnRspGenUserCaptcha(self.spi, self.evOnRspGenUserCaptcha)

        self.h.SetOnRspGenUserText.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspGenUserText.restype = None
        self.evOnRspGenUserText = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserTextField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserText)
        self.h.SetOnRspGenUserText(self.spi, self.evOnRspGenUserText)

        self.h.SetOnRspOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOrderInsert.restype = None
        self.evOnRspOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderInsert)
        self.h.SetOnRspOrderInsert(self.spi, self.evOnRspOrderInsert)

        self.h.SetOnRspParkedOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspParkedOrderInsert.restype = None
        self.evOnRspParkedOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderInsert)
        self.h.SetOnRspParkedOrderInsert(self.spi, self.evOnRspParkedOrderInsert)

        self.h.SetOnRspParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspParkedOrderAction.restype = None
        self.evOnRspParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderAction)
        self.h.SetOnRspParkedOrderAction(self.spi, self.evOnRspParkedOrderAction)

        self.h.SetOnRspOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOrderAction.restype = None
        self.evOnRspOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderAction)
        self.h.SetOnRspOrderAction(self.spi, self.evOnRspOrderAction)

        self.h.SetOnRspQryMaxOrderVolume.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryMaxOrderVolume.restype = None
        self.evOnRspQryMaxOrderVolume = CFUNCTYPE(None, POINTER(CThostFtdcQryMaxOrderVolumeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMaxOrderVolume)
        self.h.SetOnRspQryMaxOrderVolume(self.spi, self.evOnRspQryMaxOrderVolume)

        self.h.SetOnRspSettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspSettlementInfoConfirm.restype = None
        self.evOnRspSettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSettlementInfoConfirm)
        self.h.SetOnRspSettlementInfoConfirm(self.spi, self.evOnRspSettlementInfoConfirm)

        self.h.SetOnRspRemoveParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspRemoveParkedOrder.restype = None
        self.evOnRspRemoveParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrder)
        self.h.SetOnRspRemoveParkedOrder(self.spi, self.evOnRspRemoveParkedOrder)

        self.h.SetOnRspRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspRemoveParkedOrderAction.restype = None
        self.evOnRspRemoveParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrderAction)
        self.h.SetOnRspRemoveParkedOrderAction(self.spi, self.evOnRspRemoveParkedOrderAction)

        self.h.SetOnRspExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspExecOrderInsert.restype = None
        self.evOnRspExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderInsert)
        self.h.SetOnRspExecOrderInsert(self.spi, self.evOnRspExecOrderInsert)

        self.h.SetOnRspExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspExecOrderAction.restype = None
        self.evOnRspExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderAction)
        self.h.SetOnRspExecOrderAction(self.spi, self.evOnRspExecOrderAction)

        self.h.SetOnRspForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspForQuoteInsert.restype = None
        self.evOnRspForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspForQuoteInsert)
        self.h.SetOnRspForQuoteInsert(self.spi, self.evOnRspForQuoteInsert)

        self.h.SetOnRspQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQuoteInsert.restype = None
        self.evOnRspQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteInsert)
        self.h.SetOnRspQuoteInsert(self.spi, self.evOnRspQuoteInsert)

        self.h.SetOnRspQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQuoteAction.restype = None
        self.evOnRspQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteAction)
        self.h.SetOnRspQuoteAction(self.spi, self.evOnRspQuoteAction)

        self.h.SetOnRspBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspBatchOrderAction.restype = None
        self.evOnRspBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputBatchOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspBatchOrderAction)
        self.h.SetOnRspBatchOrderAction(self.spi, self.evOnRspBatchOrderAction)

        self.h.SetOnRspOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOptionSelfCloseInsert.restype = None
        self.evOnRspOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseInsert)
        self.h.SetOnRspOptionSelfCloseInsert(self.spi, self.evOnRspOptionSelfCloseInsert)

        self.h.SetOnRspOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOptionSelfCloseAction.restype = None
        self.evOnRspOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseAction)
        self.h.SetOnRspOptionSelfCloseAction(self.spi, self.evOnRspOptionSelfCloseAction)

        self.h.SetOnRspCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspCombActionInsert.restype = None
        self.evOnRspCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspCombActionInsert)
        self.h.SetOnRspCombActionInsert(self.spi, self.evOnRspCombActionInsert)

        self.h.SetOnRspQryOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryOrder.restype = None
        self.evOnRspQryOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOrder)
        self.h.SetOnRspQryOrder(self.spi, self.evOnRspQryOrder)

        self.h.SetOnRspQryTrade.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTrade.restype = None
        self.evOnRspQryTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTrade)
        self.h.SetOnRspQryTrade(self.spi, self.evOnRspQryTrade)

        self.h.SetOnRspQryInvestorPosition.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorPosition.restype = None
        self.evOnRspQryInvestorPosition = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPosition)
        self.h.SetOnRspQryInvestorPosition(self.spi, self.evOnRspQryInvestorPosition)

        self.h.SetOnRspQryTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTradingAccount.restype = None
        self.evOnRspQryTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingAccount)
        self.h.SetOnRspQryTradingAccount(self.spi, self.evOnRspQryTradingAccount)

        self.h.SetOnRspQryInvestor.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestor.restype = None
        self.evOnRspQryInvestor = CFUNCTYPE(None, POINTER(CThostFtdcInvestorField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestor)
        self.h.SetOnRspQryInvestor(self.spi, self.evOnRspQryInvestor)

        self.h.SetOnRspQryTradingCode.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTradingCode.restype = None
        self.evOnRspQryTradingCode = CFUNCTYPE(None, POINTER(CThostFtdcTradingCodeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingCode)
        self.h.SetOnRspQryTradingCode(self.spi, self.evOnRspQryTradingCode)

        self.h.SetOnRspQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrumentMarginRate.restype = None
        self.evOnRspQryInstrumentMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentMarginRate)
        self.h.SetOnRspQryInstrumentMarginRate(self.spi, self.evOnRspQryInstrumentMarginRate)

        self.h.SetOnRspQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrumentCommissionRate.restype = None
        self.evOnRspQryInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentCommissionRate)
        self.h.SetOnRspQryInstrumentCommissionRate(self.spi, self.evOnRspQryInstrumentCommissionRate)

        self.h.SetOnRspQryExchange.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExchange.restype = None
        self.evOnRspQryExchange = CFUNCTYPE(None, POINTER(CThostFtdcExchangeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchange)
        self.h.SetOnRspQryExchange(self.spi, self.evOnRspQryExchange)

        self.h.SetOnRspQryProduct.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryProduct.restype = None
        self.evOnRspQryProduct = CFUNCTYPE(None, POINTER(CThostFtdcProductField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProduct)
        self.h.SetOnRspQryProduct(self.spi, self.evOnRspQryProduct)

        self.h.SetOnRspQryInstrument.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrument.restype = None
        self.evOnRspQryInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrument)
        self.h.SetOnRspQryInstrument(self.spi, self.evOnRspQryInstrument)

        self.h.SetOnRspQryDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryDepthMarketData.restype = None
        self.evOnRspQryDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryDepthMarketData)
        self.h.SetOnRspQryDepthMarketData(self.spi, self.evOnRspQryDepthMarketData)

        self.h.SetOnRspQrySettlementInfo.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySettlementInfo.restype = None
        self.evOnRspQrySettlementInfo = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfo)
        self.h.SetOnRspQrySettlementInfo(self.spi, self.evOnRspQrySettlementInfo)

        self.h.SetOnRspQryTransferBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTransferBank.restype = None
        self.evOnRspQryTransferBank = CFUNCTYPE(None, POINTER(CThostFtdcTransferBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferBank)
        self.h.SetOnRspQryTransferBank(self.spi, self.evOnRspQryTransferBank)

        self.h.SetOnRspQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorPositionDetail.restype = None
        self.evOnRspQryInvestorPositionDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionDetail)
        self.h.SetOnRspQryInvestorPositionDetail(self.spi, self.evOnRspQryInvestorPositionDetail)

        self.h.SetOnRspQryNotice.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryNotice.restype = None
        self.evOnRspQryNotice = CFUNCTYPE(None, POINTER(CThostFtdcNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryNotice)
        self.h.SetOnRspQryNotice(self.spi, self.evOnRspQryNotice)

        self.h.SetOnRspQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySettlementInfoConfirm.restype = None
        self.evOnRspQrySettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfoConfirm)
        self.h.SetOnRspQrySettlementInfoConfirm(self.spi, self.evOnRspQrySettlementInfoConfirm)

        self.h.SetOnRspQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorPositionCombineDetail.restype = None
        self.evOnRspQryInvestorPositionCombineDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionCombineDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionCombineDetail)
        self.h.SetOnRspQryInvestorPositionCombineDetail(self.spi, self.evOnRspQryInvestorPositionCombineDetail)

        self.h.SetOnRspQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryCFMMCTradingAccountKey.restype = None
        self.evOnRspQryCFMMCTradingAccountKey = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountKeyField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCFMMCTradingAccountKey)
        self.h.SetOnRspQryCFMMCTradingAccountKey(self.spi, self.evOnRspQryCFMMCTradingAccountKey)

        self.h.SetOnRspQryEWarrantOffset.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryEWarrantOffset.restype = None
        self.evOnRspQryEWarrantOffset = CFUNCTYPE(None, POINTER(CThostFtdcEWarrantOffsetField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryEWarrantOffset)
        self.h.SetOnRspQryEWarrantOffset(self.spi, self.evOnRspQryEWarrantOffset)

        self.h.SetOnRspQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorProductGroupMargin.restype = None
        self.evOnRspQryInvestorProductGroupMargin = CFUNCTYPE(None, POINTER(CThostFtdcInvestorProductGroupMarginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorProductGroupMargin)
        self.h.SetOnRspQryInvestorProductGroupMargin(self.spi, self.evOnRspQryInvestorProductGroupMargin)

        self.h.SetOnRspQryExchangeMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExchangeMarginRate.restype = None
        self.evOnRspQryExchangeMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRate)
        self.h.SetOnRspQryExchangeMarginRate(self.spi, self.evOnRspQryExchangeMarginRate)

        self.h.SetOnRspQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExchangeMarginRateAdjust.restype = None
        self.evOnRspQryExchangeMarginRateAdjust = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateAdjustField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRateAdjust)
        self.h.SetOnRspQryExchangeMarginRateAdjust(self.spi, self.evOnRspQryExchangeMarginRateAdjust)

        self.h.SetOnRspQryExchangeRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExchangeRate.restype = None
        self.evOnRspQryExchangeRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeRate)
        self.h.SetOnRspQryExchangeRate(self.spi, self.evOnRspQryExchangeRate)

        self.h.SetOnRspQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySecAgentACIDMap.restype = None
        self.evOnRspQrySecAgentACIDMap = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentACIDMapField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentACIDMap)
        self.h.SetOnRspQrySecAgentACIDMap(self.spi, self.evOnRspQrySecAgentACIDMap)

        self.h.SetOnRspQryProductExchRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryProductExchRate.restype = None
        self.evOnRspQryProductExchRate = CFUNCTYPE(None, POINTER(CThostFtdcProductExchRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductExchRate)
        self.h.SetOnRspQryProductExchRate(self.spi, self.evOnRspQryProductExchRate)

        self.h.SetOnRspQryProductGroup.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryProductGroup.restype = None
        self.evOnRspQryProductGroup = CFUNCTYPE(None, POINTER(CThostFtdcProductGroupField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductGroup)
        self.h.SetOnRspQryProductGroup(self.spi, self.evOnRspQryProductGroup)

        self.h.SetOnRspQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryMMInstrumentCommissionRate.restype = None
        self.evOnRspQryMMInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcMMInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMInstrumentCommissionRate)
        self.h.SetOnRspQryMMInstrumentCommissionRate(self.spi, self.evOnRspQryMMInstrumentCommissionRate)

        self.h.SetOnRspQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryMMOptionInstrCommRate.restype = None
        self.evOnRspQryMMOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcMMOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMOptionInstrCommRate)
        self.h.SetOnRspQryMMOptionInstrCommRate(self.spi, self.evOnRspQryMMOptionInstrCommRate)

        self.h.SetOnRspQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrumentOrderCommRate.restype = None
        self.evOnRspQryInstrumentOrderCommRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentOrderCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentOrderCommRate)
        self.h.SetOnRspQryInstrumentOrderCommRate(self.spi, self.evOnRspQryInstrumentOrderCommRate)

        self.h.SetOnRspQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySecAgentTradingAccount.restype = None
        self.evOnRspQrySecAgentTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradingAccount)
        self.h.SetOnRspQrySecAgentTradingAccount(self.spi, self.evOnRspQrySecAgentTradingAccount)

        self.h.SetOnRspQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySecAgentCheckMode.restype = None
        self.evOnRspQrySecAgentCheckMode = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentCheckModeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentCheckMode)
        self.h.SetOnRspQrySecAgentCheckMode(self.spi, self.evOnRspQrySecAgentCheckMode)

        self.h.SetOnRspQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySecAgentTradeInfo.restype = None
        self.evOnRspQrySecAgentTradeInfo = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentTradeInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradeInfo)
        self.h.SetOnRspQrySecAgentTradeInfo(self.spi, self.evOnRspQrySecAgentTradeInfo)

        self.h.SetOnRspQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryOptionInstrTradeCost.restype = None
        self.evOnRspQryOptionInstrTradeCost = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrTradeCostField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrTradeCost)
        self.h.SetOnRspQryOptionInstrTradeCost(self.spi, self.evOnRspQryOptionInstrTradeCost)

        self.h.SetOnRspQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryOptionInstrCommRate.restype = None
        self.evOnRspQryOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrCommRate)
        self.h.SetOnRspQryOptionInstrCommRate(self.spi, self.evOnRspQryOptionInstrCommRate)

        self.h.SetOnRspQryExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExecOrder.restype = None
        self.evOnRspQryExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExecOrder)
        self.h.SetOnRspQryExecOrder(self.spi, self.evOnRspQryExecOrder)

        self.h.SetOnRspQryForQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryForQuote.restype = None
        self.evOnRspQryForQuote = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryForQuote)
        self.h.SetOnRspQryForQuote(self.spi, self.evOnRspQryForQuote)

        self.h.SetOnRspQryQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryQuote.restype = None
        self.evOnRspQryQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryQuote)
        self.h.SetOnRspQryQuote(self.spi, self.evOnRspQryQuote)

        self.h.SetOnRspQryOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryOptionSelfClose.restype = None
        self.evOnRspQryOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionSelfClose)
        self.h.SetOnRspQryOptionSelfClose(self.spi, self.evOnRspQryOptionSelfClose)

        self.h.SetOnRspQryInvestUnit.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestUnit.restype = None
        self.evOnRspQryInvestUnit = CFUNCTYPE(None, POINTER(CThostFtdcInvestUnitField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestUnit)
        self.h.SetOnRspQryInvestUnit(self.spi, self.evOnRspQryInvestUnit)

        self.h.SetOnRspQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryCombInstrumentGuard.restype = None
        self.evOnRspQryCombInstrumentGuard = CFUNCTYPE(None, POINTER(CThostFtdcCombInstrumentGuardField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombInstrumentGuard)
        self.h.SetOnRspQryCombInstrumentGuard(self.spi, self.evOnRspQryCombInstrumentGuard)

        self.h.SetOnRspQryCombAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryCombAction.restype = None
        self.evOnRspQryCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombAction)
        self.h.SetOnRspQryCombAction(self.spi, self.evOnRspQryCombAction)

        self.h.SetOnRspQryTransferSerial.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTransferSerial.restype = None
        self.evOnRspQryTransferSerial = CFUNCTYPE(None, POINTER(CThostFtdcTransferSerialField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferSerial)
        self.h.SetOnRspQryTransferSerial(self.spi, self.evOnRspQryTransferSerial)

        self.h.SetOnRspQryAccountregister.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryAccountregister.restype = None
        self.evOnRspQryAccountregister = CFUNCTYPE(None, POINTER(CThostFtdcAccountregisterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryAccountregister)
        self.h.SetOnRspQryAccountregister(self.spi, self.evOnRspQryAccountregister)

        self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspError.restype = None
        self.evOnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.SetOnRspError(self.spi, self.evOnRspError)

        self.h.SetOnRtnOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnOrder.restype = None
        self.evOnRtnOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField))(self.__OnRtnOrder)
        self.h.SetOnRtnOrder(self.spi, self.evOnRtnOrder)

        self.h.SetOnRtnTrade.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnTrade.restype = None
        self.evOnRtnTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField))(self.__OnRtnTrade)
        self.h.SetOnRtnTrade(self.spi, self.evOnRtnTrade)

        self.h.SetOnErrRtnOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOrderInsert.restype = None
        self.evOnErrRtnOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderInsert)
        self.h.SetOnErrRtnOrderInsert(self.spi, self.evOnErrRtnOrderInsert)

        self.h.SetOnErrRtnOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOrderAction.restype = None
        self.evOnErrRtnOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderAction)
        self.h.SetOnErrRtnOrderAction(self.spi, self.evOnErrRtnOrderAction)

        self.h.SetOnRtnInstrumentStatus.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnInstrumentStatus.restype = None
        self.evOnRtnInstrumentStatus = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentStatusField))(self.__OnRtnInstrumentStatus)
        self.h.SetOnRtnInstrumentStatus(self.spi, self.evOnRtnInstrumentStatus)

        self.h.SetOnRtnBulletin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnBulletin.restype = None
        self.evOnRtnBulletin = CFUNCTYPE(None, POINTER(CThostFtdcBulletinField))(self.__OnRtnBulletin)
        self.h.SetOnRtnBulletin(self.spi, self.evOnRtnBulletin)

        self.h.SetOnRtnTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnTradingNotice.restype = None
        self.evOnRtnTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeInfoField))(self.__OnRtnTradingNotice)
        self.h.SetOnRtnTradingNotice(self.spi, self.evOnRtnTradingNotice)

        self.h.SetOnRtnErrorConditionalOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnErrorConditionalOrder.restype = None
        self.evOnRtnErrorConditionalOrder = CFUNCTYPE(None, POINTER(CThostFtdcErrorConditionalOrderField))(self.__OnRtnErrorConditionalOrder)
        self.h.SetOnRtnErrorConditionalOrder(self.spi, self.evOnRtnErrorConditionalOrder)

        self.h.SetOnRtnExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnExecOrder.restype = None
        self.evOnRtnExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField))(self.__OnRtnExecOrder)
        self.h.SetOnRtnExecOrder(self.spi, self.evOnRtnExecOrder)

        self.h.SetOnErrRtnExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnExecOrderInsert.restype = None
        self.evOnErrRtnExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderInsert)
        self.h.SetOnErrRtnExecOrderInsert(self.spi, self.evOnErrRtnExecOrderInsert)

        self.h.SetOnErrRtnExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnExecOrderAction.restype = None
        self.evOnErrRtnExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderAction)
        self.h.SetOnErrRtnExecOrderAction(self.spi, self.evOnErrRtnExecOrderAction)

        self.h.SetOnErrRtnForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnForQuoteInsert.restype = None
        self.evOnErrRtnForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnForQuoteInsert)
        self.h.SetOnErrRtnForQuoteInsert(self.spi, self.evOnErrRtnForQuoteInsert)

        self.h.SetOnRtnQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnQuote.restype = None
        self.evOnRtnQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField))(self.__OnRtnQuote)
        self.h.SetOnRtnQuote(self.spi, self.evOnRtnQuote)

        self.h.SetOnErrRtnQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnQuoteInsert.restype = None
        self.evOnErrRtnQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteInsert)
        self.h.SetOnErrRtnQuoteInsert(self.spi, self.evOnErrRtnQuoteInsert)

        self.h.SetOnErrRtnQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnQuoteAction.restype = None
        self.evOnErrRtnQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcQuoteActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteAction)
        self.h.SetOnErrRtnQuoteAction(self.spi, self.evOnErrRtnQuoteAction)

        self.h.SetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnForQuoteRsp.restype = None
        self.evOnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.SetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)

        self.h.SetOnRtnCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnCFMMCTradingAccountToken.restype = None
        self.evOnRtnCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountTokenField))(self.__OnRtnCFMMCTradingAccountToken)
        self.h.SetOnRtnCFMMCTradingAccountToken(self.spi, self.evOnRtnCFMMCTradingAccountToken)

        self.h.SetOnErrRtnBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnBatchOrderAction.restype = None
        self.evOnErrRtnBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcBatchOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBatchOrderAction)
        self.h.SetOnErrRtnBatchOrderAction(self.spi, self.evOnErrRtnBatchOrderAction)

        self.h.SetOnRtnOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnOptionSelfClose.restype = None
        self.evOnRtnOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField))(self.__OnRtnOptionSelfClose)
        self.h.SetOnRtnOptionSelfClose(self.spi, self.evOnRtnOptionSelfClose)

        self.h.SetOnErrRtnOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOptionSelfCloseInsert.restype = None
        self.evOnErrRtnOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseInsert)
        self.h.SetOnErrRtnOptionSelfCloseInsert(self.spi, self.evOnErrRtnOptionSelfCloseInsert)

        self.h.SetOnErrRtnOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOptionSelfCloseAction.restype = None
        self.evOnErrRtnOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseAction)
        self.h.SetOnErrRtnOptionSelfCloseAction(self.spi, self.evOnErrRtnOptionSelfCloseAction)

        self.h.SetOnRtnCombAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnCombAction.restype = None
        self.evOnRtnCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField))(self.__OnRtnCombAction)
        self.h.SetOnRtnCombAction(self.spi, self.evOnRtnCombAction)

        self.h.SetOnErrRtnCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnCombActionInsert.restype = None
        self.evOnErrRtnCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnCombActionInsert)
        self.h.SetOnErrRtnCombActionInsert(self.spi, self.evOnErrRtnCombActionInsert)

        self.h.SetOnRspQryContractBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryContractBank.restype = None
        self.evOnRspQryContractBank = CFUNCTYPE(None, POINTER(CThostFtdcContractBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryContractBank)
        self.h.SetOnRspQryContractBank(self.spi, self.evOnRspQryContractBank)

        self.h.SetOnRspQryParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryParkedOrder.restype = None
        self.evOnRspQryParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrder)
        self.h.SetOnRspQryParkedOrder(self.spi, self.evOnRspQryParkedOrder)

        self.h.SetOnRspQryParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryParkedOrderAction.restype = None
        self.evOnRspQryParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrderAction)
        self.h.SetOnRspQryParkedOrderAction(self.spi, self.evOnRspQryParkedOrderAction)

        self.h.SetOnRspQryTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTradingNotice.restype = None
        self.evOnRspQryTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingNotice)
        self.h.SetOnRspQryTradingNotice(self.spi, self.evOnRspQryTradingNotice)

        self.h.SetOnRspQryBrokerTradingParams.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryBrokerTradingParams.restype = None
        self.evOnRspQryBrokerTradingParams = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingParamsField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingParams)
        self.h.SetOnRspQryBrokerTradingParams(self.spi, self.evOnRspQryBrokerTradingParams)

        self.h.SetOnRspQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryBrokerTradingAlgos.restype = None
        self.evOnRspQryBrokerTradingAlgos = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingAlgosField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingAlgos)
        self.h.SetOnRspQryBrokerTradingAlgos(self.spi, self.evOnRspQryBrokerTradingAlgos)

        self.h.SetOnRspQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQueryCFMMCTradingAccountToken.restype = None
        self.evOnRspQueryCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryCFMMCTradingAccountToken)
        self.h.SetOnRspQueryCFMMCTradingAccountToken(self.spi, self.evOnRspQueryCFMMCTradingAccountToken)

        self.h.SetOnRtnFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnFromBankToFutureByBank.restype = None
        self.evOnRtnFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByBank)
        self.h.SetOnRtnFromBankToFutureByBank(self.spi, self.evOnRtnFromBankToFutureByBank)

        self.h.SetOnRtnFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnFromFutureToBankByBank.restype = None
        self.evOnRtnFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByBank)
        self.h.SetOnRtnFromFutureToBankByBank(self.spi, self.evOnRtnFromFutureToBankByBank)

        self.h.SetOnRtnRepealFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromBankToFutureByBank.restype = None
        self.evOnRtnRepealFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByBank)
        self.h.SetOnRtnRepealFromBankToFutureByBank(self.spi, self.evOnRtnRepealFromBankToFutureByBank)

        self.h.SetOnRtnRepealFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromFutureToBankByBank.restype = None
        self.evOnRtnRepealFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByBank)
        self.h.SetOnRtnRepealFromFutureToBankByBank(self.spi, self.evOnRtnRepealFromFutureToBankByBank)

        self.h.SetOnRtnFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnFromBankToFutureByFuture.restype = None
        self.evOnRtnFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByFuture)
        self.h.SetOnRtnFromBankToFutureByFuture(self.spi, self.evOnRtnFromBankToFutureByFuture)

        self.h.SetOnRtnFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnFromFutureToBankByFuture.restype = None
        self.evOnRtnFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByFuture)
        self.h.SetOnRtnFromFutureToBankByFuture(self.spi, self.evOnRtnFromFutureToBankByFuture)

        self.h.SetOnRtnRepealFromBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromBankToFutureByFutureManual.restype = None
        self.evOnRtnRepealFromBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFutureManual)
        self.h.SetOnRtnRepealFromBankToFutureByFutureManual(self.spi, self.evOnRtnRepealFromBankToFutureByFutureManual)

        self.h.SetOnRtnRepealFromFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromFutureToBankByFutureManual.restype = None
        self.evOnRtnRepealFromFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFutureManual)
        self.h.SetOnRtnRepealFromFutureToBankByFutureManual(self.spi, self.evOnRtnRepealFromFutureToBankByFutureManual)

        self.h.SetOnRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnQueryBankBalanceByFuture.restype = None
        self.evOnRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcNotifyQueryAccountField))(self.__OnRtnQueryBankBalanceByFuture)
        self.h.SetOnRtnQueryBankBalanceByFuture(self.spi, self.evOnRtnQueryBankBalanceByFuture)

        self.h.SetOnErrRtnBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnBankToFutureByFuture.restype = None
        self.evOnErrRtnBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBankToFutureByFuture)
        self.h.SetOnErrRtnBankToFutureByFuture(self.spi, self.evOnErrRtnBankToFutureByFuture)

        self.h.SetOnErrRtnFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnFutureToBankByFuture.restype = None
        self.evOnErrRtnFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnFutureToBankByFuture)
        self.h.SetOnErrRtnFutureToBankByFuture(self.spi, self.evOnErrRtnFutureToBankByFuture)

        self.h.SetOnErrRtnRepealBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnRepealBankToFutureByFutureManual.restype = None
        self.evOnErrRtnRepealBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealBankToFutureByFutureManual)
        self.h.SetOnErrRtnRepealBankToFutureByFutureManual(self.spi, self.evOnErrRtnRepealBankToFutureByFutureManual)

        self.h.SetOnErrRtnRepealFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnRepealFutureToBankByFutureManual.restype = None
        self.evOnErrRtnRepealFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealFutureToBankByFutureManual)
        self.h.SetOnErrRtnRepealFutureToBankByFutureManual(self.spi, self.evOnErrRtnRepealFutureToBankByFutureManual)

        self.h.SetOnErrRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnQueryBankBalanceByFuture.restype = None
        self.evOnErrRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQueryBankBalanceByFuture)
        self.h.SetOnErrRtnQueryBankBalanceByFuture(self.spi, self.evOnErrRtnQueryBankBalanceByFuture)

        self.h.SetOnRtnRepealFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromBankToFutureByFuture.restype = None
        self.evOnRtnRepealFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFuture)
        self.h.SetOnRtnRepealFromBankToFutureByFuture(self.spi, self.evOnRtnRepealFromBankToFutureByFuture)

        self.h.SetOnRtnRepealFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnRepealFromFutureToBankByFuture.restype = None
        self.evOnRtnRepealFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFuture)
        self.h.SetOnRtnRepealFromFutureToBankByFuture(self.spi, self.evOnRtnRepealFromFutureToBankByFuture)

        self.h.SetOnRspFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspFromBankToFutureByFuture.restype = None
        self.evOnRspFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromBankToFutureByFuture)
        self.h.SetOnRspFromBankToFutureByFuture(self.spi, self.evOnRspFromBankToFutureByFuture)

        self.h.SetOnRspFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspFromFutureToBankByFuture.restype = None
        self.evOnRspFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromFutureToBankByFuture)
        self.h.SetOnRspFromFutureToBankByFuture(self.spi, self.evOnRspFromFutureToBankByFuture)

        self.h.SetOnRspQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQueryBankAccountMoneyByFuture.restype = None
        self.evOnRspQueryBankAccountMoneyByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryBankAccountMoneyByFuture)
        self.h.SetOnRspQueryBankAccountMoneyByFuture(self.spi, self.evOnRspQueryBankAccountMoneyByFuture)

        self.h.SetOnRtnOpenAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnOpenAccountByBank.restype = None
        self.evOnRtnOpenAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcOpenAccountField))(self.__OnRtnOpenAccountByBank)
        self.h.SetOnRtnOpenAccountByBank(self.spi, self.evOnRtnOpenAccountByBank)

        self.h.SetOnRtnCancelAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnCancelAccountByBank.restype = None
        self.evOnRtnCancelAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcCancelAccountField))(self.__OnRtnCancelAccountByBank)
        self.h.SetOnRtnCancelAccountByBank(self.spi, self.evOnRtnCancelAccountByBank)

        self.h.SetOnRtnChangeAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnChangeAccountByBank.restype = None
        self.evOnRtnChangeAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcChangeAccountField))(self.__OnRtnChangeAccountByBank)
        self.h.SetOnRtnChangeAccountByBank(self.spi, self.evOnRtnChangeAccountByBank)

        self.h.SetOnRspQryClassifiedInstrument.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryClassifiedInstrument.restype = None
        self.evOnRspQryClassifiedInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryClassifiedInstrument)
        self.h.SetOnRspQryClassifiedInstrument(self.spi, self.evOnRspQryClassifiedInstrument)

        self.h.SetOnRspQryCombPromotionParam.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryCombPromotionParam.restype = None
        self.evOnRspQryCombPromotionParam = CFUNCTYPE(None, POINTER(CThostFtdcCombPromotionParamField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombPromotionParam)
        self.h.SetOnRspQryCombPromotionParam(self.spi, self.evOnRspQryCombPromotionParam)

    def __OnFrontConnected(self):
        self.OnFrontConnected()

    def __OnFrontDisconnected(self, nReason):
        self.OnFrontDisconnected(nReason)

    def __OnHeartBeatWarning(self, nTimeLapse):
        self.OnHeartBeatWarning(nTimeLapse)

    def __OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast):
        self.OnRspAuthenticate(copy.deepcopy(POINTER(CThostFtdcRspAuthenticateField).from_param(pRspAuthenticateField).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcUserPasswordUpdateField).from_param(pUserPasswordUpdate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.OnRspTradingAccountPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcTradingAccountPasswordUpdateField).from_param(pTradingAccountPasswordUpdate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserAuthMethod(self, pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserAuthMethod(copy.deepcopy(POINTER(CThostFtdcRspUserAuthMethodField).from_param(pRspUserAuthMethod).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspGenUserCaptcha(self, pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast):
        self.OnRspGenUserCaptcha(copy.deepcopy(POINTER(CThostFtdcRspGenUserCaptchaField).from_param(pRspGenUserCaptcha).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspGenUserText(self, pRspGenUserText, pRspInfo, nRequestID, bIsLast):
        self.OnRspGenUserText(copy.deepcopy(POINTER(CThostFtdcRspGenUserTextField).from_param(pRspGenUserText).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspParkedOrderInsert(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspOrderAction(copy.deepcopy(POINTER(CThostFtdcInputOrderActionField).from_param(pInputOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryMaxOrderVolume(copy.deepcopy(POINTER(CThostFtdcQryMaxOrderVolumeField).from_param(pQryMaxOrderVolume).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.OnRspSettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspRemoveParkedOrder(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderField).from_param(pRemoveParkedOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspRemoveParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderActionField).from_param(pRemoveParkedOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspExecOrderAction(copy.deepcopy(POINTER(CThostFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspQuoteAction(copy.deepcopy(POINTER(CThostFtdcInputQuoteActionField).from_param(pInputQuoteAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspBatchOrderAction(self, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcInputBatchOrderActionField).from_param(pInputBatchOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast):
        self.OnRspOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseActionField).from_param(pInputOptionSelfCloseAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorPosition(copy.deepcopy(POINTER(CThostFtdcInvestorPositionField).from_param(pInvestorPosition).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestor(copy.deepcopy(POINTER(CThostFtdcInvestorField).from_param(pInvestor).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTradingCode(copy.deepcopy(POINTER(CThostFtdcTradingCodeField).from_param(pTradingCode).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrumentMarginRate(copy.deepcopy(POINTER(CThostFtdcInstrumentMarginRateField).from_param(pInstrumentMarginRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcInstrumentCommissionRateField).from_param(pInstrumentCommissionRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExchange(copy.deepcopy(POINTER(CThostFtdcExchangeField).from_param(pExchange).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryProduct(copy.deepcopy(POINTER(CThostFtdcProductField).from_param(pProduct).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySettlementInfo(copy.deepcopy(POINTER(CThostFtdcSettlementInfoField).from_param(pSettlementInfo).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTransferBank(copy.deepcopy(POINTER(CThostFtdcTransferBankField).from_param(pTransferBank).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorPositionDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionDetailField).from_param(pInvestorPositionDetail).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryNotice(copy.deepcopy(POINTER(CThostFtdcNoticeField).from_param(pNotice).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorPositionCombineDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionCombineDetailField).from_param(pInvestorPositionCombineDetail).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryCFMMCTradingAccountKey(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountKeyField).from_param(pCFMMCTradingAccountKey).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryEWarrantOffset(copy.deepcopy(POINTER(CThostFtdcEWarrantOffsetField).from_param(pEWarrantOffset).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorProductGroupMargin(copy.deepcopy(POINTER(CThostFtdcInvestorProductGroupMarginField).from_param(pInvestorProductGroupMargin).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExchangeMarginRate(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateField).from_param(pExchangeMarginRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExchangeMarginRateAdjust(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateAdjustField).from_param(pExchangeMarginRateAdjust).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExchangeRate(copy.deepcopy(POINTER(CThostFtdcExchangeRateField).from_param(pExchangeRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySecAgentACIDMap(copy.deepcopy(POINTER(CThostFtdcSecAgentACIDMapField).from_param(pSecAgentACIDMap).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryProductExchRate(copy.deepcopy(POINTER(CThostFtdcProductExchRateField).from_param(pProductExchRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryProductGroup(self, pProductGroup, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryProductGroup(copy.deepcopy(POINTER(CThostFtdcProductGroupField).from_param(pProductGroup).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryMMInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcMMInstrumentCommissionRateField).from_param(pMMInstrumentCommissionRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryMMOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcMMOptionInstrCommRateField).from_param(pMMOptionInstrCommRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrumentOrderCommRate(copy.deepcopy(POINTER(CThostFtdcInstrumentOrderCommRateField).from_param(pInstrumentOrderCommRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySecAgentTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySecAgentTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySecAgentCheckMode(copy.deepcopy(POINTER(CThostFtdcSecAgentCheckModeField).from_param(pSecAgentCheckMode).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySecAgentTradeInfo(copy.deepcopy(POINTER(CThostFtdcSecAgentTradeInfoField).from_param(pSecAgentTradeInfo).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryOptionInstrTradeCost(copy.deepcopy(POINTER(CThostFtdcOptionInstrTradeCostField).from_param(pOptionInstrTradeCost).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcOptionInstrCommRateField).from_param(pOptionInstrCommRate).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryForQuote(copy.deepcopy(POINTER(CThostFtdcForQuoteField).from_param(pForQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryOptionSelfClose(self, pOptionSelfClose, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestUnit(self, pInvestUnit, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestUnit(copy.deepcopy(POINTER(CThostFtdcInvestUnitField).from_param(pInvestUnit).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryCombInstrumentGuard(copy.deepcopy(POINTER(CThostFtdcCombInstrumentGuardField).from_param(pCombInstrumentGuard).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTransferSerial(copy.deepcopy(POINTER(CThostFtdcTransferSerialField).from_param(pTransferSerial).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryAccountregister(copy.deepcopy(POINTER(CThostFtdcAccountregisterField).from_param(pAccountregister).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnOrder(self, pOrder):
        self.OnRtnOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents))

    def __OnRtnTrade(self, pTrade):
        self.OnRtnTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents))

    def __OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        self.OnErrRtnOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        self.OnErrRtnOrderAction(copy.deepcopy(POINTER(CThostFtdcOrderActionField).from_param(pOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnInstrumentStatus(self, pInstrumentStatus):
        self.OnRtnInstrumentStatus(copy.deepcopy(POINTER(CThostFtdcInstrumentStatusField).from_param(pInstrumentStatus).contents))

    def __OnRtnBulletin(self, pBulletin):
        self.OnRtnBulletin(copy.deepcopy(POINTER(CThostFtdcBulletinField).from_param(pBulletin).contents))

    def __OnRtnTradingNotice(self, pTradingNoticeInfo):
        self.OnRtnTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeInfoField).from_param(pTradingNoticeInfo).contents))

    def __OnRtnErrorConditionalOrder(self, pErrorConditionalOrder):
        self.OnRtnErrorConditionalOrder(copy.deepcopy(POINTER(CThostFtdcErrorConditionalOrderField).from_param(pErrorConditionalOrder).contents))

    def __OnRtnExecOrder(self, pExecOrder):
        self.OnRtnExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents))

    def __OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo):
        self.OnErrRtnExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo):
        self.OnErrRtnExecOrderAction(copy.deepcopy(POINTER(CThostFtdcExecOrderActionField).from_param(pExecOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo):
        self.OnErrRtnForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnQuote(self, pQuote):
        self.OnRtnQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents))

    def __OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo):
        self.OnErrRtnQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo):
        self.OnErrRtnQuoteAction(copy.deepcopy(POINTER(CThostFtdcQuoteActionField).from_param(pQuoteAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnForQuoteRsp(self, pForQuoteRsp):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents))

    def __OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken):
        self.OnRtnCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountTokenField).from_param(pCFMMCTradingAccountToken).contents))

    def __OnErrRtnBatchOrderAction(self, pBatchOrderAction, pRspInfo):
        self.OnErrRtnBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcBatchOrderActionField).from_param(pBatchOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnOptionSelfClose(self, pOptionSelfClose):
        self.OnRtnOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents))

    def __OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo):
        self.OnErrRtnOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction, pRspInfo):
        self.OnErrRtnOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseActionField).from_param(pOptionSelfCloseAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnCombAction(self, pCombAction):
        self.OnRtnCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents))

    def __OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo):
        self.OnErrRtnCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryContractBank(copy.deepcopy(POINTER(CThostFtdcContractBankField).from_param(pContractBank).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryParkedOrder(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeField).from_param(pTradingNotice).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryBrokerTradingParams(copy.deepcopy(POINTER(CThostFtdcBrokerTradingParamsField).from_param(pBrokerTradingParams).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryBrokerTradingAlgos(copy.deepcopy(POINTER(CThostFtdcBrokerTradingAlgosField).from_param(pBrokerTradingAlgos).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast):
        self.OnRspQueryCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField).from_param(pQueryCFMMCTradingAccountToken).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnFromBankToFutureByBank(self, pRspTransfer):
        self.OnRtnFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents))

    def __OnRtnFromFutureToBankByBank(self, pRspTransfer):
        self.OnRtnFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents))

    def __OnRtnRepealFromBankToFutureByBank(self, pRspRepeal):
        self.OnRtnRepealFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRtnRepealFromFutureToBankByBank(self, pRspRepeal):
        self.OnRtnRepealFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRtnFromBankToFutureByFuture(self, pRspTransfer):
        self.OnRtnFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents))

    def __OnRtnFromFutureToBankByFuture(self, pRspTransfer):
        self.OnRtnFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents))

    def __OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal):
        self.OnRtnRepealFromBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal):
        self.OnRtnRepealFromFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount):
        self.OnRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcNotifyQueryAccountField).from_param(pNotifyQueryAccount).contents))

    def __OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo):
        self.OnErrRtnBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo):
        self.OnErrRtnFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo):
        self.OnErrRtnRepealBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo):
        self.OnErrRtnRepealFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo):
        self.OnErrRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal):
        self.OnRtnRepealFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal):
        self.OnRtnRepealFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents))

    def __OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.OnRspFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast):
        self.OnRspFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast):
        self.OnRspQueryBankAccountMoneyByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnOpenAccountByBank(self, pOpenAccount):
        self.OnRtnOpenAccountByBank(copy.deepcopy(POINTER(CThostFtdcOpenAccountField).from_param(pOpenAccount).contents))

    def __OnRtnCancelAccountByBank(self, pCancelAccount):
        self.OnRtnCancelAccountByBank(copy.deepcopy(POINTER(CThostFtdcCancelAccountField).from_param(pCancelAccount).contents))

    def __OnRtnChangeAccountByBank(self, pChangeAccount):
        self.OnRtnChangeAccountByBank(copy.deepcopy(POINTER(CThostFtdcChangeAccountField).from_param(pChangeAccount).contents))

    def __OnRspQryClassifiedInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryClassifiedInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryCombPromotionParam(self, pCombPromotionParam, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryCombPromotionParam(copy.deepcopy(POINTER(CThostFtdcCombPromotionParamField).from_param(pCombPromotionParam).contents), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def OnFrontConnected(self, ):
        print('===OnFrontConnected===: ')

    def OnFrontDisconnected(self, nReason: int):
        print('===OnFrontDisconnected===: nReason: int')

    def OnHeartBeatWarning(self, nTimeLapse: int):
        print('===OnHeartBeatWarning===: nTimeLapse: int')

    def OnRspAuthenticate(self, pRspAuthenticateField: CThostFtdcRspAuthenticateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspAuthenticate===: pRspAuthenticateField: CThostFtdcRspAuthenticateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogin===: pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserLogout(self, pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogout===: pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate: CThostFtdcUserPasswordUpdateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserPasswordUpdate===: pUserPasswordUpdate: CThostFtdcUserPasswordUpdateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate: CThostFtdcTradingAccountPasswordUpdateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspTradingAccountPasswordUpdate===: pTradingAccountPasswordUpdate: CThostFtdcTradingAccountPasswordUpdateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserAuthMethod(self, pRspUserAuthMethod: CThostFtdcRspUserAuthMethodField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserAuthMethod===: pRspUserAuthMethod: CThostFtdcRspUserAuthMethodField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha: CThostFtdcRspGenUserCaptchaField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspGenUserCaptcha===: pRspGenUserCaptcha: CThostFtdcRspGenUserCaptchaField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspGenUserText(self, pRspGenUserText: CThostFtdcRspGenUserTextField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspGenUserText===: pRspGenUserText: CThostFtdcRspGenUserTextField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOrderInsert(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOrderInsert===: pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspParkedOrderInsert(self, pParkedOrder: CThostFtdcParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspParkedOrderInsert===: pParkedOrder: CThostFtdcParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspParkedOrderAction(self, pParkedOrderAction: CThostFtdcParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspParkedOrderAction===: pParkedOrderAction: CThostFtdcParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOrderAction(self, pInputOrderAction: CThostFtdcInputOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOrderAction===: pInputOrderAction: CThostFtdcInputOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume: CThostFtdcQryMaxOrderVolumeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryMaxOrderVolume===: pQryMaxOrderVolume: CThostFtdcQryMaxOrderVolumeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspSettlementInfoConfirm===: pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder: CThostFtdcRemoveParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspRemoveParkedOrder===: pRemoveParkedOrder: CThostFtdcRemoveParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction: CThostFtdcRemoveParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspRemoveParkedOrderAction===: pRemoveParkedOrderAction: CThostFtdcRemoveParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspExecOrderInsert(self, pInputExecOrder: CThostFtdcInputExecOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspExecOrderInsert===: pInputExecOrder: CThostFtdcInputExecOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspExecOrderAction(self, pInputExecOrderAction: CThostFtdcInputExecOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspExecOrderAction===: pInputExecOrderAction: CThostFtdcInputExecOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspForQuoteInsert(self, pInputForQuote: CThostFtdcInputForQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspForQuoteInsert===: pInputForQuote: CThostFtdcInputForQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQuoteInsert(self, pInputQuote: CThostFtdcInputQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQuoteInsert===: pInputQuote: CThostFtdcInputQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQuoteAction(self, pInputQuoteAction: CThostFtdcInputQuoteActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQuoteAction===: pInputQuoteAction: CThostFtdcInputQuoteActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspBatchOrderAction(self, pInputBatchOrderAction: CThostFtdcInputBatchOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspBatchOrderAction===: pInputBatchOrderAction: CThostFtdcInputBatchOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose: CThostFtdcInputOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOptionSelfCloseInsert===: pInputOptionSelfClose: CThostFtdcInputOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction: CThostFtdcInputOptionSelfCloseActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOptionSelfCloseAction===: pInputOptionSelfCloseAction: CThostFtdcInputOptionSelfCloseActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspCombActionInsert(self, pInputCombAction: CThostFtdcInputCombActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspCombActionInsert===: pInputCombAction: CThostFtdcInputCombActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryOrder(self, pOrder: CThostFtdcOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryOrder===: pOrder: CThostFtdcOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTrade(self, pTrade: CThostFtdcTradeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTrade===: pTrade: CThostFtdcTradeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorPosition(self, pInvestorPosition: CThostFtdcInvestorPositionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorPosition===: pInvestorPosition: CThostFtdcInvestorPositionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTradingAccount(self, pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTradingAccount===: pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestor(self, pInvestor: CThostFtdcInvestorField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestor===: pInvestor: CThostFtdcInvestorField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTradingCode(self, pTradingCode: CThostFtdcTradingCodeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTradingCode===: pTradingCode: CThostFtdcTradingCodeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate: CThostFtdcInstrumentMarginRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrumentMarginRate===: pInstrumentMarginRate: CThostFtdcInstrumentMarginRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate: CThostFtdcInstrumentCommissionRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrumentCommissionRate===: pInstrumentCommissionRate: CThostFtdcInstrumentCommissionRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExchange(self, pExchange: CThostFtdcExchangeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExchange===: pExchange: CThostFtdcExchangeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryProduct(self, pProduct: CThostFtdcProductField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryProduct===: pProduct: CThostFtdcProductField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrument(self, pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrument===: pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryDepthMarketData===: pDepthMarketData: CThostFtdcDepthMarketDataField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySettlementInfo(self, pSettlementInfo: CThostFtdcSettlementInfoField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySettlementInfo===: pSettlementInfo: CThostFtdcSettlementInfoField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTransferBank(self, pTransferBank: CThostFtdcTransferBankField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTransferBank===: pTransferBank: CThostFtdcTransferBankField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail: CThostFtdcInvestorPositionDetailField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorPositionDetail===: pInvestorPositionDetail: CThostFtdcInvestorPositionDetailField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryNotice(self, pNotice: CThostFtdcNoticeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryNotice===: pNotice: CThostFtdcNoticeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySettlementInfoConfirm===: pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail: CThostFtdcInvestorPositionCombineDetailField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorPositionCombineDetail===: pInvestorPositionCombineDetail: CThostFtdcInvestorPositionCombineDetailField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey: CThostFtdcCFMMCTradingAccountKeyField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryCFMMCTradingAccountKey===: pCFMMCTradingAccountKey: CThostFtdcCFMMCTradingAccountKeyField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryEWarrantOffset(self, pEWarrantOffset: CThostFtdcEWarrantOffsetField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryEWarrantOffset===: pEWarrantOffset: CThostFtdcEWarrantOffsetField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin: CThostFtdcInvestorProductGroupMarginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorProductGroupMargin===: pInvestorProductGroupMargin: CThostFtdcInvestorProductGroupMarginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate: CThostFtdcExchangeMarginRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExchangeMarginRate===: pExchangeMarginRate: CThostFtdcExchangeMarginRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust: CThostFtdcExchangeMarginRateAdjustField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExchangeMarginRateAdjust===: pExchangeMarginRateAdjust: CThostFtdcExchangeMarginRateAdjustField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExchangeRate(self, pExchangeRate: CThostFtdcExchangeRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExchangeRate===: pExchangeRate: CThostFtdcExchangeRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap: CThostFtdcSecAgentACIDMapField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySecAgentACIDMap===: pSecAgentACIDMap: CThostFtdcSecAgentACIDMapField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryProductExchRate(self, pProductExchRate: CThostFtdcProductExchRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryProductExchRate===: pProductExchRate: CThostFtdcProductExchRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryProductGroup(self, pProductGroup: CThostFtdcProductGroupField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryProductGroup===: pProductGroup: CThostFtdcProductGroupField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate: CThostFtdcMMInstrumentCommissionRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryMMInstrumentCommissionRate===: pMMInstrumentCommissionRate: CThostFtdcMMInstrumentCommissionRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate: CThostFtdcMMOptionInstrCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryMMOptionInstrCommRate===: pMMOptionInstrCommRate: CThostFtdcMMOptionInstrCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate: CThostFtdcInstrumentOrderCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrumentOrderCommRate===: pInstrumentOrderCommRate: CThostFtdcInstrumentOrderCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySecAgentTradingAccount(self, pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySecAgentTradingAccount===: pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode: CThostFtdcSecAgentCheckModeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySecAgentCheckMode===: pSecAgentCheckMode: CThostFtdcSecAgentCheckModeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo: CThostFtdcSecAgentTradeInfoField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySecAgentTradeInfo===: pSecAgentTradeInfo: CThostFtdcSecAgentTradeInfoField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost: CThostFtdcOptionInstrTradeCostField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryOptionInstrTradeCost===: pOptionInstrTradeCost: CThostFtdcOptionInstrTradeCostField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate: CThostFtdcOptionInstrCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryOptionInstrCommRate===: pOptionInstrCommRate: CThostFtdcOptionInstrCommRateField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExecOrder(self, pExecOrder: CThostFtdcExecOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExecOrder===: pExecOrder: CThostFtdcExecOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryForQuote(self, pForQuote: CThostFtdcForQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryForQuote===: pForQuote: CThostFtdcForQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryQuote(self, pQuote: CThostFtdcQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryQuote===: pQuote: CThostFtdcQuoteField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryOptionSelfClose(self, pOptionSelfClose: CThostFtdcOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryOptionSelfClose===: pOptionSelfClose: CThostFtdcOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestUnit(self, pInvestUnit: CThostFtdcInvestUnitField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestUnit===: pInvestUnit: CThostFtdcInvestUnitField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard: CThostFtdcCombInstrumentGuardField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryCombInstrumentGuard===: pCombInstrumentGuard: CThostFtdcCombInstrumentGuardField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryCombAction(self, pCombAction: CThostFtdcCombActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryCombAction===: pCombAction: CThostFtdcCombActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTransferSerial(self, pTransferSerial: CThostFtdcTransferSerialField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTransferSerial===: pTransferSerial: CThostFtdcTransferSerialField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryAccountregister(self, pAccountregister: CThostFtdcAccountregisterField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryAccountregister===: pAccountregister: CThostFtdcAccountregisterField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspError(self, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspError===: pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnOrder(self, pOrder: CThostFtdcOrderField):
        print('===OnRtnOrder===: pOrder: CThostFtdcOrderField')

    def OnRtnTrade(self, pTrade: CThostFtdcTradeField):
        print('===OnRtnTrade===: pTrade: CThostFtdcTradeField')

    def OnErrRtnOrderInsert(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnOrderInsert===: pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnOrderAction(self, pOrderAction: CThostFtdcOrderActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnOrderAction===: pOrderAction: CThostFtdcOrderActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnInstrumentStatus(self, pInstrumentStatus: CThostFtdcInstrumentStatusField):
        print('===OnRtnInstrumentStatus===: pInstrumentStatus: CThostFtdcInstrumentStatusField')

    def OnRtnBulletin(self, pBulletin: CThostFtdcBulletinField):
        print('===OnRtnBulletin===: pBulletin: CThostFtdcBulletinField')

    def OnRtnTradingNotice(self, pTradingNoticeInfo: CThostFtdcTradingNoticeInfoField):
        print('===OnRtnTradingNotice===: pTradingNoticeInfo: CThostFtdcTradingNoticeInfoField')

    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder: CThostFtdcErrorConditionalOrderField):
        print('===OnRtnErrorConditionalOrder===: pErrorConditionalOrder: CThostFtdcErrorConditionalOrderField')

    def OnRtnExecOrder(self, pExecOrder: CThostFtdcExecOrderField):
        print('===OnRtnExecOrder===: pExecOrder: CThostFtdcExecOrderField')

    def OnErrRtnExecOrderInsert(self, pInputExecOrder: CThostFtdcInputExecOrderField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnExecOrderInsert===: pInputExecOrder: CThostFtdcInputExecOrderField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnExecOrderAction(self, pExecOrderAction: CThostFtdcExecOrderActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnExecOrderAction===: pExecOrderAction: CThostFtdcExecOrderActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnForQuoteInsert(self, pInputForQuote: CThostFtdcInputForQuoteField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnForQuoteInsert===: pInputForQuote: CThostFtdcInputForQuoteField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnQuote(self, pQuote: CThostFtdcQuoteField):
        print('===OnRtnQuote===: pQuote: CThostFtdcQuoteField')

    def OnErrRtnQuoteInsert(self, pInputQuote: CThostFtdcInputQuoteField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnQuoteInsert===: pInputQuote: CThostFtdcInputQuoteField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnQuoteAction(self, pQuoteAction: CThostFtdcQuoteActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnQuoteAction===: pQuoteAction: CThostFtdcQuoteActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnForQuoteRsp(self, pForQuoteRsp: CThostFtdcForQuoteRspField):
        print('===OnRtnForQuoteRsp===: pForQuoteRsp: CThostFtdcForQuoteRspField')

    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken: CThostFtdcCFMMCTradingAccountTokenField):
        print('===OnRtnCFMMCTradingAccountToken===: pCFMMCTradingAccountToken: CThostFtdcCFMMCTradingAccountTokenField')

    def OnErrRtnBatchOrderAction(self, pBatchOrderAction: CThostFtdcBatchOrderActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnBatchOrderAction===: pBatchOrderAction: CThostFtdcBatchOrderActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnOptionSelfClose(self, pOptionSelfClose: CThostFtdcOptionSelfCloseField):
        print('===OnRtnOptionSelfClose===: pOptionSelfClose: CThostFtdcOptionSelfCloseField')

    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose: CThostFtdcInputOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnOptionSelfCloseInsert===: pInputOptionSelfClose: CThostFtdcInputOptionSelfCloseField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction: CThostFtdcOptionSelfCloseActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnOptionSelfCloseAction===: pOptionSelfCloseAction: CThostFtdcOptionSelfCloseActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnCombAction(self, pCombAction: CThostFtdcCombActionField):
        print('===OnRtnCombAction===: pCombAction: CThostFtdcCombActionField')

    def OnErrRtnCombActionInsert(self, pInputCombAction: CThostFtdcInputCombActionField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnCombActionInsert===: pInputCombAction: CThostFtdcInputCombActionField, pRspInfo: CThostFtdcRspInfoField')

    def OnRspQryContractBank(self, pContractBank: CThostFtdcContractBankField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryContractBank===: pContractBank: CThostFtdcContractBankField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryParkedOrder(self, pParkedOrder: CThostFtdcParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryParkedOrder===: pParkedOrder: CThostFtdcParkedOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryParkedOrderAction(self, pParkedOrderAction: CThostFtdcParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryParkedOrderAction===: pParkedOrderAction: CThostFtdcParkedOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTradingNotice(self, pTradingNotice: CThostFtdcTradingNoticeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTradingNotice===: pTradingNotice: CThostFtdcTradingNoticeField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams: CThostFtdcBrokerTradingParamsField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryBrokerTradingParams===: pBrokerTradingParams: CThostFtdcBrokerTradingParamsField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos: CThostFtdcBrokerTradingAlgosField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryBrokerTradingAlgos===: pBrokerTradingAlgos: CThostFtdcBrokerTradingAlgosField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken: CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQueryCFMMCTradingAccountToken===: pQueryCFMMCTradingAccountToken: CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnFromBankToFutureByBank(self, pRspTransfer: CThostFtdcRspTransferField):
        print('===OnRtnFromBankToFutureByBank===: pRspTransfer: CThostFtdcRspTransferField')

    def OnRtnFromFutureToBankByBank(self, pRspTransfer: CThostFtdcRspTransferField):
        print('===OnRtnFromFutureToBankByBank===: pRspTransfer: CThostFtdcRspTransferField')

    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromBankToFutureByBank===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromFutureToBankByBank===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRtnFromBankToFutureByFuture(self, pRspTransfer: CThostFtdcRspTransferField):
        print('===OnRtnFromBankToFutureByFuture===: pRspTransfer: CThostFtdcRspTransferField')

    def OnRtnFromFutureToBankByFuture(self, pRspTransfer: CThostFtdcRspTransferField):
        print('===OnRtnFromFutureToBankByFuture===: pRspTransfer: CThostFtdcRspTransferField')

    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromBankToFutureByFutureManual===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromFutureToBankByFutureManual===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount: CThostFtdcNotifyQueryAccountField):
        print('===OnRtnQueryBankBalanceByFuture===: pNotifyQueryAccount: CThostFtdcNotifyQueryAccountField')

    def OnErrRtnBankToFutureByFuture(self, pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnBankToFutureByFuture===: pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnFutureToBankByFuture(self, pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnFutureToBankByFuture===: pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal: CThostFtdcReqRepealField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnRepealBankToFutureByFutureManual===: pReqRepeal: CThostFtdcReqRepealField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal: CThostFtdcReqRepealField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnRepealFutureToBankByFutureManual===: pReqRepeal: CThostFtdcReqRepealField, pRspInfo: CThostFtdcRspInfoField')

    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount: CThostFtdcReqQueryAccountField, pRspInfo: CThostFtdcRspInfoField):
        print('===OnErrRtnQueryBankBalanceByFuture===: pReqQueryAccount: CThostFtdcReqQueryAccountField, pRspInfo: CThostFtdcRspInfoField')

    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromBankToFutureByFuture===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal: CThostFtdcRspRepealField):
        print('===OnRtnRepealFromFutureToBankByFuture===: pRspRepeal: CThostFtdcRspRepealField')

    def OnRspFromBankToFutureByFuture(self, pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspFromBankToFutureByFuture===: pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspFromFutureToBankByFuture(self, pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspFromFutureToBankByFuture===: pReqTransfer: CThostFtdcReqTransferField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount: CThostFtdcReqQueryAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQueryBankAccountMoneyByFuture===: pReqQueryAccount: CThostFtdcReqQueryAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnOpenAccountByBank(self, pOpenAccount: CThostFtdcOpenAccountField):
        print('===OnRtnOpenAccountByBank===: pOpenAccount: CThostFtdcOpenAccountField')

    def OnRtnCancelAccountByBank(self, pCancelAccount: CThostFtdcCancelAccountField):
        print('===OnRtnCancelAccountByBank===: pCancelAccount: CThostFtdcCancelAccountField')

    def OnRtnChangeAccountByBank(self, pChangeAccount: CThostFtdcChangeAccountField):
        print('===OnRtnChangeAccountByBank===: pChangeAccount: CThostFtdcChangeAccountField')

    def OnRspQryClassifiedInstrument(self, pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryClassifiedInstrument===: pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryCombPromotionParam(self, pCombPromotionParam: CThostFtdcCombPromotionParamField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryCombPromotionParam===: pCombPromotionParam: CThostFtdcCombPromotionParamField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool')