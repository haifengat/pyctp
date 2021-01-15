#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2018/12/10'


from ctypes import *
from .ctp_enum import *

class  CThostFtdcDisseminationField(Structure):
    """信息分发"""
    _fields_ = [
        ("SequenceSeries", c_short),
        ("SequenceNo", c_int32),
    ]

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def __str__(self): # 可以直接print
        return f"'SequenceSeries'={self.getSequenceSeries()}, 'SequenceNo'={self.getSequenceNo()}"


class  CThostFtdcReqUserLoginField(Structure):
    """用户登录请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("Password", c_char*41),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("MacAddress", c_char*21),
        ("OneTimePassword", c_char*41),
        ("reserve1", c_char*16),
        ("LoginRemark", c_char*36),
        ("ClientIPPort", c_int32),
        ("ClientIPAddress", c_char*33),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getOneTimePassword(self):
        '''动态密码'''
        return str(self.OneTimePassword, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort

    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'MacAddress'={self.getMacAddress()}, 'OneTimePassword'={self.getOneTimePassword()}, 'reserve1'={self.getreserve1()}, 'LoginRemark'={self.getLoginRemark()}, 'ClientIPPort'={self.getClientIPPort()}, 'ClientIPAddress'={self.getClientIPAddress()}"


class  CThostFtdcRspUserLoginField(Structure):
    """用户登录应答"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("LoginTime", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("SystemName", c_char*41),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("MaxOrderRef", c_char*13),
        ("SHFETime", c_char*9),
        ("DCETime", c_char*9),
        ("CZCETime", c_char*9),
        ("FFEXTime", c_char*9),
        ("INETime", c_char*9),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getLoginTime(self):
        '''登录成功时间'''
        return str(self.LoginTime, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getSystemName(self):
        '''交易系统名称'''
        return str(self.SystemName, 'GBK')

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getMaxOrderRef(self):
        '''最大报单引用'''
        return str(self.MaxOrderRef, 'GBK')

    def getSHFETime(self):
        '''上期所时间'''
        return str(self.SHFETime, 'GBK')

    def getDCETime(self):
        '''大商所时间'''
        return str(self.DCETime, 'GBK')

    def getCZCETime(self):
        '''郑商所时间'''
        return str(self.CZCETime, 'GBK')

    def getFFEXTime(self):
        '''中金所时间'''
        return str(self.FFEXTime, 'GBK')

    def getINETime(self):
        '''能源中心时间'''
        return str(self.INETime, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'LoginTime'={self.getLoginTime()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'SystemName'={self.getSystemName()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'MaxOrderRef'={self.getMaxOrderRef()}, 'SHFETime'={self.getSHFETime()}, 'DCETime'={self.getDCETime()}, 'CZCETime'={self.getCZCETime()}, 'FFEXTime'={self.getFFEXTime()}, 'INETime'={self.getINETime()}"


class  CThostFtdcUserLogoutField(Structure):
    """用户登出请求"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcForceUserLogoutField(Structure):
    """强制交易员退出"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcReqAuthenticateField(Structure):
    """客户端认证请求"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserProductInfo", c_char*11),
        ("AuthCode", c_char*17),
        ("AppID", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getAuthCode(self):
        '''认证码'''
        return str(self.AuthCode, 'GBK')

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'AuthCode'={self.getAuthCode()}, 'AppID'={self.getAppID()}"


class  CThostFtdcRspAuthenticateField(Structure):
    """客户端认证响应"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserProductInfo", c_char*11),
        ("AppID", c_char*33),
        ("AppType", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def getAppType(self):
        '''App类型'''
        return TThostFtdcAppTypeType(ord(self.AppType)) if ord(self.AppType) in [e.value for e in list(TThostFtdcAppTypeType)] else list(TThostFtdcAppTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'AppID'={self.getAppID()}, 'AppType'={self.getAppType()}"


class  CThostFtdcAuthenticationInfoField(Structure):
    """客户端认证信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserProductInfo", c_char*11),
        ("AuthInfo", c_char*129),
        ("IsResult", c_int32),
        ("AppID", c_char*33),
        ("AppType", c_char),
        ("reserve1", c_char*16),
        ("ClientIPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getAuthInfo(self):
        '''认证信息'''
        return str(self.AuthInfo, 'GBK')

    def getIsResult(self):
        '''是否为认证结果'''
        return self.IsResult

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def getAppType(self):
        '''App类型'''
        return TThostFtdcAppTypeType(ord(self.AppType)) if ord(self.AppType) in [e.value for e in list(TThostFtdcAppTypeType)] else list(TThostFtdcAppTypeType)[0]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'AuthInfo'={self.getAuthInfo()}, 'IsResult'={self.getIsResult()}, 'AppID'={self.getAppID()}, 'AppType'={self.getAppType()}, 'reserve1'={self.getreserve1()}, 'ClientIPAddress'={self.getClientIPAddress()}"


class  CThostFtdcRspUserLogin2Field(Structure):
    """用户登录应答2"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("LoginTime", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("SystemName", c_char*41),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("MaxOrderRef", c_char*13),
        ("SHFETime", c_char*9),
        ("DCETime", c_char*9),
        ("CZCETime", c_char*9),
        ("FFEXTime", c_char*9),
        ("INETime", c_char*9),
        ("RandomString", c_char*17),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getLoginTime(self):
        '''登录成功时间'''
        return str(self.LoginTime, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getSystemName(self):
        '''交易系统名称'''
        return str(self.SystemName, 'GBK')

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getMaxOrderRef(self):
        '''最大报单引用'''
        return str(self.MaxOrderRef, 'GBK')

    def getSHFETime(self):
        '''上期所时间'''
        return str(self.SHFETime, 'GBK')

    def getDCETime(self):
        '''大商所时间'''
        return str(self.DCETime, 'GBK')

    def getCZCETime(self):
        '''郑商所时间'''
        return str(self.CZCETime, 'GBK')

    def getFFEXTime(self):
        '''中金所时间'''
        return str(self.FFEXTime, 'GBK')

    def getINETime(self):
        '''能源中心时间'''
        return str(self.INETime, 'GBK')

    def getRandomString(self):
        '''随机串'''
        return str(self.RandomString, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'LoginTime'={self.getLoginTime()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'SystemName'={self.getSystemName()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'MaxOrderRef'={self.getMaxOrderRef()}, 'SHFETime'={self.getSHFETime()}, 'DCETime'={self.getDCETime()}, 'CZCETime'={self.getCZCETime()}, 'FFEXTime'={self.getFFEXTime()}, 'INETime'={self.getINETime()}, 'RandomString'={self.getRandomString()}"


class  CThostFtdcTransferHeaderField(Structure):
    """银期转帐报文头"""
    _fields_ = [
        ("Version", c_char*4),
        ("TradeCode", c_char*7),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("TradeSerial", c_char*9),
        ("FutureID", c_char*11),
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
        ("OperNo", c_char*17),
        ("DeviceID", c_char*3),
        ("RecordNum", c_char*7),
        ("SessionID", c_int32),
        ("RequestID", c_int32),
    ]

    def getVersion(self):
        '''版本号，常量，1.0'''
        return str(self.Version, 'GBK')

    def getTradeCode(self):
        '''交易代码，必填'''
        return str(self.TradeCode, 'GBK')

    def getTradeDate(self):
        '''交易日期，必填，格式：yyyymmdd'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间，必填，格式：hhmmss'''
        return str(self.TradeTime, 'GBK')

    def getTradeSerial(self):
        '''发起方流水号，N/A'''
        return str(self.TradeSerial, 'GBK')

    def getFutureID(self):
        '''期货公司代码，必填'''
        return str(self.FutureID, 'GBK')

    def getBankID(self):
        '''银行代码，根据查询银行得到，必填'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码，根据查询银行得到，必填'''
        return str(self.BankBrchID, 'GBK')

    def getOperNo(self):
        '''操作员，N/A'''
        return str(self.OperNo, 'GBK')

    def getDeviceID(self):
        '''交易设备类型，N/A'''
        return str(self.DeviceID, 'GBK')

    def getRecordNum(self):
        '''记录数，N/A'''
        return str(self.RecordNum, 'GBK')

    def getSessionID(self):
        '''会话编号，N/A'''
        return self.SessionID

    def getRequestID(self):
        '''请求编号，N/A'''
        return self.RequestID

    def __str__(self): # 可以直接print
        return f"'Version'={self.getVersion()}, 'TradeCode'={self.getTradeCode()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'TradeSerial'={self.getTradeSerial()}, 'FutureID'={self.getFutureID()}, 'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}, 'OperNo'={self.getOperNo()}, 'DeviceID'={self.getDeviceID()}, 'RecordNum'={self.getRecordNum()}, 'SessionID'={self.getSessionID()}, 'RequestID'={self.getRequestID()}"


class  CThostFtdcTransferBankToFutureReqField(Structure):
    """银行资金转期货请求，TradeCode=202001"""
    _fields_ = [
        ("FutureAccount", c_char*13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char*17),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char*4),
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getFuturePwdFlag(self):
        '''密码标志'''
        return TThostFtdcFuturePwdFlagType(ord(self.FuturePwdFlag)) if ord(self.FuturePwdFlag) in [e.value for e in list(TThostFtdcFuturePwdFlagType)] else list(TThostFtdcFuturePwdFlagType)[0]

    def getFutureAccPwd(self):
        '''密码'''
        return str(self.FutureAccPwd, 'GBK')

    def getTradeAmt(self):
        '''转账金额'''
        return self.TradeAmt

    def getCustFee(self):
        '''客户手续费'''
        return self.CustFee

    def getCurrencyCode(self):
        '''币种：RMB-人民币 USD-美圆 HKD-港元'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FutureAccount'={self.getFutureAccount()}, 'FuturePwdFlag'={self.getFuturePwdFlag()}, 'FutureAccPwd'={self.getFutureAccPwd()}, 'TradeAmt'={self.getTradeAmt()}, 'CustFee'={self.getCustFee()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferBankToFutureRspField(Structure):
    """银行资金转期货请求响应"""
    _fields_ = [
        ("RetCode", c_char*5),
        ("RetInfo", c_char*129),
        ("FutureAccount", c_char*13),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char*4),
    ]

    def getRetCode(self):
        '''响应代码'''
        return str(self.RetCode, 'GBK')

    def getRetInfo(self):
        '''响应信息'''
        return str(self.RetInfo, 'GBK')

    def getFutureAccount(self):
        '''资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getTradeAmt(self):
        '''转帐金额'''
        return self.TradeAmt

    def getCustFee(self):
        '''应收客户手续费'''
        return self.CustFee

    def getCurrencyCode(self):
        '''币种'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'RetCode'={self.getRetCode()}, 'RetInfo'={self.getRetInfo()}, 'FutureAccount'={self.getFutureAccount()}, 'TradeAmt'={self.getTradeAmt()}, 'CustFee'={self.getCustFee()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferFutureToBankReqField(Structure):
    """期货资金转银行请求，TradeCode=202002"""
    _fields_ = [
        ("FutureAccount", c_char*13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char*17),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char*4),
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getFuturePwdFlag(self):
        '''密码标志'''
        return TThostFtdcFuturePwdFlagType(ord(self.FuturePwdFlag)) if ord(self.FuturePwdFlag) in [e.value for e in list(TThostFtdcFuturePwdFlagType)] else list(TThostFtdcFuturePwdFlagType)[0]

    def getFutureAccPwd(self):
        '''密码'''
        return str(self.FutureAccPwd, 'GBK')

    def getTradeAmt(self):
        '''转账金额'''
        return self.TradeAmt

    def getCustFee(self):
        '''客户手续费'''
        return self.CustFee

    def getCurrencyCode(self):
        '''币种：RMB-人民币 USD-美圆 HKD-港元'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FutureAccount'={self.getFutureAccount()}, 'FuturePwdFlag'={self.getFuturePwdFlag()}, 'FutureAccPwd'={self.getFutureAccPwd()}, 'TradeAmt'={self.getTradeAmt()}, 'CustFee'={self.getCustFee()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferFutureToBankRspField(Structure):
    """期货资金转银行请求响应"""
    _fields_ = [
        ("RetCode", c_char*5),
        ("RetInfo", c_char*129),
        ("FutureAccount", c_char*13),
        ("TradeAmt", c_double),
        ("CustFee", c_double),
        ("CurrencyCode", c_char*4),
    ]

    def getRetCode(self):
        '''响应代码'''
        return str(self.RetCode, 'GBK')

    def getRetInfo(self):
        '''响应信息'''
        return str(self.RetInfo, 'GBK')

    def getFutureAccount(self):
        '''资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getTradeAmt(self):
        '''转帐金额'''
        return self.TradeAmt

    def getCustFee(self):
        '''应收客户手续费'''
        return self.CustFee

    def getCurrencyCode(self):
        '''币种'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'RetCode'={self.getRetCode()}, 'RetInfo'={self.getRetInfo()}, 'FutureAccount'={self.getFutureAccount()}, 'TradeAmt'={self.getTradeAmt()}, 'CustFee'={self.getCustFee()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferQryBankReqField(Structure):
    """查询银行资金请求，TradeCode=204002"""
    _fields_ = [
        ("FutureAccount", c_char*13),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", c_char*17),
        ("CurrencyCode", c_char*4),
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getFuturePwdFlag(self):
        '''密码标志'''
        return TThostFtdcFuturePwdFlagType(ord(self.FuturePwdFlag)) if ord(self.FuturePwdFlag) in [e.value for e in list(TThostFtdcFuturePwdFlagType)] else list(TThostFtdcFuturePwdFlagType)[0]

    def getFutureAccPwd(self):
        '''密码'''
        return str(self.FutureAccPwd, 'GBK')

    def getCurrencyCode(self):
        '''币种：RMB-人民币 USD-美圆 HKD-港元'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FutureAccount'={self.getFutureAccount()}, 'FuturePwdFlag'={self.getFuturePwdFlag()}, 'FutureAccPwd'={self.getFutureAccPwd()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferQryBankRspField(Structure):
    """查询银行资金请求响应"""
    _fields_ = [
        ("RetCode", c_char*5),
        ("RetInfo", c_char*129),
        ("FutureAccount", c_char*13),
        ("TradeAmt", c_double),
        ("UseAmt", c_double),
        ("FetchAmt", c_double),
        ("CurrencyCode", c_char*4),
    ]

    def getRetCode(self):
        '''响应代码'''
        return str(self.RetCode, 'GBK')

    def getRetInfo(self):
        '''响应信息'''
        return str(self.RetInfo, 'GBK')

    def getFutureAccount(self):
        '''资金账户'''
        return str(self.FutureAccount, 'GBK')

    def getTradeAmt(self):
        '''银行余额'''
        return self.TradeAmt

    def getUseAmt(self):
        '''银行可用余额'''
        return self.UseAmt

    def getFetchAmt(self):
        '''银行可取余额'''
        return self.FetchAmt

    def getCurrencyCode(self):
        '''币种'''
        return str(self.CurrencyCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'RetCode'={self.getRetCode()}, 'RetInfo'={self.getRetInfo()}, 'FutureAccount'={self.getFutureAccount()}, 'TradeAmt'={self.getTradeAmt()}, 'UseAmt'={self.getUseAmt()}, 'FetchAmt'={self.getFetchAmt()}, 'CurrencyCode'={self.getCurrencyCode()}"


class  CThostFtdcTransferQryDetailReqField(Structure):
    """查询银行交易明细请求，TradeCode=204999"""
    _fields_ = [
        ("FutureAccount", c_char*13),
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FutureAccount'={self.getFutureAccount()}"


class  CThostFtdcTransferQryDetailRspField(Structure):
    """查询银行交易明细请求响应"""
    _fields_ = [
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("TradeCode", c_char*7),
        ("FutureSerial", c_int32),
        ("FutureID", c_char*11),
        ("FutureAccount", c_char*22),
        ("BankSerial", c_int32),
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
        ("BankAccount", c_char*41),
        ("CertCode", c_char*21),
        ("CurrencyCode", c_char*4),
        ("TxAmount", c_double),
        ("Flag", c_char),
    ]

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getTradeCode(self):
        '''交易代码'''
        return str(self.TradeCode, 'GBK')

    def getFutureSerial(self):
        '''期货流水号'''
        return self.FutureSerial

    def getFutureID(self):
        '''期货公司代码'''
        return str(self.FutureID, 'GBK')

    def getFutureAccount(self):
        '''资金帐号'''
        return str(self.FutureAccount, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return self.BankSerial

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')

    def getBankAccount(self):
        '''银行账号'''
        return str(self.BankAccount, 'GBK')

    def getCertCode(self):
        '''证件号码'''
        return str(self.CertCode, 'GBK')

    def getCurrencyCode(self):
        '''货币代码'''
        return str(self.CurrencyCode, 'GBK')

    def getTxAmount(self):
        '''发生金额'''
        return self.TxAmount

    def getFlag(self):
        '''有效标志'''
        return TThostFtdcTransferValidFlagType(ord(self.Flag)) if ord(self.Flag) in [e.value for e in list(TThostFtdcTransferValidFlagType)] else list(TThostFtdcTransferValidFlagType)[0]

    def __str__(self): # 可以直接print
        return f"'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'TradeCode'={self.getTradeCode()}, 'FutureSerial'={self.getFutureSerial()}, 'FutureID'={self.getFutureID()}, 'FutureAccount'={self.getFutureAccount()}, 'BankSerial'={self.getBankSerial()}, 'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}, 'BankAccount'={self.getBankAccount()}, 'CertCode'={self.getCertCode()}, 'CurrencyCode'={self.getCurrencyCode()}, 'TxAmount'={self.getTxAmount()}, 'Flag'={self.getFlag()}"


class  CThostFtdcRspInfoField(Structure):
    """响应信息"""
    _fields_ = [
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcExchangeField(Structure):
    """交易所"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ExchangeName", c_char*61),
        ("ExchangeProperty", c_char),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExchangeName(self):
        '''交易所名称'''
        return str(self.ExchangeName, 'GBK')

    def getExchangeProperty(self):
        '''交易所属性'''
        return TThostFtdcExchangePropertyType(ord(self.ExchangeProperty)) if ord(self.ExchangeProperty) in [e.value for e in list(TThostFtdcExchangePropertyType)] else list(TThostFtdcExchangePropertyType)[0]

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ExchangeName'={self.getExchangeName()}, 'ExchangeProperty'={self.getExchangeProperty()}"


class  CThostFtdcProductField(Structure):
    """产品"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ProductName", c_char*21),
        ("ExchangeID", c_char*9),
        ("ProductClass", c_char),
        ("VolumeMultiple", c_int32),
        ("PriceTick", c_double),
        ("MaxMarketOrderVolume", c_int32),
        ("MinMarketOrderVolume", c_int32),
        ("MaxLimitOrderVolume", c_int32),
        ("MinLimitOrderVolume", c_int32),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("CloseDealType", c_char),
        ("TradeCurrencyID", c_char*4),
        ("MortgageFundUseRange", c_char),
        ("reserve2", c_char*31),
        ("UnderlyingMultiple", c_double),
        ("ProductID", c_char*81),
        ("ExchangeProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getProductName(self):
        '''产品名称'''
        return str(self.ProductName, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductClass(self):
        '''产品类型'''
        return TThostFtdcProductClassType(ord(self.ProductClass)) if ord(self.ProductClass) in [e.value for e in list(TThostFtdcProductClassType)] else list(TThostFtdcProductClassType)[0]

    def getVolumeMultiple(self):
        '''合约数量乘数'''
        return self.VolumeMultiple

    def getPriceTick(self):
        '''最小变动价位'''
        return self.PriceTick

    def getMaxMarketOrderVolume(self):
        '''市价单最大下单量'''
        return self.MaxMarketOrderVolume

    def getMinMarketOrderVolume(self):
        '''市价单最小下单量'''
        return self.MinMarketOrderVolume

    def getMaxLimitOrderVolume(self):
        '''限价单最大下单量'''
        return self.MaxLimitOrderVolume

    def getMinLimitOrderVolume(self):
        '''限价单最小下单量'''
        return self.MinLimitOrderVolume

    def getPositionType(self):
        '''持仓类型'''
        return TThostFtdcPositionTypeType(ord(self.PositionType)) if ord(self.PositionType) in [e.value for e in list(TThostFtdcPositionTypeType)] else list(TThostFtdcPositionTypeType)[0]

    def getPositionDateType(self):
        '''持仓日期类型'''
        return TThostFtdcPositionDateTypeType(ord(self.PositionDateType)) if ord(self.PositionDateType) in [e.value for e in list(TThostFtdcPositionDateTypeType)] else list(TThostFtdcPositionDateTypeType)[0]

    def getCloseDealType(self):
        '''平仓处理类型'''
        return TThostFtdcCloseDealTypeType(ord(self.CloseDealType)) if ord(self.CloseDealType) in [e.value for e in list(TThostFtdcCloseDealTypeType)] else list(TThostFtdcCloseDealTypeType)[0]

    def getTradeCurrencyID(self):
        '''交易币种类型'''
        return str(self.TradeCurrencyID, 'GBK')

    def getMortgageFundUseRange(self):
        '''质押资金可用范围'''
        return TThostFtdcMortgageFundUseRangeType(ord(self.MortgageFundUseRange)) if ord(self.MortgageFundUseRange) in [e.value for e in list(TThostFtdcMortgageFundUseRangeType)] else list(TThostFtdcMortgageFundUseRangeType)[0]

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getUnderlyingMultiple(self):
        '''合约基础商品乘数'''
        return self.UnderlyingMultiple

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def getExchangeProductID(self):
        '''交易所产品代码'''
        return str(self.ExchangeProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ProductName'={self.getProductName()}, 'ExchangeID'={self.getExchangeID()}, 'ProductClass'={self.getProductClass()}, 'VolumeMultiple'={self.getVolumeMultiple()}, 'PriceTick'={self.getPriceTick()}, 'MaxMarketOrderVolume'={self.getMaxMarketOrderVolume()}, 'MinMarketOrderVolume'={self.getMinMarketOrderVolume()}, 'MaxLimitOrderVolume'={self.getMaxLimitOrderVolume()}, 'MinLimitOrderVolume'={self.getMinLimitOrderVolume()}, 'PositionType'={self.getPositionType()}, 'PositionDateType'={self.getPositionDateType()}, 'CloseDealType'={self.getCloseDealType()}, 'TradeCurrencyID'={self.getTradeCurrencyID()}, 'MortgageFundUseRange'={self.getMortgageFundUseRange()}, 'reserve2'={self.getreserve2()}, 'UnderlyingMultiple'={self.getUnderlyingMultiple()}, 'ProductID'={self.getProductID()}, 'ExchangeProductID'={self.getExchangeProductID()}"


class  CThostFtdcInstrumentField(Structure):
    """合约"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InstrumentName", c_char*21),
        ("reserve2", c_char*31),
        ("reserve3", c_char*31),
        ("ProductClass", c_char),
        ("DeliveryYear", c_int32),
        ("DeliveryMonth", c_int32),
        ("MaxMarketOrderVolume", c_int32),
        ("MinMarketOrderVolume", c_int32),
        ("MaxLimitOrderVolume", c_int32),
        ("MinLimitOrderVolume", c_int32),
        ("VolumeMultiple", c_int32),
        ("PriceTick", c_double),
        ("CreateDate", c_char*9),
        ("OpenDate", c_char*9),
        ("ExpireDate", c_char*9),
        ("StartDelivDate", c_char*9),
        ("EndDelivDate", c_char*9),
        ("InstLifePhase", c_char),
        ("IsTrading", c_int32),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("LongMarginRatio", c_double),
        ("ShortMarginRatio", c_double),
        ("MaxMarginSideAlgorithm", c_char),
        ("reserve4", c_char*31),
        ("StrikePrice", c_double),
        ("OptionsType", c_char),
        ("UnderlyingMultiple", c_double),
        ("CombinationType", c_char),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("ProductID", c_char*81),
        ("UnderlyingInstrID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentName(self):
        '''合约名称'''
        return str(self.InstrumentName, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getProductClass(self):
        '''产品类型'''
        return TThostFtdcProductClassType(ord(self.ProductClass)) if ord(self.ProductClass) in [e.value for e in list(TThostFtdcProductClassType)] else list(TThostFtdcProductClassType)[0]

    def getDeliveryYear(self):
        '''交割年份'''
        return self.DeliveryYear

    def getDeliveryMonth(self):
        '''交割月'''
        return self.DeliveryMonth

    def getMaxMarketOrderVolume(self):
        '''市价单最大下单量'''
        return self.MaxMarketOrderVolume

    def getMinMarketOrderVolume(self):
        '''市价单最小下单量'''
        return self.MinMarketOrderVolume

    def getMaxLimitOrderVolume(self):
        '''限价单最大下单量'''
        return self.MaxLimitOrderVolume

    def getMinLimitOrderVolume(self):
        '''限价单最小下单量'''
        return self.MinLimitOrderVolume

    def getVolumeMultiple(self):
        '''合约数量乘数'''
        return self.VolumeMultiple

    def getPriceTick(self):
        '''最小变动价位'''
        return self.PriceTick

    def getCreateDate(self):
        '''创建日'''
        return str(self.CreateDate, 'GBK')

    def getOpenDate(self):
        '''上市日'''
        return str(self.OpenDate, 'GBK')

    def getExpireDate(self):
        '''到期日'''
        return str(self.ExpireDate, 'GBK')

    def getStartDelivDate(self):
        '''开始交割日'''
        return str(self.StartDelivDate, 'GBK')

    def getEndDelivDate(self):
        '''结束交割日'''
        return str(self.EndDelivDate, 'GBK')

    def getInstLifePhase(self):
        '''合约生命周期状态'''
        return TThostFtdcInstLifePhaseType(ord(self.InstLifePhase)) if ord(self.InstLifePhase) in [e.value for e in list(TThostFtdcInstLifePhaseType)] else list(TThostFtdcInstLifePhaseType)[0]

    def getIsTrading(self):
        '''当前是否交易'''
        return self.IsTrading

    def getPositionType(self):
        '''持仓类型'''
        return TThostFtdcPositionTypeType(ord(self.PositionType)) if ord(self.PositionType) in [e.value for e in list(TThostFtdcPositionTypeType)] else list(TThostFtdcPositionTypeType)[0]

    def getPositionDateType(self):
        '''持仓日期类型'''
        return TThostFtdcPositionDateTypeType(ord(self.PositionDateType)) if ord(self.PositionDateType) in [e.value for e in list(TThostFtdcPositionDateTypeType)] else list(TThostFtdcPositionDateTypeType)[0]

    def getLongMarginRatio(self):
        '''多头保证金率'''
        return self.LongMarginRatio

    def getShortMarginRatio(self):
        '''空头保证金率'''
        return self.ShortMarginRatio

    def getMaxMarginSideAlgorithm(self):
        '''是否使用大额单边保证金算法'''
        return TThostFtdcMaxMarginSideAlgorithmType(ord(self.MaxMarginSideAlgorithm)) if ord(self.MaxMarginSideAlgorithm) in [e.value for e in list(TThostFtdcMaxMarginSideAlgorithmType)] else list(TThostFtdcMaxMarginSideAlgorithmType)[0]

    def getreserve4(self):
        '''保留的无效字段'''
        return str(self.reserve4, 'GBK')

    def getStrikePrice(self):
        '''执行价'''
        return self.StrikePrice

    def getOptionsType(self):
        '''期权类型'''
        return TThostFtdcOptionsTypeType(ord(self.OptionsType)) if ord(self.OptionsType) in [e.value for e in list(TThostFtdcOptionsTypeType)] else list(TThostFtdcOptionsTypeType)[0]

    def getUnderlyingMultiple(self):
        '''合约基础商品乘数'''
        return self.UnderlyingMultiple

    def getCombinationType(self):
        '''组合类型'''
        return TThostFtdcCombinationTypeType(ord(self.CombinationType)) if ord(self.CombinationType) in [e.value for e in list(TThostFtdcCombinationTypeType)] else list(TThostFtdcCombinationTypeType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def getUnderlyingInstrID(self):
        '''基础商品代码'''
        return str(self.UnderlyingInstrID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentName'={self.getInstrumentName()}, 'reserve2'={self.getreserve2()}, 'reserve3'={self.getreserve3()}, 'ProductClass'={self.getProductClass()}, 'DeliveryYear'={self.getDeliveryYear()}, 'DeliveryMonth'={self.getDeliveryMonth()}, 'MaxMarketOrderVolume'={self.getMaxMarketOrderVolume()}, 'MinMarketOrderVolume'={self.getMinMarketOrderVolume()}, 'MaxLimitOrderVolume'={self.getMaxLimitOrderVolume()}, 'MinLimitOrderVolume'={self.getMinLimitOrderVolume()}, 'VolumeMultiple'={self.getVolumeMultiple()}, 'PriceTick'={self.getPriceTick()}, 'CreateDate'={self.getCreateDate()}, 'OpenDate'={self.getOpenDate()}, 'ExpireDate'={self.getExpireDate()}, 'StartDelivDate'={self.getStartDelivDate()}, 'EndDelivDate'={self.getEndDelivDate()}, 'InstLifePhase'={self.getInstLifePhase()}, 'IsTrading'={self.getIsTrading()}, 'PositionType'={self.getPositionType()}, 'PositionDateType'={self.getPositionDateType()}, 'LongMarginRatio'={self.getLongMarginRatio()}, 'ShortMarginRatio'={self.getShortMarginRatio()}, 'MaxMarginSideAlgorithm'={self.getMaxMarginSideAlgorithm()}, 'reserve4'={self.getreserve4()}, 'StrikePrice'={self.getStrikePrice()}, 'OptionsType'={self.getOptionsType()}, 'UnderlyingMultiple'={self.getUnderlyingMultiple()}, 'CombinationType'={self.getCombinationType()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'ProductID'={self.getProductID()}, 'UnderlyingInstrID'={self.getUnderlyingInstrID()}"


class  CThostFtdcBrokerField(Structure):
    """经纪公司"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("BrokerAbbr", c_char*9),
        ("BrokerName", c_char*81),
        ("IsActive", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerAbbr(self):
        '''经纪公司简称'''
        return str(self.BrokerAbbr, 'GBK')

    def getBrokerName(self):
        '''经纪公司名称'''
        return str(self.BrokerName, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'BrokerAbbr'={self.getBrokerAbbr()}, 'BrokerName'={self.getBrokerName()}, 'IsActive'={self.getIsActive()}"


class  CThostFtdcTraderField(Structure):
    """交易所交易员"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ParticipantID", c_char*11),
        ("Password", c_char*41),
        ("InstallCount", c_int32),
        ("BrokerID", c_char*11),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getInstallCount(self):
        '''安装数量'''
        return self.InstallCount

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ParticipantID'={self.getParticipantID()}, 'Password'={self.getPassword()}, 'InstallCount'={self.getInstallCount()}, 'BrokerID'={self.getBrokerID()}"


class  CThostFtdcInvestorField(Structure):
    """投资者"""
    _fields_ = [
        ("InvestorID", c_char*13),
        ("BrokerID", c_char*11),
        ("InvestorGroupID", c_char*13),
        ("InvestorName", c_char*81),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("IsActive", c_int32),
        ("Telephone", c_char*41),
        ("Address", c_char*101),
        ("OpenDate", c_char*9),
        ("Mobile", c_char*41),
        ("CommModelID", c_char*13),
        ("MarginModelID", c_char*13),
    ]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorGroupID(self):
        '''投资者分组代码'''
        return str(self.InvestorGroupID, 'GBK')

    def getInvestorName(self):
        '''投资者名称'''
        return str(self.InvestorName, 'GBK')

    def getIdentifiedCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdentifiedCardType)) if ord(self.IdentifiedCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getTelephone(self):
        '''联系电话'''
        return str(self.Telephone, 'GBK')

    def getAddress(self):
        '''通讯地址'''
        return str(self.Address, 'GBK')

    def getOpenDate(self):
        '''开户日期'''
        return str(self.OpenDate, 'GBK')

    def getMobile(self):
        '''手机'''
        return str(self.Mobile, 'GBK')

    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')

    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorGroupID'={self.getInvestorGroupID()}, 'InvestorName'={self.getInvestorName()}, 'IdentifiedCardType'={self.getIdentifiedCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'IsActive'={self.getIsActive()}, 'Telephone'={self.getTelephone()}, 'Address'={self.getAddress()}, 'OpenDate'={self.getOpenDate()}, 'Mobile'={self.getMobile()}, 'CommModelID'={self.getCommModelID()}, 'MarginModelID'={self.getMarginModelID()}"


class  CThostFtdcTradingCodeField(Structure):
    """交易编码"""
    _fields_ = [
        ("InvestorID", c_char*13),
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
        ("ClientID", c_char*11),
        ("IsActive", c_int32),
        ("ClientIDType", c_char),
        ("BranchID", c_char*9),
        ("BizType", c_char),
        ("InvestUnitID", c_char*17),
    ]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getClientIDType(self):
        '''交易编码类型'''
        return TThostFtdcClientIDTypeType(ord(self.ClientIDType)) if ord(self.ClientIDType) in [e.value for e in list(TThostFtdcClientIDTypeType)] else list(TThostFtdcClientIDTypeType)[0]

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getBizType(self):
        '''业务类型'''
        return TThostFtdcBizTypeType(ord(self.BizType)) if ord(self.BizType) in [e.value for e in list(TThostFtdcBizTypeType)] else list(TThostFtdcBizTypeType)[0]

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}, 'IsActive'={self.getIsActive()}, 'ClientIDType'={self.getClientIDType()}, 'BranchID'={self.getBranchID()}, 'BizType'={self.getBizType()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcPartBrokerField(Structure):
    """会员编码和经纪公司编码对照表"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("IsActive", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'IsActive'={self.getIsActive()}"


class  CThostFtdcSuperUserField(Structure):
    """管理用户"""
    _fields_ = [
        ("UserID", c_char*16),
        ("UserName", c_char*81),
        ("Password", c_char*41),
        ("IsActive", c_int32),
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserName(self):
        '''用户名称'''
        return str(self.UserName, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def __str__(self): # 可以直接print
        return f"'UserID'={self.getUserID()}, 'UserName'={self.getUserName()}, 'Password'={self.getPassword()}, 'IsActive'={self.getIsActive()}"


class  CThostFtdcSuperUserFunctionField(Structure):
    """管理用户功能权限"""
    _fields_ = [
        ("UserID", c_char*16),
        ("FunctionCode", c_char),
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getFunctionCode(self):
        '''功能代码'''
        return TThostFtdcFunctionCodeType(ord(self.FunctionCode)) if ord(self.FunctionCode) in [e.value for e in list(TThostFtdcFunctionCodeType)] else list(TThostFtdcFunctionCodeType)[0]

    def __str__(self): # 可以直接print
        return f"'UserID'={self.getUserID()}, 'FunctionCode'={self.getFunctionCode()}"


class  CThostFtdcInvestorGroupField(Structure):
    """投资者组"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorGroupID", c_char*13),
        ("InvestorGroupName", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorGroupID(self):
        '''投资者分组代码'''
        return str(self.InvestorGroupID, 'GBK')

    def getInvestorGroupName(self):
        '''投资者分组名称'''
        return str(self.InvestorGroupName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorGroupID'={self.getInvestorGroupID()}, 'InvestorGroupName'={self.getInvestorGroupName()}"


class  CThostFtdcTradingAccountField(Structure):
    """资金账户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("PreMortgage", c_double),
        ("PreCredit", c_double),
        ("PreDeposit", c_double),
        ("PreBalance", c_double),
        ("PreMargin", c_double),
        ("InterestBase", c_double),
        ("Interest", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CurrMargin", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Balance", c_double),
        ("Available", c_double),
        ("WithdrawQuota", c_double),
        ("Reserve", c_double),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("Credit", c_double),
        ("Mortgage", c_double),
        ("ExchangeMargin", c_double),
        ("DeliveryMargin", c_double),
        ("ExchangeDeliveryMargin", c_double),
        ("ReserveBalance", c_double),
        ("CurrencyID", c_char*4),
        ("PreFundMortgageIn", c_double),
        ("PreFundMortgageOut", c_double),
        ("FundMortgageIn", c_double),
        ("FundMortgageOut", c_double),
        ("FundMortgageAvailable", c_double),
        ("MortgageableFund", c_double),
        ("SpecProductMargin", c_double),
        ("SpecProductFrozenMargin", c_double),
        ("SpecProductCommission", c_double),
        ("SpecProductFrozenCommission", c_double),
        ("SpecProductPositionProfit", c_double),
        ("SpecProductCloseProfit", c_double),
        ("SpecProductPositionProfitByAlg", c_double),
        ("SpecProductExchangeMargin", c_double),
        ("BizType", c_char),
        ("FrozenSwap", c_double),
        ("RemainSwap", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPreMortgage(self):
        '''上次质押金额'''
        return self.PreMortgage

    def getPreCredit(self):
        '''上次信用额度'''
        return self.PreCredit

    def getPreDeposit(self):
        '''上次存款额'''
        return self.PreDeposit

    def getPreBalance(self):
        '''上次结算准备金'''
        return self.PreBalance

    def getPreMargin(self):
        '''上次占用的保证金'''
        return self.PreMargin

    def getInterestBase(self):
        '''利息基数'''
        return self.InterestBase

    def getInterest(self):
        '''利息收入'''
        return self.Interest

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getWithdraw(self):
        '''出金金额'''
        return self.Withdraw

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenCash(self):
        '''冻结的资金'''
        return self.FrozenCash

    def getFrozenCommission(self):
        '''冻结的手续费'''
        return self.FrozenCommission

    def getCurrMargin(self):
        '''当前保证金总额'''
        return self.CurrMargin

    def getCashIn(self):
        '''资金差额'''
        return self.CashIn

    def getCommission(self):
        '''手续费'''
        return self.Commission

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getBalance(self):
        '''期货结算准备金'''
        return self.Balance

    def getAvailable(self):
        '''可用资金'''
        return self.Available

    def getWithdrawQuota(self):
        '''可取资金'''
        return self.WithdrawQuota

    def getReserve(self):
        '''基本准备金'''
        return self.Reserve

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getCredit(self):
        '''信用额度'''
        return self.Credit

    def getMortgage(self):
        '''质押金额'''
        return self.Mortgage

    def getExchangeMargin(self):
        '''交易所保证金'''
        return self.ExchangeMargin

    def getDeliveryMargin(self):
        '''投资者交割保证金'''
        return self.DeliveryMargin

    def getExchangeDeliveryMargin(self):
        '''交易所交割保证金'''
        return self.ExchangeDeliveryMargin

    def getReserveBalance(self):
        '''保底期货结算准备金'''
        return self.ReserveBalance

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getPreFundMortgageIn(self):
        '''上次货币质入金额'''
        return self.PreFundMortgageIn

    def getPreFundMortgageOut(self):
        '''上次货币质出金额'''
        return self.PreFundMortgageOut

    def getFundMortgageIn(self):
        '''货币质入金额'''
        return self.FundMortgageIn

    def getFundMortgageOut(self):
        '''货币质出金额'''
        return self.FundMortgageOut

    def getFundMortgageAvailable(self):
        '''货币质押余额'''
        return self.FundMortgageAvailable

    def getMortgageableFund(self):
        '''可质押货币金额'''
        return self.MortgageableFund

    def getSpecProductMargin(self):
        '''特殊产品占用保证金'''
        return self.SpecProductMargin

    def getSpecProductFrozenMargin(self):
        '''特殊产品冻结保证金'''
        return self.SpecProductFrozenMargin

    def getSpecProductCommission(self):
        '''特殊产品手续费'''
        return self.SpecProductCommission

    def getSpecProductFrozenCommission(self):
        '''特殊产品冻结手续费'''
        return self.SpecProductFrozenCommission

    def getSpecProductPositionProfit(self):
        '''特殊产品持仓盈亏'''
        return self.SpecProductPositionProfit

    def getSpecProductCloseProfit(self):
        '''特殊产品平仓盈亏'''
        return self.SpecProductCloseProfit

    def getSpecProductPositionProfitByAlg(self):
        '''根据持仓盈亏算法计算的特殊产品持仓盈亏'''
        return self.SpecProductPositionProfitByAlg

    def getSpecProductExchangeMargin(self):
        '''特殊产品交易所保证金'''
        return self.SpecProductExchangeMargin

    def getBizType(self):
        '''业务类型'''
        return TThostFtdcBizTypeType(ord(self.BizType)) if ord(self.BizType) in [e.value for e in list(TThostFtdcBizTypeType)] else list(TThostFtdcBizTypeType)[0]

    def getFrozenSwap(self):
        '''延时换汇冻结金额'''
        return self.FrozenSwap

    def getRemainSwap(self):
        '''剩余换汇额度'''
        return self.RemainSwap

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'PreMortgage'={self.getPreMortgage()}, 'PreCredit'={self.getPreCredit()}, 'PreDeposit'={self.getPreDeposit()}, 'PreBalance'={self.getPreBalance()}, 'PreMargin'={self.getPreMargin()}, 'InterestBase'={self.getInterestBase()}, 'Interest'={self.getInterest()}, 'Deposit'={self.getDeposit()}, 'Withdraw'={self.getWithdraw()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenCash'={self.getFrozenCash()}, 'FrozenCommission'={self.getFrozenCommission()}, 'CurrMargin'={self.getCurrMargin()}, 'CashIn'={self.getCashIn()}, 'Commission'={self.getCommission()}, 'CloseProfit'={self.getCloseProfit()}, 'PositionProfit'={self.getPositionProfit()}, 'Balance'={self.getBalance()}, 'Available'={self.getAvailable()}, 'WithdrawQuota'={self.getWithdrawQuota()}, 'Reserve'={self.getReserve()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'Credit'={self.getCredit()}, 'Mortgage'={self.getMortgage()}, 'ExchangeMargin'={self.getExchangeMargin()}, 'DeliveryMargin'={self.getDeliveryMargin()}, 'ExchangeDeliveryMargin'={self.getExchangeDeliveryMargin()}, 'ReserveBalance'={self.getReserveBalance()}, 'CurrencyID'={self.getCurrencyID()}, 'PreFundMortgageIn'={self.getPreFundMortgageIn()}, 'PreFundMortgageOut'={self.getPreFundMortgageOut()}, 'FundMortgageIn'={self.getFundMortgageIn()}, 'FundMortgageOut'={self.getFundMortgageOut()}, 'FundMortgageAvailable'={self.getFundMortgageAvailable()}, 'MortgageableFund'={self.getMortgageableFund()}, 'SpecProductMargin'={self.getSpecProductMargin()}, 'SpecProductFrozenMargin'={self.getSpecProductFrozenMargin()}, 'SpecProductCommission'={self.getSpecProductCommission()}, 'SpecProductFrozenCommission'={self.getSpecProductFrozenCommission()}, 'SpecProductPositionProfit'={self.getSpecProductPositionProfit()}, 'SpecProductCloseProfit'={self.getSpecProductCloseProfit()}, 'SpecProductPositionProfitByAlg'={self.getSpecProductPositionProfitByAlg()}, 'SpecProductExchangeMargin'={self.getSpecProductExchangeMargin()}, 'BizType'={self.getBizType()}, 'FrozenSwap'={self.getFrozenSwap()}, 'RemainSwap'={self.getRemainSwap()}"


class  CThostFtdcInvestorPositionField(Structure):
    """投资者持仓"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", c_int32),
        ("Position", c_int32),
        ("LongFrozen", c_int32),
        ("ShortFrozen", c_int32),
        ("LongFrozenAmount", c_double),
        ("ShortFrozenAmount", c_double),
        ("OpenVolume", c_int32),
        ("CloseVolume", c_int32),
        ("OpenAmount", c_double),
        ("CloseAmount", c_double),
        ("PositionCost", c_double),
        ("PreMargin", c_double),
        ("UseMargin", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("PreSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OpenCost", c_double),
        ("ExchangeMargin", c_double),
        ("CombPosition", c_int32),
        ("CombLongFrozen", c_int32),
        ("CombShortFrozen", c_int32),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("TodayPosition", c_int32),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("StrikeFrozen", c_int32),
        ("StrikeFrozenAmount", c_double),
        ("AbandonFrozen", c_int32),
        ("ExchangeID", c_char*9),
        ("YdStrikeFrozen", c_int32),
        ("InvestUnitID", c_char*17),
        ("PositionCostOffset", c_double),
        ("TasPosition", c_int32),
        ("TasPositionCost", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getPosiDirection(self):
        '''持仓多空方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getPositionDate(self):
        '''持仓日期'''
        return TThostFtdcPositionDateType(ord(self.PositionDate)) if ord(self.PositionDate) in [e.value for e in list(TThostFtdcPositionDateType)] else list(TThostFtdcPositionDateType)[0]

    def getYdPosition(self):
        '''上日持仓'''
        return self.YdPosition

    def getPosition(self):
        '''今日持仓'''
        return self.Position

    def getLongFrozen(self):
        '''多头冻结'''
        return self.LongFrozen

    def getShortFrozen(self):
        '''空头冻结'''
        return self.ShortFrozen

    def getLongFrozenAmount(self):
        '''开仓冻结金额'''
        return self.LongFrozenAmount

    def getShortFrozenAmount(self):
        '''开仓冻结金额'''
        return self.ShortFrozenAmount

    def getOpenVolume(self):
        '''开仓量'''
        return self.OpenVolume

    def getCloseVolume(self):
        '''平仓量'''
        return self.CloseVolume

    def getOpenAmount(self):
        '''开仓金额'''
        return self.OpenAmount

    def getCloseAmount(self):
        '''平仓金额'''
        return self.CloseAmount

    def getPositionCost(self):
        '''持仓成本'''
        return self.PositionCost

    def getPreMargin(self):
        '''上次占用的保证金'''
        return self.PreMargin

    def getUseMargin(self):
        '''占用的保证金'''
        return self.UseMargin

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenCash(self):
        '''冻结的资金'''
        return self.FrozenCash

    def getFrozenCommission(self):
        '''冻结的手续费'''
        return self.FrozenCommission

    def getCashIn(self):
        '''资金差额'''
        return self.CashIn

    def getCommission(self):
        '''手续费'''
        return self.Commission

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getPreSettlementPrice(self):
        '''上次结算价'''
        return self.PreSettlementPrice

    def getSettlementPrice(self):
        '''本次结算价'''
        return self.SettlementPrice

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOpenCost(self):
        '''开仓成本'''
        return self.OpenCost

    def getExchangeMargin(self):
        '''交易所保证金'''
        return self.ExchangeMargin

    def getCombPosition(self):
        '''组合成交形成的持仓'''
        return self.CombPosition

    def getCombLongFrozen(self):
        '''组合多头冻结'''
        return self.CombLongFrozen

    def getCombShortFrozen(self):
        '''组合空头冻结'''
        return self.CombShortFrozen

    def getCloseProfitByDate(self):
        '''逐日盯市平仓盈亏'''
        return self.CloseProfitByDate

    def getCloseProfitByTrade(self):
        '''逐笔对冲平仓盈亏'''
        return self.CloseProfitByTrade

    def getTodayPosition(self):
        '''今日持仓'''
        return self.TodayPosition

    def getMarginRateByMoney(self):
        '''保证金率'''
        return self.MarginRateByMoney

    def getMarginRateByVolume(self):
        '''保证金率(按手数)'''
        return self.MarginRateByVolume

    def getStrikeFrozen(self):
        '''执行冻结'''
        return self.StrikeFrozen

    def getStrikeFrozenAmount(self):
        '''执行冻结金额'''
        return self.StrikeFrozenAmount

    def getAbandonFrozen(self):
        '''放弃执行冻结'''
        return self.AbandonFrozen

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getYdStrikeFrozen(self):
        '''执行冻结的昨仓'''
        return self.YdStrikeFrozen

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getPositionCostOffset(self):
        '''大商所持仓成本差值，只有大商所使用'''
        return self.PositionCostOffset

    def getTasPosition(self):
        '''tas持仓手数'''
        return self.TasPosition

    def getTasPositionCost(self):
        '''tas持仓成本'''
        return self.TasPositionCost

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'PosiDirection'={self.getPosiDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'PositionDate'={self.getPositionDate()}, 'YdPosition'={self.getYdPosition()}, 'Position'={self.getPosition()}, 'LongFrozen'={self.getLongFrozen()}, 'ShortFrozen'={self.getShortFrozen()}, 'LongFrozenAmount'={self.getLongFrozenAmount()}, 'ShortFrozenAmount'={self.getShortFrozenAmount()}, 'OpenVolume'={self.getOpenVolume()}, 'CloseVolume'={self.getCloseVolume()}, 'OpenAmount'={self.getOpenAmount()}, 'CloseAmount'={self.getCloseAmount()}, 'PositionCost'={self.getPositionCost()}, 'PreMargin'={self.getPreMargin()}, 'UseMargin'={self.getUseMargin()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenCash'={self.getFrozenCash()}, 'FrozenCommission'={self.getFrozenCommission()}, 'CashIn'={self.getCashIn()}, 'Commission'={self.getCommission()}, 'CloseProfit'={self.getCloseProfit()}, 'PositionProfit'={self.getPositionProfit()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OpenCost'={self.getOpenCost()}, 'ExchangeMargin'={self.getExchangeMargin()}, 'CombPosition'={self.getCombPosition()}, 'CombLongFrozen'={self.getCombLongFrozen()}, 'CombShortFrozen'={self.getCombShortFrozen()}, 'CloseProfitByDate'={self.getCloseProfitByDate()}, 'CloseProfitByTrade'={self.getCloseProfitByTrade()}, 'TodayPosition'={self.getTodayPosition()}, 'MarginRateByMoney'={self.getMarginRateByMoney()}, 'MarginRateByVolume'={self.getMarginRateByVolume()}, 'StrikeFrozen'={self.getStrikeFrozen()}, 'StrikeFrozenAmount'={self.getStrikeFrozenAmount()}, 'AbandonFrozen'={self.getAbandonFrozen()}, 'ExchangeID'={self.getExchangeID()}, 'YdStrikeFrozen'={self.getYdStrikeFrozen()}, 'InvestUnitID'={self.getInvestUnitID()}, 'PositionCostOffset'={self.getPositionCostOffset()}, 'TasPosition'={self.getTasPosition()}, 'TasPositionCost'={self.getTasPositionCost()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInstrumentMarginRateField(Structure):
    """合约保证金率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int32),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getIsRelative(self):
        '''是否相对交易所收取'''
        return self.IsRelative

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'IsRelative'={self.getIsRelative()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInstrumentCommissionRateField(Structure):
    """合约手续费率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("ExchangeID", c_char*9),
        ("BizType", c_char),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOpenRatioByMoney(self):
        '''开仓手续费率'''
        return self.OpenRatioByMoney

    def getOpenRatioByVolume(self):
        '''开仓手续费'''
        return self.OpenRatioByVolume

    def getCloseRatioByMoney(self):
        '''平仓手续费率'''
        return self.CloseRatioByMoney

    def getCloseRatioByVolume(self):
        '''平仓手续费'''
        return self.CloseRatioByVolume

    def getCloseTodayRatioByMoney(self):
        '''平今手续费率'''
        return self.CloseTodayRatioByMoney

    def getCloseTodayRatioByVolume(self):
        '''平今手续费'''
        return self.CloseTodayRatioByVolume

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBizType(self):
        '''业务类型'''
        return TThostFtdcBizTypeType(ord(self.BizType)) if ord(self.BizType) in [e.value for e in list(TThostFtdcBizTypeType)] else list(TThostFtdcBizTypeType)[0]

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OpenRatioByMoney'={self.getOpenRatioByMoney()}, 'OpenRatioByVolume'={self.getOpenRatioByVolume()}, 'CloseRatioByMoney'={self.getCloseRatioByMoney()}, 'CloseRatioByVolume'={self.getCloseRatioByVolume()}, 'CloseTodayRatioByMoney'={self.getCloseTodayRatioByMoney()}, 'CloseTodayRatioByVolume'={self.getCloseTodayRatioByVolume()}, 'ExchangeID'={self.getExchangeID()}, 'BizType'={self.getBizType()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcDepthMarketDataField(Structure):
    """深度行情"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("reserve2", c_char*31),
        ("LastPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("ClosePrice", c_double),
        ("SettlementPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("PreDelta", c_double),
        ("CurrDelta", c_double),
        ("UpdateTime", c_char*9),
        ("UpdateMillisec", c_int32),
        ("BidPrice1", c_double),
        ("BidVolume1", c_int32),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int32),
        ("BidPrice2", c_double),
        ("BidVolume2", c_int32),
        ("AskPrice2", c_double),
        ("AskVolume2", c_int32),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int32),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int32),
        ("BidPrice4", c_double),
        ("BidVolume4", c_int32),
        ("AskPrice4", c_double),
        ("AskVolume4", c_int32),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int32),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int32),
        ("AveragePrice", c_double),
        ("ActionDay", c_char*9),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getPreSettlementPrice(self):
        '''上次结算价'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getSettlementPrice(self):
        '''本次结算价'''
        return self.SettlementPrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getBidPrice1(self):
        '''申买价一'''
        return self.BidPrice1

    def getBidVolume1(self):
        '''申买量一'''
        return self.BidVolume1

    def getAskPrice1(self):
        '''申卖价一'''
        return self.AskPrice1

    def getAskVolume1(self):
        '''申卖量一'''
        return self.AskVolume1

    def getBidPrice2(self):
        '''申买价二'''
        return self.BidPrice2

    def getBidVolume2(self):
        '''申买量二'''
        return self.BidVolume2

    def getAskPrice2(self):
        '''申卖价二'''
        return self.AskPrice2

    def getAskVolume2(self):
        '''申卖量二'''
        return self.AskVolume2

    def getBidPrice3(self):
        '''申买价三'''
        return self.BidPrice3

    def getBidVolume3(self):
        '''申买量三'''
        return self.BidVolume3

    def getAskPrice3(self):
        '''申卖价三'''
        return self.AskPrice3

    def getAskVolume3(self):
        '''申卖量三'''
        return self.AskVolume3

    def getBidPrice4(self):
        '''申买价四'''
        return self.BidPrice4

    def getBidVolume4(self):
        '''申买量四'''
        return self.BidVolume4

    def getAskPrice4(self):
        '''申卖价四'''
        return self.AskPrice4

    def getAskVolume4(self):
        '''申卖量四'''
        return self.AskVolume4

    def getBidPrice5(self):
        '''申买价五'''
        return self.BidPrice5

    def getBidVolume5(self):
        '''申买量五'''
        return self.BidVolume5

    def getAskPrice5(self):
        '''申卖价五'''
        return self.AskPrice5

    def getAskVolume5(self):
        '''申卖量五'''
        return self.AskVolume5

    def getAveragePrice(self):
        '''当日均价'''
        return self.AveragePrice

    def getActionDay(self):
        '''业务日期'''
        return str(self.ActionDay, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'reserve2'={self.getreserve2()}, 'LastPrice'={self.getLastPrice()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}, 'ClosePrice'={self.getClosePrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'PreDelta'={self.getPreDelta()}, 'CurrDelta'={self.getCurrDelta()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'BidPrice1'={self.getBidPrice1()}, 'BidVolume1'={self.getBidVolume1()}, 'AskPrice1'={self.getAskPrice1()}, 'AskVolume1'={self.getAskVolume1()}, 'BidPrice2'={self.getBidPrice2()}, 'BidVolume2'={self.getBidVolume2()}, 'AskPrice2'={self.getAskPrice2()}, 'AskVolume2'={self.getAskVolume2()}, 'BidPrice3'={self.getBidPrice3()}, 'BidVolume3'={self.getBidVolume3()}, 'AskPrice3'={self.getAskPrice3()}, 'AskVolume3'={self.getAskVolume3()}, 'BidPrice4'={self.getBidPrice4()}, 'BidVolume4'={self.getBidVolume4()}, 'AskPrice4'={self.getAskPrice4()}, 'AskVolume4'={self.getAskVolume4()}, 'BidPrice5'={self.getBidPrice5()}, 'BidVolume5'={self.getBidVolume5()}, 'AskPrice5'={self.getAskPrice5()}, 'AskVolume5'={self.getAskVolume5()}, 'AveragePrice'={self.getAveragePrice()}, 'ActionDay'={self.getActionDay()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcInstrumentTradingRightField(Structure):
    """投资者合约交易权限"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("TradingRight", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getTradingRight(self):
        '''交易权限'''
        return TThostFtdcTradingRightType(ord(self.TradingRight)) if ord(self.TradingRight) in [e.value for e in list(TThostFtdcTradingRightType)] else list(TThostFtdcTradingRightType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'TradingRight'={self.getTradingRight()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcBrokerUserField(Structure):
    """经纪公司用户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserName", c_char*81),
        ("UserType", c_char),
        ("IsActive", c_int32),
        ("IsUsingOTP", c_int32),
        ("IsAuthForce", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserName(self):
        '''用户名称'''
        return str(self.UserName, 'GBK')

    def getUserType(self):
        '''用户类型'''
        return TThostFtdcUserTypeType(ord(self.UserType)) if ord(self.UserType) in [e.value for e in list(TThostFtdcUserTypeType)] else list(TThostFtdcUserTypeType)[0]

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getIsUsingOTP(self):
        '''是否使用令牌'''
        return self.IsUsingOTP

    def getIsAuthForce(self):
        '''是否强制终端认证'''
        return self.IsAuthForce

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserName'={self.getUserName()}, 'UserType'={self.getUserType()}, 'IsActive'={self.getIsActive()}, 'IsUsingOTP'={self.getIsUsingOTP()}, 'IsAuthForce'={self.getIsAuthForce()}"


class  CThostFtdcBrokerUserPasswordField(Structure):
    """经纪公司用户口令"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("Password", c_char*41),
        ("LastUpdateTime", c_char*17),
        ("LastLoginTime", c_char*17),
        ("ExpireDate", c_char*9),
        ("WeakExpireDate", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getLastUpdateTime(self):
        '''上次修改时间'''
        return str(self.LastUpdateTime, 'GBK')

    def getLastLoginTime(self):
        '''上次登陆时间'''
        return str(self.LastLoginTime, 'GBK')

    def getExpireDate(self):
        '''密码过期时间'''
        return str(self.ExpireDate, 'GBK')

    def getWeakExpireDate(self):
        '''弱密码过期时间'''
        return str(self.WeakExpireDate, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'LastUpdateTime'={self.getLastUpdateTime()}, 'LastLoginTime'={self.getLastLoginTime()}, 'ExpireDate'={self.getExpireDate()}, 'WeakExpireDate'={self.getWeakExpireDate()}"


class  CThostFtdcBrokerUserFunctionField(Structure):
    """经纪公司用户功能权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("BrokerFunctionCode", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getBrokerFunctionCode(self):
        '''经纪公司功能代码'''
        return TThostFtdcBrokerFunctionCodeType(ord(self.BrokerFunctionCode)) if ord(self.BrokerFunctionCode) in [e.value for e in list(TThostFtdcBrokerFunctionCodeType)] else list(TThostFtdcBrokerFunctionCodeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'BrokerFunctionCode'={self.getBrokerFunctionCode()}"


class  CThostFtdcTraderOfferField(Structure):
    """交易所交易员报盘机"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ParticipantID", c_char*11),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", c_char*9),
        ("ConnectRequestTime", c_char*9),
        ("LastReportDate", c_char*9),
        ("LastReportTime", c_char*9),
        ("ConnectDate", c_char*9),
        ("ConnectTime", c_char*9),
        ("StartDate", c_char*9),
        ("StartTime", c_char*9),
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("MaxTradeID", c_char*21),
        ("MaxOrderMessageReference", c_char*7),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getTraderConnectStatus(self):
        '''交易所交易员连接状态'''
        return TThostFtdcTraderConnectStatusType(ord(self.TraderConnectStatus)) if ord(self.TraderConnectStatus) in [e.value for e in list(TThostFtdcTraderConnectStatusType)] else list(TThostFtdcTraderConnectStatusType)[0]

    def getConnectRequestDate(self):
        '''发出连接请求的日期'''
        return str(self.ConnectRequestDate, 'GBK')

    def getConnectRequestTime(self):
        '''发出连接请求的时间'''
        return str(self.ConnectRequestTime, 'GBK')

    def getLastReportDate(self):
        '''上次报告日期'''
        return str(self.LastReportDate, 'GBK')

    def getLastReportTime(self):
        '''上次报告时间'''
        return str(self.LastReportTime, 'GBK')

    def getConnectDate(self):
        '''完成连接日期'''
        return str(self.ConnectDate, 'GBK')

    def getConnectTime(self):
        '''完成连接时间'''
        return str(self.ConnectTime, 'GBK')

    def getStartDate(self):
        '''启动日期'''
        return str(self.StartDate, 'GBK')

    def getStartTime(self):
        '''启动时间'''
        return str(self.StartTime, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getMaxTradeID(self):
        '''本席位最大成交编号'''
        return str(self.MaxTradeID, 'GBK')

    def getMaxOrderMessageReference(self):
        '''本席位最大报单备拷'''
        return str(self.MaxOrderMessageReference, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ParticipantID'={self.getParticipantID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'TraderConnectStatus'={self.getTraderConnectStatus()}, 'ConnectRequestDate'={self.getConnectRequestDate()}, 'ConnectRequestTime'={self.getConnectRequestTime()}, 'LastReportDate'={self.getLastReportDate()}, 'LastReportTime'={self.getLastReportTime()}, 'ConnectDate'={self.getConnectDate()}, 'ConnectTime'={self.getConnectTime()}, 'StartDate'={self.getStartDate()}, 'StartTime'={self.getStartTime()}, 'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'MaxTradeID'={self.getMaxTradeID()}, 'MaxOrderMessageReference'={self.getMaxOrderMessageReference()}"


class  CThostFtdcSettlementInfoField(Structure):
    """投资者结算结果"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("SequenceNo", c_int32),
        ("Content", c_char*501),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getContent(self):
        '''消息正文'''
        return str(self.Content, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'SequenceNo'={self.getSequenceNo()}, 'Content'={self.getContent()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcInstrumentMarginRateAdjustField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int32),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getIsRelative(self):
        '''是否相对交易所收取'''
        return self.IsRelative

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'IsRelative'={self.getIsRelative()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeMarginRateField(Structure):
    """交易所保证金率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeMarginRateAdjustField(Structure):
    """交易所保证金率调整"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("ExchLongMarginRatioByMoney", c_double),
        ("ExchLongMarginRatioByVolume", c_double),
        ("ExchShortMarginRatioByMoney", c_double),
        ("ExchShortMarginRatioByVolume", c_double),
        ("NoLongMarginRatioByMoney", c_double),
        ("NoLongMarginRatioByVolume", c_double),
        ("NoShortMarginRatioByMoney", c_double),
        ("NoShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''跟随交易所投资者多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''跟随交易所投资者多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''跟随交易所投资者空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''跟随交易所投资者空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getExchLongMarginRatioByMoney(self):
        '''交易所多头保证金率'''
        return self.ExchLongMarginRatioByMoney

    def getExchLongMarginRatioByVolume(self):
        '''交易所多头保证金费'''
        return self.ExchLongMarginRatioByVolume

    def getExchShortMarginRatioByMoney(self):
        '''交易所空头保证金率'''
        return self.ExchShortMarginRatioByMoney

    def getExchShortMarginRatioByVolume(self):
        '''交易所空头保证金费'''
        return self.ExchShortMarginRatioByVolume

    def getNoLongMarginRatioByMoney(self):
        '''不跟随交易所投资者多头保证金率'''
        return self.NoLongMarginRatioByMoney

    def getNoLongMarginRatioByVolume(self):
        '''不跟随交易所投资者多头保证金费'''
        return self.NoLongMarginRatioByVolume

    def getNoShortMarginRatioByMoney(self):
        '''不跟随交易所投资者空头保证金率'''
        return self.NoShortMarginRatioByMoney

    def getNoShortMarginRatioByVolume(self):
        '''不跟随交易所投资者空头保证金费'''
        return self.NoShortMarginRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'ExchLongMarginRatioByMoney'={self.getExchLongMarginRatioByMoney()}, 'ExchLongMarginRatioByVolume'={self.getExchLongMarginRatioByVolume()}, 'ExchShortMarginRatioByMoney'={self.getExchShortMarginRatioByMoney()}, 'ExchShortMarginRatioByVolume'={self.getExchShortMarginRatioByVolume()}, 'NoLongMarginRatioByMoney'={self.getNoLongMarginRatioByMoney()}, 'NoLongMarginRatioByVolume'={self.getNoLongMarginRatioByVolume()}, 'NoShortMarginRatioByMoney'={self.getNoShortMarginRatioByMoney()}, 'NoShortMarginRatioByVolume'={self.getNoShortMarginRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeRateField(Structure):
    """汇率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("FromCurrencyID", c_char*4),
        ("FromCurrencyUnit", c_double),
        ("ToCurrencyID", c_char*4),
        ("ExchangeRate", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getFromCurrencyID(self):
        '''源币种'''
        return str(self.FromCurrencyID, 'GBK')

    def getFromCurrencyUnit(self):
        '''源币种单位数量'''
        return self.FromCurrencyUnit

    def getToCurrencyID(self):
        '''目标币种'''
        return str(self.ToCurrencyID, 'GBK')

    def getExchangeRate(self):
        '''汇率'''
        return self.ExchangeRate

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'FromCurrencyID'={self.getFromCurrencyID()}, 'FromCurrencyUnit'={self.getFromCurrencyUnit()}, 'ToCurrencyID'={self.getToCurrencyID()}, 'ExchangeRate'={self.getExchangeRate()}"


class  CThostFtdcSettlementRefField(Structure):
    """结算引用"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}"


class  CThostFtdcCurrentTimeField(Structure):
    """当前时间"""
    _fields_ = [
        ("CurrDate", c_char*9),
        ("CurrTime", c_char*9),
        ("CurrMillisec", c_int32),
        ("ActionDay", c_char*9),
    ]

    def getCurrDate(self):
        '''当前日期'''
        return str(self.CurrDate, 'GBK')

    def getCurrTime(self):
        '''当前时间'''
        return str(self.CurrTime, 'GBK')

    def getCurrMillisec(self):
        '''当前时间（毫秒）'''
        return self.CurrMillisec

    def getActionDay(self):
        '''业务日期'''
        return str(self.ActionDay, 'GBK')

    def __str__(self): # 可以直接print
        return f"'CurrDate'={self.getCurrDate()}, 'CurrTime'={self.getCurrTime()}, 'CurrMillisec'={self.getCurrMillisec()}, 'ActionDay'={self.getActionDay()}"


class  CThostFtdcCommPhaseField(Structure):
    """通讯阶段"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("CommPhaseNo", c_short),
        ("SystemID", c_char*21),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getCommPhaseNo(self):
        '''通讯时段编号'''
        return self.CommPhaseNo

    def getSystemID(self):
        '''系统编号'''
        return str(self.SystemID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'CommPhaseNo'={self.getCommPhaseNo()}, 'SystemID'={self.getSystemID()}"


class  CThostFtdcLoginInfoField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("LoginDate", c_char*9),
        ("LoginTime", c_char*9),
        ("reserve1", c_char*16),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("SystemName", c_char*41),
        ("PasswordDeprecated", c_char*41),
        ("MaxOrderRef", c_char*13),
        ("SHFETime", c_char*9),
        ("DCETime", c_char*9),
        ("CZCETime", c_char*9),
        ("FFEXTime", c_char*9),
        ("MacAddress", c_char*21),
        ("OneTimePassword", c_char*41),
        ("INETime", c_char*9),
        ("IsQryControl", c_int32),
        ("LoginRemark", c_char*36),
        ("Password", c_char*41),
        ("IPAddress", c_char*33),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getLoginDate(self):
        '''登录日期'''
        return str(self.LoginDate, 'GBK')

    def getLoginTime(self):
        '''登录时间'''
        return str(self.LoginTime, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getSystemName(self):
        '''系统名称'''
        return str(self.SystemName, 'GBK')

    def getPasswordDeprecated(self):
        '''密码,已弃用'''
        return str(self.PasswordDeprecated, 'GBK')

    def getMaxOrderRef(self):
        '''最大报单引用'''
        return str(self.MaxOrderRef, 'GBK')

    def getSHFETime(self):
        '''上期所时间'''
        return str(self.SHFETime, 'GBK')

    def getDCETime(self):
        '''大商所时间'''
        return str(self.DCETime, 'GBK')

    def getCZCETime(self):
        '''郑商所时间'''
        return str(self.CZCETime, 'GBK')

    def getFFEXTime(self):
        '''中金所时间'''
        return str(self.FFEXTime, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getOneTimePassword(self):
        '''动态密码'''
        return str(self.OneTimePassword, 'GBK')

    def getINETime(self):
        '''能源中心时间'''
        return str(self.INETime, 'GBK')

    def getIsQryControl(self):
        '''查询时是否需要流控'''
        return self.IsQryControl

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'LoginDate'={self.getLoginDate()}, 'LoginTime'={self.getLoginTime()}, 'reserve1'={self.getreserve1()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'SystemName'={self.getSystemName()}, 'PasswordDeprecated'={self.getPasswordDeprecated()}, 'MaxOrderRef'={self.getMaxOrderRef()}, 'SHFETime'={self.getSHFETime()}, 'DCETime'={self.getDCETime()}, 'CZCETime'={self.getCZCETime()}, 'FFEXTime'={self.getFFEXTime()}, 'MacAddress'={self.getMacAddress()}, 'OneTimePassword'={self.getOneTimePassword()}, 'INETime'={self.getINETime()}, 'IsQryControl'={self.getIsQryControl()}, 'LoginRemark'={self.getLoginRemark()}, 'Password'={self.getPassword()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcLogoutAllField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("SystemName", c_char*41),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getSystemName(self):
        '''系统名称'''
        return str(self.SystemName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'SystemName'={self.getSystemName()}"


class  CThostFtdcFrontStatusField(Structure):
    """前置状态"""
    _fields_ = [
        ("FrontID", c_int32),
        ("LastReportDate", c_char*9),
        ("LastReportTime", c_char*9),
        ("IsActive", c_int32),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getLastReportDate(self):
        '''上次报告日期'''
        return str(self.LastReportDate, 'GBK')

    def getLastReportTime(self):
        '''上次报告时间'''
        return str(self.LastReportTime, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}, 'LastReportDate'={self.getLastReportDate()}, 'LastReportTime'={self.getLastReportTime()}, 'IsActive'={self.getIsActive()}"


class  CThostFtdcUserPasswordUpdateField(Structure):
    """用户口令变更"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("OldPassword", c_char*41),
        ("NewPassword", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOldPassword(self):
        '''原来的口令'''
        return str(self.OldPassword, 'GBK')

    def getNewPassword(self):
        '''新的口令'''
        return str(self.NewPassword, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'OldPassword'={self.getOldPassword()}, 'NewPassword'={self.getNewPassword()}"


class  CThostFtdcInputOrderField(Structure):
    """输入报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("UserForceClose", c_int32),
        ("IsSwapOrder", c_int32),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getUserForceClose(self):
        '''用户强评标志'''
        return self.UserForceClose

    def getIsSwapOrder(self):
        '''互换单标志'''
        return self.IsSwapOrder

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'UserForceClose'={self.getUserForceClose()}, 'IsSwapOrder'={self.getIsSwapOrder()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcOrderField(Structure):
    """报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OrderSysID", c_char*21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int32),
        ("VolumeTotal", c_int32),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("ActiveTime", c_char*9),
        ("SuspendTime", c_char*9),
        ("UpdateTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ActiveTraderID", c_char*21),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("UserForceClose", c_int32),
        ("ActiveUserID", c_char*16),
        ("BrokerOrderSeq", c_int32),
        ("RelativeOrderSysID", c_char*21),
        ("ZCETotalTradedVolume", c_int32),
        ("IsSwapOrder", c_int32),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''报单提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getOrderSource(self):
        '''报单来源'''
        return TThostFtdcOrderSourceType(ord(self.OrderSource)) if ord(self.OrderSource) in [e.value for e in list(TThostFtdcOrderSourceType)] else list(TThostFtdcOrderSourceType)[0]

    def getOrderStatus(self):
        '''报单状态'''
        return TThostFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TThostFtdcOrderStatusType)] else list(TThostFtdcOrderStatusType)[0]

    def getOrderType(self):
        '''报单类型'''
        return TThostFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TThostFtdcOrderTypeType)] else list(TThostFtdcOrderTypeType)[0]

    def getVolumeTraded(self):
        '''今成交数量'''
        return self.VolumeTraded

    def getVolumeTotal(self):
        '''剩余数量'''
        return self.VolumeTotal

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''委托时间'''
        return str(self.InsertTime, 'GBK')

    def getActiveTime(self):
        '''激活时间'''
        return str(self.ActiveTime, 'GBK')

    def getSuspendTime(self):
        '''挂起时间'''
        return str(self.SuspendTime, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getActiveTraderID(self):
        '''最后修改交易所交易员代码'''
        return str(self.ActiveTraderID, 'GBK')

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getUserForceClose(self):
        '''用户强评标志'''
        return self.UserForceClose

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerOrderSeq(self):
        '''经纪公司报单编号'''
        return self.BrokerOrderSeq

    def getRelativeOrderSysID(self):
        '''相关报单'''
        return str(self.RelativeOrderSysID, 'GBK')

    def getZCETotalTradedVolume(self):
        '''郑商所成交数量'''
        return self.ZCETotalTradedVolume

    def getIsSwapOrder(self):
        '''互换单标志'''
        return self.IsSwapOrder

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OrderSysID'={self.getOrderSysID()}, 'OrderSource'={self.getOrderSource()}, 'OrderStatus'={self.getOrderStatus()}, 'OrderType'={self.getOrderType()}, 'VolumeTraded'={self.getVolumeTraded()}, 'VolumeTotal'={self.getVolumeTotal()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'ActiveTime'={self.getActiveTime()}, 'SuspendTime'={self.getSuspendTime()}, 'UpdateTime'={self.getUpdateTime()}, 'CancelTime'={self.getCancelTime()}, 'ActiveTraderID'={self.getActiveTraderID()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'UserForceClose'={self.getUserForceClose()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerOrderSeq'={self.getBrokerOrderSeq()}, 'RelativeOrderSysID'={self.getRelativeOrderSysID()}, 'ZCETotalTradedVolume'={self.getZCETotalTradedVolume()}, 'IsSwapOrder'={self.getIsSwapOrder()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExchangeOrderField(Structure):
    """交易所报单"""
    _fields_ = [
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OrderSysID", c_char*21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int32),
        ("VolumeTotal", c_int32),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("ActiveTime", c_char*9),
        ("SuspendTime", c_char*9),
        ("UpdateTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ActiveTraderID", c_char*21),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("BranchID", c_char*9),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''报单提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getOrderSource(self):
        '''报单来源'''
        return TThostFtdcOrderSourceType(ord(self.OrderSource)) if ord(self.OrderSource) in [e.value for e in list(TThostFtdcOrderSourceType)] else list(TThostFtdcOrderSourceType)[0]

    def getOrderStatus(self):
        '''报单状态'''
        return TThostFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TThostFtdcOrderStatusType)] else list(TThostFtdcOrderStatusType)[0]

    def getOrderType(self):
        '''报单类型'''
        return TThostFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TThostFtdcOrderTypeType)] else list(TThostFtdcOrderTypeType)[0]

    def getVolumeTraded(self):
        '''今成交数量'''
        return self.VolumeTraded

    def getVolumeTotal(self):
        '''剩余数量'''
        return self.VolumeTotal

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''委托时间'''
        return str(self.InsertTime, 'GBK')

    def getActiveTime(self):
        '''激活时间'''
        return str(self.ActiveTime, 'GBK')

    def getSuspendTime(self):
        '''挂起时间'''
        return str(self.SuspendTime, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getActiveTraderID(self):
        '''最后修改交易所交易员代码'''
        return str(self.ActiveTraderID, 'GBK')

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OrderSysID'={self.getOrderSysID()}, 'OrderSource'={self.getOrderSource()}, 'OrderStatus'={self.getOrderStatus()}, 'OrderType'={self.getOrderType()}, 'VolumeTraded'={self.getVolumeTraded()}, 'VolumeTotal'={self.getVolumeTotal()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'ActiveTime'={self.getActiveTime()}, 'SuspendTime'={self.getSuspendTime()}, 'UpdateTime'={self.getUpdateTime()}, 'CancelTime'={self.getCancelTime()}, 'ActiveTraderID'={self.getActiveTraderID()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'BranchID'={self.getBranchID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExchangeOrderInsertErrorField(Structure):
    """交易所报单插入失败"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcInputOrderActionField(Structure):
    """输入报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("OrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'OrderRef'={self.getOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcOrderActionField(Structure):
    """报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("OrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("StatusMsg", c_char*81),
        ("reserve1", c_char*31),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'OrderRef'={self.getOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve1'={self.getreserve1()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExchangeOrderActionField(Structure):
    """交易所报单操作"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("BranchID", c_char*9),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'BranchID'={self.getBranchID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExchangeOrderActionErrorField(Structure):
    """交易所报单操作失败"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcExchangeTradeField(Structure):
    """交易所成交"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("TradeID", c_char*21),
        ("Direction", c_char),
        ("OrderSysID", c_char*21),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("TradingRole", c_char),
        ("reserve1", c_char*31),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", c_double),
        ("Volume", c_int32),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", c_char*21),
        ("OrderLocalID", c_char*13),
        ("ClearingPartID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("SequenceNo", c_int32),
        ("TradeSource", c_char),
        ("ExchangeInstID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getTradingRole(self):
        '''交易角色'''
        return TThostFtdcTradingRoleType(ord(self.TradingRole)) if ord(self.TradingRole) in [e.value for e in list(TThostFtdcTradingRoleType)] else list(TThostFtdcTradingRoleType)[0]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getPrice(self):
        '''价格'''
        return self.Price

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTradeDate(self):
        '''成交时期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''成交时间'''
        return str(self.TradeTime, 'GBK')

    def getTradeType(self):
        '''成交类型'''
        return TThostFtdcTradeTypeType(ord(self.TradeType)) if ord(self.TradeType) in [e.value for e in list(TThostFtdcTradeTypeType)] else list(TThostFtdcTradeTypeType)[0]

    def getPriceSource(self):
        '''成交价来源'''
        return TThostFtdcPriceSourceType(ord(self.PriceSource)) if ord(self.PriceSource) in [e.value for e in list(TThostFtdcPriceSourceType)] else list(TThostFtdcPriceSourceType)[0]

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getTradeSource(self):
        '''成交来源'''
        return TThostFtdcTradeSourceType(ord(self.TradeSource)) if ord(self.TradeSource) in [e.value for e in list(TThostFtdcTradeSourceType)] else list(TThostFtdcTradeSourceType)[0]

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TradeID'={self.getTradeID()}, 'Direction'={self.getDirection()}, 'OrderSysID'={self.getOrderSysID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'TradingRole'={self.getTradingRole()}, 'reserve1'={self.getreserve1()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Price'={self.getPrice()}, 'Volume'={self.getVolume()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'TradeType'={self.getTradeType()}, 'PriceSource'={self.getPriceSource()}, 'TraderID'={self.getTraderID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ClearingPartID'={self.getClearingPartID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'SequenceNo'={self.getSequenceNo()}, 'TradeSource'={self.getTradeSource()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcTradeField(Structure):
    """成交"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("ExchangeID", c_char*9),
        ("TradeID", c_char*21),
        ("Direction", c_char),
        ("OrderSysID", c_char*21),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("TradingRole", c_char),
        ("reserve2", c_char*31),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", c_double),
        ("Volume", c_int32),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", c_char*21),
        ("OrderLocalID", c_char*13),
        ("ClearingPartID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("SequenceNo", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("BrokerOrderSeq", c_int32),
        ("TradeSource", c_char),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getTradingRole(self):
        '''交易角色'''
        return TThostFtdcTradingRoleType(ord(self.TradingRole)) if ord(self.TradingRole) in [e.value for e in list(TThostFtdcTradingRoleType)] else list(TThostFtdcTradingRoleType)[0]

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getPrice(self):
        '''价格'''
        return self.Price

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTradeDate(self):
        '''成交时期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''成交时间'''
        return str(self.TradeTime, 'GBK')

    def getTradeType(self):
        '''成交类型'''
        return TThostFtdcTradeTypeType(ord(self.TradeType)) if ord(self.TradeType) in [e.value for e in list(TThostFtdcTradeTypeType)] else list(TThostFtdcTradeTypeType)[0]

    def getPriceSource(self):
        '''成交价来源'''
        return TThostFtdcPriceSourceType(ord(self.PriceSource)) if ord(self.PriceSource) in [e.value for e in list(TThostFtdcPriceSourceType)] else list(TThostFtdcPriceSourceType)[0]

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getBrokerOrderSeq(self):
        '''经纪公司报单编号'''
        return self.BrokerOrderSeq

    def getTradeSource(self):
        '''成交来源'''
        return TThostFtdcTradeSourceType(ord(self.TradeSource)) if ord(self.TradeSource) in [e.value for e in list(TThostFtdcTradeSourceType)] else list(TThostFtdcTradeSourceType)[0]

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'ExchangeID'={self.getExchangeID()}, 'TradeID'={self.getTradeID()}, 'Direction'={self.getDirection()}, 'OrderSysID'={self.getOrderSysID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'TradingRole'={self.getTradingRole()}, 'reserve2'={self.getreserve2()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Price'={self.getPrice()}, 'Volume'={self.getVolume()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'TradeType'={self.getTradeType()}, 'PriceSource'={self.getPriceSource()}, 'TraderID'={self.getTraderID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ClearingPartID'={self.getClearingPartID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'SequenceNo'={self.getSequenceNo()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'BrokerOrderSeq'={self.getBrokerOrderSeq()}, 'TradeSource'={self.getTradeSource()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcUserSessionField(Structure):
    """用户会话"""
    _fields_ = [
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("LoginDate", c_char*9),
        ("LoginTime", c_char*9),
        ("reserve1", c_char*16),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("MacAddress", c_char*21),
        ("LoginRemark", c_char*36),
        ("IPAddress", c_char*33),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getLoginDate(self):
        '''登录日期'''
        return str(self.LoginDate, 'GBK')

    def getLoginTime(self):
        '''登录时间'''
        return str(self.LoginTime, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'LoginDate'={self.getLoginDate()}, 'LoginTime'={self.getLoginTime()}, 'reserve1'={self.getreserve1()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'MacAddress'={self.getMacAddress()}, 'LoginRemark'={self.getLoginRemark()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryMaxOrderVolumeField(Structure):
    """查询最大报单数量"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int32),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getMaxVolume(self):
        '''最大允许报单数量'''
        return self.MaxVolume

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'Direction'={self.getDirection()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'MaxVolume'={self.getMaxVolume()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcSettlementInfoConfirmField(Structure):
    """投资者结算结果确认信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ConfirmDate", c_char*9),
        ("ConfirmTime", c_char*9),
        ("SettlementID", c_int32),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getConfirmDate(self):
        '''确认日期'''
        return str(self.ConfirmDate, 'GBK')

    def getConfirmTime(self):
        '''确认时间'''
        return str(self.ConfirmTime, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ConfirmDate'={self.getConfirmDate()}, 'ConfirmTime'={self.getConfirmTime()}, 'SettlementID'={self.getSettlementID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcSyncDepositField(Structure):
    """出入金同步"""
    _fields_ = [
        ("DepositSeqNo", c_char*15),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Deposit", c_double),
        ("IsForce", c_int32),
        ("CurrencyID", c_char*4),
    ]

    def getDepositSeqNo(self):
        '''出入金流水号'''
        return str(self.DepositSeqNo, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getIsForce(self):
        '''是否强制进行'''
        return self.IsForce

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'DepositSeqNo'={self.getDepositSeqNo()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Deposit'={self.getDeposit()}, 'IsForce'={self.getIsForce()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcSyncFundMortgageField(Structure):
    """货币质押同步"""
    _fields_ = [
        ("MortgageSeqNo", c_char*15),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("FromCurrencyID", c_char*4),
        ("MortgageAmount", c_double),
        ("ToCurrencyID", c_char*4),
    ]

    def getMortgageSeqNo(self):
        '''货币质押流水号'''
        return str(self.MortgageSeqNo, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getFromCurrencyID(self):
        '''源币种'''
        return str(self.FromCurrencyID, 'GBK')

    def getMortgageAmount(self):
        '''质押金额'''
        return self.MortgageAmount

    def getToCurrencyID(self):
        '''目标币种'''
        return str(self.ToCurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'MortgageSeqNo'={self.getMortgageSeqNo()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'FromCurrencyID'={self.getFromCurrencyID()}, 'MortgageAmount'={self.getMortgageAmount()}, 'ToCurrencyID'={self.getToCurrencyID()}"


class  CThostFtdcBrokerSyncField(Structure):
    """经纪公司同步"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcSyncingInvestorField(Structure):
    """正在同步中的投资者"""
    _fields_ = [
        ("InvestorID", c_char*13),
        ("BrokerID", c_char*11),
        ("InvestorGroupID", c_char*13),
        ("InvestorName", c_char*81),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("IsActive", c_int32),
        ("Telephone", c_char*41),
        ("Address", c_char*101),
        ("OpenDate", c_char*9),
        ("Mobile", c_char*41),
        ("CommModelID", c_char*13),
        ("MarginModelID", c_char*13),
    ]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorGroupID(self):
        '''投资者分组代码'''
        return str(self.InvestorGroupID, 'GBK')

    def getInvestorName(self):
        '''投资者名称'''
        return str(self.InvestorName, 'GBK')

    def getIdentifiedCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdentifiedCardType)) if ord(self.IdentifiedCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getTelephone(self):
        '''联系电话'''
        return str(self.Telephone, 'GBK')

    def getAddress(self):
        '''通讯地址'''
        return str(self.Address, 'GBK')

    def getOpenDate(self):
        '''开户日期'''
        return str(self.OpenDate, 'GBK')

    def getMobile(self):
        '''手机'''
        return str(self.Mobile, 'GBK')

    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')

    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorGroupID'={self.getInvestorGroupID()}, 'InvestorName'={self.getInvestorName()}, 'IdentifiedCardType'={self.getIdentifiedCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'IsActive'={self.getIsActive()}, 'Telephone'={self.getTelephone()}, 'Address'={self.getAddress()}, 'OpenDate'={self.getOpenDate()}, 'Mobile'={self.getMobile()}, 'CommModelID'={self.getCommModelID()}, 'MarginModelID'={self.getMarginModelID()}"


class  CThostFtdcSyncingTradingCodeField(Structure):
    """正在同步中的交易代码"""
    _fields_ = [
        ("InvestorID", c_char*13),
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
        ("ClientID", c_char*11),
        ("IsActive", c_int32),
        ("ClientIDType", c_char),
    ]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getClientIDType(self):
        '''交易编码类型'''
        return TThostFtdcClientIDTypeType(ord(self.ClientIDType)) if ord(self.ClientIDType) in [e.value for e in list(TThostFtdcClientIDTypeType)] else list(TThostFtdcClientIDTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}, 'IsActive'={self.getIsActive()}, 'ClientIDType'={self.getClientIDType()}"


class  CThostFtdcSyncingInvestorGroupField(Structure):
    """正在同步中的投资者分组"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorGroupID", c_char*13),
        ("InvestorGroupName", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorGroupID(self):
        '''投资者分组代码'''
        return str(self.InvestorGroupID, 'GBK')

    def getInvestorGroupName(self):
        '''投资者分组名称'''
        return str(self.InvestorGroupName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorGroupID'={self.getInvestorGroupID()}, 'InvestorGroupName'={self.getInvestorGroupName()}"


class  CThostFtdcSyncingTradingAccountField(Structure):
    """正在同步中的交易账号"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("PreMortgage", c_double),
        ("PreCredit", c_double),
        ("PreDeposit", c_double),
        ("PreBalance", c_double),
        ("PreMargin", c_double),
        ("InterestBase", c_double),
        ("Interest", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CurrMargin", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Balance", c_double),
        ("Available", c_double),
        ("WithdrawQuota", c_double),
        ("Reserve", c_double),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("Credit", c_double),
        ("Mortgage", c_double),
        ("ExchangeMargin", c_double),
        ("DeliveryMargin", c_double),
        ("ExchangeDeliveryMargin", c_double),
        ("ReserveBalance", c_double),
        ("CurrencyID", c_char*4),
        ("PreFundMortgageIn", c_double),
        ("PreFundMortgageOut", c_double),
        ("FundMortgageIn", c_double),
        ("FundMortgageOut", c_double),
        ("FundMortgageAvailable", c_double),
        ("MortgageableFund", c_double),
        ("SpecProductMargin", c_double),
        ("SpecProductFrozenMargin", c_double),
        ("SpecProductCommission", c_double),
        ("SpecProductFrozenCommission", c_double),
        ("SpecProductPositionProfit", c_double),
        ("SpecProductCloseProfit", c_double),
        ("SpecProductPositionProfitByAlg", c_double),
        ("SpecProductExchangeMargin", c_double),
        ("FrozenSwap", c_double),
        ("RemainSwap", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPreMortgage(self):
        '''上次质押金额'''
        return self.PreMortgage

    def getPreCredit(self):
        '''上次信用额度'''
        return self.PreCredit

    def getPreDeposit(self):
        '''上次存款额'''
        return self.PreDeposit

    def getPreBalance(self):
        '''上次结算准备金'''
        return self.PreBalance

    def getPreMargin(self):
        '''上次占用的保证金'''
        return self.PreMargin

    def getInterestBase(self):
        '''利息基数'''
        return self.InterestBase

    def getInterest(self):
        '''利息收入'''
        return self.Interest

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getWithdraw(self):
        '''出金金额'''
        return self.Withdraw

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenCash(self):
        '''冻结的资金'''
        return self.FrozenCash

    def getFrozenCommission(self):
        '''冻结的手续费'''
        return self.FrozenCommission

    def getCurrMargin(self):
        '''当前保证金总额'''
        return self.CurrMargin

    def getCashIn(self):
        '''资金差额'''
        return self.CashIn

    def getCommission(self):
        '''手续费'''
        return self.Commission

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getBalance(self):
        '''期货结算准备金'''
        return self.Balance

    def getAvailable(self):
        '''可用资金'''
        return self.Available

    def getWithdrawQuota(self):
        '''可取资金'''
        return self.WithdrawQuota

    def getReserve(self):
        '''基本准备金'''
        return self.Reserve

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getCredit(self):
        '''信用额度'''
        return self.Credit

    def getMortgage(self):
        '''质押金额'''
        return self.Mortgage

    def getExchangeMargin(self):
        '''交易所保证金'''
        return self.ExchangeMargin

    def getDeliveryMargin(self):
        '''投资者交割保证金'''
        return self.DeliveryMargin

    def getExchangeDeliveryMargin(self):
        '''交易所交割保证金'''
        return self.ExchangeDeliveryMargin

    def getReserveBalance(self):
        '''保底期货结算准备金'''
        return self.ReserveBalance

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getPreFundMortgageIn(self):
        '''上次货币质入金额'''
        return self.PreFundMortgageIn

    def getPreFundMortgageOut(self):
        '''上次货币质出金额'''
        return self.PreFundMortgageOut

    def getFundMortgageIn(self):
        '''货币质入金额'''
        return self.FundMortgageIn

    def getFundMortgageOut(self):
        '''货币质出金额'''
        return self.FundMortgageOut

    def getFundMortgageAvailable(self):
        '''货币质押余额'''
        return self.FundMortgageAvailable

    def getMortgageableFund(self):
        '''可质押货币金额'''
        return self.MortgageableFund

    def getSpecProductMargin(self):
        '''特殊产品占用保证金'''
        return self.SpecProductMargin

    def getSpecProductFrozenMargin(self):
        '''特殊产品冻结保证金'''
        return self.SpecProductFrozenMargin

    def getSpecProductCommission(self):
        '''特殊产品手续费'''
        return self.SpecProductCommission

    def getSpecProductFrozenCommission(self):
        '''特殊产品冻结手续费'''
        return self.SpecProductFrozenCommission

    def getSpecProductPositionProfit(self):
        '''特殊产品持仓盈亏'''
        return self.SpecProductPositionProfit

    def getSpecProductCloseProfit(self):
        '''特殊产品平仓盈亏'''
        return self.SpecProductCloseProfit

    def getSpecProductPositionProfitByAlg(self):
        '''根据持仓盈亏算法计算的特殊产品持仓盈亏'''
        return self.SpecProductPositionProfitByAlg

    def getSpecProductExchangeMargin(self):
        '''特殊产品交易所保证金'''
        return self.SpecProductExchangeMargin

    def getFrozenSwap(self):
        '''延时换汇冻结金额'''
        return self.FrozenSwap

    def getRemainSwap(self):
        '''剩余换汇额度'''
        return self.RemainSwap

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'PreMortgage'={self.getPreMortgage()}, 'PreCredit'={self.getPreCredit()}, 'PreDeposit'={self.getPreDeposit()}, 'PreBalance'={self.getPreBalance()}, 'PreMargin'={self.getPreMargin()}, 'InterestBase'={self.getInterestBase()}, 'Interest'={self.getInterest()}, 'Deposit'={self.getDeposit()}, 'Withdraw'={self.getWithdraw()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenCash'={self.getFrozenCash()}, 'FrozenCommission'={self.getFrozenCommission()}, 'CurrMargin'={self.getCurrMargin()}, 'CashIn'={self.getCashIn()}, 'Commission'={self.getCommission()}, 'CloseProfit'={self.getCloseProfit()}, 'PositionProfit'={self.getPositionProfit()}, 'Balance'={self.getBalance()}, 'Available'={self.getAvailable()}, 'WithdrawQuota'={self.getWithdrawQuota()}, 'Reserve'={self.getReserve()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'Credit'={self.getCredit()}, 'Mortgage'={self.getMortgage()}, 'ExchangeMargin'={self.getExchangeMargin()}, 'DeliveryMargin'={self.getDeliveryMargin()}, 'ExchangeDeliveryMargin'={self.getExchangeDeliveryMargin()}, 'ReserveBalance'={self.getReserveBalance()}, 'CurrencyID'={self.getCurrencyID()}, 'PreFundMortgageIn'={self.getPreFundMortgageIn()}, 'PreFundMortgageOut'={self.getPreFundMortgageOut()}, 'FundMortgageIn'={self.getFundMortgageIn()}, 'FundMortgageOut'={self.getFundMortgageOut()}, 'FundMortgageAvailable'={self.getFundMortgageAvailable()}, 'MortgageableFund'={self.getMortgageableFund()}, 'SpecProductMargin'={self.getSpecProductMargin()}, 'SpecProductFrozenMargin'={self.getSpecProductFrozenMargin()}, 'SpecProductCommission'={self.getSpecProductCommission()}, 'SpecProductFrozenCommission'={self.getSpecProductFrozenCommission()}, 'SpecProductPositionProfit'={self.getSpecProductPositionProfit()}, 'SpecProductCloseProfit'={self.getSpecProductCloseProfit()}, 'SpecProductPositionProfitByAlg'={self.getSpecProductPositionProfitByAlg()}, 'SpecProductExchangeMargin'={self.getSpecProductExchangeMargin()}, 'FrozenSwap'={self.getFrozenSwap()}, 'RemainSwap'={self.getRemainSwap()}"


class  CThostFtdcSyncingInvestorPositionField(Structure):
    """正在同步中的投资者持仓"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", c_int32),
        ("Position", c_int32),
        ("LongFrozen", c_int32),
        ("ShortFrozen", c_int32),
        ("LongFrozenAmount", c_double),
        ("ShortFrozenAmount", c_double),
        ("OpenVolume", c_int32),
        ("CloseVolume", c_int32),
        ("OpenAmount", c_double),
        ("CloseAmount", c_double),
        ("PositionCost", c_double),
        ("PreMargin", c_double),
        ("UseMargin", c_double),
        ("FrozenMargin", c_double),
        ("FrozenCash", c_double),
        ("FrozenCommission", c_double),
        ("CashIn", c_double),
        ("Commission", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("PreSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OpenCost", c_double),
        ("ExchangeMargin", c_double),
        ("CombPosition", c_int32),
        ("CombLongFrozen", c_int32),
        ("CombShortFrozen", c_int32),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("TodayPosition", c_int32),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("StrikeFrozen", c_int32),
        ("StrikeFrozenAmount", c_double),
        ("AbandonFrozen", c_int32),
        ("ExchangeID", c_char*9),
        ("YdStrikeFrozen", c_int32),
        ("InvestUnitID", c_char*17),
        ("PositionCostOffset", c_double),
        ("TasPosition", c_int32),
        ("TasPositionCost", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getPosiDirection(self):
        '''持仓多空方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getPositionDate(self):
        '''持仓日期'''
        return TThostFtdcPositionDateType(ord(self.PositionDate)) if ord(self.PositionDate) in [e.value for e in list(TThostFtdcPositionDateType)] else list(TThostFtdcPositionDateType)[0]

    def getYdPosition(self):
        '''上日持仓'''
        return self.YdPosition

    def getPosition(self):
        '''今日持仓'''
        return self.Position

    def getLongFrozen(self):
        '''多头冻结'''
        return self.LongFrozen

    def getShortFrozen(self):
        '''空头冻结'''
        return self.ShortFrozen

    def getLongFrozenAmount(self):
        '''开仓冻结金额'''
        return self.LongFrozenAmount

    def getShortFrozenAmount(self):
        '''开仓冻结金额'''
        return self.ShortFrozenAmount

    def getOpenVolume(self):
        '''开仓量'''
        return self.OpenVolume

    def getCloseVolume(self):
        '''平仓量'''
        return self.CloseVolume

    def getOpenAmount(self):
        '''开仓金额'''
        return self.OpenAmount

    def getCloseAmount(self):
        '''平仓金额'''
        return self.CloseAmount

    def getPositionCost(self):
        '''持仓成本'''
        return self.PositionCost

    def getPreMargin(self):
        '''上次占用的保证金'''
        return self.PreMargin

    def getUseMargin(self):
        '''占用的保证金'''
        return self.UseMargin

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenCash(self):
        '''冻结的资金'''
        return self.FrozenCash

    def getFrozenCommission(self):
        '''冻结的手续费'''
        return self.FrozenCommission

    def getCashIn(self):
        '''资金差额'''
        return self.CashIn

    def getCommission(self):
        '''手续费'''
        return self.Commission

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getPreSettlementPrice(self):
        '''上次结算价'''
        return self.PreSettlementPrice

    def getSettlementPrice(self):
        '''本次结算价'''
        return self.SettlementPrice

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOpenCost(self):
        '''开仓成本'''
        return self.OpenCost

    def getExchangeMargin(self):
        '''交易所保证金'''
        return self.ExchangeMargin

    def getCombPosition(self):
        '''组合成交形成的持仓'''
        return self.CombPosition

    def getCombLongFrozen(self):
        '''组合多头冻结'''
        return self.CombLongFrozen

    def getCombShortFrozen(self):
        '''组合空头冻结'''
        return self.CombShortFrozen

    def getCloseProfitByDate(self):
        '''逐日盯市平仓盈亏'''
        return self.CloseProfitByDate

    def getCloseProfitByTrade(self):
        '''逐笔对冲平仓盈亏'''
        return self.CloseProfitByTrade

    def getTodayPosition(self):
        '''今日持仓'''
        return self.TodayPosition

    def getMarginRateByMoney(self):
        '''保证金率'''
        return self.MarginRateByMoney

    def getMarginRateByVolume(self):
        '''保证金率(按手数)'''
        return self.MarginRateByVolume

    def getStrikeFrozen(self):
        '''执行冻结'''
        return self.StrikeFrozen

    def getStrikeFrozenAmount(self):
        '''执行冻结金额'''
        return self.StrikeFrozenAmount

    def getAbandonFrozen(self):
        '''放弃执行冻结'''
        return self.AbandonFrozen

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getYdStrikeFrozen(self):
        '''执行冻结的昨仓'''
        return self.YdStrikeFrozen

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getPositionCostOffset(self):
        '''大商所持仓成本差值，只有大商所使用'''
        return self.PositionCostOffset

    def getTasPosition(self):
        '''tas持仓手数'''
        return self.TasPosition

    def getTasPositionCost(self):
        '''tas持仓成本'''
        return self.TasPositionCost

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'PosiDirection'={self.getPosiDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'PositionDate'={self.getPositionDate()}, 'YdPosition'={self.getYdPosition()}, 'Position'={self.getPosition()}, 'LongFrozen'={self.getLongFrozen()}, 'ShortFrozen'={self.getShortFrozen()}, 'LongFrozenAmount'={self.getLongFrozenAmount()}, 'ShortFrozenAmount'={self.getShortFrozenAmount()}, 'OpenVolume'={self.getOpenVolume()}, 'CloseVolume'={self.getCloseVolume()}, 'OpenAmount'={self.getOpenAmount()}, 'CloseAmount'={self.getCloseAmount()}, 'PositionCost'={self.getPositionCost()}, 'PreMargin'={self.getPreMargin()}, 'UseMargin'={self.getUseMargin()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenCash'={self.getFrozenCash()}, 'FrozenCommission'={self.getFrozenCommission()}, 'CashIn'={self.getCashIn()}, 'Commission'={self.getCommission()}, 'CloseProfit'={self.getCloseProfit()}, 'PositionProfit'={self.getPositionProfit()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OpenCost'={self.getOpenCost()}, 'ExchangeMargin'={self.getExchangeMargin()}, 'CombPosition'={self.getCombPosition()}, 'CombLongFrozen'={self.getCombLongFrozen()}, 'CombShortFrozen'={self.getCombShortFrozen()}, 'CloseProfitByDate'={self.getCloseProfitByDate()}, 'CloseProfitByTrade'={self.getCloseProfitByTrade()}, 'TodayPosition'={self.getTodayPosition()}, 'MarginRateByMoney'={self.getMarginRateByMoney()}, 'MarginRateByVolume'={self.getMarginRateByVolume()}, 'StrikeFrozen'={self.getStrikeFrozen()}, 'StrikeFrozenAmount'={self.getStrikeFrozenAmount()}, 'AbandonFrozen'={self.getAbandonFrozen()}, 'ExchangeID'={self.getExchangeID()}, 'YdStrikeFrozen'={self.getYdStrikeFrozen()}, 'InvestUnitID'={self.getInvestUnitID()}, 'PositionCostOffset'={self.getPositionCostOffset()}, 'TasPosition'={self.getTasPosition()}, 'TasPositionCost'={self.getTasPositionCost()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcSyncingInstrumentMarginRateField(Structure):
    """正在同步中的合约保证金率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int32),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getIsRelative(self):
        '''是否相对交易所收取'''
        return self.IsRelative

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'IsRelative'={self.getIsRelative()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcSyncingInstrumentCommissionRateField(Structure):
    """正在同步中的合约手续费率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOpenRatioByMoney(self):
        '''开仓手续费率'''
        return self.OpenRatioByMoney

    def getOpenRatioByVolume(self):
        '''开仓手续费'''
        return self.OpenRatioByVolume

    def getCloseRatioByMoney(self):
        '''平仓手续费率'''
        return self.CloseRatioByMoney

    def getCloseRatioByVolume(self):
        '''平仓手续费'''
        return self.CloseRatioByVolume

    def getCloseTodayRatioByMoney(self):
        '''平今手续费率'''
        return self.CloseTodayRatioByMoney

    def getCloseTodayRatioByVolume(self):
        '''平今手续费'''
        return self.CloseTodayRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OpenRatioByMoney'={self.getOpenRatioByMoney()}, 'OpenRatioByVolume'={self.getOpenRatioByVolume()}, 'CloseRatioByMoney'={self.getCloseRatioByMoney()}, 'CloseRatioByVolume'={self.getCloseRatioByVolume()}, 'CloseTodayRatioByMoney'={self.getCloseTodayRatioByMoney()}, 'CloseTodayRatioByVolume'={self.getCloseTodayRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcSyncingInstrumentTradingRightField(Structure):
    """正在同步中的合约交易权限"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("TradingRight", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getTradingRight(self):
        '''交易权限'''
        return TThostFtdcTradingRightType(ord(self.TradingRight)) if ord(self.TradingRight) in [e.value for e in list(TThostFtdcTradingRightType)] else list(TThostFtdcTradingRightType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'TradingRight'={self.getTradingRight()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryTradeField(Structure):
    """查询成交"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TradeID", c_char*21),
        ("TradeTimeStart", c_char*9),
        ("TradeTimeEnd", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getTradeTimeStart(self):
        '''开始时间'''
        return str(self.TradeTimeStart, 'GBK')

    def getTradeTimeEnd(self):
        '''结束时间'''
        return str(self.TradeTimeEnd, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TradeID'={self.getTradeID()}, 'TradeTimeStart'={self.getTradeTimeStart()}, 'TradeTimeEnd'={self.getTradeTimeEnd()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInvestorPositionField(Structure):
    """查询投资者持仓"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryTradingAccountField(Structure):
    """查询资金账户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("CurrencyID", c_char*4),
        ("BizType", c_char),
        ("AccountID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getBizType(self):
        '''业务类型'''
        return TThostFtdcBizTypeType(ord(self.BizType)) if ord(self.BizType) in [e.value for e in list(TThostFtdcBizTypeType)] else list(TThostFtdcBizTypeType)[0]

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'CurrencyID'={self.getCurrencyID()}, 'BizType'={self.getBizType()}, 'AccountID'={self.getAccountID()}"


class  CThostFtdcQryInvestorField(Structure):
    """查询投资者"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcQryTradingCodeField(Structure):
    """查询交易编码"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ClientID", c_char*11),
        ("ClientIDType", c_char),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getClientIDType(self):
        '''交易编码类型'''
        return TThostFtdcClientIDTypeType(ord(self.ClientIDType)) if ord(self.ClientIDType) in [e.value for e in list(TThostFtdcClientIDTypeType)] else list(TThostFtdcClientIDTypeType)[0]

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}, 'ClientIDType'={self.getClientIDType()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcQryInvestorGroupField(Structure):
    """查询投资者组"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcQryInstrumentMarginRateField(Structure):
    """查询合约保证金率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInstrumentCommissionRateField(Structure):
    """查询手续费率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInstrumentTradingRightField(Structure):
    """查询合约交易权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryBrokerField(Structure):
    """查询经纪公司"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcQryTraderField(Structure):
    """查询交易员"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("TraderID", c_char*21),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcQrySuperUserFunctionField(Structure):
    """查询管理用户功能权限"""
    _fields_ = [
        ("UserID", c_char*16),
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'UserID'={self.getUserID()}"


class  CThostFtdcQryUserSessionField(Structure):
    """查询用户会话"""
    _fields_ = [
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcQryPartBrokerField(Structure):
    """查询经纪公司会员代码"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("BrokerID", c_char*11),
        ("ParticipantID", c_char*11),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}"


class  CThostFtdcQryFrontStatusField(Structure):
    """查询前置状态"""
    _fields_ = [
        ("FrontID", c_int32),
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def __str__(self): # 可以直接print
        return f"'FrontID'={self.getFrontID()}"


class  CThostFtdcQryExchangeOrderField(Structure):
    """查询交易所报单"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ExchangeInstID", c_char*81),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcQryOrderActionField(Structure):
    """查询报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcQryExchangeOrderActionField(Structure):
    """查询交易所报单操作"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcQrySuperUserField(Structure):
    """查询管理用户"""
    _fields_ = [
        ("UserID", c_char*16),
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'UserID'={self.getUserID()}"


class  CThostFtdcQryExchangeField(Structure):
    """查询交易所"""
    _fields_ = [
        ("ExchangeID", c_char*9),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcQryProductField(Structure):
    """查询产品"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ProductClass", c_char),
        ("ExchangeID", c_char*9),
        ("ProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getProductClass(self):
        '''产品类型'''
        return TThostFtdcProductClassType(ord(self.ProductClass)) if ord(self.ProductClass) in [e.value for e in list(TThostFtdcProductClassType)] else list(TThostFtdcProductClassType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ProductClass'={self.getProductClass()}, 'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcQryInstrumentField(Structure):
    """查询合约"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("reserve2", c_char*31),
        ("reserve3", c_char*31),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("ProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'reserve2'={self.getreserve2()}, 'reserve3'={self.getreserve3()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcQryDepthMarketDataField(Structure):
    """查询行情"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryBrokerUserField(Structure):
    """查询经纪公司用户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcQryBrokerUserFunctionField(Structure):
    """查询经纪公司用户权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcQryTraderOfferField(Structure):
    """查询交易员报盘机"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("TraderID", c_char*21),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcQrySyncDepositField(Structure):
    """查询出入金流水"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("DepositSeqNo", c_char*15),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getDepositSeqNo(self):
        '''出入金流水号'''
        return str(self.DepositSeqNo, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'DepositSeqNo'={self.getDepositSeqNo()}"


class  CThostFtdcQrySettlementInfoField(Structure):
    """查询投资者结算结果"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("TradingDay", c_char*9),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'TradingDay'={self.getTradingDay()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcQryExchangeMarginRateField(Structure):
    """查询交易所保证金率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryExchangeMarginRateAdjustField(Structure):
    """查询交易所调整保证金率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryExchangeRateField(Structure):
    """查询汇率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("FromCurrencyID", c_char*4),
        ("ToCurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getFromCurrencyID(self):
        '''源币种'''
        return str(self.FromCurrencyID, 'GBK')

    def getToCurrencyID(self):
        '''目标币种'''
        return str(self.ToCurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'FromCurrencyID'={self.getFromCurrencyID()}, 'ToCurrencyID'={self.getToCurrencyID()}"


class  CThostFtdcQrySyncFundMortgageField(Structure):
    """查询货币质押流水"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("MortgageSeqNo", c_char*15),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getMortgageSeqNo(self):
        '''货币质押流水号'''
        return str(self.MortgageSeqNo, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'MortgageSeqNo'={self.getMortgageSeqNo()}"


class  CThostFtdcQryHisOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcOptionInstrMiniMarginField(Structure):
    """当前期权合约最小保证金"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("MinMargin", c_double),
        ("ValueMethod", c_char),
        ("IsRelative", c_int32),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getMinMargin(self):
        '''单位（手）期权合约最小保证金'''
        return self.MinMargin

    def getValueMethod(self):
        '''取值方式'''
        return TThostFtdcValueMethodType(ord(self.ValueMethod)) if ord(self.ValueMethod) in [e.value for e in list(TThostFtdcValueMethodType)] else list(TThostFtdcValueMethodType)[0]

    def getIsRelative(self):
        '''是否跟随交易所收取'''
        return self.IsRelative

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'MinMargin'={self.getMinMargin()}, 'ValueMethod'={self.getValueMethod()}, 'IsRelative'={self.getIsRelative()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcOptionInstrMarginAdjustField(Structure):
    """当前期权合约保证金调整系数"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("SShortMarginRatioByMoney", c_double),
        ("SShortMarginRatioByVolume", c_double),
        ("HShortMarginRatioByMoney", c_double),
        ("HShortMarginRatioByVolume", c_double),
        ("AShortMarginRatioByMoney", c_double),
        ("AShortMarginRatioByVolume", c_double),
        ("IsRelative", c_int32),
        ("MShortMarginRatioByMoney", c_double),
        ("MShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getSShortMarginRatioByMoney(self):
        '''投机空头保证金调整系数'''
        return self.SShortMarginRatioByMoney

    def getSShortMarginRatioByVolume(self):
        '''投机空头保证金调整系数'''
        return self.SShortMarginRatioByVolume

    def getHShortMarginRatioByMoney(self):
        '''保值空头保证金调整系数'''
        return self.HShortMarginRatioByMoney

    def getHShortMarginRatioByVolume(self):
        '''保值空头保证金调整系数'''
        return self.HShortMarginRatioByVolume

    def getAShortMarginRatioByMoney(self):
        '''套利空头保证金调整系数'''
        return self.AShortMarginRatioByMoney

    def getAShortMarginRatioByVolume(self):
        '''套利空头保证金调整系数'''
        return self.AShortMarginRatioByVolume

    def getIsRelative(self):
        '''是否跟随交易所收取'''
        return self.IsRelative

    def getMShortMarginRatioByMoney(self):
        '''做市商空头保证金调整系数'''
        return self.MShortMarginRatioByMoney

    def getMShortMarginRatioByVolume(self):
        '''做市商空头保证金调整系数'''
        return self.MShortMarginRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'SShortMarginRatioByMoney'={self.getSShortMarginRatioByMoney()}, 'SShortMarginRatioByVolume'={self.getSShortMarginRatioByVolume()}, 'HShortMarginRatioByMoney'={self.getHShortMarginRatioByMoney()}, 'HShortMarginRatioByVolume'={self.getHShortMarginRatioByVolume()}, 'AShortMarginRatioByMoney'={self.getAShortMarginRatioByMoney()}, 'AShortMarginRatioByVolume'={self.getAShortMarginRatioByVolume()}, 'IsRelative'={self.getIsRelative()}, 'MShortMarginRatioByMoney'={self.getMShortMarginRatioByMoney()}, 'MShortMarginRatioByVolume'={self.getMShortMarginRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcOptionInstrCommRateField(Structure):
    """当前期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("StrikeRatioByMoney", c_double),
        ("StrikeRatioByVolume", c_double),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOpenRatioByMoney(self):
        '''开仓手续费率'''
        return self.OpenRatioByMoney

    def getOpenRatioByVolume(self):
        '''开仓手续费'''
        return self.OpenRatioByVolume

    def getCloseRatioByMoney(self):
        '''平仓手续费率'''
        return self.CloseRatioByMoney

    def getCloseRatioByVolume(self):
        '''平仓手续费'''
        return self.CloseRatioByVolume

    def getCloseTodayRatioByMoney(self):
        '''平今手续费率'''
        return self.CloseTodayRatioByMoney

    def getCloseTodayRatioByVolume(self):
        '''平今手续费'''
        return self.CloseTodayRatioByVolume

    def getStrikeRatioByMoney(self):
        '''执行手续费率'''
        return self.StrikeRatioByMoney

    def getStrikeRatioByVolume(self):
        '''执行手续费'''
        return self.StrikeRatioByVolume

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OpenRatioByMoney'={self.getOpenRatioByMoney()}, 'OpenRatioByVolume'={self.getOpenRatioByVolume()}, 'CloseRatioByMoney'={self.getCloseRatioByMoney()}, 'CloseRatioByVolume'={self.getCloseRatioByVolume()}, 'CloseTodayRatioByMoney'={self.getCloseTodayRatioByMoney()}, 'CloseTodayRatioByVolume'={self.getCloseTodayRatioByVolume()}, 'StrikeRatioByMoney'={self.getStrikeRatioByMoney()}, 'StrikeRatioByVolume'={self.getStrikeRatioByVolume()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcOptionInstrTradeCostField(Structure):
    """期权交易成本"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("FixedMargin", c_double),
        ("MiniMargin", c_double),
        ("Royalty", c_double),
        ("ExchFixedMargin", c_double),
        ("ExchMiniMargin", c_double),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getFixedMargin(self):
        '''期权合约保证金不变部分'''
        return self.FixedMargin

    def getMiniMargin(self):
        '''期权合约最小保证金'''
        return self.MiniMargin

    def getRoyalty(self):
        '''期权合约权利金'''
        return self.Royalty

    def getExchFixedMargin(self):
        '''交易所期权合约保证金不变部分'''
        return self.ExchFixedMargin

    def getExchMiniMargin(self):
        '''交易所期权合约最小保证金'''
        return self.ExchMiniMargin

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'FixedMargin'={self.getFixedMargin()}, 'MiniMargin'={self.getMiniMargin()}, 'Royalty'={self.getRoyalty()}, 'ExchFixedMargin'={self.getExchFixedMargin()}, 'ExchMiniMargin'={self.getExchMiniMargin()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryOptionInstrTradeCostField(Structure):
    """期权交易成本查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("InputPrice", c_double),
        ("UnderlyingPrice", c_double),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getInputPrice(self):
        '''期权合约报价'''
        return self.InputPrice

    def getUnderlyingPrice(self):
        '''标的价格,填0则用昨结算价'''
        return self.UnderlyingPrice

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'InputPrice'={self.getInputPrice()}, 'UnderlyingPrice'={self.getUnderlyingPrice()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryOptionInstrCommRateField(Structure):
    """期权手续费率查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcIndexPriceField(Structure):
    """股指现货指数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("ClosePrice", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getClosePrice(self):
        '''指数现货收盘价'''
        return self.ClosePrice

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'ClosePrice'={self.getClosePrice()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInputExecOrderField(Structure):
    """输入的执行宣告"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExecOrderRef", c_char*13),
        ("UserID", c_char*16),
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return TThostFtdcExecOrderPositionFlagType(ord(self.ReservePositionFlag)) if ord(self.ReservePositionFlag) in [e.value for e in list(TThostFtdcExecOrderPositionFlagType)] else list(TThostFtdcExecOrderPositionFlagType)[0]

    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return TThostFtdcExecOrderCloseFlagType(ord(self.CloseFlag)) if ord(self.CloseFlag) in [e.value for e in list(TThostFtdcExecOrderCloseFlagType)] else list(TThostFtdcExecOrderCloseFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'UserID'={self.getUserID()}, 'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionType'={self.getActionType()}, 'PosiDirection'={self.getPosiDirection()}, 'ReservePositionFlag'={self.getReservePositionFlag()}, 'CloseFlag'={self.getCloseFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcInputExecOrderActionField(Structure):
    """输入执行宣告操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExecOrderActionRef", c_int32),
        ("ExecOrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("ExecOrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExecOrderActionRef(self):
        '''执行宣告操作引用'''
        return self.ExecOrderActionRef

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExecOrderSysID(self):
        '''执行宣告操作编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExecOrderActionRef'={self.getExecOrderActionRef()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExecOrderField(Structure):
    """执行宣告"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExecOrderRef", c_char*13),
        ("UserID", c_char*16),
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("ExecOrderSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("ActiveUserID", c_char*16),
        ("BrokerExecOrderSeq", c_int32),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return TThostFtdcExecOrderPositionFlagType(ord(self.ReservePositionFlag)) if ord(self.ReservePositionFlag) in [e.value for e in list(TThostFtdcExecOrderPositionFlagType)] else list(TThostFtdcExecOrderPositionFlagType)[0]

    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return TThostFtdcExecOrderCloseFlagType(ord(self.CloseFlag)) if ord(self.CloseFlag) in [e.value for e in list(TThostFtdcExecOrderCloseFlagType)] else list(TThostFtdcExecOrderCloseFlagType)[0]

    def getExecOrderLocalID(self):
        '''本地执行宣告编号'''
        return str(self.ExecOrderLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''执行宣告提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getExecOrderSysID(self):
        '''执行宣告编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getExecResult(self):
        '''执行结果'''
        return TThostFtdcExecResultType(ord(self.ExecResult)) if ord(self.ExecResult) in [e.value for e in list(TThostFtdcExecResultType)] else list(TThostFtdcExecResultType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerExecOrderSeq(self):
        '''经纪公司报单编号'''
        return self.BrokerExecOrderSeq

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'UserID'={self.getUserID()}, 'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionType'={self.getActionType()}, 'PosiDirection'={self.getPosiDirection()}, 'ReservePositionFlag'={self.getReservePositionFlag()}, 'CloseFlag'={self.getCloseFlag()}, 'ExecOrderLocalID'={self.getExecOrderLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'ExecResult'={self.getExecResult()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerExecOrderSeq'={self.getBrokerExecOrderSeq()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExecOrderActionField(Structure):
    """执行宣告操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExecOrderActionRef", c_int32),
        ("ExecOrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("ExecOrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ExecOrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("ActionType", c_char),
        ("StatusMsg", c_char*81),
        ("reserve1", c_char*31),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExecOrderActionRef(self):
        '''执行宣告操作引用'''
        return self.ExecOrderActionRef

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExecOrderSysID(self):
        '''执行宣告操作编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getExecOrderLocalID(self):
        '''本地执行宣告编号'''
        return str(self.ExecOrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExecOrderActionRef'={self.getExecOrderActionRef()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ExecOrderLocalID'={self.getExecOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'ActionType'={self.getActionType()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve1'={self.getreserve1()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExecOrderField(Structure):
    """执行宣告查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("ExecOrderSysID", c_char*21),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExecOrderSysID(self):
        '''执行宣告编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeExecOrderField(Structure):
    """交易所执行宣告信息"""
    _fields_ = [
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("ExecOrderSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("BranchID", c_char*9),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return TThostFtdcExecOrderPositionFlagType(ord(self.ReservePositionFlag)) if ord(self.ReservePositionFlag) in [e.value for e in list(TThostFtdcExecOrderPositionFlagType)] else list(TThostFtdcExecOrderPositionFlagType)[0]

    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return TThostFtdcExecOrderCloseFlagType(ord(self.CloseFlag)) if ord(self.CloseFlag) in [e.value for e in list(TThostFtdcExecOrderCloseFlagType)] else list(TThostFtdcExecOrderCloseFlagType)[0]

    def getExecOrderLocalID(self):
        '''本地执行宣告编号'''
        return str(self.ExecOrderLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''执行宣告提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getExecOrderSysID(self):
        '''执行宣告编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getExecResult(self):
        '''执行结果'''
        return TThostFtdcExecResultType(ord(self.ExecResult)) if ord(self.ExecResult) in [e.value for e in list(TThostFtdcExecResultType)] else list(TThostFtdcExecResultType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionType'={self.getActionType()}, 'PosiDirection'={self.getPosiDirection()}, 'ReservePositionFlag'={self.getReservePositionFlag()}, 'CloseFlag'={self.getCloseFlag()}, 'ExecOrderLocalID'={self.getExecOrderLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'ExecResult'={self.getExecResult()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'BranchID'={self.getBranchID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeExecOrderField(Structure):
    """交易所执行宣告查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ExchangeInstID", c_char*81),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcQryExecOrderActionField(Structure):
    """执行宣告操作查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ExecOrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ExecOrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("ActionType", c_char),
        ("BranchID", c_char*9),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("reserve2", c_char*31),
        ("Volume", c_int32),
        ("IPAddress", c_char*33),
        ("ExchangeInstID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExecOrderSysID(self):
        '''执行宣告操作编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getExecOrderLocalID(self):
        '''本地执行宣告编号'''
        return str(self.ExecOrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ExecOrderLocalID'={self.getExecOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'ActionType'={self.getActionType()}, 'BranchID'={self.getBranchID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'reserve2'={self.getreserve2()}, 'Volume'={self.getVolume()}, 'IPAddress'={self.getIPAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcQryExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcErrExecOrderField(Structure):
    """错误执行宣告"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExecOrderRef", c_char*13),
        ("UserID", c_char*16),
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionType(self):
        '''执行类型'''
        return TThostFtdcActionTypeType(ord(self.ActionType)) if ord(self.ActionType) in [e.value for e in list(TThostFtdcActionTypeType)] else list(TThostFtdcActionTypeType)[0]

    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return TThostFtdcPosiDirectionType(ord(self.PosiDirection)) if ord(self.PosiDirection) in [e.value for e in list(TThostFtdcPosiDirectionType)] else list(TThostFtdcPosiDirectionType)[0]

    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return TThostFtdcExecOrderPositionFlagType(ord(self.ReservePositionFlag)) if ord(self.ReservePositionFlag) in [e.value for e in list(TThostFtdcExecOrderPositionFlagType)] else list(TThostFtdcExecOrderPositionFlagType)[0]

    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return TThostFtdcExecOrderCloseFlagType(ord(self.CloseFlag)) if ord(self.CloseFlag) in [e.value for e in list(TThostFtdcExecOrderCloseFlagType)] else list(TThostFtdcExecOrderCloseFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'UserID'={self.getUserID()}, 'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionType'={self.getActionType()}, 'PosiDirection'={self.getPosiDirection()}, 'ReservePositionFlag'={self.getReservePositionFlag()}, 'CloseFlag'={self.getCloseFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryErrExecOrderField(Structure):
    """查询错误执行宣告"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcErrExecOrderActionField(Structure):
    """错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExecOrderActionRef", c_int32),
        ("ExecOrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("ExecOrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExecOrderActionRef(self):
        '''执行宣告操作引用'''
        return self.ExecOrderActionRef

    def getExecOrderRef(self):
        '''执行宣告引用'''
        return str(self.ExecOrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExecOrderSysID(self):
        '''执行宣告操作编号'''
        return str(self.ExecOrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExecOrderActionRef'={self.getExecOrderActionRef()}, 'ExecOrderRef'={self.getExecOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'ExecOrderSysID'={self.getExecOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryErrExecOrderActionField(Structure):
    """查询错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcOptionInstrTradingRightField(Structure):
    """投资者期权合约交易权限"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Direction", c_char),
        ("TradingRight", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getTradingRight(self):
        '''交易权限'''
        return TThostFtdcTradingRightType(ord(self.TradingRight)) if ord(self.TradingRight) in [e.value for e in list(TThostFtdcTradingRightType)] else list(TThostFtdcTradingRightType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Direction'={self.getDirection()}, 'TradingRight'={self.getTradingRight()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryOptionInstrTradingRightField(Structure):
    """查询期权合约交易权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("Direction", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'Direction'={self.getDirection()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInputForQuoteField(Structure):
    """输入的询价"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ForQuoteRef", c_char*13),
        ("UserID", c_char*16),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getForQuoteRef(self):
        '''询价引用'''
        return str(self.ForQuoteRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ForQuoteRef'={self.getForQuoteRef()}, 'UserID'={self.getUserID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcForQuoteField(Structure):
    """询价"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ForQuoteRef", c_char*13),
        ("UserID", c_char*16),
        ("ForQuoteLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("ForQuoteStatus", c_char),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("StatusMsg", c_char*81),
        ("ActiveUserID", c_char*16),
        ("BrokerForQutoSeq", c_int32),
        ("InvestUnitID", c_char*17),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getForQuoteRef(self):
        '''询价引用'''
        return str(self.ForQuoteRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getForQuoteLocalID(self):
        '''本地询价编号'''
        return str(self.ForQuoteLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getForQuoteStatus(self):
        '''询价状态'''
        return TThostFtdcForQuoteStatusType(ord(self.ForQuoteStatus)) if ord(self.ForQuoteStatus) in [e.value for e in list(TThostFtdcForQuoteStatusType)] else list(TThostFtdcForQuoteStatusType)[0]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerForQutoSeq(self):
        '''经纪公司询价编号'''
        return self.BrokerForQutoSeq

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ForQuoteRef'={self.getForQuoteRef()}, 'UserID'={self.getUserID()}, 'ForQuoteLocalID'={self.getForQuoteLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'ForQuoteStatus'={self.getForQuoteStatus()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'StatusMsg'={self.getStatusMsg()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerForQutoSeq'={self.getBrokerForQutoSeq()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryForQuoteField(Structure):
    """询价查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeForQuoteField(Structure):
    """交易所询价信息"""
    _fields_ = [
        ("ForQuoteLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("ForQuoteStatus", c_char),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getForQuoteLocalID(self):
        '''本地询价编号'''
        return str(self.ForQuoteLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getForQuoteStatus(self):
        '''询价状态'''
        return TThostFtdcForQuoteStatusType(ord(self.ForQuoteStatus)) if ord(self.ForQuoteStatus) in [e.value for e in list(TThostFtdcForQuoteStatusType)] else list(TThostFtdcForQuoteStatusType)[0]

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ForQuoteLocalID'={self.getForQuoteLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'ForQuoteStatus'={self.getForQuoteStatus()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeForQuoteField(Structure):
    """交易所询价查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ExchangeInstID", c_char*81),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcInputQuoteField(Structure):
    """输入的报价"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("QuoteRef", c_char*13),
        ("UserID", c_char*16),
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int32),
        ("BidVolume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("AskOrderRef", c_char*13),
        ("BidOrderRef", c_char*13),
        ("ForQuoteSysID", c_char*21),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getQuoteRef(self):
        '''报价引用'''
        return str(self.QuoteRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getAskPrice(self):
        '''卖价格'''
        return self.AskPrice

    def getBidPrice(self):
        '''买价格'''
        return self.BidPrice

    def getAskVolume(self):
        '''卖数量'''
        return self.AskVolume

    def getBidVolume(self):
        '''买数量'''
        return self.BidVolume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getAskOffsetFlag(self):
        '''卖开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.AskOffsetFlag)) if ord(self.AskOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getBidOffsetFlag(self):
        '''买开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.BidOffsetFlag)) if ord(self.BidOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.AskHedgeFlag)) if ord(self.AskHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.BidHedgeFlag)) if ord(self.BidHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getAskOrderRef(self):
        '''衍生卖报单引用'''
        return str(self.AskOrderRef, 'GBK')

    def getBidOrderRef(self):
        '''衍生买报单引用'''
        return str(self.BidOrderRef, 'GBK')

    def getForQuoteSysID(self):
        '''应价编号'''
        return str(self.ForQuoteSysID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'QuoteRef'={self.getQuoteRef()}, 'UserID'={self.getUserID()}, 'AskPrice'={self.getAskPrice()}, 'BidPrice'={self.getBidPrice()}, 'AskVolume'={self.getAskVolume()}, 'BidVolume'={self.getBidVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'AskOffsetFlag'={self.getAskOffsetFlag()}, 'BidOffsetFlag'={self.getBidOffsetFlag()}, 'AskHedgeFlag'={self.getAskHedgeFlag()}, 'BidHedgeFlag'={self.getBidHedgeFlag()}, 'AskOrderRef'={self.getAskOrderRef()}, 'BidOrderRef'={self.getBidOrderRef()}, 'ForQuoteSysID'={self.getForQuoteSysID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcInputQuoteActionField(Structure):
    """输入报价操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("QuoteActionRef", c_int32),
        ("QuoteRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("QuoteSysID", c_char*21),
        ("ActionFlag", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getQuoteActionRef(self):
        '''报价操作引用'''
        return self.QuoteActionRef

    def getQuoteRef(self):
        '''报价引用'''
        return str(self.QuoteRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getQuoteSysID(self):
        '''报价操作编号'''
        return str(self.QuoteSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'QuoteActionRef'={self.getQuoteActionRef()}, 'QuoteRef'={self.getQuoteRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'ActionFlag'={self.getActionFlag()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQuoteField(Structure):
    """报价"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("QuoteRef", c_char*13),
        ("UserID", c_char*16),
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int32),
        ("BidVolume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("NotifySequence", c_int32),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("QuoteSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("QuoteStatus", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("AskOrderSysID", c_char*21),
        ("BidOrderSysID", c_char*21),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("ActiveUserID", c_char*16),
        ("BrokerQuoteSeq", c_int32),
        ("AskOrderRef", c_char*13),
        ("BidOrderRef", c_char*13),
        ("ForQuoteSysID", c_char*21),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getQuoteRef(self):
        '''报价引用'''
        return str(self.QuoteRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getAskPrice(self):
        '''卖价格'''
        return self.AskPrice

    def getBidPrice(self):
        '''买价格'''
        return self.BidPrice

    def getAskVolume(self):
        '''卖数量'''
        return self.AskVolume

    def getBidVolume(self):
        '''买数量'''
        return self.BidVolume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getAskOffsetFlag(self):
        '''卖开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.AskOffsetFlag)) if ord(self.AskOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getBidOffsetFlag(self):
        '''买开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.BidOffsetFlag)) if ord(self.BidOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.AskHedgeFlag)) if ord(self.AskHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.BidHedgeFlag)) if ord(self.BidHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getQuoteLocalID(self):
        '''本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getNotifySequence(self):
        '''报价提示序号'''
        return self.NotifySequence

    def getOrderSubmitStatus(self):
        '''报价提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getQuoteSysID(self):
        '''报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getQuoteStatus(self):
        '''报价状态'''
        return TThostFtdcOrderStatusType(ord(self.QuoteStatus)) if ord(self.QuoteStatus) in [e.value for e in list(TThostFtdcOrderStatusType)] else list(TThostFtdcOrderStatusType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getAskOrderSysID(self):
        '''卖方报单编号'''
        return str(self.AskOrderSysID, 'GBK')

    def getBidOrderSysID(self):
        '''买方报单编号'''
        return str(self.BidOrderSysID, 'GBK')

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerQuoteSeq(self):
        '''经纪公司报价编号'''
        return self.BrokerQuoteSeq

    def getAskOrderRef(self):
        '''衍生卖报单引用'''
        return str(self.AskOrderRef, 'GBK')

    def getBidOrderRef(self):
        '''衍生买报单引用'''
        return str(self.BidOrderRef, 'GBK')

    def getForQuoteSysID(self):
        '''应价编号'''
        return str(self.ForQuoteSysID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'QuoteRef'={self.getQuoteRef()}, 'UserID'={self.getUserID()}, 'AskPrice'={self.getAskPrice()}, 'BidPrice'={self.getBidPrice()}, 'AskVolume'={self.getAskVolume()}, 'BidVolume'={self.getBidVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'AskOffsetFlag'={self.getAskOffsetFlag()}, 'BidOffsetFlag'={self.getBidOffsetFlag()}, 'AskHedgeFlag'={self.getAskHedgeFlag()}, 'BidHedgeFlag'={self.getBidHedgeFlag()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'NotifySequence'={self.getNotifySequence()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'QuoteStatus'={self.getQuoteStatus()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'AskOrderSysID'={self.getAskOrderSysID()}, 'BidOrderSysID'={self.getBidOrderSysID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerQuoteSeq'={self.getBrokerQuoteSeq()}, 'AskOrderRef'={self.getAskOrderRef()}, 'BidOrderRef'={self.getBidOrderRef()}, 'ForQuoteSysID'={self.getForQuoteSysID()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQuoteActionField(Structure):
    """报价操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("QuoteActionRef", c_int32),
        ("QuoteRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("QuoteSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("QuoteLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("StatusMsg", c_char*81),
        ("reserve1", c_char*31),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getQuoteActionRef(self):
        '''报价操作引用'''
        return self.QuoteActionRef

    def getQuoteRef(self):
        '''报价引用'''
        return str(self.QuoteRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getQuoteSysID(self):
        '''报价操作编号'''
        return str(self.QuoteSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getQuoteLocalID(self):
        '''本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'QuoteActionRef'={self.getQuoteActionRef()}, 'QuoteRef'={self.getQuoteRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve1'={self.getreserve1()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryQuoteField(Structure):
    """报价查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("QuoteSysID", c_char*21),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getQuoteSysID(self):
        '''报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeQuoteField(Structure):
    """交易所报价信息"""
    _fields_ = [
        ("AskPrice", c_double),
        ("BidPrice", c_double),
        ("AskVolume", c_int32),
        ("BidVolume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("NotifySequence", c_int32),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("QuoteSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("QuoteStatus", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("AskOrderSysID", c_char*21),
        ("BidOrderSysID", c_char*21),
        ("ForQuoteSysID", c_char*21),
        ("BranchID", c_char*9),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getAskPrice(self):
        '''卖价格'''
        return self.AskPrice

    def getBidPrice(self):
        '''买价格'''
        return self.BidPrice

    def getAskVolume(self):
        '''卖数量'''
        return self.AskVolume

    def getBidVolume(self):
        '''买数量'''
        return self.BidVolume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getAskOffsetFlag(self):
        '''卖开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.AskOffsetFlag)) if ord(self.AskOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getBidOffsetFlag(self):
        '''买开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.BidOffsetFlag)) if ord(self.BidOffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.AskHedgeFlag)) if ord(self.AskHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.BidHedgeFlag)) if ord(self.BidHedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getQuoteLocalID(self):
        '''本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getNotifySequence(self):
        '''报价提示序号'''
        return self.NotifySequence

    def getOrderSubmitStatus(self):
        '''报价提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getQuoteSysID(self):
        '''报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getQuoteStatus(self):
        '''报价状态'''
        return TThostFtdcOrderStatusType(ord(self.QuoteStatus)) if ord(self.QuoteStatus) in [e.value for e in list(TThostFtdcOrderStatusType)] else list(TThostFtdcOrderStatusType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getAskOrderSysID(self):
        '''卖方报单编号'''
        return str(self.AskOrderSysID, 'GBK')

    def getBidOrderSysID(self):
        '''买方报单编号'''
        return str(self.BidOrderSysID, 'GBK')

    def getForQuoteSysID(self):
        '''应价编号'''
        return str(self.ForQuoteSysID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'AskPrice'={self.getAskPrice()}, 'BidPrice'={self.getBidPrice()}, 'AskVolume'={self.getAskVolume()}, 'BidVolume'={self.getBidVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'AskOffsetFlag'={self.getAskOffsetFlag()}, 'BidOffsetFlag'={self.getBidOffsetFlag()}, 'AskHedgeFlag'={self.getAskHedgeFlag()}, 'BidHedgeFlag'={self.getBidHedgeFlag()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'NotifySequence'={self.getNotifySequence()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'QuoteStatus'={self.getQuoteStatus()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'AskOrderSysID'={self.getAskOrderSysID()}, 'BidOrderSysID'={self.getBidOrderSysID()}, 'ForQuoteSysID'={self.getForQuoteSysID()}, 'BranchID'={self.getBranchID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeQuoteField(Structure):
    """交易所报价查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ExchangeInstID", c_char*81),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcQryQuoteActionField(Structure):
    """报价操作查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcExchangeQuoteActionField(Structure):
    """交易所报价操作"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("QuoteSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("QuoteLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getQuoteSysID(self):
        '''报价操作编号'''
        return str(self.QuoteSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getQuoteLocalID(self):
        '''本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeQuoteActionField(Structure):
    """交易所报价操作查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcOptionInstrDeltaField(Structure):
    """期权合约delta值"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Delta", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getDelta(self):
        '''Delta值'''
        return self.Delta

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Delta'={self.getDelta()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcForQuoteRspField(Structure):
    """发给做市商的询价请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("reserve1", c_char*31),
        ("ForQuoteSysID", c_char*21),
        ("ForQuoteTime", c_char*9),
        ("ActionDay", c_char*9),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getForQuoteSysID(self):
        '''询价编号'''
        return str(self.ForQuoteSysID, 'GBK')

    def getForQuoteTime(self):
        '''询价时间'''
        return str(self.ForQuoteTime, 'GBK')

    def getActionDay(self):
        '''业务日期'''
        return str(self.ActionDay, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'reserve1'={self.getreserve1()}, 'ForQuoteSysID'={self.getForQuoteSysID()}, 'ForQuoteTime'={self.getForQuoteTime()}, 'ActionDay'={self.getActionDay()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcStrikeOffsetField(Structure):
    """当前期权合约执行偏移值的详细内容"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Offset", c_double),
        ("OffsetType", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOffset(self):
        '''执行偏移值'''
        return self.Offset

    def getOffsetType(self):
        '''执行偏移类型'''
        return TThostFtdcStrikeOffsetTypeType(ord(self.OffsetType)) if ord(self.OffsetType) in [e.value for e in list(TThostFtdcStrikeOffsetTypeType)] else list(TThostFtdcStrikeOffsetTypeType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Offset'={self.getOffset()}, 'OffsetType'={self.getOffsetType()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryStrikeOffsetField(Structure):
    """期权执行偏移值查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInputBatchOrderActionField(Structure):
    """输入批量报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("UserID", c_char*16),
        ("InvestUnitID", c_char*17),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'UserID'={self.getUserID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcBatchOrderActionField(Structure):
    """批量报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("StatusMsg", c_char*81),
        ("InvestUnitID", c_char*17),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'StatusMsg'={self.getStatusMsg()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcExchangeBatchOrderActionField(Structure):
    """交易所批量报单操作"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryBatchOrderActionField(Structure):
    """查询批量报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcCombInstrumentGuardField(Structure):
    """组合合约安全系数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("GuarantRatio", c_double),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getGuarantRatio(self):
        ''''''
        return self.GuarantRatio

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'GuarantRatio'={self.getGuarantRatio()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryCombInstrumentGuardField(Structure):
    """组合合约安全系数查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInputCombActionField(Structure):
    """输入的申请组合"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("CombActionRef", c_char*13),
        ("UserID", c_char*16),
        ("Direction", c_char),
        ("Volume", c_int32),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char*9),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InvestUnitID", c_char*17),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getCombActionRef(self):
        '''组合引用'''
        return str(self.CombActionRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getCombDirection(self):
        '''组合指令方向'''
        return TThostFtdcCombDirectionType(ord(self.CombDirection)) if ord(self.CombDirection) in [e.value for e in list(TThostFtdcCombDirectionType)] else list(TThostFtdcCombDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'CombActionRef'={self.getCombActionRef()}, 'UserID'={self.getUserID()}, 'Direction'={self.getDirection()}, 'Volume'={self.getVolume()}, 'CombDirection'={self.getCombDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ExchangeID'={self.getExchangeID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InvestUnitID'={self.getInvestUnitID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcCombActionField(Structure):
    """申请组合"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("CombActionRef", c_char*13),
        ("UserID", c_char*16),
        ("Direction", c_char),
        ("Volume", c_int32),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ActionStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("SequenceNo", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("ComTradeID", c_char*21),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getCombActionRef(self):
        '''组合引用'''
        return str(self.CombActionRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getCombDirection(self):
        '''组合指令方向'''
        return TThostFtdcCombDirectionType(ord(self.CombDirection)) if ord(self.CombDirection) in [e.value for e in list(TThostFtdcCombDirectionType)] else list(TThostFtdcCombDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionLocalID(self):
        '''本地申请组合编号'''
        return str(self.ActionLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getActionStatus(self):
        '''组合状态'''
        return TThostFtdcOrderActionStatusType(ord(self.ActionStatus)) if ord(self.ActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getComTradeID(self):
        '''组合编号'''
        return str(self.ComTradeID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'CombActionRef'={self.getCombActionRef()}, 'UserID'={self.getUserID()}, 'Direction'={self.getDirection()}, 'Volume'={self.getVolume()}, 'CombDirection'={self.getCombDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionLocalID'={self.getActionLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ActionStatus'={self.getActionStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'SequenceNo'={self.getSequenceNo()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'ComTradeID'={self.getComTradeID()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryCombActionField(Structure):
    """申请组合查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeCombActionField(Structure):
    """交易所申请组合信息"""
    _fields_ = [
        ("Direction", c_char),
        ("Volume", c_int32),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("ActionStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("SequenceNo", c_int32),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ComTradeID", c_char*21),
        ("BranchID", c_char*9),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getCombDirection(self):
        '''组合指令方向'''
        return TThostFtdcCombDirectionType(ord(self.CombDirection)) if ord(self.CombDirection) in [e.value for e in list(TThostFtdcCombDirectionType)] else list(TThostFtdcCombDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getActionLocalID(self):
        '''本地申请组合编号'''
        return str(self.ActionLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getActionStatus(self):
        '''组合状态'''
        return TThostFtdcOrderActionStatusType(ord(self.ActionStatus)) if ord(self.ActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getComTradeID(self):
        '''组合编号'''
        return str(self.ComTradeID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'Direction'={self.getDirection()}, 'Volume'={self.getVolume()}, 'CombDirection'={self.getCombDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ActionLocalID'={self.getActionLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'ActionStatus'={self.getActionStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'SequenceNo'={self.getSequenceNo()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ComTradeID'={self.getComTradeID()}, 'BranchID'={self.getBranchID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeCombActionField(Structure):
    """交易所申请组合查询"""
    _fields_ = [
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ExchangeInstID", c_char*81),
    ]

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcProductExchRateField(Structure):
    """产品报价汇率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("QuoteCurrencyID", c_char*4),
        ("ExchangeRate", c_double),
        ("ExchangeID", c_char*9),
        ("ProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getQuoteCurrencyID(self):
        '''报价币种类型'''
        return str(self.QuoteCurrencyID, 'GBK')

    def getExchangeRate(self):
        '''汇率'''
        return self.ExchangeRate

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'QuoteCurrencyID'={self.getQuoteCurrencyID()}, 'ExchangeRate'={self.getExchangeRate()}, 'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcQryProductExchRateField(Structure):
    """产品报价汇率查询"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("ProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcQryForQuoteParamField(Structure):
    """查询询价价差参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcForQuoteParamField(Structure):
    """询价价差参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("LastPrice", c_double),
        ("PriceInterval", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getPriceInterval(self):
        '''价差'''
        return self.PriceInterval

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'LastPrice'={self.getLastPrice()}, 'PriceInterval'={self.getPriceInterval()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcMMOptionInstrCommRateField(Structure):
    """当前做市商期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("StrikeRatioByMoney", c_double),
        ("StrikeRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOpenRatioByMoney(self):
        '''开仓手续费率'''
        return self.OpenRatioByMoney

    def getOpenRatioByVolume(self):
        '''开仓手续费'''
        return self.OpenRatioByVolume

    def getCloseRatioByMoney(self):
        '''平仓手续费率'''
        return self.CloseRatioByMoney

    def getCloseRatioByVolume(self):
        '''平仓手续费'''
        return self.CloseRatioByVolume

    def getCloseTodayRatioByMoney(self):
        '''平今手续费率'''
        return self.CloseTodayRatioByMoney

    def getCloseTodayRatioByVolume(self):
        '''平今手续费'''
        return self.CloseTodayRatioByVolume

    def getStrikeRatioByMoney(self):
        '''执行手续费率'''
        return self.StrikeRatioByMoney

    def getStrikeRatioByVolume(self):
        '''执行手续费'''
        return self.StrikeRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OpenRatioByMoney'={self.getOpenRatioByMoney()}, 'OpenRatioByVolume'={self.getOpenRatioByVolume()}, 'CloseRatioByMoney'={self.getCloseRatioByMoney()}, 'CloseRatioByVolume'={self.getCloseRatioByVolume()}, 'CloseTodayRatioByMoney'={self.getCloseTodayRatioByMoney()}, 'CloseTodayRatioByVolume'={self.getCloseTodayRatioByVolume()}, 'StrikeRatioByMoney'={self.getStrikeRatioByMoney()}, 'StrikeRatioByVolume'={self.getStrikeRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryMMOptionInstrCommRateField(Structure):
    """做市商期权手续费率查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcMMInstrumentCommissionRateField(Structure):
    """做市商合约手续费率"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OpenRatioByMoney", c_double),
        ("OpenRatioByVolume", c_double),
        ("CloseRatioByMoney", c_double),
        ("CloseRatioByVolume", c_double),
        ("CloseTodayRatioByMoney", c_double),
        ("CloseTodayRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOpenRatioByMoney(self):
        '''开仓手续费率'''
        return self.OpenRatioByMoney

    def getOpenRatioByVolume(self):
        '''开仓手续费'''
        return self.OpenRatioByVolume

    def getCloseRatioByMoney(self):
        '''平仓手续费率'''
        return self.CloseRatioByMoney

    def getCloseRatioByVolume(self):
        '''平仓手续费'''
        return self.CloseRatioByVolume

    def getCloseTodayRatioByMoney(self):
        '''平今手续费率'''
        return self.CloseTodayRatioByMoney

    def getCloseTodayRatioByVolume(self):
        '''平今手续费'''
        return self.CloseTodayRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OpenRatioByMoney'={self.getOpenRatioByMoney()}, 'OpenRatioByVolume'={self.getOpenRatioByVolume()}, 'CloseRatioByMoney'={self.getCloseRatioByMoney()}, 'CloseRatioByVolume'={self.getCloseRatioByVolume()}, 'CloseTodayRatioByMoney'={self.getCloseTodayRatioByMoney()}, 'CloseTodayRatioByVolume'={self.getCloseTodayRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryMMInstrumentCommissionRateField(Structure):
    """查询做市商合约手续费率"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInstrumentOrderCommRateField(Structure):
    """当前报单手续费的详细内容"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("OrderCommByVolume", c_double),
        ("OrderActionCommByVolume", c_double),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getOrderCommByVolume(self):
        '''报单手续费'''
        return self.OrderCommByVolume

    def getOrderActionCommByVolume(self):
        '''撤单手续费'''
        return self.OrderActionCommByVolume

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'OrderCommByVolume'={self.getOrderCommByVolume()}, 'OrderActionCommByVolume'={self.getOrderActionCommByVolume()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInstrumentOrderCommRateField(Structure):
    """报单手续费率查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcTradeParamField(Structure):
    """交易参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("TradeParamID", c_char),
        ("TradeParamValue", c_char*256),
        ("Memo", c_char*161),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getTradeParamID(self):
        '''参数代码'''
        return TThostFtdcTradeParamIDType(ord(self.TradeParamID)) if ord(self.TradeParamID) in [e.value for e in list(TThostFtdcTradeParamIDType)] else list(TThostFtdcTradeParamIDType)[0]

    def getTradeParamValue(self):
        '''参数代码值'''
        return str(self.TradeParamValue, 'GBK')

    def getMemo(self):
        '''备注'''
        return str(self.Memo, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'TradeParamID'={self.getTradeParamID()}, 'TradeParamValue'={self.getTradeParamValue()}, 'Memo'={self.getMemo()}"


class  CThostFtdcInstrumentMarginRateULField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", c_double),
        ("LongMarginRatioByVolume", c_double),
        ("ShortMarginRatioByMoney", c_double),
        ("ShortMarginRatioByVolume", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getLongMarginRatioByMoney(self):
        '''多头保证金率'''
        return self.LongMarginRatioByMoney

    def getLongMarginRatioByVolume(self):
        '''多头保证金费'''
        return self.LongMarginRatioByVolume

    def getShortMarginRatioByMoney(self):
        '''空头保证金率'''
        return self.ShortMarginRatioByMoney

    def getShortMarginRatioByVolume(self):
        '''空头保证金费'''
        return self.ShortMarginRatioByVolume

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LongMarginRatioByMoney'={self.getLongMarginRatioByMoney()}, 'LongMarginRatioByVolume'={self.getLongMarginRatioByVolume()}, 'ShortMarginRatioByMoney'={self.getShortMarginRatioByMoney()}, 'ShortMarginRatioByVolume'={self.getShortMarginRatioByVolume()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcFutureLimitPosiParamField(Structure):
    """期货持仓限制参数"""
    _fields_ = [
        ("InvestorRange", c_char),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("SpecOpenVolume", c_int32),
        ("ArbiOpenVolume", c_int32),
        ("OpenVolume", c_int32),
        ("ProductID", c_char*81),
    ]

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getSpecOpenVolume(self):
        '''当日投机开仓数量限制'''
        return self.SpecOpenVolume

    def getArbiOpenVolume(self):
        '''当日套利开仓数量限制'''
        return self.ArbiOpenVolume

    def getOpenVolume(self):
        '''当日投机+套利开仓数量限制'''
        return self.OpenVolume

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'InvestorRange'={self.getInvestorRange()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'SpecOpenVolume'={self.getSpecOpenVolume()}, 'ArbiOpenVolume'={self.getArbiOpenVolume()}, 'OpenVolume'={self.getOpenVolume()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcLoginForbiddenIPField(Structure):
    """禁止登录IP"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcIPListField(Structure):
    """IP列表"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IsWhite", c_int32),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIsWhite(self):
        '''是否白名单'''
        return self.IsWhite

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IsWhite'={self.getIsWhite()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcInputOptionSelfCloseField(Structure):
    """输入的期权自对冲"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OptionSelfCloseRef", c_char*13),
        ("UserID", c_char*16),
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOptionSelfCloseRef(self):
        '''期权自对冲引用'''
        return str(self.OptionSelfCloseRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return TThostFtdcOptSelfCloseFlagType(ord(self.OptSelfCloseFlag)) if ord(self.OptSelfCloseFlag) in [e.value for e in list(TThostFtdcOptSelfCloseFlagType)] else list(TThostFtdcOptSelfCloseFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OptionSelfCloseRef'={self.getOptionSelfCloseRef()}, 'UserID'={self.getUserID()}, 'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'HedgeFlag'={self.getHedgeFlag()}, 'OptSelfCloseFlag'={self.getOptSelfCloseFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcInputOptionSelfCloseActionField(Structure):
    """输入期权自对冲操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OptionSelfCloseActionRef", c_int32),
        ("OptionSelfCloseRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OptionSelfCloseSysID", c_char*21),
        ("ActionFlag", c_char),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOptionSelfCloseActionRef(self):
        '''期权自对冲操作引用'''
        return self.OptionSelfCloseActionRef

    def getOptionSelfCloseRef(self):
        '''期权自对冲引用'''
        return str(self.OptionSelfCloseRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOptionSelfCloseSysID(self):
        '''期权自对冲操作编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OptionSelfCloseActionRef'={self.getOptionSelfCloseActionRef()}, 'OptionSelfCloseRef'={self.getOptionSelfCloseRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'ActionFlag'={self.getActionFlag()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcOptionSelfCloseField(Structure):
    """期权自对冲"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OptionSelfCloseRef", c_char*13),
        ("UserID", c_char*16),
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OptionSelfCloseSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("ActiveUserID", c_char*16),
        ("BrokerOptionSelfCloseSeq", c_int32),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOptionSelfCloseRef(self):
        '''期权自对冲引用'''
        return str(self.OptionSelfCloseRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return TThostFtdcOptSelfCloseFlagType(ord(self.OptSelfCloseFlag)) if ord(self.OptSelfCloseFlag) in [e.value for e in list(TThostFtdcOptSelfCloseFlagType)] else list(TThostFtdcOptSelfCloseFlagType)[0]

    def getOptionSelfCloseLocalID(self):
        '''本地期权自对冲编号'''
        return str(self.OptionSelfCloseLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''期权自对冲提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOptionSelfCloseSysID(self):
        '''期权自对冲编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getExecResult(self):
        '''自对冲结果'''
        return TThostFtdcExecResultType(ord(self.ExecResult)) if ord(self.ExecResult) in [e.value for e in list(TThostFtdcExecResultType)] else list(TThostFtdcExecResultType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerOptionSelfCloseSeq(self):
        '''经纪公司报单编号'''
        return self.BrokerOptionSelfCloseSeq

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OptionSelfCloseRef'={self.getOptionSelfCloseRef()}, 'UserID'={self.getUserID()}, 'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'HedgeFlag'={self.getHedgeFlag()}, 'OptSelfCloseFlag'={self.getOptSelfCloseFlag()}, 'OptionSelfCloseLocalID'={self.getOptionSelfCloseLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'ExecResult'={self.getExecResult()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerOptionSelfCloseSeq'={self.getBrokerOptionSelfCloseSeq()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcOptionSelfCloseActionField(Structure):
    """期权自对冲操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OptionSelfCloseActionRef", c_int32),
        ("OptionSelfCloseRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OptionSelfCloseSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OptionSelfCloseLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("StatusMsg", c_char*81),
        ("reserve1", c_char*31),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOptionSelfCloseActionRef(self):
        '''期权自对冲操作引用'''
        return self.OptionSelfCloseActionRef

    def getOptionSelfCloseRef(self):
        '''期权自对冲引用'''
        return str(self.OptionSelfCloseRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOptionSelfCloseSysID(self):
        '''期权自对冲操作编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOptionSelfCloseLocalID(self):
        '''本地期权自对冲编号'''
        return str(self.OptionSelfCloseLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OptionSelfCloseActionRef'={self.getOptionSelfCloseActionRef()}, 'OptionSelfCloseRef'={self.getOptionSelfCloseRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OptionSelfCloseLocalID'={self.getOptionSelfCloseLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve1'={self.getreserve1()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryOptionSelfCloseField(Structure):
    """期权自对冲查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("OptionSelfCloseSysID", c_char*21),
        ("InsertTimeStart", c_char*9),
        ("InsertTimeEnd", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOptionSelfCloseSysID(self):
        '''期权自对冲编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getInsertTimeStart(self):
        '''开始时间'''
        return str(self.InsertTimeStart, 'GBK')

    def getInsertTimeEnd(self):
        '''结束时间'''
        return str(self.InsertTimeEnd, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'InsertTimeStart'={self.getInsertTimeStart()}, 'InsertTimeEnd'={self.getInsertTimeEnd()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcExchangeOptionSelfCloseField(Structure):
    """交易所期权自对冲信息"""
    _fields_ = [
        ("Volume", c_int32),
        ("RequestID", c_int32),
        ("BusinessUnit", c_char*21),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve1", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OptionSelfCloseSysID", c_char*21),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ExecResult", c_char),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("BranchID", c_char*9),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return TThostFtdcOptSelfCloseFlagType(ord(self.OptSelfCloseFlag)) if ord(self.OptSelfCloseFlag) in [e.value for e in list(TThostFtdcOptSelfCloseFlagType)] else list(TThostFtdcOptSelfCloseFlagType)[0]

    def getOptionSelfCloseLocalID(self):
        '''本地期权自对冲编号'''
        return str(self.OptionSelfCloseLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''期权自对冲提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOptionSelfCloseSysID(self):
        '''期权自对冲编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getExecResult(self):
        '''自对冲结果'''
        return TThostFtdcExecResultType(ord(self.ExecResult)) if ord(self.ExecResult) in [e.value for e in list(TThostFtdcExecResultType)] else list(TThostFtdcExecResultType)[0]

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'Volume'={self.getVolume()}, 'RequestID'={self.getRequestID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'HedgeFlag'={self.getHedgeFlag()}, 'OptSelfCloseFlag'={self.getOptSelfCloseFlag()}, 'OptionSelfCloseLocalID'={self.getOptionSelfCloseLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve1'={self.getreserve1()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'ExecResult'={self.getExecResult()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'BranchID'={self.getBranchID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryOptionSelfCloseActionField(Structure):
    """期权自对冲操作查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcExchangeOptionSelfCloseActionField(Structure):
    """交易所期权自对冲操作"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("OptionSelfCloseSysID", c_char*21),
        ("ActionFlag", c_char),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OptionSelfCloseLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("BranchID", c_char*9),
        ("reserve1", c_char*16),
        ("MacAddress", c_char*21),
        ("reserve2", c_char*31),
        ("OptSelfCloseFlag", c_char),
        ("IPAddress", c_char*33),
        ("ExchangeInstID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOptionSelfCloseSysID(self):
        '''期权自对冲操作编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOptionSelfCloseLocalID(self):
        '''本地期权自对冲编号'''
        return str(self.OptionSelfCloseLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return TThostFtdcOptSelfCloseFlagType(ord(self.OptSelfCloseFlag)) if ord(self.OptSelfCloseFlag) in [e.value for e in list(TThostFtdcOptSelfCloseFlagType)] else list(TThostFtdcOptSelfCloseFlagType)[0]

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'OptionSelfCloseSysID'={self.getOptionSelfCloseSysID()}, 'ActionFlag'={self.getActionFlag()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OptionSelfCloseLocalID'={self.getOptionSelfCloseLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'BranchID'={self.getBranchID()}, 'reserve1'={self.getreserve1()}, 'MacAddress'={self.getMacAddress()}, 'reserve2'={self.getreserve2()}, 'OptSelfCloseFlag'={self.getOptSelfCloseFlag()}, 'IPAddress'={self.getIPAddress()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcSyncDelaySwapField(Structure):
    """延时换汇同步"""
    _fields_ = [
        ("DelaySwapSeqNo", c_char*15),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("FromCurrencyID", c_char*4),
        ("FromAmount", c_double),
        ("FromFrozenSwap", c_double),
        ("FromRemainSwap", c_double),
        ("ToCurrencyID", c_char*4),
        ("ToAmount", c_double),
        ("IsManualSwap", c_int32),
        ("IsAllRemainSetZero", c_int32),
    ]

    def getDelaySwapSeqNo(self):
        '''换汇流水号'''
        return str(self.DelaySwapSeqNo, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getFromCurrencyID(self):
        '''源币种'''
        return str(self.FromCurrencyID, 'GBK')

    def getFromAmount(self):
        '''源金额'''
        return self.FromAmount

    def getFromFrozenSwap(self):
        '''源换汇冻结金额(可用冻结)'''
        return self.FromFrozenSwap

    def getFromRemainSwap(self):
        '''源剩余换汇额度(可提冻结)'''
        return self.FromRemainSwap

    def getToCurrencyID(self):
        '''目标币种'''
        return str(self.ToCurrencyID, 'GBK')

    def getToAmount(self):
        '''目标金额'''
        return self.ToAmount

    def getIsManualSwap(self):
        '''是否手工换汇'''
        return self.IsManualSwap

    def getIsAllRemainSetZero(self):
        '''是否将所有外币的剩余换汇额度设置为0'''
        return self.IsAllRemainSetZero

    def __str__(self): # 可以直接print
        return f"'DelaySwapSeqNo'={self.getDelaySwapSeqNo()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'FromCurrencyID'={self.getFromCurrencyID()}, 'FromAmount'={self.getFromAmount()}, 'FromFrozenSwap'={self.getFromFrozenSwap()}, 'FromRemainSwap'={self.getFromRemainSwap()}, 'ToCurrencyID'={self.getToCurrencyID()}, 'ToAmount'={self.getToAmount()}, 'IsManualSwap'={self.getIsManualSwap()}, 'IsAllRemainSetZero'={self.getIsAllRemainSetZero()}"


class  CThostFtdcQrySyncDelaySwapField(Structure):
    """查询延时换汇同步"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("DelaySwapSeqNo", c_char*15),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getDelaySwapSeqNo(self):
        '''延时换汇流水号'''
        return str(self.DelaySwapSeqNo, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'DelaySwapSeqNo'={self.getDelaySwapSeqNo()}"


class  CThostFtdcInvestUnitField(Structure):
    """投资单元"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("InvestUnitID", c_char*17),
        ("InvestorUnitName", c_char*81),
        ("InvestorGroupID", c_char*13),
        ("CommModelID", c_char*13),
        ("MarginModelID", c_char*13),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInvestorUnitName(self):
        '''投资者单元名称'''
        return str(self.InvestorUnitName, 'GBK')

    def getInvestorGroupID(self):
        '''投资者分组代码'''
        return str(self.InvestorGroupID, 'GBK')

    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')

    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InvestorUnitName'={self.getInvestorUnitName()}, 'InvestorGroupID'={self.getInvestorGroupID()}, 'CommModelID'={self.getCommModelID()}, 'MarginModelID'={self.getMarginModelID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcQryInvestUnitField(Structure):
    """查询投资单元"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcSecAgentCheckModeField(Structure):
    """二级代理商资金校验模式"""
    _fields_ = [
        ("InvestorID", c_char*13),
        ("BrokerID", c_char*11),
        ("CurrencyID", c_char*4),
        ("BrokerSecAgentID", c_char*13),
        ("CheckSelfAccount", c_int32),
    ]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getCurrencyID(self):
        '''币种'''
        return str(self.CurrencyID, 'GBK')

    def getBrokerSecAgentID(self):
        '''境外中介机构资金帐号'''
        return str(self.BrokerSecAgentID, 'GBK')

    def getCheckSelfAccount(self):
        '''是否需要校验自己的资金账户'''
        return self.CheckSelfAccount

    def __str__(self): # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'CurrencyID'={self.getCurrencyID()}, 'BrokerSecAgentID'={self.getBrokerSecAgentID()}, 'CheckSelfAccount'={self.getCheckSelfAccount()}"


class  CThostFtdcSecAgentTradeInfoField(Structure):
    """二级代理商信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("BrokerSecAgentID", c_char*13),
        ("InvestorID", c_char*13),
        ("LongCustomerName", c_char*161),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerSecAgentID(self):
        '''境外中介机构资金帐号'''
        return str(self.BrokerSecAgentID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getLongCustomerName(self):
        '''二级代理商姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'BrokerSecAgentID'={self.getBrokerSecAgentID()}, 'InvestorID'={self.getInvestorID()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcMarketDataField(Structure):
    """市场行情"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("reserve2", c_char*31),
        ("LastPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("ClosePrice", c_double),
        ("SettlementPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("PreDelta", c_double),
        ("CurrDelta", c_double),
        ("UpdateTime", c_char*9),
        ("UpdateMillisec", c_int32),
        ("ActionDay", c_char*9),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getPreSettlementPrice(self):
        '''上次结算价'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getSettlementPrice(self):
        '''本次结算价'''
        return self.SettlementPrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getActionDay(self):
        '''业务日期'''
        return str(self.ActionDay, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'reserve2'={self.getreserve2()}, 'LastPrice'={self.getLastPrice()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}, 'ClosePrice'={self.getClosePrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'PreDelta'={self.getPreDelta()}, 'CurrDelta'={self.getCurrDelta()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'ActionDay'={self.getActionDay()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcMarketDataBaseField(Structure):
    """行情基础属性"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getPreSettlementPrice(self):
        '''上次结算价'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'PreDelta'={self.getPreDelta()}"


class  CThostFtdcMarketDataStaticField(Structure):
    """行情静态属性"""
    _fields_ = [
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("ClosePrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("SettlementPrice", c_double),
        ("CurrDelta", c_double),
    ]

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getSettlementPrice(self):
        '''本次结算价'''
        return self.SettlementPrice

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def __str__(self): # 可以直接print
        return f"'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'ClosePrice'={self.getClosePrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'CurrDelta'={self.getCurrDelta()}"


class  CThostFtdcMarketDataLastMatchField(Structure):
    """行情最新成交属性"""
    _fields_ = [
        ("LastPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
    ]

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def __str__(self): # 可以直接print
        return f"'LastPrice'={self.getLastPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}"


class  CThostFtdcMarketDataBestPriceField(Structure):
    """行情最优价属性"""
    _fields_ = [
        ("BidPrice1", c_double),
        ("BidVolume1", c_int32),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int32),
    ]

    def getBidPrice1(self):
        '''申买价一'''
        return self.BidPrice1

    def getBidVolume1(self):
        '''申买量一'''
        return self.BidVolume1

    def getAskPrice1(self):
        '''申卖价一'''
        return self.AskPrice1

    def getAskVolume1(self):
        '''申卖量一'''
        return self.AskVolume1

    def __str__(self): # 可以直接print
        return f"'BidPrice1'={self.getBidPrice1()}, 'BidVolume1'={self.getBidVolume1()}, 'AskPrice1'={self.getAskPrice1()}, 'AskVolume1'={self.getAskVolume1()}"


class  CThostFtdcMarketDataBid23Field(Structure):
    """行情申买二、三属性"""
    _fields_ = [
        ("BidPrice2", c_double),
        ("BidVolume2", c_int32),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int32),
    ]

    def getBidPrice2(self):
        '''申买价二'''
        return self.BidPrice2

    def getBidVolume2(self):
        '''申买量二'''
        return self.BidVolume2

    def getBidPrice3(self):
        '''申买价三'''
        return self.BidPrice3

    def getBidVolume3(self):
        '''申买量三'''
        return self.BidVolume3

    def __str__(self): # 可以直接print
        return f"'BidPrice2'={self.getBidPrice2()}, 'BidVolume2'={self.getBidVolume2()}, 'BidPrice3'={self.getBidPrice3()}, 'BidVolume3'={self.getBidVolume3()}"


class  CThostFtdcMarketDataAsk23Field(Structure):
    """行情申卖二、三属性"""
    _fields_ = [
        ("AskPrice2", c_double),
        ("AskVolume2", c_int32),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int32),
    ]

    def getAskPrice2(self):
        '''申卖价二'''
        return self.AskPrice2

    def getAskVolume2(self):
        '''申卖量二'''
        return self.AskVolume2

    def getAskPrice3(self):
        '''申卖价三'''
        return self.AskPrice3

    def getAskVolume3(self):
        '''申卖量三'''
        return self.AskVolume3

    def __str__(self): # 可以直接print
        return f"'AskPrice2'={self.getAskPrice2()}, 'AskVolume2'={self.getAskVolume2()}, 'AskPrice3'={self.getAskPrice3()}, 'AskVolume3'={self.getAskVolume3()}"


class  CThostFtdcMarketDataBid45Field(Structure):
    """行情申买四、五属性"""
    _fields_ = [
        ("BidPrice4", c_double),
        ("BidVolume4", c_int32),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int32),
    ]

    def getBidPrice4(self):
        '''申买价四'''
        return self.BidPrice4

    def getBidVolume4(self):
        '''申买量四'''
        return self.BidVolume4

    def getBidPrice5(self):
        '''申买价五'''
        return self.BidPrice5

    def getBidVolume5(self):
        '''申买量五'''
        return self.BidVolume5

    def __str__(self): # 可以直接print
        return f"'BidPrice4'={self.getBidPrice4()}, 'BidVolume4'={self.getBidVolume4()}, 'BidPrice5'={self.getBidPrice5()}, 'BidVolume5'={self.getBidVolume5()}"


class  CThostFtdcMarketDataAsk45Field(Structure):
    """行情申卖四、五属性"""
    _fields_ = [
        ("AskPrice4", c_double),
        ("AskVolume4", c_int32),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int32),
    ]

    def getAskPrice4(self):
        '''申卖价四'''
        return self.AskPrice4

    def getAskVolume4(self):
        '''申卖量四'''
        return self.AskVolume4

    def getAskPrice5(self):
        '''申卖价五'''
        return self.AskPrice5

    def getAskVolume5(self):
        '''申卖量五'''
        return self.AskVolume5

    def __str__(self): # 可以直接print
        return f"'AskPrice4'={self.getAskPrice4()}, 'AskVolume4'={self.getAskVolume4()}, 'AskPrice5'={self.getAskPrice5()}, 'AskVolume5'={self.getAskVolume5()}"


class  CThostFtdcMarketDataUpdateTimeField(Structure):
    """行情更新时间属性"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("UpdateTime", c_char*9),
        ("UpdateMillisec", c_int32),
        ("ActionDay", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getActionDay(self):
        '''业务日期'''
        return str(self.ActionDay, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'ActionDay'={self.getActionDay()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcMarketDataExchangeField(Structure):
    """行情交易所代码属性"""
    _fields_ = [
        ("ExchangeID", c_char*9),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcSpecificInstrumentField(Structure):
    """指定的合约"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInstrumentStatusField(Structure):
    """合约状态"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("SettlementGroupID", c_char*9),
        ("reserve2", c_char*31),
        ("InstrumentStatus", c_char),
        ("TradingSegmentSN", c_int32),
        ("EnterTime", c_char*9),
        ("EnterReason", c_char),
        ("ExchangeInstID", c_char*81),
        ("InstrumentID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getSettlementGroupID(self):
        '''结算组代码'''
        return str(self.SettlementGroupID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getInstrumentStatus(self):
        '''合约交易状态'''
        return TThostFtdcInstrumentStatusType(ord(self.InstrumentStatus)) if ord(self.InstrumentStatus) in [e.value for e in list(TThostFtdcInstrumentStatusType)] else list(TThostFtdcInstrumentStatusType)[0]

    def getTradingSegmentSN(self):
        '''交易阶段编号'''
        return self.TradingSegmentSN

    def getEnterTime(self):
        '''进入本状态时间'''
        return str(self.EnterTime, 'GBK')

    def getEnterReason(self):
        '''进入本状态原因'''
        return TThostFtdcInstStatusEnterReasonType(ord(self.EnterReason)) if ord(self.EnterReason) in [e.value for e in list(TThostFtdcInstStatusEnterReasonType)] else list(TThostFtdcInstStatusEnterReasonType)[0]

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'SettlementGroupID'={self.getSettlementGroupID()}, 'reserve2'={self.getreserve2()}, 'InstrumentStatus'={self.getInstrumentStatus()}, 'TradingSegmentSN'={self.getTradingSegmentSN()}, 'EnterTime'={self.getEnterTime()}, 'EnterReason'={self.getEnterReason()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInstrumentStatusField(Structure):
    """查询合约状态"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("ExchangeInstID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'ExchangeInstID'={self.getExchangeInstID()}"


class  CThostFtdcInvestorAccountField(Structure):
    """投资者账户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcPositionProfitAlgorithmField(Structure):
    """浮动盈亏算法"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("Algorithm", c_char),
        ("Memo", c_char*161),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getAlgorithm(self):
        '''盈亏算法'''
        return TThostFtdcAlgorithmType(ord(self.Algorithm)) if ord(self.Algorithm) in [e.value for e in list(TThostFtdcAlgorithmType)] else list(TThostFtdcAlgorithmType)[0]

    def getMemo(self):
        '''备注'''
        return str(self.Memo, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'Algorithm'={self.getAlgorithm()}, 'Memo'={self.getMemo()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcDiscountField(Structure):
    """会员资金折扣"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char*13),
        ("Discount", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getDiscount(self):
        '''资金折扣比例'''
        return self.Discount

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorRange'={self.getInvestorRange()}, 'InvestorID'={self.getInvestorID()}, 'Discount'={self.getDiscount()}"


class  CThostFtdcQryTransferBankField(Structure):
    """查询转帐银行"""
    _fields_ = [
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
    ]

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}"


class  CThostFtdcTransferBankField(Structure):
    """转帐银行"""
    _fields_ = [
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
        ("BankName", c_char*101),
        ("IsActive", c_int32),
    ]

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')

    def getBankName(self):
        '''银行名称'''
        return str(self.BankName, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def __str__(self): # 可以直接print
        return f"'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}, 'BankName'={self.getBankName()}, 'IsActive'={self.getIsActive()}"


class  CThostFtdcQryInvestorPositionDetailField(Structure):
    """查询投资者持仓明细"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcInvestorPositionDetailField(Structure):
    """投资者持仓明细"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("OpenDate", c_char*9),
        ("TradeID", c_char*21),
        ("Volume", c_int32),
        ("OpenPrice", c_double),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("TradeType", c_char),
        ("reserve2", c_char*31),
        ("ExchangeID", c_char*9),
        ("CloseProfitByDate", c_double),
        ("CloseProfitByTrade", c_double),
        ("PositionProfitByDate", c_double),
        ("PositionProfitByTrade", c_double),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LastSettlementPrice", c_double),
        ("SettlementPrice", c_double),
        ("CloseVolume", c_int32),
        ("CloseAmount", c_double),
        ("TimeFirstVolume", c_int32),
        ("InvestUnitID", c_char*17),
        ("SpecPosiType", c_char),
        ("InstrumentID", c_char*81),
        ("CombInstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getDirection(self):
        '''买卖'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getOpenDate(self):
        '''开仓日期'''
        return str(self.OpenDate, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getOpenPrice(self):
        '''开仓价'''
        return self.OpenPrice

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getTradeType(self):
        '''成交类型'''
        return TThostFtdcTradeTypeType(ord(self.TradeType)) if ord(self.TradeType) in [e.value for e in list(TThostFtdcTradeTypeType)] else list(TThostFtdcTradeTypeType)[0]

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getCloseProfitByDate(self):
        '''逐日盯市平仓盈亏'''
        return self.CloseProfitByDate

    def getCloseProfitByTrade(self):
        '''逐笔对冲平仓盈亏'''
        return self.CloseProfitByTrade

    def getPositionProfitByDate(self):
        '''逐日盯市持仓盈亏'''
        return self.PositionProfitByDate

    def getPositionProfitByTrade(self):
        '''逐笔对冲持仓盈亏'''
        return self.PositionProfitByTrade

    def getMargin(self):
        '''投资者保证金'''
        return self.Margin

    def getExchMargin(self):
        '''交易所保证金'''
        return self.ExchMargin

    def getMarginRateByMoney(self):
        '''保证金率'''
        return self.MarginRateByMoney

    def getMarginRateByVolume(self):
        '''保证金率(按手数)'''
        return self.MarginRateByVolume

    def getLastSettlementPrice(self):
        '''昨结算价'''
        return self.LastSettlementPrice

    def getSettlementPrice(self):
        '''结算价'''
        return self.SettlementPrice

    def getCloseVolume(self):
        '''平仓量'''
        return self.CloseVolume

    def getCloseAmount(self):
        '''平仓金额'''
        return self.CloseAmount

    def getTimeFirstVolume(self):
        '''先开先平剩余数量（DCE）'''
        return self.TimeFirstVolume

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getSpecPosiType(self):
        '''特殊持仓标志'''
        return TThostFtdcSpecPosiTypeType(ord(self.SpecPosiType)) if ord(self.SpecPosiType) in [e.value for e in list(TThostFtdcSpecPosiTypeType)] else list(TThostFtdcSpecPosiTypeType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Direction'={self.getDirection()}, 'OpenDate'={self.getOpenDate()}, 'TradeID'={self.getTradeID()}, 'Volume'={self.getVolume()}, 'OpenPrice'={self.getOpenPrice()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'TradeType'={self.getTradeType()}, 'reserve2'={self.getreserve2()}, 'ExchangeID'={self.getExchangeID()}, 'CloseProfitByDate'={self.getCloseProfitByDate()}, 'CloseProfitByTrade'={self.getCloseProfitByTrade()}, 'PositionProfitByDate'={self.getPositionProfitByDate()}, 'PositionProfitByTrade'={self.getPositionProfitByTrade()}, 'Margin'={self.getMargin()}, 'ExchMargin'={self.getExchMargin()}, 'MarginRateByMoney'={self.getMarginRateByMoney()}, 'MarginRateByVolume'={self.getMarginRateByVolume()}, 'LastSettlementPrice'={self.getLastSettlementPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'CloseVolume'={self.getCloseVolume()}, 'CloseAmount'={self.getCloseAmount()}, 'TimeFirstVolume'={self.getTimeFirstVolume()}, 'InvestUnitID'={self.getInvestUnitID()}, 'SpecPosiType'={self.getSpecPosiType()}, 'InstrumentID'={self.getInstrumentID()}, 'CombInstrumentID'={self.getCombInstrumentID()}"


class  CThostFtdcTradingAccountPasswordField(Structure):
    """资金账户口令域"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcMDTraderOfferField(Structure):
    """交易所行情报盘机"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("TraderID", c_char*21),
        ("ParticipantID", c_char*11),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", c_char*9),
        ("ConnectRequestTime", c_char*9),
        ("LastReportDate", c_char*9),
        ("LastReportTime", c_char*9),
        ("ConnectDate", c_char*9),
        ("ConnectTime", c_char*9),
        ("StartDate", c_char*9),
        ("StartTime", c_char*9),
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("MaxTradeID", c_char*21),
        ("MaxOrderMessageReference", c_char*7),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getTraderConnectStatus(self):
        '''交易所交易员连接状态'''
        return TThostFtdcTraderConnectStatusType(ord(self.TraderConnectStatus)) if ord(self.TraderConnectStatus) in [e.value for e in list(TThostFtdcTraderConnectStatusType)] else list(TThostFtdcTraderConnectStatusType)[0]

    def getConnectRequestDate(self):
        '''发出连接请求的日期'''
        return str(self.ConnectRequestDate, 'GBK')

    def getConnectRequestTime(self):
        '''发出连接请求的时间'''
        return str(self.ConnectRequestTime, 'GBK')

    def getLastReportDate(self):
        '''上次报告日期'''
        return str(self.LastReportDate, 'GBK')

    def getLastReportTime(self):
        '''上次报告时间'''
        return str(self.LastReportTime, 'GBK')

    def getConnectDate(self):
        '''完成连接日期'''
        return str(self.ConnectDate, 'GBK')

    def getConnectTime(self):
        '''完成连接时间'''
        return str(self.ConnectTime, 'GBK')

    def getStartDate(self):
        '''启动日期'''
        return str(self.StartDate, 'GBK')

    def getStartTime(self):
        '''启动时间'''
        return str(self.StartTime, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getMaxTradeID(self):
        '''本席位最大成交编号'''
        return str(self.MaxTradeID, 'GBK')

    def getMaxOrderMessageReference(self):
        '''本席位最大报单备拷'''
        return str(self.MaxOrderMessageReference, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TraderID'={self.getTraderID()}, 'ParticipantID'={self.getParticipantID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'TraderConnectStatus'={self.getTraderConnectStatus()}, 'ConnectRequestDate'={self.getConnectRequestDate()}, 'ConnectRequestTime'={self.getConnectRequestTime()}, 'LastReportDate'={self.getLastReportDate()}, 'LastReportTime'={self.getLastReportTime()}, 'ConnectDate'={self.getConnectDate()}, 'ConnectTime'={self.getConnectTime()}, 'StartDate'={self.getStartDate()}, 'StartTime'={self.getStartTime()}, 'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'MaxTradeID'={self.getMaxTradeID()}, 'MaxOrderMessageReference'={self.getMaxOrderMessageReference()}"


class  CThostFtdcQryMDTraderOfferField(Structure):
    """查询行情报盘机"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("TraderID", c_char*21),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'TraderID'={self.getTraderID()}"


class  CThostFtdcQryNoticeField(Structure):
    """查询客户通知"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcNoticeField(Structure):
    """客户通知"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("Content", c_char*501),
        ("SequenceLabel", c_char*2),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getContent(self):
        '''消息正文'''
        return str(self.Content, 'GBK')

    def getSequenceLabel(self):
        '''经纪公司通知内容序列号'''
        return str(self.SequenceLabel, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'Content'={self.getContent()}, 'SequenceLabel'={self.getSequenceLabel()}"


class  CThostFtdcUserRightField(Structure):
    """用户权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserRightType", c_char),
        ("IsForbidden", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserRightType(self):
        '''客户权限类型'''
        return TThostFtdcUserRightTypeType(ord(self.UserRightType)) if ord(self.UserRightType) in [e.value for e in list(TThostFtdcUserRightTypeType)] else list(TThostFtdcUserRightTypeType)[0]

    def getIsForbidden(self):
        '''是否禁止'''
        return self.IsForbidden

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserRightType'={self.getUserRightType()}, 'IsForbidden'={self.getIsForbidden()}"


class  CThostFtdcQrySettlementInfoConfirmField(Structure):
    """查询结算信息确认域"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcLoadSettlementInfoField(Structure):
    """装载结算信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcBrokerWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("WithdrawAlgorithm", c_char),
        ("UsingRatio", c_double),
        ("IncludeCloseProfit", c_char),
        ("AllWithoutTrade", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("IsBrokerUserEvent", c_int32),
        ("CurrencyID", c_char*4),
        ("FundMortgageRatio", c_double),
        ("BalanceAlgorithm", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getWithdrawAlgorithm(self):
        '''可提资金算法'''
        return TThostFtdcAlgorithmType(ord(self.WithdrawAlgorithm)) if ord(self.WithdrawAlgorithm) in [e.value for e in list(TThostFtdcAlgorithmType)] else list(TThostFtdcAlgorithmType)[0]

    def getUsingRatio(self):
        '''资金使用率'''
        return self.UsingRatio

    def getIncludeCloseProfit(self):
        '''可提是否包含平仓盈利'''
        return TThostFtdcIncludeCloseProfitType(ord(self.IncludeCloseProfit)) if ord(self.IncludeCloseProfit) in [e.value for e in list(TThostFtdcIncludeCloseProfitType)] else list(TThostFtdcIncludeCloseProfitType)[0]

    def getAllWithoutTrade(self):
        '''本日无仓且无成交客户是否受可提比例限制'''
        return TThostFtdcAllWithoutTradeType(ord(self.AllWithoutTrade)) if ord(self.AllWithoutTrade) in [e.value for e in list(TThostFtdcAllWithoutTradeType)] else list(TThostFtdcAllWithoutTradeType)[0]

    def getAvailIncludeCloseProfit(self):
        '''可用是否包含平仓盈利'''
        return TThostFtdcIncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)) if ord(self.AvailIncludeCloseProfit) in [e.value for e in list(TThostFtdcIncludeCloseProfitType)] else list(TThostFtdcIncludeCloseProfitType)[0]

    def getIsBrokerUserEvent(self):
        '''是否启用用户事件'''
        return self.IsBrokerUserEvent

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getFundMortgageRatio(self):
        '''货币质押比率'''
        return self.FundMortgageRatio

    def getBalanceAlgorithm(self):
        '''权益算法'''
        return TThostFtdcBalanceAlgorithmType(ord(self.BalanceAlgorithm)) if ord(self.BalanceAlgorithm) in [e.value for e in list(TThostFtdcBalanceAlgorithmType)] else list(TThostFtdcBalanceAlgorithmType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'WithdrawAlgorithm'={self.getWithdrawAlgorithm()}, 'UsingRatio'={self.getUsingRatio()}, 'IncludeCloseProfit'={self.getIncludeCloseProfit()}, 'AllWithoutTrade'={self.getAllWithoutTrade()}, 'AvailIncludeCloseProfit'={self.getAvailIncludeCloseProfit()}, 'IsBrokerUserEvent'={self.getIsBrokerUserEvent()}, 'CurrencyID'={self.getCurrencyID()}, 'FundMortgageRatio'={self.getFundMortgageRatio()}, 'BalanceAlgorithm'={self.getBalanceAlgorithm()}"


class  CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OldPassword", c_char*41),
        ("NewPassword", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOldPassword(self):
        '''原来的口令'''
        return str(self.OldPassword, 'GBK')

    def getNewPassword(self):
        '''新的口令'''
        return str(self.NewPassword, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OldPassword'={self.getOldPassword()}, 'NewPassword'={self.getNewPassword()}"


class  CThostFtdcTradingAccountPasswordUpdateField(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("OldPassword", c_char*41),
        ("NewPassword", c_char*41),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getOldPassword(self):
        '''原来的口令'''
        return str(self.OldPassword, 'GBK')

    def getNewPassword(self):
        '''新的口令'''
        return str(self.NewPassword, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'OldPassword'={self.getOldPassword()}, 'NewPassword'={self.getNewPassword()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcQryCombinationLegField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("LegID", c_int32),
        ("reserve2", c_char*31),
        ("CombInstrumentID", c_char*81),
        ("LegInstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLegID(self):
        '''单腿编号'''
        return self.LegID

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getLegInstrumentID(self):
        '''单腿合约代码'''
        return str(self.LegInstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'LegID'={self.getLegID()}, 'reserve2'={self.getreserve2()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'LegInstrumentID'={self.getLegInstrumentID()}"


class  CThostFtdcQrySyncStatusField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("TradingDay", c_char*9),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}"


class  CThostFtdcCombinationLegField(Structure):
    """组合交易合约的单腿"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("LegID", c_int32),
        ("reserve2", c_char*31),
        ("Direction", c_char),
        ("LegMultiple", c_int32),
        ("ImplyLevel", c_int32),
        ("CombInstrumentID", c_char*81),
        ("LegInstrumentID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLegID(self):
        '''单腿编号'''
        return self.LegID

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getLegMultiple(self):
        '''单腿乘数'''
        return self.LegMultiple

    def getImplyLevel(self):
        '''派生层数'''
        return self.ImplyLevel

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getLegInstrumentID(self):
        '''单腿合约代码'''
        return str(self.LegInstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'LegID'={self.getLegID()}, 'reserve2'={self.getreserve2()}, 'Direction'={self.getDirection()}, 'LegMultiple'={self.getLegMultiple()}, 'ImplyLevel'={self.getImplyLevel()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'LegInstrumentID'={self.getLegInstrumentID()}"


class  CThostFtdcSyncStatusField(Structure):
    """数据同步状态"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("DataSyncStatus", c_char),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getDataSyncStatus(self):
        '''数据同步状态'''
        return TThostFtdcDataSyncStatusType(ord(self.DataSyncStatus)) if ord(self.DataSyncStatus) in [e.value for e in list(TThostFtdcDataSyncStatusType)] else list(TThostFtdcDataSyncStatusType)[0]

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'DataSyncStatus'={self.getDataSyncStatus()}"


class  CThostFtdcQryLinkManField(Structure):
    """查询联系人"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcLinkManField(Structure):
    """联系人"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("PersonType", c_char),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("PersonName", c_char*81),
        ("Telephone", c_char*41),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Priority", c_int32),
        ("UOAZipCode", c_char*11),
        ("PersonFullName", c_char*101),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getPersonType(self):
        '''联系人类型'''
        return TThostFtdcPersonTypeType(ord(self.PersonType)) if ord(self.PersonType) in [e.value for e in list(TThostFtdcPersonTypeType)] else list(TThostFtdcPersonTypeType)[0]

    def getIdentifiedCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdentifiedCardType)) if ord(self.IdentifiedCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getPersonName(self):
        '''名称'''
        return str(self.PersonName, 'GBK')

    def getTelephone(self):
        '''联系电话'''
        return str(self.Telephone, 'GBK')

    def getAddress(self):
        '''通讯地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮政编码'''
        return str(self.ZipCode, 'GBK')

    def getPriority(self):
        '''优先级'''
        return self.Priority

    def getUOAZipCode(self):
        '''开户邮政编码'''
        return str(self.UOAZipCode, 'GBK')

    def getPersonFullName(self):
        '''全称'''
        return str(self.PersonFullName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'PersonType'={self.getPersonType()}, 'IdentifiedCardType'={self.getIdentifiedCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'PersonName'={self.getPersonName()}, 'Telephone'={self.getTelephone()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Priority'={self.getPriority()}, 'UOAZipCode'={self.getUOAZipCode()}, 'PersonFullName'={self.getPersonFullName()}"


class  CThostFtdcQryBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserEventType", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserEventType(self):
        '''用户事件类型'''
        return TThostFtdcUserEventTypeType(ord(self.UserEventType)) if ord(self.UserEventType) in [e.value for e in list(TThostFtdcUserEventTypeType)] else list(TThostFtdcUserEventTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserEventType'={self.getUserEventType()}"


class  CThostFtdcBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("UserEventType", c_char),
        ("EventSequenceNo", c_int32),
        ("EventDate", c_char*9),
        ("EventTime", c_char*9),
        ("UserEventInfo", c_char*1025),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserEventType(self):
        '''用户事件类型'''
        return TThostFtdcUserEventTypeType(ord(self.UserEventType)) if ord(self.UserEventType) in [e.value for e in list(TThostFtdcUserEventTypeType)] else list(TThostFtdcUserEventTypeType)[0]

    def getEventSequenceNo(self):
        '''用户事件序号'''
        return self.EventSequenceNo

    def getEventDate(self):
        '''事件发生日期'''
        return str(self.EventDate, 'GBK')

    def getEventTime(self):
        '''事件发生时间'''
        return str(self.EventTime, 'GBK')

    def getUserEventInfo(self):
        '''用户事件信息'''
        return str(self.UserEventInfo, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'UserEventType'={self.getUserEventType()}, 'EventSequenceNo'={self.getEventSequenceNo()}, 'EventDate'={self.getEventDate()}, 'EventTime'={self.getEventTime()}, 'UserEventInfo'={self.getUserEventInfo()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryContractBankField(Structure):
    """查询签约银行请求"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}"


class  CThostFtdcContractBankField(Structure):
    """查询签约银行响应"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("BankID", c_char*4),
        ("BankBrchID", c_char*5),
        ("BankName", c_char*101),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')

    def getBankName(self):
        '''银行名称'''
        return str(self.BankName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'BankID'={self.getBankID()}, 'BankBrchID'={self.getBankBrchID()}, 'BankName'={self.getBankName()}"


class  CThostFtdcInvestorPositionCombineDetailField(Structure):
    """投资者组合持仓明细"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("OpenDate", c_char*9),
        ("ExchangeID", c_char*9),
        ("SettlementID", c_int32),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ComTradeID", c_char*21),
        ("TradeID", c_char*21),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", c_int32),
        ("Margin", c_double),
        ("ExchMargin", c_double),
        ("MarginRateByMoney", c_double),
        ("MarginRateByVolume", c_double),
        ("LegID", c_int32),
        ("LegMultiple", c_int32),
        ("reserve2", c_char*31),
        ("TradeGroupID", c_int32),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
        ("CombInstrumentID", c_char*81),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getOpenDate(self):
        '''开仓日期'''
        return str(self.OpenDate, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getComTradeID(self):
        '''组合编号'''
        return str(self.ComTradeID, 'GBK')

    def getTradeID(self):
        '''撮合编号'''
        return str(self.TradeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getDirection(self):
        '''买卖'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getTotalAmt(self):
        '''持仓量'''
        return self.TotalAmt

    def getMargin(self):
        '''投资者保证金'''
        return self.Margin

    def getExchMargin(self):
        '''交易所保证金'''
        return self.ExchMargin

    def getMarginRateByMoney(self):
        '''保证金率'''
        return self.MarginRateByMoney

    def getMarginRateByVolume(self):
        '''保证金率(按手数)'''
        return self.MarginRateByVolume

    def getLegID(self):
        '''单腿编号'''
        return self.LegID

    def getLegMultiple(self):
        '''单腿乘数'''
        return self.LegMultiple

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTradeGroupID(self):
        '''成交组号'''
        return self.TradeGroupID

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getCombInstrumentID(self):
        '''组合持仓合约编码'''
        return str(self.CombInstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'OpenDate'={self.getOpenDate()}, 'ExchangeID'={self.getExchangeID()}, 'SettlementID'={self.getSettlementID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ComTradeID'={self.getComTradeID()}, 'TradeID'={self.getTradeID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Direction'={self.getDirection()}, 'TotalAmt'={self.getTotalAmt()}, 'Margin'={self.getMargin()}, 'ExchMargin'={self.getExchMargin()}, 'MarginRateByMoney'={self.getMarginRateByMoney()}, 'MarginRateByVolume'={self.getMarginRateByVolume()}, 'LegID'={self.getLegID()}, 'LegMultiple'={self.getLegMultiple()}, 'reserve2'={self.getreserve2()}, 'TradeGroupID'={self.getTradeGroupID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}, 'CombInstrumentID'={self.getCombInstrumentID()}"


class  CThostFtdcParkedOrderField(Structure):
    """预埋单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("UserForceClose", c_int32),
        ("ExchangeID", c_char*9),
        ("ParkedOrderID", c_char*13),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("IsSwapOrder", c_int32),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getUserForceClose(self):
        '''用户强评标志'''
        return self.UserForceClose

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParkedOrderID(self):
        '''预埋报单编号'''
        return str(self.ParkedOrderID, 'GBK')

    def getUserType(self):
        '''用户类型'''
        return TThostFtdcUserTypeType(ord(self.UserType)) if ord(self.UserType) in [e.value for e in list(TThostFtdcUserTypeType)] else list(TThostFtdcUserTypeType)[0]

    def getStatus(self):
        '''预埋单状态'''
        return TThostFtdcParkedOrderStatusType(ord(self.Status)) if ord(self.Status) in [e.value for e in list(TThostFtdcParkedOrderStatusType)] else list(TThostFtdcParkedOrderStatusType)[0]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getIsSwapOrder(self):
        '''互换单标志'''
        return self.IsSwapOrder

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'UserForceClose'={self.getUserForceClose()}, 'ExchangeID'={self.getExchangeID()}, 'ParkedOrderID'={self.getParkedOrderID()}, 'UserType'={self.getUserType()}, 'Status'={self.getStatus()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'IsSwapOrder'={self.getIsSwapOrder()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcParkedOrderActionField(Structure):
    """输入预埋单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("OrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("UserID", c_char*16),
        ("reserve1", c_char*31),
        ("ParkedOrderActionID", c_char*13),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getParkedOrderActionID(self):
        '''预埋撤单单编号'''
        return str(self.ParkedOrderActionID, 'GBK')

    def getUserType(self):
        '''用户类型'''
        return TThostFtdcUserTypeType(ord(self.UserType)) if ord(self.UserType) in [e.value for e in list(TThostFtdcUserTypeType)] else list(TThostFtdcUserTypeType)[0]

    def getStatus(self):
        '''预埋撤单状态'''
        return TThostFtdcParkedOrderStatusType(ord(self.Status)) if ord(self.Status) in [e.value for e in list(TThostFtdcParkedOrderStatusType)] else list(TThostFtdcParkedOrderStatusType)[0]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'OrderRef'={self.getOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'ParkedOrderActionID'={self.getParkedOrderActionID()}, 'UserType'={self.getUserType()}, 'Status'={self.getStatus()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryParkedOrderField(Structure):
    """查询预埋单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryParkedOrderActionField(Structure):
    """查询预埋撤单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcRemoveParkedOrderField(Structure):
    """删除预埋单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ParkedOrderID", c_char*13),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getParkedOrderID(self):
        '''预埋报单编号'''
        return str(self.ParkedOrderID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ParkedOrderID'={self.getParkedOrderID()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcRemoveParkedOrderActionField(Structure):
    """删除预埋撤单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ParkedOrderActionID", c_char*13),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getParkedOrderActionID(self):
        '''预埋撤单编号'''
        return str(self.ParkedOrderActionID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ParkedOrderActionID'={self.getParkedOrderActionID()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcInvestorWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char*13),
        ("UsingRatio", c_double),
        ("CurrencyID", c_char*4),
        ("FundMortgageRatio", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getUsingRatio(self):
        '''可提资金比例'''
        return self.UsingRatio

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getFundMortgageRatio(self):
        '''货币质押比率'''
        return self.FundMortgageRatio

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorRange'={self.getInvestorRange()}, 'InvestorID'={self.getInvestorID()}, 'UsingRatio'={self.getUsingRatio()}, 'CurrencyID'={self.getCurrencyID()}, 'FundMortgageRatio'={self.getFundMortgageRatio()}"


class  CThostFtdcQryInvestorPositionCombineDetailField(Structure):
    """查询组合持仓明细"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("CombInstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getCombInstrumentID(self):
        '''组合持仓合约编码'''
        return str(self.CombInstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'CombInstrumentID'={self.getCombInstrumentID()}"


class  CThostFtdcMarketDataAveragePriceField(Structure):
    """成交均价"""
    _fields_ = [
        ("AveragePrice", c_double),
    ]

    def getAveragePrice(self):
        '''当日均价'''
        return self.AveragePrice

    def __str__(self): # 可以直接print
        return f"'AveragePrice'={self.getAveragePrice()}"


class  CThostFtdcVerifyInvestorPasswordField(Structure):
    """校验投资者密码"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Password", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Password'={self.getPassword()}"


class  CThostFtdcUserIPField(Structure):
    """用户IP"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("reserve1", c_char*16),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("IPAddress", c_char*33),
        ("IPMask", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def getIPMask(self):
        '''IP地址掩码'''
        return str(self.IPMask, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'IPAddress'={self.getIPAddress()}, 'IPMask'={self.getIPMask()}"


class  CThostFtdcTradingNoticeInfoField(Structure):
    """用户事件通知信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("SendTime", c_char*9),
        ("FieldContent", c_char*501),
        ("SequenceSeries", c_short),
        ("SequenceNo", c_int32),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getSendTime(self):
        '''发送时间'''
        return str(self.SendTime, 'GBK')

    def getFieldContent(self):
        '''消息正文'''
        return str(self.FieldContent, 'GBK')

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'SendTime'={self.getSendTime()}, 'FieldContent'={self.getFieldContent()}, 'SequenceSeries'={self.getSequenceSeries()}, 'SequenceNo'={self.getSequenceNo()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcTradingNoticeField(Structure):
    """用户事件通知"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorRange", c_char),
        ("InvestorID", c_char*13),
        ("SequenceSeries", c_short),
        ("UserID", c_char*16),
        ("SendTime", c_char*9),
        ("SequenceNo", c_int32),
        ("FieldContent", c_char*501),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcInvestorRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcInvestorRangeType)] else list(TThostFtdcInvestorRangeType)[0]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getSendTime(self):
        '''发送时间'''
        return str(self.SendTime, 'GBK')

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def getFieldContent(self):
        '''消息正文'''
        return str(self.FieldContent, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorRange'={self.getInvestorRange()}, 'InvestorID'={self.getInvestorID()}, 'SequenceSeries'={self.getSequenceSeries()}, 'UserID'={self.getUserID()}, 'SendTime'={self.getSendTime()}, 'SequenceNo'={self.getSequenceNo()}, 'FieldContent'={self.getFieldContent()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcQryTradingNoticeField(Structure):
    """查询交易事件通知"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcQryErrOrderField(Structure):
    """查询错误报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcErrOrderField(Structure):
    """错误报单"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("UserForceClose", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("IsSwapOrder", c_int32),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("ClientID", c_char*11),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getUserForceClose(self):
        '''用户强评标志'''
        return self.UserForceClose

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getIsSwapOrder(self):
        '''互换单标志'''
        return self.IsSwapOrder

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getClientID(self):
        '''交易编码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'UserForceClose'={self.getUserForceClose()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'IsSwapOrder'={self.getIsSwapOrder()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcErrorConditionalOrderField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("OrderRef", c_char*13),
        ("UserID", c_char*16),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", c_char*5),
        ("CombHedgeFlag", c_char*5),
        ("LimitPrice", c_double),
        ("VolumeTotalOriginal", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char*9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("ContingentCondition", c_char),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char*21),
        ("RequestID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ExchangeID", c_char*9),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("reserve2", c_char*31),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", c_int32),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("OrderSysID", c_char*21),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", c_int32),
        ("VolumeTotal", c_int32),
        ("InsertDate", c_char*9),
        ("InsertTime", c_char*9),
        ("ActiveTime", c_char*9),
        ("SuspendTime", c_char*9),
        ("UpdateTime", c_char*9),
        ("CancelTime", c_char*9),
        ("ActiveTraderID", c_char*21),
        ("ClearingPartID", c_char*11),
        ("SequenceNo", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("UserProductInfo", c_char*11),
        ("StatusMsg", c_char*81),
        ("UserForceClose", c_int32),
        ("ActiveUserID", c_char*16),
        ("BrokerOrderSeq", c_int32),
        ("RelativeOrderSysID", c_char*21),
        ("ZCETotalTradedVolume", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("IsSwapOrder", c_int32),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("reserve3", c_char*16),
        ("MacAddress", c_char*21),
        ("InstrumentID", c_char*81),
        ("ExchangeInstID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOrderPriceType(self):
        '''报单价格条件'''
        return TThostFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TThostFtdcOrderPriceTypeType)] else list(TThostFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getCombOffsetFlag(self):
        '''组合开平标志'''
        return str(self.CombOffsetFlag, 'GBK')

    def getCombHedgeFlag(self):
        '''组合投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeTotalOriginal(self):
        '''数量'''
        return self.VolumeTotalOriginal

    def getTimeCondition(self):
        '''有效期类型'''
        return TThostFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TThostFtdcTimeConditionType)] else list(TThostFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TThostFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TThostFtdcVolumeConditionType)] else list(TThostFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getContingentCondition(self):
        '''触发条件'''
        return TThostFtdcContingentConditionType(ord(self.ContingentCondition)) if ord(self.ContingentCondition) in [e.value for e in list(TThostFtdcContingentConditionType)] else list(TThostFtdcContingentConditionType)[0]

    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TThostFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TThostFtdcForceCloseReasonType)] else list(TThostFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderSubmitStatus(self):
        '''报单提交状态'''
        return TThostFtdcOrderSubmitStatusType(ord(self.OrderSubmitStatus)) if ord(self.OrderSubmitStatus) in [e.value for e in list(TThostFtdcOrderSubmitStatusType)] else list(TThostFtdcOrderSubmitStatusType)[0]

    def getNotifySequence(self):
        '''报单提示序号'''
        return self.NotifySequence

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getOrderSource(self):
        '''报单来源'''
        return TThostFtdcOrderSourceType(ord(self.OrderSource)) if ord(self.OrderSource) in [e.value for e in list(TThostFtdcOrderSourceType)] else list(TThostFtdcOrderSourceType)[0]

    def getOrderStatus(self):
        '''报单状态'''
        return TThostFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TThostFtdcOrderStatusType)] else list(TThostFtdcOrderStatusType)[0]

    def getOrderType(self):
        '''报单类型'''
        return TThostFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TThostFtdcOrderTypeType)] else list(TThostFtdcOrderTypeType)[0]

    def getVolumeTraded(self):
        '''今成交数量'''
        return self.VolumeTraded

    def getVolumeTotal(self):
        '''剩余数量'''
        return self.VolumeTotal

    def getInsertDate(self):
        '''报单日期'''
        return str(self.InsertDate, 'GBK')

    def getInsertTime(self):
        '''委托时间'''
        return str(self.InsertTime, 'GBK')

    def getActiveTime(self):
        '''激活时间'''
        return str(self.ActiveTime, 'GBK')

    def getSuspendTime(self):
        '''挂起时间'''
        return str(self.SuspendTime, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getActiveTraderID(self):
        '''最后修改交易所交易员代码'''
        return str(self.ActiveTraderID, 'GBK')

    def getClearingPartID(self):
        '''结算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getUserForceClose(self):
        '''用户强评标志'''
        return self.UserForceClose

    def getActiveUserID(self):
        '''操作用户代码'''
        return str(self.ActiveUserID, 'GBK')

    def getBrokerOrderSeq(self):
        '''经纪公司报单编号'''
        return self.BrokerOrderSeq

    def getRelativeOrderSysID(self):
        '''相关报单'''
        return str(self.RelativeOrderSysID, 'GBK')

    def getZCETotalTradedVolume(self):
        '''郑商所成交数量'''
        return self.ZCETotalTradedVolume

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getIsSwapOrder(self):
        '''互换单标志'''
        return self.IsSwapOrder

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getAccountID(self):
        '''资金账号'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getreserve3(self):
        '''保留的无效字段'''
        return str(self.reserve3, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'OrderRef'={self.getOrderRef()}, 'UserID'={self.getUserID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'CombOffsetFlag'={self.getCombOffsetFlag()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeTotalOriginal'={self.getVolumeTotalOriginal()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'ContingentCondition'={self.getContingentCondition()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'RequestID'={self.getRequestID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ExchangeID'={self.getExchangeID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'reserve2'={self.getreserve2()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderSubmitStatus'={self.getOrderSubmitStatus()}, 'NotifySequence'={self.getNotifySequence()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'OrderSysID'={self.getOrderSysID()}, 'OrderSource'={self.getOrderSource()}, 'OrderStatus'={self.getOrderStatus()}, 'OrderType'={self.getOrderType()}, 'VolumeTraded'={self.getVolumeTraded()}, 'VolumeTotal'={self.getVolumeTotal()}, 'InsertDate'={self.getInsertDate()}, 'InsertTime'={self.getInsertTime()}, 'ActiveTime'={self.getActiveTime()}, 'SuspendTime'={self.getSuspendTime()}, 'UpdateTime'={self.getUpdateTime()}, 'CancelTime'={self.getCancelTime()}, 'ActiveTraderID'={self.getActiveTraderID()}, 'ClearingPartID'={self.getClearingPartID()}, 'SequenceNo'={self.getSequenceNo()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'UserProductInfo'={self.getUserProductInfo()}, 'StatusMsg'={self.getStatusMsg()}, 'UserForceClose'={self.getUserForceClose()}, 'ActiveUserID'={self.getActiveUserID()}, 'BrokerOrderSeq'={self.getBrokerOrderSeq()}, 'RelativeOrderSysID'={self.getRelativeOrderSysID()}, 'ZCETotalTradedVolume'={self.getZCETotalTradedVolume()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'IsSwapOrder'={self.getIsSwapOrder()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'reserve3'={self.getreserve3()}, 'MacAddress'={self.getMacAddress()}, 'InstrumentID'={self.getInstrumentID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryErrOrderActionField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcErrOrderActionField(Structure):
    """错误报单操作"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("OrderActionRef", c_int32),
        ("OrderRef", c_char*13),
        ("RequestID", c_int32),
        ("FrontID", c_int32),
        ("SessionID", c_int32),
        ("ExchangeID", c_char*9),
        ("OrderSysID", c_char*21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("ActionDate", c_char*9),
        ("ActionTime", c_char*9),
        ("TraderID", c_char*21),
        ("InstallID", c_int32),
        ("OrderLocalID", c_char*13),
        ("ActionLocalID", c_char*13),
        ("ParticipantID", c_char*11),
        ("ClientID", c_char*11),
        ("BusinessUnit", c_char*21),
        ("OrderActionStatus", c_char),
        ("UserID", c_char*16),
        ("StatusMsg", c_char*81),
        ("reserve1", c_char*31),
        ("BranchID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("reserve2", c_char*16),
        ("MacAddress", c_char*21),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("InstrumentID", c_char*81),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getOrderActionRef(self):
        '''报单操作引用'''
        return self.OrderActionRef

    def getOrderRef(self):
        '''报单引用'''
        return str(self.OrderRef, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getActionFlag(self):
        '''操作标志'''
        return TThostFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TThostFtdcActionFlagType)] else list(TThostFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getActionDate(self):
        '''操作日期'''
        return str(self.ActionDate, 'GBK')

    def getActionTime(self):
        '''操作时间'''
        return str(self.ActionTime, 'GBK')

    def getTraderID(self):
        '''交易所交易员代码'''
        return str(self.TraderID, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getActionLocalID(self):
        '''操作本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户代码'''
        return str(self.ClientID, 'GBK')

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getOrderActionStatus(self):
        '''报单操作状态'''
        return TThostFtdcOrderActionStatusType(ord(self.OrderActionStatus)) if ord(self.OrderActionStatus) in [e.value for e in list(TThostFtdcOrderActionStatusType)] else list(TThostFtdcOrderActionStatusType)[0]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getStatusMsg(self):
        '''状态信息'''
        return str(self.StatusMsg, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'OrderActionRef'={self.getOrderActionRef()}, 'OrderRef'={self.getOrderRef()}, 'RequestID'={self.getRequestID()}, 'FrontID'={self.getFrontID()}, 'SessionID'={self.getSessionID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'ActionDate'={self.getActionDate()}, 'ActionTime'={self.getActionTime()}, 'TraderID'={self.getTraderID()}, 'InstallID'={self.getInstallID()}, 'OrderLocalID'={self.getOrderLocalID()}, 'ActionLocalID'={self.getActionLocalID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'OrderActionStatus'={self.getOrderActionStatus()}, 'UserID'={self.getUserID()}, 'StatusMsg'={self.getStatusMsg()}, 'reserve1'={self.getreserve1()}, 'BranchID'={self.getBranchID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'reserve2'={self.getreserve2()}, 'MacAddress'={self.getMacAddress()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'InstrumentID'={self.getInstrumentID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryExchangeSequenceField(Structure):
    """查询交易所状态"""
    _fields_ = [
        ("ExchangeID", c_char*9),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcExchangeSequenceField(Structure):
    """交易所状态"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("SequenceNo", c_int32),
        ("MarketStatus", c_char),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getSequenceNo(self):
        '''序号'''
        return self.SequenceNo

    def getMarketStatus(self):
        '''合约交易状态'''
        return TThostFtdcInstrumentStatusType(ord(self.MarketStatus)) if ord(self.MarketStatus) in [e.value for e in list(TThostFtdcInstrumentStatusType)] else list(TThostFtdcInstrumentStatusType)[0]

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'SequenceNo'={self.getSequenceNo()}, 'MarketStatus'={self.getMarketStatus()}"


class  CThostFtdcQryMaxOrderVolumeWithPriceField(Structure):
    """根据价格查询最大报单数量"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", c_int32),
        ("Price", c_double),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getOffsetFlag(self):
        '''开平标志'''
        return TThostFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TThostFtdcOffsetFlagType)] else list(TThostFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getMaxVolume(self):
        '''最大允许报单数量'''
        return self.MaxVolume

    def getPrice(self):
        '''报单价格'''
        return self.Price

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'Direction'={self.getDirection()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'MaxVolume'={self.getMaxVolume()}, 'Price'={self.getPrice()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryBrokerTradingParamsField(Structure):
    """查询经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("CurrencyID", c_char*4),
        ("AccountID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'CurrencyID'={self.getCurrencyID()}, 'AccountID'={self.getAccountID()}"


class  CThostFtdcBrokerTradingParamsField(Structure):
    """经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("MarginPriceType", c_char),
        ("Algorithm", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("CurrencyID", c_char*4),
        ("OptionRoyaltyPriceType", c_char),
        ("AccountID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getMarginPriceType(self):
        '''保证金价格类型'''
        return TThostFtdcMarginPriceTypeType(ord(self.MarginPriceType)) if ord(self.MarginPriceType) in [e.value for e in list(TThostFtdcMarginPriceTypeType)] else list(TThostFtdcMarginPriceTypeType)[0]

    def getAlgorithm(self):
        '''盈亏算法'''
        return TThostFtdcAlgorithmType(ord(self.Algorithm)) if ord(self.Algorithm) in [e.value for e in list(TThostFtdcAlgorithmType)] else list(TThostFtdcAlgorithmType)[0]

    def getAvailIncludeCloseProfit(self):
        '''可用是否包含平仓盈利'''
        return TThostFtdcIncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)) if ord(self.AvailIncludeCloseProfit) in [e.value for e in list(TThostFtdcIncludeCloseProfitType)] else list(TThostFtdcIncludeCloseProfitType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getOptionRoyaltyPriceType(self):
        '''期权权利金价格类型'''
        return TThostFtdcOptionRoyaltyPriceTypeType(ord(self.OptionRoyaltyPriceType)) if ord(self.OptionRoyaltyPriceType) in [e.value for e in list(TThostFtdcOptionRoyaltyPriceTypeType)] else list(TThostFtdcOptionRoyaltyPriceTypeType)[0]

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'MarginPriceType'={self.getMarginPriceType()}, 'Algorithm'={self.getAlgorithm()}, 'AvailIncludeCloseProfit'={self.getAvailIncludeCloseProfit()}, 'CurrencyID'={self.getCurrencyID()}, 'OptionRoyaltyPriceType'={self.getOptionRoyaltyPriceType()}, 'AccountID'={self.getAccountID()}"


class  CThostFtdcQryBrokerTradingAlgosField(Structure):
    """查询经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcBrokerTradingAlgosField(Structure):
    """经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("HandlePositionAlgoID", c_char),
        ("FindMarginRateAlgoID", c_char),
        ("HandleTradingAccountAlgoID", c_char),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHandlePositionAlgoID(self):
        '''持仓处理算法编号'''
        return TThostFtdcHandlePositionAlgoIDType(ord(self.HandlePositionAlgoID)) if ord(self.HandlePositionAlgoID) in [e.value for e in list(TThostFtdcHandlePositionAlgoIDType)] else list(TThostFtdcHandlePositionAlgoIDType)[0]

    def getFindMarginRateAlgoID(self):
        '''寻找保证金率算法编号'''
        return TThostFtdcFindMarginRateAlgoIDType(ord(self.FindMarginRateAlgoID)) if ord(self.FindMarginRateAlgoID) in [e.value for e in list(TThostFtdcFindMarginRateAlgoIDType)] else list(TThostFtdcFindMarginRateAlgoIDType)[0]

    def getHandleTradingAccountAlgoID(self):
        '''资金处理算法编号'''
        return TThostFtdcHandleTradingAccountAlgoIDType(ord(self.HandleTradingAccountAlgoID)) if ord(self.HandleTradingAccountAlgoID) in [e.value for e in list(TThostFtdcHandleTradingAccountAlgoIDType)] else list(TThostFtdcHandleTradingAccountAlgoIDType)[0]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'HandlePositionAlgoID'={self.getHandlePositionAlgoID()}, 'FindMarginRateAlgoID'={self.getFindMarginRateAlgoID()}, 'HandleTradingAccountAlgoID'={self.getHandleTradingAccountAlgoID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQueryBrokerDepositField(Structure):
    """查询经纪公司资金"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ExchangeID", c_char*9),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}"


class  CThostFtdcBrokerDepositField(Structure):
    """经纪公司资金"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("ParticipantID", c_char*11),
        ("ExchangeID", c_char*9),
        ("PreBalance", c_double),
        ("CurrMargin", c_double),
        ("CloseProfit", c_double),
        ("Balance", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("Available", c_double),
        ("Reserve", c_double),
        ("FrozenMargin", c_double),
    ]

    def getTradingDay(self):
        '''交易日期'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getPreBalance(self):
        '''上次结算准备金'''
        return self.PreBalance

    def getCurrMargin(self):
        '''当前保证金总额'''
        return self.CurrMargin

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getBalance(self):
        '''期货结算准备金'''
        return self.Balance

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getWithdraw(self):
        '''出金金额'''
        return self.Withdraw

    def getAvailable(self):
        '''可提资金'''
        return self.Available

    def getReserve(self):
        '''基本准备金'''
        return self.Reserve

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}, 'ExchangeID'={self.getExchangeID()}, 'PreBalance'={self.getPreBalance()}, 'CurrMargin'={self.getCurrMargin()}, 'CloseProfit'={self.getCloseProfit()}, 'Balance'={self.getBalance()}, 'Deposit'={self.getDeposit()}, 'Withdraw'={self.getWithdraw()}, 'Available'={self.getAvailable()}, 'Reserve'={self.getReserve()}, 'FrozenMargin'={self.getFrozenMargin()}"


class  CThostFtdcQryCFMMCBrokerKeyField(Structure):
    """查询保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", c_char*11),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}"


class  CThostFtdcCFMMCBrokerKeyField(Structure):
    """保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ParticipantID", c_char*11),
        ("CreateDate", c_char*9),
        ("CreateTime", c_char*9),
        ("KeyID", c_int32),
        ("CurrentKey", c_char*21),
        ("KeyKind", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''经纪公司统一编码'''
        return str(self.ParticipantID, 'GBK')

    def getCreateDate(self):
        '''密钥生成日期'''
        return str(self.CreateDate, 'GBK')

    def getCreateTime(self):
        '''密钥生成时间'''
        return str(self.CreateTime, 'GBK')

    def getKeyID(self):
        '''密钥编号'''
        return self.KeyID

    def getCurrentKey(self):
        '''动态密钥'''
        return str(self.CurrentKey, 'GBK')

    def getKeyKind(self):
        '''动态密钥类型'''
        return TThostFtdcCFMMCKeyKindType(ord(self.KeyKind)) if ord(self.KeyKind) in [e.value for e in list(TThostFtdcCFMMCKeyKindType)] else list(TThostFtdcCFMMCKeyKindType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}, 'CreateDate'={self.getCreateDate()}, 'CreateTime'={self.getCreateTime()}, 'KeyID'={self.getKeyID()}, 'CurrentKey'={self.getCurrentKey()}, 'KeyKind'={self.getKeyKind()}"


class  CThostFtdcCFMMCTradingAccountKeyField(Structure):
    """保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ParticipantID", c_char*11),
        ("AccountID", c_char*13),
        ("KeyID", c_int32),
        ("CurrentKey", c_char*21),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''经纪公司统一编码'''
        return str(self.ParticipantID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getKeyID(self):
        '''密钥编号'''
        return self.KeyID

    def getCurrentKey(self):
        '''动态密钥'''
        return str(self.CurrentKey, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}, 'AccountID'={self.getAccountID()}, 'KeyID'={self.getKeyID()}, 'CurrentKey'={self.getCurrentKey()}"


class  CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
    """请求查询保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcBrokerUserOTPParamField(Structure):
    """用户动态令牌参数"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("OTPVendorsID", c_char*2),
        ("SerialNumber", c_char*17),
        ("AuthKey", c_char*41),
        ("LastDrift", c_int32),
        ("LastSuccess", c_int32),
        ("OTPType", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOTPVendorsID(self):
        '''动态令牌提供商'''
        return str(self.OTPVendorsID, 'GBK')

    def getSerialNumber(self):
        '''动态令牌序列号'''
        return str(self.SerialNumber, 'GBK')

    def getAuthKey(self):
        '''令牌密钥'''
        return str(self.AuthKey, 'GBK')

    def getLastDrift(self):
        '''漂移值'''
        return self.LastDrift

    def getLastSuccess(self):
        '''成功值'''
        return self.LastSuccess

    def getOTPType(self):
        '''动态令牌类型'''
        return TThostFtdcOTPTypeType(ord(self.OTPType)) if ord(self.OTPType) in [e.value for e in list(TThostFtdcOTPTypeType)] else list(TThostFtdcOTPTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'OTPVendorsID'={self.getOTPVendorsID()}, 'SerialNumber'={self.getSerialNumber()}, 'AuthKey'={self.getAuthKey()}, 'LastDrift'={self.getLastDrift()}, 'LastSuccess'={self.getLastSuccess()}, 'OTPType'={self.getOTPType()}"


class  CThostFtdcManualSyncBrokerUserOTPField(Structure):
    """手工同步用户动态令牌"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("OTPType", c_char),
        ("FirstOTP", c_char*41),
        ("SecondOTP", c_char*41),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getOTPType(self):
        '''动态令牌类型'''
        return TThostFtdcOTPTypeType(ord(self.OTPType)) if ord(self.OTPType) in [e.value for e in list(TThostFtdcOTPTypeType)] else list(TThostFtdcOTPTypeType)[0]

    def getFirstOTP(self):
        '''第一个动态密码'''
        return str(self.FirstOTP, 'GBK')

    def getSecondOTP(self):
        '''第二个动态密码'''
        return str(self.SecondOTP, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'OTPType'={self.getOTPType()}, 'FirstOTP'={self.getFirstOTP()}, 'SecondOTP'={self.getSecondOTP()}"


class  CThostFtdcCommRateModelField(Structure):
    """投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("CommModelID", c_char*13),
        ("CommModelName", c_char*161),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')

    def getCommModelName(self):
        '''模板名称'''
        return str(self.CommModelName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'CommModelID'={self.getCommModelID()}, 'CommModelName'={self.getCommModelName()}"


class  CThostFtdcQryCommRateModelField(Structure):
    """请求查询投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("CommModelID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'CommModelID'={self.getCommModelID()}"


class  CThostFtdcMarginModelField(Structure):
    """投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("MarginModelID", c_char*13),
        ("MarginModelName", c_char*161),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')

    def getMarginModelName(self):
        '''模板名称'''
        return str(self.MarginModelName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'MarginModelID'={self.getMarginModelID()}, 'MarginModelName'={self.getMarginModelName()}"


class  CThostFtdcQryMarginModelField(Structure):
    """请求查询投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("MarginModelID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'MarginModelID'={self.getMarginModelID()}"


class  CThostFtdcEWarrantOffsetField(Structure):
    """仓单折抵信息"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int32),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getTradingDay(self):
        '''交易日期'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TThostFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TThostFtdcDirectionType)] else list(TThostFtdcDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'Direction'={self.getDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Volume'={self.getVolume()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryEWarrantOffsetField(Structure):
    """查询仓单折抵信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("ExchangeID", c_char*9),
        ("reserve1", c_char*31),
        ("InvestUnitID", c_char*17),
        ("InstrumentID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'reserve1'={self.getreserve1()}, 'InvestUnitID'={self.getInvestUnitID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryInvestorProductGroupMarginField(Structure):
    """查询投资者品种/跨品种保证金"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("reserve1", c_char*31),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("ProductGroupID", c_char*81),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getProductGroupID(self):
        '''品种/跨品种标示'''
        return str(self.ProductGroupID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'reserve1'={self.getreserve1()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'ProductGroupID'={self.getProductGroupID()}"


class  CThostFtdcInvestorProductGroupMarginField(Structure):
    """投资者品种/跨品种保证金"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("TradingDay", c_char*9),
        ("SettlementID", c_int32),
        ("FrozenMargin", c_double),
        ("LongFrozenMargin", c_double),
        ("ShortFrozenMargin", c_double),
        ("UseMargin", c_double),
        ("LongUseMargin", c_double),
        ("ShortUseMargin", c_double),
        ("ExchMargin", c_double),
        ("LongExchMargin", c_double),
        ("ShortExchMargin", c_double),
        ("CloseProfit", c_double),
        ("FrozenCommission", c_double),
        ("Commission", c_double),
        ("FrozenCash", c_double),
        ("CashIn", c_double),
        ("PositionProfit", c_double),
        ("OffsetAmount", c_double),
        ("LongOffsetAmount", c_double),
        ("ShortOffsetAmount", c_double),
        ("ExchOffsetAmount", c_double),
        ("LongExchOffsetAmount", c_double),
        ("ShortExchOffsetAmount", c_double),
        ("HedgeFlag", c_char),
        ("ExchangeID", c_char*9),
        ("InvestUnitID", c_char*17),
        ("ProductGroupID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getLongFrozenMargin(self):
        '''多头冻结的保证金'''
        return self.LongFrozenMargin

    def getShortFrozenMargin(self):
        '''空头冻结的保证金'''
        return self.ShortFrozenMargin

    def getUseMargin(self):
        '''占用的保证金'''
        return self.UseMargin

    def getLongUseMargin(self):
        '''多头保证金'''
        return self.LongUseMargin

    def getShortUseMargin(self):
        '''空头保证金'''
        return self.ShortUseMargin

    def getExchMargin(self):
        '''交易所保证金'''
        return self.ExchMargin

    def getLongExchMargin(self):
        '''交易所多头保证金'''
        return self.LongExchMargin

    def getShortExchMargin(self):
        '''交易所空头保证金'''
        return self.ShortExchMargin

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getFrozenCommission(self):
        '''冻结的手续费'''
        return self.FrozenCommission

    def getCommission(self):
        '''手续费'''
        return self.Commission

    def getFrozenCash(self):
        '''冻结的资金'''
        return self.FrozenCash

    def getCashIn(self):
        '''资金差额'''
        return self.CashIn

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getOffsetAmount(self):
        '''折抵总金额'''
        return self.OffsetAmount

    def getLongOffsetAmount(self):
        '''多头折抵总金额'''
        return self.LongOffsetAmount

    def getShortOffsetAmount(self):
        '''空头折抵总金额'''
        return self.ShortOffsetAmount

    def getExchOffsetAmount(self):
        '''交易所折抵总金额'''
        return self.ExchOffsetAmount

    def getLongExchOffsetAmount(self):
        '''交易所多头折抵总金额'''
        return self.LongExchOffsetAmount

    def getShortExchOffsetAmount(self):
        '''交易所空头折抵总金额'''
        return self.ShortExchOffsetAmount

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TThostFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TThostFtdcHedgeFlagType)] else list(TThostFtdcHedgeFlagType)[0]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def getProductGroupID(self):
        '''品种/跨品种标示'''
        return str(self.ProductGroupID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'TradingDay'={self.getTradingDay()}, 'SettlementID'={self.getSettlementID()}, 'FrozenMargin'={self.getFrozenMargin()}, 'LongFrozenMargin'={self.getLongFrozenMargin()}, 'ShortFrozenMargin'={self.getShortFrozenMargin()}, 'UseMargin'={self.getUseMargin()}, 'LongUseMargin'={self.getLongUseMargin()}, 'ShortUseMargin'={self.getShortUseMargin()}, 'ExchMargin'={self.getExchMargin()}, 'LongExchMargin'={self.getLongExchMargin()}, 'ShortExchMargin'={self.getShortExchMargin()}, 'CloseProfit'={self.getCloseProfit()}, 'FrozenCommission'={self.getFrozenCommission()}, 'Commission'={self.getCommission()}, 'FrozenCash'={self.getFrozenCash()}, 'CashIn'={self.getCashIn()}, 'PositionProfit'={self.getPositionProfit()}, 'OffsetAmount'={self.getOffsetAmount()}, 'LongOffsetAmount'={self.getLongOffsetAmount()}, 'ShortOffsetAmount'={self.getShortOffsetAmount()}, 'ExchOffsetAmount'={self.getExchOffsetAmount()}, 'LongExchOffsetAmount'={self.getLongExchOffsetAmount()}, 'ShortExchOffsetAmount'={self.getShortExchOffsetAmount()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ExchangeID'={self.getExchangeID()}, 'InvestUnitID'={self.getInvestUnitID()}, 'ProductGroupID'={self.getProductGroupID()}"


class  CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
    """查询监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("InvestUnitID", c_char*17),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'InvestUnitID'={self.getInvestUnitID()}"


class  CThostFtdcCFMMCTradingAccountTokenField(Structure):
    """监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("ParticipantID", c_char*11),
        ("AccountID", c_char*13),
        ("KeyID", c_int32),
        ("Token", c_char*21),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''经纪公司统一编码'''
        return str(self.ParticipantID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getKeyID(self):
        '''密钥编号'''
        return self.KeyID

    def getToken(self):
        '''动态令牌'''
        return str(self.Token, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}, 'AccountID'={self.getAccountID()}, 'KeyID'={self.getKeyID()}, 'Token'={self.getToken()}"


class  CThostFtdcQryProductGroupField(Structure):
    """查询产品组"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("ProductID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}"


class  CThostFtdcProductGroupField(Structure):
    """投资者品种/跨品种保证金产品组"""
    _fields_ = [
        ("reserve1", c_char*31),
        ("ExchangeID", c_char*9),
        ("reserve2", c_char*31),
        ("ProductID", c_char*81),
        ("ProductGroupID", c_char*81),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def getProductGroupID(self):
        '''产品组代码'''
        return str(self.ProductGroupID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'ExchangeID'={self.getExchangeID()}, 'reserve2'={self.getreserve2()}, 'ProductID'={self.getProductID()}, 'ProductGroupID'={self.getProductGroupID()}"


class  CThostFtdcBulletinField(Structure):
    """交易所公告"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("TradingDay", c_char*9),
        ("BulletinID", c_int32),
        ("SequenceNo", c_int32),
        ("NewsType", c_char*3),
        ("NewsUrgency", c_char),
        ("SendTime", c_char*9),
        ("Abstract", c_char*81),
        ("ComeFrom", c_char*21),
        ("Content", c_char*501),
        ("URLLink", c_char*201),
        ("MarketID", c_char*31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBulletinID(self):
        '''公告编号'''
        return self.BulletinID

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def getNewsType(self):
        '''公告类型'''
        return str(self.NewsType, 'GBK')

    def getNewsUrgency(self):
        '''紧急程度'''
        return TThostFtdcNewsUrgencyType(ord(self.NewsUrgency)) if ord(self.NewsUrgency) in [e.value for e in list(TThostFtdcNewsUrgencyType)] else list(TThostFtdcNewsUrgencyType)[0]

    def getSendTime(self):
        '''发送时间'''
        return str(self.SendTime, 'GBK')

    def getAbstract(self):
        '''消息摘要'''
        return str(self.Abstract, 'GBK')

    def getComeFrom(self):
        '''消息来源'''
        return str(self.ComeFrom, 'GBK')

    def getContent(self):
        '''消息正文'''
        return str(self.Content, 'GBK')

    def getURLLink(self):
        '''WEB地址'''
        return str(self.URLLink, 'GBK')

    def getMarketID(self):
        '''市场代码'''
        return str(self.MarketID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TradingDay'={self.getTradingDay()}, 'BulletinID'={self.getBulletinID()}, 'SequenceNo'={self.getSequenceNo()}, 'NewsType'={self.getNewsType()}, 'NewsUrgency'={self.getNewsUrgency()}, 'SendTime'={self.getSendTime()}, 'Abstract'={self.getAbstract()}, 'ComeFrom'={self.getComeFrom()}, 'Content'={self.getContent()}, 'URLLink'={self.getURLLink()}, 'MarketID'={self.getMarketID()}"


class  CThostFtdcQryBulletinField(Structure):
    """查询交易所公告"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("BulletinID", c_int32),
        ("SequenceNo", c_int32),
        ("NewsType", c_char*3),
        ("NewsUrgency", c_char),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBulletinID(self):
        '''公告编号'''
        return self.BulletinID

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def getNewsType(self):
        '''公告类型'''
        return str(self.NewsType, 'GBK')

    def getNewsUrgency(self):
        '''紧急程度'''
        return TThostFtdcNewsUrgencyType(ord(self.NewsUrgency)) if ord(self.NewsUrgency) in [e.value for e in list(TThostFtdcNewsUrgencyType)] else list(TThostFtdcNewsUrgencyType)[0]

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BulletinID'={self.getBulletinID()}, 'SequenceNo'={self.getSequenceNo()}, 'NewsType'={self.getNewsType()}, 'NewsUrgency'={self.getNewsUrgency()}"


class  CThostFtdcMulticastInstrumentField(Structure):
    """MulticastInstrument"""
    _fields_ = [
        ("TopicID", c_int32),
        ("reserve1", c_char*31),
        ("InstrumentNo", c_int32),
        ("CodePrice", c_double),
        ("VolumeMultiple", c_int32),
        ("PriceTick", c_double),
        ("InstrumentID", c_char*81),
    ]

    def getTopicID(self):
        '''主题号'''
        return self.TopicID

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentNo(self):
        '''合约编号'''
        return self.InstrumentNo

    def getCodePrice(self):
        '''基准价'''
        return self.CodePrice

    def getVolumeMultiple(self):
        '''合约数量乘数'''
        return self.VolumeMultiple

    def getPriceTick(self):
        '''最小变动价位'''
        return self.PriceTick

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TopicID'={self.getTopicID()}, 'reserve1'={self.getreserve1()}, 'InstrumentNo'={self.getInstrumentNo()}, 'CodePrice'={self.getCodePrice()}, 'VolumeMultiple'={self.getVolumeMultiple()}, 'PriceTick'={self.getPriceTick()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcQryMulticastInstrumentField(Structure):
    """QryMulticastInstrument"""
    _fields_ = [
        ("TopicID", c_int32),
        ("reserve1", c_char*31),
        ("InstrumentID", c_char*81),
    ]

    def getTopicID(self):
        '''主题号'''
        return self.TopicID

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TopicID'={self.getTopicID()}, 'reserve1'={self.getreserve1()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcAppIDAuthAssignField(Structure):
    """App客户端权限分配"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AppID", c_char*33),
        ("DRIdentityID", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AppID'={self.getAppID()}, 'DRIdentityID'={self.getDRIdentityID()}"


class  CThostFtdcReqOpenAccountField(Structure):
    """转帐开户请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("TID", c_int32),
        ("UserID", c_char*16),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getCashExchangeCode(self):
        '''汇钞标志'''
        return TThostFtdcCashExchangeCodeType(ord(self.CashExchangeCode)) if ord(self.CashExchangeCode) in [e.value for e in list(TThostFtdcCashExchangeCodeType)] else list(TThostFtdcCashExchangeCodeType)[0]

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'CashExchangeCode'={self.getCashExchangeCode()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'TID'={self.getTID()}, 'UserID'={self.getUserID()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcReqCancelAccountField(Structure):
    """转帐销户请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("TID", c_int32),
        ("UserID", c_char*16),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getCashExchangeCode(self):
        '''汇钞标志'''
        return TThostFtdcCashExchangeCodeType(ord(self.CashExchangeCode)) if ord(self.CashExchangeCode) in [e.value for e in list(TThostFtdcCashExchangeCodeType)] else list(TThostFtdcCashExchangeCodeType)[0]

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'CashExchangeCode'={self.getCashExchangeCode()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'TID'={self.getTID()}, 'UserID'={self.getUserID()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcReqChangeAccountField(Structure):
    """变更银行账户请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("NewBankAccount", c_char*41),
        ("NewBankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("BankAccType", c_char),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("BrokerIDByBank", c_char*33),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", c_int32),
        ("Digest", c_char*36),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getNewBankAccount(self):
        '''新银行帐号'''
        return str(self.NewBankAccount, 'GBK')

    def getNewBankPassWord(self):
        '''新银行密码'''
        return str(self.NewBankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'NewBankAccount'={self.getNewBankAccount()}, 'NewBankPassWord'={self.getNewBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'BankAccType'={self.getBankAccType()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'TID'={self.getTID()}, 'Digest'={self.getDigest()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcReqTransferField(Structure):
    """转账请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("FutureSerial", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char*129),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("TransferStatus", c_char),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getFutureFetchAmount(self):
        '''期货可取金额'''
        return self.FutureFetchAmount

    def getFeePayFlag(self):
        '''费用支付标志'''
        return TThostFtdcFeePayFlagType(ord(self.FeePayFlag)) if ord(self.FeePayFlag) in [e.value for e in list(TThostFtdcFeePayFlagType)] else list(TThostFtdcFeePayFlagType)[0]

    def getCustFee(self):
        '''应收客户费用'''
        return self.CustFee

    def getBrokerFee(self):
        '''应收期货公司费用'''
        return self.BrokerFee

    def getMessage(self):
        '''发送方给接收方的消息'''
        return str(self.Message, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getTransferStatus(self):
        '''转账交易状态'''
        return TThostFtdcTransferStatusType(ord(self.TransferStatus)) if ord(self.TransferStatus) in [e.value for e in list(TThostFtdcTransferStatusType)] else list(TThostFtdcTransferStatusType)[0]

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'FutureSerial'={self.getFutureSerial()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'FutureFetchAmount'={self.getFutureFetchAmount()}, 'FeePayFlag'={self.getFeePayFlag()}, 'CustFee'={self.getCustFee()}, 'BrokerFee'={self.getBrokerFee()}, 'Message'={self.getMessage()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'TransferStatus'={self.getTransferStatus()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcRspTransferField(Structure):
    """银行发起银行资金转期货响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("FutureSerial", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char*129),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("TransferStatus", c_char),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getFutureFetchAmount(self):
        '''期货可取金额'''
        return self.FutureFetchAmount

    def getFeePayFlag(self):
        '''费用支付标志'''
        return TThostFtdcFeePayFlagType(ord(self.FeePayFlag)) if ord(self.FeePayFlag) in [e.value for e in list(TThostFtdcFeePayFlagType)] else list(TThostFtdcFeePayFlagType)[0]

    def getCustFee(self):
        '''应收客户费用'''
        return self.CustFee

    def getBrokerFee(self):
        '''应收期货公司费用'''
        return self.BrokerFee

    def getMessage(self):
        '''发送方给接收方的消息'''
        return str(self.Message, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getTransferStatus(self):
        '''转账交易状态'''
        return TThostFtdcTransferStatusType(ord(self.TransferStatus)) if ord(self.TransferStatus) in [e.value for e in list(TThostFtdcTransferStatusType)] else list(TThostFtdcTransferStatusType)[0]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'FutureSerial'={self.getFutureSerial()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'FutureFetchAmount'={self.getFutureFetchAmount()}, 'FeePayFlag'={self.getFeePayFlag()}, 'CustFee'={self.getCustFee()}, 'BrokerFee'={self.getBrokerFee()}, 'Message'={self.getMessage()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'TransferStatus'={self.getTransferStatus()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcReqRepealField(Structure):
    """冲正请求"""
    _fields_ = [
        ("RepealTimeInterval", c_int32),
        ("RepealedTimes", c_int32),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", c_int32),
        ("BankRepealSerial", c_char*13),
        ("FutureRepealSerial", c_int32),
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("FutureSerial", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char*129),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("TransferStatus", c_char),
        ("LongCustomerName", c_char*161),
    ]

    def getRepealTimeInterval(self):
        '''冲正时间间隔'''
        return self.RepealTimeInterval

    def getRepealedTimes(self):
        '''已经冲正次数'''
        return self.RepealedTimes

    def getBankRepealFlag(self):
        '''银行冲正标志'''
        return TThostFtdcBankRepealFlagType(ord(self.BankRepealFlag)) if ord(self.BankRepealFlag) in [e.value for e in list(TThostFtdcBankRepealFlagType)] else list(TThostFtdcBankRepealFlagType)[0]

    def getBrokerRepealFlag(self):
        '''期商冲正标志'''
        return TThostFtdcBrokerRepealFlagType(ord(self.BrokerRepealFlag)) if ord(self.BrokerRepealFlag) in [e.value for e in list(TThostFtdcBrokerRepealFlagType)] else list(TThostFtdcBrokerRepealFlagType)[0]

    def getPlateRepealSerial(self):
        '''被冲正平台流水号'''
        return self.PlateRepealSerial

    def getBankRepealSerial(self):
        '''被冲正银行流水号'''
        return str(self.BankRepealSerial, 'GBK')

    def getFutureRepealSerial(self):
        '''被冲正期货流水号'''
        return self.FutureRepealSerial

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getFutureFetchAmount(self):
        '''期货可取金额'''
        return self.FutureFetchAmount

    def getFeePayFlag(self):
        '''费用支付标志'''
        return TThostFtdcFeePayFlagType(ord(self.FeePayFlag)) if ord(self.FeePayFlag) in [e.value for e in list(TThostFtdcFeePayFlagType)] else list(TThostFtdcFeePayFlagType)[0]

    def getCustFee(self):
        '''应收客户费用'''
        return self.CustFee

    def getBrokerFee(self):
        '''应收期货公司费用'''
        return self.BrokerFee

    def getMessage(self):
        '''发送方给接收方的消息'''
        return str(self.Message, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getTransferStatus(self):
        '''转账交易状态'''
        return TThostFtdcTransferStatusType(ord(self.TransferStatus)) if ord(self.TransferStatus) in [e.value for e in list(TThostFtdcTransferStatusType)] else list(TThostFtdcTransferStatusType)[0]

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'RepealTimeInterval'={self.getRepealTimeInterval()}, 'RepealedTimes'={self.getRepealedTimes()}, 'BankRepealFlag'={self.getBankRepealFlag()}, 'BrokerRepealFlag'={self.getBrokerRepealFlag()}, 'PlateRepealSerial'={self.getPlateRepealSerial()}, 'BankRepealSerial'={self.getBankRepealSerial()}, 'FutureRepealSerial'={self.getFutureRepealSerial()}, 'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'FutureSerial'={self.getFutureSerial()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'FutureFetchAmount'={self.getFutureFetchAmount()}, 'FeePayFlag'={self.getFeePayFlag()}, 'CustFee'={self.getCustFee()}, 'BrokerFee'={self.getBrokerFee()}, 'Message'={self.getMessage()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'TransferStatus'={self.getTransferStatus()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcRspRepealField(Structure):
    """冲正响应"""
    _fields_ = [
        ("RepealTimeInterval", c_int32),
        ("RepealedTimes", c_int32),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", c_int32),
        ("BankRepealSerial", c_char*13),
        ("FutureRepealSerial", c_int32),
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("FutureSerial", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("FutureFetchAmount", c_double),
        ("FeePayFlag", c_char),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("Message", c_char*129),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("TransferStatus", c_char),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getRepealTimeInterval(self):
        '''冲正时间间隔'''
        return self.RepealTimeInterval

    def getRepealedTimes(self):
        '''已经冲正次数'''
        return self.RepealedTimes

    def getBankRepealFlag(self):
        '''银行冲正标志'''
        return TThostFtdcBankRepealFlagType(ord(self.BankRepealFlag)) if ord(self.BankRepealFlag) in [e.value for e in list(TThostFtdcBankRepealFlagType)] else list(TThostFtdcBankRepealFlagType)[0]

    def getBrokerRepealFlag(self):
        '''期商冲正标志'''
        return TThostFtdcBrokerRepealFlagType(ord(self.BrokerRepealFlag)) if ord(self.BrokerRepealFlag) in [e.value for e in list(TThostFtdcBrokerRepealFlagType)] else list(TThostFtdcBrokerRepealFlagType)[0]

    def getPlateRepealSerial(self):
        '''被冲正平台流水号'''
        return self.PlateRepealSerial

    def getBankRepealSerial(self):
        '''被冲正银行流水号'''
        return str(self.BankRepealSerial, 'GBK')

    def getFutureRepealSerial(self):
        '''被冲正期货流水号'''
        return self.FutureRepealSerial

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getFutureFetchAmount(self):
        '''期货可取金额'''
        return self.FutureFetchAmount

    def getFeePayFlag(self):
        '''费用支付标志'''
        return TThostFtdcFeePayFlagType(ord(self.FeePayFlag)) if ord(self.FeePayFlag) in [e.value for e in list(TThostFtdcFeePayFlagType)] else list(TThostFtdcFeePayFlagType)[0]

    def getCustFee(self):
        '''应收客户费用'''
        return self.CustFee

    def getBrokerFee(self):
        '''应收期货公司费用'''
        return self.BrokerFee

    def getMessage(self):
        '''发送方给接收方的消息'''
        return str(self.Message, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getTransferStatus(self):
        '''转账交易状态'''
        return TThostFtdcTransferStatusType(ord(self.TransferStatus)) if ord(self.TransferStatus) in [e.value for e in list(TThostFtdcTransferStatusType)] else list(TThostFtdcTransferStatusType)[0]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'RepealTimeInterval'={self.getRepealTimeInterval()}, 'RepealedTimes'={self.getRepealedTimes()}, 'BankRepealFlag'={self.getBankRepealFlag()}, 'BrokerRepealFlag'={self.getBrokerRepealFlag()}, 'PlateRepealSerial'={self.getPlateRepealSerial()}, 'BankRepealSerial'={self.getBankRepealSerial()}, 'FutureRepealSerial'={self.getFutureRepealSerial()}, 'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'FutureSerial'={self.getFutureSerial()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'FutureFetchAmount'={self.getFutureFetchAmount()}, 'FeePayFlag'={self.getFeePayFlag()}, 'CustFee'={self.getCustFee()}, 'BrokerFee'={self.getBrokerFee()}, 'Message'={self.getMessage()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'TransferStatus'={self.getTransferStatus()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcReqQueryAccountField(Structure):
    """查询账户信息请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("FutureSerial", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'FutureSerial'={self.getFutureSerial()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcRspQueryAccountField(Structure):
    """查询账户信息响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("FutureSerial", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("BankUseAmount", c_double),
        ("BankFetchAmount", c_double),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getBankUseAmount(self):
        '''银行可用金额'''
        return self.BankUseAmount

    def getBankFetchAmount(self):
        '''银行可取金额'''
        return self.BankFetchAmount

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'FutureSerial'={self.getFutureSerial()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'BankUseAmount'={self.getBankUseAmount()}, 'BankFetchAmount'={self.getBankFetchAmount()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcFutureSignIOField(Structure):
    """期商签到签退"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}"


class  CThostFtdcRspFutureSignInField(Structure):
    """期商签到响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("PinKey", c_char*129),
        ("MacKey", c_char*129),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getPinKey(self):
        '''PIN密钥'''
        return str(self.PinKey, 'GBK')

    def getMacKey(self):
        '''MAC密钥'''
        return str(self.MacKey, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'PinKey'={self.getPinKey()}, 'MacKey'={self.getMacKey()}"


class  CThostFtdcReqFutureSignOutField(Structure):
    """期商签退请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}"


class  CThostFtdcRspFutureSignOutField(Structure):
    """期商签退响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcReqQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("Reference", c_int32),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", c_char*36),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("Digest", c_char*36),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getReference(self):
        '''流水号'''
        return self.Reference

    def getRefrenceIssureType(self):
        '''本流水号发布者的机构类型'''
        return TThostFtdcInstitutionTypeType(ord(self.RefrenceIssureType)) if ord(self.RefrenceIssureType) in [e.value for e in list(TThostFtdcInstitutionTypeType)] else list(TThostFtdcInstitutionTypeType)[0]

    def getRefrenceIssure(self):
        '''本流水号发布者机构编码'''
        return str(self.RefrenceIssure, 'GBK')

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'Reference'={self.getReference()}, 'RefrenceIssureType'={self.getRefrenceIssureType()}, 'RefrenceIssure'={self.getRefrenceIssure()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'Digest'={self.getDigest()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcRspQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("Reference", c_int32),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", c_char*36),
        ("OriginReturnCode", c_char*7),
        ("OriginDescrInfoForReturnCode", c_char*129),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("Digest", c_char*36),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getReference(self):
        '''流水号'''
        return self.Reference

    def getRefrenceIssureType(self):
        '''本流水号发布者的机构类型'''
        return TThostFtdcInstitutionTypeType(ord(self.RefrenceIssureType)) if ord(self.RefrenceIssureType) in [e.value for e in list(TThostFtdcInstitutionTypeType)] else list(TThostFtdcInstitutionTypeType)[0]

    def getRefrenceIssure(self):
        '''本流水号发布者机构编码'''
        return str(self.RefrenceIssure, 'GBK')

    def getOriginReturnCode(self):
        '''原始返回代码'''
        return str(self.OriginReturnCode, 'GBK')

    def getOriginDescrInfoForReturnCode(self):
        '''原始返回码描述'''
        return str(self.OriginDescrInfoForReturnCode, 'GBK')

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''转帐金额'''
        return self.TradeAmount

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'Reference'={self.getReference()}, 'RefrenceIssureType'={self.getRefrenceIssureType()}, 'RefrenceIssure'={self.getRefrenceIssure()}, 'OriginReturnCode'={self.getOriginReturnCode()}, 'OriginDescrInfoForReturnCode'={self.getOriginDescrInfoForReturnCode()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'Digest'={self.getDigest()}"


class  CThostFtdcReqDayEndFileReadyField(Structure):
    """日终文件就绪请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("FileBusinessCode", c_char),
        ("Digest", c_char*36),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getFileBusinessCode(self):
        '''文件业务功能'''
        return TThostFtdcFileBusinessCodeType(ord(self.FileBusinessCode)) if ord(self.FileBusinessCode) in [e.value for e in list(TThostFtdcFileBusinessCodeType)] else list(TThostFtdcFileBusinessCodeType)[0]

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'FileBusinessCode'={self.getFileBusinessCode()}, 'Digest'={self.getDigest()}"


class  CThostFtdcReturnResultField(Structure):
    """返回结果"""
    _fields_ = [
        ("ReturnCode", c_char*7),
        ("DescrInfoForReturnCode", c_char*129),
    ]

    def getReturnCode(self):
        '''返回代码'''
        return str(self.ReturnCode, 'GBK')

    def getDescrInfoForReturnCode(self):
        '''返回码描述'''
        return str(self.DescrInfoForReturnCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ReturnCode'={self.getReturnCode()}, 'DescrInfoForReturnCode'={self.getDescrInfoForReturnCode()}"


class  CThostFtdcVerifyFuturePasswordField(Structure):
    """验证期货资金密码"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("InstallID", c_int32),
        ("TID", c_int32),
        ("CurrencyID", c_char*4),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'InstallID'={self.getInstallID()}, 'TID'={self.getTID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcVerifyCustInfoField(Structure):
    """验证客户信息"""
    _fields_ = [
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("LongCustomerName", c_char*161),
    ]

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("CurrencyID", c_char*4),
        ("LongCustomerName", c_char*161),
    ]

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'CurrencyID'={self.getCurrencyID()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcDepositResultInformField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("DepositSeqNo", c_char*15),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("Deposit", c_double),
        ("RequestID", c_int32),
        ("ReturnCode", c_char*7),
        ("DescrInfoForReturnCode", c_char*129),
    ]

    def getDepositSeqNo(self):
        '''出入金流水号，该流水号为银期报盘返回的流水号'''
        return str(self.DepositSeqNo, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getReturnCode(self):
        '''返回代码'''
        return str(self.ReturnCode, 'GBK')

    def getDescrInfoForReturnCode(self):
        '''返回码描述'''
        return str(self.DescrInfoForReturnCode, 'GBK')

    def __str__(self): # 可以直接print
        return f"'DepositSeqNo'={self.getDepositSeqNo()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'Deposit'={self.getDeposit()}, 'RequestID'={self.getRequestID()}, 'ReturnCode'={self.getReturnCode()}, 'DescrInfoForReturnCode'={self.getDescrInfoForReturnCode()}"


class  CThostFtdcReqSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Message", c_char*129),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getMessage(self):
        '''交易核心给银期报盘的消息'''
        return str(self.Message, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Message'={self.getMessage()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}"


class  CThostFtdcRspSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步响应"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Message", c_char*129),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getMessage(self):
        '''交易核心给银期报盘的消息'''
        return str(self.Message, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Message'={self.getMessage()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcNotifyQueryAccountField(Structure):
    """查询账户信息通知"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustType", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("FutureSerial", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("BankUseAmount", c_double),
        ("BankFetchAmount", c_double),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getBankUseAmount(self):
        '''银行可用金额'''
        return self.BankUseAmount

    def getBankFetchAmount(self):
        '''银行可取金额'''
        return self.BankFetchAmount

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustType'={self.getCustType()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'FutureSerial'={self.getFutureSerial()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'BankUseAmount'={self.getBankUseAmount()}, 'BankFetchAmount'={self.getBankFetchAmount()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcTransferSerialField(Structure):
    """银期转账交易流水表"""
    _fields_ = [
        ("PlateSerial", c_int32),
        ("TradeDate", c_char*9),
        ("TradingDay", c_char*9),
        ("TradeTime", c_char*9),
        ("TradeCode", c_char*7),
        ("SessionID", c_int32),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BankAccType", c_char),
        ("BankAccount", c_char*41),
        ("BankSerial", c_char*13),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("FutureAccType", c_char),
        ("AccountID", c_char*13),
        ("InvestorID", c_char*13),
        ("FutureSerial", c_int32),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CurrencyID", c_char*4),
        ("TradeAmount", c_double),
        ("CustFee", c_double),
        ("BrokerFee", c_double),
        ("AvailabilityFlag", c_char),
        ("OperatorCode", c_char*17),
        ("BankNewAccount", c_char*41),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getPlateSerial(self):
        '''平台流水号'''
        return self.PlateSerial

    def getTradeDate(self):
        '''交易发起方日期'''
        return str(self.TradeDate, 'GBK')

    def getTradingDay(self):
        '''交易日期'''
        return str(self.TradingDay, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getTradeCode(self):
        '''交易代码'''
        return str(self.TradeCode, 'GBK')

    def getSessionID(self):
        '''会话编号'''
        return self.SessionID

    def getBankID(self):
        '''银行编码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构编码'''
        return str(self.BankBranchID, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getBrokerID(self):
        '''期货公司编码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getFutureAccType(self):
        '''期货公司帐号类型'''
        return TThostFtdcFutureAccTypeType(ord(self.FutureAccType)) if ord(self.FutureAccType) in [e.value for e in list(TThostFtdcFutureAccTypeType)] else list(TThostFtdcFutureAccTypeType)[0]

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getFutureSerial(self):
        '''期货公司流水号'''
        return self.FutureSerial

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getTradeAmount(self):
        '''交易金额'''
        return self.TradeAmount

    def getCustFee(self):
        '''应收客户费用'''
        return self.CustFee

    def getBrokerFee(self):
        '''应收期货公司费用'''
        return self.BrokerFee

    def getAvailabilityFlag(self):
        '''有效标志'''
        return TThostFtdcAvailabilityFlagType(ord(self.AvailabilityFlag)) if ord(self.AvailabilityFlag) in [e.value for e in list(TThostFtdcAvailabilityFlagType)] else list(TThostFtdcAvailabilityFlagType)[0]

    def getOperatorCode(self):
        '''操作员'''
        return str(self.OperatorCode, 'GBK')

    def getBankNewAccount(self):
        '''新银行帐号'''
        return str(self.BankNewAccount, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'PlateSerial'={self.getPlateSerial()}, 'TradeDate'={self.getTradeDate()}, 'TradingDay'={self.getTradingDay()}, 'TradeTime'={self.getTradeTime()}, 'TradeCode'={self.getTradeCode()}, 'SessionID'={self.getSessionID()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BankAccType'={self.getBankAccType()}, 'BankAccount'={self.getBankAccount()}, 'BankSerial'={self.getBankSerial()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'FutureAccType'={self.getFutureAccType()}, 'AccountID'={self.getAccountID()}, 'InvestorID'={self.getInvestorID()}, 'FutureSerial'={self.getFutureSerial()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CurrencyID'={self.getCurrencyID()}, 'TradeAmount'={self.getTradeAmount()}, 'CustFee'={self.getCustFee()}, 'BrokerFee'={self.getBrokerFee()}, 'AvailabilityFlag'={self.getAvailabilityFlag()}, 'OperatorCode'={self.getOperatorCode()}, 'BankNewAccount'={self.getBankNewAccount()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcQryTransferSerialField(Structure):
    """请求查询转帐流水"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("BankID", c_char*4),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getBankID(self):
        '''银行编码'''
        return str(self.BankID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'BankID'={self.getBankID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcNotifyFutureSignInField(Structure):
    """期商签到通知"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("PinKey", c_char*129),
        ("MacKey", c_char*129),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getPinKey(self):
        '''PIN密钥'''
        return str(self.PinKey, 'GBK')

    def getMacKey(self):
        '''MAC密钥'''
        return str(self.MacKey, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'PinKey'={self.getPinKey()}, 'MacKey'={self.getMacKey()}"


class  CThostFtdcNotifyFutureSignOutField(Structure):
    """期商签退通知"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Digest", c_char*36),
        ("CurrencyID", c_char*4),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Digest'={self.getDigest()}, 'CurrencyID'={self.getCurrencyID()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcNotifySyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("InstallID", c_int32),
        ("UserID", c_char*16),
        ("Message", c_char*129),
        ("DeviceID", c_char*3),
        ("BrokerIDByBank", c_char*33),
        ("OperNo", c_char*17),
        ("RequestID", c_int32),
        ("TID", c_int32),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getMessage(self):
        '''交易核心给银期报盘的消息'''
        return str(self.Message, 'GBK')

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getRequestID(self):
        '''请求编号'''
        return self.RequestID

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'InstallID'={self.getInstallID()}, 'UserID'={self.getUserID()}, 'Message'={self.getMessage()}, 'DeviceID'={self.getDeviceID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'OperNo'={self.getOperNo()}, 'RequestID'={self.getRequestID()}, 'TID'={self.getTID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcQryAccountregisterField(Structure):
    """请求查询银期签约关系"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getBankID(self):
        '''银行编码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构编码'''
        return str(self.BankBranchID, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcAccountregisterField(Structure):
    """客户开销户信息表"""
    _fields_ = [
        ("TradeDay", c_char*9),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BankAccount", c_char*41),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("AccountID", c_char*13),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("CustomerName", c_char*51),
        ("CurrencyID", c_char*4),
        ("OpenOrDestroy", c_char),
        ("RegDate", c_char*9),
        ("OutDate", c_char*9),
        ("TID", c_int32),
        ("CustType", c_char),
        ("BankAccType", c_char),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeDay(self):
        '''交易日期'''
        return str(self.TradeDay, 'GBK')

    def getBankID(self):
        '''银行编码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构编码'''
        return str(self.BankBranchID, 'GBK')

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBrokerID(self):
        '''期货公司编码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期货公司分支机构编码'''
        return str(self.BrokerBranchID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getOpenOrDestroy(self):
        '''开销户类别'''
        return TThostFtdcOpenOrDestroyType(ord(self.OpenOrDestroy)) if ord(self.OpenOrDestroy) in [e.value for e in list(TThostFtdcOpenOrDestroyType)] else list(TThostFtdcOpenOrDestroyType)[0]

    def getRegDate(self):
        '''签约日期'''
        return str(self.RegDate, 'GBK')

    def getOutDate(self):
        '''解约日期'''
        return str(self.OutDate, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeDay'={self.getTradeDay()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BankAccount'={self.getBankAccount()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'AccountID'={self.getAccountID()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'CustomerName'={self.getCustomerName()}, 'CurrencyID'={self.getCurrencyID()}, 'OpenOrDestroy'={self.getOpenOrDestroy()}, 'RegDate'={self.getRegDate()}, 'OutDate'={self.getOutDate()}, 'TID'={self.getTID()}, 'CustType'={self.getCustType()}, 'BankAccType'={self.getBankAccType()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcOpenAccountField(Structure):
    """银期开户信息"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("TID", c_int32),
        ("UserID", c_char*16),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getCashExchangeCode(self):
        '''汇钞标志'''
        return TThostFtdcCashExchangeCodeType(ord(self.CashExchangeCode)) if ord(self.CashExchangeCode) in [e.value for e in list(TThostFtdcCashExchangeCodeType)] else list(TThostFtdcCashExchangeCodeType)[0]

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'CashExchangeCode'={self.getCashExchangeCode()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'TID'={self.getTID()}, 'UserID'={self.getUserID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcCancelAccountField(Structure):
    """银期销户信息"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("CashExchangeCode", c_char),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("DeviceID", c_char*3),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("BankSecuAcc", c_char*41),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", c_char*17),
        ("TID", c_int32),
        ("UserID", c_char*16),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getCashExchangeCode(self):
        '''汇钞标志'''
        return TThostFtdcCashExchangeCodeType(ord(self.CashExchangeCode)) if ord(self.CashExchangeCode) in [e.value for e in list(TThostFtdcCashExchangeCodeType)] else list(TThostFtdcCashExchangeCodeType)[0]

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')

    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankSecuAccType)) if ord(self.BankSecuAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getOperNo(self):
        '''交易柜员'''
        return str(self.OperNo, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getUserID(self):
        '''用户标识'''
        return str(self.UserID, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'CashExchangeCode'={self.getCashExchangeCode()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'DeviceID'={self.getDeviceID()}, 'BankSecuAccType'={self.getBankSecuAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankSecuAcc'={self.getBankSecuAcc()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'OperNo'={self.getOperNo()}, 'TID'={self.getTID()}, 'UserID'={self.getUserID()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcChangeAccountField(Structure):
    """银期变更银行账号信息"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*51),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("NewBankAccount", c_char*41),
        ("NewBankPassWord", c_char*41),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("BankAccType", c_char),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("BrokerIDByBank", c_char*33),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", c_int32),
        ("Digest", c_char*36),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
        ("LongCustomerName", c_char*161),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getNewBankAccount(self):
        '''新银行帐号'''
        return str(self.NewBankAccount, 'GBK')

    def getNewBankPassWord(self):
        '''新银行密码'''
        return str(self.NewBankPassWord, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getBankPwdFlag(self):
        '''银行密码标志'''
        return TThostFtdcPwdFlagType(ord(self.BankPwdFlag)) if ord(self.BankPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return TThostFtdcPwdFlagType(ord(self.SecuPwdFlag)) if ord(self.SecuPwdFlag) in [e.value for e in list(TThostFtdcPwdFlagType)] else list(TThostFtdcPwdFlagType)[0]

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'NewBankAccount'={self.getNewBankAccount()}, 'NewBankPassWord'={self.getNewBankPassWord()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'BankAccType'={self.getBankAccType()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'BankPwdFlag'={self.getBankPwdFlag()}, 'SecuPwdFlag'={self.getSecuPwdFlag()}, 'TID'={self.getTID()}, 'Digest'={self.getDigest()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}, 'LongCustomerName'={self.getLongCustomerName()}"


class  CThostFtdcSecAgentACIDMapField(Structure):
    """二级代理操作员银期权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
        ("BrokerSecAgentID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getAccountID(self):
        '''资金账户'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种'''
        return str(self.CurrencyID, 'GBK')

    def getBrokerSecAgentID(self):
        '''境外中介机构资金帐号'''
        return str(self.BrokerSecAgentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}, 'BrokerSecAgentID'={self.getBrokerSecAgentID()}"


class  CThostFtdcQrySecAgentACIDMapField(Structure):
    """二级代理操作员银期权限查询"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("AccountID", c_char*13),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getAccountID(self):
        '''资金账户'''
        return str(self.AccountID, 'GBK')

    def getCurrencyID(self):
        '''币种'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'AccountID'={self.getAccountID()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcUserRightsAssignField(Structure):
    """灾备中心交易权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("DRIdentityID", c_int32),
    ]

    def getBrokerID(self):
        '''应用单元代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'DRIdentityID'={self.getDRIdentityID()}"


class  CThostFtdcBrokerUserRightAssignField(Structure):
    """经济公司是否有在本标示的交易权限"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("DRIdentityID", c_int32),
        ("Tradeable", c_int32),
    ]

    def getBrokerID(self):
        '''应用单元代码'''
        return str(self.BrokerID, 'GBK')

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID

    def getTradeable(self):
        '''能否交易'''
        return self.Tradeable

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'DRIdentityID'={self.getDRIdentityID()}, 'Tradeable'={self.getTradeable()}"


class  CThostFtdcDRTransferField(Structure):
    """灾备交易转换报文"""
    _fields_ = [
        ("OrigDRIdentityID", c_int32),
        ("DestDRIdentityID", c_int32),
        ("OrigBrokerID", c_char*11),
        ("DestBrokerID", c_char*11),
    ]

    def getOrigDRIdentityID(self):
        '''原交易中心代码'''
        return self.OrigDRIdentityID

    def getDestDRIdentityID(self):
        '''目标交易中心代码'''
        return self.DestDRIdentityID

    def getOrigBrokerID(self):
        '''原应用单元代码'''
        return str(self.OrigBrokerID, 'GBK')

    def getDestBrokerID(self):
        '''目标易用单元代码'''
        return str(self.DestBrokerID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'OrigDRIdentityID'={self.getOrigDRIdentityID()}, 'DestDRIdentityID'={self.getDestDRIdentityID()}, 'OrigBrokerID'={self.getOrigBrokerID()}, 'DestBrokerID'={self.getDestBrokerID()}"


class  CThostFtdcFensUserInfoField(Structure):
    """Fens用户信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("LoginMode", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getLoginMode(self):
        '''登录模式'''
        return TThostFtdcLoginModeType(ord(self.LoginMode)) if ord(self.LoginMode) in [e.value for e in list(TThostFtdcLoginModeType)] else list(TThostFtdcLoginModeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'LoginMode'={self.getLoginMode()}"


class  CThostFtdcCurrTransferIdentityField(Structure):
    """当前银期所属交易中心"""
    _fields_ = [
        ("IdentityID", c_int32),
    ]

    def getIdentityID(self):
        '''交易中心代码'''
        return self.IdentityID

    def __str__(self): # 可以直接print
        return f"'IdentityID'={self.getIdentityID()}"


class  CThostFtdcLoginForbiddenUserField(Structure):
    """禁止登录用户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryLoginForbiddenUserField(Structure):
    """查询禁止登录用户"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcTradingAccountReserveField(Structure):
    """资金账户基本准备金"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("Reserve", c_double),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getReserve(self):
        '''基本准备金'''
        return self.Reserve

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'Reserve'={self.getReserve()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcQryLoginForbiddenIPField(Structure):
    """查询禁止登录IP"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryIPListField(Structure):
    """查询IP列表"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryUserRightsAssignField(Structure):
    """查询用户下单权限分配表"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getBrokerID(self):
        '''应用单元代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcReserveOpenAccountConfirmField(Structure):
    """银期预约开户确认请求"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*161),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("TID", c_int32),
        ("AccountID", c_char*13),
        ("Password", c_char*41),
        ("BankReserveOpenSeq", c_char*13),
        ("BookDate", c_char*9),
        ("BookPsw", c_char*41),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getPassword(self):
        '''期货密码'''
        return str(self.Password, 'GBK')

    def getBankReserveOpenSeq(self):
        '''预约开户银行流水号'''
        return str(self.BankReserveOpenSeq, 'GBK')

    def getBookDate(self):
        '''预约开户日期'''
        return str(self.BookDate, 'GBK')

    def getBookPsw(self):
        '''预约开户验证密码'''
        return str(self.BookPsw, 'GBK')

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'TID'={self.getTID()}, 'AccountID'={self.getAccountID()}, 'Password'={self.getPassword()}, 'BankReserveOpenSeq'={self.getBankReserveOpenSeq()}, 'BookDate'={self.getBookDate()}, 'BookPsw'={self.getBookPsw()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcReserveOpenAccountField(Structure):
    """银期预约开户"""
    _fields_ = [
        ("TradeCode", c_char*7),
        ("BankID", c_char*4),
        ("BankBranchID", c_char*5),
        ("BrokerID", c_char*11),
        ("BrokerBranchID", c_char*31),
        ("TradeDate", c_char*9),
        ("TradeTime", c_char*9),
        ("BankSerial", c_char*13),
        ("TradingDay", c_char*9),
        ("PlateSerial", c_int32),
        ("LastFragment", c_char),
        ("SessionID", c_int32),
        ("CustomerName", c_char*161),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", c_char*51),
        ("Gender", c_char),
        ("CountryCode", c_char*21),
        ("CustType", c_char),
        ("Address", c_char*101),
        ("ZipCode", c_char*7),
        ("Telephone", c_char*41),
        ("MobilePhone", c_char*21),
        ("Fax", c_char*41),
        ("EMail", c_char*41),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", c_char*41),
        ("BankPassWord", c_char*41),
        ("InstallID", c_int32),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", c_char*4),
        ("Digest", c_char*36),
        ("BankAccType", c_char),
        ("BrokerIDByBank", c_char*33),
        ("TID", c_int32),
        ("ReserveOpenAccStas", c_char),
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char*81),
    ]

    def getTradeCode(self):
        '''业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankBranchID(self):
        '''银行分支机构代码'''
        return str(self.BankBranchID, 'GBK')

    def getBrokerID(self):
        '''期商代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerBranchID(self):
        '''期商分支机构代码'''
        return str(self.BrokerBranchID, 'GBK')

    def getTradeDate(self):
        '''交易日期'''
        return str(self.TradeDate, 'GBK')

    def getTradeTime(self):
        '''交易时间'''
        return str(self.TradeTime, 'GBK')

    def getBankSerial(self):
        '''银行流水号'''
        return str(self.BankSerial, 'GBK')

    def getTradingDay(self):
        '''交易系统日期 '''
        return str(self.TradingDay, 'GBK')

    def getPlateSerial(self):
        '''银期平台消息流水号'''
        return self.PlateSerial

    def getLastFragment(self):
        '''最后分片标志'''
        return TThostFtdcLastFragmentType(ord(self.LastFragment)) if ord(self.LastFragment) in [e.value for e in list(TThostFtdcLastFragmentType)] else list(TThostFtdcLastFragmentType)[0]

    def getSessionID(self):
        '''会话号'''
        return self.SessionID

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')

    def getIdCardType(self):
        '''证件类型'''
        return TThostFtdcIdCardTypeType(ord(self.IdCardType)) if ord(self.IdCardType) in [e.value for e in list(TThostFtdcIdCardTypeType)] else list(TThostFtdcIdCardTypeType)[0]

    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')

    def getGender(self):
        '''性别'''
        return TThostFtdcGenderType(ord(self.Gender)) if ord(self.Gender) in [e.value for e in list(TThostFtdcGenderType)] else list(TThostFtdcGenderType)[0]

    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')

    def getCustType(self):
        '''客户类型'''
        return TThostFtdcCustTypeType(ord(self.CustType)) if ord(self.CustType) in [e.value for e in list(TThostFtdcCustTypeType)] else list(TThostFtdcCustTypeType)[0]

    def getAddress(self):
        '''地址'''
        return str(self.Address, 'GBK')

    def getZipCode(self):
        '''邮编'''
        return str(self.ZipCode, 'GBK')

    def getTelephone(self):
        '''电话号码'''
        return str(self.Telephone, 'GBK')

    def getMobilePhone(self):
        '''手机'''
        return str(self.MobilePhone, 'GBK')

    def getFax(self):
        '''传真'''
        return str(self.Fax, 'GBK')

    def getEMail(self):
        '''电子邮件'''
        return str(self.EMail, 'GBK')

    def getMoneyAccountStatus(self):
        '''资金账户状态'''
        return TThostFtdcMoneyAccountStatusType(ord(self.MoneyAccountStatus)) if ord(self.MoneyAccountStatus) in [e.value for e in list(TThostFtdcMoneyAccountStatusType)] else list(TThostFtdcMoneyAccountStatusType)[0]

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getBankPassWord(self):
        '''银行密码'''
        return str(self.BankPassWord, 'GBK')

    def getInstallID(self):
        '''安装编号'''
        return self.InstallID

    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return TThostFtdcYesNoIndicatorType(ord(self.VerifyCertNoFlag)) if ord(self.VerifyCertNoFlag) in [e.value for e in list(TThostFtdcYesNoIndicatorType)] else list(TThostFtdcYesNoIndicatorType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')

    def getBankAccType(self):
        '''银行帐号类型'''
        return TThostFtdcBankAccTypeType(ord(self.BankAccType)) if ord(self.BankAccType) in [e.value for e in list(TThostFtdcBankAccTypeType)] else list(TThostFtdcBankAccTypeType)[0]

    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')

    def getTID(self):
        '''交易ID'''
        return self.TID

    def getReserveOpenAccStas(self):
        '''预约开户状态'''
        return TThostFtdcReserveOpenAccStasType(ord(self.ReserveOpenAccStas)) if ord(self.ReserveOpenAccStas) in [e.value for e in list(TThostFtdcReserveOpenAccStasType)] else list(TThostFtdcReserveOpenAccStasType)[0]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradeCode'={self.getTradeCode()}, 'BankID'={self.getBankID()}, 'BankBranchID'={self.getBankBranchID()}, 'BrokerID'={self.getBrokerID()}, 'BrokerBranchID'={self.getBrokerBranchID()}, 'TradeDate'={self.getTradeDate()}, 'TradeTime'={self.getTradeTime()}, 'BankSerial'={self.getBankSerial()}, 'TradingDay'={self.getTradingDay()}, 'PlateSerial'={self.getPlateSerial()}, 'LastFragment'={self.getLastFragment()}, 'SessionID'={self.getSessionID()}, 'CustomerName'={self.getCustomerName()}, 'IdCardType'={self.getIdCardType()}, 'IdentifiedCardNo'={self.getIdentifiedCardNo()}, 'Gender'={self.getGender()}, 'CountryCode'={self.getCountryCode()}, 'CustType'={self.getCustType()}, 'Address'={self.getAddress()}, 'ZipCode'={self.getZipCode()}, 'Telephone'={self.getTelephone()}, 'MobilePhone'={self.getMobilePhone()}, 'Fax'={self.getFax()}, 'EMail'={self.getEMail()}, 'MoneyAccountStatus'={self.getMoneyAccountStatus()}, 'BankAccount'={self.getBankAccount()}, 'BankPassWord'={self.getBankPassWord()}, 'InstallID'={self.getInstallID()}, 'VerifyCertNoFlag'={self.getVerifyCertNoFlag()}, 'CurrencyID'={self.getCurrencyID()}, 'Digest'={self.getDigest()}, 'BankAccType'={self.getBankAccType()}, 'BrokerIDByBank'={self.getBrokerIDByBank()}, 'TID'={self.getTID()}, 'ReserveOpenAccStas'={self.getReserveOpenAccStas()}, 'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class  CThostFtdcAccountPropertyField(Structure):
    """银行账户属性"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AccountID", c_char*13),
        ("BankID", c_char*4),
        ("BankAccount", c_char*41),
        ("OpenName", c_char*101),
        ("OpenBank", c_char*101),
        ("IsActive", c_int32),
        ("AccountSourceType", c_char),
        ("OpenDate", c_char*9),
        ("CancelDate", c_char*9),
        ("OperatorID", c_char*65),
        ("OperateDate", c_char*9),
        ("OperateTime", c_char*9),
        ("CurrencyID", c_char*4),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')

    def getBankID(self):
        '''银行统一标识类型'''
        return str(self.BankID, 'GBK')

    def getBankAccount(self):
        '''银行账户'''
        return str(self.BankAccount, 'GBK')

    def getOpenName(self):
        '''银行账户的开户人名称'''
        return str(self.OpenName, 'GBK')

    def getOpenBank(self):
        '''银行账户的开户行'''
        return str(self.OpenBank, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive

    def getAccountSourceType(self):
        '''账户来源'''
        return TThostFtdcAccountSourceTypeType(ord(self.AccountSourceType)) if ord(self.AccountSourceType) in [e.value for e in list(TThostFtdcAccountSourceTypeType)] else list(TThostFtdcAccountSourceTypeType)[0]

    def getOpenDate(self):
        '''开户日期'''
        return str(self.OpenDate, 'GBK')

    def getCancelDate(self):
        '''注销日期'''
        return str(self.CancelDate, 'GBK')

    def getOperatorID(self):
        '''录入员代码'''
        return str(self.OperatorID, 'GBK')

    def getOperateDate(self):
        '''录入日期'''
        return str(self.OperateDate, 'GBK')

    def getOperateTime(self):
        '''录入时间'''
        return str(self.OperateTime, 'GBK')

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'BankID'={self.getBankID()}, 'BankAccount'={self.getBankAccount()}, 'OpenName'={self.getOpenName()}, 'OpenBank'={self.getOpenBank()}, 'IsActive'={self.getIsActive()}, 'AccountSourceType'={self.getAccountSourceType()}, 'OpenDate'={self.getOpenDate()}, 'CancelDate'={self.getCancelDate()}, 'OperatorID'={self.getOperatorID()}, 'OperateDate'={self.getOperateDate()}, 'OperateTime'={self.getOperateTime()}, 'CurrencyID'={self.getCurrencyID()}"


class  CThostFtdcQryCurrDRIdentityField(Structure):
    """查询当前交易中心"""
    _fields_ = [
        ("DRIdentityID", c_int32),
    ]

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID

    def __str__(self): # 可以直接print
        return f"'DRIdentityID'={self.getDRIdentityID()}"


class  CThostFtdcCurrDRIdentityField(Structure):
    """当前交易中心"""
    _fields_ = [
        ("DRIdentityID", c_int32),
    ]

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID

    def __str__(self): # 可以直接print
        return f"'DRIdentityID'={self.getDRIdentityID()}"


class  CThostFtdcQrySecAgentCheckModeField(Structure):
    """查询二级代理商资金校验模式"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcQrySecAgentTradeInfoField(Structure):
    """查询二级代理商信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("BrokerSecAgentID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getBrokerSecAgentID(self):
        '''境外中介机构资金帐号'''
        return str(self.BrokerSecAgentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'BrokerSecAgentID'={self.getBrokerSecAgentID()}"


class  CThostFtdcReqUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcRspUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法回复"""
    _fields_ = [
        ("UsableAuthMethod", c_int32),
    ]

    def getUsableAuthMethod(self):
        '''当前可以用的认证模式'''
        return self.UsableAuthMethod

    def __str__(self): # 可以直接print
        return f"'UsableAuthMethod'={self.getUsableAuthMethod()}"


class  CThostFtdcReqGenUserCaptchaField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcRspGenUserCaptchaField(Structure):
    """生成的图片验证码信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("CaptchaInfoLen", c_int32),
        ("CaptchaInfo", c_char*2561),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getCaptchaInfoLen(self):
        '''图片信息长度'''
        return self.CaptchaInfoLen

    def getCaptchaInfo(self):
        '''图片信息'''
        return str(self.CaptchaInfo, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'CaptchaInfoLen'={self.getCaptchaInfoLen()}, 'CaptchaInfo'={self.getCaptchaInfo()}"


class  CThostFtdcReqGenUserTextField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class  CThostFtdcRspGenUserTextField(Structure):
    """短信验证码生成的回复"""
    _fields_ = [
        ("UserTextSeq", c_int32),
    ]

    def getUserTextSeq(self):
        '''短信验证码序号'''
        return self.UserTextSeq

    def __str__(self): # 可以直接print
        return f"'UserTextSeq'={self.getUserTextSeq()}"


class  CThostFtdcReqUserLoginWithCaptchaField(Structure):
    """用户发出带图形验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("Password", c_char*41),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("MacAddress", c_char*21),
        ("reserve1", c_char*16),
        ("LoginRemark", c_char*36),
        ("Captcha", c_char*41),
        ("ClientIPPort", c_int32),
        ("ClientIPAddress", c_char*33),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getCaptcha(self):
        '''图形验证码的文字内容'''
        return str(self.Captcha, 'GBK')

    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort

    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'MacAddress'={self.getMacAddress()}, 'reserve1'={self.getreserve1()}, 'LoginRemark'={self.getLoginRemark()}, 'Captcha'={self.getCaptcha()}, 'ClientIPPort'={self.getClientIPPort()}, 'ClientIPAddress'={self.getClientIPAddress()}"


class  CThostFtdcReqUserLoginWithTextField(Structure):
    """用户发出带短信验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("Password", c_char*41),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("MacAddress", c_char*21),
        ("reserve1", c_char*16),
        ("LoginRemark", c_char*36),
        ("Text", c_char*41),
        ("ClientIPPort", c_int32),
        ("ClientIPAddress", c_char*33),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getText(self):
        '''短信验证码文字内容'''
        return str(self.Text, 'GBK')

    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort

    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'MacAddress'={self.getMacAddress()}, 'reserve1'={self.getreserve1()}, 'LoginRemark'={self.getLoginRemark()}, 'Text'={self.getText()}, 'ClientIPPort'={self.getClientIPPort()}, 'ClientIPAddress'={self.getClientIPAddress()}"


class  CThostFtdcReqUserLoginWithOTPField(Structure):
    """用户发出带动态验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", c_char*9),
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("Password", c_char*41),
        ("UserProductInfo", c_char*11),
        ("InterfaceProductInfo", c_char*11),
        ("ProtocolInfo", c_char*11),
        ("MacAddress", c_char*21),
        ("reserve1", c_char*16),
        ("LoginRemark", c_char*36),
        ("OTPPassword", c_char*41),
        ("ClientIPPort", c_int32),
        ("ClientIPAddress", c_char*33),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')

    def getOTPPassword(self):
        '''OTP密码'''
        return str(self.OTPPassword, 'GBK')

    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort

    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'MacAddress'={self.getMacAddress()}, 'reserve1'={self.getreserve1()}, 'LoginRemark'={self.getLoginRemark()}, 'OTPPassword'={self.getOTPPassword()}, 'ClientIPPort'={self.getClientIPPort()}, 'ClientIPAddress'={self.getClientIPAddress()}"


class  CThostFtdcReqApiHandshakeField(Structure):
    """api握手请求"""
    _fields_ = [
        ("CryptoKeyVersion", c_char*31),
    ]

    def getCryptoKeyVersion(self):
        '''api与front通信密钥版本号'''
        return str(self.CryptoKeyVersion, 'GBK')

    def __str__(self): # 可以直接print
        return f"'CryptoKeyVersion'={self.getCryptoKeyVersion()}"


class  CThostFtdcRspApiHandshakeField(Structure):
    """front发给api的握手回复"""
    _fields_ = [
        ("FrontHandshakeDataLen", c_int32),
        ("FrontHandshakeData", c_char*301),
        ("IsApiAuthEnabled", c_int32),
    ]

    def getFrontHandshakeDataLen(self):
        '''握手回复数据长度'''
        return self.FrontHandshakeDataLen

    def getFrontHandshakeData(self):
        '''握手回复数据'''
        return str(self.FrontHandshakeData, 'GBK')

    def getIsApiAuthEnabled(self):
        '''API认证是否开启'''
        return self.IsApiAuthEnabled

    def __str__(self): # 可以直接print
        return f"'FrontHandshakeDataLen'={self.getFrontHandshakeDataLen()}, 'FrontHandshakeData'={self.getFrontHandshakeData()}, 'IsApiAuthEnabled'={self.getIsApiAuthEnabled()}"


class  CThostFtdcReqVerifyApiKeyField(Structure):
    """api给front的验证key的请求"""
    _fields_ = [
        ("ApiHandshakeDataLen", c_int32),
        ("ApiHandshakeData", c_char*301),
    ]

    def getApiHandshakeDataLen(self):
        '''握手回复数据长度'''
        return self.ApiHandshakeDataLen

    def getApiHandshakeData(self):
        '''握手回复数据'''
        return str(self.ApiHandshakeData, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ApiHandshakeDataLen'={self.getApiHandshakeDataLen()}, 'ApiHandshakeData'={self.getApiHandshakeData()}"


class  CThostFtdcDepartmentUserField(Structure):
    """操作员组织架构关系"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("InvestorRange", c_char),
        ("InvestorID", c_char*13),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorRange(self):
        '''投资者范围'''
        return TThostFtdcDepartmentRangeType(ord(self.InvestorRange)) if ord(self.InvestorRange) in [e.value for e in list(TThostFtdcDepartmentRangeType)] else list(TThostFtdcDepartmentRangeType)[0]

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorRange'={self.getInvestorRange()}, 'InvestorID'={self.getInvestorID()}"


class  CThostFtdcQueryFreqField(Structure):
    """查询频率，每秒查询比数"""
    _fields_ = [
        ("QueryFreq", c_int32),
    ]

    def getQueryFreq(self):
        '''查询频率'''
        return self.QueryFreq

    def __str__(self): # 可以直接print
        return f"'QueryFreq'={self.getQueryFreq()}"


class  CThostFtdcAuthForbiddenIPField(Structure):
    """禁止认证IP"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryAuthForbiddenIPField(Structure):
    """查询禁止认证IP"""
    _fields_ = [
        ("reserve1", c_char*16),
        ("IPAddress", c_char*33),
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'reserve1'={self.getreserve1()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcSyncDelaySwapFrozenField(Structure):
    """换汇可提冻结"""
    _fields_ = [
        ("DelaySwapSeqNo", c_char*15),
        ("BrokerID", c_char*11),
        ("InvestorID", c_char*13),
        ("FromCurrencyID", c_char*4),
        ("FromRemainSwap", c_double),
        ("IsManualSwap", c_int32),
    ]

    def getDelaySwapSeqNo(self):
        '''换汇流水号'''
        return str(self.DelaySwapSeqNo, 'GBK')

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')

    def getFromCurrencyID(self):
        '''源币种'''
        return str(self.FromCurrencyID, 'GBK')

    def getFromRemainSwap(self):
        '''源剩余换汇额度(可提冻结)'''
        return self.FromRemainSwap

    def getIsManualSwap(self):
        '''是否手工换汇'''
        return self.IsManualSwap

    def __str__(self): # 可以直接print
        return f"'DelaySwapSeqNo'={self.getDelaySwapSeqNo()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'FromCurrencyID'={self.getFromCurrencyID()}, 'FromRemainSwap'={self.getFromRemainSwap()}, 'IsManualSwap'={self.getIsManualSwap()}"


class  CThostFtdcUserSystemInfoField(Structure):
    """用户系统信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("UserID", c_char*16),
        ("ClientSystemInfoLen", c_int32),
        ("ClientSystemInfo", c_char*273),
        ("reserve1", c_char*16),
        ("ClientIPPort", c_int32),
        ("ClientLoginTime", c_char*9),
        ("ClientAppID", c_char*33),
        ("ClientPublicIP", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getClientSystemInfoLen(self):
        '''用户端系统内部信息长度'''
        return self.ClientSystemInfoLen

    def getClientSystemInfo(self):
        '''用户端系统内部信息'''
        return str(self.ClientSystemInfo, 'GBK')

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')

    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort

    def getClientLoginTime(self):
        '''登录成功时间'''
        return str(self.ClientLoginTime, 'GBK')

    def getClientAppID(self):
        '''App代码'''
        return str(self.ClientAppID, 'GBK')

    def getClientPublicIP(self):
        '''用户公网IP'''
        return str(self.ClientPublicIP, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'ClientSystemInfoLen'={self.getClientSystemInfoLen()}, 'ClientSystemInfo'={self.getClientSystemInfo()}, 'reserve1'={self.getreserve1()}, 'ClientIPPort'={self.getClientIPPort()}, 'ClientLoginTime'={self.getClientLoginTime()}, 'ClientAppID'={self.getClientAppID()}, 'ClientPublicIP'={self.getClientPublicIP()}"


class  CThostFtdcAuthUserIDField(Structure):
    """终端用户绑定信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AppID", c_char*33),
        ("UserID", c_char*16),
        ("AuthType", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getAuthType(self):
        '''校验类型'''
        return TThostFtdcAuthTypeType(ord(self.AuthType)) if ord(self.AuthType) in [e.value for e in list(TThostFtdcAuthTypeType)] else list(TThostFtdcAuthTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AppID'={self.getAppID()}, 'UserID'={self.getUserID()}, 'AuthType'={self.getAuthType()}"


class  CThostFtdcAuthIPField(Structure):
    """用户IP绑定信息"""
    _fields_ = [
        ("BrokerID", c_char*11),
        ("AppID", c_char*33),
        ("IPAddress", c_char*33),
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')

    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')

    def getIPAddress(self):
        '''用户代码'''
        return str(self.IPAddress, 'GBK')

    def __str__(self): # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AppID'={self.getAppID()}, 'IPAddress'={self.getIPAddress()}"


class  CThostFtdcQryClassifiedInstrumentField(Structure):
    """查询分类合约"""
    _fields_ = [
        ("InstrumentID", c_char*81),
        ("ExchangeID", c_char*9),
        ("ExchangeInstID", c_char*81),
        ("ProductID", c_char*81),
        ("TradingType", c_char),
        ("ClassType", c_char),
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def getTradingType(self):
        '''合约交易状态'''
        return TThostFtdcTradingTypeType(ord(self.TradingType)) if ord(self.TradingType) in [e.value for e in list(TThostFtdcTradingTypeType)] else list(TThostFtdcTradingTypeType)[0]

    def getClassType(self):
        '''合约分类类型'''
        return TThostFtdcClassTypeType(ord(self.ClassType)) if ord(self.ClassType) in [e.value for e in list(TThostFtdcClassTypeType)] else list(TThostFtdcClassTypeType)[0]

    def __str__(self): # 可以直接print
        return f"'InstrumentID'={self.getInstrumentID()}, 'ExchangeID'={self.getExchangeID()}, 'ExchangeInstID'={self.getExchangeInstID()}, 'ProductID'={self.getProductID()}, 'TradingType'={self.getTradingType()}, 'ClassType'={self.getClassType()}"


class  CThostFtdcQryCombPromotionParamField(Structure):
    """查询组合优惠比例"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class  CThostFtdcCombPromotionParamField(Structure):
    """组合优惠比例"""
    _fields_ = [
        ("ExchangeID", c_char*9),
        ("InstrumentID", c_char*81),
        ("CombHedgeFlag", c_char*5),
        ("Xparameter", c_double),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getCombHedgeFlag(self):
        '''投机套保标志'''
        return str(self.CombHedgeFlag, 'GBK')

    def getXparameter(self):
        '''期权组合保证金比例'''
        return self.Xparameter

    def __str__(self): # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}, 'CombHedgeFlag'={self.getCombHedgeFlag()}, 'Xparameter'={self.getXparameter()}"

