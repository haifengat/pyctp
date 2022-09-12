#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import *
from .datatype import *


class  CThostFtdcDisseminationField(Structure):
    """信息分发"""
    _fields_ = [
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries
    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo
    
class  CThostFtdcReqUserLoginField(Structure):
    """用户登录请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcRspUserLoginField(Structure):
    """用户登录应答"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("SystemName", TThostFtdcSystemNameType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("INETime", TThostFtdcTimeType),
        ("SysVersion", TThostFtdcSysVersionType),
        ("GFEXTime", TThostFtdcTimeType),
        
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
    def getSysVersion(self):
        '''后台版本信息'''
        return str(self.SysVersion, 'GBK')
    def getGFEXTime(self):
        '''广期所时间'''
        return str(self.GFEXTime, 'GBK')
    
class  CThostFtdcUserLogoutField(Structure):
    """用户登出请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcForceUserLogoutField(Structure):
    """强制交易员退出"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcReqAuthenticateField(Structure):
    """客户端认证请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AuthCode", TThostFtdcAuthCodeType),
        ("AppID", TThostFtdcAppIDType),
        
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
    
class  CThostFtdcRspAuthenticateField(Structure):
    """客户端认证响应"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AppID", TThostFtdcAppIDType),
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
        return self.AppType
    
class  CThostFtdcAuthenticationInfoField(Structure):
    """客户端认证信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AuthInfo", TThostFtdcAuthInfoType),
        ("IsResult", TThostFtdcBoolType),
        ("AppID", TThostFtdcAppIDType),
        ("AppType", c_char),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
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
        return self.AppType
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')
    
class  CThostFtdcRspUserLogin2Field(Structure):
    """用户登录应答2"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("SystemName", TThostFtdcSystemNameType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("INETime", TThostFtdcTimeType),
        ("RandomString", TThostFtdcRandomStringType),
        
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
    
class  CThostFtdcTransferHeaderField(Structure):
    """银期转帐报文头"""
    _fields_ = [
        ("Version", TThostFtdcVersionType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeSerial", TThostFtdcTradeSerialType),
        ("FutureID", TThostFtdcFutureIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("OperNo", TThostFtdcOperNoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("RecordNum", TThostFtdcRecordNumType),
        ("SessionID", TThostFtdcSessionIDType),
        ("RequestID", TThostFtdcRequestIDType),
        
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
    
class  CThostFtdcTransferBankToFutureReqField(Structure):
    """银行资金转期货请求，TradeCode=202001"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')
    def getFuturePwdFlag(self):
        '''密码标志'''
        return self.FuturePwdFlag
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
    
class  CThostFtdcTransferBankToFutureRspField(Structure):
    """银行资金转期货请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
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
    
class  CThostFtdcTransferFutureToBankReqField(Structure):
    """期货资金转银行请求，TradeCode=202002"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')
    def getFuturePwdFlag(self):
        '''密码标志'''
        return self.FuturePwdFlag
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
    
class  CThostFtdcTransferFutureToBankRspField(Structure):
    """期货资金转银行请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
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
    
class  CThostFtdcTransferQryBankReqField(Structure):
    """查询银行资金请求，TradeCode=204002"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", c_char),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')
    def getFuturePwdFlag(self):
        '''密码标志'''
        return self.FuturePwdFlag
    def getFutureAccPwd(self):
        '''密码'''
        return str(self.FutureAccPwd, 'GBK')
    def getCurrencyCode(self):
        '''币种：RMB-人民币 USD-美圆 HKD-港元'''
        return str(self.CurrencyCode, 'GBK')
    
class  CThostFtdcTransferQryBankRspField(Structure):
    """查询银行资金请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("UseAmt", TThostFtdcMoneyType),
        ("FetchAmt", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
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
    
class  CThostFtdcTransferQryDetailReqField(Structure):
    """查询银行交易明细请求，TradeCode=204999"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        
    ]

    def getFutureAccount(self):
        '''期货资金账户'''
        return str(self.FutureAccount, 'GBK')
    
class  CThostFtdcTransferQryDetailRspField(Structure):
    """查询银行交易明细请求响应"""
    _fields_ = [
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("FutureSerial", TThostFtdcTradeSerialNoType),
        ("FutureID", TThostFtdcFutureIDType),
        ("FutureAccount", TThostFtdcFutureAccountType),
        ("BankSerial", TThostFtdcTradeSerialNoType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("CertCode", TThostFtdcCertCodeType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        ("TxAmount", TThostFtdcMoneyType),
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
        return self.Flag
    
class  CThostFtdcRspInfoField(Structure):
    """响应信息"""
    _fields_ = [
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID
    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')
    
class  CThostFtdcExchangeField(Structure):
    """交易所"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeName", TThostFtdcExchangeNameType),
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
        return self.ExchangeProperty
    
class  CThostFtdcProductField(Structure):
    """产品"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ProductName", TThostFtdcProductNameType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductClass", c_char),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("MaxMarketOrderVolume", TThostFtdcVolumeType),
        ("MinMarketOrderVolume", TThostFtdcVolumeType),
        ("MaxLimitOrderVolume", TThostFtdcVolumeType),
        ("MinLimitOrderVolume", TThostFtdcVolumeType),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("CloseDealType", c_char),
        ("TradeCurrencyID", TThostFtdcCurrencyIDType),
        ("MortgageFundUseRange", c_char),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("UnderlyingMultiple", TThostFtdcUnderlyingMultipleType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ExchangeProductID", TThostFtdcInstrumentIDType),
        ("OpenLimitControlLevel", c_char),
        ("OrderFreqControlLevel", c_char),
        
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
        return self.ProductClass
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
        return self.PositionType
    def getPositionDateType(self):
        '''持仓日期类型'''
        return self.PositionDateType
    def getCloseDealType(self):
        '''平仓处理类型'''
        return self.CloseDealType
    def getTradeCurrencyID(self):
        '''交易币种类型'''
        return str(self.TradeCurrencyID, 'GBK')
    def getMortgageFundUseRange(self):
        '''质押资金可用范围'''
        return self.MortgageFundUseRange
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
    def getOpenLimitControlLevel(self):
        '''开仓量限制粒度'''
        return self.OpenLimitControlLevel
    def getOrderFreqControlLevel(self):
        '''报单频率控制粒度'''
        return self.OrderFreqControlLevel
    
class  CThostFtdcInstrumentField(Structure):
    """合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentName", TThostFtdcInstrumentNameType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("reserve3", TThostFtdcOldInstrumentIDType),
        ("ProductClass", c_char),
        ("DeliveryYear", TThostFtdcYearType),
        ("DeliveryMonth", TThostFtdcMonthType),
        ("MaxMarketOrderVolume", TThostFtdcVolumeType),
        ("MinMarketOrderVolume", TThostFtdcVolumeType),
        ("MaxLimitOrderVolume", TThostFtdcVolumeType),
        ("MinLimitOrderVolume", TThostFtdcVolumeType),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("CreateDate", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExpireDate", TThostFtdcDateType),
        ("StartDelivDate", TThostFtdcDateType),
        ("EndDelivDate", TThostFtdcDateType),
        ("InstLifePhase", c_char),
        ("IsTrading", TThostFtdcBoolType),
        ("PositionType", c_char),
        ("PositionDateType", c_char),
        ("LongMarginRatio", TThostFtdcRatioType),
        ("ShortMarginRatio", TThostFtdcRatioType),
        ("MaxMarginSideAlgorithm", c_char),
        ("reserve4", TThostFtdcOldInstrumentIDType),
        ("StrikePrice", TThostFtdcPriceType),
        ("OptionsType", c_char),
        ("UnderlyingMultiple", TThostFtdcUnderlyingMultipleType),
        ("CombinationType", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("UnderlyingInstrID", TThostFtdcInstrumentIDType),
        
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
        return self.ProductClass
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
        return self.InstLifePhase
    def getIsTrading(self):
        '''当前是否交易'''
        return self.IsTrading
    def getPositionType(self):
        '''持仓类型'''
        return self.PositionType
    def getPositionDateType(self):
        '''持仓日期类型'''
        return self.PositionDateType
    def getLongMarginRatio(self):
        '''多头保证金率'''
        return self.LongMarginRatio
    def getShortMarginRatio(self):
        '''空头保证金率'''
        return self.ShortMarginRatio
    def getMaxMarginSideAlgorithm(self):
        '''是否使用大额单边保证金算法'''
        return self.MaxMarginSideAlgorithm
    def getreserve4(self):
        '''保留的无效字段'''
        return str(self.reserve4, 'GBK')
    def getStrikePrice(self):
        '''执行价'''
        return self.StrikePrice
    def getOptionsType(self):
        '''期权类型'''
        return self.OptionsType
    def getUnderlyingMultiple(self):
        '''合约基础商品乘数'''
        return self.UnderlyingMultiple
    def getCombinationType(self):
        '''组合类型'''
        return self.CombinationType
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
    
class  CThostFtdcBrokerField(Structure):
    """经纪公司"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerAbbr", TThostFtdcBrokerAbbrType),
        ("BrokerName", TThostFtdcBrokerNameType),
        ("IsActive", TThostFtdcBoolType),
        
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
    
class  CThostFtdcTraderField(Structure):
    """交易所交易员"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallCount", TThostFtdcInstallCountType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("OrderCancelAlg", c_char),
        
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
    def getOrderCancelAlg(self):
        '''撤单时选择席位算法'''
        return self.OrderCancelAlg
    
class  CThostFtdcInvestorField(Structure):
    """投资者"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorName", TThostFtdcPartyNameType),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("IsActive", TThostFtdcBoolType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("OpenDate", TThostFtdcDateType),
        ("Mobile", TThostFtdcMobileType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("IsOrderFreq", c_char),
        ("IsOpenVolLimit", c_char),
        
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
        return self.IdentifiedCardType
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
    def getIsOrderFreq(self):
        '''是否频率控制'''
        return self.IsOrderFreq
    def getIsOpenVolLimit(self):
        '''是否开仓限制'''
        return self.IsOpenVolLimit
    
class  CThostFtdcTradingCodeField(Structure):
    """交易编码"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("IsActive", TThostFtdcBoolType),
        ("ClientIDType", c_char),
        ("BranchID", TThostFtdcBranchIDType),
        ("BizType", c_char),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
        return self.ClientIDType
    def getBranchID(self):
        '''营业部编号'''
        return str(self.BranchID, 'GBK')
    def getBizType(self):
        '''业务类型'''
        return self.BizType
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    
class  CThostFtdcPartBrokerField(Structure):
    """会员编码和经纪公司编码对照表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("IsActive", TThostFtdcBoolType),
        
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
    
class  CThostFtdcSuperUserField(Structure):
    """管理用户"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        ("UserName", TThostFtdcUserNameType),
        ("Password", TThostFtdcPasswordType),
        ("IsActive", TThostFtdcBoolType),
        
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
    
class  CThostFtdcSuperUserFunctionField(Structure):
    """管理用户功能权限"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        ("FunctionCode", c_char),
        
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getFunctionCode(self):
        '''功能代码'''
        return self.FunctionCode
    
class  CThostFtdcInvestorGroupField(Structure):
    """投资者组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorGroupName", TThostFtdcInvestorGroupNameType),
        
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
    
class  CThostFtdcTradingAccountField(Structure):
    """资金账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("BizType", c_char),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        
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
        return self.BizType
    def getFrozenSwap(self):
        '''延时换汇冻结金额'''
        return self.FrozenSwap
    def getRemainSwap(self):
        '''剩余换汇额度'''
        return self.RemainSwap
    
class  CThostFtdcInvestorPositionField(Structure):
    """投资者持仓"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.PosiDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getPositionDate(self):
        '''持仓日期'''
        return self.PositionDate
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
        '''持仓成本差值'''
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
    
class  CThostFtdcInstrumentMarginRateField(Structure):
    """合约保证金率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcInstrumentCommissionRateField(Structure):
    """合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BizType", c_char),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
        return self.BizType
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcDepthMarketDataField(Structure):
    """深度行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        ("AveragePrice", TThostFtdcPriceType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        
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
    def getBandingUpperPrice(self):
        '''上带价'''
        return self.BandingUpperPrice
    def getBandingLowerPrice(self):
        '''下带价'''
        return self.BandingLowerPrice
    
class  CThostFtdcInstrumentTradingRightField(Structure):
    """投资者合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingRight", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getTradingRight(self):
        '''交易权限'''
        return self.TradingRight
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcBrokerUserField(Structure):
    """经纪公司用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserName", TThostFtdcUserNameType),
        ("UserType", c_char),
        ("IsActive", TThostFtdcBoolType),
        ("IsUsingOTP", TThostFtdcBoolType),
        ("IsAuthForce", TThostFtdcBoolType),
        
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
        return self.UserType
    def getIsActive(self):
        '''是否活跃'''
        return self.IsActive
    def getIsUsingOTP(self):
        '''是否使用令牌'''
        return self.IsUsingOTP
    def getIsAuthForce(self):
        '''是否强制终端认证'''
        return self.IsAuthForce
    
class  CThostFtdcBrokerUserPasswordField(Structure):
    """经纪公司用户口令"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("LastUpdateTime", TThostFtdcDateTimeType),
        ("LastLoginTime", TThostFtdcDateTimeType),
        ("ExpireDate", TThostFtdcDateType),
        ("WeakExpireDate", TThostFtdcDateType),
        
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
    
class  CThostFtdcBrokerUserFunctionField(Structure):
    """经纪公司用户功能权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
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
        return self.BrokerFunctionCode
    
class  CThostFtdcTraderOfferField(Structure):
    """交易所交易员报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", TThostFtdcDateType),
        ("ConnectRequestTime", TThostFtdcTimeType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("ConnectDate", TThostFtdcDateType),
        ("ConnectTime", TThostFtdcTimeType),
        ("StartDate", TThostFtdcDateType),
        ("StartTime", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MaxTradeID", TThostFtdcTradeIDType),
        ("MaxOrderMessageReference", TThostFtdcReturnCodeType),
        ("OrderCancelAlg", c_char),
        
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
        return self.TraderConnectStatus
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
    def getOrderCancelAlg(self):
        '''撤单时选择席位算法'''
        return self.OrderCancelAlg
    
class  CThostFtdcSettlementInfoField(Structure):
    """投资者结算结果"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("Content", TThostFtdcContentType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcInstrumentMarginRateAdjustField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcExchangeMarginRateField(Structure):
    """交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcExchangeMarginRateAdjustField(Structure):
    """交易所保证金率调整"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchLongMarginRatioByMoney", TThostFtdcRatioType),
        ("ExchLongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ExchShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("NoLongMarginRatioByMoney", TThostFtdcRatioType),
        ("NoLongMarginRatioByVolume", TThostFtdcMoneyType),
        ("NoShortMarginRatioByMoney", TThostFtdcRatioType),
        ("NoShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcExchangeRateField(Structure):
    """汇率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromCurrencyUnit", TThostFtdcCurrencyUnitType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        
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
    
class  CThostFtdcSettlementRefField(Structure):
    """结算引用"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')
    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID
    
class  CThostFtdcCurrentTimeField(Structure):
    """当前时间"""
    _fields_ = [
        ("CurrDate", TThostFtdcDateType),
        ("CurrTime", TThostFtdcTimeType),
        ("CurrMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        
    ]

    def getCurrDate(self):
        '''当前交易日'''
        return str(self.CurrDate, 'GBK')
    def getCurrTime(self):
        '''当前时间'''
        return str(self.CurrTime, 'GBK')
    def getCurrMillisec(self):
        '''当前时间（毫秒）'''
        return self.CurrMillisec
    def getActionDay(self):
        '''自然日期'''
        return str(self.ActionDay, 'GBK')
    
class  CThostFtdcCommPhaseField(Structure):
    """通讯阶段"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("CommPhaseNo", TThostFtdcCommPhaseNoType),
        ("SystemID", TThostFtdcSystemIDType),
        
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
    
class  CThostFtdcLoginInfoField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LoginDate", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("SystemName", TThostFtdcSystemNameType),
        ("PasswordDeprecated", TThostFtdcPasswordType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("INETime", TThostFtdcTimeType),
        ("IsQryControl", TThostFtdcBoolType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Password", TThostFtdcPasswordType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcLogoutAllField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("SystemName", TThostFtdcSystemNameType),
        
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
    
class  CThostFtdcFrontStatusField(Structure):
    """前置状态"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("IsActive", TThostFtdcBoolType),
        
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
    
class  CThostFtdcUserPasswordUpdateField(Structure):
    """用户口令变更"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        
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
    
class  CThostFtdcInputOrderField(Structure):
    """输入报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
    
class  CThostFtdcOrderField(Structure):
    """报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("RelativeOrderSysID", TThostFtdcOrderSysIDType),
        ("ZCETotalTradedVolume", TThostFtdcVolumeType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
        return self.OrderSubmitStatus
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
        return self.OrderSource
    def getOrderStatus(self):
        '''报单状态'''
        return self.OrderStatus
    def getOrderType(self):
        '''报单类型'''
        return self.OrderType
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
    
class  CThostFtdcExchangeOrderField(Structure):
    """交易所报单"""
    _fields_ = [
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getOrderPriceType(self):
        '''报单价格条件'''
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
        return self.OrderSubmitStatus
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
        return self.OrderSource
    def getOrderStatus(self):
        '''报单状态'''
        return self.OrderStatus
    def getOrderType(self):
        '''报单类型'''
        return self.OrderType
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
    
class  CThostFtdcExchangeOrderInsertErrorField(Structure):
    """交易所报单插入失败"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
    
class  CThostFtdcInputOrderActionField(Structure):
    """输入报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
    
class  CThostFtdcOrderActionField(Structure):
    """报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcExchangeOrderActionField(Structure):
    """交易所报单操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getOrderSysID(self):
        '''报单编号'''
        return str(self.OrderSysID, 'GBK')
    def getActionFlag(self):
        '''操作标志'''
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcExchangeOrderActionErrorField(Structure):
    """交易所报单操作失败"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
    
class  CThostFtdcExchangeTradeField(Structure):
    """交易所成交"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Direction", c_char),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("TradingRole", c_char),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTimeType),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", TThostFtdcTraderIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("TradeSource", c_char),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TradingRole
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getOffsetFlag(self):
        '''开平标志'''
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
        return self.TradeType
    def getPriceSource(self):
        '''成交价来源'''
        return self.PriceSource
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
        return self.TradeSource
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
    
class  CThostFtdcTradeField(Structure):
    """成交"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Direction", c_char),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("TradingRole", c_char),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("Price", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTimeType),
        ("TradeType", c_char),
        ("PriceSource", c_char),
        ("TraderID", TThostFtdcTraderIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("TradeSource", c_char),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
        return self.Direction
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
        return self.TradingRole
    def getreserve2(self):
        '''保留的无效字段'''
        return str(self.reserve2, 'GBK')
    def getOffsetFlag(self):
        '''开平标志'''
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
        return self.TradeType
    def getPriceSource(self):
        '''成交价来源'''
        return self.PriceSource
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
        return self.TradeSource
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
    
class  CThostFtdcUserSessionField(Structure):
    """用户会话"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LoginDate", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcQryMaxOrderVolumeField(Structure):
    """查询最大报单数量"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.Direction
    def getOffsetFlag(self):
        '''开平标志'''
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcSettlementInfoConfirmField(Structure):
    """投资者结算结果确认信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ConfirmDate", TThostFtdcDateType),
        ("ConfirmTime", TThostFtdcTimeType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcSyncDepositField(Structure):
    """出入金同步"""
    _fields_ = [
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Deposit", TThostFtdcMoneyType),
        ("IsForce", TThostFtdcBoolType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("IsFromSopt", TThostFtdcBoolType),
        ("TradingPassword", TThostFtdcPasswordType),
        
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
    def getIsFromSopt(self):
        '''是否是个股期权内转'''
        return self.IsFromSopt
    def getTradingPassword(self):
        '''资金密码'''
        return str(self.TradingPassword, 'GBK')
    
class  CThostFtdcSyncFundMortgageField(Structure):
    """货币质押同步"""
    _fields_ = [
        ("MortgageSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("MortgageAmount", TThostFtdcMoneyType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcBrokerSyncField(Structure):
    """经纪公司同步"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcSyncingInvestorField(Structure):
    """正在同步中的投资者"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorName", TThostFtdcPartyNameType),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("IsActive", TThostFtdcBoolType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("OpenDate", TThostFtdcDateType),
        ("Mobile", TThostFtdcMobileType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("IsOrderFreq", c_char),
        ("IsOpenVolLimit", c_char),
        
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
        return self.IdentifiedCardType
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
    def getIsOrderFreq(self):
        '''是否频率控制'''
        return self.IsOrderFreq
    def getIsOpenVolLimit(self):
        '''是否开仓限制'''
        return self.IsOpenVolLimit
    
class  CThostFtdcSyncingTradingCodeField(Structure):
    """正在同步中的交易代码"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("IsActive", TThostFtdcBoolType),
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
        return self.ClientIDType
    
class  CThostFtdcSyncingInvestorGroupField(Structure):
    """正在同步中的投资者分组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorGroupName", TThostFtdcInvestorGroupNameType),
        
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
    
class  CThostFtdcSyncingTradingAccountField(Structure):
    """正在同步中的交易账号"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        
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
    
class  CThostFtdcSyncingInvestorPositionField(Structure):
    """正在同步中的投资者持仓"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.PosiDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getPositionDate(self):
        '''持仓日期'''
        return self.PositionDate
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
        '''持仓成本差值'''
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
    
class  CThostFtdcSyncingInstrumentMarginRateField(Structure):
    """正在同步中的合约保证金率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcSyncingInstrumentCommissionRateField(Structure):
    """正在同步中的合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcSyncingInstrumentTradingRightField(Structure):
    """正在同步中的合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingRight", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getTradingRight(self):
        '''交易权限'''
        return self.TradingRight
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryTradeField(Structure):
    """查询成交"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("TradeTimeStart", TThostFtdcTimeType),
        ("TradeTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryInvestorPositionField(Structure):
    """查询投资者持仓"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryTradingAccountField(Structure):
    """查询资金账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BizType", c_char),
        ("AccountID", TThostFtdcAccountIDType),
        
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
        return self.BizType
    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')
    
class  CThostFtdcQryInvestorField(Structure):
    """查询投资者"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcQryTradingCodeField(Structure):
    """查询交易编码"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ClientIDType", c_char),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
        return self.ClientIDType
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    
class  CThostFtdcQryInvestorGroupField(Structure):
    """查询投资者组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcQryInstrumentMarginRateField(Structure):
    """查询合约保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryInstrumentCommissionRateField(Structure):
    """查询手续费率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryInstrumentTradingRightField(Structure):
    """查询合约交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryBrokerField(Structure):
    """查询经纪公司"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcQryTraderField(Structure):
    """查询交易员"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcQrySuperUserFunctionField(Structure):
    """查询管理用户功能权限"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcQryUserSessionField(Structure):
    """查询用户会话"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
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
    
class  CThostFtdcQryPartBrokerField(Structure):
    """查询经纪公司会员代码"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        
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
    
class  CThostFtdcQryFrontStatusField(Structure):
    """查询前置状态"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        
    ]

    def getFrontID(self):
        '''前置编号'''
        return self.FrontID
    
class  CThostFtdcQryExchangeOrderField(Structure):
    """查询交易所报单"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcQryOrderActionField(Structure):
    """查询报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
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
    
class  CThostFtdcQryExchangeOrderActionField(Structure):
    """查询交易所报单操作"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcQrySuperUserField(Structure):
    """查询管理用户"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcQryExchangeField(Structure):
    """查询交易所"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    
class  CThostFtdcQryProductField(Structure):
    """查询产品"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ProductClass", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getProductClass(self):
        '''产品类型'''
        return self.ProductClass
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')
    
class  CThostFtdcQryInstrumentField(Structure):
    """查询合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("reserve3", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryDepthMarketDataField(Structure):
    """查询行情"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryBrokerUserField(Structure):
    """查询经纪公司用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcQryBrokerUserFunctionField(Structure):
    """查询经纪公司用户权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcQryTraderOfferField(Structure):
    """查询交易员报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcQrySyncDepositField(Structure):
    """查询出入金流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getDepositSeqNo(self):
        '''出入金流水号'''
        return str(self.DepositSeqNo, 'GBK')
    
class  CThostFtdcQrySettlementInfoField(Structure):
    """查询投资者结算结果"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingDay", TThostFtdcDateType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcQryExchangeMarginRateField(Structure):
    """查询交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryExchangeMarginRateAdjustField(Structure):
    """查询交易所调整保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryExchangeRateField(Structure):
    """查询汇率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcQrySyncFundMortgageField(Structure):
    """查询货币质押流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MortgageSeqNo", TThostFtdcDepositSeqNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getMortgageSeqNo(self):
        '''货币质押流水号'''
        return str(self.MortgageSeqNo, 'GBK')
    
class  CThostFtdcQryHisOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcOptionInstrMiniMarginField(Structure):
    """当前期权合约最小保证金"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("MinMargin", TThostFtdcMoneyType),
        ("ValueMethod", c_char),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
        return self.ValueMethod
    def getIsRelative(self):
        '''是否跟随交易所收取'''
        return self.IsRelative
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcOptionInstrMarginAdjustField(Structure):
    """当前期权合约保证金调整系数"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcOptionInstrCommRateField(Structure):
    """当前期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcOptionInstrTradeCostField(Structure):
    """期权交易成本"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("FixedMargin", TThostFtdcMoneyType),
        ("MiniMargin", TThostFtdcMoneyType),
        ("Royalty", TThostFtdcMoneyType),
        ("ExchFixedMargin", TThostFtdcMoneyType),
        ("ExchMiniMargin", TThostFtdcMoneyType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
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
    
class  CThostFtdcQryOptionInstrTradeCostField(Structure):
    """期权交易成本查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("InputPrice", TThostFtdcPriceType),
        ("UnderlyingPrice", TThostFtdcPriceType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
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
    
class  CThostFtdcQryOptionInstrCommRateField(Structure):
    """期权手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcIndexPriceField(Structure):
    """股指现货指数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ClosePrice", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcInputExecOrderField(Structure):
    """输入的执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return self.PosiDirection
    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return self.ReservePositionFlag
    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return self.CloseFlag
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
    
class  CThostFtdcInputExecOrderActionField(Structure):
    """输入执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
    
class  CThostFtdcExecOrderField(Structure):
    """执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerExecOrderSeq", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return self.PosiDirection
    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return self.ReservePositionFlag
    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return self.CloseFlag
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
        return self.OrderSubmitStatus
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
        return self.ExecResult
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
    
class  CThostFtdcExecOrderActionField(Structure):
    """执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("ActionType", c_char),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.OrderActionStatus
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
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
    
class  CThostFtdcQryExecOrderField(Structure):
    """执行宣告查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcExchangeExecOrderField(Structure):
    """交易所执行宣告信息"""
    _fields_ = [
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return self.PosiDirection
    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return self.ReservePositionFlag
    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return self.CloseFlag
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
        return self.OrderSubmitStatus
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
        return self.ExecResult
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
    
class  CThostFtdcQryExchangeExecOrderField(Structure):
    """交易所执行宣告查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcQryExecOrderActionField(Structure):
    """执行宣告操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
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
    
class  CThostFtdcExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("ActionType", c_char),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("Volume", TThostFtdcVolumeType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getExecOrderSysID(self):
        '''执行宣告操作编号'''
        return str(self.ExecOrderSysID, 'GBK')
    def getActionFlag(self):
        '''操作标志'''
        return self.ActionFlag
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
        return self.OrderActionStatus
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
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
    
class  CThostFtdcQryExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcErrExecOrderField(Structure):
    """错误执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("ActionType", c_char),
        ("PosiDirection", c_char),
        ("ReservePositionFlag", c_char),
        ("CloseFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getActionType(self):
        '''执行类型'''
        return self.ActionType
    def getPosiDirection(self):
        '''保留头寸申请的持仓方向'''
        return self.PosiDirection
    def getReservePositionFlag(self):
        '''期权行权后是否保留期货头寸的标记,该字段已废弃'''
        return self.ReservePositionFlag
    def getCloseFlag(self):
        '''期权行权后生成的头寸是否自动平仓'''
        return self.CloseFlag
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
    
class  CThostFtdcQryErrExecOrderField(Structure):
    """查询错误执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcErrExecOrderActionField(Structure):
    """错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
    
class  CThostFtdcQryErrExecOrderActionField(Structure):
    """查询错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcOptionInstrTradingRightField(Structure):
    """投资者期权合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Direction", c_char),
        ("TradingRight", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
    def getTradingRight(self):
        '''交易权限'''
        return self.TradingRight
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryOptionInstrTradingRightField(Structure):
    """查询期权合约交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.Direction
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcInputForQuoteField(Structure):
    """输入的询价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcForQuoteField(Structure):
    """询价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ForQuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ForQuoteStatus", c_char),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerForQutoSeq", TThostFtdcSequenceNoType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ForQuoteStatus
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
    
class  CThostFtdcQryForQuoteField(Structure):
    """询价查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcExchangeForQuoteField(Structure):
    """交易所询价信息"""
    _fields_ = [
        ("ForQuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ForQuoteStatus", c_char),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ForQuoteStatus
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
    
class  CThostFtdcQryExchangeForQuoteField(Structure):
    """交易所询价查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcInputQuoteField(Structure):
    """输入的报价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("AskOrderRef", TThostFtdcOrderRefType),
        ("BidOrderRef", TThostFtdcOrderRefType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ReplaceSysID", TThostFtdcOrderSysIDType),
        
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
        return self.AskOffsetFlag
    def getBidOffsetFlag(self):
        '''买开平标志'''
        return self.BidOffsetFlag
    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return self.AskHedgeFlag
    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return self.BidHedgeFlag
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
    def getReplaceSysID(self):
        '''被顶单编号'''
        return str(self.ReplaceSysID, 'GBK')
    
class  CThostFtdcInputQuoteActionField(Structure):
    """输入报价操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("QuoteActionRef", TThostFtdcOrderActionRefType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
    
class  CThostFtdcQuoteField(Structure):
    """报价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("QuoteStatus", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("AskOrderSysID", TThostFtdcOrderSysIDType),
        ("BidOrderSysID", TThostFtdcOrderSysIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerQuoteSeq", TThostFtdcSequenceNoType),
        ("AskOrderRef", TThostFtdcOrderRefType),
        ("BidOrderRef", TThostFtdcOrderRefType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ReplaceSysID", TThostFtdcOrderSysIDType),
        
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
        return self.AskOffsetFlag
    def getBidOffsetFlag(self):
        '''买开平标志'''
        return self.BidOffsetFlag
    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return self.AskHedgeFlag
    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return self.BidHedgeFlag
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
        return self.OrderSubmitStatus
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
        return self.QuoteStatus
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
    def getReplaceSysID(self):
        '''被顶单编号'''
        return str(self.ReplaceSysID, 'GBK')
    
class  CThostFtdcQuoteActionField(Structure):
    """报价操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("QuoteActionRef", TThostFtdcOrderActionRefType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcQryQuoteField(Structure):
    """报价查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcExchangeQuoteField(Structure):
    """交易所报价信息"""
    _fields_ = [
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", c_char),
        ("BidOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("OrderSubmitStatus", c_char),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("QuoteStatus", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("AskOrderSysID", TThostFtdcOrderSysIDType),
        ("BidOrderSysID", TThostFtdcOrderSysIDType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.AskOffsetFlag
    def getBidOffsetFlag(self):
        '''买开平标志'''
        return self.BidOffsetFlag
    def getAskHedgeFlag(self):
        '''卖投机套保标志'''
        return self.AskHedgeFlag
    def getBidHedgeFlag(self):
        '''买投机套保标志'''
        return self.BidHedgeFlag
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
        return self.OrderSubmitStatus
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
        return self.QuoteStatus
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
    
class  CThostFtdcQryExchangeQuoteField(Structure):
    """交易所报价查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcQryQuoteActionField(Structure):
    """报价操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
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
    
class  CThostFtdcExchangeQuoteActionField(Structure):
    """交易所报价操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getQuoteSysID(self):
        '''报价操作编号'''
        return str(self.QuoteSysID, 'GBK')
    def getActionFlag(self):
        '''操作标志'''
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcQryExchangeQuoteActionField(Structure):
    """交易所报价操作查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcOptionInstrDeltaField(Structure):
    """期权合约delta值"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Delta", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcForQuoteRspField(Structure):
    """发给做市商的询价请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("ForQuoteTime", TThostFtdcTimeType),
        ("ActionDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcStrikeOffsetField(Structure):
    """当前期权合约执行偏移值的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Offset", TThostFtdcMoneyType),
        ("OffsetType", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
        return self.OffsetType
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryStrikeOffsetField(Structure):
    """期权执行偏移值查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcInputBatchOrderActionField(Structure):
    """输入批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("UserID", TThostFtdcUserIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcBatchOrderActionField(Structure):
    """批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderActionStatus
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
    
class  CThostFtdcExchangeBatchOrderActionField(Structure):
    """交易所批量报单操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderActionStatus
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
    
class  CThostFtdcQryBatchOrderActionField(Structure):
    """查询批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
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
    
class  CThostFtdcCombInstrumentGuardField(Structure):
    """组合合约安全系数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("GuarantRatio", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryCombInstrumentGuardField(Structure):
    """组合合约安全系数查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcInputCombActionField(Structure):
    """输入的申请组合"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("CombActionRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Direction", c_char),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.Direction
    def getVolume(self):
        '''数量'''
        return self.Volume
    def getCombDirection(self):
        '''组合指令方向'''
        return self.CombDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcCombActionField(Structure):
    """申请组合"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("CombActionRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Direction", c_char),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.Direction
    def getVolume(self):
        '''数量'''
        return self.Volume
    def getCombDirection(self):
        '''组合指令方向'''
        return self.CombDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
        return self.ActionStatus
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
    
class  CThostFtdcQryCombActionField(Structure):
    """申请组合查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcExchangeCombActionField(Structure):
    """交易所申请组合信息"""
    _fields_ = [
        ("Direction", c_char),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", c_char),
        ("HedgeFlag", c_char),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getDirection(self):
        '''买卖方向'''
        return self.Direction
    def getVolume(self):
        '''数量'''
        return self.Volume
    def getCombDirection(self):
        '''组合指令方向'''
        return self.CombDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
        return self.ActionStatus
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
    
class  CThostFtdcQryExchangeCombActionField(Structure):
    """交易所申请组合查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcProductExchRateField(Structure):
    """产品报价汇率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryProductExchRateField(Structure):
    """产品报价汇率查询"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryForQuoteParamField(Structure):
    """查询询价价差参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcForQuoteParamField(Structure):
    """询价价差参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PriceInterval", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcMMOptionInstrCommRateField(Structure):
    """当前做市商期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcQryMMOptionInstrCommRateField(Structure):
    """做市商期权手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcMMInstrumentCommissionRateField(Structure):
    """做市商合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcQryMMInstrumentCommissionRateField(Structure):
    """查询做市商合约手续费率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcInstrumentOrderCommRateField(Structure):
    """当前报单手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("OrderCommByVolume", TThostFtdcRatioType),
        ("OrderActionCommByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("OrderCommByTrade", TThostFtdcRatioType),
        ("OrderActionCommByTrade", TThostFtdcRatioType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    def getOrderCommByTrade(self):
        '''报单手续费'''
        return self.OrderCommByTrade
    def getOrderActionCommByTrade(self):
        '''撤单手续费'''
        return self.OrderActionCommByTrade
    
class  CThostFtdcQryInstrumentOrderCommRateField(Structure):
    """报单手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcTradeParamField(Structure):
    """交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("TradeParamID", c_char),
        ("TradeParamValue", TThostFtdcSettlementParamValueType),
        ("Memo", TThostFtdcMemoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getTradeParamID(self):
        '''参数代码'''
        return self.TradeParamID
    def getTradeParamValue(self):
        '''参数代码值'''
        return str(self.TradeParamValue, 'GBK')
    def getMemo(self):
        '''备注'''
        return str(self.Memo, 'GBK')
    
class  CThostFtdcInstrumentMarginRateULField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcFutureLimitPosiParamField(Structure):
    """期货持仓限制参数"""
    _fields_ = [
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("SpecOpenVolume", TThostFtdcVolumeType),
        ("ArbiOpenVolume", TThostFtdcVolumeType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]

    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcLoginForbiddenIPField(Structure):
    """禁止登录IP"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    
class  CThostFtdcIPListField(Structure):
    """IP列表"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IsWhite", TThostFtdcBoolType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcInputOptionSelfCloseField(Structure):
    """输入的期权自对冲"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.HedgeFlag
    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return self.OptSelfCloseFlag
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
    
class  CThostFtdcInputOptionSelfCloseActionField(Structure):
    """输入期权自对冲操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OptionSelfCloseActionRef", TThostFtdcOrderActionRefType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
    
class  CThostFtdcOptionSelfCloseField(Structure):
    """期权自对冲"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOptionSelfCloseSeq", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.HedgeFlag
    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return self.OptSelfCloseFlag
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
        return self.OrderSubmitStatus
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
        return self.ExecResult
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
    
class  CThostFtdcOptionSelfCloseActionField(Structure):
    """期权自对冲操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OptionSelfCloseActionRef", TThostFtdcOrderActionRefType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcQryOptionSelfCloseField(Structure):
    """期权自对冲查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcExchangeOptionSelfCloseField(Structure):
    """交易所期权自对冲信息"""
    _fields_ = [
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", c_char),
        ("OptSelfCloseFlag", c_char),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", c_char),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.HedgeFlag
    def getOptSelfCloseFlag(self):
        '''期权行权的头寸是否自对冲'''
        return self.OptSelfCloseFlag
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
        return self.OrderSubmitStatus
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
        return self.ExecResult
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
    
class  CThostFtdcQryOptionSelfCloseActionField(Structure):
    """期权自对冲操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
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
    
class  CThostFtdcExchangeOptionSelfCloseActionField(Structure):
    """交易所期权自对冲操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("OptSelfCloseFlag", c_char),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getOptionSelfCloseSysID(self):
        '''期权自对冲操作编号'''
        return str(self.OptionSelfCloseSysID, 'GBK')
    def getActionFlag(self):
        '''操作标志'''
        return self.ActionFlag
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
        return self.OrderActionStatus
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
        return self.OptSelfCloseFlag
    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
    
class  CThostFtdcSyncDelaySwapField(Structure):
    """延时换汇同步"""
    _fields_ = [
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromAmount", TThostFtdcMoneyType),
        ("FromFrozenSwap", TThostFtdcMoneyType),
        ("FromRemainSwap", TThostFtdcMoneyType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        ("ToAmount", TThostFtdcMoneyType),
        ("IsManualSwap", TThostFtdcBoolType),
        ("IsAllRemainSetZero", TThostFtdcBoolType),
        
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
    
class  CThostFtdcQrySyncDelaySwapField(Structure):
    """查询延时换汇同步"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getDelaySwapSeqNo(self):
        '''延时换汇流水号'''
        return str(self.DelaySwapSeqNo, 'GBK')
    
class  CThostFtdcInvestUnitField(Structure):
    """投资单元"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InvestorUnitName", TThostFtdcPartyNameType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcQryInvestUnitField(Structure):
    """查询投资单元"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcSecAgentCheckModeField(Structure):
    """二级代理商资金校验模式"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        ("CheckSelfAccount", TThostFtdcBoolType),
        
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
    
class  CThostFtdcSecAgentTradeInfoField(Structure):
    """二级代理商信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
    
class  CThostFtdcMarketDataField(Structure):
    """市场行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcMarketDataBaseField(Structure):
    """行情基础属性"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("PreDelta", TThostFtdcRatioType),
        
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
    
class  CThostFtdcMarketDataStaticField(Structure):
    """行情静态属性"""
    _fields_ = [
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("ClosePrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CurrDelta", TThostFtdcRatioType),
        
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
    
class  CThostFtdcMarketDataLastMatchField(Structure):
    """行情最新成交属性"""
    _fields_ = [
        ("LastPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        
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
    
class  CThostFtdcMarketDataBestPriceField(Structure):
    """行情最优价属性"""
    _fields_ = [
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        
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
    
class  CThostFtdcMarketDataBid23Field(Structure):
    """行情申买二、三属性"""
    _fields_ = [
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        
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
    
class  CThostFtdcMarketDataAsk23Field(Structure):
    """行情申卖二、三属性"""
    _fields_ = [
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        
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
    
class  CThostFtdcMarketDataBid45Field(Structure):
    """行情申买四、五属性"""
    _fields_ = [
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        
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
    
class  CThostFtdcMarketDataAsk45Field(Structure):
    """行情申卖四、五属性"""
    _fields_ = [
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        
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
    
class  CThostFtdcMarketDataUpdateTimeField(Structure):
    """行情更新时间属性"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcMarketDataBandingPriceField(Structure):
    """行情上下带价"""
    _fields_ = [
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        
    ]

    def getBandingUpperPrice(self):
        '''上带价'''
        return self.BandingUpperPrice
    def getBandingLowerPrice(self):
        '''下带价'''
        return self.BandingLowerPrice
    
class  CThostFtdcMarketDataExchangeField(Structure):
    """行情交易所代码属性"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    
class  CThostFtdcSpecificInstrumentField(Structure):
    """指定的合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcInstrumentStatusField(Structure):
    """合约状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("SettlementGroupID", TThostFtdcSettlementGroupIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("InstrumentStatus", c_char),
        ("TradingSegmentSN", TThostFtdcTradingSegmentSNType),
        ("EnterTime", TThostFtdcTimeType),
        ("EnterReason", c_char),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.InstrumentStatus
    def getTradingSegmentSN(self):
        '''交易阶段编号'''
        return self.TradingSegmentSN
    def getEnterTime(self):
        '''进入本状态时间'''
        return str(self.EnterTime, 'GBK')
    def getEnterReason(self):
        '''进入本状态原因'''
        return self.EnterReason
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryInstrumentStatusField(Structure):
    """查询合约状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
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
    
class  CThostFtdcInvestorAccountField(Structure):
    """投资者账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcPositionProfitAlgorithmField(Structure):
    """浮动盈亏算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Algorithm", c_char),
        ("Memo", TThostFtdcMemoType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')
    def getAlgorithm(self):
        '''盈亏算法'''
        return self.Algorithm
    def getMemo(self):
        '''备注'''
        return str(self.Memo, 'GBK')
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    
class  CThostFtdcDiscountField(Structure):
    """会员资金折扣"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", c_char),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Discount", TThostFtdcRatioType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getDiscount(self):
        '''资金折扣比例'''
        return self.Discount
    
class  CThostFtdcQryTransferBankField(Structure):
    """查询转帐银行"""
    _fields_ = [
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        
    ]

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')
    def getBankBrchID(self):
        '''银行分中心代码'''
        return str(self.BankBrchID, 'GBK')
    
class  CThostFtdcTransferBankField(Structure):
    """转帐银行"""
    _fields_ = [
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankName", TThostFtdcBankNameType),
        ("IsActive", TThostFtdcBoolType),
        
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
    
class  CThostFtdcQryInvestorPositionDetailField(Structure):
    """查询投资者持仓明细"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcInvestorPositionDetailField(Structure):
    """投资者持仓明细"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("OpenDate", TThostFtdcDateType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Volume", TThostFtdcVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("TradeType", c_char),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("PositionProfitByDate", TThostFtdcMoneyType),
        ("PositionProfitByTrade", TThostFtdcMoneyType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LastSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("TimeFirstVolume", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("SpecPosiType", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
    def getDirection(self):
        '''买卖'''
        return self.Direction
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
        return self.TradeType
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
        '''先开先平剩余数量'''
        return self.TimeFirstVolume
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getSpecPosiType(self):
        '''特殊持仓标志'''
        return self.SpecPosiType
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')
    
class  CThostFtdcTradingAccountPasswordField(Structure):
    """资金账户口令域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcMDTraderOfferField(Structure):
    """交易所行情报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("TraderConnectStatus", c_char),
        ("ConnectRequestDate", TThostFtdcDateType),
        ("ConnectRequestTime", TThostFtdcTimeType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("ConnectDate", TThostFtdcDateType),
        ("ConnectTime", TThostFtdcTimeType),
        ("StartDate", TThostFtdcDateType),
        ("StartTime", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MaxTradeID", TThostFtdcTradeIDType),
        ("MaxOrderMessageReference", TThostFtdcReturnCodeType),
        ("OrderCancelAlg", c_char),
        
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
        return self.TraderConnectStatus
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
    def getOrderCancelAlg(self):
        '''撤单时选择席位算法'''
        return self.OrderCancelAlg
    
class  CThostFtdcQryMDTraderOfferField(Structure):
    """查询行情报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
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
    
class  CThostFtdcQryNoticeField(Structure):
    """查询客户通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcNoticeField(Structure):
    """客户通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("Content", TThostFtdcContentType),
        ("SequenceLabel", TThostFtdcSequenceLabelType),
        
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
    
class  CThostFtdcUserRightField(Structure):
    """用户权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserRightType", c_char),
        ("IsForbidden", TThostFtdcBoolType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getUserRightType(self):
        '''客户权限类型'''
        return self.UserRightType
    def getIsForbidden(self):
        '''是否禁止'''
        return self.IsForbidden
    
class  CThostFtdcQrySettlementInfoConfirmField(Structure):
    """查询结算信息确认域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcLoadSettlementInfoField(Structure):
    """装载结算信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcBrokerWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("WithdrawAlgorithm", c_char),
        ("UsingRatio", TThostFtdcRatioType),
        ("IncludeCloseProfit", c_char),
        ("AllWithoutTrade", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("IsBrokerUserEvent", TThostFtdcBoolType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("FundMortgageRatio", TThostFtdcRatioType),
        ("BalanceAlgorithm", c_char),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getWithdrawAlgorithm(self):
        '''可提资金算法'''
        return self.WithdrawAlgorithm
    def getUsingRatio(self):
        '''资金使用率'''
        return self.UsingRatio
    def getIncludeCloseProfit(self):
        '''可提是否包含平仓盈利'''
        return self.IncludeCloseProfit
    def getAllWithoutTrade(self):
        '''本日无仓且无成交客户是否受可提比例限制'''
        return self.AllWithoutTrade
    def getAvailIncludeCloseProfit(self):
        '''可用是否包含平仓盈利'''
        return self.AvailIncludeCloseProfit
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
        return self.BalanceAlgorithm
    
class  CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        
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
    
class  CThostFtdcTradingAccountPasswordUpdateField(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcQryCombinationLegField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("LegID", TThostFtdcLegIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("LegInstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQrySyncStatusField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')
    
class  CThostFtdcCombinationLegField(Structure):
    """组合交易合约的单腿"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("LegID", TThostFtdcLegIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("Direction", c_char),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("ImplyLevel", TThostFtdcImplyLevelType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("LegInstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.Direction
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
    
class  CThostFtdcSyncStatusField(Structure):
    """数据同步状态"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("DataSyncStatus", c_char),
        
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')
    def getDataSyncStatus(self):
        '''数据同步状态'''
        return self.DataSyncStatus
    
class  CThostFtdcQryLinkManField(Structure):
    """查询联系人"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcLinkManField(Structure):
    """联系人"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PersonType", c_char),
        ("IdentifiedCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("PersonName", TThostFtdcPartyNameType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Priority", TThostFtdcPriorityType),
        ("UOAZipCode", TThostFtdcUOAZipCodeType),
        ("PersonFullName", TThostFtdcInvestorFullNameType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getPersonType(self):
        '''联系人类型'''
        return self.PersonType
    def getIdentifiedCardType(self):
        '''证件类型'''
        return self.IdentifiedCardType
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
    
class  CThostFtdcQryBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
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
        return self.UserEventType
    
class  CThostFtdcBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserEventType", c_char),
        ("EventSequenceNo", TThostFtdcSequenceNoType),
        ("EventDate", TThostFtdcDateType),
        ("EventTime", TThostFtdcTimeType),
        ("UserEventInfo", TThostFtdcUserEventInfoType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getUserEventType(self):
        '''用户事件类型'''
        return self.UserEventType
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
    
class  CThostFtdcQryContractBankField(Structure):
    """查询签约银行请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        
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
    
class  CThostFtdcContractBankField(Structure):
    """查询签约银行响应"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankName", TThostFtdcBankNameType),
        
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
    
class  CThostFtdcInvestorPositionCombineDetailField(Structure):
    """投资者组合持仓明细"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", TThostFtdcVolumeType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LegID", TThostFtdcLegIDType),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
    def getDirection(self):
        '''买卖'''
        return self.Direction
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
    
class  CThostFtdcParkedOrderField(Structure):
    """预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParkedOrderID", TThostFtdcParkedOrderIDType),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
        return self.UserType
    def getStatus(self):
        '''预埋单状态'''
        return self.Status
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
    
class  CThostFtdcParkedOrderActionField(Structure):
    """输入预埋单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ParkedOrderActionID", TThostFtdcParkedOrderActionIDType),
        ("UserType", c_char),
        ("Status", c_char),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.UserType
    def getStatus(self):
        '''预埋撤单状态'''
        return self.Status
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
    
class  CThostFtdcQryParkedOrderField(Structure):
    """查询预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryParkedOrderActionField(Structure):
    """查询预埋撤单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcRemoveParkedOrderField(Structure):
    """删除预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ParkedOrderID", TThostFtdcParkedOrderIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcRemoveParkedOrderActionField(Structure):
    """删除预埋撤单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ParkedOrderActionID", TThostFtdcParkedOrderActionIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcInvestorWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", c_char),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("UsingRatio", TThostFtdcRatioType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("FundMortgageRatio", TThostFtdcRatioType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcQryInvestorPositionCombineDetailField(Structure):
    """查询组合持仓明细"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcMarketDataAveragePriceField(Structure):
    """成交均价"""
    _fields_ = [
        ("AveragePrice", TThostFtdcPriceType),
        
    ]

    def getAveragePrice(self):
        '''当日均价'''
        return self.AveragePrice
    
class  CThostFtdcVerifyInvestorPasswordField(Structure):
    """校验投资者密码"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Password", TThostFtdcPasswordType),
        
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
    
class  CThostFtdcUserIPField(Structure):
    """用户IP"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("IPMask", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcTradingNoticeInfoField(Structure):
    """用户事件通知信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SendTime", TThostFtdcTimeType),
        ("FieldContent", TThostFtdcContentType),
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcTradingNoticeField(Structure):
    """用户事件通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", c_char),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("UserID", TThostFtdcUserIDType),
        ("SendTime", TThostFtdcTimeType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FieldContent", TThostFtdcContentType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    
class  CThostFtdcQryTradingNoticeField(Structure):
    """查询交易事件通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcQryErrOrderField(Structure):
    """查询错误报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcErrOrderField(Structure):
    """错误报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
    
class  CThostFtdcErrorConditionalOrderField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", c_char),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", c_char),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", c_char),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", c_char),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("RelativeOrderSysID", TThostFtdcOrderSysIDType),
        ("ZCETotalTradedVolume", TThostFtdcVolumeType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.OrderPriceType
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
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
        return self.TimeCondition
    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')
    def getVolumeCondition(self):
        '''成交量类型'''
        return self.VolumeCondition
    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume
    def getContingentCondition(self):
        '''触发条件'''
        return self.ContingentCondition
    def getStopPrice(self):
        '''止损价'''
        return self.StopPrice
    def getForceCloseReason(self):
        '''强平原因'''
        return self.ForceCloseReason
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
        return self.OrderSubmitStatus
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
        return self.OrderSource
    def getOrderStatus(self):
        '''报单状态'''
        return self.OrderStatus
    def getOrderType(self):
        '''报单类型'''
        return self.OrderType
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
    
class  CThostFtdcQryErrOrderActionField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcErrOrderActionField(Structure):
    """错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", c_char),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", c_char),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
        return self.ActionFlag
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
        return self.OrderActionStatus
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
    
class  CThostFtdcQryExchangeSequenceField(Structure):
    """查询交易所状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    
class  CThostFtdcExchangeSequenceField(Structure):
    """交易所状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
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
        return self.MarketStatus
    
class  CThostFtdcQryMaxOrderVolumeWithPriceField(Structure):
    """根据价格查询最大报单数量"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("MaxVolume", TThostFtdcVolumeType),
        ("Price", TThostFtdcPriceType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.Direction
    def getOffsetFlag(self):
        '''开平标志'''
        return self.OffsetFlag
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    
class  CThostFtdcQryBrokerTradingParamsField(Structure):
    """查询经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("AccountID", TThostFtdcAccountIDType),
        
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
    
class  CThostFtdcBrokerTradingParamsField(Structure):
    """经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("MarginPriceType", c_char),
        ("Algorithm", c_char),
        ("AvailIncludeCloseProfit", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("OptionRoyaltyPriceType", c_char),
        ("AccountID", TThostFtdcAccountIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getMarginPriceType(self):
        '''保证金价格类型'''
        return self.MarginPriceType
    def getAlgorithm(self):
        '''盈亏算法'''
        return self.Algorithm
    def getAvailIncludeCloseProfit(self):
        '''可用是否包含平仓盈利'''
        return self.AvailIncludeCloseProfit
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getOptionRoyaltyPriceType(self):
        '''期权权利金价格类型'''
        return self.OptionRoyaltyPriceType
    def getAccountID(self):
        '''投资者帐号'''
        return str(self.AccountID, 'GBK')
    
class  CThostFtdcQryBrokerTradingAlgosField(Structure):
    """查询经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcBrokerTradingAlgosField(Structure):
    """经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HandlePositionAlgoID", c_char),
        ("FindMarginRateAlgoID", c_char),
        ("HandleTradingAccountAlgoID", c_char),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.HandlePositionAlgoID
    def getFindMarginRateAlgoID(self):
        '''寻找保证金率算法编号'''
        return self.FindMarginRateAlgoID
    def getHandleTradingAccountAlgoID(self):
        '''资金处理算法编号'''
        return self.HandleTradingAccountAlgoID
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQueryBrokerDepositField(Structure):
    """查询经纪公司资金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    
class  CThostFtdcBrokerDepositField(Structure):
    """经纪公司资金"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("PreBalance", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        
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
    
class  CThostFtdcQryCFMMCBrokerKeyField(Structure):
    """查询保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    
class  CThostFtdcCFMMCBrokerKeyField(Structure):
    """保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("CreateDate", TThostFtdcDateType),
        ("CreateTime", TThostFtdcTimeType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("CurrentKey", TThostFtdcCFMMCKeyType),
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
        return self.KeyKind
    
class  CThostFtdcCFMMCTradingAccountKeyField(Structure):
    """保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("CurrentKey", TThostFtdcCFMMCKeyType),
        
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
    
class  CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
    """请求查询保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcBrokerUserOTPParamField(Structure):
    """用户动态令牌参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OTPVendorsID", TThostFtdcOTPVendorsIDType),
        ("SerialNumber", TThostFtdcSerialNumberType),
        ("AuthKey", TThostFtdcAuthKeyType),
        ("LastDrift", TThostFtdcLastDriftType),
        ("LastSuccess", TThostFtdcLastSuccessType),
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
        return self.OTPType
    
class  CThostFtdcManualSyncBrokerUserOTPField(Structure):
    """手工同步用户动态令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OTPType", c_char),
        ("FirstOTP", TThostFtdcPasswordType),
        ("SecondOTP", TThostFtdcPasswordType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getOTPType(self):
        '''动态令牌类型'''
        return self.OTPType
    def getFirstOTP(self):
        '''第一个动态密码'''
        return str(self.FirstOTP, 'GBK')
    def getSecondOTP(self):
        '''第二个动态密码'''
        return str(self.SecondOTP, 'GBK')
    
class  CThostFtdcCommRateModelField(Structure):
    """投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("CommModelName", TThostFtdcCommModelNameType),
        
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
    
class  CThostFtdcQryCommRateModelField(Structure):
    """请求查询投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getCommModelID(self):
        '''手续费率模板代码'''
        return str(self.CommModelID, 'GBK')
    
class  CThostFtdcMarginModelField(Structure):
    """投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("MarginModelName", TThostFtdcCommModelNameType),
        
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
    
class  CThostFtdcQryMarginModelField(Structure):
    """请求查询投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getMarginModelID(self):
        '''保证金率模板代码'''
        return str(self.MarginModelID, 'GBK')
    
class  CThostFtdcEWarrantOffsetField(Structure):
    """仓单折抵信息"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
        return self.Direction
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getVolume(self):
        '''数量'''
        return self.Volume
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryEWarrantOffsetField(Structure):
    """查询仓单折抵信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryInvestorProductGroupMarginField(Structure):
    """查询投资者品种/跨品种保证金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getProductGroupID(self):
        '''品种/跨品种标示'''
        return str(self.ProductGroupID, 'GBK')
    
class  CThostFtdcInvestorProductGroupMarginField(Structure):
    """投资者品种/跨品种保证金"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("LongFrozenMargin", TThostFtdcMoneyType),
        ("ShortFrozenMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("LongUseMargin", TThostFtdcMoneyType),
        ("ShortUseMargin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("LongExchMargin", TThostFtdcMoneyType),
        ("ShortExchMargin", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("OffsetAmount", TThostFtdcMoneyType),
        ("LongOffsetAmount", TThostFtdcMoneyType),
        ("ShortOffsetAmount", TThostFtdcMoneyType),
        ("ExchOffsetAmount", TThostFtdcMoneyType),
        ("LongExchOffsetAmount", TThostFtdcMoneyType),
        ("ShortExchOffsetAmount", TThostFtdcMoneyType),
        ("HedgeFlag", c_char),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
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
        return self.HedgeFlag
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getInvestUnitID(self):
        '''投资单元代码'''
        return str(self.InvestUnitID, 'GBK')
    def getProductGroupID(self):
        '''品种/跨品种标示'''
        return str(self.ProductGroupID, 'GBK')
    
class  CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
    """查询监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
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
    
class  CThostFtdcCFMMCTradingAccountTokenField(Structure):
    """监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("Token", TThostFtdcCFMMCTokenType),
        
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
    
class  CThostFtdcQryProductGroupField(Structure):
    """查询产品组"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcProductGroupField(Structure):
    """投资者品种/跨品种保证金产品组"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcBulletinField(Structure):
    """交易所公告"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradingDay", TThostFtdcDateType),
        ("BulletinID", TThostFtdcBulletinIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("NewsType", TThostFtdcNewsTypeType),
        ("NewsUrgency", TThostFtdcNewsUrgencyType),
        ("SendTime", TThostFtdcTimeType),
        ("Abstract", TThostFtdcAbstractType),
        ("ComeFrom", TThostFtdcComeFromType),
        ("Content", TThostFtdcContentType),
        ("URLLink", TThostFtdcURLLinkType),
        ("MarketID", TThostFtdcMarketIDType),
        
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
        return self.NewsUrgency
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
    
class  CThostFtdcQryBulletinField(Structure):
    """查询交易所公告"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BulletinID", TThostFtdcBulletinIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("NewsType", TThostFtdcNewsTypeType),
        ("NewsUrgency", TThostFtdcNewsUrgencyType),
        
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
        return self.NewsUrgency
    
class  CThostFtdcMulticastInstrumentField(Structure):
    """MulticastInstrument"""
    _fields_ = [
        ("TopicID", TThostFtdcInstallIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentNo", TThostFtdcInstallIDType),
        ("CodePrice", TThostFtdcPriceType),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcQryMulticastInstrumentField(Structure):
    """QryMulticastInstrument"""
    _fields_ = [
        ("TopicID", TThostFtdcInstallIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
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
    
class  CThostFtdcAppIDAuthAssignField(Structure):
    """App客户端权限分配"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
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
    
class  CThostFtdcReqOpenAccountField(Structure):
    """转帐开户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", c_char),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getCashExchangeCode(self):
        '''汇钞标志'''
        return self.CashExchangeCode
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcReqCancelAccountField(Structure):
    """转帐销户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", c_char),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getCashExchangeCode(self):
        '''汇钞标志'''
        return self.CashExchangeCode
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcReqChangeAccountField(Structure):
    """变更银行账户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("NewBankAccount", TThostFtdcBankAccountType),
        ("NewBankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccType", c_char),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", TThostFtdcTIDType),
        ("Digest", TThostFtdcDigestType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.BankAccType
    def getInstallID(self):
        '''安装编号'''
        return self.InstallID
    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
    def getTID(self):
        '''交易ID'''
        return self.TID
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcReqTransferField(Structure):
    """转账请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", c_char),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", c_char),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
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
        return self.FeePayFlag
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
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
        return self.TransferStatus
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcRspTransferField(Structure):
    """银行发起银行资金转期货响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", c_char),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", c_char),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
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
        return self.FeePayFlag
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
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
        return self.TransferStatus
    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID
    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcReqRepealField(Structure):
    """冲正请求"""
    _fields_ = [
        ("RepealTimeInterval", TThostFtdcRepealTimeIntervalType),
        ("RepealedTimes", TThostFtdcRepealedTimesType),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", TThostFtdcPlateSerialType),
        ("BankRepealSerial", TThostFtdcBankSerialType),
        ("FutureRepealSerial", TThostFtdcFutureSerialType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", c_char),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", c_char),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]

    def getRepealTimeInterval(self):
        '''冲正时间间隔'''
        return self.RepealTimeInterval
    def getRepealedTimes(self):
        '''已经冲正次数'''
        return self.RepealedTimes
    def getBankRepealFlag(self):
        '''银行冲正标志'''
        return self.BankRepealFlag
    def getBrokerRepealFlag(self):
        '''期商冲正标志'''
        return self.BrokerRepealFlag
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
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
        return self.FeePayFlag
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
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
        return self.TransferStatus
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcRspRepealField(Structure):
    """冲正响应"""
    _fields_ = [
        ("RepealTimeInterval", TThostFtdcRepealTimeIntervalType),
        ("RepealedTimes", TThostFtdcRepealedTimesType),
        ("BankRepealFlag", c_char),
        ("BrokerRepealFlag", c_char),
        ("PlateRepealSerial", TThostFtdcPlateSerialType),
        ("BankRepealSerial", TThostFtdcBankSerialType),
        ("FutureRepealSerial", TThostFtdcFutureSerialType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", c_char),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", c_char),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]

    def getRepealTimeInterval(self):
        '''冲正时间间隔'''
        return self.RepealTimeInterval
    def getRepealedTimes(self):
        '''已经冲正次数'''
        return self.RepealedTimes
    def getBankRepealFlag(self):
        '''银行冲正标志'''
        return self.BankRepealFlag
    def getBrokerRepealFlag(self):
        '''期商冲正标志'''
        return self.BrokerRepealFlag
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
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
        return self.FeePayFlag
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
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
        return self.TransferStatus
    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID
    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcReqQueryAccountField(Structure):
    """查询账户信息请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcRspQueryAccountField(Structure):
    """查询账户信息响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("BankUseAmount", TThostFtdcTradeAmountType),
        ("BankFetchAmount", TThostFtdcTradeAmountType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcFutureSignIOField(Structure):
    """期商签到签退"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcRspFutureSignInField(Structure):
    """期商签到响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("PinKey", TThostFtdcPasswordKeyType),
        ("MacKey", TThostFtdcPasswordKeyType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcReqFutureSignOutField(Structure):
    """期商签退请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcRspFutureSignOutField(Structure):
    """期商签退响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcReqQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("Reference", TThostFtdcSerialType),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", TThostFtdcOrganCodeType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("Digest", TThostFtdcDigestType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getReference(self):
        '''流水号'''
        return self.Reference
    def getRefrenceIssureType(self):
        '''本流水号发布者的机构类型'''
        return self.RefrenceIssureType
    def getRefrenceIssure(self):
        '''本流水号发布者机构编码'''
        return str(self.RefrenceIssure, 'GBK')
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
    
class  CThostFtdcRspQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("Reference", TThostFtdcSerialType),
        ("RefrenceIssureType", c_char),
        ("RefrenceIssure", TThostFtdcOrganCodeType),
        ("OriginReturnCode", TThostFtdcReturnCodeType),
        ("OriginDescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("Digest", TThostFtdcDigestType),
        
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
        return self.LastFragment
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
        return self.RefrenceIssureType
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
    
class  CThostFtdcReqDayEndFileReadyField(Structure):
    """日终文件就绪请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("FileBusinessCode", c_char),
        ("Digest", TThostFtdcDigestType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getFileBusinessCode(self):
        '''文件业务功能'''
        return self.FileBusinessCode
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    
class  CThostFtdcReturnResultField(Structure):
    """返回结果"""
    _fields_ = [
        ("ReturnCode", TThostFtdcReturnCodeType),
        ("DescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        
    ]

    def getReturnCode(self):
        '''返回代码'''
        return str(self.ReturnCode, 'GBK')
    def getDescrInfoForReturnCode(self):
        '''返回码描述'''
        return str(self.DescrInfoForReturnCode, 'GBK')
    
class  CThostFtdcVerifyFuturePasswordField(Structure):
    """验证期货资金密码"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("TID", TThostFtdcTIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcVerifyCustInfoField(Structure):
    """验证客户信息"""
    _fields_ = [
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]

    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
    
class  CThostFtdcDepositResultInformField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Deposit", TThostFtdcMoneyType),
        ("RequestID", TThostFtdcRequestIDType),
        ("ReturnCode", TThostFtdcReturnCodeType),
        ("DescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        
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
    
class  CThostFtdcReqSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcRspSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcNotifyQueryAccountField(Structure):
    """查询账户信息通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("BankUseAmount", TThostFtdcTradeAmountType),
        ("BankFetchAmount", TThostFtdcTradeAmountType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcTransferSerialField(Structure):
    """银期转账交易流水表"""
    _fields_ = [
        ("PlateSerial", TThostFtdcPlateSerialType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradingDay", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BankAccType", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("FutureAccType", c_char),
        ("AccountID", TThostFtdcAccountIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("AvailabilityFlag", c_char),
        ("OperatorCode", TThostFtdcOperatorCodeType),
        ("BankNewAccount", TThostFtdcBankAccountType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.BankAccType
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
        return self.FutureAccType
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
        return self.IdCardType
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
        return self.AvailabilityFlag
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
    
class  CThostFtdcQryTransferSerialField(Structure):
    """请求查询转帐流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcNotifyFutureSignInField(Structure):
    """期商签到通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("PinKey", TThostFtdcPasswordKeyType),
        ("MacKey", TThostFtdcPasswordKeyType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcNotifyFutureSignOutField(Structure):
    """期商签退通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcNotifySyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
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
    
class  CThostFtdcQryAccountregisterField(Structure):
    """请求查询银期签约关系"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcAccountregisterField(Structure):
    """客户开销户信息表"""
    _fields_ = [
        ("TradeDay", TThostFtdcTradeDateType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("OpenOrDestroy", c_char),
        ("RegDate", TThostFtdcTradeDateType),
        ("OutDate", TThostFtdcTradeDateType),
        ("TID", TThostFtdcTIDType),
        ("CustType", c_char),
        ("BankAccType", c_char),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.IdCardType
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
        return self.OpenOrDestroy
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
        return self.CustType
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getLongCustomerName(self):
        '''长客户姓名'''
        return str(self.LongCustomerName, 'GBK')
    
class  CThostFtdcOpenAccountField(Structure):
    """银期开户信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", c_char),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getCashExchangeCode(self):
        '''汇钞标志'''
        return self.CashExchangeCode
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcCancelAccountField(Structure):
    """银期销户信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", c_char),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getCashExchangeCode(self):
        '''汇钞标志'''
        return self.CashExchangeCode
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getDeviceID(self):
        '''渠道标志'''
        return str(self.DeviceID, 'GBK')
    def getBankSecuAccType(self):
        '''期货单位帐号类型'''
        return self.BankSecuAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankSecuAcc(self):
        '''期货单位帐号'''
        return str(self.BankSecuAcc, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcChangeAccountField(Structure):
    """银期变更银行账号信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("NewBankAccount", TThostFtdcBankAccountType),
        ("NewBankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccType", c_char),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankPwdFlag", c_char),
        ("SecuPwdFlag", c_char),
        ("TID", TThostFtdcTIDType),
        ("Digest", TThostFtdcDigestType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.BankAccType
    def getInstallID(self):
        '''安装编号'''
        return self.InstallID
    def getVerifyCertNoFlag(self):
        '''验证客户证件号码标志'''
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getBankPwdFlag(self):
        '''银行密码标志'''
        return self.BankPwdFlag
    def getSecuPwdFlag(self):
        '''期货资金密码核对标志'''
        return self.SecuPwdFlag
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
    
class  CThostFtdcSecAgentACIDMapField(Structure):
    """二级代理操作员银期权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        
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
    
class  CThostFtdcQrySecAgentACIDMapField(Structure):
    """二级代理操作员银期权限查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcUserRightsAssignField(Structure):
    """灾备中心交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
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
    
class  CThostFtdcBrokerUserRightAssignField(Structure):
    """经济公司是否有在本标示的交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        ("Tradeable", TThostFtdcBoolType),
        
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
    
class  CThostFtdcDRTransferField(Structure):
    """灾备交易转换报文"""
    _fields_ = [
        ("OrigDRIdentityID", TThostFtdcDRIdentityIDType),
        ("DestDRIdentityID", TThostFtdcDRIdentityIDType),
        ("OrigBrokerID", TThostFtdcBrokerIDType),
        ("DestBrokerID", TThostFtdcBrokerIDType),
        
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
    
class  CThostFtdcFensUserInfoField(Structure):
    """Fens用户信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
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
        return self.LoginMode
    
class  CThostFtdcCurrTransferIdentityField(Structure):
    """当前银期所属交易中心"""
    _fields_ = [
        ("IdentityID", TThostFtdcDRIdentityIDType),
        
    ]

    def getIdentityID(self):
        '''交易中心代码'''
        return self.IdentityID
    
class  CThostFtdcLoginForbiddenUserField(Structure):
    """禁止登录用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcQryLoginForbiddenUserField(Structure):
    """查询禁止登录用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcTradingAccountReserveField(Structure):
    """资金账户基本准备金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Reserve", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
    
class  CThostFtdcQryLoginForbiddenIPField(Structure):
    """查询禁止登录IP"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    
class  CThostFtdcQryIPListField(Structure):
    """查询IP列表"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getreserve1(self):
        '''保留的无效字段'''
        return str(self.reserve1, 'GBK')
    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    
class  CThostFtdcQryUserRightsAssignField(Structure):
    """查询用户下单权限分配表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]

    def getBrokerID(self):
        '''应用单元代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    
class  CThostFtdcReserveOpenAccountConfirmField(Structure):
    """银期预约开户确认请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcLongIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("TID", TThostFtdcTIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankReserveOpenSeq", TThostFtdcBankSerialType),
        ("BookDate", TThostFtdcTradeDateType),
        ("BookPsw", TThostFtdcPasswordType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
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
    
class  CThostFtdcReserveOpenAccountField(Structure):
    """银期预约开户"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", c_char),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcLongIndividualNameType),
        ("IdCardType", c_char),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", c_char),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", c_char),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", c_char),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", c_char),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", c_char),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("TID", TThostFtdcTIDType),
        ("ReserveOpenAccStas", c_char),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
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
        return self.LastFragment
    def getSessionID(self):
        '''会话号'''
        return self.SessionID
    def getCustomerName(self):
        '''客户姓名'''
        return str(self.CustomerName, 'GBK')
    def getIdCardType(self):
        '''证件类型'''
        return self.IdCardType
    def getIdentifiedCardNo(self):
        '''证件号码'''
        return str(self.IdentifiedCardNo, 'GBK')
    def getGender(self):
        '''性别'''
        return self.Gender
    def getCountryCode(self):
        '''国家代码'''
        return str(self.CountryCode, 'GBK')
    def getCustType(self):
        '''客户类型'''
        return self.CustType
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
        return self.MoneyAccountStatus
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
        return self.VerifyCertNoFlag
    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')
    def getDigest(self):
        '''摘要'''
        return str(self.Digest, 'GBK')
    def getBankAccType(self):
        '''银行帐号类型'''
        return self.BankAccType
    def getBrokerIDByBank(self):
        '''期货公司银行编码'''
        return str(self.BrokerIDByBank, 'GBK')
    def getTID(self):
        '''交易ID'''
        return self.TID
    def getReserveOpenAccStas(self):
        '''预约开户状态'''
        return self.ReserveOpenAccStas
    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID
    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')
    
class  CThostFtdcAccountPropertyField(Structure):
    """银行账户属性"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("OpenName", TThostFtdcInvestorFullNameType),
        ("OpenBank", TThostFtdcOpenBankType),
        ("IsActive", TThostFtdcBoolType),
        ("AccountSourceType", c_char),
        ("OpenDate", TThostFtdcDateType),
        ("CancelDate", TThostFtdcDateType),
        ("OperatorID", TThostFtdcOperatorIDType),
        ("OperateDate", TThostFtdcDateType),
        ("OperateTime", TThostFtdcTimeType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
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
        return self.AccountSourceType
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
    
class  CThostFtdcQryCurrDRIdentityField(Structure):
    """查询当前交易中心"""
    _fields_ = [
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID
    
class  CThostFtdcCurrDRIdentityField(Structure):
    """当前交易中心"""
    _fields_ = [
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]

    def getDRIdentityID(self):
        '''交易中心代码'''
        return self.DRIdentityID
    
class  CThostFtdcQrySecAgentCheckModeField(Structure):
    """查询二级代理商资金校验模式"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcQrySecAgentTradeInfoField(Structure):
    """查询二级代理商信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getBrokerSecAgentID(self):
        '''境外中介机构资金帐号'''
        return str(self.BrokerSecAgentID, 'GBK')
    
class  CThostFtdcReqUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
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
    
class  CThostFtdcRspUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法回复"""
    _fields_ = [
        ("UsableAuthMethod", TThostFtdcCurrentAuthMethodType),
        
    ]

    def getUsableAuthMethod(self):
        '''当前可以用的认证模式'''
        return self.UsableAuthMethod
    
class  CThostFtdcReqGenUserCaptchaField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
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
    
class  CThostFtdcRspGenUserCaptchaField(Structure):
    """生成的图片验证码信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("CaptchaInfoLen", TThostFtdcCaptchaInfoLenType),
        ("CaptchaInfo", TThostFtdcCaptchaInfoType),
        
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
    
class  CThostFtdcReqGenUserTextField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
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
    
class  CThostFtdcRspGenUserTextField(Structure):
    """短信验证码生成的回复"""
    _fields_ = [
        ("UserTextSeq", TThostFtdcUserTextSeqType),
        
    ]

    def getUserTextSeq(self):
        '''短信验证码序号'''
        return self.UserTextSeq
    
class  CThostFtdcReqUserLoginWithCaptchaField(Structure):
    """用户发出带图形验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Captcha", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcReqUserLoginWithTextField(Structure):
    """用户发出带短信验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Text", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcReqUserLoginWithOTPField(Structure):
    """用户发出带动态验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("OTPPassword", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcReqApiHandshakeField(Structure):
    """api握手请求"""
    _fields_ = [
        ("CryptoKeyVersion", TThostFtdcCryptoKeyVersionType),
        
    ]

    def getCryptoKeyVersion(self):
        '''api与front通信密钥版本号'''
        return str(self.CryptoKeyVersion, 'GBK')
    
class  CThostFtdcRspApiHandshakeField(Structure):
    """front发给api的握手回复"""
    _fields_ = [
        ("FrontHandshakeDataLen", TThostFtdcHandshakeDataLenType),
        ("FrontHandshakeData", TThostFtdcHandshakeDataType),
        ("IsApiAuthEnabled", TThostFtdcBoolType),
        
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
    
class  CThostFtdcReqVerifyApiKeyField(Structure):
    """api给front的验证key的请求"""
    _fields_ = [
        ("ApiHandshakeDataLen", TThostFtdcHandshakeDataLenType),
        ("ApiHandshakeData", TThostFtdcHandshakeDataType),
        
    ]

    def getApiHandshakeDataLen(self):
        '''握手回复数据长度'''
        return self.ApiHandshakeDataLen
    def getApiHandshakeData(self):
        '''握手回复数据'''
        return str(self.ApiHandshakeData, 'GBK')
    
class  CThostFtdcDepartmentUserField(Structure):
    """操作员组织架构关系"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("InvestorRange", c_char),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    
class  CThostFtdcQueryFreqField(Structure):
    """查询频率，每秒查询比数"""
    _fields_ = [
        ("QueryFreq", TThostFtdcQueryFreqType),
        
    ]

    def getQueryFreq(self):
        '''查询频率'''
        return self.QueryFreq
    
class  CThostFtdcAuthForbiddenIPField(Structure):
    """禁止认证IP"""
    _fields_ = [
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    
class  CThostFtdcQryAuthForbiddenIPField(Structure):
    """查询禁止认证IP"""
    _fields_ = [
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')
    
class  CThostFtdcSyncDelaySwapFrozenField(Structure):
    """换汇可提冻结"""
    _fields_ = [
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromRemainSwap", TThostFtdcMoneyType),
        ("IsManualSwap", TThostFtdcBoolType),
        
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
    
class  CThostFtdcUserSystemInfoField(Structure):
    """用户系统信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ClientSystemInfoLen", TThostFtdcSystemInfoLenType),
        ("ClientSystemInfo", TThostFtdcClientSystemInfoType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientLoginTime", TThostFtdcTimeType),
        ("ClientAppID", TThostFtdcAppIDType),
        ("ClientPublicIP", TThostFtdcIPAddressType),
        ("ClientLoginRemark", TThostFtdcClientLoginRemarkType),
        
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
    def getClientLoginRemark(self):
        '''客户登录备注2'''
        return str(self.ClientLoginRemark, 'GBK')
    
class  CThostFtdcAuthUserIDField(Structure):
    """终端用户绑定信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("UserID", TThostFtdcUserIDType),
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
        return self.AuthType
    
class  CThostFtdcAuthIPField(Structure):
    """用户IP绑定信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
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
    
class  CThostFtdcQryClassifiedInstrumentField(Structure):
    """查询分类合约"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
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
        return self.TradingType
    def getClassType(self):
        '''合约分类类型'''
        return self.ClassType
    
class  CThostFtdcQryCombPromotionParamField(Structure):
    """查询组合优惠比例"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcCombPromotionParamField(Structure):
    """组合优惠比例"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("Xparameter", TThostFtdcDiscountRatioType),
        
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
    
class  CThostFtdcReqUserLoginSCField(Structure):
    """国密用户登录请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("AuthCode", TThostFtdcAuthCodeType),
        ("AppID", TThostFtdcAppIDType),
        
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
    def getClientIPAddress(self):
        '''终端IP地址'''
        return str(self.ClientIPAddress, 'GBK')
    def getLoginRemark(self):
        '''登录备注'''
        return str(self.LoginRemark, 'GBK')
    def getClientIPPort(self):
        '''终端IP端口'''
        return self.ClientIPPort
    def getAuthCode(self):
        '''认证码'''
        return str(self.AuthCode, 'GBK')
    def getAppID(self):
        '''App代码'''
        return str(self.AppID, 'GBK')
    
class  CThostFtdcQryRiskSettleInvstPositionField(Structure):
    """投资者风险结算持仓查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    
class  CThostFtdcQryRiskSettleProductStatusField(Structure):
    """风险结算产品查询"""
    _fields_ = [
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')
    
class  CThostFtdcRiskSettleInvstPositionField(Structure):
    """投资者风险结算持仓"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", c_char),
        ("HedgeFlag", c_char),
        ("PositionDate", c_char),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getPosiDirection(self):
        '''持仓多空方向'''
        return self.PosiDirection
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getPositionDate(self):
        '''持仓日期'''
        return self.PositionDate
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
        '''持仓成本差值'''
        return self.PositionCostOffset
    def getTasPosition(self):
        '''tas持仓手数'''
        return self.TasPosition
    def getTasPositionCost(self):
        '''tas持仓成本'''
        return self.TasPositionCost
    
class  CThostFtdcRiskSettleProductStatusField(Structure):
    """风险品种"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductStatus", c_char),
        
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getProductID(self):
        '''产品编号'''
        return str(self.ProductID, 'GBK')
    def getProductStatus(self):
        '''产品结算状态'''
        return self.ProductStatus
    
class  CThostFtdcSyncDeltaInfoField(Structure):
    """风险结算追平信息"""
    _fields_ = [
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        ("SyncDeltaStatus", c_char),
        ("SyncDescription", TThostFtdcSyncDescriptionType),
        ("IsOnlyTrdDelta", TThostFtdcBoolType),
        
    ]

    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    def getSyncDeltaStatus(self):
        '''追平状态'''
        return self.SyncDeltaStatus
    def getSyncDescription(self):
        '''追平描述'''
        return str(self.SyncDescription, 'GBK')
    def getIsOnlyTrdDelta(self):
        '''是否只有资金追平'''
        return self.IsOnlyTrdDelta
    
class  CThostFtdcSyncDeltaProductStatusField(Structure):
    """风险结算追平产品信息"""
    _fields_ = [
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductStatus", c_char),
        
    ]

    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')
    def getProductStatus(self):
        '''是否允许交易'''
        return self.ProductStatus
    
class  CThostFtdcSyncDeltaInvstPosDtlField(Structure):
    """风险结算追平持仓明细"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("OpenDate", TThostFtdcDateType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Volume", TThostFtdcVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("TradeType", c_char),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("PositionProfitByDate", TThostFtdcMoneyType),
        ("PositionProfitByTrade", TThostFtdcMoneyType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LastSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("TimeFirstVolume", TThostFtdcVolumeType),
        ("SpecPosiType", c_char),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getDirection(self):
        '''买卖'''
        return self.Direction
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
        return self.TradeType
    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')
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
        '''先开先平剩余数量'''
        return self.TimeFirstVolume
    def getSpecPosiType(self):
        '''特殊持仓标志'''
        return self.SpecPosiType
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaInvstPosCombDtlField(Structure):
    """风险结算追平组合持仓明细"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("HedgeFlag", c_char),
        ("Direction", c_char),
        ("TotalAmt", TThostFtdcVolumeType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LegID", TThostFtdcLegIDType),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
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
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getDirection(self):
        '''买卖'''
        return self.Direction
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
    def getTradeGroupID(self):
        '''成交组号'''
        return self.TradeGroupID
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaTradingAccountField(Structure):
    """风险结算追平资金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
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
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaInitInvstMarginField(Structure):
    """投资者风险结算总保证金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("LastRiskTotalInvstMargin", TThostFtdcMoneyType),
        ("LastRiskTotalExchMargin", TThostFtdcMoneyType),
        ("ThisSyncInvstMargin", TThostFtdcMoneyType),
        ("ThisSyncExchMargin", TThostFtdcMoneyType),
        ("RemainRiskInvstMargin", TThostFtdcMoneyType),
        ("RemainRiskExchMargin", TThostFtdcMoneyType),
        ("LastRiskSpecTotalInvstMargin", TThostFtdcMoneyType),
        ("LastRiskSpecTotalExchMargin", TThostFtdcMoneyType),
        ("ThisSyncSpecInvstMargin", TThostFtdcMoneyType),
        ("ThisSyncSpecExchMargin", TThostFtdcMoneyType),
        ("RemainRiskSpecInvstMargin", TThostFtdcMoneyType),
        ("RemainRiskSpecExchMargin", TThostFtdcMoneyType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getLastRiskTotalInvstMargin(self):
        '''追平前总风险保证金'''
        return self.LastRiskTotalInvstMargin
    def getLastRiskTotalExchMargin(self):
        '''追平前交易所总风险保证金'''
        return self.LastRiskTotalExchMargin
    def getThisSyncInvstMargin(self):
        '''本次追平品种总保证金'''
        return self.ThisSyncInvstMargin
    def getThisSyncExchMargin(self):
        '''本次追平品种交易所总保证金'''
        return self.ThisSyncExchMargin
    def getRemainRiskInvstMargin(self):
        '''本次未追平品种总保证金'''
        return self.RemainRiskInvstMargin
    def getRemainRiskExchMargin(self):
        '''本次未追平品种交易所总保证金'''
        return self.RemainRiskExchMargin
    def getLastRiskSpecTotalInvstMargin(self):
        '''追平前总特殊产品风险保证金'''
        return self.LastRiskSpecTotalInvstMargin
    def getLastRiskSpecTotalExchMargin(self):
        '''追平前总特殊产品交易所风险保证金'''
        return self.LastRiskSpecTotalExchMargin
    def getThisSyncSpecInvstMargin(self):
        '''本次追平品种特殊产品总保证金'''
        return self.ThisSyncSpecInvstMargin
    def getThisSyncSpecExchMargin(self):
        '''本次追平品种特殊产品交易所总保证金'''
        return self.ThisSyncSpecExchMargin
    def getRemainRiskSpecInvstMargin(self):
        '''本次未追平品种特殊产品总保证金'''
        return self.RemainRiskSpecInvstMargin
    def getRemainRiskSpecExchMargin(self):
        '''本次未追平品种特殊产品交易所总保证金'''
        return self.RemainRiskSpecExchMargin
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaDceCombInstrumentField(Structure):
    """风险结算追平组合优先级"""
    _fields_ = [
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("CombHedgeFlag", c_char),
        ("CombinationType", c_char),
        ("Direction", c_char),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("Xparameter", TThostFtdcDiscountRatioType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getCombInstrumentID(self):
        '''合约代码'''
        return str(self.CombInstrumentID, 'GBK')
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
    def getTradeGroupID(self):
        '''成交组号'''
        return self.TradeGroupID
    def getCombHedgeFlag(self):
        '''投机套保标志'''
        return self.CombHedgeFlag
    def getCombinationType(self):
        '''组合类型'''
        return self.CombinationType
    def getDirection(self):
        '''买卖'''
        return self.Direction
    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')
    def getXparameter(self):
        '''期权组合保证金比例'''
        return self.Xparameter
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaInvstMarginRateField(Structure):
    """风险结算追平投资者期货保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaExchMarginRateField(Structure):
    """风险结算追平交易所期货保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaOptExchMarginField(Structure):
    """风险结算追平中金现货期权交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
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
    def getMShortMarginRatioByMoney(self):
        '''做市商空头保证金调整系数'''
        return self.MShortMarginRatioByMoney
    def getMShortMarginRatioByVolume(self):
        '''做市商空头保证金调整系数'''
        return self.MShortMarginRatioByVolume
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaOptInvstMarginField(Structure):
    """风险结算追平中金现货期权投资者保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaInvstMarginRateULField(Structure):
    """风险结算追平期权标的调整保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", c_char),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInvestorID(self):
        '''投资者代码'''
        return str(self.InvestorID, 'GBK')
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaOptInvstCommRateField(Structure):
    """风险结算追平期权手续费率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaInvstCommRateField(Structure):
    """风险结算追平期货手续费率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", c_char),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getInvestorRange(self):
        '''投资者范围'''
        return self.InvestorRange
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
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaProductExchRateField(Structure):
    """风险结算追平交叉汇率"""
    _fields_ = [
        ("ProductID", TThostFtdcInstrumentIDType),
        ("QuoteCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')
    def getQuoteCurrencyID(self):
        '''报价币种类型'''
        return str(self.QuoteCurrencyID, 'GBK')
    def getExchangeRate(self):
        '''汇率'''
        return self.ExchangeRate
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaDepthMarketDataField(Structure):
    """风险结算追平行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        ("AveragePrice", TThostFtdcPriceType),
        ("ActionDay", TThostFtdcDateType),
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')
    def getExchangeInstID(self):
        '''合约在交易所的代码'''
        return str(self.ExchangeInstID, 'GBK')
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
    def getBandingUpperPrice(self):
        '''上带价'''
        return self.BandingUpperPrice
    def getBandingLowerPrice(self):
        '''下带价'''
        return self.BandingLowerPrice
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaIndexPriceField(Structure):
    """风险结算追平现货指数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ClosePrice", TThostFtdcPriceType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]

    def getBrokerID(self):
        '''经纪公司代码'''
        return str(self.BrokerID, 'GBK')
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getClosePrice(self):
        '''指数现货收盘价'''
        return self.ClosePrice
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    
class  CThostFtdcSyncDeltaEWarrantOffsetField(Structure):
    """风险结算追平仓单折抵"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("Volume", TThostFtdcVolumeType),
        ("ActionDirection", c_char),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
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
    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')
    def getDirection(self):
        '''买卖方向'''
        return self.Direction
    def getHedgeFlag(self):
        '''投机套保标志'''
        return self.HedgeFlag
    def getVolume(self):
        '''数量'''
        return self.Volume
    def getActionDirection(self):
        '''操作标志'''
        return self.ActionDirection
    def getSyncDeltaSequenceNo(self):
        '''追平序号'''
        return self.SyncDeltaSequenceNo
    