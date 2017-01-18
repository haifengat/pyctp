#!/usr/bin/env python
#coding:utf-8
from ctypes import *
from py_ctp.ctp_enum import *

class CThostFtdcDisseminationField(Structure):
	"""信息分发"""
	_fields_ = [
		#序列系列号
		("SequenceSeries",c_int32),
		#序列号
		("SequenceNo",c_int32),
		]

	def getSequenceSeries(self):
		return self.SequenceSeries
	def getSequenceNo(self):
		return self.SequenceNo

	def __str__(self):
		return 'SequenceSeries={0}, SequenceNo={1}'.format(self.SequenceSeries, self.SequenceNo)

	@property
	def __dict__(self):
		return {'SequenceSeries':self.SequenceSeries,'SequenceNo':self.SequenceNo}

	def clone(self):
		obj=CThostFtdcDisseminationField()
		obj.SequenceSeries=self.SequenceSeries
		obj.SequenceNo=self.SequenceNo
		return obj

class CThostFtdcReqUserLoginField(Structure):
	"""用户登录请求"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#密码
		("Password",c_char*41),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#Mac地址
		("MacAddress",c_char*21),
		#动态密码
		("OneTimePassword",c_char*41),
		#终端IP地址
		("ClientIPAddress",c_char*16),
		#登录备注
		("LoginRemark",c_char*36),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getInterfaceProductInfo(self):
		return str(self.InterfaceProductInfo, 'GB2312')
	def getProtocolInfo(self):
		return str(self.ProtocolInfo, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getOneTimePassword(self):
		return str(self.OneTimePassword, 'GB2312')
	def getClientIPAddress(self):
		return str(self.ClientIPAddress, 'GB2312')
	def getLoginRemark(self):
		return str(self.LoginRemark, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', BrokerID=\'{1}\', UserID=\'{2}\', Password=\'{3}\', UserProductInfo=\'{4}\', InterfaceProductInfo=\'{5}\', ProtocolInfo=\'{6}\', MacAddress=\'{7}\', OneTimePassword=\'{8}\', ClientIPAddress=\'{9}\', LoginRemark=\'{10}\''.format(str(self.TradingDay, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.Password, 'GB2312'), str(self.UserProductInfo, 'GB2312'), str(self.InterfaceProductInfo, 'GB2312'), str(self.ProtocolInfo, 'GB2312'), str(self.MacAddress, 'GB2312'), str(self.OneTimePassword, 'GB2312'), str(self.ClientIPAddress, 'GB2312'), str(self.LoginRemark, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'InterfaceProductInfo':str(self.InterfaceProductInfo, 'GB2312'),'ProtocolInfo':str(self.ProtocolInfo, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'OneTimePassword':str(self.OneTimePassword, 'GB2312'),'ClientIPAddress':str(self.ClientIPAddress, 'GB2312'),'LoginRemark':str(self.LoginRemark, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqUserLoginField()
		obj.TradingDay=self.TradingDay
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.Password=self.Password
		obj.UserProductInfo=self.UserProductInfo
		obj.InterfaceProductInfo=self.InterfaceProductInfo
		obj.ProtocolInfo=self.ProtocolInfo
		obj.MacAddress=self.MacAddress
		obj.OneTimePassword=self.OneTimePassword
		obj.ClientIPAddress=self.ClientIPAddress
		obj.LoginRemark=self.LoginRemark
		return obj

class CThostFtdcRspUserLoginField(Structure):
	"""用户登录应答"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#登录成功时间
		("LoginTime",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#交易系统名称
		("SystemName",c_char*41),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#最大报单引用
		("MaxOrderRef",c_char*13),
		#上期所时间
		("SHFETime",c_char*9),
		#大商所时间
		("DCETime",c_char*9),
		#郑商所时间
		("CZCETime",c_char*9),
		#中金所时间
		("FFEXTime",c_char*9),
		#能源中心时间
		("INETime",c_char*9),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getLoginTime(self):
		return str(self.LoginTime, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getSystemName(self):
		return str(self.SystemName, 'GB2312')
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getMaxOrderRef(self):
		return str(self.MaxOrderRef, 'GB2312')
	def getSHFETime(self):
		return str(self.SHFETime, 'GB2312')
	def getDCETime(self):
		return str(self.DCETime, 'GB2312')
	def getCZCETime(self):
		return str(self.CZCETime, 'GB2312')
	def getFFEXTime(self):
		return str(self.FFEXTime, 'GB2312')
	def getINETime(self):
		return str(self.INETime, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', LoginTime=\'{1}\', BrokerID=\'{2}\', UserID=\'{3}\', SystemName=\'{4}\', FrontID={5}, SessionID={6}, MaxOrderRef=\'{7}\', SHFETime=\'{8}\', DCETime=\'{9}\', CZCETime=\'{10}\', FFEXTime=\'{11}\', INETime=\'{12}\''.format(str(self.TradingDay, 'GB2312'), str(self.LoginTime, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.SystemName, 'GB2312'), self.FrontID, self.SessionID, str(self.MaxOrderRef, 'GB2312'), str(self.SHFETime, 'GB2312'), str(self.DCETime, 'GB2312'), str(self.CZCETime, 'GB2312'), str(self.FFEXTime, 'GB2312'), str(self.INETime, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'LoginTime':str(self.LoginTime, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'SystemName':str(self.SystemName, 'GB2312'),'FrontID':self.FrontID,'SessionID':self.SessionID,'MaxOrderRef':str(self.MaxOrderRef, 'GB2312'),'SHFETime':str(self.SHFETime, 'GB2312'),'DCETime':str(self.DCETime, 'GB2312'),'CZCETime':str(self.CZCETime, 'GB2312'),'FFEXTime':str(self.FFEXTime, 'GB2312'),'INETime':str(self.INETime, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspUserLoginField()
		obj.TradingDay=self.TradingDay
		obj.LoginTime=self.LoginTime
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.SystemName=self.SystemName
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.MaxOrderRef=self.MaxOrderRef
		obj.SHFETime=self.SHFETime
		obj.DCETime=self.DCETime
		obj.CZCETime=self.CZCETime
		obj.FFEXTime=self.FFEXTime
		obj.INETime=self.INETime
		return obj

class CThostFtdcUserLogoutField(Structure):
	"""用户登出请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcUserLogoutField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcForceUserLogoutField(Structure):
	"""强制交易员退出"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcForceUserLogoutField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcReqAuthenticateField(Structure):
	"""客户端认证请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#认证码
		("AuthCode",c_char*17),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getAuthCode(self):
		return str(self.AuthCode, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserProductInfo=\'{2}\', AuthCode=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.UserProductInfo, 'GB2312'), str(self.AuthCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'AuthCode':str(self.AuthCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqAuthenticateField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserProductInfo=self.UserProductInfo
		obj.AuthCode=self.AuthCode
		return obj

class CThostFtdcRspAuthenticateField(Structure):
	"""客户端认证响应"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserProductInfo=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.UserProductInfo, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspAuthenticateField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserProductInfo=self.UserProductInfo
		return obj

class CThostFtdcAuthenticationInfoField(Structure):
	"""客户端认证信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#认证信息
		("AuthInfo",c_char*129),
		#是否为认证结果
		("IsResult",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getAuthInfo(self):
		return str(self.AuthInfo, 'GB2312')
	def getIsResult(self):
		return self.IsResult

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserProductInfo=\'{2}\', AuthInfo=\'{3}\', IsResult={4}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.UserProductInfo, 'GB2312'), str(self.AuthInfo, 'GB2312'), self.IsResult)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'AuthInfo':str(self.AuthInfo, 'GB2312'),'IsResult':self.IsResult}

	def clone(self):
		obj=CThostFtdcAuthenticationInfoField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserProductInfo=self.UserProductInfo
		obj.AuthInfo=self.AuthInfo
		obj.IsResult=self.IsResult
		return obj

class CThostFtdcTransferHeaderField(Structure):
	"""银期转帐报文头"""
	_fields_ = [
		#版本号，常量，1.0
		("Version",c_char*4),
		#交易代码，必填
		("TradeCode",c_char*7),
		#交易日期，必填，格式：yyyymmdd
		("TradeDate",c_char*9),
		#交易时间，必填，格式：hhmmss
		("TradeTime",c_char*9),
		#发起方流水号，N/A
		("TradeSerial",c_char*9),
		#期货公司代码，必填
		("FutureID",c_char*11),
		#银行代码，根据查询银行得到，必填
		("BankID",c_char*4),
		#银行分中心代码，根据查询银行得到，必填
		("BankBrchID",c_char*5),
		#操作员，N/A
		("OperNo",c_char*17),
		#交易设备类型，N/A
		("DeviceID",c_char*3),
		#记录数，N/A
		("RecordNum",c_char*7),
		#会话编号，N/A
		("SessionID",c_int32),
		#请求编号，N/A
		("RequestID",c_int32),
		]

	def getVersion(self):
		return str(self.Version, 'GB2312')
	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getTradeSerial(self):
		return str(self.TradeSerial, 'GB2312')
	def getFutureID(self):
		return str(self.FutureID, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getRecordNum(self):
		return str(self.RecordNum, 'GB2312')
	def getSessionID(self):
		return self.SessionID
	def getRequestID(self):
		return self.RequestID

	def __str__(self):
		return 'Version=\'{0}\', TradeCode=\'{1}\', TradeDate=\'{2}\', TradeTime=\'{3}\', TradeSerial=\'{4}\', FutureID=\'{5}\', BankID=\'{6}\', BankBrchID=\'{7}\', OperNo=\'{8}\', DeviceID=\'{9}\', RecordNum=\'{10}\', SessionID={11}, RequestID={12}'.format(str(self.Version, 'GB2312'), str(self.TradeCode, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.TradeSerial, 'GB2312'), str(self.FutureID, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'), str(self.OperNo, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.RecordNum, 'GB2312'), self.SessionID, self.RequestID)

	@property
	def __dict__(self):
		return {'Version':str(self.Version, 'GB2312'),'TradeCode':str(self.TradeCode, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'TradeSerial':str(self.TradeSerial, 'GB2312'),'FutureID':str(self.FutureID, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'RecordNum':str(self.RecordNum, 'GB2312'),'SessionID':self.SessionID,'RequestID':self.RequestID}

	def clone(self):
		obj=CThostFtdcTransferHeaderField()
		obj.Version=self.Version
		obj.TradeCode=self.TradeCode
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.TradeSerial=self.TradeSerial
		obj.FutureID=self.FutureID
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		obj.OperNo=self.OperNo
		obj.DeviceID=self.DeviceID
		obj.RecordNum=self.RecordNum
		obj.SessionID=self.SessionID
		obj.RequestID=self.RequestID
		return obj

class CThostFtdcTransferBankToFutureReqField(Structure):
	"""银行资金转期货请求，TradeCode=202001"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#转账金额
		("TradeAmt",c_double),
		#客户手续费
		("CustFee",c_double),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return str(self.FutureAccPwd, 'GB2312')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'FutureAccount=\'{0}\', FuturePwdFlag=FuturePwdFlagType.{1}, FutureAccPwd=\'{2}\', TradeAmt={3}, CustFee={4}, CurrencyCode=\'{5}\''.format(str(self.FutureAccount, 'GB2312'), '' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name, str(self.FutureAccPwd, 'GB2312'), self.TradeAmt, self.CustFee, str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'FutureAccount':str(self.FutureAccount, 'GB2312'),'FuturePwdFlag':'' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name,'FutureAccPwd':str(self.FutureAccPwd, 'GB2312'),'TradeAmt':self.TradeAmt,'CustFee':self.CustFee,'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferBankToFutureReqField()
		obj.FutureAccount=self.FutureAccount
		obj.FuturePwdFlag=self.FuturePwdFlag
		obj.FutureAccPwd=self.FutureAccPwd
		obj.TradeAmt=self.TradeAmt
		obj.CustFee=self.CustFee
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferBankToFutureRspField(Structure):
	"""银行资金转期货请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#转帐金额
		("TradeAmt",c_double),
		#应收客户手续费
		("CustFee",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return str(self.RetCode, 'GB2312')
	def getRetInfo(self):
		return str(self.RetInfo, 'GB2312')
	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'RetCode=\'{0}\', RetInfo=\'{1}\', FutureAccount=\'{2}\', TradeAmt={3}, CustFee={4}, CurrencyCode=\'{5}\''.format(str(self.RetCode, 'GB2312'), str(self.RetInfo, 'GB2312'), str(self.FutureAccount, 'GB2312'), self.TradeAmt, self.CustFee, str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'RetCode':str(self.RetCode, 'GB2312'),'RetInfo':str(self.RetInfo, 'GB2312'),'FutureAccount':str(self.FutureAccount, 'GB2312'),'TradeAmt':self.TradeAmt,'CustFee':self.CustFee,'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferBankToFutureRspField()
		obj.RetCode=self.RetCode
		obj.RetInfo=self.RetInfo
		obj.FutureAccount=self.FutureAccount
		obj.TradeAmt=self.TradeAmt
		obj.CustFee=self.CustFee
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferFutureToBankReqField(Structure):
	"""期货资金转银行请求，TradeCode=202002"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#转账金额
		("TradeAmt",c_double),
		#客户手续费
		("CustFee",c_double),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return str(self.FutureAccPwd, 'GB2312')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'FutureAccount=\'{0}\', FuturePwdFlag=FuturePwdFlagType.{1}, FutureAccPwd=\'{2}\', TradeAmt={3}, CustFee={4}, CurrencyCode=\'{5}\''.format(str(self.FutureAccount, 'GB2312'), '' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name, str(self.FutureAccPwd, 'GB2312'), self.TradeAmt, self.CustFee, str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'FutureAccount':str(self.FutureAccount, 'GB2312'),'FuturePwdFlag':'' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name,'FutureAccPwd':str(self.FutureAccPwd, 'GB2312'),'TradeAmt':self.TradeAmt,'CustFee':self.CustFee,'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferFutureToBankReqField()
		obj.FutureAccount=self.FutureAccount
		obj.FuturePwdFlag=self.FuturePwdFlag
		obj.FutureAccPwd=self.FutureAccPwd
		obj.TradeAmt=self.TradeAmt
		obj.CustFee=self.CustFee
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferFutureToBankRspField(Structure):
	"""期货资金转银行请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#转帐金额
		("TradeAmt",c_double),
		#应收客户手续费
		("CustFee",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return str(self.RetCode, 'GB2312')
	def getRetInfo(self):
		return str(self.RetInfo, 'GB2312')
	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getTradeAmt(self):
		return self.TradeAmt
	def getCustFee(self):
		return self.CustFee
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'RetCode=\'{0}\', RetInfo=\'{1}\', FutureAccount=\'{2}\', TradeAmt={3}, CustFee={4}, CurrencyCode=\'{5}\''.format(str(self.RetCode, 'GB2312'), str(self.RetInfo, 'GB2312'), str(self.FutureAccount, 'GB2312'), self.TradeAmt, self.CustFee, str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'RetCode':str(self.RetCode, 'GB2312'),'RetInfo':str(self.RetInfo, 'GB2312'),'FutureAccount':str(self.FutureAccount, 'GB2312'),'TradeAmt':self.TradeAmt,'CustFee':self.CustFee,'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferFutureToBankRspField()
		obj.RetCode=self.RetCode
		obj.RetInfo=self.RetInfo
		obj.FutureAccount=self.FutureAccount
		obj.TradeAmt=self.TradeAmt
		obj.CustFee=self.CustFee
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferQryBankReqField(Structure):
	"""查询银行资金请求，TradeCode=204002"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		#密码标志
		("FuturePwdFlag",c_char),
		#密码
		("FutureAccPwd",c_char*17),
		#币种：RMB-人民币 USD-美圆 HKD-港元
		("CurrencyCode",c_char*4),
		]

	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getFuturePwdFlag(self):
		return FuturePwdFlagType(ord(self.FuturePwdFlag))
	def getFutureAccPwd(self):
		return str(self.FutureAccPwd, 'GB2312')
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'FutureAccount=\'{0}\', FuturePwdFlag=FuturePwdFlagType.{1}, FutureAccPwd=\'{2}\', CurrencyCode=\'{3}\''.format(str(self.FutureAccount, 'GB2312'), '' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name, str(self.FutureAccPwd, 'GB2312'), str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'FutureAccount':str(self.FutureAccount, 'GB2312'),'FuturePwdFlag':'' if ord(self.FuturePwdFlag) == 0 else FuturePwdFlagType(ord(self.FuturePwdFlag)).name,'FutureAccPwd':str(self.FutureAccPwd, 'GB2312'),'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferQryBankReqField()
		obj.FutureAccount=self.FutureAccount
		obj.FuturePwdFlag=self.FuturePwdFlag
		obj.FutureAccPwd=self.FutureAccPwd
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferQryBankRspField(Structure):
	"""查询银行资金请求响应"""
	_fields_ = [
		#响应代码
		("RetCode",c_char*5),
		#响应信息
		("RetInfo",c_char*129),
		#资金账户
		("FutureAccount",c_char*13),
		#银行余额
		("TradeAmt",c_double),
		#银行可用余额
		("UseAmt",c_double),
		#银行可取余额
		("FetchAmt",c_double),
		#币种
		("CurrencyCode",c_char*4),
		]

	def getRetCode(self):
		return str(self.RetCode, 'GB2312')
	def getRetInfo(self):
		return str(self.RetInfo, 'GB2312')
	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getTradeAmt(self):
		return self.TradeAmt
	def getUseAmt(self):
		return self.UseAmt
	def getFetchAmt(self):
		return self.FetchAmt
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')

	def __str__(self):
		return 'RetCode=\'{0}\', RetInfo=\'{1}\', FutureAccount=\'{2}\', TradeAmt={3}, UseAmt={4}, FetchAmt={5}, CurrencyCode=\'{6}\''.format(str(self.RetCode, 'GB2312'), str(self.RetInfo, 'GB2312'), str(self.FutureAccount, 'GB2312'), self.TradeAmt, self.UseAmt, self.FetchAmt, str(self.CurrencyCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'RetCode':str(self.RetCode, 'GB2312'),'RetInfo':str(self.RetInfo, 'GB2312'),'FutureAccount':str(self.FutureAccount, 'GB2312'),'TradeAmt':self.TradeAmt,'UseAmt':self.UseAmt,'FetchAmt':self.FetchAmt,'CurrencyCode':str(self.CurrencyCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferQryBankRspField()
		obj.RetCode=self.RetCode
		obj.RetInfo=self.RetInfo
		obj.FutureAccount=self.FutureAccount
		obj.TradeAmt=self.TradeAmt
		obj.UseAmt=self.UseAmt
		obj.FetchAmt=self.FetchAmt
		obj.CurrencyCode=self.CurrencyCode
		return obj

class CThostFtdcTransferQryDetailReqField(Structure):
	"""查询银行交易明细请求，TradeCode=204999"""
	_fields_ = [
		#期货资金账户
		("FutureAccount",c_char*13),
		]

	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')

	def __str__(self):
		return 'FutureAccount=\'{0}\''.format(str(self.FutureAccount, 'GB2312'))

	@property
	def __dict__(self):
		return {'FutureAccount':str(self.FutureAccount, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferQryDetailReqField()
		obj.FutureAccount=self.FutureAccount
		return obj

class CThostFtdcTransferQryDetailRspField(Structure):
	"""查询银行交易明细请求响应"""
	_fields_ = [
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#交易代码
		("TradeCode",c_char*7),
		#期货流水号
		("FutureSerial",c_int32),
		#期货公司代码
		("FutureID",c_char*11),
		#资金帐号
		("FutureAccount",c_char*22),
		#银行流水号
		("BankSerial",c_int32),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行账号
		("BankAccount",c_char*41),
		#证件号码
		("CertCode",c_char*21),
		#货币代码
		("CurrencyCode",c_char*4),
		#发生金额
		("TxAmount",c_double),
		#有效标志
		("Flag",c_char),
		]

	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getFutureSerial(self):
		return self.FutureSerial
	def getFutureID(self):
		return str(self.FutureID, 'GB2312')
	def getFutureAccount(self):
		return str(self.FutureAccount, 'GB2312')
	def getBankSerial(self):
		return self.BankSerial
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getCertCode(self):
		return str(self.CertCode, 'GB2312')
	def getCurrencyCode(self):
		return str(self.CurrencyCode, 'GB2312')
	def getTxAmount(self):
		return self.TxAmount
	def getFlag(self):
		return TransferValidFlagType(ord(self.Flag))

	def __str__(self):
		return 'TradeDate=\'{0}\', TradeTime=\'{1}\', TradeCode=\'{2}\', FutureSerial={3}, FutureID=\'{4}\', FutureAccount=\'{5}\', BankSerial={6}, BankID=\'{7}\', BankBrchID=\'{8}\', BankAccount=\'{9}\', CertCode=\'{10}\', CurrencyCode=\'{11}\', TxAmount={12}, Flag=TransferValidFlagType.{13}'.format(str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.TradeCode, 'GB2312'), self.FutureSerial, str(self.FutureID, 'GB2312'), str(self.FutureAccount, 'GB2312'), self.BankSerial, str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'), str(self.BankAccount, 'GB2312'), str(self.CertCode, 'GB2312'), str(self.CurrencyCode, 'GB2312'), self.TxAmount, '' if ord(self.Flag) == 0 else TransferValidFlagType(ord(self.Flag)).name)

	@property
	def __dict__(self):
		return {'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'TradeCode':str(self.TradeCode, 'GB2312'),'FutureSerial':self.FutureSerial,'FutureID':str(self.FutureID, 'GB2312'),'FutureAccount':str(self.FutureAccount, 'GB2312'),'BankSerial':self.BankSerial,'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312'),'BankAccount':str(self.BankAccount, 'GB2312'),'CertCode':str(self.CertCode, 'GB2312'),'CurrencyCode':str(self.CurrencyCode, 'GB2312'),'TxAmount':self.TxAmount,'Flag':'' if ord(self.Flag) == 0 else TransferValidFlagType(ord(self.Flag)).name}

	def clone(self):
		obj=CThostFtdcTransferQryDetailRspField()
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.TradeCode=self.TradeCode
		obj.FutureSerial=self.FutureSerial
		obj.FutureID=self.FutureID
		obj.FutureAccount=self.FutureAccount
		obj.BankSerial=self.BankSerial
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		obj.BankAccount=self.BankAccount
		obj.CertCode=self.CertCode
		obj.CurrencyCode=self.CurrencyCode
		obj.TxAmount=self.TxAmount
		obj.Flag=self.Flag
		return obj

class CThostFtdcRspInfoField(Structure):
	"""响应信息"""
	_fields_ = [
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'ErrorID={0}, ErrorMsg=\'{1}\''.format(self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspInfoField()
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcExchangeField(Structure):
	"""交易所"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所名称
		("ExchangeName",c_char*61),
		#交易所属性
		("ExchangeProperty",c_char),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeName(self):
		return str(self.ExchangeName, 'GB2312')
	def getExchangeProperty(self):
		return ExchangePropertyType(ord(self.ExchangeProperty))

	def __str__(self):
		return 'ExchangeID=\'{0}\', ExchangeName=\'{1}\', ExchangeProperty=ExchangePropertyType.{2}'.format(str(self.ExchangeID, 'GB2312'), str(self.ExchangeName, 'GB2312'), '' if ord(self.ExchangeProperty) == 0 else ExchangePropertyType(ord(self.ExchangeProperty)).name)

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeName':str(self.ExchangeName, 'GB2312'),'ExchangeProperty':'' if ord(self.ExchangeProperty) == 0 else ExchangePropertyType(ord(self.ExchangeProperty)).name}

	def clone(self):
		obj=CThostFtdcExchangeField()
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeName=self.ExchangeName
		obj.ExchangeProperty=self.ExchangeProperty
		return obj

class CThostFtdcProductField(Structure):
	"""产品"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#产品名称
		("ProductName",c_char*21),
		#交易所代码
		("ExchangeID",c_char*9),
		#产品类型
		("ProductClass",c_char),
		#合约数量乘数
		("VolumeMultiple",c_int32),
		#最小变动价位
		("PriceTick",c_double),
		#市价单最大下单量
		("MaxMarketOrderVolume",c_int32),
		#市价单最小下单量
		("MinMarketOrderVolume",c_int32),
		#限价单最大下单量
		("MaxLimitOrderVolume",c_int32),
		#限价单最小下单量
		("MinLimitOrderVolume",c_int32),
		#持仓类型
		("PositionType",c_char),
		#持仓日期类型
		("PositionDateType",c_char),
		#平仓处理类型
		("CloseDealType",c_char),
		#交易币种类型
		("TradeCurrencyID",c_char*4),
		#质押资金可用范围
		("MortgageFundUseRange",c_char),
		#交易所产品代码
		("ExchangeProductID",c_char*31),
		#合约基础商品乘数
		("UnderlyingMultiple",c_double),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getProductName(self):
		return str(self.ProductName, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))
	def getVolumeMultiple(self):
		return self.VolumeMultiple
	def getPriceTick(self):
		return self.PriceTick
	def getMaxMarketOrderVolume(self):
		return self.MaxMarketOrderVolume
	def getMinMarketOrderVolume(self):
		return self.MinMarketOrderVolume
	def getMaxLimitOrderVolume(self):
		return self.MaxLimitOrderVolume
	def getMinLimitOrderVolume(self):
		return self.MinLimitOrderVolume
	def getPositionType(self):
		return PositionTypeType(ord(self.PositionType))
	def getPositionDateType(self):
		return PositionDateTypeType(ord(self.PositionDateType))
	def getCloseDealType(self):
		return CloseDealTypeType(ord(self.CloseDealType))
	def getTradeCurrencyID(self):
		return str(self.TradeCurrencyID, 'GB2312')
	def getMortgageFundUseRange(self):
		return MortgageFundUseRangeType(ord(self.MortgageFundUseRange))
	def getExchangeProductID(self):
		return str(self.ExchangeProductID, 'GB2312')
	def getUnderlyingMultiple(self):
		return self.UnderlyingMultiple

	def __str__(self):
		return 'ProductID=\'{0}\', ProductName=\'{1}\', ExchangeID=\'{2}\', ProductClass=ProductClassType.{3}, VolumeMultiple={4}, PriceTick={5}, MaxMarketOrderVolume={6}, MinMarketOrderVolume={7}, MaxLimitOrderVolume={8}, MinLimitOrderVolume={9}, PositionType=PositionTypeType.{10}, PositionDateType=PositionDateTypeType.{11}, CloseDealType=CloseDealTypeType.{12}, TradeCurrencyID=\'{13}\', MortgageFundUseRange=MortgageFundUseRangeType.{14}, ExchangeProductID=\'{15}\', UnderlyingMultiple={16}'.format(str(self.ProductID, 'GB2312'), str(self.ProductName, 'GB2312'), str(self.ExchangeID, 'GB2312'), '' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name, self.VolumeMultiple, self.PriceTick, self.MaxMarketOrderVolume, self.MinMarketOrderVolume, self.MaxLimitOrderVolume, self.MinLimitOrderVolume, '' if ord(self.PositionType) == 0 else PositionTypeType(ord(self.PositionType)).name, '' if ord(self.PositionDateType) == 0 else PositionDateTypeType(ord(self.PositionDateType)).name, '' if ord(self.CloseDealType) == 0 else CloseDealTypeType(ord(self.CloseDealType)).name, str(self.TradeCurrencyID, 'GB2312'), '' if ord(self.MortgageFundUseRange) == 0 else MortgageFundUseRangeType(ord(self.MortgageFundUseRange)).name, str(self.ExchangeProductID, 'GB2312'), self.UnderlyingMultiple)

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312'),'ProductName':str(self.ProductName, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ProductClass':'' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name,'VolumeMultiple':self.VolumeMultiple,'PriceTick':self.PriceTick,'MaxMarketOrderVolume':self.MaxMarketOrderVolume,'MinMarketOrderVolume':self.MinMarketOrderVolume,'MaxLimitOrderVolume':self.MaxLimitOrderVolume,'MinLimitOrderVolume':self.MinLimitOrderVolume,'PositionType':'' if ord(self.PositionType) == 0 else PositionTypeType(ord(self.PositionType)).name,'PositionDateType':'' if ord(self.PositionDateType) == 0 else PositionDateTypeType(ord(self.PositionDateType)).name,'CloseDealType':'' if ord(self.CloseDealType) == 0 else CloseDealTypeType(ord(self.CloseDealType)).name,'TradeCurrencyID':str(self.TradeCurrencyID, 'GB2312'),'MortgageFundUseRange':'' if ord(self.MortgageFundUseRange) == 0 else MortgageFundUseRangeType(ord(self.MortgageFundUseRange)).name,'ExchangeProductID':str(self.ExchangeProductID, 'GB2312'),'UnderlyingMultiple':self.UnderlyingMultiple}

	def clone(self):
		obj=CThostFtdcProductField()
		obj.ProductID=self.ProductID
		obj.ProductName=self.ProductName
		obj.ExchangeID=self.ExchangeID
		obj.ProductClass=self.ProductClass
		obj.VolumeMultiple=self.VolumeMultiple
		obj.PriceTick=self.PriceTick
		obj.MaxMarketOrderVolume=self.MaxMarketOrderVolume
		obj.MinMarketOrderVolume=self.MinMarketOrderVolume
		obj.MaxLimitOrderVolume=self.MaxLimitOrderVolume
		obj.MinLimitOrderVolume=self.MinLimitOrderVolume
		obj.PositionType=self.PositionType
		obj.PositionDateType=self.PositionDateType
		obj.CloseDealType=self.CloseDealType
		obj.TradeCurrencyID=self.TradeCurrencyID
		obj.MortgageFundUseRange=self.MortgageFundUseRange
		obj.ExchangeProductID=self.ExchangeProductID
		obj.UnderlyingMultiple=self.UnderlyingMultiple
		return obj

class CThostFtdcInstrumentField(Structure):
	"""合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约名称
		("InstrumentName",c_char*21),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#产品代码
		("ProductID",c_char*31),
		#产品类型
		("ProductClass",c_char),
		#交割年份
		("DeliveryYear",c_int32),
		#交割月
		("DeliveryMonth",c_int32),
		#市价单最大下单量
		("MaxMarketOrderVolume",c_int32),
		#市价单最小下单量
		("MinMarketOrderVolume",c_int32),
		#限价单最大下单量
		("MaxLimitOrderVolume",c_int32),
		#限价单最小下单量
		("MinLimitOrderVolume",c_int32),
		#合约数量乘数
		("VolumeMultiple",c_int32),
		#最小变动价位
		("PriceTick",c_double),
		#创建日
		("CreateDate",c_char*9),
		#上市日
		("OpenDate",c_char*9),
		#到期日
		("ExpireDate",c_char*9),
		#开始交割日
		("StartDelivDate",c_char*9),
		#结束交割日
		("EndDelivDate",c_char*9),
		#合约生命周期状态
		("InstLifePhase",c_char),
		#当前是否交易
		("IsTrading",c_int32),
		#持仓类型
		("PositionType",c_char),
		#持仓日期类型
		("PositionDateType",c_char),
		#多头保证金率
		("LongMarginRatio",c_double),
		#空头保证金率
		("ShortMarginRatio",c_double),
		#是否使用大额单边保证金算法
		("MaxMarginSideAlgorithm",c_char),
		#基础商品代码
		("UnderlyingInstrID",c_char*31),
		#执行价
		("StrikePrice",c_double),
		#期权类型
		("OptionsType",c_char),
		#合约基础商品乘数
		("UnderlyingMultiple",c_double),
		#组合类型
		("CombinationType",c_char),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInstrumentName(self):
		return str(self.InstrumentName, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))
	def getDeliveryYear(self):
		return self.DeliveryYear
	def getDeliveryMonth(self):
		return self.DeliveryMonth
	def getMaxMarketOrderVolume(self):
		return self.MaxMarketOrderVolume
	def getMinMarketOrderVolume(self):
		return self.MinMarketOrderVolume
	def getMaxLimitOrderVolume(self):
		return self.MaxLimitOrderVolume
	def getMinLimitOrderVolume(self):
		return self.MinLimitOrderVolume
	def getVolumeMultiple(self):
		return self.VolumeMultiple
	def getPriceTick(self):
		return self.PriceTick
	def getCreateDate(self):
		return str(self.CreateDate, 'GB2312')
	def getOpenDate(self):
		return str(self.OpenDate, 'GB2312')
	def getExpireDate(self):
		return str(self.ExpireDate, 'GB2312')
	def getStartDelivDate(self):
		return str(self.StartDelivDate, 'GB2312')
	def getEndDelivDate(self):
		return str(self.EndDelivDate, 'GB2312')
	def getInstLifePhase(self):
		return InstLifePhaseType(ord(self.InstLifePhase))
	def getIsTrading(self):
		return self.IsTrading
	def getPositionType(self):
		return PositionTypeType(ord(self.PositionType))
	def getPositionDateType(self):
		return PositionDateTypeType(ord(self.PositionDateType))
	def getLongMarginRatio(self):
		return self.LongMarginRatio
	def getShortMarginRatio(self):
		return self.ShortMarginRatio
	def getMaxMarginSideAlgorithm(self):
		return MaxMarginSideAlgorithmType(ord(self.MaxMarginSideAlgorithm))
	def getUnderlyingInstrID(self):
		return str(self.UnderlyingInstrID, 'GB2312')
	def getStrikePrice(self):
		return self.StrikePrice
	def getOptionsType(self):
		return OptionsTypeType(ord(self.OptionsType))
	def getUnderlyingMultiple(self):
		return self.UnderlyingMultiple
	def getCombinationType(self):
		return CombinationTypeType(ord(self.CombinationType))

	def __str__(self):
		return 'InstrumentID=\'{0}\', ExchangeID=\'{1}\', InstrumentName=\'{2}\', ExchangeInstID=\'{3}\', ProductID=\'{4}\', ProductClass=ProductClassType.{5}, DeliveryYear={6}, DeliveryMonth={7}, MaxMarketOrderVolume={8}, MinMarketOrderVolume={9}, MaxLimitOrderVolume={10}, MinLimitOrderVolume={11}, VolumeMultiple={12}, PriceTick={13}, CreateDate=\'{14}\', OpenDate=\'{15}\', ExpireDate=\'{16}\', StartDelivDate=\'{17}\', EndDelivDate=\'{18}\', InstLifePhase=InstLifePhaseType.{19}, IsTrading={20}, PositionType=PositionTypeType.{21}, PositionDateType=PositionDateTypeType.{22}, LongMarginRatio={23}, ShortMarginRatio={24}, MaxMarginSideAlgorithm=MaxMarginSideAlgorithmType.{25}, UnderlyingInstrID=\'{26}\', StrikePrice={27}, OptionsType=OptionsTypeType.{28}, UnderlyingMultiple={29}, CombinationType=CombinationTypeType.{30}'.format(str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InstrumentName, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ProductID, 'GB2312'), '' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name, self.DeliveryYear, self.DeliveryMonth, self.MaxMarketOrderVolume, self.MinMarketOrderVolume, self.MaxLimitOrderVolume, self.MinLimitOrderVolume, self.VolumeMultiple, self.PriceTick, str(self.CreateDate, 'GB2312'), str(self.OpenDate, 'GB2312'), str(self.ExpireDate, 'GB2312'), str(self.StartDelivDate, 'GB2312'), str(self.EndDelivDate, 'GB2312'), '' if ord(self.InstLifePhase) == 0 else InstLifePhaseType(ord(self.InstLifePhase)).name, self.IsTrading, '' if ord(self.PositionType) == 0 else PositionTypeType(ord(self.PositionType)).name, '' if ord(self.PositionDateType) == 0 else PositionDateTypeType(ord(self.PositionDateType)).name, self.LongMarginRatio, self.ShortMarginRatio, '' if ord(self.MaxMarginSideAlgorithm) == 0 else MaxMarginSideAlgorithmType(ord(self.MaxMarginSideAlgorithm)).name, str(self.UnderlyingInstrID, 'GB2312'), self.StrikePrice, '' if ord(self.OptionsType) == 0 else OptionsTypeType(ord(self.OptionsType)).name, self.UnderlyingMultiple, '' if ord(self.CombinationType) == 0 else CombinationTypeType(ord(self.CombinationType)).name)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InstrumentName':str(self.InstrumentName, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ProductID':str(self.ProductID, 'GB2312'),'ProductClass':'' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name,'DeliveryYear':self.DeliveryYear,'DeliveryMonth':self.DeliveryMonth,'MaxMarketOrderVolume':self.MaxMarketOrderVolume,'MinMarketOrderVolume':self.MinMarketOrderVolume,'MaxLimitOrderVolume':self.MaxLimitOrderVolume,'MinLimitOrderVolume':self.MinLimitOrderVolume,'VolumeMultiple':self.VolumeMultiple,'PriceTick':self.PriceTick,'CreateDate':str(self.CreateDate, 'GB2312'),'OpenDate':str(self.OpenDate, 'GB2312'),'ExpireDate':str(self.ExpireDate, 'GB2312'),'StartDelivDate':str(self.StartDelivDate, 'GB2312'),'EndDelivDate':str(self.EndDelivDate, 'GB2312'),'InstLifePhase':'' if ord(self.InstLifePhase) == 0 else InstLifePhaseType(ord(self.InstLifePhase)).name,'IsTrading':self.IsTrading,'PositionType':'' if ord(self.PositionType) == 0 else PositionTypeType(ord(self.PositionType)).name,'PositionDateType':'' if ord(self.PositionDateType) == 0 else PositionDateTypeType(ord(self.PositionDateType)).name,'LongMarginRatio':self.LongMarginRatio,'ShortMarginRatio':self.ShortMarginRatio,'MaxMarginSideAlgorithm':'' if ord(self.MaxMarginSideAlgorithm) == 0 else MaxMarginSideAlgorithmType(ord(self.MaxMarginSideAlgorithm)).name,'UnderlyingInstrID':str(self.UnderlyingInstrID, 'GB2312'),'StrikePrice':self.StrikePrice,'OptionsType':'' if ord(self.OptionsType) == 0 else OptionsTypeType(ord(self.OptionsType)).name,'UnderlyingMultiple':self.UnderlyingMultiple,'CombinationType':'' if ord(self.CombinationType) == 0 else CombinationTypeType(ord(self.CombinationType)).name}

	def clone(self):
		obj=CThostFtdcInstrumentField()
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.InstrumentName=self.InstrumentName
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ProductID=self.ProductID
		obj.ProductClass=self.ProductClass
		obj.DeliveryYear=self.DeliveryYear
		obj.DeliveryMonth=self.DeliveryMonth
		obj.MaxMarketOrderVolume=self.MaxMarketOrderVolume
		obj.MinMarketOrderVolume=self.MinMarketOrderVolume
		obj.MaxLimitOrderVolume=self.MaxLimitOrderVolume
		obj.MinLimitOrderVolume=self.MinLimitOrderVolume
		obj.VolumeMultiple=self.VolumeMultiple
		obj.PriceTick=self.PriceTick
		obj.CreateDate=self.CreateDate
		obj.OpenDate=self.OpenDate
		obj.ExpireDate=self.ExpireDate
		obj.StartDelivDate=self.StartDelivDate
		obj.EndDelivDate=self.EndDelivDate
		obj.InstLifePhase=self.InstLifePhase
		obj.IsTrading=self.IsTrading
		obj.PositionType=self.PositionType
		obj.PositionDateType=self.PositionDateType
		obj.LongMarginRatio=self.LongMarginRatio
		obj.ShortMarginRatio=self.ShortMarginRatio
		obj.MaxMarginSideAlgorithm=self.MaxMarginSideAlgorithm
		obj.UnderlyingInstrID=self.UnderlyingInstrID
		obj.StrikePrice=self.StrikePrice
		obj.OptionsType=self.OptionsType
		obj.UnderlyingMultiple=self.UnderlyingMultiple
		obj.CombinationType=self.CombinationType
		return obj

class CThostFtdcBrokerField(Structure):
	"""经纪公司"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司简称
		("BrokerAbbr",c_char*9),
		#经纪公司名称
		("BrokerName",c_char*81),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerAbbr(self):
		return str(self.BrokerAbbr, 'GB2312')
	def getBrokerName(self):
		return str(self.BrokerName, 'GB2312')
	def getIsActive(self):
		return self.IsActive

	def __str__(self):
		return 'BrokerID=\'{0}\', BrokerAbbr=\'{1}\', BrokerName=\'{2}\', IsActive={3}'.format(str(self.BrokerID, 'GB2312'), str(self.BrokerAbbr, 'GB2312'), str(self.BrokerName, 'GB2312'), self.IsActive)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerAbbr':str(self.BrokerAbbr, 'GB2312'),'BrokerName':str(self.BrokerName, 'GB2312'),'IsActive':self.IsActive}

	def clone(self):
		obj=CThostFtdcBrokerField()
		obj.BrokerID=self.BrokerID
		obj.BrokerAbbr=self.BrokerAbbr
		obj.BrokerName=self.BrokerName
		obj.IsActive=self.IsActive
		return obj

class CThostFtdcTraderField(Structure):
	"""交易所交易员"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装数量
		("InstallCount",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallCount(self):
		return self.InstallCount
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', TraderID=\'{1}\', ParticipantID=\'{2}\', Password=\'{3}\', InstallCount={4}, BrokerID=\'{5}\''.format(str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallCount, str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallCount':self.InstallCount,'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTraderField()
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		obj.ParticipantID=self.ParticipantID
		obj.Password=self.Password
		obj.InstallCount=self.InstallCount
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcInvestorField(Structure):
	"""投资者"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者名称
		("InvestorName",c_char*81),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#是否活跃
		("IsActive",c_int32),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#开户日期
		("OpenDate",c_char*9),
		#手机
		("Mobile",c_char*41),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorGroupID(self):
		return str(self.InvestorGroupID, 'GB2312')
	def getInvestorName(self):
		return str(self.InvestorName, 'GB2312')
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getIsActive(self):
		return self.IsActive
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getOpenDate(self):
		return str(self.OpenDate, 'GB2312')
	def getMobile(self):
		return str(self.Mobile, 'GB2312')
	def getCommModelID(self):
		return str(self.CommModelID, 'GB2312')
	def getMarginModelID(self):
		return str(self.MarginModelID, 'GB2312')

	def __str__(self):
		return 'InvestorID=\'{0}\', BrokerID=\'{1}\', InvestorGroupID=\'{2}\', InvestorName=\'{3}\', IdentifiedCardType=IdCardTypeType.{4}, IdentifiedCardNo=\'{5}\', IsActive={6}, Telephone=\'{7}\', Address=\'{8}\', OpenDate=\'{9}\', Mobile=\'{10}\', CommModelID=\'{11}\', MarginModelID=\'{12}\''.format(str(self.InvestorID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorGroupID, 'GB2312'), str(self.InvestorName, 'GB2312'), '' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), self.IsActive, str(self.Telephone, 'GB2312'), str(self.Address, 'GB2312'), str(self.OpenDate, 'GB2312'), str(self.Mobile, 'GB2312'), str(self.CommModelID, 'GB2312'), str(self.MarginModelID, 'GB2312'))

	@property
	def __dict__(self):
		return {'InvestorID':str(self.InvestorID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorGroupID':str(self.InvestorGroupID, 'GB2312'),'InvestorName':str(self.InvestorName, 'GB2312'),'IdentifiedCardType':'' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'IsActive':self.IsActive,'Telephone':str(self.Telephone, 'GB2312'),'Address':str(self.Address, 'GB2312'),'OpenDate':str(self.OpenDate, 'GB2312'),'Mobile':str(self.Mobile, 'GB2312'),'CommModelID':str(self.CommModelID, 'GB2312'),'MarginModelID':str(self.MarginModelID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInvestorField()
		obj.InvestorID=self.InvestorID
		obj.BrokerID=self.BrokerID
		obj.InvestorGroupID=self.InvestorGroupID
		obj.InvestorName=self.InvestorName
		obj.IdentifiedCardType=self.IdentifiedCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.IsActive=self.IsActive
		obj.Telephone=self.Telephone
		obj.Address=self.Address
		obj.OpenDate=self.OpenDate
		obj.Mobile=self.Mobile
		obj.CommModelID=self.CommModelID
		obj.MarginModelID=self.MarginModelID
		return obj

class CThostFtdcTradingCodeField(Structure):
	"""交易编码"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIsActive(self):
		return self.IsActive
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

	def __str__(self):
		return 'InvestorID=\'{0}\', BrokerID=\'{1}\', ExchangeID=\'{2}\', ClientID=\'{3}\', IsActive={4}, ClientIDType=ClientIDTypeType.{5}'.format(str(self.InvestorID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ClientID, 'GB2312'), self.IsActive, '' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name)

	@property
	def __dict__(self):
		return {'InvestorID':str(self.InvestorID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IsActive':self.IsActive,'ClientIDType':'' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name}

	def clone(self):
		obj=CThostFtdcTradingCodeField()
		obj.InvestorID=self.InvestorID
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		obj.ClientID=self.ClientID
		obj.IsActive=self.IsActive
		obj.ClientIDType=self.ClientIDType
		return obj

class CThostFtdcPartBrokerField(Structure):
	"""会员编码和经纪公司编码对照表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getIsActive(self):
		return self.IsActive

	def __str__(self):
		return 'BrokerID=\'{0}\', ExchangeID=\'{1}\', ParticipantID=\'{2}\', IsActive={3}'.format(str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), self.IsActive)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'IsActive':self.IsActive}

	def clone(self):
		obj=CThostFtdcPartBrokerField()
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.IsActive=self.IsActive
		return obj

class CThostFtdcSuperUserField(Structure):
	"""管理用户"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		#用户名称
		("UserName",c_char*81),
		#密码
		("Password",c_char*41),
		#是否活跃
		("IsActive",c_int32),
		]

	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserName(self):
		return str(self.UserName, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getIsActive(self):
		return self.IsActive

	def __str__(self):
		return 'UserID=\'{0}\', UserName=\'{1}\', Password=\'{2}\', IsActive={3}'.format(str(self.UserID, 'GB2312'), str(self.UserName, 'GB2312'), str(self.Password, 'GB2312'), self.IsActive)

	@property
	def __dict__(self):
		return {'UserID':str(self.UserID, 'GB2312'),'UserName':str(self.UserName, 'GB2312'),'Password':str(self.Password, 'GB2312'),'IsActive':self.IsActive}

	def clone(self):
		obj=CThostFtdcSuperUserField()
		obj.UserID=self.UserID
		obj.UserName=self.UserName
		obj.Password=self.Password
		obj.IsActive=self.IsActive
		return obj

class CThostFtdcSuperUserFunctionField(Structure):
	"""管理用户功能权限"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		#功能代码
		("FunctionCode",c_char),
		]

	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getFunctionCode(self):
		return FunctionCodeType(ord(self.FunctionCode))

	def __str__(self):
		return 'UserID=\'{0}\', FunctionCode=FunctionCodeType.{1}'.format(str(self.UserID, 'GB2312'), '' if ord(self.FunctionCode) == 0 else FunctionCodeType(ord(self.FunctionCode)).name)

	@property
	def __dict__(self):
		return {'UserID':str(self.UserID, 'GB2312'),'FunctionCode':'' if ord(self.FunctionCode) == 0 else FunctionCodeType(ord(self.FunctionCode)).name}

	def clone(self):
		obj=CThostFtdcSuperUserFunctionField()
		obj.UserID=self.UserID
		obj.FunctionCode=self.FunctionCode
		return obj

class CThostFtdcInvestorGroupField(Structure):
	"""投资者组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者分组名称
		("InvestorGroupName",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorGroupID(self):
		return str(self.InvestorGroupID, 'GB2312')
	def getInvestorGroupName(self):
		return str(self.InvestorGroupName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorGroupID=\'{1}\', InvestorGroupName=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorGroupID, 'GB2312'), str(self.InvestorGroupName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorGroupID':str(self.InvestorGroupID, 'GB2312'),'InvestorGroupName':str(self.InvestorGroupName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInvestorGroupField()
		obj.BrokerID=self.BrokerID
		obj.InvestorGroupID=self.InvestorGroupID
		obj.InvestorGroupName=self.InvestorGroupName
		return obj

class CThostFtdcTradingAccountField(Structure):
	"""资金账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#上次质押金额
		("PreMortgage",c_double),
		#上次信用额度
		("PreCredit",c_double),
		#上次存款额
		("PreDeposit",c_double),
		#上次结算准备金
		("PreBalance",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#利息基数
		("InterestBase",c_double),
		#利息收入
		("Interest",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#可用资金
		("Available",c_double),
		#可取资金
		("WithdrawQuota",c_double),
		#基本准备金
		("Reserve",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#信用额度
		("Credit",c_double),
		#质押金额
		("Mortgage",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#投资者交割保证金
		("DeliveryMargin",c_double),
		#交易所交割保证金
		("ExchangeDeliveryMargin",c_double),
		#保底期货结算准备金
		("ReserveBalance",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#上次货币质入金额
		("PreFundMortgageIn",c_double),
		#上次货币质出金额
		("PreFundMortgageOut",c_double),
		#货币质入金额
		("FundMortgageIn",c_double),
		#货币质出金额
		("FundMortgageOut",c_double),
		#货币质押余额
		("FundMortgageAvailable",c_double),
		#可质押货币金额
		("MortgageableFund",c_double),
		#特殊产品占用保证金
		("SpecProductMargin",c_double),
		#特殊产品冻结保证金
		("SpecProductFrozenMargin",c_double),
		#特殊产品手续费
		("SpecProductCommission",c_double),
		#特殊产品冻结手续费
		("SpecProductFrozenCommission",c_double),
		#特殊产品持仓盈亏
		("SpecProductPositionProfit",c_double),
		#特殊产品平仓盈亏
		("SpecProductCloseProfit",c_double),
		#根据持仓盈亏算法计算的特殊产品持仓盈亏
		("SpecProductPositionProfitByAlg",c_double),
		#特殊产品交易所保证金
		("SpecProductExchangeMargin",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPreMortgage(self):
		return self.PreMortgage
	def getPreCredit(self):
		return self.PreCredit
	def getPreDeposit(self):
		return self.PreDeposit
	def getPreBalance(self):
		return self.PreBalance
	def getPreMargin(self):
		return self.PreMargin
	def getInterestBase(self):
		return self.InterestBase
	def getInterest(self):
		return self.Interest
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCurrMargin(self):
		return self.CurrMargin
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getBalance(self):
		return self.Balance
	def getAvailable(self):
		return self.Available
	def getWithdrawQuota(self):
		return self.WithdrawQuota
	def getReserve(self):
		return self.Reserve
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getCredit(self):
		return self.Credit
	def getMortgage(self):
		return self.Mortgage
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getDeliveryMargin(self):
		return self.DeliveryMargin
	def getExchangeDeliveryMargin(self):
		return self.ExchangeDeliveryMargin
	def getReserveBalance(self):
		return self.ReserveBalance
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getPreFundMortgageIn(self):
		return self.PreFundMortgageIn
	def getPreFundMortgageOut(self):
		return self.PreFundMortgageOut
	def getFundMortgageIn(self):
		return self.FundMortgageIn
	def getFundMortgageOut(self):
		return self.FundMortgageOut
	def getFundMortgageAvailable(self):
		return self.FundMortgageAvailable
	def getMortgageableFund(self):
		return self.MortgageableFund
	def getSpecProductMargin(self):
		return self.SpecProductMargin
	def getSpecProductFrozenMargin(self):
		return self.SpecProductFrozenMargin
	def getSpecProductCommission(self):
		return self.SpecProductCommission
	def getSpecProductFrozenCommission(self):
		return self.SpecProductFrozenCommission
	def getSpecProductPositionProfit(self):
		return self.SpecProductPositionProfit
	def getSpecProductCloseProfit(self):
		return self.SpecProductCloseProfit
	def getSpecProductPositionProfitByAlg(self):
		return self.SpecProductPositionProfitByAlg
	def getSpecProductExchangeMargin(self):
		return self.SpecProductExchangeMargin

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', PreMortgage={2}, PreCredit={3}, PreDeposit={4}, PreBalance={5}, PreMargin={6}, InterestBase={7}, Interest={8}, Deposit={9}, Withdraw={10}, FrozenMargin={11}, FrozenCash={12}, FrozenCommission={13}, CurrMargin={14}, CashIn={15}, Commission={16}, CloseProfit={17}, PositionProfit={18}, Balance={19}, Available={20}, WithdrawQuota={21}, Reserve={22}, TradingDay=\'{23}\', SettlementID={24}, Credit={25}, Mortgage={26}, ExchangeMargin={27}, DeliveryMargin={28}, ExchangeDeliveryMargin={29}, ReserveBalance={30}, CurrencyID=\'{31}\', PreFundMortgageIn={32}, PreFundMortgageOut={33}, FundMortgageIn={34}, FundMortgageOut={35}, FundMortgageAvailable={36}, MortgageableFund={37}, SpecProductMargin={38}, SpecProductFrozenMargin={39}, SpecProductCommission={40}, SpecProductFrozenCommission={41}, SpecProductPositionProfit={42}, SpecProductCloseProfit={43}, SpecProductPositionProfitByAlg={44}, SpecProductExchangeMargin={45}'.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), self.PreMortgage, self.PreCredit, self.PreDeposit, self.PreBalance, self.PreMargin, self.InterestBase, self.Interest, self.Deposit, self.Withdraw, self.FrozenMargin, self.FrozenCash, self.FrozenCommission, self.CurrMargin, self.CashIn, self.Commission, self.CloseProfit, self.PositionProfit, self.Balance, self.Available, self.WithdrawQuota, self.Reserve, str(self.TradingDay, 'GB2312'), self.SettlementID, self.Credit, self.Mortgage, self.ExchangeMargin, self.DeliveryMargin, self.ExchangeDeliveryMargin, self.ReserveBalance, str(self.CurrencyID, 'GB2312'), self.PreFundMortgageIn, self.PreFundMortgageOut, self.FundMortgageIn, self.FundMortgageOut, self.FundMortgageAvailable, self.MortgageableFund, self.SpecProductMargin, self.SpecProductFrozenMargin, self.SpecProductCommission, self.SpecProductFrozenCommission, self.SpecProductPositionProfit, self.SpecProductCloseProfit, self.SpecProductPositionProfitByAlg, self.SpecProductExchangeMargin)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'PreMortgage':self.PreMortgage,'PreCredit':self.PreCredit,'PreDeposit':self.PreDeposit,'PreBalance':self.PreBalance,'PreMargin':self.PreMargin,'InterestBase':self.InterestBase,'Interest':self.Interest,'Deposit':self.Deposit,'Withdraw':self.Withdraw,'FrozenMargin':self.FrozenMargin,'FrozenCash':self.FrozenCash,'FrozenCommission':self.FrozenCommission,'CurrMargin':self.CurrMargin,'CashIn':self.CashIn,'Commission':self.Commission,'CloseProfit':self.CloseProfit,'PositionProfit':self.PositionProfit,'Balance':self.Balance,'Available':self.Available,'WithdrawQuota':self.WithdrawQuota,'Reserve':self.Reserve,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'Credit':self.Credit,'Mortgage':self.Mortgage,'ExchangeMargin':self.ExchangeMargin,'DeliveryMargin':self.DeliveryMargin,'ExchangeDeliveryMargin':self.ExchangeDeliveryMargin,'ReserveBalance':self.ReserveBalance,'CurrencyID':str(self.CurrencyID, 'GB2312'),'PreFundMortgageIn':self.PreFundMortgageIn,'PreFundMortgageOut':self.PreFundMortgageOut,'FundMortgageIn':self.FundMortgageIn,'FundMortgageOut':self.FundMortgageOut,'FundMortgageAvailable':self.FundMortgageAvailable,'MortgageableFund':self.MortgageableFund,'SpecProductMargin':self.SpecProductMargin,'SpecProductFrozenMargin':self.SpecProductFrozenMargin,'SpecProductCommission':self.SpecProductCommission,'SpecProductFrozenCommission':self.SpecProductFrozenCommission,'SpecProductPositionProfit':self.SpecProductPositionProfit,'SpecProductCloseProfit':self.SpecProductCloseProfit,'SpecProductPositionProfitByAlg':self.SpecProductPositionProfitByAlg,'SpecProductExchangeMargin':self.SpecProductExchangeMargin}

	def clone(self):
		obj=CThostFtdcTradingAccountField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.PreMortgage=self.PreMortgage
		obj.PreCredit=self.PreCredit
		obj.PreDeposit=self.PreDeposit
		obj.PreBalance=self.PreBalance
		obj.PreMargin=self.PreMargin
		obj.InterestBase=self.InterestBase
		obj.Interest=self.Interest
		obj.Deposit=self.Deposit
		obj.Withdraw=self.Withdraw
		obj.FrozenMargin=self.FrozenMargin
		obj.FrozenCash=self.FrozenCash
		obj.FrozenCommission=self.FrozenCommission
		obj.CurrMargin=self.CurrMargin
		obj.CashIn=self.CashIn
		obj.Commission=self.Commission
		obj.CloseProfit=self.CloseProfit
		obj.PositionProfit=self.PositionProfit
		obj.Balance=self.Balance
		obj.Available=self.Available
		obj.WithdrawQuota=self.WithdrawQuota
		obj.Reserve=self.Reserve
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.Credit=self.Credit
		obj.Mortgage=self.Mortgage
		obj.ExchangeMargin=self.ExchangeMargin
		obj.DeliveryMargin=self.DeliveryMargin
		obj.ExchangeDeliveryMargin=self.ExchangeDeliveryMargin
		obj.ReserveBalance=self.ReserveBalance
		obj.CurrencyID=self.CurrencyID
		obj.PreFundMortgageIn=self.PreFundMortgageIn
		obj.PreFundMortgageOut=self.PreFundMortgageOut
		obj.FundMortgageIn=self.FundMortgageIn
		obj.FundMortgageOut=self.FundMortgageOut
		obj.FundMortgageAvailable=self.FundMortgageAvailable
		obj.MortgageableFund=self.MortgageableFund
		obj.SpecProductMargin=self.SpecProductMargin
		obj.SpecProductFrozenMargin=self.SpecProductFrozenMargin
		obj.SpecProductCommission=self.SpecProductCommission
		obj.SpecProductFrozenCommission=self.SpecProductFrozenCommission
		obj.SpecProductPositionProfit=self.SpecProductPositionProfit
		obj.SpecProductCloseProfit=self.SpecProductCloseProfit
		obj.SpecProductPositionProfitByAlg=self.SpecProductPositionProfitByAlg
		obj.SpecProductExchangeMargin=self.SpecProductExchangeMargin
		return obj

class CThostFtdcInvestorPositionField(Structure):
	"""投资者持仓"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#持仓多空方向
		("PosiDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#持仓日期
		("PositionDate",c_char),
		#上日持仓
		("YdPosition",c_int32),
		#今日持仓
		("Position",c_int32),
		#多头冻结
		("LongFrozen",c_int32),
		#空头冻结
		("ShortFrozen",c_int32),
		#开仓冻结金额
		("LongFrozenAmount",c_double),
		#开仓冻结金额
		("ShortFrozenAmount",c_double),
		#开仓量
		("OpenVolume",c_int32),
		#平仓量
		("CloseVolume",c_int32),
		#开仓金额
		("OpenAmount",c_double),
		#平仓金额
		("CloseAmount",c_double),
		#持仓成本
		("PositionCost",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#开仓成本
		("OpenCost",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#组合成交形成的持仓
		("CombPosition",c_int32),
		#组合多头冻结
		("CombLongFrozen",c_int32),
		#组合空头冻结
		("CombShortFrozen",c_int32),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#今日持仓
		("TodayPosition",c_int32),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#执行冻结
		("StrikeFrozen",c_int32),
		#执行冻结金额
		("StrikeFrozenAmount",c_double),
		#放弃执行冻结
		("AbandonFrozen",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPositionDate(self):
		return PositionDateType(ord(self.PositionDate))
	def getYdPosition(self):
		return self.YdPosition
	def getPosition(self):
		return self.Position
	def getLongFrozen(self):
		return self.LongFrozen
	def getShortFrozen(self):
		return self.ShortFrozen
	def getLongFrozenAmount(self):
		return self.LongFrozenAmount
	def getShortFrozenAmount(self):
		return self.ShortFrozenAmount
	def getOpenVolume(self):
		return self.OpenVolume
	def getCloseVolume(self):
		return self.CloseVolume
	def getOpenAmount(self):
		return self.OpenAmount
	def getCloseAmount(self):
		return self.CloseAmount
	def getPositionCost(self):
		return self.PositionCost
	def getPreMargin(self):
		return self.PreMargin
	def getUseMargin(self):
		return self.UseMargin
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getOpenCost(self):
		return self.OpenCost
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getCombPosition(self):
		return self.CombPosition
	def getCombLongFrozen(self):
		return self.CombLongFrozen
	def getCombShortFrozen(self):
		return self.CombShortFrozen
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getTodayPosition(self):
		return self.TodayPosition
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getStrikeFrozen(self):
		return self.StrikeFrozen
	def getStrikeFrozenAmount(self):
		return self.StrikeFrozenAmount
	def getAbandonFrozen(self):
		return self.AbandonFrozen

	def __str__(self):
		return 'InstrumentID=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', PosiDirection=PosiDirectionType.{3}, HedgeFlag=HedgeFlagType.{4}, PositionDate=PositionDateType.{5}, YdPosition={6}, Position={7}, LongFrozen={8}, ShortFrozen={9}, LongFrozenAmount={10}, ShortFrozenAmount={11}, OpenVolume={12}, CloseVolume={13}, OpenAmount={14}, CloseAmount={15}, PositionCost={16}, PreMargin={17}, UseMargin={18}, FrozenMargin={19}, FrozenCash={20}, FrozenCommission={21}, CashIn={22}, Commission={23}, CloseProfit={24}, PositionProfit={25}, PreSettlementPrice={26}, SettlementPrice={27}, TradingDay=\'{28}\', SettlementID={29}, OpenCost={30}, ExchangeMargin={31}, CombPosition={32}, CombLongFrozen={33}, CombShortFrozen={34}, CloseProfitByDate={35}, CloseProfitByTrade={36}, TodayPosition={37}, MarginRateByMoney={38}, MarginRateByVolume={39}, StrikeFrozen={40}, StrikeFrozenAmount={41}, AbandonFrozen={42}'.format(str(self.InstrumentID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.PositionDate) == 0 else PositionDateType(ord(self.PositionDate)).name, self.YdPosition, self.Position, self.LongFrozen, self.ShortFrozen, self.LongFrozenAmount, self.ShortFrozenAmount, self.OpenVolume, self.CloseVolume, self.OpenAmount, self.CloseAmount, self.PositionCost, self.PreMargin, self.UseMargin, self.FrozenMargin, self.FrozenCash, self.FrozenCommission, self.CashIn, self.Commission, self.CloseProfit, self.PositionProfit, self.PreSettlementPrice, self.SettlementPrice, str(self.TradingDay, 'GB2312'), self.SettlementID, self.OpenCost, self.ExchangeMargin, self.CombPosition, self.CombLongFrozen, self.CombShortFrozen, self.CloseProfitByDate, self.CloseProfitByTrade, self.TodayPosition, self.MarginRateByMoney, self.MarginRateByVolume, self.StrikeFrozen, self.StrikeFrozenAmount, self.AbandonFrozen)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'PositionDate':'' if ord(self.PositionDate) == 0 else PositionDateType(ord(self.PositionDate)).name,'YdPosition':self.YdPosition,'Position':self.Position,'LongFrozen':self.LongFrozen,'ShortFrozen':self.ShortFrozen,'LongFrozenAmount':self.LongFrozenAmount,'ShortFrozenAmount':self.ShortFrozenAmount,'OpenVolume':self.OpenVolume,'CloseVolume':self.CloseVolume,'OpenAmount':self.OpenAmount,'CloseAmount':self.CloseAmount,'PositionCost':self.PositionCost,'PreMargin':self.PreMargin,'UseMargin':self.UseMargin,'FrozenMargin':self.FrozenMargin,'FrozenCash':self.FrozenCash,'FrozenCommission':self.FrozenCommission,'CashIn':self.CashIn,'Commission':self.Commission,'CloseProfit':self.CloseProfit,'PositionProfit':self.PositionProfit,'PreSettlementPrice':self.PreSettlementPrice,'SettlementPrice':self.SettlementPrice,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'OpenCost':self.OpenCost,'ExchangeMargin':self.ExchangeMargin,'CombPosition':self.CombPosition,'CombLongFrozen':self.CombLongFrozen,'CombShortFrozen':self.CombShortFrozen,'CloseProfitByDate':self.CloseProfitByDate,'CloseProfitByTrade':self.CloseProfitByTrade,'TodayPosition':self.TodayPosition,'MarginRateByMoney':self.MarginRateByMoney,'MarginRateByVolume':self.MarginRateByVolume,'StrikeFrozen':self.StrikeFrozen,'StrikeFrozenAmount':self.StrikeFrozenAmount,'AbandonFrozen':self.AbandonFrozen}

	def clone(self):
		obj=CThostFtdcInvestorPositionField()
		obj.InstrumentID=self.InstrumentID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.PosiDirection=self.PosiDirection
		obj.HedgeFlag=self.HedgeFlag
		obj.PositionDate=self.PositionDate
		obj.YdPosition=self.YdPosition
		obj.Position=self.Position
		obj.LongFrozen=self.LongFrozen
		obj.ShortFrozen=self.ShortFrozen
		obj.LongFrozenAmount=self.LongFrozenAmount
		obj.ShortFrozenAmount=self.ShortFrozenAmount
		obj.OpenVolume=self.OpenVolume
		obj.CloseVolume=self.CloseVolume
		obj.OpenAmount=self.OpenAmount
		obj.CloseAmount=self.CloseAmount
		obj.PositionCost=self.PositionCost
		obj.PreMargin=self.PreMargin
		obj.UseMargin=self.UseMargin
		obj.FrozenMargin=self.FrozenMargin
		obj.FrozenCash=self.FrozenCash
		obj.FrozenCommission=self.FrozenCommission
		obj.CashIn=self.CashIn
		obj.Commission=self.Commission
		obj.CloseProfit=self.CloseProfit
		obj.PositionProfit=self.PositionProfit
		obj.PreSettlementPrice=self.PreSettlementPrice
		obj.SettlementPrice=self.SettlementPrice
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.OpenCost=self.OpenCost
		obj.ExchangeMargin=self.ExchangeMargin
		obj.CombPosition=self.CombPosition
		obj.CombLongFrozen=self.CombLongFrozen
		obj.CombShortFrozen=self.CombShortFrozen
		obj.CloseProfitByDate=self.CloseProfitByDate
		obj.CloseProfitByTrade=self.CloseProfitByTrade
		obj.TodayPosition=self.TodayPosition
		obj.MarginRateByMoney=self.MarginRateByMoney
		obj.MarginRateByVolume=self.MarginRateByVolume
		obj.StrikeFrozen=self.StrikeFrozen
		obj.StrikeFrozenAmount=self.StrikeFrozenAmount
		obj.AbandonFrozen=self.AbandonFrozen
		return obj

class CThostFtdcInstrumentMarginRateField(Structure):
	"""合约保证金率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', HedgeFlag=HedgeFlagType.{4}, LongMarginRatioByMoney={5}, LongMarginRatioByVolume={6}, ShortMarginRatioByMoney={7}, ShortMarginRatioByVolume={8}, IsRelative={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.LongMarginRatioByMoney, self.LongMarginRatioByVolume, self.ShortMarginRatioByMoney, self.ShortMarginRatioByVolume, self.IsRelative)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'LongMarginRatioByMoney':self.LongMarginRatioByMoney,'LongMarginRatioByVolume':self.LongMarginRatioByVolume,'ShortMarginRatioByMoney':self.ShortMarginRatioByMoney,'ShortMarginRatioByVolume':self.ShortMarginRatioByVolume,'IsRelative':self.IsRelative}

	def clone(self):
		obj=CThostFtdcInstrumentMarginRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.HedgeFlag=self.HedgeFlag
		obj.LongMarginRatioByMoney=self.LongMarginRatioByMoney
		obj.LongMarginRatioByVolume=self.LongMarginRatioByVolume
		obj.ShortMarginRatioByMoney=self.ShortMarginRatioByMoney
		obj.ShortMarginRatioByVolume=self.ShortMarginRatioByVolume
		obj.IsRelative=self.IsRelative
		return obj

class CThostFtdcInstrumentCommissionRateField(Structure):
	"""合约手续费率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', OpenRatioByMoney={4}, OpenRatioByVolume={5}, CloseRatioByMoney={6}, CloseRatioByVolume={7}, CloseTodayRatioByMoney={8}, CloseTodayRatioByVolume={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OpenRatioByMoney, self.OpenRatioByVolume, self.CloseRatioByMoney, self.CloseRatioByVolume, self.CloseTodayRatioByMoney, self.CloseTodayRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OpenRatioByMoney':self.OpenRatioByMoney,'OpenRatioByVolume':self.OpenRatioByVolume,'CloseRatioByMoney':self.CloseRatioByMoney,'CloseRatioByVolume':self.CloseRatioByVolume,'CloseTodayRatioByMoney':self.CloseTodayRatioByMoney,'CloseTodayRatioByVolume':self.CloseTodayRatioByVolume}

	def clone(self):
		obj=CThostFtdcInstrumentCommissionRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OpenRatioByMoney=self.OpenRatioByMoney
		obj.OpenRatioByVolume=self.OpenRatioByVolume
		obj.CloseRatioByMoney=self.CloseRatioByMoney
		obj.CloseRatioByVolume=self.CloseRatioByVolume
		obj.CloseTodayRatioByMoney=self.CloseTodayRatioByMoney
		obj.CloseTodayRatioByVolume=self.CloseTodayRatioByVolume
		return obj

class CThostFtdcDepthMarketDataField(Structure):
	"""深度行情"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#最新价
		("LastPrice",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		#今收盘
		("ClosePrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#昨虚实度
		("PreDelta",c_double),
		#今虚实度
		("CurrDelta",c_double),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#申买价一
		("BidPrice1",c_double),
		#申买量一
		("BidVolume1",c_int32),
		#申卖价一
		("AskPrice1",c_double),
		#申卖量一
		("AskVolume1",c_int32),
		#申买价二
		("BidPrice2",c_double),
		#申买量二
		("BidVolume2",c_int32),
		#申卖价二
		("AskPrice2",c_double),
		#申卖量二
		("AskVolume2",c_int32),
		#申买价三
		("BidPrice3",c_double),
		#申买量三
		("BidVolume3",c_int32),
		#申卖价三
		("AskPrice3",c_double),
		#申卖量三
		("AskVolume3",c_int32),
		#申买价四
		("BidPrice4",c_double),
		#申买量四
		("BidVolume4",c_int32),
		#申卖价四
		("AskPrice4",c_double),
		#申卖量四
		("AskVolume4",c_int32),
		#申买价五
		("BidPrice5",c_double),
		#申买量五
		("BidVolume5",c_int32),
		#申卖价五
		("AskPrice5",c_double),
		#申卖量五
		("AskVolume5",c_int32),
		#当日均价
		("AveragePrice",c_double),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getLastPrice(self):
		return self.LastPrice
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest
	def getClosePrice(self):
		return self.ClosePrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getPreDelta(self):
		return self.PreDelta
	def getCurrDelta(self):
		return self.CurrDelta
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getBidPrice1(self):
		return self.BidPrice1
	def getBidVolume1(self):
		return self.BidVolume1
	def getAskPrice1(self):
		return self.AskPrice1
	def getAskVolume1(self):
		return self.AskVolume1
	def getBidPrice2(self):
		return self.BidPrice2
	def getBidVolume2(self):
		return self.BidVolume2
	def getAskPrice2(self):
		return self.AskPrice2
	def getAskVolume2(self):
		return self.AskVolume2
	def getBidPrice3(self):
		return self.BidPrice3
	def getBidVolume3(self):
		return self.BidVolume3
	def getAskPrice3(self):
		return self.AskPrice3
	def getAskVolume3(self):
		return self.AskVolume3
	def getBidPrice4(self):
		return self.BidPrice4
	def getBidVolume4(self):
		return self.BidVolume4
	def getAskPrice4(self):
		return self.AskPrice4
	def getAskVolume4(self):
		return self.AskVolume4
	def getBidPrice5(self):
		return self.BidPrice5
	def getBidVolume5(self):
		return self.BidVolume5
	def getAskPrice5(self):
		return self.AskPrice5
	def getAskVolume5(self):
		return self.AskVolume5
	def getAveragePrice(self):
		return self.AveragePrice
	def getActionDay(self):
		return str(self.ActionDay, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', InstrumentID=\'{1}\', ExchangeID=\'{2}\', ExchangeInstID=\'{3}\', LastPrice={4}, PreSettlementPrice={5}, PreClosePrice={6}, PreOpenInterest={7}, OpenPrice={8}, HighestPrice={9}, LowestPrice={10}, Volume={11}, Turnover={12}, OpenInterest={13}, ClosePrice={14}, SettlementPrice={15}, UpperLimitPrice={16}, LowerLimitPrice={17}, PreDelta={18}, CurrDelta={19}, UpdateTime=\'{20}\', UpdateMillisec={21}, BidPrice1={22}, BidVolume1={23}, AskPrice1={24}, AskVolume1={25}, BidPrice2={26}, BidVolume2={27}, AskPrice2={28}, AskVolume2={29}, BidPrice3={30}, BidVolume3={31}, AskPrice3={32}, AskVolume3={33}, BidPrice4={34}, BidVolume4={35}, AskPrice4={36}, AskVolume4={37}, BidPrice5={38}, BidVolume5={39}, AskPrice5={40}, AskVolume5={41}, AveragePrice={42}, ActionDay=\'{43}\''.format(str(self.TradingDay, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), self.LastPrice, self.PreSettlementPrice, self.PreClosePrice, self.PreOpenInterest, self.OpenPrice, self.HighestPrice, self.LowestPrice, self.Volume, self.Turnover, self.OpenInterest, self.ClosePrice, self.SettlementPrice, self.UpperLimitPrice, self.LowerLimitPrice, self.PreDelta, self.CurrDelta, str(self.UpdateTime, 'GB2312'), self.UpdateMillisec, self.BidPrice1, self.BidVolume1, self.AskPrice1, self.AskVolume1, self.BidPrice2, self.BidVolume2, self.AskPrice2, self.AskVolume2, self.BidPrice3, self.BidVolume3, self.AskPrice3, self.AskVolume3, self.BidPrice4, self.BidVolume4, self.AskPrice4, self.AskVolume4, self.BidPrice5, self.BidVolume5, self.AskPrice5, self.AskVolume5, self.AveragePrice, str(self.ActionDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'LastPrice':self.LastPrice,'PreSettlementPrice':self.PreSettlementPrice,'PreClosePrice':self.PreClosePrice,'PreOpenInterest':self.PreOpenInterest,'OpenPrice':self.OpenPrice,'HighestPrice':self.HighestPrice,'LowestPrice':self.LowestPrice,'Volume':self.Volume,'Turnover':self.Turnover,'OpenInterest':self.OpenInterest,'ClosePrice':self.ClosePrice,'SettlementPrice':self.SettlementPrice,'UpperLimitPrice':self.UpperLimitPrice,'LowerLimitPrice':self.LowerLimitPrice,'PreDelta':self.PreDelta,'CurrDelta':self.CurrDelta,'UpdateTime':str(self.UpdateTime, 'GB2312'),'UpdateMillisec':self.UpdateMillisec,'BidPrice1':self.BidPrice1,'BidVolume1':self.BidVolume1,'AskPrice1':self.AskPrice1,'AskVolume1':self.AskVolume1,'BidPrice2':self.BidPrice2,'BidVolume2':self.BidVolume2,'AskPrice2':self.AskPrice2,'AskVolume2':self.AskVolume2,'BidPrice3':self.BidPrice3,'BidVolume3':self.BidVolume3,'AskPrice3':self.AskPrice3,'AskVolume3':self.AskVolume3,'BidPrice4':self.BidPrice4,'BidVolume4':self.BidVolume4,'AskPrice4':self.AskPrice4,'AskVolume4':self.AskVolume4,'BidPrice5':self.BidPrice5,'BidVolume5':self.BidVolume5,'AskPrice5':self.AskPrice5,'AskVolume5':self.AskVolume5,'AveragePrice':self.AveragePrice,'ActionDay':str(self.ActionDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcDepthMarketDataField()
		obj.TradingDay=self.TradingDay
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.LastPrice=self.LastPrice
		obj.PreSettlementPrice=self.PreSettlementPrice
		obj.PreClosePrice=self.PreClosePrice
		obj.PreOpenInterest=self.PreOpenInterest
		obj.OpenPrice=self.OpenPrice
		obj.HighestPrice=self.HighestPrice
		obj.LowestPrice=self.LowestPrice
		obj.Volume=self.Volume
		obj.Turnover=self.Turnover
		obj.OpenInterest=self.OpenInterest
		obj.ClosePrice=self.ClosePrice
		obj.SettlementPrice=self.SettlementPrice
		obj.UpperLimitPrice=self.UpperLimitPrice
		obj.LowerLimitPrice=self.LowerLimitPrice
		obj.PreDelta=self.PreDelta
		obj.CurrDelta=self.CurrDelta
		obj.UpdateTime=self.UpdateTime
		obj.UpdateMillisec=self.UpdateMillisec
		obj.BidPrice1=self.BidPrice1
		obj.BidVolume1=self.BidVolume1
		obj.AskPrice1=self.AskPrice1
		obj.AskVolume1=self.AskVolume1
		obj.BidPrice2=self.BidPrice2
		obj.BidVolume2=self.BidVolume2
		obj.AskPrice2=self.AskPrice2
		obj.AskVolume2=self.AskVolume2
		obj.BidPrice3=self.BidPrice3
		obj.BidVolume3=self.BidVolume3
		obj.AskPrice3=self.AskPrice3
		obj.AskVolume3=self.AskVolume3
		obj.BidPrice4=self.BidPrice4
		obj.BidVolume4=self.BidVolume4
		obj.AskPrice4=self.AskPrice4
		obj.AskVolume4=self.AskVolume4
		obj.BidPrice5=self.BidPrice5
		obj.BidVolume5=self.BidVolume5
		obj.AskPrice5=self.AskPrice5
		obj.AskVolume5=self.AskVolume5
		obj.AveragePrice=self.AveragePrice
		obj.ActionDay=self.ActionDay
		return obj

class CThostFtdcInstrumentTradingRightField(Structure):
	"""投资者合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', TradingRight=TradingRightType.{4}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'TradingRight':'' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name}

	def clone(self):
		obj=CThostFtdcInstrumentTradingRightField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.TradingRight=self.TradingRight
		return obj

class CThostFtdcBrokerUserField(Structure):
	"""经纪公司用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户名称
		("UserName",c_char*81),
		#用户类型
		("UserType",c_char),
		#是否活跃
		("IsActive",c_int32),
		#是否使用令牌
		("IsUsingOTP",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserName(self):
		return str(self.UserName, 'GB2312')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getIsActive(self):
		return self.IsActive
	def getIsUsingOTP(self):
		return self.IsUsingOTP

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserName=\'{2}\', UserType=UserTypeType.{3}, IsActive={4}, IsUsingOTP={5}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.UserName, 'GB2312'), '' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name, self.IsActive, self.IsUsingOTP)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserName':str(self.UserName, 'GB2312'),'UserType':'' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name,'IsActive':self.IsActive,'IsUsingOTP':self.IsUsingOTP}

	def clone(self):
		obj=CThostFtdcBrokerUserField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserName=self.UserName
		obj.UserType=self.UserType
		obj.IsActive=self.IsActive
		obj.IsUsingOTP=self.IsUsingOTP
		return obj

class CThostFtdcBrokerUserPasswordField(Structure):
	"""经纪公司用户口令"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#密码
		("Password",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', Password=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.Password, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Password':str(self.Password, 'GB2312')}

	def clone(self):
		obj=CThostFtdcBrokerUserPasswordField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.Password=self.Password
		return obj

class CThostFtdcBrokerUserFunctionField(Structure):
	"""经纪公司用户功能权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#经纪公司功能代码
		("BrokerFunctionCode",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getBrokerFunctionCode(self):
		return BrokerFunctionCodeType(ord(self.BrokerFunctionCode))

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', BrokerFunctionCode=BrokerFunctionCodeType.{2}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.BrokerFunctionCode) == 0 else BrokerFunctionCodeType(ord(self.BrokerFunctionCode)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'BrokerFunctionCode':'' if ord(self.BrokerFunctionCode) == 0 else BrokerFunctionCodeType(ord(self.BrokerFunctionCode)).name}

	def clone(self):
		obj=CThostFtdcBrokerUserFunctionField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.BrokerFunctionCode=self.BrokerFunctionCode
		return obj

class CThostFtdcTraderOfferField(Structure):
	"""交易所交易员报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所交易员连接状态
		("TraderConnectStatus",c_char),
		#发出连接请求的日期
		("ConnectRequestDate",c_char*9),
		#发出连接请求的时间
		("ConnectRequestTime",c_char*9),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#完成连接日期
		("ConnectDate",c_char*9),
		#完成连接时间
		("ConnectTime",c_char*9),
		#启动日期
		("StartDate",c_char*9),
		#启动时间
		("StartTime",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#本席位最大成交编号
		("MaxTradeID",c_char*21),
		#本席位最大报单备拷
		("MaxOrderMessageReference",c_char*7),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getTraderConnectStatus(self):
		return TraderConnectStatusType(ord(self.TraderConnectStatus))
	def getConnectRequestDate(self):
		return str(self.ConnectRequestDate, 'GB2312')
	def getConnectRequestTime(self):
		return str(self.ConnectRequestTime, 'GB2312')
	def getLastReportDate(self):
		return str(self.LastReportDate, 'GB2312')
	def getLastReportTime(self):
		return str(self.LastReportTime, 'GB2312')
	def getConnectDate(self):
		return str(self.ConnectDate, 'GB2312')
	def getConnectTime(self):
		return str(self.ConnectTime, 'GB2312')
	def getStartDate(self):
		return str(self.StartDate, 'GB2312')
	def getStartTime(self):
		return str(self.StartTime, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getMaxTradeID(self):
		return str(self.MaxTradeID, 'GB2312')
	def getMaxOrderMessageReference(self):
		return str(self.MaxOrderMessageReference, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', TraderID=\'{1}\', ParticipantID=\'{2}\', Password=\'{3}\', InstallID={4}, OrderLocalID=\'{5}\', TraderConnectStatus=TraderConnectStatusType.{6}, ConnectRequestDate=\'{7}\', ConnectRequestTime=\'{8}\', LastReportDate=\'{9}\', LastReportTime=\'{10}\', ConnectDate=\'{11}\', ConnectTime=\'{12}\', StartDate=\'{13}\', StartTime=\'{14}\', TradingDay=\'{15}\', BrokerID=\'{16}\', MaxTradeID=\'{17}\', MaxOrderMessageReference=\'{18}\''.format(str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), '' if ord(self.TraderConnectStatus) == 0 else TraderConnectStatusType(ord(self.TraderConnectStatus)).name, str(self.ConnectRequestDate, 'GB2312'), str(self.ConnectRequestTime, 'GB2312'), str(self.LastReportDate, 'GB2312'), str(self.LastReportTime, 'GB2312'), str(self.ConnectDate, 'GB2312'), str(self.ConnectTime, 'GB2312'), str(self.StartDate, 'GB2312'), str(self.StartTime, 'GB2312'), str(self.TradingDay, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.MaxTradeID, 'GB2312'), str(self.MaxOrderMessageReference, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'TraderConnectStatus':'' if ord(self.TraderConnectStatus) == 0 else TraderConnectStatusType(ord(self.TraderConnectStatus)).name,'ConnectRequestDate':str(self.ConnectRequestDate, 'GB2312'),'ConnectRequestTime':str(self.ConnectRequestTime, 'GB2312'),'LastReportDate':str(self.LastReportDate, 'GB2312'),'LastReportTime':str(self.LastReportTime, 'GB2312'),'ConnectDate':str(self.ConnectDate, 'GB2312'),'ConnectTime':str(self.ConnectTime, 'GB2312'),'StartDate':str(self.StartDate, 'GB2312'),'StartTime':str(self.StartTime, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'MaxTradeID':str(self.MaxTradeID, 'GB2312'),'MaxOrderMessageReference':str(self.MaxOrderMessageReference, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTraderOfferField()
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		obj.ParticipantID=self.ParticipantID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.TraderConnectStatus=self.TraderConnectStatus
		obj.ConnectRequestDate=self.ConnectRequestDate
		obj.ConnectRequestTime=self.ConnectRequestTime
		obj.LastReportDate=self.LastReportDate
		obj.LastReportTime=self.LastReportTime
		obj.ConnectDate=self.ConnectDate
		obj.ConnectTime=self.ConnectTime
		obj.StartDate=self.StartDate
		obj.StartTime=self.StartTime
		obj.TradingDay=self.TradingDay
		obj.BrokerID=self.BrokerID
		obj.MaxTradeID=self.MaxTradeID
		obj.MaxOrderMessageReference=self.MaxOrderMessageReference
		return obj

class CThostFtdcSettlementInfoField(Structure):
	"""投资者结算结果"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#序号
		("SequenceNo",c_int32),
		#消息正文
		("Content",c_char*501),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getContent(self):
		return str(self.Content, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', SettlementID={1}, BrokerID=\'{2}\', InvestorID=\'{3}\', SequenceNo={4}, Content=\'{5}\''.format(str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.SequenceNo, str(self.Content, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'SequenceNo':self.SequenceNo,'Content':str(self.Content, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSettlementInfoField()
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.SequenceNo=self.SequenceNo
		obj.Content=self.Content
		return obj

class CThostFtdcInstrumentMarginRateAdjustField(Structure):
	"""合约保证金率调整"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', HedgeFlag=HedgeFlagType.{4}, LongMarginRatioByMoney={5}, LongMarginRatioByVolume={6}, ShortMarginRatioByMoney={7}, ShortMarginRatioByVolume={8}, IsRelative={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.LongMarginRatioByMoney, self.LongMarginRatioByVolume, self.ShortMarginRatioByMoney, self.ShortMarginRatioByVolume, self.IsRelative)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'LongMarginRatioByMoney':self.LongMarginRatioByMoney,'LongMarginRatioByVolume':self.LongMarginRatioByVolume,'ShortMarginRatioByMoney':self.ShortMarginRatioByMoney,'ShortMarginRatioByVolume':self.ShortMarginRatioByVolume,'IsRelative':self.IsRelative}

	def clone(self):
		obj=CThostFtdcInstrumentMarginRateAdjustField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.HedgeFlag=self.HedgeFlag
		obj.LongMarginRatioByMoney=self.LongMarginRatioByMoney
		obj.LongMarginRatioByVolume=self.LongMarginRatioByVolume
		obj.ShortMarginRatioByMoney=self.ShortMarginRatioByMoney
		obj.ShortMarginRatioByVolume=self.ShortMarginRatioByVolume
		obj.IsRelative=self.IsRelative
		return obj

class CThostFtdcExchangeMarginRateField(Structure):
	"""交易所保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', HedgeFlag=HedgeFlagType.{2}, LongMarginRatioByMoney={3}, LongMarginRatioByVolume={4}, ShortMarginRatioByMoney={5}, ShortMarginRatioByVolume={6}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.LongMarginRatioByMoney, self.LongMarginRatioByVolume, self.ShortMarginRatioByMoney, self.ShortMarginRatioByVolume)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'LongMarginRatioByMoney':self.LongMarginRatioByMoney,'LongMarginRatioByVolume':self.LongMarginRatioByVolume,'ShortMarginRatioByMoney':self.ShortMarginRatioByMoney,'ShortMarginRatioByVolume':self.ShortMarginRatioByVolume}

	def clone(self):
		obj=CThostFtdcExchangeMarginRateField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		obj.LongMarginRatioByMoney=self.LongMarginRatioByMoney
		obj.LongMarginRatioByVolume=self.LongMarginRatioByVolume
		obj.ShortMarginRatioByMoney=self.ShortMarginRatioByMoney
		obj.ShortMarginRatioByVolume=self.ShortMarginRatioByVolume
		return obj

class CThostFtdcExchangeMarginRateAdjustField(Structure):
	"""交易所保证金率调整"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#跟随交易所投资者多头保证金率
		("LongMarginRatioByMoney",c_double),
		#跟随交易所投资者多头保证金费
		("LongMarginRatioByVolume",c_double),
		#跟随交易所投资者空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#跟随交易所投资者空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#交易所多头保证金率
		("ExchLongMarginRatioByMoney",c_double),
		#交易所多头保证金费
		("ExchLongMarginRatioByVolume",c_double),
		#交易所空头保证金率
		("ExchShortMarginRatioByMoney",c_double),
		#交易所空头保证金费
		("ExchShortMarginRatioByVolume",c_double),
		#不跟随交易所投资者多头保证金率
		("NoLongMarginRatioByMoney",c_double),
		#不跟随交易所投资者多头保证金费
		("NoLongMarginRatioByVolume",c_double),
		#不跟随交易所投资者空头保证金率
		("NoShortMarginRatioByMoney",c_double),
		#不跟随交易所投资者空头保证金费
		("NoShortMarginRatioByVolume",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getExchLongMarginRatioByMoney(self):
		return self.ExchLongMarginRatioByMoney
	def getExchLongMarginRatioByVolume(self):
		return self.ExchLongMarginRatioByVolume
	def getExchShortMarginRatioByMoney(self):
		return self.ExchShortMarginRatioByMoney
	def getExchShortMarginRatioByVolume(self):
		return self.ExchShortMarginRatioByVolume
	def getNoLongMarginRatioByMoney(self):
		return self.NoLongMarginRatioByMoney
	def getNoLongMarginRatioByVolume(self):
		return self.NoLongMarginRatioByVolume
	def getNoShortMarginRatioByMoney(self):
		return self.NoShortMarginRatioByMoney
	def getNoShortMarginRatioByVolume(self):
		return self.NoShortMarginRatioByVolume

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', HedgeFlag=HedgeFlagType.{2}, LongMarginRatioByMoney={3}, LongMarginRatioByVolume={4}, ShortMarginRatioByMoney={5}, ShortMarginRatioByVolume={6}, ExchLongMarginRatioByMoney={7}, ExchLongMarginRatioByVolume={8}, ExchShortMarginRatioByMoney={9}, ExchShortMarginRatioByVolume={10}, NoLongMarginRatioByMoney={11}, NoLongMarginRatioByVolume={12}, NoShortMarginRatioByMoney={13}, NoShortMarginRatioByVolume={14}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.LongMarginRatioByMoney, self.LongMarginRatioByVolume, self.ShortMarginRatioByMoney, self.ShortMarginRatioByVolume, self.ExchLongMarginRatioByMoney, self.ExchLongMarginRatioByVolume, self.ExchShortMarginRatioByMoney, self.ExchShortMarginRatioByVolume, self.NoLongMarginRatioByMoney, self.NoLongMarginRatioByVolume, self.NoShortMarginRatioByMoney, self.NoShortMarginRatioByVolume)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'LongMarginRatioByMoney':self.LongMarginRatioByMoney,'LongMarginRatioByVolume':self.LongMarginRatioByVolume,'ShortMarginRatioByMoney':self.ShortMarginRatioByMoney,'ShortMarginRatioByVolume':self.ShortMarginRatioByVolume,'ExchLongMarginRatioByMoney':self.ExchLongMarginRatioByMoney,'ExchLongMarginRatioByVolume':self.ExchLongMarginRatioByVolume,'ExchShortMarginRatioByMoney':self.ExchShortMarginRatioByMoney,'ExchShortMarginRatioByVolume':self.ExchShortMarginRatioByVolume,'NoLongMarginRatioByMoney':self.NoLongMarginRatioByMoney,'NoLongMarginRatioByVolume':self.NoLongMarginRatioByVolume,'NoShortMarginRatioByMoney':self.NoShortMarginRatioByMoney,'NoShortMarginRatioByVolume':self.NoShortMarginRatioByVolume}

	def clone(self):
		obj=CThostFtdcExchangeMarginRateAdjustField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		obj.LongMarginRatioByMoney=self.LongMarginRatioByMoney
		obj.LongMarginRatioByVolume=self.LongMarginRatioByVolume
		obj.ShortMarginRatioByMoney=self.ShortMarginRatioByMoney
		obj.ShortMarginRatioByVolume=self.ShortMarginRatioByVolume
		obj.ExchLongMarginRatioByMoney=self.ExchLongMarginRatioByMoney
		obj.ExchLongMarginRatioByVolume=self.ExchLongMarginRatioByVolume
		obj.ExchShortMarginRatioByMoney=self.ExchShortMarginRatioByMoney
		obj.ExchShortMarginRatioByVolume=self.ExchShortMarginRatioByVolume
		obj.NoLongMarginRatioByMoney=self.NoLongMarginRatioByMoney
		obj.NoLongMarginRatioByVolume=self.NoLongMarginRatioByVolume
		obj.NoShortMarginRatioByMoney=self.NoShortMarginRatioByMoney
		obj.NoShortMarginRatioByVolume=self.NoShortMarginRatioByVolume
		return obj

class CThostFtdcExchangeRateField(Structure):
	"""汇率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#源币种
		("FromCurrencyID",c_char*4),
		#源币种单位数量
		("FromCurrencyUnit",c_double),
		#目标币种
		("ToCurrencyID",c_char*4),
		#汇率
		("ExchangeRate",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getFromCurrencyID(self):
		return str(self.FromCurrencyID, 'GB2312')
	def getFromCurrencyUnit(self):
		return self.FromCurrencyUnit
	def getToCurrencyID(self):
		return str(self.ToCurrencyID, 'GB2312')
	def getExchangeRate(self):
		return self.ExchangeRate

	def __str__(self):
		return 'BrokerID=\'{0}\', FromCurrencyID=\'{1}\', FromCurrencyUnit={2}, ToCurrencyID=\'{3}\', ExchangeRate={4}'.format(str(self.BrokerID, 'GB2312'), str(self.FromCurrencyID, 'GB2312'), self.FromCurrencyUnit, str(self.ToCurrencyID, 'GB2312'), self.ExchangeRate)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'FromCurrencyID':str(self.FromCurrencyID, 'GB2312'),'FromCurrencyUnit':self.FromCurrencyUnit,'ToCurrencyID':str(self.ToCurrencyID, 'GB2312'),'ExchangeRate':self.ExchangeRate}

	def clone(self):
		obj=CThostFtdcExchangeRateField()
		obj.BrokerID=self.BrokerID
		obj.FromCurrencyID=self.FromCurrencyID
		obj.FromCurrencyUnit=self.FromCurrencyUnit
		obj.ToCurrencyID=self.ToCurrencyID
		obj.ExchangeRate=self.ExchangeRate
		return obj

class CThostFtdcSettlementRefField(Structure):
	"""结算引用"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID

	def __str__(self):
		return 'TradingDay=\'{0}\', SettlementID={1}'.format(str(self.TradingDay, 'GB2312'), self.SettlementID)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID}

	def clone(self):
		obj=CThostFtdcSettlementRefField()
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		return obj

class CThostFtdcCurrentTimeField(Structure):
	"""当前时间"""
	_fields_ = [
		#当前日期
		("CurrDate",c_char*9),
		#当前时间
		("CurrTime",c_char*9),
		#当前时间（毫秒）
		("CurrMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getCurrDate(self):
		return str(self.CurrDate, 'GB2312')
	def getCurrTime(self):
		return str(self.CurrTime, 'GB2312')
	def getCurrMillisec(self):
		return self.CurrMillisec
	def getActionDay(self):
		return str(self.ActionDay, 'GB2312')

	def __str__(self):
		return 'CurrDate=\'{0}\', CurrTime=\'{1}\', CurrMillisec={2}, ActionDay=\'{3}\''.format(str(self.CurrDate, 'GB2312'), str(self.CurrTime, 'GB2312'), self.CurrMillisec, str(self.ActionDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'CurrDate':str(self.CurrDate, 'GB2312'),'CurrTime':str(self.CurrTime, 'GB2312'),'CurrMillisec':self.CurrMillisec,'ActionDay':str(self.ActionDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCurrentTimeField()
		obj.CurrDate=self.CurrDate
		obj.CurrTime=self.CurrTime
		obj.CurrMillisec=self.CurrMillisec
		obj.ActionDay=self.ActionDay
		return obj

class CThostFtdcCommPhaseField(Structure):
	"""通讯阶段"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#通讯时段编号
		("CommPhaseNo",c_int32),
		#系统编号
		("SystemID",c_char*21),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getCommPhaseNo(self):
		return self.CommPhaseNo
	def getSystemID(self):
		return str(self.SystemID, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', CommPhaseNo={1}, SystemID=\'{2}\''.format(str(self.TradingDay, 'GB2312'), self.CommPhaseNo, str(self.SystemID, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'CommPhaseNo':self.CommPhaseNo,'SystemID':str(self.SystemID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCommPhaseField()
		obj.TradingDay=self.TradingDay
		obj.CommPhaseNo=self.CommPhaseNo
		obj.SystemID=self.SystemID
		return obj

class CThostFtdcLoginInfoField(Structure):
	"""登录信息"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录日期
		("LoginDate",c_char*9),
		#登录时间
		("LoginTime",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#系统名称
		("SystemName",c_char*41),
		#密码
		("Password",c_char*41),
		#最大报单引用
		("MaxOrderRef",c_char*13),
		#上期所时间
		("SHFETime",c_char*9),
		#大商所时间
		("DCETime",c_char*9),
		#郑商所时间
		("CZCETime",c_char*9),
		#中金所时间
		("FFEXTime",c_char*9),
		#Mac地址
		("MacAddress",c_char*21),
		#动态密码
		("OneTimePassword",c_char*41),
		#能源中心时间
		("INETime",c_char*9),
		#查询时是否需要流控
		("IsQryControl",c_int32),
		#登录备注
		("LoginRemark",c_char*36),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getLoginDate(self):
		return str(self.LoginDate, 'GB2312')
	def getLoginTime(self):
		return str(self.LoginTime, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getInterfaceProductInfo(self):
		return str(self.InterfaceProductInfo, 'GB2312')
	def getProtocolInfo(self):
		return str(self.ProtocolInfo, 'GB2312')
	def getSystemName(self):
		return str(self.SystemName, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getMaxOrderRef(self):
		return str(self.MaxOrderRef, 'GB2312')
	def getSHFETime(self):
		return str(self.SHFETime, 'GB2312')
	def getDCETime(self):
		return str(self.DCETime, 'GB2312')
	def getCZCETime(self):
		return str(self.CZCETime, 'GB2312')
	def getFFEXTime(self):
		return str(self.FFEXTime, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getOneTimePassword(self):
		return str(self.OneTimePassword, 'GB2312')
	def getINETime(self):
		return str(self.INETime, 'GB2312')
	def getIsQryControl(self):
		return self.IsQryControl
	def getLoginRemark(self):
		return str(self.LoginRemark, 'GB2312')

	def __str__(self):
		return 'FrontID={0}, SessionID={1}, BrokerID=\'{2}\', UserID=\'{3}\', LoginDate=\'{4}\', LoginTime=\'{5}\', IPAddress=\'{6}\', UserProductInfo=\'{7}\', InterfaceProductInfo=\'{8}\', ProtocolInfo=\'{9}\', SystemName=\'{10}\', Password=\'{11}\', MaxOrderRef=\'{12}\', SHFETime=\'{13}\', DCETime=\'{14}\', CZCETime=\'{15}\', FFEXTime=\'{16}\', MacAddress=\'{17}\', OneTimePassword=\'{18}\', INETime=\'{19}\', IsQryControl={20}, LoginRemark=\'{21}\''.format(self.FrontID, self.SessionID, str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.LoginDate, 'GB2312'), str(self.LoginTime, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.UserProductInfo, 'GB2312'), str(self.InterfaceProductInfo, 'GB2312'), str(self.ProtocolInfo, 'GB2312'), str(self.SystemName, 'GB2312'), str(self.Password, 'GB2312'), str(self.MaxOrderRef, 'GB2312'), str(self.SHFETime, 'GB2312'), str(self.DCETime, 'GB2312'), str(self.CZCETime, 'GB2312'), str(self.FFEXTime, 'GB2312'), str(self.MacAddress, 'GB2312'), str(self.OneTimePassword, 'GB2312'), str(self.INETime, 'GB2312'), self.IsQryControl, str(self.LoginRemark, 'GB2312'))

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID,'SessionID':self.SessionID,'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'LoginDate':str(self.LoginDate, 'GB2312'),'LoginTime':str(self.LoginTime, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'InterfaceProductInfo':str(self.InterfaceProductInfo, 'GB2312'),'ProtocolInfo':str(self.ProtocolInfo, 'GB2312'),'SystemName':str(self.SystemName, 'GB2312'),'Password':str(self.Password, 'GB2312'),'MaxOrderRef':str(self.MaxOrderRef, 'GB2312'),'SHFETime':str(self.SHFETime, 'GB2312'),'DCETime':str(self.DCETime, 'GB2312'),'CZCETime':str(self.CZCETime, 'GB2312'),'FFEXTime':str(self.FFEXTime, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'OneTimePassword':str(self.OneTimePassword, 'GB2312'),'INETime':str(self.INETime, 'GB2312'),'IsQryControl':self.IsQryControl,'LoginRemark':str(self.LoginRemark, 'GB2312')}

	def clone(self):
		obj=CThostFtdcLoginInfoField()
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.LoginDate=self.LoginDate
		obj.LoginTime=self.LoginTime
		obj.IPAddress=self.IPAddress
		obj.UserProductInfo=self.UserProductInfo
		obj.InterfaceProductInfo=self.InterfaceProductInfo
		obj.ProtocolInfo=self.ProtocolInfo
		obj.SystemName=self.SystemName
		obj.Password=self.Password
		obj.MaxOrderRef=self.MaxOrderRef
		obj.SHFETime=self.SHFETime
		obj.DCETime=self.DCETime
		obj.CZCETime=self.CZCETime
		obj.FFEXTime=self.FFEXTime
		obj.MacAddress=self.MacAddress
		obj.OneTimePassword=self.OneTimePassword
		obj.INETime=self.INETime
		obj.IsQryControl=self.IsQryControl
		obj.LoginRemark=self.LoginRemark
		return obj

class CThostFtdcLogoutAllField(Structure):
	"""登录信息"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#系统名称
		("SystemName",c_char*41),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getSystemName(self):
		return str(self.SystemName, 'GB2312')

	def __str__(self):
		return 'FrontID={0}, SessionID={1}, SystemName=\'{2}\''.format(self.FrontID, self.SessionID, str(self.SystemName, 'GB2312'))

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID,'SessionID':self.SessionID,'SystemName':str(self.SystemName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcLogoutAllField()
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.SystemName=self.SystemName
		return obj

class CThostFtdcFrontStatusField(Structure):
	"""前置状态"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#是否活跃
		("IsActive",c_int32),
		]

	def getFrontID(self):
		return self.FrontID
	def getLastReportDate(self):
		return str(self.LastReportDate, 'GB2312')
	def getLastReportTime(self):
		return str(self.LastReportTime, 'GB2312')
	def getIsActive(self):
		return self.IsActive

	def __str__(self):
		return 'FrontID={0}, LastReportDate=\'{1}\', LastReportTime=\'{2}\', IsActive={3}'.format(self.FrontID, str(self.LastReportDate, 'GB2312'), str(self.LastReportTime, 'GB2312'), self.IsActive)

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID,'LastReportDate':str(self.LastReportDate, 'GB2312'),'LastReportTime':str(self.LastReportTime, 'GB2312'),'IsActive':self.IsActive}

	def clone(self):
		obj=CThostFtdcFrontStatusField()
		obj.FrontID=self.FrontID
		obj.LastReportDate=self.LastReportDate
		obj.LastReportTime=self.LastReportTime
		obj.IsActive=self.IsActive
		return obj

class CThostFtdcUserPasswordUpdateField(Structure):
	"""用户口令变更"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOldPassword(self):
		return str(self.OldPassword, 'GB2312')
	def getNewPassword(self):
		return str(self.NewPassword, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', OldPassword=\'{2}\', NewPassword=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.OldPassword, 'GB2312'), str(self.NewPassword, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OldPassword':str(self.OldPassword, 'GB2312'),'NewPassword':str(self.NewPassword, 'GB2312')}

	def clone(self):
		obj=CThostFtdcUserPasswordUpdateField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.OldPassword=self.OldPassword
		obj.NewPassword=self.NewPassword
		return obj

class CThostFtdcInputOrderField(Structure):
	"""输入报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#互换单标志
		("IsSwapOrder",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getIsSwapOrder(self):
		return self.IsSwapOrder
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', OrderPriceType=OrderPriceTypeType.{5}, Direction=DirectionType.{6}, CombOffsetFlag=\'{7}\', CombHedgeFlag=\'{8}\', LimitPrice={9}, VolumeTotalOriginal={10}, TimeCondition=TimeConditionType.{11}, GTDDate=\'{12}\', VolumeCondition=VolumeConditionType.{13}, MinVolume={14}, ContingentCondition=ContingentConditionType.{15}, StopPrice={16}, ForceCloseReason=ForceCloseReasonType.{17}, IsAutoSuspend={18}, BusinessUnit=\'{19}\', RequestID={20}, UserForceClose={21}, IsSwapOrder={22}, ExchangeID=\'{23}\', InvestUnitID=\'{24}\', AccountID=\'{25}\', CurrencyID=\'{26}\', ClientID=\'{27}\', IPAddress=\'{28}\', MacAddress=\'{29}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, self.UserForceClose, self.IsSwapOrder, str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'UserForceClose':self.UserForceClose,'IsSwapOrder':self.IsSwapOrder,'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.UserForceClose=self.UserForceClose
		obj.IsSwapOrder=self.IsSwapOrder
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcOrderField(Structure):
	"""报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#用户强评标志
		("UserForceClose",c_int32),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#相关报单
		("RelativeOrderSysID",c_char*21),
		#郑商所成交数量
		("ZCETotalTradedVolume",c_int32),
		#互换单标志
		("IsSwapOrder",c_int32),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getActiveTime(self):
		return str(self.ActiveTime, 'GB2312')
	def getSuspendTime(self):
		return str(self.SuspendTime, 'GB2312')
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getActiveTraderID(self):
		return str(self.ActiveTraderID, 'GB2312')
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getUserForceClose(self):
		return self.UserForceClose
	def getActiveUserID(self):
		return str(self.ActiveUserID, 'GB2312')
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getRelativeOrderSysID(self):
		return str(self.RelativeOrderSysID, 'GB2312')
	def getZCETotalTradedVolume(self):
		return self.ZCETotalTradedVolume
	def getIsSwapOrder(self):
		return self.IsSwapOrder
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', OrderPriceType=OrderPriceTypeType.{5}, Direction=DirectionType.{6}, CombOffsetFlag=\'{7}\', CombHedgeFlag=\'{8}\', LimitPrice={9}, VolumeTotalOriginal={10}, TimeCondition=TimeConditionType.{11}, GTDDate=\'{12}\', VolumeCondition=VolumeConditionType.{13}, MinVolume={14}, ContingentCondition=ContingentConditionType.{15}, StopPrice={16}, ForceCloseReason=ForceCloseReasonType.{17}, IsAutoSuspend={18}, BusinessUnit=\'{19}\', RequestID={20}, OrderLocalID=\'{21}\', ExchangeID=\'{22}\', ParticipantID=\'{23}\', ClientID=\'{24}\', ExchangeInstID=\'{25}\', TraderID=\'{26}\', InstallID={27}, OrderSubmitStatus=OrderSubmitStatusType.{28}, NotifySequence={29}, TradingDay=\'{30}\', SettlementID={31}, OrderSysID=\'{32}\', OrderSource=OrderSourceType.{33}, OrderStatus=OrderStatusType.{34}, OrderType=OrderTypeType.{35}, VolumeTraded={36}, VolumeTotal={37}, InsertDate=\'{38}\', InsertTime=\'{39}\', ActiveTime=\'{40}\', SuspendTime=\'{41}\', UpdateTime=\'{42}\', CancelTime=\'{43}\', ActiveTraderID=\'{44}\', ClearingPartID=\'{45}\', SequenceNo={46}, FrontID={47}, SessionID={48}, UserProductInfo=\'{49}\', StatusMsg=\'{50}\', UserForceClose={51}, ActiveUserID=\'{52}\', BrokerOrderSeq={53}, RelativeOrderSysID=\'{54}\', ZCETotalTradedVolume={55}, IsSwapOrder={56}, BranchID=\'{57}\', InvestUnitID=\'{58}\', AccountID=\'{59}\', CurrencyID=\'{60}\', IPAddress=\'{61}\', MacAddress=\'{62}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, str(self.OrderLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.OrderSysID, 'GB2312'), '' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name, '' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name, '' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name, self.VolumeTraded, self.VolumeTotal, str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.ActiveTime, 'GB2312'), str(self.SuspendTime, 'GB2312'), str(self.UpdateTime, 'GB2312'), str(self.CancelTime, 'GB2312'), str(self.ActiveTraderID, 'GB2312'), str(self.ClearingPartID, 'GB2312'), self.SequenceNo, self.FrontID, self.SessionID, str(self.UserProductInfo, 'GB2312'), str(self.StatusMsg, 'GB2312'), self.UserForceClose, str(self.ActiveUserID, 'GB2312'), self.BrokerOrderSeq, str(self.RelativeOrderSysID, 'GB2312'), self.ZCETotalTradedVolume, self.IsSwapOrder, str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'OrderSysID':str(self.OrderSysID, 'GB2312'),'OrderSource':'' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name,'OrderStatus':'' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name,'OrderType':'' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name,'VolumeTraded':self.VolumeTraded,'VolumeTotal':self.VolumeTotal,'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'ActiveTime':str(self.ActiveTime, 'GB2312'),'SuspendTime':str(self.SuspendTime, 'GB2312'),'UpdateTime':str(self.UpdateTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'ActiveTraderID':str(self.ActiveTraderID, 'GB2312'),'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'FrontID':self.FrontID,'SessionID':self.SessionID,'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'UserForceClose':self.UserForceClose,'ActiveUserID':str(self.ActiveUserID, 'GB2312'),'BrokerOrderSeq':self.BrokerOrderSeq,'RelativeOrderSysID':str(self.RelativeOrderSysID, 'GB2312'),'ZCETotalTradedVolume':self.ZCETotalTradedVolume,'IsSwapOrder':self.IsSwapOrder,'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.OrderLocalID=self.OrderLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.OrderSysID=self.OrderSysID
		obj.OrderSource=self.OrderSource
		obj.OrderStatus=self.OrderStatus
		obj.OrderType=self.OrderType
		obj.VolumeTraded=self.VolumeTraded
		obj.VolumeTotal=self.VolumeTotal
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.ActiveTime=self.ActiveTime
		obj.SuspendTime=self.SuspendTime
		obj.UpdateTime=self.UpdateTime
		obj.CancelTime=self.CancelTime
		obj.ActiveTraderID=self.ActiveTraderID
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.UserProductInfo=self.UserProductInfo
		obj.StatusMsg=self.StatusMsg
		obj.UserForceClose=self.UserForceClose
		obj.ActiveUserID=self.ActiveUserID
		obj.BrokerOrderSeq=self.BrokerOrderSeq
		obj.RelativeOrderSysID=self.RelativeOrderSysID
		obj.ZCETotalTradedVolume=self.ZCETotalTradedVolume
		obj.IsSwapOrder=self.IsSwapOrder
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExchangeOrderField(Structure):
	"""交易所报单"""
	_fields_ = [
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#营业部编号
		("BranchID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getActiveTime(self):
		return str(self.ActiveTime, 'GB2312')
	def getSuspendTime(self):
		return str(self.SuspendTime, 'GB2312')
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getActiveTraderID(self):
		return str(self.ActiveTraderID, 'GB2312')
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'OrderPriceType=OrderPriceTypeType.{0}, Direction=DirectionType.{1}, CombOffsetFlag=\'{2}\', CombHedgeFlag=\'{3}\', LimitPrice={4}, VolumeTotalOriginal={5}, TimeCondition=TimeConditionType.{6}, GTDDate=\'{7}\', VolumeCondition=VolumeConditionType.{8}, MinVolume={9}, ContingentCondition=ContingentConditionType.{10}, StopPrice={11}, ForceCloseReason=ForceCloseReasonType.{12}, IsAutoSuspend={13}, BusinessUnit=\'{14}\', RequestID={15}, OrderLocalID=\'{16}\', ExchangeID=\'{17}\', ParticipantID=\'{18}\', ClientID=\'{19}\', ExchangeInstID=\'{20}\', TraderID=\'{21}\', InstallID={22}, OrderSubmitStatus=OrderSubmitStatusType.{23}, NotifySequence={24}, TradingDay=\'{25}\', SettlementID={26}, OrderSysID=\'{27}\', OrderSource=OrderSourceType.{28}, OrderStatus=OrderStatusType.{29}, OrderType=OrderTypeType.{30}, VolumeTraded={31}, VolumeTotal={32}, InsertDate=\'{33}\', InsertTime=\'{34}\', ActiveTime=\'{35}\', SuspendTime=\'{36}\', UpdateTime=\'{37}\', CancelTime=\'{38}\', ActiveTraderID=\'{39}\', ClearingPartID=\'{40}\', SequenceNo={41}, BranchID=\'{42}\', IPAddress=\'{43}\', MacAddress=\'{44}\''.format('' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, str(self.OrderLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.OrderSysID, 'GB2312'), '' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name, '' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name, '' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name, self.VolumeTraded, self.VolumeTotal, str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.ActiveTime, 'GB2312'), str(self.SuspendTime, 'GB2312'), str(self.UpdateTime, 'GB2312'), str(self.CancelTime, 'GB2312'), str(self.ActiveTraderID, 'GB2312'), str(self.ClearingPartID, 'GB2312'), self.SequenceNo, str(self.BranchID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'OrderSysID':str(self.OrderSysID, 'GB2312'),'OrderSource':'' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name,'OrderStatus':'' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name,'OrderType':'' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name,'VolumeTraded':self.VolumeTraded,'VolumeTotal':self.VolumeTotal,'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'ActiveTime':str(self.ActiveTime, 'GB2312'),'SuspendTime':str(self.SuspendTime, 'GB2312'),'UpdateTime':str(self.UpdateTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'ActiveTraderID':str(self.ActiveTraderID, 'GB2312'),'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'BranchID':str(self.BranchID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeOrderField()
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.OrderLocalID=self.OrderLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.OrderSysID=self.OrderSysID
		obj.OrderSource=self.OrderSource
		obj.OrderStatus=self.OrderStatus
		obj.OrderType=self.OrderType
		obj.VolumeTraded=self.VolumeTraded
		obj.VolumeTotal=self.VolumeTotal
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.ActiveTime=self.ActiveTime
		obj.SuspendTime=self.SuspendTime
		obj.UpdateTime=self.UpdateTime
		obj.CancelTime=self.CancelTime
		obj.ActiveTraderID=self.ActiveTraderID
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.BranchID=self.BranchID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExchangeOrderInsertErrorField(Structure):
	"""交易所报单插入失败"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ParticipantID=\'{1}\', TraderID=\'{2}\', InstallID={3}, OrderLocalID=\'{4}\', ErrorID={5}, ErrorMsg=\'{6}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeOrderInsertErrorField()
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcInputOrderActionField(Structure):
	"""输入报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, OrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', OrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, LimitPrice={10}, VolumeChange={11}, UserID=\'{12}\', InstrumentID=\'{13}\', InvestUnitID=\'{14}\', IPAddress=\'{15}\', MacAddress=\'{16}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, str(self.OrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, self.LimitPrice, self.VolumeChange, str(self.UserID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'OrderRef':str(self.OrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'LimitPrice':self.LimitPrice,'VolumeChange':self.VolumeChange,'UserID':str(self.UserID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.OrderRef=self.OrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeChange=self.VolumeChange
		obj.UserID=self.UserID
		obj.InstrumentID=self.InstrumentID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcOrderActionField(Structure):
	"""报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, OrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', OrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, LimitPrice={10}, VolumeChange={11}, ActionDate=\'{12}\', ActionTime=\'{13}\', TraderID=\'{14}\', InstallID={15}, OrderLocalID=\'{16}\', ActionLocalID=\'{17}\', ParticipantID=\'{18}\', ClientID=\'{19}\', BusinessUnit=\'{20}\', OrderActionStatus=OrderActionStatusType.{21}, UserID=\'{22}\', StatusMsg=\'{23}\', InstrumentID=\'{24}\', BranchID=\'{25}\', InvestUnitID=\'{26}\', IPAddress=\'{27}\', MacAddress=\'{28}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, str(self.OrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, self.LimitPrice, self.VolumeChange, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'OrderRef':str(self.OrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'LimitPrice':self.LimitPrice,'VolumeChange':self.VolumeChange,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.OrderRef=self.OrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeChange=self.VolumeChange
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.StatusMsg=self.StatusMsg
		obj.InstrumentID=self.InstrumentID
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExchangeOrderActionField(Structure):
	"""交易所报单操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#营业部编号
		("BranchID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', OrderSysID=\'{1}\', ActionFlag=ActionFlagType.{2}, LimitPrice={3}, VolumeChange={4}, ActionDate=\'{5}\', ActionTime=\'{6}\', TraderID=\'{7}\', InstallID={8}, OrderLocalID=\'{9}\', ActionLocalID=\'{10}\', ParticipantID=\'{11}\', ClientID=\'{12}\', BusinessUnit=\'{13}\', OrderActionStatus=OrderActionStatusType.{14}, UserID=\'{15}\', BranchID=\'{16}\', IPAddress=\'{17}\', MacAddress=\'{18}\''.format(str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, self.LimitPrice, self.VolumeChange, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'LimitPrice':self.LimitPrice,'VolumeChange':self.VolumeChange,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeOrderActionField()
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeChange=self.VolumeChange
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.BranchID=self.BranchID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExchangeOrderActionErrorField(Structure):
	"""交易所报单操作失败"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', OrderSysID=\'{1}\', TraderID=\'{2}\', InstallID={3}, OrderLocalID=\'{4}\', ActionLocalID=\'{5}\', ErrorID={6}, ErrorMsg=\'{7}\''.format(str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeOrderActionErrorField()
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcExchangeTradeField(Structure):
	"""交易所成交"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#买卖方向
		("Direction",c_char),
		#报单编号
		("OrderSysID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易角色
		("TradingRole",c_char),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#价格
		("Price",c_double),
		#数量
		("Volume",c_int32),
		#成交时期
		("TradeDate",c_char*9),
		#成交时间
		("TradeTime",c_char*9),
		#成交类型
		("TradeType",c_char),
		#成交价来源
		("PriceSource",c_char),
		#交易所交易员代码
		("TraderID",c_char*21),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#序号
		("SequenceNo",c_int32),
		#成交来源
		("TradeSource",c_char),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTradeID(self):
		return str(self.TradeID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getTradingRole(self):
		return TradingRoleType(ord(self.TradingRole))
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPrice(self):
		return self.Price
	def getVolume(self):
		return self.Volume
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getPriceSource(self):
		return PriceSourceType(ord(self.PriceSource))
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getTradeSource(self):
		return TradeSourceType(ord(self.TradeSource))

	def __str__(self):
		return 'ExchangeID=\'{0}\', TradeID=\'{1}\', Direction=DirectionType.{2}, OrderSysID=\'{3}\', ParticipantID=\'{4}\', ClientID=\'{5}\', TradingRole=TradingRoleType.{6}, ExchangeInstID=\'{7}\', OffsetFlag=OffsetFlagType.{8}, HedgeFlag=HedgeFlagType.{9}, Price={10}, Volume={11}, TradeDate=\'{12}\', TradeTime=\'{13}\', TradeType=TradeTypeType.{14}, PriceSource=PriceSourceType.{15}, TraderID=\'{16}\', OrderLocalID=\'{17}\', ClearingPartID=\'{18}\', BusinessUnit=\'{19}\', SequenceNo={20}, TradeSource=TradeSourceType.{21}'.format(str(self.ExchangeID, 'GB2312'), str(self.TradeID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.OrderSysID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), '' if ord(self.TradingRole) == 0 else TradingRoleType(ord(self.TradingRole)).name, str(self.ExchangeInstID, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.Price, self.Volume, str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), '' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name, '' if ord(self.PriceSource) == 0 else PriceSourceType(ord(self.PriceSource)).name, str(self.TraderID, 'GB2312'), str(self.OrderLocalID, 'GB2312'), str(self.ClearingPartID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), self.SequenceNo, '' if ord(self.TradeSource) == 0 else TradeSourceType(ord(self.TradeSource)).name)

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'TradeID':str(self.TradeID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'OrderSysID':str(self.OrderSysID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'TradingRole':'' if ord(self.TradingRole) == 0 else TradingRoleType(ord(self.TradingRole)).name,'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'Price':self.Price,'Volume':self.Volume,'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'TradeType':'' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name,'PriceSource':'' if ord(self.PriceSource) == 0 else PriceSourceType(ord(self.PriceSource)).name,'TraderID':str(self.TraderID, 'GB2312'),'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'SequenceNo':self.SequenceNo,'TradeSource':'' if ord(self.TradeSource) == 0 else TradeSourceType(ord(self.TradeSource)).name}

	def clone(self):
		obj=CThostFtdcExchangeTradeField()
		obj.ExchangeID=self.ExchangeID
		obj.TradeID=self.TradeID
		obj.Direction=self.Direction
		obj.OrderSysID=self.OrderSysID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.TradingRole=self.TradingRole
		obj.ExchangeInstID=self.ExchangeInstID
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.Price=self.Price
		obj.Volume=self.Volume
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.TradeType=self.TradeType
		obj.PriceSource=self.PriceSource
		obj.TraderID=self.TraderID
		obj.OrderLocalID=self.OrderLocalID
		obj.ClearingPartID=self.ClearingPartID
		obj.BusinessUnit=self.BusinessUnit
		obj.SequenceNo=self.SequenceNo
		obj.TradeSource=self.TradeSource
		return obj

class CThostFtdcTradeField(Structure):
	"""成交"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#买卖方向
		("Direction",c_char),
		#报单编号
		("OrderSysID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易角色
		("TradingRole",c_char),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#价格
		("Price",c_double),
		#数量
		("Volume",c_int32),
		#成交时期
		("TradeDate",c_char*9),
		#成交时间
		("TradeTime",c_char*9),
		#成交类型
		("TradeType",c_char),
		#成交价来源
		("PriceSource",c_char),
		#交易所交易员代码
		("TraderID",c_char*21),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#序号
		("SequenceNo",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#成交来源
		("TradeSource",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTradeID(self):
		return str(self.TradeID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getTradingRole(self):
		return TradingRoleType(ord(self.TradingRole))
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPrice(self):
		return self.Price
	def getVolume(self):
		return self.Volume
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getPriceSource(self):
		return PriceSourceType(ord(self.PriceSource))
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getTradeSource(self):
		return TradeSourceType(ord(self.TradeSource))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', ExchangeID=\'{5}\', TradeID=\'{6}\', Direction=DirectionType.{7}, OrderSysID=\'{8}\', ParticipantID=\'{9}\', ClientID=\'{10}\', TradingRole=TradingRoleType.{11}, ExchangeInstID=\'{12}\', OffsetFlag=OffsetFlagType.{13}, HedgeFlag=HedgeFlagType.{14}, Price={15}, Volume={16}, TradeDate=\'{17}\', TradeTime=\'{18}\', TradeType=TradeTypeType.{19}, PriceSource=PriceSourceType.{20}, TraderID=\'{21}\', OrderLocalID=\'{22}\', ClearingPartID=\'{23}\', BusinessUnit=\'{24}\', SequenceNo={25}, TradingDay=\'{26}\', SettlementID={27}, BrokerOrderSeq={28}, TradeSource=TradeSourceType.{29}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TradeID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.OrderSysID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), '' if ord(self.TradingRole) == 0 else TradingRoleType(ord(self.TradingRole)).name, str(self.ExchangeInstID, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.Price, self.Volume, str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), '' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name, '' if ord(self.PriceSource) == 0 else PriceSourceType(ord(self.PriceSource)).name, str(self.TraderID, 'GB2312'), str(self.OrderLocalID, 'GB2312'), str(self.ClearingPartID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), self.SequenceNo, str(self.TradingDay, 'GB2312'), self.SettlementID, self.BrokerOrderSeq, '' if ord(self.TradeSource) == 0 else TradeSourceType(ord(self.TradeSource)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TradeID':str(self.TradeID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'OrderSysID':str(self.OrderSysID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'TradingRole':'' if ord(self.TradingRole) == 0 else TradingRoleType(ord(self.TradingRole)).name,'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'Price':self.Price,'Volume':self.Volume,'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'TradeType':'' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name,'PriceSource':'' if ord(self.PriceSource) == 0 else PriceSourceType(ord(self.PriceSource)).name,'TraderID':str(self.TraderID, 'GB2312'),'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'SequenceNo':self.SequenceNo,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'BrokerOrderSeq':self.BrokerOrderSeq,'TradeSource':'' if ord(self.TradeSource) == 0 else TradeSourceType(ord(self.TradeSource)).name}

	def clone(self):
		obj=CThostFtdcTradeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.ExchangeID=self.ExchangeID
		obj.TradeID=self.TradeID
		obj.Direction=self.Direction
		obj.OrderSysID=self.OrderSysID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.TradingRole=self.TradingRole
		obj.ExchangeInstID=self.ExchangeInstID
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.Price=self.Price
		obj.Volume=self.Volume
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.TradeType=self.TradeType
		obj.PriceSource=self.PriceSource
		obj.TraderID=self.TraderID
		obj.OrderLocalID=self.OrderLocalID
		obj.ClearingPartID=self.ClearingPartID
		obj.BusinessUnit=self.BusinessUnit
		obj.SequenceNo=self.SequenceNo
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.BrokerOrderSeq=self.BrokerOrderSeq
		obj.TradeSource=self.TradeSource
		return obj

class CThostFtdcUserSessionField(Structure):
	"""用户会话"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录日期
		("LoginDate",c_char*9),
		#登录时间
		("LoginTime",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#接口端产品信息
		("InterfaceProductInfo",c_char*11),
		#协议信息
		("ProtocolInfo",c_char*11),
		#Mac地址
		("MacAddress",c_char*21),
		#登录备注
		("LoginRemark",c_char*36),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getLoginDate(self):
		return str(self.LoginDate, 'GB2312')
	def getLoginTime(self):
		return str(self.LoginTime, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getInterfaceProductInfo(self):
		return str(self.InterfaceProductInfo, 'GB2312')
	def getProtocolInfo(self):
		return str(self.ProtocolInfo, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getLoginRemark(self):
		return str(self.LoginRemark, 'GB2312')

	def __str__(self):
		return 'FrontID={0}, SessionID={1}, BrokerID=\'{2}\', UserID=\'{3}\', LoginDate=\'{4}\', LoginTime=\'{5}\', IPAddress=\'{6}\', UserProductInfo=\'{7}\', InterfaceProductInfo=\'{8}\', ProtocolInfo=\'{9}\', MacAddress=\'{10}\', LoginRemark=\'{11}\''.format(self.FrontID, self.SessionID, str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.LoginDate, 'GB2312'), str(self.LoginTime, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.UserProductInfo, 'GB2312'), str(self.InterfaceProductInfo, 'GB2312'), str(self.ProtocolInfo, 'GB2312'), str(self.MacAddress, 'GB2312'), str(self.LoginRemark, 'GB2312'))

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID,'SessionID':self.SessionID,'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'LoginDate':str(self.LoginDate, 'GB2312'),'LoginTime':str(self.LoginTime, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'InterfaceProductInfo':str(self.InterfaceProductInfo, 'GB2312'),'ProtocolInfo':str(self.ProtocolInfo, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'LoginRemark':str(self.LoginRemark, 'GB2312')}

	def clone(self):
		obj=CThostFtdcUserSessionField()
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.LoginDate=self.LoginDate
		obj.LoginTime=self.LoginTime
		obj.IPAddress=self.IPAddress
		obj.UserProductInfo=self.UserProductInfo
		obj.InterfaceProductInfo=self.InterfaceProductInfo
		obj.ProtocolInfo=self.ProtocolInfo
		obj.MacAddress=self.MacAddress
		obj.LoginRemark=self.LoginRemark
		return obj

class CThostFtdcQueryMaxOrderVolumeField(Structure):
	"""查询最大报单数量"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#最大允许报单数量
		("MaxVolume",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getMaxVolume(self):
		return self.MaxVolume

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', Direction=DirectionType.{3}, OffsetFlag=OffsetFlagType.{4}, HedgeFlag=HedgeFlagType.{5}, MaxVolume={6}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.MaxVolume)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'MaxVolume':self.MaxVolume}

	def clone(self):
		obj=CThostFtdcQueryMaxOrderVolumeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.Direction=self.Direction
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.MaxVolume=self.MaxVolume
		return obj

class CThostFtdcSettlementInfoConfirmField(Structure):
	"""投资者结算结果确认信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#确认日期
		("ConfirmDate",c_char*9),
		#确认时间
		("ConfirmTime",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getConfirmDate(self):
		return str(self.ConfirmDate, 'GB2312')
	def getConfirmTime(self):
		return str(self.ConfirmTime, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ConfirmDate=\'{2}\', ConfirmTime=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ConfirmDate, 'GB2312'), str(self.ConfirmTime, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ConfirmDate':str(self.ConfirmDate, 'GB2312'),'ConfirmTime':str(self.ConfirmTime, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSettlementInfoConfirmField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ConfirmDate=self.ConfirmDate
		obj.ConfirmTime=self.ConfirmTime
		return obj

class CThostFtdcSyncDepositField(Structure):
	"""出入金同步"""
	_fields_ = [
		#出入金流水号
		("DepositSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#入金金额
		("Deposit",c_double),
		#是否强制进行
		("IsForce",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getDepositSeqNo(self):
		return str(self.DepositSeqNo, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getDeposit(self):
		return self.Deposit
	def getIsForce(self):
		return self.IsForce
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'DepositSeqNo=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', Deposit={3}, IsForce={4}, CurrencyID=\'{5}\''.format(str(self.DepositSeqNo, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.Deposit, self.IsForce, str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'DepositSeqNo':str(self.DepositSeqNo, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Deposit':self.Deposit,'IsForce':self.IsForce,'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSyncDepositField()
		obj.DepositSeqNo=self.DepositSeqNo
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Deposit=self.Deposit
		obj.IsForce=self.IsForce
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcSyncFundMortgageField(Structure):
	"""货币质押同步"""
	_fields_ = [
		#货币质押流水号
		("MortgageSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#源币种
		("FromCurrencyID",c_char*4),
		#质押金额
		("MortgageAmount",c_double),
		#目标币种
		("ToCurrencyID",c_char*4),
		]

	def getMortgageSeqNo(self):
		return str(self.MortgageSeqNo, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getFromCurrencyID(self):
		return str(self.FromCurrencyID, 'GB2312')
	def getMortgageAmount(self):
		return self.MortgageAmount
	def getToCurrencyID(self):
		return str(self.ToCurrencyID, 'GB2312')

	def __str__(self):
		return 'MortgageSeqNo=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', FromCurrencyID=\'{3}\', MortgageAmount={4}, ToCurrencyID=\'{5}\''.format(str(self.MortgageSeqNo, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.FromCurrencyID, 'GB2312'), self.MortgageAmount, str(self.ToCurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'MortgageSeqNo':str(self.MortgageSeqNo, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'FromCurrencyID':str(self.FromCurrencyID, 'GB2312'),'MortgageAmount':self.MortgageAmount,'ToCurrencyID':str(self.ToCurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSyncFundMortgageField()
		obj.MortgageSeqNo=self.MortgageSeqNo
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.FromCurrencyID=self.FromCurrencyID
		obj.MortgageAmount=self.MortgageAmount
		obj.ToCurrencyID=self.ToCurrencyID
		return obj

class CThostFtdcBrokerSyncField(Structure):
	"""经纪公司同步"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcBrokerSyncField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcSyncingInvestorField(Structure):
	"""正在同步中的投资者"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者名称
		("InvestorName",c_char*81),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#是否活跃
		("IsActive",c_int32),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#开户日期
		("OpenDate",c_char*9),
		#手机
		("Mobile",c_char*41),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorGroupID(self):
		return str(self.InvestorGroupID, 'GB2312')
	def getInvestorName(self):
		return str(self.InvestorName, 'GB2312')
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getIsActive(self):
		return self.IsActive
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getOpenDate(self):
		return str(self.OpenDate, 'GB2312')
	def getMobile(self):
		return str(self.Mobile, 'GB2312')
	def getCommModelID(self):
		return str(self.CommModelID, 'GB2312')
	def getMarginModelID(self):
		return str(self.MarginModelID, 'GB2312')

	def __str__(self):
		return 'InvestorID=\'{0}\', BrokerID=\'{1}\', InvestorGroupID=\'{2}\', InvestorName=\'{3}\', IdentifiedCardType=IdCardTypeType.{4}, IdentifiedCardNo=\'{5}\', IsActive={6}, Telephone=\'{7}\', Address=\'{8}\', OpenDate=\'{9}\', Mobile=\'{10}\', CommModelID=\'{11}\', MarginModelID=\'{12}\''.format(str(self.InvestorID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorGroupID, 'GB2312'), str(self.InvestorName, 'GB2312'), '' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), self.IsActive, str(self.Telephone, 'GB2312'), str(self.Address, 'GB2312'), str(self.OpenDate, 'GB2312'), str(self.Mobile, 'GB2312'), str(self.CommModelID, 'GB2312'), str(self.MarginModelID, 'GB2312'))

	@property
	def __dict__(self):
		return {'InvestorID':str(self.InvestorID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorGroupID':str(self.InvestorGroupID, 'GB2312'),'InvestorName':str(self.InvestorName, 'GB2312'),'IdentifiedCardType':'' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'IsActive':self.IsActive,'Telephone':str(self.Telephone, 'GB2312'),'Address':str(self.Address, 'GB2312'),'OpenDate':str(self.OpenDate, 'GB2312'),'Mobile':str(self.Mobile, 'GB2312'),'CommModelID':str(self.CommModelID, 'GB2312'),'MarginModelID':str(self.MarginModelID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSyncingInvestorField()
		obj.InvestorID=self.InvestorID
		obj.BrokerID=self.BrokerID
		obj.InvestorGroupID=self.InvestorGroupID
		obj.InvestorName=self.InvestorName
		obj.IdentifiedCardType=self.IdentifiedCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.IsActive=self.IsActive
		obj.Telephone=self.Telephone
		obj.Address=self.Address
		obj.OpenDate=self.OpenDate
		obj.Mobile=self.Mobile
		obj.CommModelID=self.CommModelID
		obj.MarginModelID=self.MarginModelID
		return obj

class CThostFtdcSyncingTradingCodeField(Structure):
	"""正在同步中的交易代码"""
	_fields_ = [
		#投资者代码
		("InvestorID",c_char*13),
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#是否活跃
		("IsActive",c_int32),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIsActive(self):
		return self.IsActive
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

	def __str__(self):
		return 'InvestorID=\'{0}\', BrokerID=\'{1}\', ExchangeID=\'{2}\', ClientID=\'{3}\', IsActive={4}, ClientIDType=ClientIDTypeType.{5}'.format(str(self.InvestorID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ClientID, 'GB2312'), self.IsActive, '' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name)

	@property
	def __dict__(self):
		return {'InvestorID':str(self.InvestorID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IsActive':self.IsActive,'ClientIDType':'' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name}

	def clone(self):
		obj=CThostFtdcSyncingTradingCodeField()
		obj.InvestorID=self.InvestorID
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		obj.ClientID=self.ClientID
		obj.IsActive=self.IsActive
		obj.ClientIDType=self.ClientIDType
		return obj

class CThostFtdcSyncingInvestorGroupField(Structure):
	"""正在同步中的投资者分组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者分组代码
		("InvestorGroupID",c_char*13),
		#投资者分组名称
		("InvestorGroupName",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorGroupID(self):
		return str(self.InvestorGroupID, 'GB2312')
	def getInvestorGroupName(self):
		return str(self.InvestorGroupName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorGroupID=\'{1}\', InvestorGroupName=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorGroupID, 'GB2312'), str(self.InvestorGroupName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorGroupID':str(self.InvestorGroupID, 'GB2312'),'InvestorGroupName':str(self.InvestorGroupName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSyncingInvestorGroupField()
		obj.BrokerID=self.BrokerID
		obj.InvestorGroupID=self.InvestorGroupID
		obj.InvestorGroupName=self.InvestorGroupName
		return obj

class CThostFtdcSyncingTradingAccountField(Structure):
	"""正在同步中的交易账号"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#上次质押金额
		("PreMortgage",c_double),
		#上次信用额度
		("PreCredit",c_double),
		#上次存款额
		("PreDeposit",c_double),
		#上次结算准备金
		("PreBalance",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#利息基数
		("InterestBase",c_double),
		#利息收入
		("Interest",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#可用资金
		("Available",c_double),
		#可取资金
		("WithdrawQuota",c_double),
		#基本准备金
		("Reserve",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#信用额度
		("Credit",c_double),
		#质押金额
		("Mortgage",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#投资者交割保证金
		("DeliveryMargin",c_double),
		#交易所交割保证金
		("ExchangeDeliveryMargin",c_double),
		#保底期货结算准备金
		("ReserveBalance",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#上次货币质入金额
		("PreFundMortgageIn",c_double),
		#上次货币质出金额
		("PreFundMortgageOut",c_double),
		#货币质入金额
		("FundMortgageIn",c_double),
		#货币质出金额
		("FundMortgageOut",c_double),
		#货币质押余额
		("FundMortgageAvailable",c_double),
		#可质押货币金额
		("MortgageableFund",c_double),
		#特殊产品占用保证金
		("SpecProductMargin",c_double),
		#特殊产品冻结保证金
		("SpecProductFrozenMargin",c_double),
		#特殊产品手续费
		("SpecProductCommission",c_double),
		#特殊产品冻结手续费
		("SpecProductFrozenCommission",c_double),
		#特殊产品持仓盈亏
		("SpecProductPositionProfit",c_double),
		#特殊产品平仓盈亏
		("SpecProductCloseProfit",c_double),
		#根据持仓盈亏算法计算的特殊产品持仓盈亏
		("SpecProductPositionProfitByAlg",c_double),
		#特殊产品交易所保证金
		("SpecProductExchangeMargin",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPreMortgage(self):
		return self.PreMortgage
	def getPreCredit(self):
		return self.PreCredit
	def getPreDeposit(self):
		return self.PreDeposit
	def getPreBalance(self):
		return self.PreBalance
	def getPreMargin(self):
		return self.PreMargin
	def getInterestBase(self):
		return self.InterestBase
	def getInterest(self):
		return self.Interest
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCurrMargin(self):
		return self.CurrMargin
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getBalance(self):
		return self.Balance
	def getAvailable(self):
		return self.Available
	def getWithdrawQuota(self):
		return self.WithdrawQuota
	def getReserve(self):
		return self.Reserve
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getCredit(self):
		return self.Credit
	def getMortgage(self):
		return self.Mortgage
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getDeliveryMargin(self):
		return self.DeliveryMargin
	def getExchangeDeliveryMargin(self):
		return self.ExchangeDeliveryMargin
	def getReserveBalance(self):
		return self.ReserveBalance
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getPreFundMortgageIn(self):
		return self.PreFundMortgageIn
	def getPreFundMortgageOut(self):
		return self.PreFundMortgageOut
	def getFundMortgageIn(self):
		return self.FundMortgageIn
	def getFundMortgageOut(self):
		return self.FundMortgageOut
	def getFundMortgageAvailable(self):
		return self.FundMortgageAvailable
	def getMortgageableFund(self):
		return self.MortgageableFund
	def getSpecProductMargin(self):
		return self.SpecProductMargin
	def getSpecProductFrozenMargin(self):
		return self.SpecProductFrozenMargin
	def getSpecProductCommission(self):
		return self.SpecProductCommission
	def getSpecProductFrozenCommission(self):
		return self.SpecProductFrozenCommission
	def getSpecProductPositionProfit(self):
		return self.SpecProductPositionProfit
	def getSpecProductCloseProfit(self):
		return self.SpecProductCloseProfit
	def getSpecProductPositionProfitByAlg(self):
		return self.SpecProductPositionProfitByAlg
	def getSpecProductExchangeMargin(self):
		return self.SpecProductExchangeMargin

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', PreMortgage={2}, PreCredit={3}, PreDeposit={4}, PreBalance={5}, PreMargin={6}, InterestBase={7}, Interest={8}, Deposit={9}, Withdraw={10}, FrozenMargin={11}, FrozenCash={12}, FrozenCommission={13}, CurrMargin={14}, CashIn={15}, Commission={16}, CloseProfit={17}, PositionProfit={18}, Balance={19}, Available={20}, WithdrawQuota={21}, Reserve={22}, TradingDay=\'{23}\', SettlementID={24}, Credit={25}, Mortgage={26}, ExchangeMargin={27}, DeliveryMargin={28}, ExchangeDeliveryMargin={29}, ReserveBalance={30}, CurrencyID=\'{31}\', PreFundMortgageIn={32}, PreFundMortgageOut={33}, FundMortgageIn={34}, FundMortgageOut={35}, FundMortgageAvailable={36}, MortgageableFund={37}, SpecProductMargin={38}, SpecProductFrozenMargin={39}, SpecProductCommission={40}, SpecProductFrozenCommission={41}, SpecProductPositionProfit={42}, SpecProductCloseProfit={43}, SpecProductPositionProfitByAlg={44}, SpecProductExchangeMargin={45}'.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), self.PreMortgage, self.PreCredit, self.PreDeposit, self.PreBalance, self.PreMargin, self.InterestBase, self.Interest, self.Deposit, self.Withdraw, self.FrozenMargin, self.FrozenCash, self.FrozenCommission, self.CurrMargin, self.CashIn, self.Commission, self.CloseProfit, self.PositionProfit, self.Balance, self.Available, self.WithdrawQuota, self.Reserve, str(self.TradingDay, 'GB2312'), self.SettlementID, self.Credit, self.Mortgage, self.ExchangeMargin, self.DeliveryMargin, self.ExchangeDeliveryMargin, self.ReserveBalance, str(self.CurrencyID, 'GB2312'), self.PreFundMortgageIn, self.PreFundMortgageOut, self.FundMortgageIn, self.FundMortgageOut, self.FundMortgageAvailable, self.MortgageableFund, self.SpecProductMargin, self.SpecProductFrozenMargin, self.SpecProductCommission, self.SpecProductFrozenCommission, self.SpecProductPositionProfit, self.SpecProductCloseProfit, self.SpecProductPositionProfitByAlg, self.SpecProductExchangeMargin)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'PreMortgage':self.PreMortgage,'PreCredit':self.PreCredit,'PreDeposit':self.PreDeposit,'PreBalance':self.PreBalance,'PreMargin':self.PreMargin,'InterestBase':self.InterestBase,'Interest':self.Interest,'Deposit':self.Deposit,'Withdraw':self.Withdraw,'FrozenMargin':self.FrozenMargin,'FrozenCash':self.FrozenCash,'FrozenCommission':self.FrozenCommission,'CurrMargin':self.CurrMargin,'CashIn':self.CashIn,'Commission':self.Commission,'CloseProfit':self.CloseProfit,'PositionProfit':self.PositionProfit,'Balance':self.Balance,'Available':self.Available,'WithdrawQuota':self.WithdrawQuota,'Reserve':self.Reserve,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'Credit':self.Credit,'Mortgage':self.Mortgage,'ExchangeMargin':self.ExchangeMargin,'DeliveryMargin':self.DeliveryMargin,'ExchangeDeliveryMargin':self.ExchangeDeliveryMargin,'ReserveBalance':self.ReserveBalance,'CurrencyID':str(self.CurrencyID, 'GB2312'),'PreFundMortgageIn':self.PreFundMortgageIn,'PreFundMortgageOut':self.PreFundMortgageOut,'FundMortgageIn':self.FundMortgageIn,'FundMortgageOut':self.FundMortgageOut,'FundMortgageAvailable':self.FundMortgageAvailable,'MortgageableFund':self.MortgageableFund,'SpecProductMargin':self.SpecProductMargin,'SpecProductFrozenMargin':self.SpecProductFrozenMargin,'SpecProductCommission':self.SpecProductCommission,'SpecProductFrozenCommission':self.SpecProductFrozenCommission,'SpecProductPositionProfit':self.SpecProductPositionProfit,'SpecProductCloseProfit':self.SpecProductCloseProfit,'SpecProductPositionProfitByAlg':self.SpecProductPositionProfitByAlg,'SpecProductExchangeMargin':self.SpecProductExchangeMargin}

	def clone(self):
		obj=CThostFtdcSyncingTradingAccountField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.PreMortgage=self.PreMortgage
		obj.PreCredit=self.PreCredit
		obj.PreDeposit=self.PreDeposit
		obj.PreBalance=self.PreBalance
		obj.PreMargin=self.PreMargin
		obj.InterestBase=self.InterestBase
		obj.Interest=self.Interest
		obj.Deposit=self.Deposit
		obj.Withdraw=self.Withdraw
		obj.FrozenMargin=self.FrozenMargin
		obj.FrozenCash=self.FrozenCash
		obj.FrozenCommission=self.FrozenCommission
		obj.CurrMargin=self.CurrMargin
		obj.CashIn=self.CashIn
		obj.Commission=self.Commission
		obj.CloseProfit=self.CloseProfit
		obj.PositionProfit=self.PositionProfit
		obj.Balance=self.Balance
		obj.Available=self.Available
		obj.WithdrawQuota=self.WithdrawQuota
		obj.Reserve=self.Reserve
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.Credit=self.Credit
		obj.Mortgage=self.Mortgage
		obj.ExchangeMargin=self.ExchangeMargin
		obj.DeliveryMargin=self.DeliveryMargin
		obj.ExchangeDeliveryMargin=self.ExchangeDeliveryMargin
		obj.ReserveBalance=self.ReserveBalance
		obj.CurrencyID=self.CurrencyID
		obj.PreFundMortgageIn=self.PreFundMortgageIn
		obj.PreFundMortgageOut=self.PreFundMortgageOut
		obj.FundMortgageIn=self.FundMortgageIn
		obj.FundMortgageOut=self.FundMortgageOut
		obj.FundMortgageAvailable=self.FundMortgageAvailable
		obj.MortgageableFund=self.MortgageableFund
		obj.SpecProductMargin=self.SpecProductMargin
		obj.SpecProductFrozenMargin=self.SpecProductFrozenMargin
		obj.SpecProductCommission=self.SpecProductCommission
		obj.SpecProductFrozenCommission=self.SpecProductFrozenCommission
		obj.SpecProductPositionProfit=self.SpecProductPositionProfit
		obj.SpecProductCloseProfit=self.SpecProductCloseProfit
		obj.SpecProductPositionProfitByAlg=self.SpecProductPositionProfitByAlg
		obj.SpecProductExchangeMargin=self.SpecProductExchangeMargin
		return obj

class CThostFtdcSyncingInvestorPositionField(Structure):
	"""正在同步中的投资者持仓"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#持仓多空方向
		("PosiDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#持仓日期
		("PositionDate",c_char),
		#上日持仓
		("YdPosition",c_int32),
		#今日持仓
		("Position",c_int32),
		#多头冻结
		("LongFrozen",c_int32),
		#空头冻结
		("ShortFrozen",c_int32),
		#开仓冻结金额
		("LongFrozenAmount",c_double),
		#开仓冻结金额
		("ShortFrozenAmount",c_double),
		#开仓量
		("OpenVolume",c_int32),
		#平仓量
		("CloseVolume",c_int32),
		#开仓金额
		("OpenAmount",c_double),
		#平仓金额
		("CloseAmount",c_double),
		#持仓成本
		("PositionCost",c_double),
		#上次占用的保证金
		("PreMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#资金差额
		("CashIn",c_double),
		#手续费
		("Commission",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#开仓成本
		("OpenCost",c_double),
		#交易所保证金
		("ExchangeMargin",c_double),
		#组合成交形成的持仓
		("CombPosition",c_int32),
		#组合多头冻结
		("CombLongFrozen",c_int32),
		#组合空头冻结
		("CombShortFrozen",c_int32),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#今日持仓
		("TodayPosition",c_int32),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#执行冻结
		("StrikeFrozen",c_int32),
		#执行冻结金额
		("StrikeFrozenAmount",c_double),
		#放弃执行冻结
		("AbandonFrozen",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getPositionDate(self):
		return PositionDateType(ord(self.PositionDate))
	def getYdPosition(self):
		return self.YdPosition
	def getPosition(self):
		return self.Position
	def getLongFrozen(self):
		return self.LongFrozen
	def getShortFrozen(self):
		return self.ShortFrozen
	def getLongFrozenAmount(self):
		return self.LongFrozenAmount
	def getShortFrozenAmount(self):
		return self.ShortFrozenAmount
	def getOpenVolume(self):
		return self.OpenVolume
	def getCloseVolume(self):
		return self.CloseVolume
	def getOpenAmount(self):
		return self.OpenAmount
	def getCloseAmount(self):
		return self.CloseAmount
	def getPositionCost(self):
		return self.PositionCost
	def getPreMargin(self):
		return self.PreMargin
	def getUseMargin(self):
		return self.UseMargin
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getFrozenCash(self):
		return self.FrozenCash
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCashIn(self):
		return self.CashIn
	def getCommission(self):
		return self.Commission
	def getCloseProfit(self):
		return self.CloseProfit
	def getPositionProfit(self):
		return self.PositionProfit
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getOpenCost(self):
		return self.OpenCost
	def getExchangeMargin(self):
		return self.ExchangeMargin
	def getCombPosition(self):
		return self.CombPosition
	def getCombLongFrozen(self):
		return self.CombLongFrozen
	def getCombShortFrozen(self):
		return self.CombShortFrozen
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getTodayPosition(self):
		return self.TodayPosition
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getStrikeFrozen(self):
		return self.StrikeFrozen
	def getStrikeFrozenAmount(self):
		return self.StrikeFrozenAmount
	def getAbandonFrozen(self):
		return self.AbandonFrozen

	def __str__(self):
		return 'InstrumentID=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', PosiDirection=PosiDirectionType.{3}, HedgeFlag=HedgeFlagType.{4}, PositionDate=PositionDateType.{5}, YdPosition={6}, Position={7}, LongFrozen={8}, ShortFrozen={9}, LongFrozenAmount={10}, ShortFrozenAmount={11}, OpenVolume={12}, CloseVolume={13}, OpenAmount={14}, CloseAmount={15}, PositionCost={16}, PreMargin={17}, UseMargin={18}, FrozenMargin={19}, FrozenCash={20}, FrozenCommission={21}, CashIn={22}, Commission={23}, CloseProfit={24}, PositionProfit={25}, PreSettlementPrice={26}, SettlementPrice={27}, TradingDay=\'{28}\', SettlementID={29}, OpenCost={30}, ExchangeMargin={31}, CombPosition={32}, CombLongFrozen={33}, CombShortFrozen={34}, CloseProfitByDate={35}, CloseProfitByTrade={36}, TodayPosition={37}, MarginRateByMoney={38}, MarginRateByVolume={39}, StrikeFrozen={40}, StrikeFrozenAmount={41}, AbandonFrozen={42}'.format(str(self.InstrumentID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.PositionDate) == 0 else PositionDateType(ord(self.PositionDate)).name, self.YdPosition, self.Position, self.LongFrozen, self.ShortFrozen, self.LongFrozenAmount, self.ShortFrozenAmount, self.OpenVolume, self.CloseVolume, self.OpenAmount, self.CloseAmount, self.PositionCost, self.PreMargin, self.UseMargin, self.FrozenMargin, self.FrozenCash, self.FrozenCommission, self.CashIn, self.Commission, self.CloseProfit, self.PositionProfit, self.PreSettlementPrice, self.SettlementPrice, str(self.TradingDay, 'GB2312'), self.SettlementID, self.OpenCost, self.ExchangeMargin, self.CombPosition, self.CombLongFrozen, self.CombShortFrozen, self.CloseProfitByDate, self.CloseProfitByTrade, self.TodayPosition, self.MarginRateByMoney, self.MarginRateByVolume, self.StrikeFrozen, self.StrikeFrozenAmount, self.AbandonFrozen)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'PositionDate':'' if ord(self.PositionDate) == 0 else PositionDateType(ord(self.PositionDate)).name,'YdPosition':self.YdPosition,'Position':self.Position,'LongFrozen':self.LongFrozen,'ShortFrozen':self.ShortFrozen,'LongFrozenAmount':self.LongFrozenAmount,'ShortFrozenAmount':self.ShortFrozenAmount,'OpenVolume':self.OpenVolume,'CloseVolume':self.CloseVolume,'OpenAmount':self.OpenAmount,'CloseAmount':self.CloseAmount,'PositionCost':self.PositionCost,'PreMargin':self.PreMargin,'UseMargin':self.UseMargin,'FrozenMargin':self.FrozenMargin,'FrozenCash':self.FrozenCash,'FrozenCommission':self.FrozenCommission,'CashIn':self.CashIn,'Commission':self.Commission,'CloseProfit':self.CloseProfit,'PositionProfit':self.PositionProfit,'PreSettlementPrice':self.PreSettlementPrice,'SettlementPrice':self.SettlementPrice,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'OpenCost':self.OpenCost,'ExchangeMargin':self.ExchangeMargin,'CombPosition':self.CombPosition,'CombLongFrozen':self.CombLongFrozen,'CombShortFrozen':self.CombShortFrozen,'CloseProfitByDate':self.CloseProfitByDate,'CloseProfitByTrade':self.CloseProfitByTrade,'TodayPosition':self.TodayPosition,'MarginRateByMoney':self.MarginRateByMoney,'MarginRateByVolume':self.MarginRateByVolume,'StrikeFrozen':self.StrikeFrozen,'StrikeFrozenAmount':self.StrikeFrozenAmount,'AbandonFrozen':self.AbandonFrozen}

	def clone(self):
		obj=CThostFtdcSyncingInvestorPositionField()
		obj.InstrumentID=self.InstrumentID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.PosiDirection=self.PosiDirection
		obj.HedgeFlag=self.HedgeFlag
		obj.PositionDate=self.PositionDate
		obj.YdPosition=self.YdPosition
		obj.Position=self.Position
		obj.LongFrozen=self.LongFrozen
		obj.ShortFrozen=self.ShortFrozen
		obj.LongFrozenAmount=self.LongFrozenAmount
		obj.ShortFrozenAmount=self.ShortFrozenAmount
		obj.OpenVolume=self.OpenVolume
		obj.CloseVolume=self.CloseVolume
		obj.OpenAmount=self.OpenAmount
		obj.CloseAmount=self.CloseAmount
		obj.PositionCost=self.PositionCost
		obj.PreMargin=self.PreMargin
		obj.UseMargin=self.UseMargin
		obj.FrozenMargin=self.FrozenMargin
		obj.FrozenCash=self.FrozenCash
		obj.FrozenCommission=self.FrozenCommission
		obj.CashIn=self.CashIn
		obj.Commission=self.Commission
		obj.CloseProfit=self.CloseProfit
		obj.PositionProfit=self.PositionProfit
		obj.PreSettlementPrice=self.PreSettlementPrice
		obj.SettlementPrice=self.SettlementPrice
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.OpenCost=self.OpenCost
		obj.ExchangeMargin=self.ExchangeMargin
		obj.CombPosition=self.CombPosition
		obj.CombLongFrozen=self.CombLongFrozen
		obj.CombShortFrozen=self.CombShortFrozen
		obj.CloseProfitByDate=self.CloseProfitByDate
		obj.CloseProfitByTrade=self.CloseProfitByTrade
		obj.TodayPosition=self.TodayPosition
		obj.MarginRateByMoney=self.MarginRateByMoney
		obj.MarginRateByVolume=self.MarginRateByVolume
		obj.StrikeFrozen=self.StrikeFrozen
		obj.StrikeFrozenAmount=self.StrikeFrozenAmount
		obj.AbandonFrozen=self.AbandonFrozen
		return obj

class CThostFtdcSyncingInstrumentMarginRateField(Structure):
	"""正在同步中的合约保证金率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#多头保证金率
		("LongMarginRatioByMoney",c_double),
		#多头保证金费
		("LongMarginRatioByVolume",c_double),
		#空头保证金率
		("ShortMarginRatioByMoney",c_double),
		#空头保证金费
		("ShortMarginRatioByVolume",c_double),
		#是否相对交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getLongMarginRatioByMoney(self):
		return self.LongMarginRatioByMoney
	def getLongMarginRatioByVolume(self):
		return self.LongMarginRatioByVolume
	def getShortMarginRatioByMoney(self):
		return self.ShortMarginRatioByMoney
	def getShortMarginRatioByVolume(self):
		return self.ShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', HedgeFlag=HedgeFlagType.{4}, LongMarginRatioByMoney={5}, LongMarginRatioByVolume={6}, ShortMarginRatioByMoney={7}, ShortMarginRatioByVolume={8}, IsRelative={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.LongMarginRatioByMoney, self.LongMarginRatioByVolume, self.ShortMarginRatioByMoney, self.ShortMarginRatioByVolume, self.IsRelative)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'LongMarginRatioByMoney':self.LongMarginRatioByMoney,'LongMarginRatioByVolume':self.LongMarginRatioByVolume,'ShortMarginRatioByMoney':self.ShortMarginRatioByMoney,'ShortMarginRatioByVolume':self.ShortMarginRatioByVolume,'IsRelative':self.IsRelative}

	def clone(self):
		obj=CThostFtdcSyncingInstrumentMarginRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.HedgeFlag=self.HedgeFlag
		obj.LongMarginRatioByMoney=self.LongMarginRatioByMoney
		obj.LongMarginRatioByVolume=self.LongMarginRatioByVolume
		obj.ShortMarginRatioByMoney=self.ShortMarginRatioByMoney
		obj.ShortMarginRatioByVolume=self.ShortMarginRatioByVolume
		obj.IsRelative=self.IsRelative
		return obj

class CThostFtdcSyncingInstrumentCommissionRateField(Structure):
	"""正在同步中的合约手续费率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', OpenRatioByMoney={4}, OpenRatioByVolume={5}, CloseRatioByMoney={6}, CloseRatioByVolume={7}, CloseTodayRatioByMoney={8}, CloseTodayRatioByVolume={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OpenRatioByMoney, self.OpenRatioByVolume, self.CloseRatioByMoney, self.CloseRatioByVolume, self.CloseTodayRatioByMoney, self.CloseTodayRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OpenRatioByMoney':self.OpenRatioByMoney,'OpenRatioByVolume':self.OpenRatioByVolume,'CloseRatioByMoney':self.CloseRatioByMoney,'CloseRatioByVolume':self.CloseRatioByVolume,'CloseTodayRatioByMoney':self.CloseTodayRatioByMoney,'CloseTodayRatioByVolume':self.CloseTodayRatioByVolume}

	def clone(self):
		obj=CThostFtdcSyncingInstrumentCommissionRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OpenRatioByMoney=self.OpenRatioByMoney
		obj.OpenRatioByVolume=self.OpenRatioByVolume
		obj.CloseRatioByMoney=self.CloseRatioByMoney
		obj.CloseRatioByVolume=self.CloseRatioByVolume
		obj.CloseTodayRatioByMoney=self.CloseTodayRatioByMoney
		obj.CloseTodayRatioByVolume=self.CloseTodayRatioByVolume
		return obj

class CThostFtdcSyncingInstrumentTradingRightField(Structure):
	"""正在同步中的合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', TradingRight=TradingRightType.{4}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'TradingRight':'' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name}

	def clone(self):
		obj=CThostFtdcSyncingInstrumentTradingRightField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.TradingRight=self.TradingRight
		return obj

class CThostFtdcQryOrderField(Structure):
	"""查询报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getInsertTimeStart(self):
		return str(self.InsertTimeStart, 'GB2312')
	def getInsertTimeEnd(self):
		return str(self.InsertTimeEnd, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', OrderSysID=\'{4}\', InsertTimeStart=\'{5}\', InsertTimeEnd=\'{6}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), str(self.InsertTimeStart, 'GB2312'), str(self.InsertTimeEnd, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'InsertTimeStart':str(self.InsertTimeStart, 'GB2312'),'InsertTimeEnd':str(self.InsertTimeEnd, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.InsertTimeStart=self.InsertTimeStart
		obj.InsertTimeEnd=self.InsertTimeEnd
		return obj

class CThostFtdcQryTradeField(Structure):
	"""查询成交"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#开始时间
		("TradeTimeStart",c_char*9),
		#结束时间
		("TradeTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTradeID(self):
		return str(self.TradeID, 'GB2312')
	def getTradeTimeStart(self):
		return str(self.TradeTimeStart, 'GB2312')
	def getTradeTimeEnd(self):
		return str(self.TradeTimeEnd, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', TradeID=\'{4}\', TradeTimeStart=\'{5}\', TradeTimeEnd=\'{6}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TradeID, 'GB2312'), str(self.TradeTimeStart, 'GB2312'), str(self.TradeTimeEnd, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TradeID':str(self.TradeID, 'GB2312'),'TradeTimeStart':str(self.TradeTimeStart, 'GB2312'),'TradeTimeEnd':str(self.TradeTimeEnd, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTradeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.TradeID=self.TradeID
		obj.TradeTimeStart=self.TradeTimeStart
		obj.TradeTimeEnd=self.TradeTimeEnd
		return obj

class CThostFtdcQryInvestorPositionField(Structure):
	"""查询投资者持仓"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInvestorPositionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryTradingAccountField(Structure):
	"""查询资金账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', CurrencyID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTradingAccountField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcQryInvestorField(Structure):
	"""查询投资者"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInvestorField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcQryTradingCodeField(Structure):
	"""查询交易编码"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#客户代码
		("ClientID",c_char*11),
		#交易编码类型
		("ClientIDType",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getClientIDType(self):
		return ClientIDTypeType(ord(self.ClientIDType))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\', ClientID=\'{3}\', ClientIDType=ClientIDTypeType.{4}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ClientID, 'GB2312'), '' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ClientIDType':'' if ord(self.ClientIDType) == 0 else ClientIDTypeType(ord(self.ClientIDType)).name}

	def clone(self):
		obj=CThostFtdcQryTradingCodeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		obj.ClientID=self.ClientID
		obj.ClientIDType=self.ClientIDType
		return obj

class CThostFtdcQryInvestorGroupField(Structure):
	"""查询投资者组"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInvestorGroupField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcQryInstrumentMarginRateField(Structure):
	"""查询合约保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', HedgeFlag=HedgeFlagType.{3}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name}

	def clone(self):
		obj=CThostFtdcQryInstrumentMarginRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		return obj

class CThostFtdcQryInstrumentCommissionRateField(Structure):
	"""查询手续费率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInstrumentCommissionRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryInstrumentTradingRightField(Structure):
	"""查询合约交易权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInstrumentTradingRightField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryBrokerField(Structure):
	"""查询经纪公司"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBrokerField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcQryTraderField(Structure):
	"""查询交易员"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ParticipantID=\'{1}\', TraderID=\'{2}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTraderField()
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQrySuperUserFunctionField(Structure):
	"""查询管理用户功能权限"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		]

	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'UserID=\'{0}\''.format(str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySuperUserFunctionField()
		obj.UserID=self.UserID
		return obj

class CThostFtdcQryUserSessionField(Structure):
	"""查询用户会话"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'FrontID={0}, SessionID={1}, BrokerID=\'{2}\', UserID=\'{3}\''.format(self.FrontID, self.SessionID, str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID,'SessionID':self.SessionID,'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryUserSessionField()
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcQryPartBrokerField(Structure):
	"""查询经纪公司会员代码"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#会员代码
		("ParticipantID",c_char*11),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', BrokerID=\'{1}\', ParticipantID=\'{2}\''.format(str(self.ExchangeID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.ParticipantID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryPartBrokerField()
		obj.ExchangeID=self.ExchangeID
		obj.BrokerID=self.BrokerID
		obj.ParticipantID=self.ParticipantID
		return obj

class CThostFtdcQryFrontStatusField(Structure):
	"""查询前置状态"""
	_fields_ = [
		#前置编号
		("FrontID",c_int32),
		]

	def getFrontID(self):
		return self.FrontID

	def __str__(self):
		return 'FrontID={0}'.format(self.FrontID)

	@property
	def __dict__(self):
		return {'FrontID':self.FrontID}

	def clone(self):
		obj=CThostFtdcQryFrontStatusField()
		obj.FrontID=self.FrontID
		return obj

class CThostFtdcQryExchangeOrderField(Structure):
	"""查询交易所报单"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeInstID=\'{2}\', ExchangeID=\'{3}\', TraderID=\'{4}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeOrderField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQryOrderActionField(Structure):
	"""查询报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcQryExchangeOrderActionField(Structure):
	"""查询交易所报单操作"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeID=\'{2}\', TraderID=\'{3}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeOrderActionField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQrySuperUserField(Structure):
	"""查询管理用户"""
	_fields_ = [
		#用户代码
		("UserID",c_char*16),
		]

	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'UserID=\'{0}\''.format(str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySuperUserField()
		obj.UserID=self.UserID
		return obj

class CThostFtdcQryExchangeField(Structure):
	"""查询交易所"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\''.format(str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeField()
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcQryProductField(Structure):
	"""查询产品"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#产品类型
		("ProductClass",c_char),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getProductClass(self):
		return ProductClassType(ord(self.ProductClass))

	def __str__(self):
		return 'ProductID=\'{0}\', ProductClass=ProductClassType.{1}'.format(str(self.ProductID, 'GB2312'), '' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name)

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312'),'ProductClass':'' if ord(self.ProductClass) == 0 else ProductClassType(ord(self.ProductClass)).name}

	def clone(self):
		obj=CThostFtdcQryProductField()
		obj.ProductID=self.ProductID
		obj.ProductClass=self.ProductClass
		return obj

class CThostFtdcQryInstrumentField(Structure):
	"""查询合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#产品代码
		("ProductID",c_char*31),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getProductID(self):
		return str(self.ProductID, 'GB2312')

	def __str__(self):
		return 'InstrumentID=\'{0}\', ExchangeID=\'{1}\', ExchangeInstID=\'{2}\', ProductID=\'{3}\''.format(str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ProductID, 'GB2312'))

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ProductID':str(self.ProductID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInstrumentField()
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ProductID=self.ProductID
		return obj

class CThostFtdcQryDepthMarketDataField(Structure):
	"""查询行情"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'InstrumentID=\'{0}\''.format(str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryDepthMarketDataField()
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryBrokerUserField(Structure):
	"""查询经纪公司用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBrokerUserField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcQryBrokerUserFunctionField(Structure):
	"""查询经纪公司用户权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBrokerUserFunctionField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcQryTraderOfferField(Structure):
	"""查询交易员报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ParticipantID=\'{1}\', TraderID=\'{2}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTraderOfferField()
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQrySyncDepositField(Structure):
	"""查询出入金流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#出入金流水号
		("DepositSeqNo",c_char*15),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getDepositSeqNo(self):
		return str(self.DepositSeqNo, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', DepositSeqNo=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.DepositSeqNo, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'DepositSeqNo':str(self.DepositSeqNo, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySyncDepositField()
		obj.BrokerID=self.BrokerID
		obj.DepositSeqNo=self.DepositSeqNo
		return obj

class CThostFtdcQrySettlementInfoField(Structure):
	"""查询投资者结算结果"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易日
		("TradingDay",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', TradingDay=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.TradingDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySettlementInfoField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.TradingDay=self.TradingDay
		return obj

class CThostFtdcQryExchangeMarginRateField(Structure):
	"""查询交易所保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', HedgeFlag=HedgeFlagType.{2}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name}

	def clone(self):
		obj=CThostFtdcQryExchangeMarginRateField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		return obj

class CThostFtdcQryExchangeMarginRateAdjustField(Structure):
	"""查询交易所调整保证金率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', HedgeFlag=HedgeFlagType.{2}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name}

	def clone(self):
		obj=CThostFtdcQryExchangeMarginRateAdjustField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		return obj

class CThostFtdcQryExchangeRateField(Structure):
	"""查询汇率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#源币种
		("FromCurrencyID",c_char*4),
		#目标币种
		("ToCurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getFromCurrencyID(self):
		return str(self.FromCurrencyID, 'GB2312')
	def getToCurrencyID(self):
		return str(self.ToCurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', FromCurrencyID=\'{1}\', ToCurrencyID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.FromCurrencyID, 'GB2312'), str(self.ToCurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'FromCurrencyID':str(self.FromCurrencyID, 'GB2312'),'ToCurrencyID':str(self.ToCurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeRateField()
		obj.BrokerID=self.BrokerID
		obj.FromCurrencyID=self.FromCurrencyID
		obj.ToCurrencyID=self.ToCurrencyID
		return obj

class CThostFtdcQrySyncFundMortgageField(Structure):
	"""查询货币质押流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#货币质押流水号
		("MortgageSeqNo",c_char*15),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getMortgageSeqNo(self):
		return str(self.MortgageSeqNo, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', MortgageSeqNo=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.MortgageSeqNo, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'MortgageSeqNo':str(self.MortgageSeqNo, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySyncFundMortgageField()
		obj.BrokerID=self.BrokerID
		obj.MortgageSeqNo=self.MortgageSeqNo
		return obj

class CThostFtdcQryHisOrderField(Structure):
	"""查询报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getInsertTimeStart(self):
		return str(self.InsertTimeStart, 'GB2312')
	def getInsertTimeEnd(self):
		return str(self.InsertTimeEnd, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', OrderSysID=\'{4}\', InsertTimeStart=\'{5}\', InsertTimeEnd=\'{6}\', TradingDay=\'{7}\', SettlementID={8}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), str(self.InsertTimeStart, 'GB2312'), str(self.InsertTimeEnd, 'GB2312'), str(self.TradingDay, 'GB2312'), self.SettlementID)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'InsertTimeStart':str(self.InsertTimeStart, 'GB2312'),'InsertTimeEnd':str(self.InsertTimeEnd, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID}

	def clone(self):
		obj=CThostFtdcQryHisOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.InsertTimeStart=self.InsertTimeStart
		obj.InsertTimeEnd=self.InsertTimeEnd
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		return obj

class CThostFtdcOptionInstrMiniMarginField(Structure):
	"""当前期权合约最小保证金"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#单位（手）期权合约最小保证金
		("MinMargin",c_double),
		#取值方式
		("ValueMethod",c_char),
		#是否跟随交易所收取
		("IsRelative",c_int32),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getMinMargin(self):
		return self.MinMargin
	def getValueMethod(self):
		return ValueMethodType(ord(self.ValueMethod))
	def getIsRelative(self):
		return self.IsRelative

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', MinMargin={4}, ValueMethod=ValueMethodType.{5}, IsRelative={6}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.MinMargin, '' if ord(self.ValueMethod) == 0 else ValueMethodType(ord(self.ValueMethod)).name, self.IsRelative)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'MinMargin':self.MinMargin,'ValueMethod':'' if ord(self.ValueMethod) == 0 else ValueMethodType(ord(self.ValueMethod)).name,'IsRelative':self.IsRelative}

	def clone(self):
		obj=CThostFtdcOptionInstrMiniMarginField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.MinMargin=self.MinMargin
		obj.ValueMethod=self.ValueMethod
		obj.IsRelative=self.IsRelative
		return obj

class CThostFtdcOptionInstrMarginAdjustField(Structure):
	"""当前期权合约保证金调整系数"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机空头保证金调整系数
		("SShortMarginRatioByMoney",c_double),
		#投机空头保证金调整系数
		("SShortMarginRatioByVolume",c_double),
		#保值空头保证金调整系数
		("HShortMarginRatioByMoney",c_double),
		#保值空头保证金调整系数
		("HShortMarginRatioByVolume",c_double),
		#套利空头保证金调整系数
		("AShortMarginRatioByMoney",c_double),
		#套利空头保证金调整系数
		("AShortMarginRatioByVolume",c_double),
		#是否跟随交易所收取
		("IsRelative",c_int32),
		#做市商空头保证金调整系数
		("MShortMarginRatioByMoney",c_double),
		#做市商空头保证金调整系数
		("MShortMarginRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getSShortMarginRatioByMoney(self):
		return self.SShortMarginRatioByMoney
	def getSShortMarginRatioByVolume(self):
		return self.SShortMarginRatioByVolume
	def getHShortMarginRatioByMoney(self):
		return self.HShortMarginRatioByMoney
	def getHShortMarginRatioByVolume(self):
		return self.HShortMarginRatioByVolume
	def getAShortMarginRatioByMoney(self):
		return self.AShortMarginRatioByMoney
	def getAShortMarginRatioByVolume(self):
		return self.AShortMarginRatioByVolume
	def getIsRelative(self):
		return self.IsRelative
	def getMShortMarginRatioByMoney(self):
		return self.MShortMarginRatioByMoney
	def getMShortMarginRatioByVolume(self):
		return self.MShortMarginRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', SShortMarginRatioByMoney={4}, SShortMarginRatioByVolume={5}, HShortMarginRatioByMoney={6}, HShortMarginRatioByVolume={7}, AShortMarginRatioByMoney={8}, AShortMarginRatioByVolume={9}, IsRelative={10}, MShortMarginRatioByMoney={11}, MShortMarginRatioByVolume={12}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.SShortMarginRatioByMoney, self.SShortMarginRatioByVolume, self.HShortMarginRatioByMoney, self.HShortMarginRatioByVolume, self.AShortMarginRatioByMoney, self.AShortMarginRatioByVolume, self.IsRelative, self.MShortMarginRatioByMoney, self.MShortMarginRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'SShortMarginRatioByMoney':self.SShortMarginRatioByMoney,'SShortMarginRatioByVolume':self.SShortMarginRatioByVolume,'HShortMarginRatioByMoney':self.HShortMarginRatioByMoney,'HShortMarginRatioByVolume':self.HShortMarginRatioByVolume,'AShortMarginRatioByMoney':self.AShortMarginRatioByMoney,'AShortMarginRatioByVolume':self.AShortMarginRatioByVolume,'IsRelative':self.IsRelative,'MShortMarginRatioByMoney':self.MShortMarginRatioByMoney,'MShortMarginRatioByVolume':self.MShortMarginRatioByVolume}

	def clone(self):
		obj=CThostFtdcOptionInstrMarginAdjustField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.SShortMarginRatioByMoney=self.SShortMarginRatioByMoney
		obj.SShortMarginRatioByVolume=self.SShortMarginRatioByVolume
		obj.HShortMarginRatioByMoney=self.HShortMarginRatioByMoney
		obj.HShortMarginRatioByVolume=self.HShortMarginRatioByVolume
		obj.AShortMarginRatioByMoney=self.AShortMarginRatioByMoney
		obj.AShortMarginRatioByVolume=self.AShortMarginRatioByVolume
		obj.IsRelative=self.IsRelative
		obj.MShortMarginRatioByMoney=self.MShortMarginRatioByMoney
		obj.MShortMarginRatioByVolume=self.MShortMarginRatioByVolume
		return obj

class CThostFtdcOptionInstrCommRateField(Structure):
	"""当前期权合约手续费的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		#执行手续费率
		("StrikeRatioByMoney",c_double),
		#执行手续费
		("StrikeRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume
	def getStrikeRatioByMoney(self):
		return self.StrikeRatioByMoney
	def getStrikeRatioByVolume(self):
		return self.StrikeRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', OpenRatioByMoney={4}, OpenRatioByVolume={5}, CloseRatioByMoney={6}, CloseRatioByVolume={7}, CloseTodayRatioByMoney={8}, CloseTodayRatioByVolume={9}, StrikeRatioByMoney={10}, StrikeRatioByVolume={11}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OpenRatioByMoney, self.OpenRatioByVolume, self.CloseRatioByMoney, self.CloseRatioByVolume, self.CloseTodayRatioByMoney, self.CloseTodayRatioByVolume, self.StrikeRatioByMoney, self.StrikeRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OpenRatioByMoney':self.OpenRatioByMoney,'OpenRatioByVolume':self.OpenRatioByVolume,'CloseRatioByMoney':self.CloseRatioByMoney,'CloseRatioByVolume':self.CloseRatioByVolume,'CloseTodayRatioByMoney':self.CloseTodayRatioByMoney,'CloseTodayRatioByVolume':self.CloseTodayRatioByVolume,'StrikeRatioByMoney':self.StrikeRatioByMoney,'StrikeRatioByVolume':self.StrikeRatioByVolume}

	def clone(self):
		obj=CThostFtdcOptionInstrCommRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OpenRatioByMoney=self.OpenRatioByMoney
		obj.OpenRatioByVolume=self.OpenRatioByVolume
		obj.CloseRatioByMoney=self.CloseRatioByMoney
		obj.CloseRatioByVolume=self.CloseRatioByVolume
		obj.CloseTodayRatioByMoney=self.CloseTodayRatioByMoney
		obj.CloseTodayRatioByVolume=self.CloseTodayRatioByVolume
		obj.StrikeRatioByMoney=self.StrikeRatioByMoney
		obj.StrikeRatioByVolume=self.StrikeRatioByVolume
		return obj

class CThostFtdcOptionInstrTradeCostField(Structure):
	"""期权交易成本"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#期权合约保证金不变部分
		("FixedMargin",c_double),
		#期权合约最小保证金
		("MiniMargin",c_double),
		#期权合约权利金
		("Royalty",c_double),
		#交易所期权合约保证金不变部分
		("ExchFixedMargin",c_double),
		#交易所期权合约最小保证金
		("ExchMiniMargin",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getFixedMargin(self):
		return self.FixedMargin
	def getMiniMargin(self):
		return self.MiniMargin
	def getRoyalty(self):
		return self.Royalty
	def getExchFixedMargin(self):
		return self.ExchFixedMargin
	def getExchMiniMargin(self):
		return self.ExchMiniMargin

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', HedgeFlag=HedgeFlagType.{3}, FixedMargin={4}, MiniMargin={5}, Royalty={6}, ExchFixedMargin={7}, ExchMiniMargin={8}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.FixedMargin, self.MiniMargin, self.Royalty, self.ExchFixedMargin, self.ExchMiniMargin)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'FixedMargin':self.FixedMargin,'MiniMargin':self.MiniMargin,'Royalty':self.Royalty,'ExchFixedMargin':self.ExchFixedMargin,'ExchMiniMargin':self.ExchMiniMargin}

	def clone(self):
		obj=CThostFtdcOptionInstrTradeCostField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		obj.FixedMargin=self.FixedMargin
		obj.MiniMargin=self.MiniMargin
		obj.Royalty=self.Royalty
		obj.ExchFixedMargin=self.ExchFixedMargin
		obj.ExchMiniMargin=self.ExchMiniMargin
		return obj

class CThostFtdcQryOptionInstrTradeCostField(Structure):
	"""期权交易成本查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#期权合约报价
		("InputPrice",c_double),
		#标的价格,填0则用昨结算价
		("UnderlyingPrice",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getInputPrice(self):
		return self.InputPrice
	def getUnderlyingPrice(self):
		return self.UnderlyingPrice

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', HedgeFlag=HedgeFlagType.{3}, InputPrice={4}, UnderlyingPrice={5}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.InputPrice, self.UnderlyingPrice)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'InputPrice':self.InputPrice,'UnderlyingPrice':self.UnderlyingPrice}

	def clone(self):
		obj=CThostFtdcQryOptionInstrTradeCostField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		obj.InputPrice=self.InputPrice
		obj.UnderlyingPrice=self.UnderlyingPrice
		return obj

class CThostFtdcQryOptionInstrCommRateField(Structure):
	"""期权手续费率查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryOptionInstrCommRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcIndexPriceField(Structure):
	"""股指现货指数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#指数现货收盘价
		("ClosePrice",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getClosePrice(self):
		return self.ClosePrice

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', ClosePrice={2}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), self.ClosePrice)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ClosePrice':self.ClosePrice}

	def clone(self):
		obj=CThostFtdcIndexPriceField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.ClosePrice=self.ClosePrice
		return obj

class CThostFtdcInputExecOrderField(Structure):
	"""输入的执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExecOrderRef=\'{3}\', UserID=\'{4}\', Volume={5}, RequestID={6}, BusinessUnit=\'{7}\', OffsetFlag=OffsetFlagType.{8}, HedgeFlag=HedgeFlagType.{9}, ActionType=ActionTypeType.{10}, PosiDirection=PosiDirectionType.{11}, ReservePositionFlag=ExecOrderPositionFlagType.{12}, CloseFlag=ExecOrderCloseFlagType.{13}, ExchangeID=\'{14}\', InvestUnitID=\'{15}\', AccountID=\'{16}\', CurrencyID=\'{17}\', ClientID=\'{18}\', IPAddress=\'{19}\', MacAddress=\'{20}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExecOrderRef, 'GB2312'), str(self.UserID, 'GB2312'), self.Volume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name, '' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name, str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Volume':self.Volume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'ReservePositionFlag':'' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name,'CloseFlag':'' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name,'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputExecOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExecOrderRef=self.ExecOrderRef
		obj.UserID=self.UserID
		obj.Volume=self.Volume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionType=self.ActionType
		obj.PosiDirection=self.PosiDirection
		obj.ReservePositionFlag=self.ReservePositionFlag
		obj.CloseFlag=self.CloseFlag
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcInputExecOrderActionField(Structure):
	"""输入执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExecOrderActionRef={2}, ExecOrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', ExecOrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, UserID=\'{10}\', InstrumentID=\'{11}\', InvestUnitID=\'{12}\', IPAddress=\'{13}\', MacAddress=\'{14}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.ExecOrderActionRef, str(self.ExecOrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.ExecOrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.UserID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExecOrderActionRef':self.ExecOrderActionRef,'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'UserID':str(self.UserID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputExecOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExecOrderActionRef=self.ExecOrderActionRef
		obj.ExecOrderRef=self.ExecOrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.UserID=self.UserID
		obj.InstrumentID=self.InstrumentID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExecOrderField(Structure):
	"""执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#执行宣告提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#执行结果
		("ExecResult",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerExecOrderSeq",c_int32),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExecOrderLocalID(self):
		return str(self.ExecOrderLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getExecResult(self):
		return ExecResultType(ord(self.ExecResult))
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getActiveUserID(self):
		return str(self.ActiveUserID, 'GB2312')
	def getBrokerExecOrderSeq(self):
		return self.BrokerExecOrderSeq
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExecOrderRef=\'{3}\', UserID=\'{4}\', Volume={5}, RequestID={6}, BusinessUnit=\'{7}\', OffsetFlag=OffsetFlagType.{8}, HedgeFlag=HedgeFlagType.{9}, ActionType=ActionTypeType.{10}, PosiDirection=PosiDirectionType.{11}, ReservePositionFlag=ExecOrderPositionFlagType.{12}, CloseFlag=ExecOrderCloseFlagType.{13}, ExecOrderLocalID=\'{14}\', ExchangeID=\'{15}\', ParticipantID=\'{16}\', ClientID=\'{17}\', ExchangeInstID=\'{18}\', TraderID=\'{19}\', InstallID={20}, OrderSubmitStatus=OrderSubmitStatusType.{21}, NotifySequence={22}, TradingDay=\'{23}\', SettlementID={24}, ExecOrderSysID=\'{25}\', InsertDate=\'{26}\', InsertTime=\'{27}\', CancelTime=\'{28}\', ExecResult=ExecResultType.{29}, ClearingPartID=\'{30}\', SequenceNo={31}, FrontID={32}, SessionID={33}, UserProductInfo=\'{34}\', StatusMsg=\'{35}\', ActiveUserID=\'{36}\', BrokerExecOrderSeq={37}, BranchID=\'{38}\', InvestUnitID=\'{39}\', AccountID=\'{40}\', CurrencyID=\'{41}\', IPAddress=\'{42}\', MacAddress=\'{43}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExecOrderRef, 'GB2312'), str(self.UserID, 'GB2312'), self.Volume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name, '' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name, str(self.ExecOrderLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.ExecOrderSysID, 'GB2312'), str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.CancelTime, 'GB2312'), '' if ord(self.ExecResult) == 0 else ExecResultType(ord(self.ExecResult)).name, str(self.ClearingPartID, 'GB2312'), self.SequenceNo, self.FrontID, self.SessionID, str(self.UserProductInfo, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.ActiveUserID, 'GB2312'), self.BrokerExecOrderSeq, str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Volume':self.Volume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'ReservePositionFlag':'' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name,'CloseFlag':'' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name,'ExecOrderLocalID':str(self.ExecOrderLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'ExecResult':'' if ord(self.ExecResult) == 0 else ExecResultType(ord(self.ExecResult)).name,'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'FrontID':self.FrontID,'SessionID':self.SessionID,'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'ActiveUserID':str(self.ActiveUserID, 'GB2312'),'BrokerExecOrderSeq':self.BrokerExecOrderSeq,'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExecOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExecOrderRef=self.ExecOrderRef
		obj.UserID=self.UserID
		obj.Volume=self.Volume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionType=self.ActionType
		obj.PosiDirection=self.PosiDirection
		obj.ReservePositionFlag=self.ReservePositionFlag
		obj.CloseFlag=self.CloseFlag
		obj.ExecOrderLocalID=self.ExecOrderLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.CancelTime=self.CancelTime
		obj.ExecResult=self.ExecResult
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.UserProductInfo=self.UserProductInfo
		obj.StatusMsg=self.StatusMsg
		obj.ActiveUserID=self.ActiveUserID
		obj.BrokerExecOrderSeq=self.BrokerExecOrderSeq
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExecOrderActionField(Structure):
	"""执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#执行类型
		("ActionType",c_char),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getExecOrderLocalID(self):
		return str(self.ExecOrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExecOrderActionRef={2}, ExecOrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', ExecOrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, ActionDate=\'{10}\', ActionTime=\'{11}\', TraderID=\'{12}\', InstallID={13}, ExecOrderLocalID=\'{14}\', ActionLocalID=\'{15}\', ParticipantID=\'{16}\', ClientID=\'{17}\', BusinessUnit=\'{18}\', OrderActionStatus=OrderActionStatusType.{19}, UserID=\'{20}\', ActionType=ActionTypeType.{21}, StatusMsg=\'{22}\', InstrumentID=\'{23}\', BranchID=\'{24}\', InvestUnitID=\'{25}\', IPAddress=\'{26}\', MacAddress=\'{27}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.ExecOrderActionRef, str(self.ExecOrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.ExecOrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.ExecOrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, str(self.StatusMsg, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExecOrderActionRef':self.ExecOrderActionRef,'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ExecOrderLocalID':str(self.ExecOrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'StatusMsg':str(self.StatusMsg, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExecOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExecOrderActionRef=self.ExecOrderActionRef
		obj.ExecOrderRef=self.ExecOrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ExecOrderLocalID=self.ExecOrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.ActionType=self.ActionType
		obj.StatusMsg=self.StatusMsg
		obj.InstrumentID=self.InstrumentID
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExecOrderField(Structure):
	"""执行宣告查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getInsertTimeStart(self):
		return str(self.InsertTimeStart, 'GB2312')
	def getInsertTimeEnd(self):
		return str(self.InsertTimeEnd, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', ExecOrderSysID=\'{4}\', InsertTimeStart=\'{5}\', InsertTimeEnd=\'{6}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ExecOrderSysID, 'GB2312'), str(self.InsertTimeStart, 'GB2312'), str(self.InsertTimeEnd, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'InsertTimeStart':str(self.InsertTimeStart, 'GB2312'),'InsertTimeEnd':str(self.InsertTimeEnd, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExecOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.InsertTimeStart=self.InsertTimeStart
		obj.InsertTimeEnd=self.InsertTimeEnd
		return obj

class CThostFtdcExchangeExecOrderField(Structure):
	"""交易所执行宣告信息"""
	_fields_ = [
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#执行宣告提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#执行宣告编号
		("ExecOrderSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#执行结果
		("ExecResult",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#营业部编号
		("BranchID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExecOrderLocalID(self):
		return str(self.ExecOrderLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getExecResult(self):
		return ExecResultType(ord(self.ExecResult))
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'Volume={0}, RequestID={1}, BusinessUnit=\'{2}\', OffsetFlag=OffsetFlagType.{3}, HedgeFlag=HedgeFlagType.{4}, ActionType=ActionTypeType.{5}, PosiDirection=PosiDirectionType.{6}, ReservePositionFlag=ExecOrderPositionFlagType.{7}, CloseFlag=ExecOrderCloseFlagType.{8}, ExecOrderLocalID=\'{9}\', ExchangeID=\'{10}\', ParticipantID=\'{11}\', ClientID=\'{12}\', ExchangeInstID=\'{13}\', TraderID=\'{14}\', InstallID={15}, OrderSubmitStatus=OrderSubmitStatusType.{16}, NotifySequence={17}, TradingDay=\'{18}\', SettlementID={19}, ExecOrderSysID=\'{20}\', InsertDate=\'{21}\', InsertTime=\'{22}\', CancelTime=\'{23}\', ExecResult=ExecResultType.{24}, ClearingPartID=\'{25}\', SequenceNo={26}, BranchID=\'{27}\', IPAddress=\'{28}\', MacAddress=\'{29}\''.format(self.Volume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name, '' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name, str(self.ExecOrderLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.ExecOrderSysID, 'GB2312'), str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.CancelTime, 'GB2312'), '' if ord(self.ExecResult) == 0 else ExecResultType(ord(self.ExecResult)).name, str(self.ClearingPartID, 'GB2312'), self.SequenceNo, str(self.BranchID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'Volume':self.Volume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'ReservePositionFlag':'' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name,'CloseFlag':'' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name,'ExecOrderLocalID':str(self.ExecOrderLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'ExecResult':'' if ord(self.ExecResult) == 0 else ExecResultType(ord(self.ExecResult)).name,'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'BranchID':str(self.BranchID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeExecOrderField()
		obj.Volume=self.Volume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionType=self.ActionType
		obj.PosiDirection=self.PosiDirection
		obj.ReservePositionFlag=self.ReservePositionFlag
		obj.CloseFlag=self.CloseFlag
		obj.ExecOrderLocalID=self.ExecOrderLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.CancelTime=self.CancelTime
		obj.ExecResult=self.ExecResult
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.BranchID=self.BranchID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeExecOrderField(Structure):
	"""交易所执行宣告查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeInstID=\'{2}\', ExchangeID=\'{3}\', TraderID=\'{4}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeExecOrderField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQryExecOrderActionField(Structure):
	"""执行宣告操作查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExecOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcExchangeExecOrderActionField(Structure):
	"""交易所执行宣告操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地执行宣告编号
		("ExecOrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#执行类型
		("ActionType",c_char),
		#营业部编号
		("BranchID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getExecOrderLocalID(self):
		return str(self.ExecOrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ExecOrderSysID=\'{1}\', ActionFlag=ActionFlagType.{2}, ActionDate=\'{3}\', ActionTime=\'{4}\', TraderID=\'{5}\', InstallID={6}, ExecOrderLocalID=\'{7}\', ActionLocalID=\'{8}\', ParticipantID=\'{9}\', ClientID=\'{10}\', BusinessUnit=\'{11}\', OrderActionStatus=OrderActionStatusType.{12}, UserID=\'{13}\', ActionType=ActionTypeType.{14}, BranchID=\'{15}\', IPAddress=\'{16}\', MacAddress=\'{17}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ExecOrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.ExecOrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, str(self.BranchID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ExecOrderLocalID':str(self.ExecOrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'BranchID':str(self.BranchID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeExecOrderActionField()
		obj.ExchangeID=self.ExchangeID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ExecOrderLocalID=self.ExecOrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.ActionType=self.ActionType
		obj.BranchID=self.BranchID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeExecOrderActionField(Structure):
	"""交易所执行宣告操作查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeID=\'{2}\', TraderID=\'{3}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeExecOrderActionField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcErrExecOrderField(Structure):
	"""错误执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#数量
		("Volume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#执行类型
		("ActionType",c_char),
		#保留头寸申请的持仓方向
		("PosiDirection",c_char),
		#期权行权后是否保留期货头寸的标记
		("ReservePositionFlag",c_char),
		#期权行权后生成的头寸是否自动平仓
		("CloseFlag",c_char),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVolume(self):
		return self.Volume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionType(self):
		return ActionTypeType(ord(self.ActionType))
	def getPosiDirection(self):
		return PosiDirectionType(ord(self.PosiDirection))
	def getReservePositionFlag(self):
		return ExecOrderPositionFlagType(ord(self.ReservePositionFlag))
	def getCloseFlag(self):
		return ExecOrderCloseFlagType(ord(self.CloseFlag))
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExecOrderRef=\'{3}\', UserID=\'{4}\', Volume={5}, RequestID={6}, BusinessUnit=\'{7}\', OffsetFlag=OffsetFlagType.{8}, HedgeFlag=HedgeFlagType.{9}, ActionType=ActionTypeType.{10}, PosiDirection=PosiDirectionType.{11}, ReservePositionFlag=ExecOrderPositionFlagType.{12}, CloseFlag=ExecOrderCloseFlagType.{13}, ExchangeID=\'{14}\', InvestUnitID=\'{15}\', AccountID=\'{16}\', CurrencyID=\'{17}\', ClientID=\'{18}\', IPAddress=\'{19}\', MacAddress=\'{20}\', ErrorID={21}, ErrorMsg=\'{22}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExecOrderRef, 'GB2312'), str(self.UserID, 'GB2312'), self.Volume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name, '' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name, '' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name, '' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name, str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Volume':self.Volume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionType':'' if ord(self.ActionType) == 0 else ActionTypeType(ord(self.ActionType)).name,'PosiDirection':'' if ord(self.PosiDirection) == 0 else PosiDirectionType(ord(self.PosiDirection)).name,'ReservePositionFlag':'' if ord(self.ReservePositionFlag) == 0 else ExecOrderPositionFlagType(ord(self.ReservePositionFlag)).name,'CloseFlag':'' if ord(self.CloseFlag) == 0 else ExecOrderCloseFlagType(ord(self.CloseFlag)).name,'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcErrExecOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExecOrderRef=self.ExecOrderRef
		obj.UserID=self.UserID
		obj.Volume=self.Volume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionType=self.ActionType
		obj.PosiDirection=self.PosiDirection
		obj.ReservePositionFlag=self.ReservePositionFlag
		obj.CloseFlag=self.CloseFlag
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcQryErrExecOrderField(Structure):
	"""查询错误执行宣告"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryErrExecOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcErrExecOrderActionField(Structure):
	"""错误执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行宣告操作引用
		("ExecOrderActionRef",c_int32),
		#执行宣告引用
		("ExecOrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#执行宣告操作编号
		("ExecOrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExecOrderActionRef(self):
		return self.ExecOrderActionRef
	def getExecOrderRef(self):
		return str(self.ExecOrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExecOrderSysID(self):
		return str(self.ExecOrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExecOrderActionRef={2}, ExecOrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', ExecOrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, UserID=\'{10}\', InstrumentID=\'{11}\', InvestUnitID=\'{12}\', IPAddress=\'{13}\', MacAddress=\'{14}\', ErrorID={15}, ErrorMsg=\'{16}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.ExecOrderActionRef, str(self.ExecOrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.ExecOrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.UserID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExecOrderActionRef':self.ExecOrderActionRef,'ExecOrderRef':str(self.ExecOrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExecOrderSysID':str(self.ExecOrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'UserID':str(self.UserID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcErrExecOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExecOrderActionRef=self.ExecOrderActionRef
		obj.ExecOrderRef=self.ExecOrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.ExecOrderSysID=self.ExecOrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.UserID=self.UserID
		obj.InstrumentID=self.InstrumentID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcQryErrExecOrderActionField(Structure):
	"""查询错误执行宣告操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryErrExecOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcOptionInstrTradingRightField(Structure):
	"""投资者期权合约交易权限"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#买卖方向
		("Direction",c_char),
		#交易权限
		("TradingRight",c_char),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getTradingRight(self):
		return TradingRightType(ord(self.TradingRight))

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', Direction=DirectionType.{4}, TradingRight=TradingRightType.{5}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, '' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'TradingRight':'' if ord(self.TradingRight) == 0 else TradingRightType(ord(self.TradingRight)).name}

	def clone(self):
		obj=CThostFtdcOptionInstrTradingRightField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Direction=self.Direction
		obj.TradingRight=self.TradingRight
		return obj

class CThostFtdcQryOptionInstrTradingRightField(Structure):
	"""查询期权合约交易权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', Direction=DirectionType.{3}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name}

	def clone(self):
		obj=CThostFtdcQryOptionInstrTradingRightField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.Direction=self.Direction
		return obj

class CThostFtdcInputForQuoteField(Structure):
	"""输入的询价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#询价引用
		("ForQuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getForQuoteRef(self):
		return str(self.ForQuoteRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ForQuoteRef=\'{3}\', UserID=\'{4}\', ExchangeID=\'{5}\', InvestUnitID=\'{6}\', IPAddress=\'{7}\', MacAddress=\'{8}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ForQuoteRef, 'GB2312'), str(self.UserID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ForQuoteRef':str(self.ForQuoteRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputForQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ForQuoteRef=self.ForQuoteRef
		obj.UserID=self.UserID
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcForQuoteField(Structure):
	"""询价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#询价引用
		("ForQuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#本地询价编号
		("ForQuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#询价状态
		("ForQuoteStatus",c_char),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司询价编号
		("BrokerForQutoSeq",c_int32),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getForQuoteRef(self):
		return str(self.ForQuoteRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getForQuoteLocalID(self):
		return str(self.ForQuoteLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getForQuoteStatus(self):
		return ForQuoteStatusType(ord(self.ForQuoteStatus))
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getActiveUserID(self):
		return str(self.ActiveUserID, 'GB2312')
	def getBrokerForQutoSeq(self):
		return self.BrokerForQutoSeq
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ForQuoteRef=\'{3}\', UserID=\'{4}\', ForQuoteLocalID=\'{5}\', ExchangeID=\'{6}\', ParticipantID=\'{7}\', ClientID=\'{8}\', ExchangeInstID=\'{9}\', TraderID=\'{10}\', InstallID={11}, InsertDate=\'{12}\', InsertTime=\'{13}\', ForQuoteStatus=ForQuoteStatusType.{14}, FrontID={15}, SessionID={16}, StatusMsg=\'{17}\', ActiveUserID=\'{18}\', BrokerForQutoSeq={19}, InvestUnitID=\'{20}\', IPAddress=\'{21}\', MacAddress=\'{22}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ForQuoteRef, 'GB2312'), str(self.UserID, 'GB2312'), str(self.ForQuoteLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), '' if ord(self.ForQuoteStatus) == 0 else ForQuoteStatusType(ord(self.ForQuoteStatus)).name, self.FrontID, self.SessionID, str(self.StatusMsg, 'GB2312'), str(self.ActiveUserID, 'GB2312'), self.BrokerForQutoSeq, str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ForQuoteRef':str(self.ForQuoteRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'ForQuoteLocalID':str(self.ForQuoteLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'ForQuoteStatus':'' if ord(self.ForQuoteStatus) == 0 else ForQuoteStatusType(ord(self.ForQuoteStatus)).name,'FrontID':self.FrontID,'SessionID':self.SessionID,'StatusMsg':str(self.StatusMsg, 'GB2312'),'ActiveUserID':str(self.ActiveUserID, 'GB2312'),'BrokerForQutoSeq':self.BrokerForQutoSeq,'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcForQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ForQuoteRef=self.ForQuoteRef
		obj.UserID=self.UserID
		obj.ForQuoteLocalID=self.ForQuoteLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.ForQuoteStatus=self.ForQuoteStatus
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.StatusMsg=self.StatusMsg
		obj.ActiveUserID=self.ActiveUserID
		obj.BrokerForQutoSeq=self.BrokerForQutoSeq
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryForQuoteField(Structure):
	"""询价查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInsertTimeStart(self):
		return str(self.InsertTimeStart, 'GB2312')
	def getInsertTimeEnd(self):
		return str(self.InsertTimeEnd, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', InsertTimeStart=\'{4}\', InsertTimeEnd=\'{5}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InsertTimeStart, 'GB2312'), str(self.InsertTimeEnd, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InsertTimeStart':str(self.InsertTimeStart, 'GB2312'),'InsertTimeEnd':str(self.InsertTimeEnd, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryForQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.InsertTimeStart=self.InsertTimeStart
		obj.InsertTimeEnd=self.InsertTimeEnd
		return obj

class CThostFtdcExchangeForQuoteField(Structure):
	"""交易所询价信息"""
	_fields_ = [
		#本地询价编号
		("ForQuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#询价状态
		("ForQuoteStatus",c_char),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getForQuoteLocalID(self):
		return str(self.ForQuoteLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getForQuoteStatus(self):
		return ForQuoteStatusType(ord(self.ForQuoteStatus))
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'ForQuoteLocalID=\'{0}\', ExchangeID=\'{1}\', ParticipantID=\'{2}\', ClientID=\'{3}\', ExchangeInstID=\'{4}\', TraderID=\'{5}\', InstallID={6}, InsertDate=\'{7}\', InsertTime=\'{8}\', ForQuoteStatus=ForQuoteStatusType.{9}, IPAddress=\'{10}\', MacAddress=\'{11}\''.format(str(self.ForQuoteLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), '' if ord(self.ForQuoteStatus) == 0 else ForQuoteStatusType(ord(self.ForQuoteStatus)).name, str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'ForQuoteLocalID':str(self.ForQuoteLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'ForQuoteStatus':'' if ord(self.ForQuoteStatus) == 0 else ForQuoteStatusType(ord(self.ForQuoteStatus)).name,'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeForQuoteField()
		obj.ForQuoteLocalID=self.ForQuoteLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.ForQuoteStatus=self.ForQuoteStatus
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeForQuoteField(Structure):
	"""交易所询价查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeInstID=\'{2}\', ExchangeID=\'{3}\', TraderID=\'{4}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeForQuoteField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcInputQuoteField(Structure):
	"""输入的报价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报价引用
		("QuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#衍生卖报单引用
		("AskOrderRef",c_char*13),
		#衍生买报单引用
		("BidOrderRef",c_char*13),
		#应价编号
		("ForQuoteSysID",c_char*21),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getQuoteRef(self):
		return str(self.QuoteRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getAskOrderRef(self):
		return str(self.AskOrderRef, 'GB2312')
	def getBidOrderRef(self):
		return str(self.BidOrderRef, 'GB2312')
	def getForQuoteSysID(self):
		return str(self.ForQuoteSysID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', QuoteRef=\'{3}\', UserID=\'{4}\', AskPrice={5}, BidPrice={6}, AskVolume={7}, BidVolume={8}, RequestID={9}, BusinessUnit=\'{10}\', AskOffsetFlag=OffsetFlagType.{11}, BidOffsetFlag=OffsetFlagType.{12}, AskHedgeFlag=HedgeFlagType.{13}, BidHedgeFlag=HedgeFlagType.{14}, AskOrderRef=\'{15}\', BidOrderRef=\'{16}\', ForQuoteSysID=\'{17}\', ExchangeID=\'{18}\', InvestUnitID=\'{19}\', ClientID=\'{20}\', IPAddress=\'{21}\', MacAddress=\'{22}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.QuoteRef, 'GB2312'), str(self.UserID, 'GB2312'), self.AskPrice, self.BidPrice, self.AskVolume, self.BidVolume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name, '' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name, '' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name, '' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name, str(self.AskOrderRef, 'GB2312'), str(self.BidOrderRef, 'GB2312'), str(self.ForQuoteSysID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'QuoteRef':str(self.QuoteRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'AskPrice':self.AskPrice,'BidPrice':self.BidPrice,'AskVolume':self.AskVolume,'BidVolume':self.BidVolume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'AskOffsetFlag':'' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name,'BidOffsetFlag':'' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name,'AskHedgeFlag':'' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name,'BidHedgeFlag':'' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name,'AskOrderRef':str(self.AskOrderRef, 'GB2312'),'BidOrderRef':str(self.BidOrderRef, 'GB2312'),'ForQuoteSysID':str(self.ForQuoteSysID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.QuoteRef=self.QuoteRef
		obj.UserID=self.UserID
		obj.AskPrice=self.AskPrice
		obj.BidPrice=self.BidPrice
		obj.AskVolume=self.AskVolume
		obj.BidVolume=self.BidVolume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.AskOffsetFlag=self.AskOffsetFlag
		obj.BidOffsetFlag=self.BidOffsetFlag
		obj.AskHedgeFlag=self.AskHedgeFlag
		obj.BidHedgeFlag=self.BidHedgeFlag
		obj.AskOrderRef=self.AskOrderRef
		obj.BidOrderRef=self.BidOrderRef
		obj.ForQuoteSysID=self.ForQuoteSysID
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcInputQuoteActionField(Structure):
	"""输入报价操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报价操作引用
		("QuoteActionRef",c_int32),
		#报价引用
		("QuoteRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getQuoteActionRef(self):
		return self.QuoteActionRef
	def getQuoteRef(self):
		return str(self.QuoteRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', QuoteActionRef={2}, QuoteRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', QuoteSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, UserID=\'{10}\', InstrumentID=\'{11}\', InvestUnitID=\'{12}\', ClientID=\'{13}\', IPAddress=\'{14}\', MacAddress=\'{15}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.QuoteActionRef, str(self.QuoteRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.QuoteSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.UserID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'QuoteActionRef':self.QuoteActionRef,'QuoteRef':str(self.QuoteRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'UserID':str(self.UserID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputQuoteActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.QuoteActionRef=self.QuoteActionRef
		obj.QuoteRef=self.QuoteRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.QuoteSysID=self.QuoteSysID
		obj.ActionFlag=self.ActionFlag
		obj.UserID=self.UserID
		obj.InstrumentID=self.InstrumentID
		obj.InvestUnitID=self.InvestUnitID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQuoteField(Structure):
	"""报价"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报价引用
		("QuoteRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报价提示序号
		("NotifySequence",c_int32),
		#报价提交状态
		("OrderSubmitStatus",c_char),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报价编号
		("QuoteSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#报价状态
		("QuoteStatus",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#卖方报单编号
		("AskOrderSysID",c_char*21),
		#买方报单编号
		("BidOrderSysID",c_char*21),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报价编号
		("BrokerQuoteSeq",c_int32),
		#衍生卖报单引用
		("AskOrderRef",c_char*13),
		#衍生买报单引用
		("BidOrderRef",c_char*13),
		#应价编号
		("ForQuoteSysID",c_char*21),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getQuoteRef(self):
		return str(self.QuoteRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getQuoteLocalID(self):
		return str(self.QuoteLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getNotifySequence(self):
		return self.NotifySequence
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getQuoteStatus(self):
		return OrderStatusType(ord(self.QuoteStatus))
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getAskOrderSysID(self):
		return str(self.AskOrderSysID, 'GB2312')
	def getBidOrderSysID(self):
		return str(self.BidOrderSysID, 'GB2312')
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getActiveUserID(self):
		return str(self.ActiveUserID, 'GB2312')
	def getBrokerQuoteSeq(self):
		return self.BrokerQuoteSeq
	def getAskOrderRef(self):
		return str(self.AskOrderRef, 'GB2312')
	def getBidOrderRef(self):
		return str(self.BidOrderRef, 'GB2312')
	def getForQuoteSysID(self):
		return str(self.ForQuoteSysID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', QuoteRef=\'{3}\', UserID=\'{4}\', AskPrice={5}, BidPrice={6}, AskVolume={7}, BidVolume={8}, RequestID={9}, BusinessUnit=\'{10}\', AskOffsetFlag=OffsetFlagType.{11}, BidOffsetFlag=OffsetFlagType.{12}, AskHedgeFlag=HedgeFlagType.{13}, BidHedgeFlag=HedgeFlagType.{14}, QuoteLocalID=\'{15}\', ExchangeID=\'{16}\', ParticipantID=\'{17}\', ClientID=\'{18}\', ExchangeInstID=\'{19}\', TraderID=\'{20}\', InstallID={21}, NotifySequence={22}, OrderSubmitStatus=OrderSubmitStatusType.{23}, TradingDay=\'{24}\', SettlementID={25}, QuoteSysID=\'{26}\', InsertDate=\'{27}\', InsertTime=\'{28}\', CancelTime=\'{29}\', QuoteStatus=OrderStatusType.{30}, ClearingPartID=\'{31}\', SequenceNo={32}, AskOrderSysID=\'{33}\', BidOrderSysID=\'{34}\', FrontID={35}, SessionID={36}, UserProductInfo=\'{37}\', StatusMsg=\'{38}\', ActiveUserID=\'{39}\', BrokerQuoteSeq={40}, AskOrderRef=\'{41}\', BidOrderRef=\'{42}\', ForQuoteSysID=\'{43}\', BranchID=\'{44}\', InvestUnitID=\'{45}\', AccountID=\'{46}\', CurrencyID=\'{47}\', IPAddress=\'{48}\', MacAddress=\'{49}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.QuoteRef, 'GB2312'), str(self.UserID, 'GB2312'), self.AskPrice, self.BidPrice, self.AskVolume, self.BidVolume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name, '' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name, '' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name, '' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name, str(self.QuoteLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, self.NotifySequence, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.QuoteSysID, 'GB2312'), str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.CancelTime, 'GB2312'), '' if ord(self.QuoteStatus) == 0 else OrderStatusType(ord(self.QuoteStatus)).name, str(self.ClearingPartID, 'GB2312'), self.SequenceNo, str(self.AskOrderSysID, 'GB2312'), str(self.BidOrderSysID, 'GB2312'), self.FrontID, self.SessionID, str(self.UserProductInfo, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.ActiveUserID, 'GB2312'), self.BrokerQuoteSeq, str(self.AskOrderRef, 'GB2312'), str(self.BidOrderRef, 'GB2312'), str(self.ForQuoteSysID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'QuoteRef':str(self.QuoteRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'AskPrice':self.AskPrice,'BidPrice':self.BidPrice,'AskVolume':self.AskVolume,'BidVolume':self.BidVolume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'AskOffsetFlag':'' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name,'BidOffsetFlag':'' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name,'AskHedgeFlag':'' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name,'BidHedgeFlag':'' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name,'QuoteLocalID':str(self.QuoteLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'NotifySequence':self.NotifySequence,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'QuoteStatus':'' if ord(self.QuoteStatus) == 0 else OrderStatusType(ord(self.QuoteStatus)).name,'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'AskOrderSysID':str(self.AskOrderSysID, 'GB2312'),'BidOrderSysID':str(self.BidOrderSysID, 'GB2312'),'FrontID':self.FrontID,'SessionID':self.SessionID,'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'ActiveUserID':str(self.ActiveUserID, 'GB2312'),'BrokerQuoteSeq':self.BrokerQuoteSeq,'AskOrderRef':str(self.AskOrderRef, 'GB2312'),'BidOrderRef':str(self.BidOrderRef, 'GB2312'),'ForQuoteSysID':str(self.ForQuoteSysID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.QuoteRef=self.QuoteRef
		obj.UserID=self.UserID
		obj.AskPrice=self.AskPrice
		obj.BidPrice=self.BidPrice
		obj.AskVolume=self.AskVolume
		obj.BidVolume=self.BidVolume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.AskOffsetFlag=self.AskOffsetFlag
		obj.BidOffsetFlag=self.BidOffsetFlag
		obj.AskHedgeFlag=self.AskHedgeFlag
		obj.BidHedgeFlag=self.BidHedgeFlag
		obj.QuoteLocalID=self.QuoteLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.NotifySequence=self.NotifySequence
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.QuoteSysID=self.QuoteSysID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.CancelTime=self.CancelTime
		obj.QuoteStatus=self.QuoteStatus
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.AskOrderSysID=self.AskOrderSysID
		obj.BidOrderSysID=self.BidOrderSysID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.UserProductInfo=self.UserProductInfo
		obj.StatusMsg=self.StatusMsg
		obj.ActiveUserID=self.ActiveUserID
		obj.BrokerQuoteSeq=self.BrokerQuoteSeq
		obj.AskOrderRef=self.AskOrderRef
		obj.BidOrderRef=self.BidOrderRef
		obj.ForQuoteSysID=self.ForQuoteSysID
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQuoteActionField(Structure):
	"""报价操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报价操作引用
		("QuoteActionRef",c_int32),
		#报价引用
		("QuoteRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getQuoteActionRef(self):
		return self.QuoteActionRef
	def getQuoteRef(self):
		return str(self.QuoteRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getQuoteLocalID(self):
		return str(self.QuoteLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', QuoteActionRef={2}, QuoteRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', QuoteSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, ActionDate=\'{10}\', ActionTime=\'{11}\', TraderID=\'{12}\', InstallID={13}, QuoteLocalID=\'{14}\', ActionLocalID=\'{15}\', ParticipantID=\'{16}\', ClientID=\'{17}\', BusinessUnit=\'{18}\', OrderActionStatus=OrderActionStatusType.{19}, UserID=\'{20}\', StatusMsg=\'{21}\', InstrumentID=\'{22}\', BranchID=\'{23}\', InvestUnitID=\'{24}\', IPAddress=\'{25}\', MacAddress=\'{26}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.QuoteActionRef, str(self.QuoteRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.QuoteSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.QuoteLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'QuoteActionRef':self.QuoteActionRef,'QuoteRef':str(self.QuoteRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'QuoteLocalID':str(self.QuoteLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQuoteActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.QuoteActionRef=self.QuoteActionRef
		obj.QuoteRef=self.QuoteRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.QuoteSysID=self.QuoteSysID
		obj.ActionFlag=self.ActionFlag
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.QuoteLocalID=self.QuoteLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.StatusMsg=self.StatusMsg
		obj.InstrumentID=self.InstrumentID
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryQuoteField(Structure):
	"""报价查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#报价编号
		("QuoteSysID",c_char*21),
		#开始时间
		("InsertTimeStart",c_char*9),
		#结束时间
		("InsertTimeEnd",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getInsertTimeStart(self):
		return str(self.InsertTimeStart, 'GB2312')
	def getInsertTimeEnd(self):
		return str(self.InsertTimeEnd, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\', QuoteSysID=\'{4}\', InsertTimeStart=\'{5}\', InsertTimeEnd=\'{6}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.QuoteSysID, 'GB2312'), str(self.InsertTimeStart, 'GB2312'), str(self.InsertTimeEnd, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'InsertTimeStart':str(self.InsertTimeStart, 'GB2312'),'InsertTimeEnd':str(self.InsertTimeEnd, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryQuoteField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.QuoteSysID=self.QuoteSysID
		obj.InsertTimeStart=self.InsertTimeStart
		obj.InsertTimeEnd=self.InsertTimeEnd
		return obj

class CThostFtdcExchangeQuoteField(Structure):
	"""交易所报价信息"""
	_fields_ = [
		#卖价格
		("AskPrice",c_double),
		#买价格
		("BidPrice",c_double),
		#卖数量
		("AskVolume",c_int32),
		#买数量
		("BidVolume",c_int32),
		#请求编号
		("RequestID",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#卖开平标志
		("AskOffsetFlag",c_char),
		#买开平标志
		("BidOffsetFlag",c_char),
		#卖投机套保标志
		("AskHedgeFlag",c_char),
		#买投机套保标志
		("BidHedgeFlag",c_char),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报价提示序号
		("NotifySequence",c_int32),
		#报价提交状态
		("OrderSubmitStatus",c_char),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报价编号
		("QuoteSysID",c_char*21),
		#报单日期
		("InsertDate",c_char*9),
		#插入时间
		("InsertTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#报价状态
		("QuoteStatus",c_char),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#卖方报单编号
		("AskOrderSysID",c_char*21),
		#买方报单编号
		("BidOrderSysID",c_char*21),
		#应价编号
		("ForQuoteSysID",c_char*21),
		#营业部编号
		("BranchID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getAskPrice(self):
		return self.AskPrice
	def getBidPrice(self):
		return self.BidPrice
	def getAskVolume(self):
		return self.AskVolume
	def getBidVolume(self):
		return self.BidVolume
	def getRequestID(self):
		return self.RequestID
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getAskOffsetFlag(self):
		return OffsetFlagType(ord(self.AskOffsetFlag))
	def getBidOffsetFlag(self):
		return OffsetFlagType(ord(self.BidOffsetFlag))
	def getAskHedgeFlag(self):
		return HedgeFlagType(ord(self.AskHedgeFlag))
	def getBidHedgeFlag(self):
		return HedgeFlagType(ord(self.BidHedgeFlag))
	def getQuoteLocalID(self):
		return str(self.QuoteLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getNotifySequence(self):
		return self.NotifySequence
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getQuoteStatus(self):
		return OrderStatusType(ord(self.QuoteStatus))
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getAskOrderSysID(self):
		return str(self.AskOrderSysID, 'GB2312')
	def getBidOrderSysID(self):
		return str(self.BidOrderSysID, 'GB2312')
	def getForQuoteSysID(self):
		return str(self.ForQuoteSysID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'AskPrice={0}, BidPrice={1}, AskVolume={2}, BidVolume={3}, RequestID={4}, BusinessUnit=\'{5}\', AskOffsetFlag=OffsetFlagType.{6}, BidOffsetFlag=OffsetFlagType.{7}, AskHedgeFlag=HedgeFlagType.{8}, BidHedgeFlag=HedgeFlagType.{9}, QuoteLocalID=\'{10}\', ExchangeID=\'{11}\', ParticipantID=\'{12}\', ClientID=\'{13}\', ExchangeInstID=\'{14}\', TraderID=\'{15}\', InstallID={16}, NotifySequence={17}, OrderSubmitStatus=OrderSubmitStatusType.{18}, TradingDay=\'{19}\', SettlementID={20}, QuoteSysID=\'{21}\', InsertDate=\'{22}\', InsertTime=\'{23}\', CancelTime=\'{24}\', QuoteStatus=OrderStatusType.{25}, ClearingPartID=\'{26}\', SequenceNo={27}, AskOrderSysID=\'{28}\', BidOrderSysID=\'{29}\', ForQuoteSysID=\'{30}\', BranchID=\'{31}\', IPAddress=\'{32}\', MacAddress=\'{33}\''.format(self.AskPrice, self.BidPrice, self.AskVolume, self.BidVolume, self.RequestID, str(self.BusinessUnit, 'GB2312'), '' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name, '' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name, '' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name, '' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name, str(self.QuoteLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, self.NotifySequence, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.QuoteSysID, 'GB2312'), str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.CancelTime, 'GB2312'), '' if ord(self.QuoteStatus) == 0 else OrderStatusType(ord(self.QuoteStatus)).name, str(self.ClearingPartID, 'GB2312'), self.SequenceNo, str(self.AskOrderSysID, 'GB2312'), str(self.BidOrderSysID, 'GB2312'), str(self.ForQuoteSysID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'AskPrice':self.AskPrice,'BidPrice':self.BidPrice,'AskVolume':self.AskVolume,'BidVolume':self.BidVolume,'RequestID':self.RequestID,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'AskOffsetFlag':'' if ord(self.AskOffsetFlag) == 0 else OffsetFlagType(ord(self.AskOffsetFlag)).name,'BidOffsetFlag':'' if ord(self.BidOffsetFlag) == 0 else OffsetFlagType(ord(self.BidOffsetFlag)).name,'AskHedgeFlag':'' if ord(self.AskHedgeFlag) == 0 else HedgeFlagType(ord(self.AskHedgeFlag)).name,'BidHedgeFlag':'' if ord(self.BidHedgeFlag) == 0 else HedgeFlagType(ord(self.BidHedgeFlag)).name,'QuoteLocalID':str(self.QuoteLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'NotifySequence':self.NotifySequence,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'QuoteStatus':'' if ord(self.QuoteStatus) == 0 else OrderStatusType(ord(self.QuoteStatus)).name,'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'AskOrderSysID':str(self.AskOrderSysID, 'GB2312'),'BidOrderSysID':str(self.BidOrderSysID, 'GB2312'),'ForQuoteSysID':str(self.ForQuoteSysID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeQuoteField()
		obj.AskPrice=self.AskPrice
		obj.BidPrice=self.BidPrice
		obj.AskVolume=self.AskVolume
		obj.BidVolume=self.BidVolume
		obj.RequestID=self.RequestID
		obj.BusinessUnit=self.BusinessUnit
		obj.AskOffsetFlag=self.AskOffsetFlag
		obj.BidOffsetFlag=self.BidOffsetFlag
		obj.AskHedgeFlag=self.AskHedgeFlag
		obj.BidHedgeFlag=self.BidHedgeFlag
		obj.QuoteLocalID=self.QuoteLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.NotifySequence=self.NotifySequence
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.QuoteSysID=self.QuoteSysID
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.CancelTime=self.CancelTime
		obj.QuoteStatus=self.QuoteStatus
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.AskOrderSysID=self.AskOrderSysID
		obj.BidOrderSysID=self.BidOrderSysID
		obj.ForQuoteSysID=self.ForQuoteSysID
		obj.BranchID=self.BranchID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeQuoteField(Structure):
	"""交易所报价查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeInstID=\'{2}\', ExchangeID=\'{3}\', TraderID=\'{4}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeQuoteField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQryQuoteActionField(Structure):
	"""报价操作查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryQuoteActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcExchangeQuoteActionField(Structure):
	"""交易所报价操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#报价操作编号
		("QuoteSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报价编号
		("QuoteLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getQuoteSysID(self):
		return str(self.QuoteSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getQuoteLocalID(self):
		return str(self.QuoteLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', QuoteSysID=\'{1}\', ActionFlag=ActionFlagType.{2}, ActionDate=\'{3}\', ActionTime=\'{4}\', TraderID=\'{5}\', InstallID={6}, QuoteLocalID=\'{7}\', ActionLocalID=\'{8}\', ParticipantID=\'{9}\', ClientID=\'{10}\', BusinessUnit=\'{11}\', OrderActionStatus=OrderActionStatusType.{12}, UserID=\'{13}\', IPAddress=\'{14}\', MacAddress=\'{15}\''.format(str(self.ExchangeID, 'GB2312'), str(self.QuoteSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.QuoteLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'QuoteSysID':str(self.QuoteSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'QuoteLocalID':str(self.QuoteLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeQuoteActionField()
		obj.ExchangeID=self.ExchangeID
		obj.QuoteSysID=self.QuoteSysID
		obj.ActionFlag=self.ActionFlag
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.QuoteLocalID=self.QuoteLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeQuoteActionField(Structure):
	"""交易所报价操作查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeID=\'{2}\', TraderID=\'{3}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeQuoteActionField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcOptionInstrDeltaField(Structure):
	"""期权合约delta值"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#Delta值
		("Delta",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getDelta(self):
		return self.Delta

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', Delta={4}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.Delta)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Delta':self.Delta}

	def clone(self):
		obj=CThostFtdcOptionInstrDeltaField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Delta=self.Delta
		return obj

class CThostFtdcForQuoteRspField(Structure):
	"""发给做市商的询价请求"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#询价编号
		("ForQuoteSysID",c_char*21),
		#询价时间
		("ForQuoteTime",c_char*9),
		#业务日期
		("ActionDay",c_char*9),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getForQuoteSysID(self):
		return str(self.ForQuoteSysID, 'GB2312')
	def getForQuoteTime(self):
		return str(self.ForQuoteTime, 'GB2312')
	def getActionDay(self):
		return str(self.ActionDay, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', InstrumentID=\'{1}\', ForQuoteSysID=\'{2}\', ForQuoteTime=\'{3}\', ActionDay=\'{4}\', ExchangeID=\'{5}\''.format(str(self.TradingDay, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ForQuoteSysID, 'GB2312'), str(self.ForQuoteTime, 'GB2312'), str(self.ActionDay, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ForQuoteSysID':str(self.ForQuoteSysID, 'GB2312'),'ForQuoteTime':str(self.ForQuoteTime, 'GB2312'),'ActionDay':str(self.ActionDay, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcForQuoteRspField()
		obj.TradingDay=self.TradingDay
		obj.InstrumentID=self.InstrumentID
		obj.ForQuoteSysID=self.ForQuoteSysID
		obj.ForQuoteTime=self.ForQuoteTime
		obj.ActionDay=self.ActionDay
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcStrikeOffsetField(Structure):
	"""当前期权合约执行偏移值的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#执行偏移值
		("Offset",c_double),
		#执行偏移类型
		("OffsetType",c_char),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOffset(self):
		return self.Offset
	def getOffsetType(self):
		return StrikeOffsetTypeType(ord(self.OffsetType))

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', Offset={4}, OffsetType=StrikeOffsetTypeType.{5}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.Offset, '' if ord(self.OffsetType) == 0 else StrikeOffsetTypeType(ord(self.OffsetType)).name)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Offset':self.Offset,'OffsetType':'' if ord(self.OffsetType) == 0 else StrikeOffsetTypeType(ord(self.OffsetType)).name}

	def clone(self):
		obj=CThostFtdcStrikeOffsetField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Offset=self.Offset
		obj.OffsetType=self.OffsetType
		return obj

class CThostFtdcQryStrikeOffsetField(Structure):
	"""期权执行偏移值查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryStrikeOffsetField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcInputBatchOrderActionField(Structure):
	"""输入批量报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#用户代码
		("UserID",c_char*16),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, RequestID={3}, FrontID={4}, SessionID={5}, ExchangeID=\'{6}\', UserID=\'{7}\', InvestUnitID=\'{8}\', IPAddress=\'{9}\', MacAddress=\'{10}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputBatchOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.UserID=self.UserID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcBatchOrderActionField(Structure):
	"""批量报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, RequestID={3}, FrontID={4}, SessionID={5}, ExchangeID=\'{6}\', ActionDate=\'{7}\', ActionTime=\'{8}\', TraderID=\'{9}\', InstallID={10}, ActionLocalID=\'{11}\', ParticipantID=\'{12}\', ClientID=\'{13}\', BusinessUnit=\'{14}\', OrderActionStatus=OrderActionStatusType.{15}, UserID=\'{16}\', StatusMsg=\'{17}\', InvestUnitID=\'{18}\', IPAddress=\'{19}\', MacAddress=\'{20}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcBatchOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.StatusMsg=self.StatusMsg
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcExchangeBatchOrderActionField(Structure):
	"""交易所批量报单操作"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ActionDate=\'{1}\', ActionTime=\'{2}\', TraderID=\'{3}\', InstallID={4}, ActionLocalID=\'{5}\', ParticipantID=\'{6}\', ClientID=\'{7}\', BusinessUnit=\'{8}\', OrderActionStatus=OrderActionStatusType.{9}, UserID=\'{10}\', IPAddress=\'{11}\', MacAddress=\'{12}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeBatchOrderActionField()
		obj.ExchangeID=self.ExchangeID
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryBatchOrderActionField(Structure):
	"""查询批量报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBatchOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcCombInstrumentGuardField(Structure):
	"""组合合约安全系数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#
		("GuarantRatio",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getGuarantRatio(self):
		return self.GuarantRatio

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', GuarantRatio={2}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), self.GuarantRatio)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'GuarantRatio':self.GuarantRatio}

	def clone(self):
		obj=CThostFtdcCombInstrumentGuardField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.GuarantRatio=self.GuarantRatio
		return obj

class CThostFtdcQryCombInstrumentGuardField(Structure):
	"""组合合约安全系数查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCombInstrumentGuardField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcInputCombActionField(Structure):
	"""输入的申请组合"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#组合引用
		("CombActionRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#买卖方向
		("Direction",c_char),
		#数量
		("Volume",c_int32),
		#组合指令方向
		("CombDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#交易所代码
		("ExchangeID",c_char*9),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getCombActionRef(self):
		return str(self.CombActionRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getVolume(self):
		return self.Volume
	def getCombDirection(self):
		return CombDirectionType(ord(self.CombDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', CombActionRef=\'{3}\', UserID=\'{4}\', Direction=DirectionType.{5}, Volume={6}, CombDirection=CombDirectionType.{7}, HedgeFlag=HedgeFlagType.{8}, ExchangeID=\'{9}\', IPAddress=\'{10}\', MacAddress=\'{11}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.CombActionRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, self.Volume, '' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, str(self.ExchangeID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'CombActionRef':str(self.CombActionRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'Volume':self.Volume,'CombDirection':'' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ExchangeID':str(self.ExchangeID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInputCombActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.CombActionRef=self.CombActionRef
		obj.UserID=self.UserID
		obj.Direction=self.Direction
		obj.Volume=self.Volume
		obj.CombDirection=self.CombDirection
		obj.HedgeFlag=self.HedgeFlag
		obj.ExchangeID=self.ExchangeID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcCombActionField(Structure):
	"""申请组合"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#组合引用
		("CombActionRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#买卖方向
		("Direction",c_char),
		#数量
		("Volume",c_int32),
		#组合指令方向
		("CombDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#本地申请组合编号
		("ActionLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#组合状态
		("ActionStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getCombActionRef(self):
		return str(self.CombActionRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getVolume(self):
		return self.Volume
	def getCombDirection(self):
		return CombDirectionType(ord(self.CombDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getActionStatus(self):
		return OrderActionStatusType(ord(self.ActionStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', CombActionRef=\'{3}\', UserID=\'{4}\', Direction=DirectionType.{5}, Volume={6}, CombDirection=CombDirectionType.{7}, HedgeFlag=HedgeFlagType.{8}, ActionLocalID=\'{9}\', ExchangeID=\'{10}\', ParticipantID=\'{11}\', ClientID=\'{12}\', ExchangeInstID=\'{13}\', TraderID=\'{14}\', InstallID={15}, ActionStatus=OrderActionStatusType.{16}, NotifySequence={17}, TradingDay=\'{18}\', SettlementID={19}, SequenceNo={20}, FrontID={21}, SessionID={22}, UserProductInfo=\'{23}\', StatusMsg=\'{24}\', IPAddress=\'{25}\', MacAddress=\'{26}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.CombActionRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, self.Volume, '' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, str(self.ActionLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.ActionStatus) == 0 else OrderActionStatusType(ord(self.ActionStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, self.SequenceNo, self.FrontID, self.SessionID, str(self.UserProductInfo, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'CombActionRef':str(self.CombActionRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'Volume':self.Volume,'CombDirection':'' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ActionStatus':'' if ord(self.ActionStatus) == 0 else OrderActionStatusType(ord(self.ActionStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'SequenceNo':self.SequenceNo,'FrontID':self.FrontID,'SessionID':self.SessionID,'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCombActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.CombActionRef=self.CombActionRef
		obj.UserID=self.UserID
		obj.Direction=self.Direction
		obj.Volume=self.Volume
		obj.CombDirection=self.CombDirection
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionLocalID=self.ActionLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ActionStatus=self.ActionStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.SequenceNo=self.SequenceNo
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.UserProductInfo=self.UserProductInfo
		obj.StatusMsg=self.StatusMsg
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryCombActionField(Structure):
	"""申请组合查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCombActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcExchangeCombActionField(Structure):
	"""交易所申请组合信息"""
	_fields_ = [
		#买卖方向
		("Direction",c_char),
		#数量
		("Volume",c_int32),
		#组合指令方向
		("CombDirection",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#本地申请组合编号
		("ActionLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#组合状态
		("ActionStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#序号
		("SequenceNo",c_int32),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getVolume(self):
		return self.Volume
	def getCombDirection(self):
		return CombDirectionType(ord(self.CombDirection))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getActionStatus(self):
		return OrderActionStatusType(ord(self.ActionStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getSequenceNo(self):
		return self.SequenceNo
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'Direction=DirectionType.{0}, Volume={1}, CombDirection=CombDirectionType.{2}, HedgeFlag=HedgeFlagType.{3}, ActionLocalID=\'{4}\', ExchangeID=\'{5}\', ParticipantID=\'{6}\', ClientID=\'{7}\', ExchangeInstID=\'{8}\', TraderID=\'{9}\', InstallID={10}, ActionStatus=OrderActionStatusType.{11}, NotifySequence={12}, TradingDay=\'{13}\', SettlementID={14}, SequenceNo={15}, IPAddress=\'{16}\', MacAddress=\'{17}\''.format('' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, self.Volume, '' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, str(self.ActionLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.ActionStatus) == 0 else OrderActionStatusType(ord(self.ActionStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, self.SequenceNo, str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'Volume':self.Volume,'CombDirection':'' if ord(self.CombDirection) == 0 else CombDirectionType(ord(self.CombDirection)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'ActionStatus':'' if ord(self.ActionStatus) == 0 else OrderActionStatusType(ord(self.ActionStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'SequenceNo':self.SequenceNo,'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcExchangeCombActionField()
		obj.Direction=self.Direction
		obj.Volume=self.Volume
		obj.CombDirection=self.CombDirection
		obj.HedgeFlag=self.HedgeFlag
		obj.ActionLocalID=self.ActionLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.ActionStatus=self.ActionStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.SequenceNo=self.SequenceNo
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryExchangeCombActionField(Structure):
	"""交易所申请组合查询"""
	_fields_ = [
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ParticipantID=\'{0}\', ClientID=\'{1}\', ExchangeInstID=\'{2}\', ExchangeID=\'{3}\', TraderID=\'{4}\''.format(str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeCombActionField()
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcProductExchRateField(Structure):
	"""产品报价汇率"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#报价币种类型
		("QuoteCurrencyID",c_char*4),
		#汇率
		("ExchangeRate",c_double),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getQuoteCurrencyID(self):
		return str(self.QuoteCurrencyID, 'GB2312')
	def getExchangeRate(self):
		return self.ExchangeRate

	def __str__(self):
		return 'ProductID=\'{0}\', QuoteCurrencyID=\'{1}\', ExchangeRate={2}'.format(str(self.ProductID, 'GB2312'), str(self.QuoteCurrencyID, 'GB2312'), self.ExchangeRate)

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312'),'QuoteCurrencyID':str(self.QuoteCurrencyID, 'GB2312'),'ExchangeRate':self.ExchangeRate}

	def clone(self):
		obj=CThostFtdcProductExchRateField()
		obj.ProductID=self.ProductID
		obj.QuoteCurrencyID=self.QuoteCurrencyID
		obj.ExchangeRate=self.ExchangeRate
		return obj

class CThostFtdcQryProductExchRateField(Structure):
	"""产品报价汇率查询"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')

	def __str__(self):
		return 'ProductID=\'{0}\''.format(str(self.ProductID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryProductExchRateField()
		obj.ProductID=self.ProductID
		return obj

class CThostFtdcQryForQuoteParamField(Structure):
	"""查询询价价差参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', ExchangeID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryForQuoteParamField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcForQuoteParamField(Structure):
	"""询价价差参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#最新价
		("LastPrice",c_double),
		#价差
		("PriceInterval",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getLastPrice(self):
		return self.LastPrice
	def getPriceInterval(self):
		return self.PriceInterval

	def __str__(self):
		return 'BrokerID=\'{0}\', InstrumentID=\'{1}\', ExchangeID=\'{2}\', LastPrice={3}, PriceInterval={4}'.format(str(self.BrokerID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), self.LastPrice, self.PriceInterval)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'LastPrice':self.LastPrice,'PriceInterval':self.PriceInterval}

	def clone(self):
		obj=CThostFtdcForQuoteParamField()
		obj.BrokerID=self.BrokerID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.LastPrice=self.LastPrice
		obj.PriceInterval=self.PriceInterval
		return obj

class CThostFtdcMMOptionInstrCommRateField(Structure):
	"""当前做市商期权合约手续费的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		#执行手续费率
		("StrikeRatioByMoney",c_double),
		#执行手续费
		("StrikeRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume
	def getStrikeRatioByMoney(self):
		return self.StrikeRatioByMoney
	def getStrikeRatioByVolume(self):
		return self.StrikeRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', OpenRatioByMoney={4}, OpenRatioByVolume={5}, CloseRatioByMoney={6}, CloseRatioByVolume={7}, CloseTodayRatioByMoney={8}, CloseTodayRatioByVolume={9}, StrikeRatioByMoney={10}, StrikeRatioByVolume={11}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OpenRatioByMoney, self.OpenRatioByVolume, self.CloseRatioByMoney, self.CloseRatioByVolume, self.CloseTodayRatioByMoney, self.CloseTodayRatioByVolume, self.StrikeRatioByMoney, self.StrikeRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OpenRatioByMoney':self.OpenRatioByMoney,'OpenRatioByVolume':self.OpenRatioByVolume,'CloseRatioByMoney':self.CloseRatioByMoney,'CloseRatioByVolume':self.CloseRatioByVolume,'CloseTodayRatioByMoney':self.CloseTodayRatioByMoney,'CloseTodayRatioByVolume':self.CloseTodayRatioByVolume,'StrikeRatioByMoney':self.StrikeRatioByMoney,'StrikeRatioByVolume':self.StrikeRatioByVolume}

	def clone(self):
		obj=CThostFtdcMMOptionInstrCommRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OpenRatioByMoney=self.OpenRatioByMoney
		obj.OpenRatioByVolume=self.OpenRatioByVolume
		obj.CloseRatioByMoney=self.CloseRatioByMoney
		obj.CloseRatioByVolume=self.CloseRatioByVolume
		obj.CloseTodayRatioByMoney=self.CloseTodayRatioByMoney
		obj.CloseTodayRatioByVolume=self.CloseTodayRatioByVolume
		obj.StrikeRatioByMoney=self.StrikeRatioByMoney
		obj.StrikeRatioByVolume=self.StrikeRatioByVolume
		return obj

class CThostFtdcQryMMOptionInstrCommRateField(Structure):
	"""做市商期权手续费率查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryMMOptionInstrCommRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcMMInstrumentCommissionRateField(Structure):
	"""做市商合约手续费率"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#开仓手续费率
		("OpenRatioByMoney",c_double),
		#开仓手续费
		("OpenRatioByVolume",c_double),
		#平仓手续费率
		("CloseRatioByMoney",c_double),
		#平仓手续费
		("CloseRatioByVolume",c_double),
		#平今手续费率
		("CloseTodayRatioByMoney",c_double),
		#平今手续费
		("CloseTodayRatioByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOpenRatioByMoney(self):
		return self.OpenRatioByMoney
	def getOpenRatioByVolume(self):
		return self.OpenRatioByVolume
	def getCloseRatioByMoney(self):
		return self.CloseRatioByMoney
	def getCloseRatioByVolume(self):
		return self.CloseRatioByVolume
	def getCloseTodayRatioByMoney(self):
		return self.CloseTodayRatioByMoney
	def getCloseTodayRatioByVolume(self):
		return self.CloseTodayRatioByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', OpenRatioByMoney={4}, OpenRatioByVolume={5}, CloseRatioByMoney={6}, CloseRatioByVolume={7}, CloseTodayRatioByMoney={8}, CloseTodayRatioByVolume={9}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OpenRatioByMoney, self.OpenRatioByVolume, self.CloseRatioByMoney, self.CloseRatioByVolume, self.CloseTodayRatioByMoney, self.CloseTodayRatioByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OpenRatioByMoney':self.OpenRatioByMoney,'OpenRatioByVolume':self.OpenRatioByVolume,'CloseRatioByMoney':self.CloseRatioByMoney,'CloseRatioByVolume':self.CloseRatioByVolume,'CloseTodayRatioByMoney':self.CloseTodayRatioByMoney,'CloseTodayRatioByVolume':self.CloseTodayRatioByVolume}

	def clone(self):
		obj=CThostFtdcMMInstrumentCommissionRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OpenRatioByMoney=self.OpenRatioByMoney
		obj.OpenRatioByVolume=self.OpenRatioByVolume
		obj.CloseRatioByMoney=self.CloseRatioByMoney
		obj.CloseRatioByVolume=self.CloseRatioByVolume
		obj.CloseTodayRatioByMoney=self.CloseTodayRatioByMoney
		obj.CloseTodayRatioByVolume=self.CloseTodayRatioByVolume
		return obj

class CThostFtdcQryMMInstrumentCommissionRateField(Structure):
	"""查询做市商合约手续费率"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryMMInstrumentCommissionRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcInstrumentOrderCommRateField(Structure):
	"""当前报单手续费的详细内容"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#投资者范围
		("InvestorRange",c_char),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#报单手续费
		("OrderCommByVolume",c_double),
		#撤单手续费
		("OrderActionCommByVolume",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getOrderCommByVolume(self):
		return self.OrderCommByVolume
	def getOrderActionCommByVolume(self):
		return self.OrderActionCommByVolume

	def __str__(self):
		return 'InstrumentID=\'{0}\', InvestorRange=InvestorRangeType.{1}, BrokerID=\'{2}\', InvestorID=\'{3}\', HedgeFlag=HedgeFlagType.{4}, OrderCommByVolume={5}, OrderActionCommByVolume={6}'.format(str(self.InstrumentID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.OrderCommByVolume, self.OrderActionCommByVolume)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'OrderCommByVolume':self.OrderCommByVolume,'OrderActionCommByVolume':self.OrderActionCommByVolume}

	def clone(self):
		obj=CThostFtdcInstrumentOrderCommRateField()
		obj.InstrumentID=self.InstrumentID
		obj.InvestorRange=self.InvestorRange
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.HedgeFlag=self.HedgeFlag
		obj.OrderCommByVolume=self.OrderCommByVolume
		obj.OrderActionCommByVolume=self.OrderActionCommByVolume
		return obj

class CThostFtdcQryInstrumentOrderCommRateField(Structure):
	"""报单手续费率查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInstrumentOrderCommRateField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcMarketDataField(Structure):
	"""市场行情"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#最新价
		("LastPrice",c_double),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		#今收盘
		("ClosePrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#昨虚实度
		("PreDelta",c_double),
		#今虚实度
		("CurrDelta",c_double),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getLastPrice(self):
		return self.LastPrice
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest
	def getClosePrice(self):
		return self.ClosePrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getPreDelta(self):
		return self.PreDelta
	def getCurrDelta(self):
		return self.CurrDelta
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getActionDay(self):
		return str(self.ActionDay, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\', InstrumentID=\'{1}\', ExchangeID=\'{2}\', ExchangeInstID=\'{3}\', LastPrice={4}, PreSettlementPrice={5}, PreClosePrice={6}, PreOpenInterest={7}, OpenPrice={8}, HighestPrice={9}, LowestPrice={10}, Volume={11}, Turnover={12}, OpenInterest={13}, ClosePrice={14}, SettlementPrice={15}, UpperLimitPrice={16}, LowerLimitPrice={17}, PreDelta={18}, CurrDelta={19}, UpdateTime=\'{20}\', UpdateMillisec={21}, ActionDay=\'{22}\''.format(str(self.TradingDay, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), self.LastPrice, self.PreSettlementPrice, self.PreClosePrice, self.PreOpenInterest, self.OpenPrice, self.HighestPrice, self.LowestPrice, self.Volume, self.Turnover, self.OpenInterest, self.ClosePrice, self.SettlementPrice, self.UpperLimitPrice, self.LowerLimitPrice, self.PreDelta, self.CurrDelta, str(self.UpdateTime, 'GB2312'), self.UpdateMillisec, str(self.ActionDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'LastPrice':self.LastPrice,'PreSettlementPrice':self.PreSettlementPrice,'PreClosePrice':self.PreClosePrice,'PreOpenInterest':self.PreOpenInterest,'OpenPrice':self.OpenPrice,'HighestPrice':self.HighestPrice,'LowestPrice':self.LowestPrice,'Volume':self.Volume,'Turnover':self.Turnover,'OpenInterest':self.OpenInterest,'ClosePrice':self.ClosePrice,'SettlementPrice':self.SettlementPrice,'UpperLimitPrice':self.UpperLimitPrice,'LowerLimitPrice':self.LowerLimitPrice,'PreDelta':self.PreDelta,'CurrDelta':self.CurrDelta,'UpdateTime':str(self.UpdateTime, 'GB2312'),'UpdateMillisec':self.UpdateMillisec,'ActionDay':str(self.ActionDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMarketDataField()
		obj.TradingDay=self.TradingDay
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.LastPrice=self.LastPrice
		obj.PreSettlementPrice=self.PreSettlementPrice
		obj.PreClosePrice=self.PreClosePrice
		obj.PreOpenInterest=self.PreOpenInterest
		obj.OpenPrice=self.OpenPrice
		obj.HighestPrice=self.HighestPrice
		obj.LowestPrice=self.LowestPrice
		obj.Volume=self.Volume
		obj.Turnover=self.Turnover
		obj.OpenInterest=self.OpenInterest
		obj.ClosePrice=self.ClosePrice
		obj.SettlementPrice=self.SettlementPrice
		obj.UpperLimitPrice=self.UpperLimitPrice
		obj.LowerLimitPrice=self.LowerLimitPrice
		obj.PreDelta=self.PreDelta
		obj.CurrDelta=self.CurrDelta
		obj.UpdateTime=self.UpdateTime
		obj.UpdateMillisec=self.UpdateMillisec
		obj.ActionDay=self.ActionDay
		return obj

class CThostFtdcMarketDataBaseField(Structure):
	"""行情基础属性"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#上次结算价
		("PreSettlementPrice",c_double),
		#昨收盘
		("PreClosePrice",c_double),
		#昨持仓量
		("PreOpenInterest",c_double),
		#昨虚实度
		("PreDelta",c_double),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPreSettlementPrice(self):
		return self.PreSettlementPrice
	def getPreClosePrice(self):
		return self.PreClosePrice
	def getPreOpenInterest(self):
		return self.PreOpenInterest
	def getPreDelta(self):
		return self.PreDelta

	def __str__(self):
		return 'TradingDay=\'{0}\', PreSettlementPrice={1}, PreClosePrice={2}, PreOpenInterest={3}, PreDelta={4}'.format(str(self.TradingDay, 'GB2312'), self.PreSettlementPrice, self.PreClosePrice, self.PreOpenInterest, self.PreDelta)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'PreSettlementPrice':self.PreSettlementPrice,'PreClosePrice':self.PreClosePrice,'PreOpenInterest':self.PreOpenInterest,'PreDelta':self.PreDelta}

	def clone(self):
		obj=CThostFtdcMarketDataBaseField()
		obj.TradingDay=self.TradingDay
		obj.PreSettlementPrice=self.PreSettlementPrice
		obj.PreClosePrice=self.PreClosePrice
		obj.PreOpenInterest=self.PreOpenInterest
		obj.PreDelta=self.PreDelta
		return obj

class CThostFtdcMarketDataStaticField(Structure):
	"""行情静态属性"""
	_fields_ = [
		#今开盘
		("OpenPrice",c_double),
		#最高价
		("HighestPrice",c_double),
		#最低价
		("LowestPrice",c_double),
		#今收盘
		("ClosePrice",c_double),
		#涨停板价
		("UpperLimitPrice",c_double),
		#跌停板价
		("LowerLimitPrice",c_double),
		#本次结算价
		("SettlementPrice",c_double),
		#今虚实度
		("CurrDelta",c_double),
		]

	def getOpenPrice(self):
		return self.OpenPrice
	def getHighestPrice(self):
		return self.HighestPrice
	def getLowestPrice(self):
		return self.LowestPrice
	def getClosePrice(self):
		return self.ClosePrice
	def getUpperLimitPrice(self):
		return self.UpperLimitPrice
	def getLowerLimitPrice(self):
		return self.LowerLimitPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getCurrDelta(self):
		return self.CurrDelta

	def __str__(self):
		return 'OpenPrice={0}, HighestPrice={1}, LowestPrice={2}, ClosePrice={3}, UpperLimitPrice={4}, LowerLimitPrice={5}, SettlementPrice={6}, CurrDelta={7}'.format(self.OpenPrice, self.HighestPrice, self.LowestPrice, self.ClosePrice, self.UpperLimitPrice, self.LowerLimitPrice, self.SettlementPrice, self.CurrDelta)

	@property
	def __dict__(self):
		return {'OpenPrice':self.OpenPrice,'HighestPrice':self.HighestPrice,'LowestPrice':self.LowestPrice,'ClosePrice':self.ClosePrice,'UpperLimitPrice':self.UpperLimitPrice,'LowerLimitPrice':self.LowerLimitPrice,'SettlementPrice':self.SettlementPrice,'CurrDelta':self.CurrDelta}

	def clone(self):
		obj=CThostFtdcMarketDataStaticField()
		obj.OpenPrice=self.OpenPrice
		obj.HighestPrice=self.HighestPrice
		obj.LowestPrice=self.LowestPrice
		obj.ClosePrice=self.ClosePrice
		obj.UpperLimitPrice=self.UpperLimitPrice
		obj.LowerLimitPrice=self.LowerLimitPrice
		obj.SettlementPrice=self.SettlementPrice
		obj.CurrDelta=self.CurrDelta
		return obj

class CThostFtdcMarketDataLastMatchField(Structure):
	"""行情最新成交属性"""
	_fields_ = [
		#最新价
		("LastPrice",c_double),
		#数量
		("Volume",c_int32),
		#成交金额
		("Turnover",c_double),
		#持仓量
		("OpenInterest",c_double),
		]

	def getLastPrice(self):
		return self.LastPrice
	def getVolume(self):
		return self.Volume
	def getTurnover(self):
		return self.Turnover
	def getOpenInterest(self):
		return self.OpenInterest

	def __str__(self):
		return 'LastPrice={0}, Volume={1}, Turnover={2}, OpenInterest={3}'.format(self.LastPrice, self.Volume, self.Turnover, self.OpenInterest)

	@property
	def __dict__(self):
		return {'LastPrice':self.LastPrice,'Volume':self.Volume,'Turnover':self.Turnover,'OpenInterest':self.OpenInterest}

	def clone(self):
		obj=CThostFtdcMarketDataLastMatchField()
		obj.LastPrice=self.LastPrice
		obj.Volume=self.Volume
		obj.Turnover=self.Turnover
		obj.OpenInterest=self.OpenInterest
		return obj

class CThostFtdcMarketDataBestPriceField(Structure):
	"""行情最优价属性"""
	_fields_ = [
		#申买价一
		("BidPrice1",c_double),
		#申买量一
		("BidVolume1",c_int32),
		#申卖价一
		("AskPrice1",c_double),
		#申卖量一
		("AskVolume1",c_int32),
		]

	def getBidPrice1(self):
		return self.BidPrice1
	def getBidVolume1(self):
		return self.BidVolume1
	def getAskPrice1(self):
		return self.AskPrice1
	def getAskVolume1(self):
		return self.AskVolume1

	def __str__(self):
		return 'BidPrice1={0}, BidVolume1={1}, AskPrice1={2}, AskVolume1={3}'.format(self.BidPrice1, self.BidVolume1, self.AskPrice1, self.AskVolume1)

	@property
	def __dict__(self):
		return {'BidPrice1':self.BidPrice1,'BidVolume1':self.BidVolume1,'AskPrice1':self.AskPrice1,'AskVolume1':self.AskVolume1}

	def clone(self):
		obj=CThostFtdcMarketDataBestPriceField()
		obj.BidPrice1=self.BidPrice1
		obj.BidVolume1=self.BidVolume1
		obj.AskPrice1=self.AskPrice1
		obj.AskVolume1=self.AskVolume1
		return obj

class CThostFtdcMarketDataBid23Field(Structure):
	"""行情申买二、三属性"""
	_fields_ = [
		#申买价二
		("BidPrice2",c_double),
		#申买量二
		("BidVolume2",c_int32),
		#申买价三
		("BidPrice3",c_double),
		#申买量三
		("BidVolume3",c_int32),
		]

	def getBidPrice2(self):
		return self.BidPrice2
	def getBidVolume2(self):
		return self.BidVolume2
	def getBidPrice3(self):
		return self.BidPrice3
	def getBidVolume3(self):
		return self.BidVolume3

	def __str__(self):
		return 'BidPrice2={0}, BidVolume2={1}, BidPrice3={2}, BidVolume3={3}'.format(self.BidPrice2, self.BidVolume2, self.BidPrice3, self.BidVolume3)

	@property
	def __dict__(self):
		return {'BidPrice2':self.BidPrice2,'BidVolume2':self.BidVolume2,'BidPrice3':self.BidPrice3,'BidVolume3':self.BidVolume3}

	def clone(self):
		obj=CThostFtdcMarketDataBid23Field()
		obj.BidPrice2=self.BidPrice2
		obj.BidVolume2=self.BidVolume2
		obj.BidPrice3=self.BidPrice3
		obj.BidVolume3=self.BidVolume3
		return obj

class CThostFtdcMarketDataAsk23Field(Structure):
	"""行情申卖二、三属性"""
	_fields_ = [
		#申卖价二
		("AskPrice2",c_double),
		#申卖量二
		("AskVolume2",c_int32),
		#申卖价三
		("AskPrice3",c_double),
		#申卖量三
		("AskVolume3",c_int32),
		]

	def getAskPrice2(self):
		return self.AskPrice2
	def getAskVolume2(self):
		return self.AskVolume2
	def getAskPrice3(self):
		return self.AskPrice3
	def getAskVolume3(self):
		return self.AskVolume3

	def __str__(self):
		return 'AskPrice2={0}, AskVolume2={1}, AskPrice3={2}, AskVolume3={3}'.format(self.AskPrice2, self.AskVolume2, self.AskPrice3, self.AskVolume3)

	@property
	def __dict__(self):
		return {'AskPrice2':self.AskPrice2,'AskVolume2':self.AskVolume2,'AskPrice3':self.AskPrice3,'AskVolume3':self.AskVolume3}

	def clone(self):
		obj=CThostFtdcMarketDataAsk23Field()
		obj.AskPrice2=self.AskPrice2
		obj.AskVolume2=self.AskVolume2
		obj.AskPrice3=self.AskPrice3
		obj.AskVolume3=self.AskVolume3
		return obj

class CThostFtdcMarketDataBid45Field(Structure):
	"""行情申买四、五属性"""
	_fields_ = [
		#申买价四
		("BidPrice4",c_double),
		#申买量四
		("BidVolume4",c_int32),
		#申买价五
		("BidPrice5",c_double),
		#申买量五
		("BidVolume5",c_int32),
		]

	def getBidPrice4(self):
		return self.BidPrice4
	def getBidVolume4(self):
		return self.BidVolume4
	def getBidPrice5(self):
		return self.BidPrice5
	def getBidVolume5(self):
		return self.BidVolume5

	def __str__(self):
		return 'BidPrice4={0}, BidVolume4={1}, BidPrice5={2}, BidVolume5={3}'.format(self.BidPrice4, self.BidVolume4, self.BidPrice5, self.BidVolume5)

	@property
	def __dict__(self):
		return {'BidPrice4':self.BidPrice4,'BidVolume4':self.BidVolume4,'BidPrice5':self.BidPrice5,'BidVolume5':self.BidVolume5}

	def clone(self):
		obj=CThostFtdcMarketDataBid45Field()
		obj.BidPrice4=self.BidPrice4
		obj.BidVolume4=self.BidVolume4
		obj.BidPrice5=self.BidPrice5
		obj.BidVolume5=self.BidVolume5
		return obj

class CThostFtdcMarketDataAsk45Field(Structure):
	"""行情申卖四、五属性"""
	_fields_ = [
		#申卖价四
		("AskPrice4",c_double),
		#申卖量四
		("AskVolume4",c_int32),
		#申卖价五
		("AskPrice5",c_double),
		#申卖量五
		("AskVolume5",c_int32),
		]

	def getAskPrice4(self):
		return self.AskPrice4
	def getAskVolume4(self):
		return self.AskVolume4
	def getAskPrice5(self):
		return self.AskPrice5
	def getAskVolume5(self):
		return self.AskVolume5

	def __str__(self):
		return 'AskPrice4={0}, AskVolume4={1}, AskPrice5={2}, AskVolume5={3}'.format(self.AskPrice4, self.AskVolume4, self.AskPrice5, self.AskVolume5)

	@property
	def __dict__(self):
		return {'AskPrice4':self.AskPrice4,'AskVolume4':self.AskVolume4,'AskPrice5':self.AskPrice5,'AskVolume5':self.AskVolume5}

	def clone(self):
		obj=CThostFtdcMarketDataAsk45Field()
		obj.AskPrice4=self.AskPrice4
		obj.AskVolume4=self.AskVolume4
		obj.AskPrice5=self.AskPrice5
		obj.AskVolume5=self.AskVolume5
		return obj

class CThostFtdcMarketDataUpdateTimeField(Structure):
	"""行情更新时间属性"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#最后修改时间
		("UpdateTime",c_char*9),
		#最后修改毫秒
		("UpdateMillisec",c_int32),
		#业务日期
		("ActionDay",c_char*9),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getUpdateMillisec(self):
		return self.UpdateMillisec
	def getActionDay(self):
		return str(self.ActionDay, 'GB2312')

	def __str__(self):
		return 'InstrumentID=\'{0}\', UpdateTime=\'{1}\', UpdateMillisec={2}, ActionDay=\'{3}\''.format(str(self.InstrumentID, 'GB2312'), str(self.UpdateTime, 'GB2312'), self.UpdateMillisec, str(self.ActionDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'UpdateTime':str(self.UpdateTime, 'GB2312'),'UpdateMillisec':self.UpdateMillisec,'ActionDay':str(self.ActionDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMarketDataUpdateTimeField()
		obj.InstrumentID=self.InstrumentID
		obj.UpdateTime=self.UpdateTime
		obj.UpdateMillisec=self.UpdateMillisec
		obj.ActionDay=self.ActionDay
		return obj

class CThostFtdcMarketDataExchangeField(Structure):
	"""行情交易所代码属性"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\''.format(str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMarketDataExchangeField()
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcSpecificInstrumentField(Structure):
	"""指定的合约"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'InstrumentID=\'{0}\''.format(str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSpecificInstrumentField()
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcInstrumentStatusField(Structure):
	"""合约状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#结算组代码
		("SettlementGroupID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#合约交易状态
		("InstrumentStatus",c_char),
		#交易阶段编号
		("TradingSegmentSN",c_int32),
		#进入本状态时间
		("EnterTime",c_char*9),
		#进入本状态原因
		("EnterReason",c_char),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getSettlementGroupID(self):
		return str(self.SettlementGroupID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getInstrumentStatus(self):
		return InstrumentStatusType(ord(self.InstrumentStatus))
	def getTradingSegmentSN(self):
		return self.TradingSegmentSN
	def getEnterTime(self):
		return str(self.EnterTime, 'GB2312')
	def getEnterReason(self):
		return InstStatusEnterReasonType(ord(self.EnterReason))

	def __str__(self):
		return 'ExchangeID=\'{0}\', ExchangeInstID=\'{1}\', SettlementGroupID=\'{2}\', InstrumentID=\'{3}\', InstrumentStatus=InstrumentStatusType.{4}, TradingSegmentSN={5}, EnterTime=\'{6}\', EnterReason=InstStatusEnterReasonType.{7}'.format(str(self.ExchangeID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.SettlementGroupID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.InstrumentStatus) == 0 else InstrumentStatusType(ord(self.InstrumentStatus)).name, self.TradingSegmentSN, str(self.EnterTime, 'GB2312'), '' if ord(self.EnterReason) == 0 else InstStatusEnterReasonType(ord(self.EnterReason)).name)

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'SettlementGroupID':str(self.SettlementGroupID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'InstrumentStatus':'' if ord(self.InstrumentStatus) == 0 else InstrumentStatusType(ord(self.InstrumentStatus)).name,'TradingSegmentSN':self.TradingSegmentSN,'EnterTime':str(self.EnterTime, 'GB2312'),'EnterReason':'' if ord(self.EnterReason) == 0 else InstStatusEnterReasonType(ord(self.EnterReason)).name}

	def clone(self):
		obj=CThostFtdcInstrumentStatusField()
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.SettlementGroupID=self.SettlementGroupID
		obj.InstrumentID=self.InstrumentID
		obj.InstrumentStatus=self.InstrumentStatus
		obj.TradingSegmentSN=self.TradingSegmentSN
		obj.EnterTime=self.EnterTime
		obj.EnterReason=self.EnterReason
		return obj

class CThostFtdcQryInstrumentStatusField(Structure):
	"""查询合约状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ExchangeInstID=\'{1}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInstrumentStatusField()
		obj.ExchangeID=self.ExchangeID
		obj.ExchangeInstID=self.ExchangeInstID
		return obj

class CThostFtdcInvestorAccountField(Structure):
	"""投资者账户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投资者帐号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', AccountID=\'{2}\', CurrencyID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcInvestorAccountField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcPositionProfitAlgorithmField(Structure):
	"""浮动盈亏算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#盈亏算法
		("Algorithm",c_char),
		#备注
		("Memo",c_char*161),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getAlgorithm(self):
		return AlgorithmType(ord(self.Algorithm))
	def getMemo(self):
		return str(self.Memo, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', Algorithm=AlgorithmType.{2}, Memo=\'{3}\', CurrencyID=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), '' if ord(self.Algorithm) == 0 else AlgorithmType(ord(self.Algorithm)).name, str(self.Memo, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Algorithm':'' if ord(self.Algorithm) == 0 else AlgorithmType(ord(self.Algorithm)).name,'Memo':str(self.Memo, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcPositionProfitAlgorithmField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.Algorithm=self.Algorithm
		obj.Memo=self.Memo
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcDiscountField(Structure):
	"""会员资金折扣"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#资金折扣比例
		("Discount",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getDiscount(self):
		return self.Discount

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorRange=InvestorRangeType.{1}, InvestorID=\'{2}\', Discount={3}'.format(str(self.BrokerID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.InvestorID, 'GB2312'), self.Discount)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'InvestorID':str(self.InvestorID, 'GB2312'),'Discount':self.Discount}

	def clone(self):
		obj=CThostFtdcDiscountField()
		obj.BrokerID=self.BrokerID
		obj.InvestorRange=self.InvestorRange
		obj.InvestorID=self.InvestorID
		obj.Discount=self.Discount
		return obj

class CThostFtdcQryTransferBankField(Structure):
	"""查询转帐银行"""
	_fields_ = [
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		]

	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')

	def __str__(self):
		return 'BankID=\'{0}\', BankBrchID=\'{1}\''.format(str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTransferBankField()
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		return obj

class CThostFtdcTransferBankField(Structure):
	"""转帐银行"""
	_fields_ = [
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行名称
		("BankName",c_char*101),
		#是否活跃
		("IsActive",c_int32),
		]

	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')
	def getBankName(self):
		return str(self.BankName, 'GB2312')
	def getIsActive(self):
		return self.IsActive

	def __str__(self):
		return 'BankID=\'{0}\', BankBrchID=\'{1}\', BankName=\'{2}\', IsActive={3}'.format(str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'), str(self.BankName, 'GB2312'), self.IsActive)

	@property
	def __dict__(self):
		return {'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312'),'BankName':str(self.BankName, 'GB2312'),'IsActive':self.IsActive}

	def clone(self):
		obj=CThostFtdcTransferBankField()
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		obj.BankName=self.BankName
		obj.IsActive=self.IsActive
		return obj

class CThostFtdcQryInvestorPositionDetailField(Structure):
	"""查询投资者持仓明细"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInvestorPositionDetailField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcInvestorPositionDetailField(Structure):
	"""投资者持仓明细"""
	_fields_ = [
		#合约代码
		("InstrumentID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#投机套保标志
		("HedgeFlag",c_char),
		#买卖
		("Direction",c_char),
		#开仓日期
		("OpenDate",c_char*9),
		#成交编号
		("TradeID",c_char*21),
		#数量
		("Volume",c_int32),
		#开仓价
		("OpenPrice",c_double),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#成交类型
		("TradeType",c_char),
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#逐日盯市平仓盈亏
		("CloseProfitByDate",c_double),
		#逐笔对冲平仓盈亏
		("CloseProfitByTrade",c_double),
		#逐日盯市持仓盈亏
		("PositionProfitByDate",c_double),
		#逐笔对冲持仓盈亏
		("PositionProfitByTrade",c_double),
		#投资者保证金
		("Margin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#昨结算价
		("LastSettlementPrice",c_double),
		#结算价
		("SettlementPrice",c_double),
		#平仓量
		("CloseVolume",c_int32),
		#平仓金额
		("CloseAmount",c_double),
		]

	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOpenDate(self):
		return str(self.OpenDate, 'GB2312')
	def getTradeID(self):
		return str(self.TradeID, 'GB2312')
	def getVolume(self):
		return self.Volume
	def getOpenPrice(self):
		return self.OpenPrice
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getTradeType(self):
		return TradeTypeType(ord(self.TradeType))
	def getCombInstrumentID(self):
		return str(self.CombInstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getCloseProfitByDate(self):
		return self.CloseProfitByDate
	def getCloseProfitByTrade(self):
		return self.CloseProfitByTrade
	def getPositionProfitByDate(self):
		return self.PositionProfitByDate
	def getPositionProfitByTrade(self):
		return self.PositionProfitByTrade
	def getMargin(self):
		return self.Margin
	def getExchMargin(self):
		return self.ExchMargin
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getLastSettlementPrice(self):
		return self.LastSettlementPrice
	def getSettlementPrice(self):
		return self.SettlementPrice
	def getCloseVolume(self):
		return self.CloseVolume
	def getCloseAmount(self):
		return self.CloseAmount

	def __str__(self):
		return 'InstrumentID=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', HedgeFlag=HedgeFlagType.{3}, Direction=DirectionType.{4}, OpenDate=\'{5}\', TradeID=\'{6}\', Volume={7}, OpenPrice={8}, TradingDay=\'{9}\', SettlementID={10}, TradeType=TradeTypeType.{11}, CombInstrumentID=\'{12}\', ExchangeID=\'{13}\', CloseProfitByDate={14}, CloseProfitByTrade={15}, PositionProfitByDate={16}, PositionProfitByTrade={17}, Margin={18}, ExchMargin={19}, MarginRateByMoney={20}, MarginRateByVolume={21}, LastSettlementPrice={22}, SettlementPrice={23}, CloseVolume={24}, CloseAmount={25}'.format(str(self.InstrumentID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.OpenDate, 'GB2312'), str(self.TradeID, 'GB2312'), self.Volume, self.OpenPrice, str(self.TradingDay, 'GB2312'), self.SettlementID, '' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name, str(self.CombInstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'), self.CloseProfitByDate, self.CloseProfitByTrade, self.PositionProfitByDate, self.PositionProfitByTrade, self.Margin, self.ExchMargin, self.MarginRateByMoney, self.MarginRateByVolume, self.LastSettlementPrice, self.SettlementPrice, self.CloseVolume, self.CloseAmount)

	@property
	def __dict__(self):
		return {'InstrumentID':str(self.InstrumentID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'OpenDate':str(self.OpenDate, 'GB2312'),'TradeID':str(self.TradeID, 'GB2312'),'Volume':self.Volume,'OpenPrice':self.OpenPrice,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'TradeType':'' if ord(self.TradeType) == 0 else TradeTypeType(ord(self.TradeType)).name,'CombInstrumentID':str(self.CombInstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'CloseProfitByDate':self.CloseProfitByDate,'CloseProfitByTrade':self.CloseProfitByTrade,'PositionProfitByDate':self.PositionProfitByDate,'PositionProfitByTrade':self.PositionProfitByTrade,'Margin':self.Margin,'ExchMargin':self.ExchMargin,'MarginRateByMoney':self.MarginRateByMoney,'MarginRateByVolume':self.MarginRateByVolume,'LastSettlementPrice':self.LastSettlementPrice,'SettlementPrice':self.SettlementPrice,'CloseVolume':self.CloseVolume,'CloseAmount':self.CloseAmount}

	def clone(self):
		obj=CThostFtdcInvestorPositionDetailField()
		obj.InstrumentID=self.InstrumentID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.HedgeFlag=self.HedgeFlag
		obj.Direction=self.Direction
		obj.OpenDate=self.OpenDate
		obj.TradeID=self.TradeID
		obj.Volume=self.Volume
		obj.OpenPrice=self.OpenPrice
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.TradeType=self.TradeType
		obj.CombInstrumentID=self.CombInstrumentID
		obj.ExchangeID=self.ExchangeID
		obj.CloseProfitByDate=self.CloseProfitByDate
		obj.CloseProfitByTrade=self.CloseProfitByTrade
		obj.PositionProfitByDate=self.PositionProfitByDate
		obj.PositionProfitByTrade=self.PositionProfitByTrade
		obj.Margin=self.Margin
		obj.ExchMargin=self.ExchMargin
		obj.MarginRateByMoney=self.MarginRateByMoney
		obj.MarginRateByVolume=self.MarginRateByVolume
		obj.LastSettlementPrice=self.LastSettlementPrice
		obj.SettlementPrice=self.SettlementPrice
		obj.CloseVolume=self.CloseVolume
		obj.CloseAmount=self.CloseAmount
		return obj

class CThostFtdcTradingAccountPasswordField(Structure):
	"""资金账户口令域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', Password=\'{2}\', CurrencyID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTradingAccountPasswordField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcMDTraderOfferField(Structure):
	"""交易所行情报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#会员代码
		("ParticipantID",c_char*11),
		#密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所交易员连接状态
		("TraderConnectStatus",c_char),
		#发出连接请求的日期
		("ConnectRequestDate",c_char*9),
		#发出连接请求的时间
		("ConnectRequestTime",c_char*9),
		#上次报告日期
		("LastReportDate",c_char*9),
		#上次报告时间
		("LastReportTime",c_char*9),
		#完成连接日期
		("ConnectDate",c_char*9),
		#完成连接时间
		("ConnectTime",c_char*9),
		#启动日期
		("StartDate",c_char*9),
		#启动时间
		("StartTime",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#本席位最大成交编号
		("MaxTradeID",c_char*21),
		#本席位最大报单备拷
		("MaxOrderMessageReference",c_char*7),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getTraderConnectStatus(self):
		return TraderConnectStatusType(ord(self.TraderConnectStatus))
	def getConnectRequestDate(self):
		return str(self.ConnectRequestDate, 'GB2312')
	def getConnectRequestTime(self):
		return str(self.ConnectRequestTime, 'GB2312')
	def getLastReportDate(self):
		return str(self.LastReportDate, 'GB2312')
	def getLastReportTime(self):
		return str(self.LastReportTime, 'GB2312')
	def getConnectDate(self):
		return str(self.ConnectDate, 'GB2312')
	def getConnectTime(self):
		return str(self.ConnectTime, 'GB2312')
	def getStartDate(self):
		return str(self.StartDate, 'GB2312')
	def getStartTime(self):
		return str(self.StartTime, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getMaxTradeID(self):
		return str(self.MaxTradeID, 'GB2312')
	def getMaxOrderMessageReference(self):
		return str(self.MaxOrderMessageReference, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', TraderID=\'{1}\', ParticipantID=\'{2}\', Password=\'{3}\', InstallID={4}, OrderLocalID=\'{5}\', TraderConnectStatus=TraderConnectStatusType.{6}, ConnectRequestDate=\'{7}\', ConnectRequestTime=\'{8}\', LastReportDate=\'{9}\', LastReportTime=\'{10}\', ConnectDate=\'{11}\', ConnectTime=\'{12}\', StartDate=\'{13}\', StartTime=\'{14}\', TradingDay=\'{15}\', BrokerID=\'{16}\', MaxTradeID=\'{17}\', MaxOrderMessageReference=\'{18}\''.format(str(self.ExchangeID, 'GB2312'), str(self.TraderID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), '' if ord(self.TraderConnectStatus) == 0 else TraderConnectStatusType(ord(self.TraderConnectStatus)).name, str(self.ConnectRequestDate, 'GB2312'), str(self.ConnectRequestTime, 'GB2312'), str(self.LastReportDate, 'GB2312'), str(self.LastReportTime, 'GB2312'), str(self.ConnectDate, 'GB2312'), str(self.ConnectTime, 'GB2312'), str(self.StartDate, 'GB2312'), str(self.StartTime, 'GB2312'), str(self.TradingDay, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.MaxTradeID, 'GB2312'), str(self.MaxOrderMessageReference, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'TraderConnectStatus':'' if ord(self.TraderConnectStatus) == 0 else TraderConnectStatusType(ord(self.TraderConnectStatus)).name,'ConnectRequestDate':str(self.ConnectRequestDate, 'GB2312'),'ConnectRequestTime':str(self.ConnectRequestTime, 'GB2312'),'LastReportDate':str(self.LastReportDate, 'GB2312'),'LastReportTime':str(self.LastReportTime, 'GB2312'),'ConnectDate':str(self.ConnectDate, 'GB2312'),'ConnectTime':str(self.ConnectTime, 'GB2312'),'StartDate':str(self.StartDate, 'GB2312'),'StartTime':str(self.StartTime, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'MaxTradeID':str(self.MaxTradeID, 'GB2312'),'MaxOrderMessageReference':str(self.MaxOrderMessageReference, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMDTraderOfferField()
		obj.ExchangeID=self.ExchangeID
		obj.TraderID=self.TraderID
		obj.ParticipantID=self.ParticipantID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.TraderConnectStatus=self.TraderConnectStatus
		obj.ConnectRequestDate=self.ConnectRequestDate
		obj.ConnectRequestTime=self.ConnectRequestTime
		obj.LastReportDate=self.LastReportDate
		obj.LastReportTime=self.LastReportTime
		obj.ConnectDate=self.ConnectDate
		obj.ConnectTime=self.ConnectTime
		obj.StartDate=self.StartDate
		obj.StartTime=self.StartTime
		obj.TradingDay=self.TradingDay
		obj.BrokerID=self.BrokerID
		obj.MaxTradeID=self.MaxTradeID
		obj.MaxOrderMessageReference=self.MaxOrderMessageReference
		return obj

class CThostFtdcQryMDTraderOfferField(Structure):
	"""查询行情报盘机"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所交易员代码
		("TraderID",c_char*21),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', ParticipantID=\'{1}\', TraderID=\'{2}\''.format(str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.TraderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryMDTraderOfferField()
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.TraderID=self.TraderID
		return obj

class CThostFtdcQryNoticeField(Structure):
	"""查询客户通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryNoticeField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcNoticeField(Structure):
	"""客户通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#消息正文
		("Content",c_char*501),
		#经纪公司通知内容序列号
		("SequenceLabel",c_char*2),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getContent(self):
		return str(self.Content, 'GB2312')
	def getSequenceLabel(self):
		return str(self.SequenceLabel, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', Content=\'{1}\', SequenceLabel=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.Content, 'GB2312'), str(self.SequenceLabel, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'Content':str(self.Content, 'GB2312'),'SequenceLabel':str(self.SequenceLabel, 'GB2312')}

	def clone(self):
		obj=CThostFtdcNoticeField()
		obj.BrokerID=self.BrokerID
		obj.Content=self.Content
		obj.SequenceLabel=self.SequenceLabel
		return obj

class CThostFtdcUserRightField(Structure):
	"""用户权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#客户权限类型
		("UserRightType",c_char),
		#是否禁止
		("IsForbidden",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserRightType(self):
		return UserRightTypeType(ord(self.UserRightType))
	def getIsForbidden(self):
		return self.IsForbidden

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserRightType=UserRightTypeType.{2}, IsForbidden={3}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.UserRightType) == 0 else UserRightTypeType(ord(self.UserRightType)).name, self.IsForbidden)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserRightType':'' if ord(self.UserRightType) == 0 else UserRightTypeType(ord(self.UserRightType)).name,'IsForbidden':self.IsForbidden}

	def clone(self):
		obj=CThostFtdcUserRightField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserRightType=self.UserRightType
		obj.IsForbidden=self.IsForbidden
		return obj

class CThostFtdcQrySettlementInfoConfirmField(Structure):
	"""查询结算信息确认域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySettlementInfoConfirmField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcLoadSettlementInfoField(Structure):
	"""装载结算信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcLoadSettlementInfoField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcBrokerWithdrawAlgorithmField(Structure):
	"""经纪公司可提资金算法表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#可提资金算法
		("WithdrawAlgorithm",c_char),
		#资金使用率
		("UsingRatio",c_double),
		#可提是否包含平仓盈利
		("IncludeCloseProfit",c_char),
		#本日无仓且无成交客户是否受可提比例限制
		("AllWithoutTrade",c_char),
		#可用是否包含平仓盈利
		("AvailIncludeCloseProfit",c_char),
		#是否启用用户事件
		("IsBrokerUserEvent",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		#货币质押比率
		("FundMortgageRatio",c_double),
		#权益算法
		("BalanceAlgorithm",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getWithdrawAlgorithm(self):
		return AlgorithmType(ord(self.WithdrawAlgorithm))
	def getUsingRatio(self):
		return self.UsingRatio
	def getIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.IncludeCloseProfit))
	def getAllWithoutTrade(self):
		return AllWithoutTradeType(ord(self.AllWithoutTrade))
	def getAvailIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit))
	def getIsBrokerUserEvent(self):
		return self.IsBrokerUserEvent
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getFundMortgageRatio(self):
		return self.FundMortgageRatio
	def getBalanceAlgorithm(self):
		return BalanceAlgorithmType(ord(self.BalanceAlgorithm))

	def __str__(self):
		return 'BrokerID=\'{0}\', WithdrawAlgorithm=AlgorithmType.{1}, UsingRatio={2}, IncludeCloseProfit=IncludeCloseProfitType.{3}, AllWithoutTrade=AllWithoutTradeType.{4}, AvailIncludeCloseProfit=IncludeCloseProfitType.{5}, IsBrokerUserEvent={6}, CurrencyID=\'{7}\', FundMortgageRatio={8}, BalanceAlgorithm=BalanceAlgorithmType.{9}'.format(str(self.BrokerID, 'GB2312'), '' if ord(self.WithdrawAlgorithm) == 0 else AlgorithmType(ord(self.WithdrawAlgorithm)).name, self.UsingRatio, '' if ord(self.IncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.IncludeCloseProfit)).name, '' if ord(self.AllWithoutTrade) == 0 else AllWithoutTradeType(ord(self.AllWithoutTrade)).name, '' if ord(self.AvailIncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)).name, self.IsBrokerUserEvent, str(self.CurrencyID, 'GB2312'), self.FundMortgageRatio, '' if ord(self.BalanceAlgorithm) == 0 else BalanceAlgorithmType(ord(self.BalanceAlgorithm)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'WithdrawAlgorithm':'' if ord(self.WithdrawAlgorithm) == 0 else AlgorithmType(ord(self.WithdrawAlgorithm)).name,'UsingRatio':self.UsingRatio,'IncludeCloseProfit':'' if ord(self.IncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.IncludeCloseProfit)).name,'AllWithoutTrade':'' if ord(self.AllWithoutTrade) == 0 else AllWithoutTradeType(ord(self.AllWithoutTrade)).name,'AvailIncludeCloseProfit':'' if ord(self.AvailIncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)).name,'IsBrokerUserEvent':self.IsBrokerUserEvent,'CurrencyID':str(self.CurrencyID, 'GB2312'),'FundMortgageRatio':self.FundMortgageRatio,'BalanceAlgorithm':'' if ord(self.BalanceAlgorithm) == 0 else BalanceAlgorithmType(ord(self.BalanceAlgorithm)).name}

	def clone(self):
		obj=CThostFtdcBrokerWithdrawAlgorithmField()
		obj.BrokerID=self.BrokerID
		obj.WithdrawAlgorithm=self.WithdrawAlgorithm
		obj.UsingRatio=self.UsingRatio
		obj.IncludeCloseProfit=self.IncludeCloseProfit
		obj.AllWithoutTrade=self.AllWithoutTrade
		obj.AvailIncludeCloseProfit=self.AvailIncludeCloseProfit
		obj.IsBrokerUserEvent=self.IsBrokerUserEvent
		obj.CurrencyID=self.CurrencyID
		obj.FundMortgageRatio=self.FundMortgageRatio
		obj.BalanceAlgorithm=self.BalanceAlgorithm
		return obj

class CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
	"""资金账户口令变更域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOldPassword(self):
		return str(self.OldPassword, 'GB2312')
	def getNewPassword(self):
		return str(self.NewPassword, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OldPassword=\'{2}\', NewPassword=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.OldPassword, 'GB2312'), str(self.NewPassword, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OldPassword':str(self.OldPassword, 'GB2312'),'NewPassword':str(self.NewPassword, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTradingAccountPasswordUpdateV1Field()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OldPassword=self.OldPassword
		obj.NewPassword=self.NewPassword
		return obj

class CThostFtdcTradingAccountPasswordUpdateField(Structure):
	"""资金账户口令变更域"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#原来的口令
		("OldPassword",c_char*41),
		#新的口令
		("NewPassword",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getOldPassword(self):
		return str(self.OldPassword, 'GB2312')
	def getNewPassword(self):
		return str(self.NewPassword, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', OldPassword=\'{2}\', NewPassword=\'{3}\', CurrencyID=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.OldPassword, 'GB2312'), str(self.NewPassword, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'OldPassword':str(self.OldPassword, 'GB2312'),'NewPassword':str(self.NewPassword, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTradingAccountPasswordUpdateField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.OldPassword=self.OldPassword
		obj.NewPassword=self.NewPassword
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcQryCombinationLegField(Structure):
	"""查询组合合约分腿"""
	_fields_ = [
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#单腿编号
		("LegID",c_int32),
		#单腿合约代码
		("LegInstrumentID",c_char*31),
		]

	def getCombInstrumentID(self):
		return str(self.CombInstrumentID, 'GB2312')
	def getLegID(self):
		return self.LegID
	def getLegInstrumentID(self):
		return str(self.LegInstrumentID, 'GB2312')

	def __str__(self):
		return 'CombInstrumentID=\'{0}\', LegID={1}, LegInstrumentID=\'{2}\''.format(str(self.CombInstrumentID, 'GB2312'), self.LegID, str(self.LegInstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'CombInstrumentID':str(self.CombInstrumentID, 'GB2312'),'LegID':self.LegID,'LegInstrumentID':str(self.LegInstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCombinationLegField()
		obj.CombInstrumentID=self.CombInstrumentID
		obj.LegID=self.LegID
		obj.LegInstrumentID=self.LegInstrumentID
		return obj

class CThostFtdcQrySyncStatusField(Structure):
	"""查询组合合约分腿"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')

	def __str__(self):
		return 'TradingDay=\'{0}\''.format(str(self.TradingDay, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySyncStatusField()
		obj.TradingDay=self.TradingDay
		return obj

class CThostFtdcCombinationLegField(Structure):
	"""组合交易合约的单腿"""
	_fields_ = [
		#组合合约代码
		("CombInstrumentID",c_char*31),
		#单腿编号
		("LegID",c_int32),
		#单腿合约代码
		("LegInstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#单腿乘数
		("LegMultiple",c_int32),
		#派生层数
		("ImplyLevel",c_int32),
		]

	def getCombInstrumentID(self):
		return str(self.CombInstrumentID, 'GB2312')
	def getLegID(self):
		return self.LegID
	def getLegInstrumentID(self):
		return str(self.LegInstrumentID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getLegMultiple(self):
		return self.LegMultiple
	def getImplyLevel(self):
		return self.ImplyLevel

	def __str__(self):
		return 'CombInstrumentID=\'{0}\', LegID={1}, LegInstrumentID=\'{2}\', Direction=DirectionType.{3}, LegMultiple={4}, ImplyLevel={5}'.format(str(self.CombInstrumentID, 'GB2312'), self.LegID, str(self.LegInstrumentID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, self.LegMultiple, self.ImplyLevel)

	@property
	def __dict__(self):
		return {'CombInstrumentID':str(self.CombInstrumentID, 'GB2312'),'LegID':self.LegID,'LegInstrumentID':str(self.LegInstrumentID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'LegMultiple':self.LegMultiple,'ImplyLevel':self.ImplyLevel}

	def clone(self):
		obj=CThostFtdcCombinationLegField()
		obj.CombInstrumentID=self.CombInstrumentID
		obj.LegID=self.LegID
		obj.LegInstrumentID=self.LegInstrumentID
		obj.Direction=self.Direction
		obj.LegMultiple=self.LegMultiple
		obj.ImplyLevel=self.ImplyLevel
		return obj

class CThostFtdcSyncStatusField(Structure):
	"""数据同步状态"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#数据同步状态
		("DataSyncStatus",c_char),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getDataSyncStatus(self):
		return DataSyncStatusType(ord(self.DataSyncStatus))

	def __str__(self):
		return 'TradingDay=\'{0}\', DataSyncStatus=DataSyncStatusType.{1}'.format(str(self.TradingDay, 'GB2312'), '' if ord(self.DataSyncStatus) == 0 else DataSyncStatusType(ord(self.DataSyncStatus)).name)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'DataSyncStatus':'' if ord(self.DataSyncStatus) == 0 else DataSyncStatusType(ord(self.DataSyncStatus)).name}

	def clone(self):
		obj=CThostFtdcSyncStatusField()
		obj.TradingDay=self.TradingDay
		obj.DataSyncStatus=self.DataSyncStatus
		return obj

class CThostFtdcQryLinkManField(Structure):
	"""查询联系人"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryLinkManField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcLinkManField(Structure):
	"""联系人"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#联系人类型
		("PersonType",c_char),
		#证件类型
		("IdentifiedCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#名称
		("PersonName",c_char*81),
		#联系电话
		("Telephone",c_char*41),
		#通讯地址
		("Address",c_char*101),
		#邮政编码
		("ZipCode",c_char*7),
		#优先级
		("Priority",c_int32),
		#开户邮政编码
		("UOAZipCode",c_char*11),
		#全称
		("PersonFullName",c_char*101),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getPersonType(self):
		return PersonTypeType(ord(self.PersonType))
	def getIdentifiedCardType(self):
		return IdCardTypeType(ord(self.IdentifiedCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getPersonName(self):
		return str(self.PersonName, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getPriority(self):
		return self.Priority
	def getUOAZipCode(self):
		return str(self.UOAZipCode, 'GB2312')
	def getPersonFullName(self):
		return str(self.PersonFullName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', PersonType=PersonTypeType.{2}, IdentifiedCardType=IdCardTypeType.{3}, IdentifiedCardNo=\'{4}\', PersonName=\'{5}\', Telephone=\'{6}\', Address=\'{7}\', ZipCode=\'{8}\', Priority={9}, UOAZipCode=\'{10}\', PersonFullName=\'{11}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.PersonType) == 0 else PersonTypeType(ord(self.PersonType)).name, '' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), str(self.PersonName, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), self.Priority, str(self.UOAZipCode, 'GB2312'), str(self.PersonFullName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'PersonType':'' if ord(self.PersonType) == 0 else PersonTypeType(ord(self.PersonType)).name,'IdentifiedCardType':'' if ord(self.IdentifiedCardType) == 0 else IdCardTypeType(ord(self.IdentifiedCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'PersonName':str(self.PersonName, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Priority':self.Priority,'UOAZipCode':str(self.UOAZipCode, 'GB2312'),'PersonFullName':str(self.PersonFullName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcLinkManField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.PersonType=self.PersonType
		obj.IdentifiedCardType=self.IdentifiedCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.PersonName=self.PersonName
		obj.Telephone=self.Telephone
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Priority=self.Priority
		obj.UOAZipCode=self.UOAZipCode
		obj.PersonFullName=self.PersonFullName
		return obj

class CThostFtdcQryBrokerUserEventField(Structure):
	"""查询经纪公司用户事件"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户事件类型
		("UserEventType",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserEventType(self):
		return UserEventTypeType(ord(self.UserEventType))

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserEventType=UserEventTypeType.{2}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.UserEventType) == 0 else UserEventTypeType(ord(self.UserEventType)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserEventType':'' if ord(self.UserEventType) == 0 else UserEventTypeType(ord(self.UserEventType)).name}

	def clone(self):
		obj=CThostFtdcQryBrokerUserEventField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserEventType=self.UserEventType
		return obj

class CThostFtdcBrokerUserEventField(Structure):
	"""查询经纪公司用户事件"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#用户事件类型
		("UserEventType",c_char),
		#用户事件序号
		("EventSequenceNo",c_int32),
		#事件发生日期
		("EventDate",c_char*9),
		#事件发生时间
		("EventTime",c_char*9),
		#用户事件信息
		("UserEventInfo",c_char*1025),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getUserEventType(self):
		return UserEventTypeType(ord(self.UserEventType))
	def getEventSequenceNo(self):
		return self.EventSequenceNo
	def getEventDate(self):
		return str(self.EventDate, 'GB2312')
	def getEventTime(self):
		return str(self.EventTime, 'GB2312')
	def getUserEventInfo(self):
		return str(self.UserEventInfo, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', UserEventType=UserEventTypeType.{2}, EventSequenceNo={3}, EventDate=\'{4}\', EventTime=\'{5}\', UserEventInfo=\'{6}\', InvestorID=\'{7}\', InstrumentID=\'{8}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.UserEventType) == 0 else UserEventTypeType(ord(self.UserEventType)).name, self.EventSequenceNo, str(self.EventDate, 'GB2312'), str(self.EventTime, 'GB2312'), str(self.UserEventInfo, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'UserEventType':'' if ord(self.UserEventType) == 0 else UserEventTypeType(ord(self.UserEventType)).name,'EventSequenceNo':self.EventSequenceNo,'EventDate':str(self.EventDate, 'GB2312'),'EventTime':str(self.EventTime, 'GB2312'),'UserEventInfo':str(self.UserEventInfo, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcBrokerUserEventField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.UserEventType=self.UserEventType
		obj.EventSequenceNo=self.EventSequenceNo
		obj.EventDate=self.EventDate
		obj.EventTime=self.EventTime
		obj.UserEventInfo=self.UserEventInfo
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryContractBankField(Structure):
	"""查询签约银行请求"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', BankID=\'{1}\', BankBrchID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryContractBankField()
		obj.BrokerID=self.BrokerID
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		return obj

class CThostFtdcContractBankField(Structure):
	"""查询签约银行响应"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#银行代码
		("BankID",c_char*4),
		#银行分中心代码
		("BankBrchID",c_char*5),
		#银行名称
		("BankName",c_char*101),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBrchID(self):
		return str(self.BankBrchID, 'GB2312')
	def getBankName(self):
		return str(self.BankName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', BankID=\'{1}\', BankBrchID=\'{2}\', BankName=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBrchID, 'GB2312'), str(self.BankName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBrchID':str(self.BankBrchID, 'GB2312'),'BankName':str(self.BankName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcContractBankField()
		obj.BrokerID=self.BrokerID
		obj.BankID=self.BankID
		obj.BankBrchID=self.BankBrchID
		obj.BankName=self.BankName
		return obj

class CThostFtdcInvestorPositionCombineDetailField(Structure):
	"""投资者组合持仓明细"""
	_fields_ = [
		#交易日
		("TradingDay",c_char*9),
		#开仓日期
		("OpenDate",c_char*9),
		#交易所代码
		("ExchangeID",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#组合编号
		("ComTradeID",c_char*21),
		#撮合编号
		("TradeID",c_char*21),
		#合约代码
		("InstrumentID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		#买卖
		("Direction",c_char),
		#持仓量
		("TotalAmt",c_int32),
		#投资者保证金
		("Margin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#保证金率
		("MarginRateByMoney",c_double),
		#保证金率(按手数)
		("MarginRateByVolume",c_double),
		#单腿编号
		("LegID",c_int32),
		#单腿乘数
		("LegMultiple",c_int32),
		#组合持仓合约编码
		("CombInstrumentID",c_char*31),
		#成交组号
		("TradeGroupID",c_int32),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getOpenDate(self):
		return str(self.OpenDate, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getComTradeID(self):
		return str(self.ComTradeID, 'GB2312')
	def getTradeID(self):
		return str(self.TradeID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getTotalAmt(self):
		return self.TotalAmt
	def getMargin(self):
		return self.Margin
	def getExchMargin(self):
		return self.ExchMargin
	def getMarginRateByMoney(self):
		return self.MarginRateByMoney
	def getMarginRateByVolume(self):
		return self.MarginRateByVolume
	def getLegID(self):
		return self.LegID
	def getLegMultiple(self):
		return self.LegMultiple
	def getCombInstrumentID(self):
		return str(self.CombInstrumentID, 'GB2312')
	def getTradeGroupID(self):
		return self.TradeGroupID

	def __str__(self):
		return 'TradingDay=\'{0}\', OpenDate=\'{1}\', ExchangeID=\'{2}\', SettlementID={3}, BrokerID=\'{4}\', InvestorID=\'{5}\', ComTradeID=\'{6}\', TradeID=\'{7}\', InstrumentID=\'{8}\', HedgeFlag=HedgeFlagType.{9}, Direction=DirectionType.{10}, TotalAmt={11}, Margin={12}, ExchMargin={13}, MarginRateByMoney={14}, MarginRateByVolume={15}, LegID={16}, LegMultiple={17}, CombInstrumentID=\'{18}\', TradeGroupID={19}'.format(str(self.TradingDay, 'GB2312'), str(self.OpenDate, 'GB2312'), str(self.ExchangeID, 'GB2312'), self.SettlementID, str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ComTradeID, 'GB2312'), str(self.TradeID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, self.TotalAmt, self.Margin, self.ExchMargin, self.MarginRateByMoney, self.MarginRateByVolume, self.LegID, self.LegMultiple, str(self.CombInstrumentID, 'GB2312'), self.TradeGroupID)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'OpenDate':str(self.OpenDate, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'SettlementID':self.SettlementID,'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ComTradeID':str(self.ComTradeID, 'GB2312'),'TradeID':str(self.TradeID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'TotalAmt':self.TotalAmt,'Margin':self.Margin,'ExchMargin':self.ExchMargin,'MarginRateByMoney':self.MarginRateByMoney,'MarginRateByVolume':self.MarginRateByVolume,'LegID':self.LegID,'LegMultiple':self.LegMultiple,'CombInstrumentID':str(self.CombInstrumentID, 'GB2312'),'TradeGroupID':self.TradeGroupID}

	def clone(self):
		obj=CThostFtdcInvestorPositionCombineDetailField()
		obj.TradingDay=self.TradingDay
		obj.OpenDate=self.OpenDate
		obj.ExchangeID=self.ExchangeID
		obj.SettlementID=self.SettlementID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ComTradeID=self.ComTradeID
		obj.TradeID=self.TradeID
		obj.InstrumentID=self.InstrumentID
		obj.HedgeFlag=self.HedgeFlag
		obj.Direction=self.Direction
		obj.TotalAmt=self.TotalAmt
		obj.Margin=self.Margin
		obj.ExchMargin=self.ExchMargin
		obj.MarginRateByMoney=self.MarginRateByMoney
		obj.MarginRateByVolume=self.MarginRateByVolume
		obj.LegID=self.LegID
		obj.LegMultiple=self.LegMultiple
		obj.CombInstrumentID=self.CombInstrumentID
		obj.TradeGroupID=self.TradeGroupID
		return obj

class CThostFtdcParkedOrderField(Structure):
	"""预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#预埋报单编号
		("ParkedOrderID",c_char*13),
		#用户类型
		("UserType",c_char),
		#预埋单状态
		("Status",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#交易编码
		("ClientID",c_char*11),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParkedOrderID(self):
		return str(self.ParkedOrderID, 'GB2312')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getStatus(self):
		return ParkedOrderStatusType(ord(self.Status))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', OrderPriceType=OrderPriceTypeType.{5}, Direction=DirectionType.{6}, CombOffsetFlag=\'{7}\', CombHedgeFlag=\'{8}\', LimitPrice={9}, VolumeTotalOriginal={10}, TimeCondition=TimeConditionType.{11}, GTDDate=\'{12}\', VolumeCondition=VolumeConditionType.{13}, MinVolume={14}, ContingentCondition=ContingentConditionType.{15}, StopPrice={16}, ForceCloseReason=ForceCloseReasonType.{17}, IsAutoSuspend={18}, BusinessUnit=\'{19}\', RequestID={20}, UserForceClose={21}, ExchangeID=\'{22}\', ParkedOrderID=\'{23}\', UserType=UserTypeType.{24}, Status=ParkedOrderStatusType.{25}, ErrorID={26}, ErrorMsg=\'{27}\', IsSwapOrder={28}, AccountID=\'{29}\', CurrencyID=\'{30}\', ClientID=\'{31}\', InvestUnitID=\'{32}\', IPAddress=\'{33}\', MacAddress=\'{34}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, self.UserForceClose, str(self.ExchangeID, 'GB2312'), str(self.ParkedOrderID, 'GB2312'), '' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name, '' if ord(self.Status) == 0 else ParkedOrderStatusType(ord(self.Status)).name, self.ErrorID, str(self.ErrorMsg, 'GB2312'), self.IsSwapOrder, str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'UserForceClose':self.UserForceClose,'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParkedOrderID':str(self.ParkedOrderID, 'GB2312'),'UserType':'' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name,'Status':'' if ord(self.Status) == 0 else ParkedOrderStatusType(ord(self.Status)).name,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'IsSwapOrder':self.IsSwapOrder,'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcParkedOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.UserForceClose=self.UserForceClose
		obj.ExchangeID=self.ExchangeID
		obj.ParkedOrderID=self.ParkedOrderID
		obj.UserType=self.UserType
		obj.Status=self.Status
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.IsSwapOrder=self.IsSwapOrder
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.ClientID=self.ClientID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcParkedOrderActionField(Structure):
	"""输入预埋单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#用户代码
		("UserID",c_char*16),
		#合约代码
		("InstrumentID",c_char*31),
		#预埋撤单单编号
		("ParkedOrderActionID",c_char*13),
		#用户类型
		("UserType",c_char),
		#预埋撤单状态
		("Status",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getParkedOrderActionID(self):
		return str(self.ParkedOrderActionID, 'GB2312')
	def getUserType(self):
		return UserTypeType(ord(self.UserType))
	def getStatus(self):
		return ParkedOrderStatusType(ord(self.Status))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, OrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', OrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, LimitPrice={10}, VolumeChange={11}, UserID=\'{12}\', InstrumentID=\'{13}\', ParkedOrderActionID=\'{14}\', UserType=UserTypeType.{15}, Status=ParkedOrderStatusType.{16}, ErrorID={17}, ErrorMsg=\'{18}\', InvestUnitID=\'{19}\', IPAddress=\'{20}\', MacAddress=\'{21}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, str(self.OrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, self.LimitPrice, self.VolumeChange, str(self.UserID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ParkedOrderActionID, 'GB2312'), '' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name, '' if ord(self.Status) == 0 else ParkedOrderStatusType(ord(self.Status)).name, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'OrderRef':str(self.OrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'LimitPrice':self.LimitPrice,'VolumeChange':self.VolumeChange,'UserID':str(self.UserID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ParkedOrderActionID':str(self.ParkedOrderActionID, 'GB2312'),'UserType':'' if ord(self.UserType) == 0 else UserTypeType(ord(self.UserType)).name,'Status':'' if ord(self.Status) == 0 else ParkedOrderStatusType(ord(self.Status)).name,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcParkedOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.OrderRef=self.OrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeChange=self.VolumeChange
		obj.UserID=self.UserID
		obj.InstrumentID=self.InstrumentID
		obj.ParkedOrderActionID=self.ParkedOrderActionID
		obj.UserType=self.UserType
		obj.Status=self.Status
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryParkedOrderField(Structure):
	"""查询预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryParkedOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcQryParkedOrderActionField(Structure):
	"""查询预埋撤单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', ExchangeID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryParkedOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcRemoveParkedOrderField(Structure):
	"""删除预埋单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#预埋报单编号
		("ParkedOrderID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getParkedOrderID(self):
		return str(self.ParkedOrderID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ParkedOrderID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ParkedOrderID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ParkedOrderID':str(self.ParkedOrderID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRemoveParkedOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ParkedOrderID=self.ParkedOrderID
		return obj

class CThostFtdcRemoveParkedOrderActionField(Structure):
	"""删除预埋撤单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#预埋撤单编号
		("ParkedOrderActionID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getParkedOrderActionID(self):
		return str(self.ParkedOrderActionID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ParkedOrderActionID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ParkedOrderActionID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ParkedOrderActionID':str(self.ParkedOrderActionID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRemoveParkedOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ParkedOrderActionID=self.ParkedOrderActionID
		return obj

class CThostFtdcInvestorWithdrawAlgorithmField(Structure):
	"""经纪公司可提资金算法表"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#可提资金比例
		("UsingRatio",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		#货币质押比率
		("FundMortgageRatio",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getUsingRatio(self):
		return self.UsingRatio
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getFundMortgageRatio(self):
		return self.FundMortgageRatio

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorRange=InvestorRangeType.{1}, InvestorID=\'{2}\', UsingRatio={3}, CurrencyID=\'{4}\', FundMortgageRatio={5}'.format(str(self.BrokerID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.InvestorID, 'GB2312'), self.UsingRatio, str(self.CurrencyID, 'GB2312'), self.FundMortgageRatio)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'InvestorID':str(self.InvestorID, 'GB2312'),'UsingRatio':self.UsingRatio,'CurrencyID':str(self.CurrencyID, 'GB2312'),'FundMortgageRatio':self.FundMortgageRatio}

	def clone(self):
		obj=CThostFtdcInvestorWithdrawAlgorithmField()
		obj.BrokerID=self.BrokerID
		obj.InvestorRange=self.InvestorRange
		obj.InvestorID=self.InvestorID
		obj.UsingRatio=self.UsingRatio
		obj.CurrencyID=self.CurrencyID
		obj.FundMortgageRatio=self.FundMortgageRatio
		return obj

class CThostFtdcQryInvestorPositionCombineDetailField(Structure):
	"""查询组合持仓明细"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#组合持仓合约编码
		("CombInstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getCombInstrumentID(self):
		return str(self.CombInstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', CombInstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.CombInstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'CombInstrumentID':str(self.CombInstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryInvestorPositionCombineDetailField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.CombInstrumentID=self.CombInstrumentID
		return obj

class CThostFtdcMarketDataAveragePriceField(Structure):
	"""成交均价"""
	_fields_ = [
		#当日均价
		("AveragePrice",c_double),
		]

	def getAveragePrice(self):
		return self.AveragePrice

	def __str__(self):
		return 'AveragePrice={0}'.format(self.AveragePrice)

	@property
	def __dict__(self):
		return {'AveragePrice':self.AveragePrice}

	def clone(self):
		obj=CThostFtdcMarketDataAveragePriceField()
		obj.AveragePrice=self.AveragePrice
		return obj

class CThostFtdcVerifyInvestorPasswordField(Structure):
	"""校验投资者密码"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#密码
		("Password",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', Password=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.Password, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Password':str(self.Password, 'GB2312')}

	def clone(self):
		obj=CThostFtdcVerifyInvestorPasswordField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Password=self.Password
		return obj

class CThostFtdcUserIPField(Structure):
	"""用户IP"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#IP地址
		("IPAddress",c_char*16),
		#IP地址掩码
		("IPMask",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getIPMask(self):
		return str(self.IPMask, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', IPAddress=\'{2}\', IPMask=\'{3}\', MacAddress=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.IPMask, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'IPMask':str(self.IPMask, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcUserIPField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.IPAddress=self.IPAddress
		obj.IPMask=self.IPMask
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcTradingNoticeInfoField(Structure):
	"""用户事件通知信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#发送时间
		("SendTime",c_char*9),
		#消息正文
		("FieldContent",c_char*501),
		#序列系列号
		("SequenceSeries",c_int32),
		#序列号
		("SequenceNo",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getSendTime(self):
		return str(self.SendTime, 'GB2312')
	def getFieldContent(self):
		return str(self.FieldContent, 'GB2312')
	def getSequenceSeries(self):
		return self.SequenceSeries
	def getSequenceNo(self):
		return self.SequenceNo

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', SendTime=\'{2}\', FieldContent=\'{3}\', SequenceSeries={4}, SequenceNo={5}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.SendTime, 'GB2312'), str(self.FieldContent, 'GB2312'), self.SequenceSeries, self.SequenceNo)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'SendTime':str(self.SendTime, 'GB2312'),'FieldContent':str(self.FieldContent, 'GB2312'),'SequenceSeries':self.SequenceSeries,'SequenceNo':self.SequenceNo}

	def clone(self):
		obj=CThostFtdcTradingNoticeInfoField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.SendTime=self.SendTime
		obj.FieldContent=self.FieldContent
		obj.SequenceSeries=self.SequenceSeries
		obj.SequenceNo=self.SequenceNo
		return obj

class CThostFtdcTradingNoticeField(Structure):
	"""用户事件通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者范围
		("InvestorRange",c_char),
		#投资者代码
		("InvestorID",c_char*13),
		#序列系列号
		("SequenceSeries",c_int32),
		#用户代码
		("UserID",c_char*16),
		#发送时间
		("SendTime",c_char*9),
		#序列号
		("SequenceNo",c_int32),
		#消息正文
		("FieldContent",c_char*501),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorRange(self):
		return InvestorRangeType(ord(self.InvestorRange))
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getSequenceSeries(self):
		return self.SequenceSeries
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getSendTime(self):
		return str(self.SendTime, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFieldContent(self):
		return str(self.FieldContent, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorRange=InvestorRangeType.{1}, InvestorID=\'{2}\', SequenceSeries={3}, UserID=\'{4}\', SendTime=\'{5}\', SequenceNo={6}, FieldContent=\'{7}\''.format(str(self.BrokerID, 'GB2312'), '' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name, str(self.InvestorID, 'GB2312'), self.SequenceSeries, str(self.UserID, 'GB2312'), str(self.SendTime, 'GB2312'), self.SequenceNo, str(self.FieldContent, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorRange':'' if ord(self.InvestorRange) == 0 else InvestorRangeType(ord(self.InvestorRange)).name,'InvestorID':str(self.InvestorID, 'GB2312'),'SequenceSeries':self.SequenceSeries,'UserID':str(self.UserID, 'GB2312'),'SendTime':str(self.SendTime, 'GB2312'),'SequenceNo':self.SequenceNo,'FieldContent':str(self.FieldContent, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTradingNoticeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorRange=self.InvestorRange
		obj.InvestorID=self.InvestorID
		obj.SequenceSeries=self.SequenceSeries
		obj.UserID=self.UserID
		obj.SendTime=self.SendTime
		obj.SequenceNo=self.SequenceNo
		obj.FieldContent=self.FieldContent
		return obj

class CThostFtdcQryTradingNoticeField(Structure):
	"""查询交易事件通知"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTradingNoticeField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcQryErrOrderField(Structure):
	"""查询错误报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryErrOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcErrOrderField(Structure):
	"""错误报单"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#用户强评标志
		("UserForceClose",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#交易编码
		("ClientID",c_char*11),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getUserForceClose(self):
		return self.UserForceClose
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', OrderPriceType=OrderPriceTypeType.{5}, Direction=DirectionType.{6}, CombOffsetFlag=\'{7}\', CombHedgeFlag=\'{8}\', LimitPrice={9}, VolumeTotalOriginal={10}, TimeCondition=TimeConditionType.{11}, GTDDate=\'{12}\', VolumeCondition=VolumeConditionType.{13}, MinVolume={14}, ContingentCondition=ContingentConditionType.{15}, StopPrice={16}, ForceCloseReason=ForceCloseReasonType.{17}, IsAutoSuspend={18}, BusinessUnit=\'{19}\', RequestID={20}, UserForceClose={21}, ErrorID={22}, ErrorMsg=\'{23}\', IsSwapOrder={24}, ExchangeID=\'{25}\', InvestUnitID=\'{26}\', AccountID=\'{27}\', CurrencyID=\'{28}\', ClientID=\'{29}\', IPAddress=\'{30}\', MacAddress=\'{31}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, self.UserForceClose, self.ErrorID, str(self.ErrorMsg, 'GB2312'), self.IsSwapOrder, str(self.ExchangeID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'UserForceClose':self.UserForceClose,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'IsSwapOrder':self.IsSwapOrder,'ExchangeID':str(self.ExchangeID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcErrOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.UserForceClose=self.UserForceClose
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.IsSwapOrder=self.IsSwapOrder
		obj.ExchangeID=self.ExchangeID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.ClientID=self.ClientID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcErrorConditionalOrderField(Structure):
	"""查询错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#报单引用
		("OrderRef",c_char*13),
		#用户代码
		("UserID",c_char*16),
		#报单价格条件
		("OrderPriceType",c_char),
		#买卖方向
		("Direction",c_char),
		#组合开平标志
		("CombOffsetFlag",c_char*5),
		#组合投机套保标志
		("CombHedgeFlag",c_char*5),
		#价格
		("LimitPrice",c_double),
		#数量
		("VolumeTotalOriginal",c_int32),
		#有效期类型
		("TimeCondition",c_char),
		#GTD日期
		("GTDDate",c_char*9),
		#成交量类型
		("VolumeCondition",c_char),
		#最小成交量
		("MinVolume",c_int32),
		#触发条件
		("ContingentCondition",c_char),
		#止损价
		("StopPrice",c_double),
		#强平原因
		("ForceCloseReason",c_char),
		#自动挂起标志
		("IsAutoSuspend",c_int32),
		#业务单元
		("BusinessUnit",c_char*21),
		#请求编号
		("RequestID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#合约在交易所的代码
		("ExchangeInstID",c_char*31),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#报单提交状态
		("OrderSubmitStatus",c_char),
		#报单提示序号
		("NotifySequence",c_int32),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#报单编号
		("OrderSysID",c_char*21),
		#报单来源
		("OrderSource",c_char),
		#报单状态
		("OrderStatus",c_char),
		#报单类型
		("OrderType",c_char),
		#今成交数量
		("VolumeTraded",c_int32),
		#剩余数量
		("VolumeTotal",c_int32),
		#报单日期
		("InsertDate",c_char*9),
		#委托时间
		("InsertTime",c_char*9),
		#激活时间
		("ActiveTime",c_char*9),
		#挂起时间
		("SuspendTime",c_char*9),
		#最后修改时间
		("UpdateTime",c_char*9),
		#撤销时间
		("CancelTime",c_char*9),
		#最后修改交易所交易员代码
		("ActiveTraderID",c_char*21),
		#结算会员编号
		("ClearingPartID",c_char*11),
		#序号
		("SequenceNo",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#用户端产品信息
		("UserProductInfo",c_char*11),
		#状态信息
		("StatusMsg",c_char*81),
		#用户强评标志
		("UserForceClose",c_int32),
		#操作用户代码
		("ActiveUserID",c_char*16),
		#经纪公司报单编号
		("BrokerOrderSeq",c_int32),
		#相关报单
		("RelativeOrderSysID",c_char*21),
		#郑商所成交数量
		("ZCETotalTradedVolume",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#互换单标志
		("IsSwapOrder",c_int32),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#资金账号
		("AccountID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOrderPriceType(self):
		return OrderPriceTypeType(ord(self.OrderPriceType))
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getCombOffsetFlag(self):
		return str(self.CombOffsetFlag, 'GB2312')
	def getCombHedgeFlag(self):
		return str(self.CombHedgeFlag, 'GB2312')
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeTotalOriginal(self):
		return self.VolumeTotalOriginal
	def getTimeCondition(self):
		return TimeConditionType(ord(self.TimeCondition))
	def getGTDDate(self):
		return str(self.GTDDate, 'GB2312')
	def getVolumeCondition(self):
		return VolumeConditionType(ord(self.VolumeCondition))
	def getMinVolume(self):
		return self.MinVolume
	def getContingentCondition(self):
		return ContingentConditionType(ord(self.ContingentCondition))
	def getStopPrice(self):
		return self.StopPrice
	def getForceCloseReason(self):
		return ForceCloseReasonType(ord(self.ForceCloseReason))
	def getIsAutoSuspend(self):
		return self.IsAutoSuspend
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getExchangeInstID(self):
		return str(self.ExchangeInstID, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderSubmitStatus(self):
		return OrderSubmitStatusType(ord(self.OrderSubmitStatus))
	def getNotifySequence(self):
		return self.NotifySequence
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getOrderSource(self):
		return OrderSourceType(ord(self.OrderSource))
	def getOrderStatus(self):
		return OrderStatusType(ord(self.OrderStatus))
	def getOrderType(self):
		return OrderTypeType(ord(self.OrderType))
	def getVolumeTraded(self):
		return self.VolumeTraded
	def getVolumeTotal(self):
		return self.VolumeTotal
	def getInsertDate(self):
		return str(self.InsertDate, 'GB2312')
	def getInsertTime(self):
		return str(self.InsertTime, 'GB2312')
	def getActiveTime(self):
		return str(self.ActiveTime, 'GB2312')
	def getSuspendTime(self):
		return str(self.SuspendTime, 'GB2312')
	def getUpdateTime(self):
		return str(self.UpdateTime, 'GB2312')
	def getCancelTime(self):
		return str(self.CancelTime, 'GB2312')
	def getActiveTraderID(self):
		return str(self.ActiveTraderID, 'GB2312')
	def getClearingPartID(self):
		return str(self.ClearingPartID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getUserProductInfo(self):
		return str(self.UserProductInfo, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getUserForceClose(self):
		return self.UserForceClose
	def getActiveUserID(self):
		return str(self.ActiveUserID, 'GB2312')
	def getBrokerOrderSeq(self):
		return self.BrokerOrderSeq
	def getRelativeOrderSysID(self):
		return str(self.RelativeOrderSysID, 'GB2312')
	def getZCETotalTradedVolume(self):
		return self.ZCETotalTradedVolume
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getIsSwapOrder(self):
		return self.IsSwapOrder
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', OrderRef=\'{3}\', UserID=\'{4}\', OrderPriceType=OrderPriceTypeType.{5}, Direction=DirectionType.{6}, CombOffsetFlag=\'{7}\', CombHedgeFlag=\'{8}\', LimitPrice={9}, VolumeTotalOriginal={10}, TimeCondition=TimeConditionType.{11}, GTDDate=\'{12}\', VolumeCondition=VolumeConditionType.{13}, MinVolume={14}, ContingentCondition=ContingentConditionType.{15}, StopPrice={16}, ForceCloseReason=ForceCloseReasonType.{17}, IsAutoSuspend={18}, BusinessUnit=\'{19}\', RequestID={20}, OrderLocalID=\'{21}\', ExchangeID=\'{22}\', ParticipantID=\'{23}\', ClientID=\'{24}\', ExchangeInstID=\'{25}\', TraderID=\'{26}\', InstallID={27}, OrderSubmitStatus=OrderSubmitStatusType.{28}, NotifySequence={29}, TradingDay=\'{30}\', SettlementID={31}, OrderSysID=\'{32}\', OrderSource=OrderSourceType.{33}, OrderStatus=OrderStatusType.{34}, OrderType=OrderTypeType.{35}, VolumeTraded={36}, VolumeTotal={37}, InsertDate=\'{38}\', InsertTime=\'{39}\', ActiveTime=\'{40}\', SuspendTime=\'{41}\', UpdateTime=\'{42}\', CancelTime=\'{43}\', ActiveTraderID=\'{44}\', ClearingPartID=\'{45}\', SequenceNo={46}, FrontID={47}, SessionID={48}, UserProductInfo=\'{49}\', StatusMsg=\'{50}\', UserForceClose={51}, ActiveUserID=\'{52}\', BrokerOrderSeq={53}, RelativeOrderSysID=\'{54}\', ZCETotalTradedVolume={55}, ErrorID={56}, ErrorMsg=\'{57}\', IsSwapOrder={58}, BranchID=\'{59}\', InvestUnitID=\'{60}\', AccountID=\'{61}\', CurrencyID=\'{62}\', IPAddress=\'{63}\', MacAddress=\'{64}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.OrderRef, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name, '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, str(self.CombOffsetFlag, 'GB2312'), str(self.CombHedgeFlag, 'GB2312'), self.LimitPrice, self.VolumeTotalOriginal, '' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name, str(self.GTDDate, 'GB2312'), '' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name, self.MinVolume, '' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name, self.StopPrice, '' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name, self.IsAutoSuspend, str(self.BusinessUnit, 'GB2312'), self.RequestID, str(self.OrderLocalID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.ExchangeInstID, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, '' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name, self.NotifySequence, str(self.TradingDay, 'GB2312'), self.SettlementID, str(self.OrderSysID, 'GB2312'), '' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name, '' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name, '' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name, self.VolumeTraded, self.VolumeTotal, str(self.InsertDate, 'GB2312'), str(self.InsertTime, 'GB2312'), str(self.ActiveTime, 'GB2312'), str(self.SuspendTime, 'GB2312'), str(self.UpdateTime, 'GB2312'), str(self.CancelTime, 'GB2312'), str(self.ActiveTraderID, 'GB2312'), str(self.ClearingPartID, 'GB2312'), self.SequenceNo, self.FrontID, self.SessionID, str(self.UserProductInfo, 'GB2312'), str(self.StatusMsg, 'GB2312'), self.UserForceClose, str(self.ActiveUserID, 'GB2312'), self.BrokerOrderSeq, str(self.RelativeOrderSysID, 'GB2312'), self.ZCETotalTradedVolume, self.ErrorID, str(self.ErrorMsg, 'GB2312'), self.IsSwapOrder, str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'OrderRef':str(self.OrderRef, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OrderPriceType':'' if ord(self.OrderPriceType) == 0 else OrderPriceTypeType(ord(self.OrderPriceType)).name,'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'CombOffsetFlag':str(self.CombOffsetFlag, 'GB2312'),'CombHedgeFlag':str(self.CombHedgeFlag, 'GB2312'),'LimitPrice':self.LimitPrice,'VolumeTotalOriginal':self.VolumeTotalOriginal,'TimeCondition':'' if ord(self.TimeCondition) == 0 else TimeConditionType(ord(self.TimeCondition)).name,'GTDDate':str(self.GTDDate, 'GB2312'),'VolumeCondition':'' if ord(self.VolumeCondition) == 0 else VolumeConditionType(ord(self.VolumeCondition)).name,'MinVolume':self.MinVolume,'ContingentCondition':'' if ord(self.ContingentCondition) == 0 else ContingentConditionType(ord(self.ContingentCondition)).name,'StopPrice':self.StopPrice,'ForceCloseReason':'' if ord(self.ForceCloseReason) == 0 else ForceCloseReasonType(ord(self.ForceCloseReason)).name,'IsAutoSuspend':self.IsAutoSuspend,'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'RequestID':self.RequestID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'ExchangeInstID':str(self.ExchangeInstID, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderSubmitStatus':'' if ord(self.OrderSubmitStatus) == 0 else OrderSubmitStatusType(ord(self.OrderSubmitStatus)).name,'NotifySequence':self.NotifySequence,'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'OrderSysID':str(self.OrderSysID, 'GB2312'),'OrderSource':'' if ord(self.OrderSource) == 0 else OrderSourceType(ord(self.OrderSource)).name,'OrderStatus':'' if ord(self.OrderStatus) == 0 else OrderStatusType(ord(self.OrderStatus)).name,'OrderType':'' if ord(self.OrderType) == 0 else OrderTypeType(ord(self.OrderType)).name,'VolumeTraded':self.VolumeTraded,'VolumeTotal':self.VolumeTotal,'InsertDate':str(self.InsertDate, 'GB2312'),'InsertTime':str(self.InsertTime, 'GB2312'),'ActiveTime':str(self.ActiveTime, 'GB2312'),'SuspendTime':str(self.SuspendTime, 'GB2312'),'UpdateTime':str(self.UpdateTime, 'GB2312'),'CancelTime':str(self.CancelTime, 'GB2312'),'ActiveTraderID':str(self.ActiveTraderID, 'GB2312'),'ClearingPartID':str(self.ClearingPartID, 'GB2312'),'SequenceNo':self.SequenceNo,'FrontID':self.FrontID,'SessionID':self.SessionID,'UserProductInfo':str(self.UserProductInfo, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'UserForceClose':self.UserForceClose,'ActiveUserID':str(self.ActiveUserID, 'GB2312'),'BrokerOrderSeq':self.BrokerOrderSeq,'RelativeOrderSysID':str(self.RelativeOrderSysID, 'GB2312'),'ZCETotalTradedVolume':self.ZCETotalTradedVolume,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'IsSwapOrder':self.IsSwapOrder,'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcErrorConditionalOrderField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.OrderRef=self.OrderRef
		obj.UserID=self.UserID
		obj.OrderPriceType=self.OrderPriceType
		obj.Direction=self.Direction
		obj.CombOffsetFlag=self.CombOffsetFlag
		obj.CombHedgeFlag=self.CombHedgeFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeTotalOriginal=self.VolumeTotalOriginal
		obj.TimeCondition=self.TimeCondition
		obj.GTDDate=self.GTDDate
		obj.VolumeCondition=self.VolumeCondition
		obj.MinVolume=self.MinVolume
		obj.ContingentCondition=self.ContingentCondition
		obj.StopPrice=self.StopPrice
		obj.ForceCloseReason=self.ForceCloseReason
		obj.IsAutoSuspend=self.IsAutoSuspend
		obj.BusinessUnit=self.BusinessUnit
		obj.RequestID=self.RequestID
		obj.OrderLocalID=self.OrderLocalID
		obj.ExchangeID=self.ExchangeID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.ExchangeInstID=self.ExchangeInstID
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderSubmitStatus=self.OrderSubmitStatus
		obj.NotifySequence=self.NotifySequence
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.OrderSysID=self.OrderSysID
		obj.OrderSource=self.OrderSource
		obj.OrderStatus=self.OrderStatus
		obj.OrderType=self.OrderType
		obj.VolumeTraded=self.VolumeTraded
		obj.VolumeTotal=self.VolumeTotal
		obj.InsertDate=self.InsertDate
		obj.InsertTime=self.InsertTime
		obj.ActiveTime=self.ActiveTime
		obj.SuspendTime=self.SuspendTime
		obj.UpdateTime=self.UpdateTime
		obj.CancelTime=self.CancelTime
		obj.ActiveTraderID=self.ActiveTraderID
		obj.ClearingPartID=self.ClearingPartID
		obj.SequenceNo=self.SequenceNo
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.UserProductInfo=self.UserProductInfo
		obj.StatusMsg=self.StatusMsg
		obj.UserForceClose=self.UserForceClose
		obj.ActiveUserID=self.ActiveUserID
		obj.BrokerOrderSeq=self.BrokerOrderSeq
		obj.RelativeOrderSysID=self.RelativeOrderSysID
		obj.ZCETotalTradedVolume=self.ZCETotalTradedVolume
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.IsSwapOrder=self.IsSwapOrder
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		return obj

class CThostFtdcQryErrOrderActionField(Structure):
	"""查询错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryErrOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcErrOrderActionField(Structure):
	"""错误报单操作"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#报单操作引用
		("OrderActionRef",c_int32),
		#报单引用
		("OrderRef",c_char*13),
		#请求编号
		("RequestID",c_int32),
		#前置编号
		("FrontID",c_int32),
		#会话编号
		("SessionID",c_int32),
		#交易所代码
		("ExchangeID",c_char*9),
		#报单编号
		("OrderSysID",c_char*21),
		#操作标志
		("ActionFlag",c_char),
		#价格
		("LimitPrice",c_double),
		#数量变化
		("VolumeChange",c_int32),
		#操作日期
		("ActionDate",c_char*9),
		#操作时间
		("ActionTime",c_char*9),
		#交易所交易员代码
		("TraderID",c_char*21),
		#安装编号
		("InstallID",c_int32),
		#本地报单编号
		("OrderLocalID",c_char*13),
		#操作本地编号
		("ActionLocalID",c_char*13),
		#会员代码
		("ParticipantID",c_char*11),
		#客户代码
		("ClientID",c_char*11),
		#业务单元
		("BusinessUnit",c_char*21),
		#报单操作状态
		("OrderActionStatus",c_char),
		#用户代码
		("UserID",c_char*16),
		#状态信息
		("StatusMsg",c_char*81),
		#合约代码
		("InstrumentID",c_char*31),
		#营业部编号
		("BranchID",c_char*9),
		#投资单元代码
		("InvestUnitID",c_char*17),
		#IP地址
		("IPAddress",c_char*16),
		#Mac地址
		("MacAddress",c_char*21),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getOrderActionRef(self):
		return self.OrderActionRef
	def getOrderRef(self):
		return str(self.OrderRef, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getFrontID(self):
		return self.FrontID
	def getSessionID(self):
		return self.SessionID
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getOrderSysID(self):
		return str(self.OrderSysID, 'GB2312')
	def getActionFlag(self):
		return ActionFlagType(ord(self.ActionFlag))
	def getLimitPrice(self):
		return self.LimitPrice
	def getVolumeChange(self):
		return self.VolumeChange
	def getActionDate(self):
		return str(self.ActionDate, 'GB2312')
	def getActionTime(self):
		return str(self.ActionTime, 'GB2312')
	def getTraderID(self):
		return str(self.TraderID, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getOrderLocalID(self):
		return str(self.OrderLocalID, 'GB2312')
	def getActionLocalID(self):
		return str(self.ActionLocalID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getClientID(self):
		return str(self.ClientID, 'GB2312')
	def getBusinessUnit(self):
		return str(self.BusinessUnit, 'GB2312')
	def getOrderActionStatus(self):
		return OrderActionStatusType(ord(self.OrderActionStatus))
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getStatusMsg(self):
		return str(self.StatusMsg, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getBranchID(self):
		return str(self.BranchID, 'GB2312')
	def getInvestUnitID(self):
		return str(self.InvestUnitID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')
	def getMacAddress(self):
		return str(self.MacAddress, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', OrderActionRef={2}, OrderRef=\'{3}\', RequestID={4}, FrontID={5}, SessionID={6}, ExchangeID=\'{7}\', OrderSysID=\'{8}\', ActionFlag=ActionFlagType.{9}, LimitPrice={10}, VolumeChange={11}, ActionDate=\'{12}\', ActionTime=\'{13}\', TraderID=\'{14}\', InstallID={15}, OrderLocalID=\'{16}\', ActionLocalID=\'{17}\', ParticipantID=\'{18}\', ClientID=\'{19}\', BusinessUnit=\'{20}\', OrderActionStatus=OrderActionStatusType.{21}, UserID=\'{22}\', StatusMsg=\'{23}\', InstrumentID=\'{24}\', BranchID=\'{25}\', InvestUnitID=\'{26}\', IPAddress=\'{27}\', MacAddress=\'{28}\', ErrorID={29}, ErrorMsg=\'{30}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.OrderActionRef, str(self.OrderRef, 'GB2312'), self.RequestID, self.FrontID, self.SessionID, str(self.ExchangeID, 'GB2312'), str(self.OrderSysID, 'GB2312'), '' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name, self.LimitPrice, self.VolumeChange, str(self.ActionDate, 'GB2312'), str(self.ActionTime, 'GB2312'), str(self.TraderID, 'GB2312'), self.InstallID, str(self.OrderLocalID, 'GB2312'), str(self.ActionLocalID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ClientID, 'GB2312'), str(self.BusinessUnit, 'GB2312'), '' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name, str(self.UserID, 'GB2312'), str(self.StatusMsg, 'GB2312'), str(self.InstrumentID, 'GB2312'), str(self.BranchID, 'GB2312'), str(self.InvestUnitID, 'GB2312'), str(self.IPAddress, 'GB2312'), str(self.MacAddress, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'OrderActionRef':self.OrderActionRef,'OrderRef':str(self.OrderRef, 'GB2312'),'RequestID':self.RequestID,'FrontID':self.FrontID,'SessionID':self.SessionID,'ExchangeID':str(self.ExchangeID, 'GB2312'),'OrderSysID':str(self.OrderSysID, 'GB2312'),'ActionFlag':'' if ord(self.ActionFlag) == 0 else ActionFlagType(ord(self.ActionFlag)).name,'LimitPrice':self.LimitPrice,'VolumeChange':self.VolumeChange,'ActionDate':str(self.ActionDate, 'GB2312'),'ActionTime':str(self.ActionTime, 'GB2312'),'TraderID':str(self.TraderID, 'GB2312'),'InstallID':self.InstallID,'OrderLocalID':str(self.OrderLocalID, 'GB2312'),'ActionLocalID':str(self.ActionLocalID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ClientID':str(self.ClientID, 'GB2312'),'BusinessUnit':str(self.BusinessUnit, 'GB2312'),'OrderActionStatus':'' if ord(self.OrderActionStatus) == 0 else OrderActionStatusType(ord(self.OrderActionStatus)).name,'UserID':str(self.UserID, 'GB2312'),'StatusMsg':str(self.StatusMsg, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'BranchID':str(self.BranchID, 'GB2312'),'InvestUnitID':str(self.InvestUnitID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312'),'MacAddress':str(self.MacAddress, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcErrOrderActionField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.OrderActionRef=self.OrderActionRef
		obj.OrderRef=self.OrderRef
		obj.RequestID=self.RequestID
		obj.FrontID=self.FrontID
		obj.SessionID=self.SessionID
		obj.ExchangeID=self.ExchangeID
		obj.OrderSysID=self.OrderSysID
		obj.ActionFlag=self.ActionFlag
		obj.LimitPrice=self.LimitPrice
		obj.VolumeChange=self.VolumeChange
		obj.ActionDate=self.ActionDate
		obj.ActionTime=self.ActionTime
		obj.TraderID=self.TraderID
		obj.InstallID=self.InstallID
		obj.OrderLocalID=self.OrderLocalID
		obj.ActionLocalID=self.ActionLocalID
		obj.ParticipantID=self.ParticipantID
		obj.ClientID=self.ClientID
		obj.BusinessUnit=self.BusinessUnit
		obj.OrderActionStatus=self.OrderActionStatus
		obj.UserID=self.UserID
		obj.StatusMsg=self.StatusMsg
		obj.InstrumentID=self.InstrumentID
		obj.BranchID=self.BranchID
		obj.InvestUnitID=self.InvestUnitID
		obj.IPAddress=self.IPAddress
		obj.MacAddress=self.MacAddress
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcQryExchangeSequenceField(Structure):
	"""查询交易所状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\''.format(str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryExchangeSequenceField()
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcExchangeSequenceField(Structure):
	"""交易所状态"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#序号
		("SequenceNo",c_int32),
		#合约交易状态
		("MarketStatus",c_char),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getSequenceNo(self):
		return self.SequenceNo
	def getMarketStatus(self):
		return InstrumentStatusType(ord(self.MarketStatus))

	def __str__(self):
		return 'ExchangeID=\'{0}\', SequenceNo={1}, MarketStatus=InstrumentStatusType.{2}'.format(str(self.ExchangeID, 'GB2312'), self.SequenceNo, '' if ord(self.MarketStatus) == 0 else InstrumentStatusType(ord(self.MarketStatus)).name)

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'SequenceNo':self.SequenceNo,'MarketStatus':'' if ord(self.MarketStatus) == 0 else InstrumentStatusType(ord(self.MarketStatus)).name}

	def clone(self):
		obj=CThostFtdcExchangeSequenceField()
		obj.ExchangeID=self.ExchangeID
		obj.SequenceNo=self.SequenceNo
		obj.MarketStatus=self.MarketStatus
		return obj

class CThostFtdcQueryMaxOrderVolumeWithPriceField(Structure):
	"""根据价格查询最大报单数量"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#开平标志
		("OffsetFlag",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#最大允许报单数量
		("MaxVolume",c_int32),
		#报单价格
		("Price",c_double),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getOffsetFlag(self):
		return OffsetFlagType(ord(self.OffsetFlag))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getMaxVolume(self):
		return self.MaxVolume
	def getPrice(self):
		return self.Price

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', InstrumentID=\'{2}\', Direction=DirectionType.{3}, OffsetFlag=OffsetFlagType.{4}, HedgeFlag=HedgeFlagType.{5}, MaxVolume={6}, Price={7}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, '' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.MaxVolume, self.Price)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'OffsetFlag':'' if ord(self.OffsetFlag) == 0 else OffsetFlagType(ord(self.OffsetFlag)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'MaxVolume':self.MaxVolume,'Price':self.Price}

	def clone(self):
		obj=CThostFtdcQueryMaxOrderVolumeWithPriceField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.InstrumentID=self.InstrumentID
		obj.Direction=self.Direction
		obj.OffsetFlag=self.OffsetFlag
		obj.HedgeFlag=self.HedgeFlag
		obj.MaxVolume=self.MaxVolume
		obj.Price=self.Price
		return obj

class CThostFtdcQryBrokerTradingParamsField(Structure):
	"""查询经纪公司交易参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', CurrencyID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBrokerTradingParamsField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcBrokerTradingParamsField(Structure):
	"""经纪公司交易参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#保证金价格类型
		("MarginPriceType",c_char),
		#盈亏算法
		("Algorithm",c_char),
		#可用是否包含平仓盈利
		("AvailIncludeCloseProfit",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期权权利金价格类型
		("OptionRoyaltyPriceType",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getMarginPriceType(self):
		return MarginPriceTypeType(ord(self.MarginPriceType))
	def getAlgorithm(self):
		return AlgorithmType(ord(self.Algorithm))
	def getAvailIncludeCloseProfit(self):
		return IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getOptionRoyaltyPriceType(self):
		return OptionRoyaltyPriceTypeType(ord(self.OptionRoyaltyPriceType))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', MarginPriceType=MarginPriceTypeType.{2}, Algorithm=AlgorithmType.{3}, AvailIncludeCloseProfit=IncludeCloseProfitType.{4}, CurrencyID=\'{5}\', OptionRoyaltyPriceType=OptionRoyaltyPriceTypeType.{6}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), '' if ord(self.MarginPriceType) == 0 else MarginPriceTypeType(ord(self.MarginPriceType)).name, '' if ord(self.Algorithm) == 0 else AlgorithmType(ord(self.Algorithm)).name, '' if ord(self.AvailIncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)).name, str(self.CurrencyID, 'GB2312'), '' if ord(self.OptionRoyaltyPriceType) == 0 else OptionRoyaltyPriceTypeType(ord(self.OptionRoyaltyPriceType)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'MarginPriceType':'' if ord(self.MarginPriceType) == 0 else MarginPriceTypeType(ord(self.MarginPriceType)).name,'Algorithm':'' if ord(self.Algorithm) == 0 else AlgorithmType(ord(self.Algorithm)).name,'AvailIncludeCloseProfit':'' if ord(self.AvailIncludeCloseProfit) == 0 else IncludeCloseProfitType(ord(self.AvailIncludeCloseProfit)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'OptionRoyaltyPriceType':'' if ord(self.OptionRoyaltyPriceType) == 0 else OptionRoyaltyPriceTypeType(ord(self.OptionRoyaltyPriceType)).name}

	def clone(self):
		obj=CThostFtdcBrokerTradingParamsField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.MarginPriceType=self.MarginPriceType
		obj.Algorithm=self.Algorithm
		obj.AvailIncludeCloseProfit=self.AvailIncludeCloseProfit
		obj.CurrencyID=self.CurrencyID
		obj.OptionRoyaltyPriceType=self.OptionRoyaltyPriceType
		return obj

class CThostFtdcQryBrokerTradingAlgosField(Structure):
	"""查询经纪公司交易算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', ExchangeID=\'{1}\', InstrumentID=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryBrokerTradingAlgosField()
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcBrokerTradingAlgosField(Structure):
	"""经纪公司交易算法"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#持仓处理算法编号
		("HandlePositionAlgoID",c_char),
		#寻找保证金率算法编号
		("FindMarginRateAlgoID",c_char),
		#资金处理算法编号
		("HandleTradingAccountAlgoID",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getHandlePositionAlgoID(self):
		return HandlePositionAlgoIDType(ord(self.HandlePositionAlgoID))
	def getFindMarginRateAlgoID(self):
		return FindMarginRateAlgoIDType(ord(self.FindMarginRateAlgoID))
	def getHandleTradingAccountAlgoID(self):
		return HandleTradingAccountAlgoIDType(ord(self.HandleTradingAccountAlgoID))

	def __str__(self):
		return 'BrokerID=\'{0}\', ExchangeID=\'{1}\', InstrumentID=\'{2}\', HandlePositionAlgoID=HandlePositionAlgoIDType.{3}, FindMarginRateAlgoID=FindMarginRateAlgoIDType.{4}, HandleTradingAccountAlgoID=HandleTradingAccountAlgoIDType.{5}'.format(str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.HandlePositionAlgoID) == 0 else HandlePositionAlgoIDType(ord(self.HandlePositionAlgoID)).name, '' if ord(self.FindMarginRateAlgoID) == 0 else FindMarginRateAlgoIDType(ord(self.FindMarginRateAlgoID)).name, '' if ord(self.HandleTradingAccountAlgoID) == 0 else HandleTradingAccountAlgoIDType(ord(self.HandleTradingAccountAlgoID)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'HandlePositionAlgoID':'' if ord(self.HandlePositionAlgoID) == 0 else HandlePositionAlgoIDType(ord(self.HandlePositionAlgoID)).name,'FindMarginRateAlgoID':'' if ord(self.FindMarginRateAlgoID) == 0 else FindMarginRateAlgoIDType(ord(self.FindMarginRateAlgoID)).name,'HandleTradingAccountAlgoID':'' if ord(self.HandleTradingAccountAlgoID) == 0 else HandleTradingAccountAlgoIDType(ord(self.HandleTradingAccountAlgoID)).name}

	def clone(self):
		obj=CThostFtdcBrokerTradingAlgosField()
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		obj.InstrumentID=self.InstrumentID
		obj.HandlePositionAlgoID=self.HandlePositionAlgoID
		obj.FindMarginRateAlgoID=self.FindMarginRateAlgoID
		obj.HandleTradingAccountAlgoID=self.HandleTradingAccountAlgoID
		return obj

class CThostFtdcQueryBrokerDepositField(Structure):
	"""查询经纪公司资金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', ExchangeID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQueryBrokerDepositField()
		obj.BrokerID=self.BrokerID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcBrokerDepositField(Structure):
	"""经纪公司资金"""
	_fields_ = [
		#交易日期
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#会员代码
		("ParticipantID",c_char*11),
		#交易所代码
		("ExchangeID",c_char*9),
		#上次结算准备金
		("PreBalance",c_double),
		#当前保证金总额
		("CurrMargin",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#期货结算准备金
		("Balance",c_double),
		#入金金额
		("Deposit",c_double),
		#出金金额
		("Withdraw",c_double),
		#可提资金
		("Available",c_double),
		#基本准备金
		("Reserve",c_double),
		#冻结的保证金
		("FrozenMargin",c_double),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getPreBalance(self):
		return self.PreBalance
	def getCurrMargin(self):
		return self.CurrMargin
	def getCloseProfit(self):
		return self.CloseProfit
	def getBalance(self):
		return self.Balance
	def getDeposit(self):
		return self.Deposit
	def getWithdraw(self):
		return self.Withdraw
	def getAvailable(self):
		return self.Available
	def getReserve(self):
		return self.Reserve
	def getFrozenMargin(self):
		return self.FrozenMargin

	def __str__(self):
		return 'TradingDay=\'{0}\', BrokerID=\'{1}\', ParticipantID=\'{2}\', ExchangeID=\'{3}\', PreBalance={4}, CurrMargin={5}, CloseProfit={6}, Balance={7}, Deposit={8}, Withdraw={9}, Available={10}, Reserve={11}, FrozenMargin={12}'.format(str(self.TradingDay, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.ExchangeID, 'GB2312'), self.PreBalance, self.CurrMargin, self.CloseProfit, self.Balance, self.Deposit, self.Withdraw, self.Available, self.Reserve, self.FrozenMargin)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'PreBalance':self.PreBalance,'CurrMargin':self.CurrMargin,'CloseProfit':self.CloseProfit,'Balance':self.Balance,'Deposit':self.Deposit,'Withdraw':self.Withdraw,'Available':self.Available,'Reserve':self.Reserve,'FrozenMargin':self.FrozenMargin}

	def clone(self):
		obj=CThostFtdcBrokerDepositField()
		obj.TradingDay=self.TradingDay
		obj.BrokerID=self.BrokerID
		obj.ParticipantID=self.ParticipantID
		obj.ExchangeID=self.ExchangeID
		obj.PreBalance=self.PreBalance
		obj.CurrMargin=self.CurrMargin
		obj.CloseProfit=self.CloseProfit
		obj.Balance=self.Balance
		obj.Deposit=self.Deposit
		obj.Withdraw=self.Withdraw
		obj.Available=self.Available
		obj.Reserve=self.Reserve
		obj.FrozenMargin=self.FrozenMargin
		return obj

class CThostFtdcQryCFMMCBrokerKeyField(Structure):
	"""查询保证金监管系统经纪公司密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\''.format(str(self.BrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCFMMCBrokerKeyField()
		obj.BrokerID=self.BrokerID
		return obj

class CThostFtdcCFMMCBrokerKeyField(Structure):
	"""保证金监管系统经纪公司密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#密钥生成日期
		("CreateDate",c_char*9),
		#密钥生成时间
		("CreateTime",c_char*9),
		#密钥编号
		("KeyID",c_int32),
		#动态密钥
		("CurrentKey",c_char*21),
		#动态密钥类型
		("KeyKind",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getCreateDate(self):
		return str(self.CreateDate, 'GB2312')
	def getCreateTime(self):
		return str(self.CreateTime, 'GB2312')
	def getKeyID(self):
		return self.KeyID
	def getCurrentKey(self):
		return str(self.CurrentKey, 'GB2312')
	def getKeyKind(self):
		return CFMMCKeyKindType(ord(self.KeyKind))

	def __str__(self):
		return 'BrokerID=\'{0}\', ParticipantID=\'{1}\', CreateDate=\'{2}\', CreateTime=\'{3}\', KeyID={4}, CurrentKey=\'{5}\', KeyKind=CFMMCKeyKindType.{6}'.format(str(self.BrokerID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.CreateDate, 'GB2312'), str(self.CreateTime, 'GB2312'), self.KeyID, str(self.CurrentKey, 'GB2312'), '' if ord(self.KeyKind) == 0 else CFMMCKeyKindType(ord(self.KeyKind)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'CreateDate':str(self.CreateDate, 'GB2312'),'CreateTime':str(self.CreateTime, 'GB2312'),'KeyID':self.KeyID,'CurrentKey':str(self.CurrentKey, 'GB2312'),'KeyKind':'' if ord(self.KeyKind) == 0 else CFMMCKeyKindType(ord(self.KeyKind)).name}

	def clone(self):
		obj=CThostFtdcCFMMCBrokerKeyField()
		obj.BrokerID=self.BrokerID
		obj.ParticipantID=self.ParticipantID
		obj.CreateDate=self.CreateDate
		obj.CreateTime=self.CreateTime
		obj.KeyID=self.KeyID
		obj.CurrentKey=self.CurrentKey
		obj.KeyKind=self.KeyKind
		return obj

class CThostFtdcCFMMCTradingAccountKeyField(Structure):
	"""保证金监管系统经纪公司资金账户密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密钥编号
		("KeyID",c_int32),
		#动态密钥
		("CurrentKey",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getKeyID(self):
		return self.KeyID
	def getCurrentKey(self):
		return str(self.CurrentKey, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', ParticipantID=\'{1}\', AccountID=\'{2}\', KeyID={3}, CurrentKey=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.AccountID, 'GB2312'), self.KeyID, str(self.CurrentKey, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'KeyID':self.KeyID,'CurrentKey':str(self.CurrentKey, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCFMMCTradingAccountKeyField()
		obj.BrokerID=self.BrokerID
		obj.ParticipantID=self.ParticipantID
		obj.AccountID=self.AccountID
		obj.KeyID=self.KeyID
		obj.CurrentKey=self.CurrentKey
		return obj

class CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
	"""请求查询保证金监管系统经纪公司资金账户密钥"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCFMMCTradingAccountKeyField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcBrokerUserOTPParamField(Structure):
	"""用户动态令牌参数"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#动态令牌提供商
		("OTPVendorsID",c_char*2),
		#动态令牌序列号
		("SerialNumber",c_char*17),
		#令牌密钥
		("AuthKey",c_char*41),
		#漂移值
		("LastDrift",c_int32),
		#成功值
		("LastSuccess",c_int32),
		#动态令牌类型
		("OTPType",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOTPVendorsID(self):
		return str(self.OTPVendorsID, 'GB2312')
	def getSerialNumber(self):
		return str(self.SerialNumber, 'GB2312')
	def getAuthKey(self):
		return str(self.AuthKey, 'GB2312')
	def getLastDrift(self):
		return self.LastDrift
	def getLastSuccess(self):
		return self.LastSuccess
	def getOTPType(self):
		return OTPTypeType(ord(self.OTPType))

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', OTPVendorsID=\'{2}\', SerialNumber=\'{3}\', AuthKey=\'{4}\', LastDrift={5}, LastSuccess={6}, OTPType=OTPTypeType.{7}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.OTPVendorsID, 'GB2312'), str(self.SerialNumber, 'GB2312'), str(self.AuthKey, 'GB2312'), self.LastDrift, self.LastSuccess, '' if ord(self.OTPType) == 0 else OTPTypeType(ord(self.OTPType)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OTPVendorsID':str(self.OTPVendorsID, 'GB2312'),'SerialNumber':str(self.SerialNumber, 'GB2312'),'AuthKey':str(self.AuthKey, 'GB2312'),'LastDrift':self.LastDrift,'LastSuccess':self.LastSuccess,'OTPType':'' if ord(self.OTPType) == 0 else OTPTypeType(ord(self.OTPType)).name}

	def clone(self):
		obj=CThostFtdcBrokerUserOTPParamField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.OTPVendorsID=self.OTPVendorsID
		obj.SerialNumber=self.SerialNumber
		obj.AuthKey=self.AuthKey
		obj.LastDrift=self.LastDrift
		obj.LastSuccess=self.LastSuccess
		obj.OTPType=self.OTPType
		return obj

class CThostFtdcManualSyncBrokerUserOTPField(Structure):
	"""手工同步用户动态令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#动态令牌类型
		("OTPType",c_char),
		#第一个动态密码
		("FirstOTP",c_char*41),
		#第二个动态密码
		("SecondOTP",c_char*41),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getOTPType(self):
		return OTPTypeType(ord(self.OTPType))
	def getFirstOTP(self):
		return str(self.FirstOTP, 'GB2312')
	def getSecondOTP(self):
		return str(self.SecondOTP, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', OTPType=OTPTypeType.{2}, FirstOTP=\'{3}\', SecondOTP=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.OTPType) == 0 else OTPTypeType(ord(self.OTPType)).name, str(self.FirstOTP, 'GB2312'), str(self.SecondOTP, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'OTPType':'' if ord(self.OTPType) == 0 else OTPTypeType(ord(self.OTPType)).name,'FirstOTP':str(self.FirstOTP, 'GB2312'),'SecondOTP':str(self.SecondOTP, 'GB2312')}

	def clone(self):
		obj=CThostFtdcManualSyncBrokerUserOTPField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.OTPType=self.OTPType
		obj.FirstOTP=self.FirstOTP
		obj.SecondOTP=self.SecondOTP
		return obj

class CThostFtdcCommRateModelField(Structure):
	"""投资者手续费率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#手续费率模板代码
		("CommModelID",c_char*13),
		#模板名称
		("CommModelName",c_char*161),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getCommModelID(self):
		return str(self.CommModelID, 'GB2312')
	def getCommModelName(self):
		return str(self.CommModelName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', CommModelID=\'{1}\', CommModelName=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.CommModelID, 'GB2312'), str(self.CommModelName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'CommModelID':str(self.CommModelID, 'GB2312'),'CommModelName':str(self.CommModelName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCommRateModelField()
		obj.BrokerID=self.BrokerID
		obj.CommModelID=self.CommModelID
		obj.CommModelName=self.CommModelName
		return obj

class CThostFtdcQryCommRateModelField(Structure):
	"""请求查询投资者手续费率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#手续费率模板代码
		("CommModelID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getCommModelID(self):
		return str(self.CommModelID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', CommModelID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.CommModelID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'CommModelID':str(self.CommModelID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryCommRateModelField()
		obj.BrokerID=self.BrokerID
		obj.CommModelID=self.CommModelID
		return obj

class CThostFtdcMarginModelField(Structure):
	"""投资者保证金率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		#模板名称
		("MarginModelName",c_char*161),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getMarginModelID(self):
		return str(self.MarginModelID, 'GB2312')
	def getMarginModelName(self):
		return str(self.MarginModelName, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', MarginModelID=\'{1}\', MarginModelName=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.MarginModelID, 'GB2312'), str(self.MarginModelName, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'MarginModelID':str(self.MarginModelID, 'GB2312'),'MarginModelName':str(self.MarginModelName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMarginModelField()
		obj.BrokerID=self.BrokerID
		obj.MarginModelID=self.MarginModelID
		obj.MarginModelName=self.MarginModelName
		return obj

class CThostFtdcQryMarginModelField(Structure):
	"""请求查询投资者保证金率模板"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#保证金率模板代码
		("MarginModelID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getMarginModelID(self):
		return str(self.MarginModelID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', MarginModelID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.MarginModelID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'MarginModelID':str(self.MarginModelID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryMarginModelField()
		obj.BrokerID=self.BrokerID
		obj.MarginModelID=self.MarginModelID
		return obj

class CThostFtdcEWarrantOffsetField(Structure):
	"""仓单折抵信息"""
	_fields_ = [
		#交易日期
		("TradingDay",c_char*9),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		#买卖方向
		("Direction",c_char),
		#投机套保标志
		("HedgeFlag",c_char),
		#数量
		("Volume",c_int32),
		]

	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')
	def getDirection(self):
		return DirectionType(ord(self.Direction))
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))
	def getVolume(self):
		return self.Volume

	def __str__(self):
		return 'TradingDay=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', ExchangeID=\'{3}\', InstrumentID=\'{4}\', Direction=DirectionType.{5}, HedgeFlag=HedgeFlagType.{6}, Volume={7}'.format(str(self.TradingDay, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InstrumentID, 'GB2312'), '' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name, self.Volume)

	@property
	def __dict__(self):
		return {'TradingDay':str(self.TradingDay, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312'),'Direction':'' if ord(self.Direction) == 0 else DirectionType(ord(self.Direction)).name,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name,'Volume':self.Volume}

	def clone(self):
		obj=CThostFtdcEWarrantOffsetField()
		obj.TradingDay=self.TradingDay
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		obj.InstrumentID=self.InstrumentID
		obj.Direction=self.Direction
		obj.HedgeFlag=self.HedgeFlag
		obj.Volume=self.Volume
		return obj

class CThostFtdcQryEWarrantOffsetField(Structure):
	"""查询仓单折抵信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易所代码
		("ExchangeID",c_char*9),
		#合约代码
		("InstrumentID",c_char*31),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getInstrumentID(self):
		return str(self.InstrumentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ExchangeID=\'{2}\', InstrumentID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.InstrumentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'InstrumentID':str(self.InstrumentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryEWarrantOffsetField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ExchangeID=self.ExchangeID
		obj.InstrumentID=self.InstrumentID
		return obj

class CThostFtdcQryInvestorProductGroupMarginField(Structure):
	"""查询投资者品种/跨品种保证金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#品种/跨品种标示
		("ProductGroupID",c_char*31),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getProductGroupID(self):
		return str(self.ProductGroupID, 'GB2312')
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\', ProductGroupID=\'{2}\', HedgeFlag=HedgeFlagType.{3}'.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.ProductGroupID, 'GB2312'), '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'ProductGroupID':str(self.ProductGroupID, 'GB2312'),'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name}

	def clone(self):
		obj=CThostFtdcQryInvestorProductGroupMarginField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.ProductGroupID=self.ProductGroupID
		obj.HedgeFlag=self.HedgeFlag
		return obj

class CThostFtdcInvestorProductGroupMarginField(Structure):
	"""投资者品种/跨品种保证金"""
	_fields_ = [
		#品种/跨品种标示
		("ProductGroupID",c_char*31),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#交易日
		("TradingDay",c_char*9),
		#结算编号
		("SettlementID",c_int32),
		#冻结的保证金
		("FrozenMargin",c_double),
		#多头冻结的保证金
		("LongFrozenMargin",c_double),
		#空头冻结的保证金
		("ShortFrozenMargin",c_double),
		#占用的保证金
		("UseMargin",c_double),
		#多头保证金
		("LongUseMargin",c_double),
		#空头保证金
		("ShortUseMargin",c_double),
		#交易所保证金
		("ExchMargin",c_double),
		#交易所多头保证金
		("LongExchMargin",c_double),
		#交易所空头保证金
		("ShortExchMargin",c_double),
		#平仓盈亏
		("CloseProfit",c_double),
		#冻结的手续费
		("FrozenCommission",c_double),
		#手续费
		("Commission",c_double),
		#冻结的资金
		("FrozenCash",c_double),
		#资金差额
		("CashIn",c_double),
		#持仓盈亏
		("PositionProfit",c_double),
		#折抵总金额
		("OffsetAmount",c_double),
		#多头折抵总金额
		("LongOffsetAmount",c_double),
		#空头折抵总金额
		("ShortOffsetAmount",c_double),
		#交易所折抵总金额
		("ExchOffsetAmount",c_double),
		#交易所多头折抵总金额
		("LongExchOffsetAmount",c_double),
		#交易所空头折抵总金额
		("ShortExchOffsetAmount",c_double),
		#投机套保标志
		("HedgeFlag",c_char),
		]

	def getProductGroupID(self):
		return str(self.ProductGroupID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getSettlementID(self):
		return self.SettlementID
	def getFrozenMargin(self):
		return self.FrozenMargin
	def getLongFrozenMargin(self):
		return self.LongFrozenMargin
	def getShortFrozenMargin(self):
		return self.ShortFrozenMargin
	def getUseMargin(self):
		return self.UseMargin
	def getLongUseMargin(self):
		return self.LongUseMargin
	def getShortUseMargin(self):
		return self.ShortUseMargin
	def getExchMargin(self):
		return self.ExchMargin
	def getLongExchMargin(self):
		return self.LongExchMargin
	def getShortExchMargin(self):
		return self.ShortExchMargin
	def getCloseProfit(self):
		return self.CloseProfit
	def getFrozenCommission(self):
		return self.FrozenCommission
	def getCommission(self):
		return self.Commission
	def getFrozenCash(self):
		return self.FrozenCash
	def getCashIn(self):
		return self.CashIn
	def getPositionProfit(self):
		return self.PositionProfit
	def getOffsetAmount(self):
		return self.OffsetAmount
	def getLongOffsetAmount(self):
		return self.LongOffsetAmount
	def getShortOffsetAmount(self):
		return self.ShortOffsetAmount
	def getExchOffsetAmount(self):
		return self.ExchOffsetAmount
	def getLongExchOffsetAmount(self):
		return self.LongExchOffsetAmount
	def getShortExchOffsetAmount(self):
		return self.ShortExchOffsetAmount
	def getHedgeFlag(self):
		return HedgeFlagType(ord(self.HedgeFlag))

	def __str__(self):
		return 'ProductGroupID=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', TradingDay=\'{3}\', SettlementID={4}, FrozenMargin={5}, LongFrozenMargin={6}, ShortFrozenMargin={7}, UseMargin={8}, LongUseMargin={9}, ShortUseMargin={10}, ExchMargin={11}, LongExchMargin={12}, ShortExchMargin={13}, CloseProfit={14}, FrozenCommission={15}, Commission={16}, FrozenCash={17}, CashIn={18}, PositionProfit={19}, OffsetAmount={20}, LongOffsetAmount={21}, ShortOffsetAmount={22}, ExchOffsetAmount={23}, LongExchOffsetAmount={24}, ShortExchOffsetAmount={25}, HedgeFlag=HedgeFlagType.{26}'.format(str(self.ProductGroupID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), str(self.TradingDay, 'GB2312'), self.SettlementID, self.FrozenMargin, self.LongFrozenMargin, self.ShortFrozenMargin, self.UseMargin, self.LongUseMargin, self.ShortUseMargin, self.ExchMargin, self.LongExchMargin, self.ShortExchMargin, self.CloseProfit, self.FrozenCommission, self.Commission, self.FrozenCash, self.CashIn, self.PositionProfit, self.OffsetAmount, self.LongOffsetAmount, self.ShortOffsetAmount, self.ExchOffsetAmount, self.LongExchOffsetAmount, self.ShortExchOffsetAmount, '' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name)

	@property
	def __dict__(self):
		return {'ProductGroupID':str(self.ProductGroupID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'SettlementID':self.SettlementID,'FrozenMargin':self.FrozenMargin,'LongFrozenMargin':self.LongFrozenMargin,'ShortFrozenMargin':self.ShortFrozenMargin,'UseMargin':self.UseMargin,'LongUseMargin':self.LongUseMargin,'ShortUseMargin':self.ShortUseMargin,'ExchMargin':self.ExchMargin,'LongExchMargin':self.LongExchMargin,'ShortExchMargin':self.ShortExchMargin,'CloseProfit':self.CloseProfit,'FrozenCommission':self.FrozenCommission,'Commission':self.Commission,'FrozenCash':self.FrozenCash,'CashIn':self.CashIn,'PositionProfit':self.PositionProfit,'OffsetAmount':self.OffsetAmount,'LongOffsetAmount':self.LongOffsetAmount,'ShortOffsetAmount':self.ShortOffsetAmount,'ExchOffsetAmount':self.ExchOffsetAmount,'LongExchOffsetAmount':self.LongExchOffsetAmount,'ShortExchOffsetAmount':self.ShortExchOffsetAmount,'HedgeFlag':'' if ord(self.HedgeFlag) == 0 else HedgeFlagType(ord(self.HedgeFlag)).name}

	def clone(self):
		obj=CThostFtdcInvestorProductGroupMarginField()
		obj.ProductGroupID=self.ProductGroupID
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.TradingDay=self.TradingDay
		obj.SettlementID=self.SettlementID
		obj.FrozenMargin=self.FrozenMargin
		obj.LongFrozenMargin=self.LongFrozenMargin
		obj.ShortFrozenMargin=self.ShortFrozenMargin
		obj.UseMargin=self.UseMargin
		obj.LongUseMargin=self.LongUseMargin
		obj.ShortUseMargin=self.ShortUseMargin
		obj.ExchMargin=self.ExchMargin
		obj.LongExchMargin=self.LongExchMargin
		obj.ShortExchMargin=self.ShortExchMargin
		obj.CloseProfit=self.CloseProfit
		obj.FrozenCommission=self.FrozenCommission
		obj.Commission=self.Commission
		obj.FrozenCash=self.FrozenCash
		obj.CashIn=self.CashIn
		obj.PositionProfit=self.PositionProfit
		obj.OffsetAmount=self.OffsetAmount
		obj.LongOffsetAmount=self.LongOffsetAmount
		obj.ShortOffsetAmount=self.ShortOffsetAmount
		obj.ExchOffsetAmount=self.ExchOffsetAmount
		obj.LongExchOffsetAmount=self.LongExchOffsetAmount
		obj.ShortExchOffsetAmount=self.ShortExchOffsetAmount
		obj.HedgeFlag=self.HedgeFlag
		return obj

class CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
	"""查询监控中心用户令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', InvestorID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQueryCFMMCTradingAccountTokenField()
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		return obj

class CThostFtdcCFMMCTradingAccountTokenField(Structure):
	"""监控中心用户令牌"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#经纪公司统一编码
		("ParticipantID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#密钥编号
		("KeyID",c_int32),
		#动态令牌
		("Token",c_char*21),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getParticipantID(self):
		return str(self.ParticipantID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getKeyID(self):
		return self.KeyID
	def getToken(self):
		return str(self.Token, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', ParticipantID=\'{1}\', AccountID=\'{2}\', KeyID={3}, Token=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.ParticipantID, 'GB2312'), str(self.AccountID, 'GB2312'), self.KeyID, str(self.Token, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'ParticipantID':str(self.ParticipantID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'KeyID':self.KeyID,'Token':str(self.Token, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCFMMCTradingAccountTokenField()
		obj.BrokerID=self.BrokerID
		obj.ParticipantID=self.ParticipantID
		obj.AccountID=self.AccountID
		obj.KeyID=self.KeyID
		obj.Token=self.Token
		return obj

class CThostFtdcQryProductGroupField(Structure):
	"""查询产品组"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')

	def __str__(self):
		return 'ProductID=\'{0}\', ExchangeID=\'{1}\''.format(str(self.ProductID, 'GB2312'), str(self.ExchangeID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryProductGroupField()
		obj.ProductID=self.ProductID
		obj.ExchangeID=self.ExchangeID
		return obj

class CThostFtdcProductGroupField(Structure):
	"""投资者品种/跨品种保证金产品组"""
	_fields_ = [
		#产品代码
		("ProductID",c_char*31),
		#交易所代码
		("ExchangeID",c_char*9),
		#产品组代码
		("ProductGroupID",c_char*31),
		]

	def getProductID(self):
		return str(self.ProductID, 'GB2312')
	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getProductGroupID(self):
		return str(self.ProductGroupID, 'GB2312')

	def __str__(self):
		return 'ProductID=\'{0}\', ExchangeID=\'{1}\', ProductGroupID=\'{2}\''.format(str(self.ProductID, 'GB2312'), str(self.ExchangeID, 'GB2312'), str(self.ProductGroupID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ProductID':str(self.ProductID, 'GB2312'),'ExchangeID':str(self.ExchangeID, 'GB2312'),'ProductGroupID':str(self.ProductGroupID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcProductGroupField()
		obj.ProductID=self.ProductID
		obj.ExchangeID=self.ExchangeID
		obj.ProductGroupID=self.ProductGroupID
		return obj

class CThostFtdcBulletinField(Structure):
	"""交易所公告"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#交易日
		("TradingDay",c_char*9),
		#公告编号
		("BulletinID",c_int32),
		#序列号
		("SequenceNo",c_int32),
		#公告类型
		("NewsType",c_char*3),
		#紧急程度
		("NewsUrgency",c_char),
		#发送时间
		("SendTime",c_char*9),
		#消息摘要
		("Abstract",c_char*81),
		#消息来源
		("ComeFrom",c_char*21),
		#消息正文
		("Content",c_char*501),
		#WEB地址
		("URLLink",c_char*201),
		#市场代码
		("MarketID",c_char*31),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getBulletinID(self):
		return self.BulletinID
	def getSequenceNo(self):
		return self.SequenceNo
	def getNewsType(self):
		return str(self.NewsType, 'GB2312')
	def getNewsUrgency(self):
		return NewsUrgencyType(ord(self.NewsUrgency))
	def getSendTime(self):
		return str(self.SendTime, 'GB2312')
	def getAbstract(self):
		return str(self.Abstract, 'GB2312')
	def getComeFrom(self):
		return str(self.ComeFrom, 'GB2312')
	def getContent(self):
		return str(self.Content, 'GB2312')
	def getURLLink(self):
		return str(self.URLLink, 'GB2312')
	def getMarketID(self):
		return str(self.MarketID, 'GB2312')

	def __str__(self):
		return 'ExchangeID=\'{0}\', TradingDay=\'{1}\', BulletinID={2}, SequenceNo={3}, NewsType=\'{4}\', NewsUrgency=NewsUrgencyType.{5}, SendTime=\'{6}\', Abstract=\'{7}\', ComeFrom=\'{8}\', Content=\'{9}\', URLLink=\'{10}\', MarketID=\'{11}\''.format(str(self.ExchangeID, 'GB2312'), str(self.TradingDay, 'GB2312'), self.BulletinID, self.SequenceNo, str(self.NewsType, 'GB2312'), '' if ord(self.NewsUrgency) == 0 else NewsUrgencyType(ord(self.NewsUrgency)).name, str(self.SendTime, 'GB2312'), str(self.Abstract, 'GB2312'), str(self.ComeFrom, 'GB2312'), str(self.Content, 'GB2312'), str(self.URLLink, 'GB2312'), str(self.MarketID, 'GB2312'))

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'BulletinID':self.BulletinID,'SequenceNo':self.SequenceNo,'NewsType':str(self.NewsType, 'GB2312'),'NewsUrgency':'' if ord(self.NewsUrgency) == 0 else NewsUrgencyType(ord(self.NewsUrgency)).name,'SendTime':str(self.SendTime, 'GB2312'),'Abstract':str(self.Abstract, 'GB2312'),'ComeFrom':str(self.ComeFrom, 'GB2312'),'Content':str(self.Content, 'GB2312'),'URLLink':str(self.URLLink, 'GB2312'),'MarketID':str(self.MarketID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcBulletinField()
		obj.ExchangeID=self.ExchangeID
		obj.TradingDay=self.TradingDay
		obj.BulletinID=self.BulletinID
		obj.SequenceNo=self.SequenceNo
		obj.NewsType=self.NewsType
		obj.NewsUrgency=self.NewsUrgency
		obj.SendTime=self.SendTime
		obj.Abstract=self.Abstract
		obj.ComeFrom=self.ComeFrom
		obj.Content=self.Content
		obj.URLLink=self.URLLink
		obj.MarketID=self.MarketID
		return obj

class CThostFtdcQryBulletinField(Structure):
	"""查询交易所公告"""
	_fields_ = [
		#交易所代码
		("ExchangeID",c_char*9),
		#公告编号
		("BulletinID",c_int32),
		#序列号
		("SequenceNo",c_int32),
		#公告类型
		("NewsType",c_char*3),
		#紧急程度
		("NewsUrgency",c_char),
		]

	def getExchangeID(self):
		return str(self.ExchangeID, 'GB2312')
	def getBulletinID(self):
		return self.BulletinID
	def getSequenceNo(self):
		return self.SequenceNo
	def getNewsType(self):
		return str(self.NewsType, 'GB2312')
	def getNewsUrgency(self):
		return NewsUrgencyType(ord(self.NewsUrgency))

	def __str__(self):
		return 'ExchangeID=\'{0}\', BulletinID={1}, SequenceNo={2}, NewsType=\'{3}\', NewsUrgency=NewsUrgencyType.{4}'.format(str(self.ExchangeID, 'GB2312'), self.BulletinID, self.SequenceNo, str(self.NewsType, 'GB2312'), '' if ord(self.NewsUrgency) == 0 else NewsUrgencyType(ord(self.NewsUrgency)).name)

	@property
	def __dict__(self):
		return {'ExchangeID':str(self.ExchangeID, 'GB2312'),'BulletinID':self.BulletinID,'SequenceNo':self.SequenceNo,'NewsType':str(self.NewsType, 'GB2312'),'NewsUrgency':'' if ord(self.NewsUrgency) == 0 else NewsUrgencyType(ord(self.NewsUrgency)).name}

	def clone(self):
		obj=CThostFtdcQryBulletinField()
		obj.ExchangeID=self.ExchangeID
		obj.BulletinID=self.BulletinID
		obj.SequenceNo=self.SequenceNo
		obj.NewsType=self.NewsType
		obj.NewsUrgency=self.NewsUrgency
		return obj

class CThostFtdcReqOpenAccountField(Structure):
	"""转帐开户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', AccountID=\'{27}\', Password=\'{28}\', InstallID={29}, VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', CashExchangeCode=CashExchangeCodeType.{32}, Digest=\'{33}\', BankAccType=BankAccTypeType.{34}, DeviceID=\'{35}\', BankSecuAccType=BankAccTypeType.{36}, BrokerIDByBank=\'{37}\', BankSecuAcc=\'{38}\', BankPwdFlag=PwdFlagType.{39}, SecuPwdFlag=PwdFlagType.{40}, OperNo=\'{41}\', TID={42}, UserID=\'{43}\', LongCustomerName=\'{44}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), '' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name, str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.TID, str(self.UserID, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'CashExchangeCode':'' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name,'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'TID':self.TID,'UserID':str(self.UserID, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqOpenAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.CashExchangeCode=self.CashExchangeCode
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.TID=self.TID
		obj.UserID=self.UserID
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcReqCancelAccountField(Structure):
	"""转帐销户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', AccountID=\'{27}\', Password=\'{28}\', InstallID={29}, VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', CashExchangeCode=CashExchangeCodeType.{32}, Digest=\'{33}\', BankAccType=BankAccTypeType.{34}, DeviceID=\'{35}\', BankSecuAccType=BankAccTypeType.{36}, BrokerIDByBank=\'{37}\', BankSecuAcc=\'{38}\', BankPwdFlag=PwdFlagType.{39}, SecuPwdFlag=PwdFlagType.{40}, OperNo=\'{41}\', TID={42}, UserID=\'{43}\', LongCustomerName=\'{44}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), '' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name, str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.TID, str(self.UserID, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'CashExchangeCode':'' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name,'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'TID':self.TID,'UserID':str(self.UserID, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqCancelAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.CashExchangeCode=self.CashExchangeCode
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.TID=self.TID
		obj.UserID=self.UserID
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcReqChangeAccountField(Structure):
	"""变更银行账户请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#新银行帐号
		("NewBankAccount",c_char*41),
		#新银行密码
		("NewBankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号类型
		("BankAccType",c_char),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易ID
		("TID",c_int32),
		#摘要
		("Digest",c_char*36),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getNewBankAccount(self):
		return str(self.NewBankAccount, 'GB2312')
	def getNewBankPassWord(self):
		return str(self.NewBankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getTID(self):
		return self.TID
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', NewBankAccount=\'{27}\', NewBankPassWord=\'{28}\', AccountID=\'{29}\', Password=\'{30}\', BankAccType=BankAccTypeType.{31}, InstallID={32}, VerifyCertNoFlag=YesNoIndicatorType.{33}, CurrencyID=\'{34}\', BrokerIDByBank=\'{35}\', BankPwdFlag=PwdFlagType.{36}, SecuPwdFlag=PwdFlagType.{37}, TID={38}, Digest=\'{39}\', LongCustomerName=\'{40}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.NewBankAccount, 'GB2312'), str(self.NewBankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, self.TID, str(self.Digest, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'NewBankAccount':str(self.NewBankAccount, 'GB2312'),'NewBankPassWord':str(self.NewBankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'TID':self.TID,'Digest':str(self.Digest, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqChangeAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.NewBankAccount=self.NewBankAccount
		obj.NewBankPassWord=self.NewBankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.BankAccType=self.BankAccType
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.TID=self.TID
		obj.Digest=self.Digest
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcReqTransferField(Structure):
	"""转账请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', CustType=CustTypeType.{15}, BankAccount=\'{16}\', BankPassWord=\'{17}\', AccountID=\'{18}\', Password=\'{19}\', InstallID={20}, FutureSerial={21}, UserID=\'{22}\', VerifyCertNoFlag=YesNoIndicatorType.{23}, CurrencyID=\'{24}\', TradeAmount={25}, FutureFetchAmount={26}, FeePayFlag=FeePayFlagType.{27}, CustFee={28}, BrokerFee={29}, Message=\'{30}\', Digest=\'{31}\', BankAccType=BankAccTypeType.{32}, DeviceID=\'{33}\', BankSecuAccType=BankAccTypeType.{34}, BrokerIDByBank=\'{35}\', BankSecuAcc=\'{36}\', BankPwdFlag=PwdFlagType.{37}, SecuPwdFlag=PwdFlagType.{38}, OperNo=\'{39}\', RequestID={40}, TID={41}, TransferStatus=TransferStatusType.{42}, LongCustomerName=\'{43}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, self.FutureSerial, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), self.TradeAmount, self.FutureFetchAmount, '' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name, self.CustFee, self.BrokerFee, str(self.Message, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, '' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'FutureSerial':self.FutureSerial,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'FutureFetchAmount':self.FutureFetchAmount,'FeePayFlag':'' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name,'CustFee':self.CustFee,'BrokerFee':self.BrokerFee,'Message':str(self.Message, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'TransferStatus':'' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqTransferField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.FutureSerial=self.FutureSerial
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.FutureFetchAmount=self.FutureFetchAmount
		obj.FeePayFlag=self.FeePayFlag
		obj.CustFee=self.CustFee
		obj.BrokerFee=self.BrokerFee
		obj.Message=self.Message
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.TransferStatus=self.TransferStatus
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcRspTransferField(Structure):
	"""银行发起银行资金转期货响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', CustType=CustTypeType.{15}, BankAccount=\'{16}\', BankPassWord=\'{17}\', AccountID=\'{18}\', Password=\'{19}\', InstallID={20}, FutureSerial={21}, UserID=\'{22}\', VerifyCertNoFlag=YesNoIndicatorType.{23}, CurrencyID=\'{24}\', TradeAmount={25}, FutureFetchAmount={26}, FeePayFlag=FeePayFlagType.{27}, CustFee={28}, BrokerFee={29}, Message=\'{30}\', Digest=\'{31}\', BankAccType=BankAccTypeType.{32}, DeviceID=\'{33}\', BankSecuAccType=BankAccTypeType.{34}, BrokerIDByBank=\'{35}\', BankSecuAcc=\'{36}\', BankPwdFlag=PwdFlagType.{37}, SecuPwdFlag=PwdFlagType.{38}, OperNo=\'{39}\', RequestID={40}, TID={41}, TransferStatus=TransferStatusType.{42}, ErrorID={43}, ErrorMsg=\'{44}\', LongCustomerName=\'{45}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, self.FutureSerial, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), self.TradeAmount, self.FutureFetchAmount, '' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name, self.CustFee, self.BrokerFee, str(self.Message, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, '' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'FutureSerial':self.FutureSerial,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'FutureFetchAmount':self.FutureFetchAmount,'FeePayFlag':'' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name,'CustFee':self.CustFee,'BrokerFee':self.BrokerFee,'Message':str(self.Message, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'TransferStatus':'' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspTransferField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.FutureSerial=self.FutureSerial
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.FutureFetchAmount=self.FutureFetchAmount
		obj.FeePayFlag=self.FeePayFlag
		obj.CustFee=self.CustFee
		obj.BrokerFee=self.BrokerFee
		obj.Message=self.Message
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.TransferStatus=self.TransferStatus
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcReqRepealField(Structure):
	"""冲正请求"""
	_fields_ = [
		#冲正时间间隔
		("RepealTimeInterval",c_int32),
		#已经冲正次数
		("RepealedTimes",c_int32),
		#银行冲正标志
		("BankRepealFlag",c_char),
		#期商冲正标志
		("BrokerRepealFlag",c_char),
		#被冲正平台流水号
		("PlateRepealSerial",c_int32),
		#被冲正银行流水号
		("BankRepealSerial",c_char*13),
		#被冲正期货流水号
		("FutureRepealSerial",c_int32),
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getRepealTimeInterval(self):
		return self.RepealTimeInterval
	def getRepealedTimes(self):
		return self.RepealedTimes
	def getBankRepealFlag(self):
		return BankRepealFlagType(ord(self.BankRepealFlag))
	def getBrokerRepealFlag(self):
		return BrokerRepealFlagType(ord(self.BrokerRepealFlag))
	def getPlateRepealSerial(self):
		return self.PlateRepealSerial
	def getBankRepealSerial(self):
		return str(self.BankRepealSerial, 'GB2312')
	def getFutureRepealSerial(self):
		return self.FutureRepealSerial
	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'RepealTimeInterval={0}, RepealedTimes={1}, BankRepealFlag=BankRepealFlagType.{2}, BrokerRepealFlag=BrokerRepealFlagType.{3}, PlateRepealSerial={4}, BankRepealSerial=\'{5}\', FutureRepealSerial={6}, TradeCode=\'{7}\', BankID=\'{8}\', BankBranchID=\'{9}\', BrokerID=\'{10}\', BrokerBranchID=\'{11}\', TradeDate=\'{12}\', TradeTime=\'{13}\', BankSerial=\'{14}\', TradingDay=\'{15}\', PlateSerial={16}, LastFragment=LastFragmentType.{17}, SessionID={18}, CustomerName=\'{19}\', IdCardType=IdCardTypeType.{20}, IdentifiedCardNo=\'{21}\', CustType=CustTypeType.{22}, BankAccount=\'{23}\', BankPassWord=\'{24}\', AccountID=\'{25}\', Password=\'{26}\', InstallID={27}, FutureSerial={28}, UserID=\'{29}\', VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', TradeAmount={32}, FutureFetchAmount={33}, FeePayFlag=FeePayFlagType.{34}, CustFee={35}, BrokerFee={36}, Message=\'{37}\', Digest=\'{38}\', BankAccType=BankAccTypeType.{39}, DeviceID=\'{40}\', BankSecuAccType=BankAccTypeType.{41}, BrokerIDByBank=\'{42}\', BankSecuAcc=\'{43}\', BankPwdFlag=PwdFlagType.{44}, SecuPwdFlag=PwdFlagType.{45}, OperNo=\'{46}\', RequestID={47}, TID={48}, TransferStatus=TransferStatusType.{49}, LongCustomerName=\'{50}\''.format(self.RepealTimeInterval, self.RepealedTimes, '' if ord(self.BankRepealFlag) == 0 else BankRepealFlagType(ord(self.BankRepealFlag)).name, '' if ord(self.BrokerRepealFlag) == 0 else BrokerRepealFlagType(ord(self.BrokerRepealFlag)).name, self.PlateRepealSerial, str(self.BankRepealSerial, 'GB2312'), self.FutureRepealSerial, str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, self.FutureSerial, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), self.TradeAmount, self.FutureFetchAmount, '' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name, self.CustFee, self.BrokerFee, str(self.Message, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, '' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'RepealTimeInterval':self.RepealTimeInterval,'RepealedTimes':self.RepealedTimes,'BankRepealFlag':'' if ord(self.BankRepealFlag) == 0 else BankRepealFlagType(ord(self.BankRepealFlag)).name,'BrokerRepealFlag':'' if ord(self.BrokerRepealFlag) == 0 else BrokerRepealFlagType(ord(self.BrokerRepealFlag)).name,'PlateRepealSerial':self.PlateRepealSerial,'BankRepealSerial':str(self.BankRepealSerial, 'GB2312'),'FutureRepealSerial':self.FutureRepealSerial,'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'FutureSerial':self.FutureSerial,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'FutureFetchAmount':self.FutureFetchAmount,'FeePayFlag':'' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name,'CustFee':self.CustFee,'BrokerFee':self.BrokerFee,'Message':str(self.Message, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'TransferStatus':'' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqRepealField()
		obj.RepealTimeInterval=self.RepealTimeInterval
		obj.RepealedTimes=self.RepealedTimes
		obj.BankRepealFlag=self.BankRepealFlag
		obj.BrokerRepealFlag=self.BrokerRepealFlag
		obj.PlateRepealSerial=self.PlateRepealSerial
		obj.BankRepealSerial=self.BankRepealSerial
		obj.FutureRepealSerial=self.FutureRepealSerial
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.FutureSerial=self.FutureSerial
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.FutureFetchAmount=self.FutureFetchAmount
		obj.FeePayFlag=self.FeePayFlag
		obj.CustFee=self.CustFee
		obj.BrokerFee=self.BrokerFee
		obj.Message=self.Message
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.TransferStatus=self.TransferStatus
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcRspRepealField(Structure):
	"""冲正响应"""
	_fields_ = [
		#冲正时间间隔
		("RepealTimeInterval",c_int32),
		#已经冲正次数
		("RepealedTimes",c_int32),
		#银行冲正标志
		("BankRepealFlag",c_char),
		#期商冲正标志
		("BrokerRepealFlag",c_char),
		#被冲正平台流水号
		("PlateRepealSerial",c_int32),
		#被冲正银行流水号
		("BankRepealSerial",c_char*13),
		#被冲正期货流水号
		("FutureRepealSerial",c_int32),
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#期货公司流水号
		("FutureSerial",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#期货可取金额
		("FutureFetchAmount",c_double),
		#费用支付标志
		("FeePayFlag",c_char),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#发送方给接收方的消息
		("Message",c_char*129),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#转账交易状态
		("TransferStatus",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getRepealTimeInterval(self):
		return self.RepealTimeInterval
	def getRepealedTimes(self):
		return self.RepealedTimes
	def getBankRepealFlag(self):
		return BankRepealFlagType(ord(self.BankRepealFlag))
	def getBrokerRepealFlag(self):
		return BrokerRepealFlagType(ord(self.BrokerRepealFlag))
	def getPlateRepealSerial(self):
		return self.PlateRepealSerial
	def getBankRepealSerial(self):
		return str(self.BankRepealSerial, 'GB2312')
	def getFutureRepealSerial(self):
		return self.FutureRepealSerial
	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getFutureSerial(self):
		return self.FutureSerial
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getFutureFetchAmount(self):
		return self.FutureFetchAmount
	def getFeePayFlag(self):
		return FeePayFlagType(ord(self.FeePayFlag))
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getTransferStatus(self):
		return TransferStatusType(ord(self.TransferStatus))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'RepealTimeInterval={0}, RepealedTimes={1}, BankRepealFlag=BankRepealFlagType.{2}, BrokerRepealFlag=BrokerRepealFlagType.{3}, PlateRepealSerial={4}, BankRepealSerial=\'{5}\', FutureRepealSerial={6}, TradeCode=\'{7}\', BankID=\'{8}\', BankBranchID=\'{9}\', BrokerID=\'{10}\', BrokerBranchID=\'{11}\', TradeDate=\'{12}\', TradeTime=\'{13}\', BankSerial=\'{14}\', TradingDay=\'{15}\', PlateSerial={16}, LastFragment=LastFragmentType.{17}, SessionID={18}, CustomerName=\'{19}\', IdCardType=IdCardTypeType.{20}, IdentifiedCardNo=\'{21}\', CustType=CustTypeType.{22}, BankAccount=\'{23}\', BankPassWord=\'{24}\', AccountID=\'{25}\', Password=\'{26}\', InstallID={27}, FutureSerial={28}, UserID=\'{29}\', VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', TradeAmount={32}, FutureFetchAmount={33}, FeePayFlag=FeePayFlagType.{34}, CustFee={35}, BrokerFee={36}, Message=\'{37}\', Digest=\'{38}\', BankAccType=BankAccTypeType.{39}, DeviceID=\'{40}\', BankSecuAccType=BankAccTypeType.{41}, BrokerIDByBank=\'{42}\', BankSecuAcc=\'{43}\', BankPwdFlag=PwdFlagType.{44}, SecuPwdFlag=PwdFlagType.{45}, OperNo=\'{46}\', RequestID={47}, TID={48}, TransferStatus=TransferStatusType.{49}, ErrorID={50}, ErrorMsg=\'{51}\', LongCustomerName=\'{52}\''.format(self.RepealTimeInterval, self.RepealedTimes, '' if ord(self.BankRepealFlag) == 0 else BankRepealFlagType(ord(self.BankRepealFlag)).name, '' if ord(self.BrokerRepealFlag) == 0 else BrokerRepealFlagType(ord(self.BrokerRepealFlag)).name, self.PlateRepealSerial, str(self.BankRepealSerial, 'GB2312'), self.FutureRepealSerial, str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, self.FutureSerial, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), self.TradeAmount, self.FutureFetchAmount, '' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name, self.CustFee, self.BrokerFee, str(self.Message, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, '' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'RepealTimeInterval':self.RepealTimeInterval,'RepealedTimes':self.RepealedTimes,'BankRepealFlag':'' if ord(self.BankRepealFlag) == 0 else BankRepealFlagType(ord(self.BankRepealFlag)).name,'BrokerRepealFlag':'' if ord(self.BrokerRepealFlag) == 0 else BrokerRepealFlagType(ord(self.BrokerRepealFlag)).name,'PlateRepealSerial':self.PlateRepealSerial,'BankRepealSerial':str(self.BankRepealSerial, 'GB2312'),'FutureRepealSerial':self.FutureRepealSerial,'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'FutureSerial':self.FutureSerial,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'FutureFetchAmount':self.FutureFetchAmount,'FeePayFlag':'' if ord(self.FeePayFlag) == 0 else FeePayFlagType(ord(self.FeePayFlag)).name,'CustFee':self.CustFee,'BrokerFee':self.BrokerFee,'Message':str(self.Message, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'TransferStatus':'' if ord(self.TransferStatus) == 0 else TransferStatusType(ord(self.TransferStatus)).name,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspRepealField()
		obj.RepealTimeInterval=self.RepealTimeInterval
		obj.RepealedTimes=self.RepealedTimes
		obj.BankRepealFlag=self.BankRepealFlag
		obj.BrokerRepealFlag=self.BrokerRepealFlag
		obj.PlateRepealSerial=self.PlateRepealSerial
		obj.BankRepealSerial=self.BankRepealSerial
		obj.FutureRepealSerial=self.FutureRepealSerial
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.FutureSerial=self.FutureSerial
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.FutureFetchAmount=self.FutureFetchAmount
		obj.FeePayFlag=self.FeePayFlag
		obj.CustFee=self.CustFee
		obj.BrokerFee=self.BrokerFee
		obj.Message=self.Message
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.TransferStatus=self.TransferStatus
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcReqQueryAccountField(Structure):
	"""查询账户信息请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', CustType=CustTypeType.{15}, BankAccount=\'{16}\', BankPassWord=\'{17}\', AccountID=\'{18}\', Password=\'{19}\', FutureSerial={20}, InstallID={21}, UserID=\'{22}\', VerifyCertNoFlag=YesNoIndicatorType.{23}, CurrencyID=\'{24}\', Digest=\'{25}\', BankAccType=BankAccTypeType.{26}, DeviceID=\'{27}\', BankSecuAccType=BankAccTypeType.{28}, BrokerIDByBank=\'{29}\', BankSecuAcc=\'{30}\', BankPwdFlag=PwdFlagType.{31}, SecuPwdFlag=PwdFlagType.{32}, OperNo=\'{33}\', RequestID={34}, TID={35}, LongCustomerName=\'{36}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.FutureSerial, self.InstallID, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'FutureSerial':self.FutureSerial,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqQueryAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.FutureSerial=self.FutureSerial
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcRspQueryAccountField(Structure):
	"""查询账户信息响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#银行可用金额
		("BankUseAmount",c_double),
		#银行可取金额
		("BankFetchAmount",c_double),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getBankUseAmount(self):
		return self.BankUseAmount
	def getBankFetchAmount(self):
		return self.BankFetchAmount
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', CustType=CustTypeType.{15}, BankAccount=\'{16}\', BankPassWord=\'{17}\', AccountID=\'{18}\', Password=\'{19}\', FutureSerial={20}, InstallID={21}, UserID=\'{22}\', VerifyCertNoFlag=YesNoIndicatorType.{23}, CurrencyID=\'{24}\', Digest=\'{25}\', BankAccType=BankAccTypeType.{26}, DeviceID=\'{27}\', BankSecuAccType=BankAccTypeType.{28}, BrokerIDByBank=\'{29}\', BankSecuAcc=\'{30}\', BankPwdFlag=PwdFlagType.{31}, SecuPwdFlag=PwdFlagType.{32}, OperNo=\'{33}\', RequestID={34}, TID={35}, BankUseAmount={36}, BankFetchAmount={37}, LongCustomerName=\'{38}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.FutureSerial, self.InstallID, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.BankUseAmount, self.BankFetchAmount, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'FutureSerial':self.FutureSerial,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'BankUseAmount':self.BankUseAmount,'BankFetchAmount':self.BankFetchAmount,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspQueryAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.FutureSerial=self.FutureSerial
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.BankUseAmount=self.BankUseAmount
		obj.BankFetchAmount=self.BankFetchAmount
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcFutureSignIOField(Structure):
	"""期商签到签退"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}'.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID)

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID}

	def clone(self):
		obj=CThostFtdcFutureSignIOField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		return obj

class CThostFtdcRspFutureSignInField(Structure):
	"""期商签到响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#PIN密钥
		("PinKey",c_char*129),
		#MAC密钥
		("MacKey",c_char*129),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getPinKey(self):
		return str(self.PinKey, 'GB2312')
	def getMacKey(self):
		return str(self.MacKey, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}, ErrorID={21}, ErrorMsg=\'{22}\', PinKey=\'{23}\', MacKey=\'{24}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.PinKey, 'GB2312'), str(self.MacKey, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'PinKey':str(self.PinKey, 'GB2312'),'MacKey':str(self.MacKey, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspFutureSignInField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.PinKey=self.PinKey
		obj.MacKey=self.MacKey
		return obj

class CThostFtdcReqFutureSignOutField(Structure):
	"""期商签退请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}'.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID)

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID}

	def clone(self):
		obj=CThostFtdcReqFutureSignOutField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		return obj

class CThostFtdcRspFutureSignOutField(Structure):
	"""期商签退响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}, ErrorID={21}, ErrorMsg=\'{22}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspFutureSignOutField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcReqQueryTradeResultBySerialField(Structure):
	"""查询指定流水号的交易结果请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#流水号
		("Reference",c_int32),
		#本流水号发布者的机构类型
		("RefrenceIssureType",c_char),
		#本流水号发布者机构编码
		("RefrenceIssure",c_char*36),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#摘要
		("Digest",c_char*36),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getReference(self):
		return self.Reference
	def getRefrenceIssureType(self):
		return InstitutionTypeType(ord(self.RefrenceIssureType))
	def getRefrenceIssure(self):
		return str(self.RefrenceIssure, 'GB2312')
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, Reference={12}, RefrenceIssureType=InstitutionTypeType.{13}, RefrenceIssure=\'{14}\', CustomerName=\'{15}\', IdCardType=IdCardTypeType.{16}, IdentifiedCardNo=\'{17}\', CustType=CustTypeType.{18}, BankAccount=\'{19}\', BankPassWord=\'{20}\', AccountID=\'{21}\', Password=\'{22}\', CurrencyID=\'{23}\', TradeAmount={24}, Digest=\'{25}\', LongCustomerName=\'{26}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.Reference, '' if ord(self.RefrenceIssureType) == 0 else InstitutionTypeType(ord(self.RefrenceIssureType)).name, str(self.RefrenceIssure, 'GB2312'), str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.CurrencyID, 'GB2312'), self.TradeAmount, str(self.Digest, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'Reference':self.Reference,'RefrenceIssureType':'' if ord(self.RefrenceIssureType) == 0 else InstitutionTypeType(ord(self.RefrenceIssureType)).name,'RefrenceIssure':str(self.RefrenceIssure, 'GB2312'),'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'Digest':str(self.Digest, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqQueryTradeResultBySerialField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.Reference=self.Reference
		obj.RefrenceIssureType=self.RefrenceIssureType
		obj.RefrenceIssure=self.RefrenceIssure
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.Digest=self.Digest
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcRspQueryTradeResultBySerialField(Structure):
	"""查询指定流水号的交易结果响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#流水号
		("Reference",c_int32),
		#本流水号发布者的机构类型
		("RefrenceIssureType",c_char),
		#本流水号发布者机构编码
		("RefrenceIssure",c_char*36),
		#原始返回代码
		("OriginReturnCode",c_char*7),
		#原始返回码描述
		("OriginDescrInfoForReturnCode",c_char*129),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		#转帐金额
		("TradeAmount",c_double),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getReference(self):
		return self.Reference
	def getRefrenceIssureType(self):
		return InstitutionTypeType(ord(self.RefrenceIssureType))
	def getRefrenceIssure(self):
		return str(self.RefrenceIssure, 'GB2312')
	def getOriginReturnCode(self):
		return str(self.OriginReturnCode, 'GB2312')
	def getOriginDescrInfoForReturnCode(self):
		return str(self.OriginDescrInfoForReturnCode, 'GB2312')
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getDigest(self):
		return str(self.Digest, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, ErrorID={12}, ErrorMsg=\'{13}\', Reference={14}, RefrenceIssureType=InstitutionTypeType.{15}, RefrenceIssure=\'{16}\', OriginReturnCode=\'{17}\', OriginDescrInfoForReturnCode=\'{18}\', BankAccount=\'{19}\', BankPassWord=\'{20}\', AccountID=\'{21}\', Password=\'{22}\', CurrencyID=\'{23}\', TradeAmount={24}, Digest=\'{25}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.ErrorID, str(self.ErrorMsg, 'GB2312'), self.Reference, '' if ord(self.RefrenceIssureType) == 0 else InstitutionTypeType(ord(self.RefrenceIssureType)).name, str(self.RefrenceIssure, 'GB2312'), str(self.OriginReturnCode, 'GB2312'), str(self.OriginDescrInfoForReturnCode, 'GB2312'), str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.CurrencyID, 'GB2312'), self.TradeAmount, str(self.Digest, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'Reference':self.Reference,'RefrenceIssureType':'' if ord(self.RefrenceIssureType) == 0 else InstitutionTypeType(ord(self.RefrenceIssureType)).name,'RefrenceIssure':str(self.RefrenceIssure, 'GB2312'),'OriginReturnCode':str(self.OriginReturnCode, 'GB2312'),'OriginDescrInfoForReturnCode':str(self.OriginDescrInfoForReturnCode, 'GB2312'),'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'Digest':str(self.Digest, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspQueryTradeResultBySerialField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.Reference=self.Reference
		obj.RefrenceIssureType=self.RefrenceIssureType
		obj.RefrenceIssure=self.RefrenceIssure
		obj.OriginReturnCode=self.OriginReturnCode
		obj.OriginDescrInfoForReturnCode=self.OriginDescrInfoForReturnCode
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.Digest=self.Digest
		return obj

class CThostFtdcReqDayEndFileReadyField(Structure):
	"""日终文件就绪请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#文件业务功能
		("FileBusinessCode",c_char),
		#摘要
		("Digest",c_char*36),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getFileBusinessCode(self):
		return FileBusinessCodeType(ord(self.FileBusinessCode))
	def getDigest(self):
		return str(self.Digest, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, FileBusinessCode=FileBusinessCodeType.{12}, Digest=\'{13}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, '' if ord(self.FileBusinessCode) == 0 else FileBusinessCodeType(ord(self.FileBusinessCode)).name, str(self.Digest, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'FileBusinessCode':'' if ord(self.FileBusinessCode) == 0 else FileBusinessCodeType(ord(self.FileBusinessCode)).name,'Digest':str(self.Digest, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReqDayEndFileReadyField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.FileBusinessCode=self.FileBusinessCode
		obj.Digest=self.Digest
		return obj

class CThostFtdcReturnResultField(Structure):
	"""返回结果"""
	_fields_ = [
		#返回代码
		("ReturnCode",c_char*7),
		#返回码描述
		("DescrInfoForReturnCode",c_char*129),
		]

	def getReturnCode(self):
		return str(self.ReturnCode, 'GB2312')
	def getDescrInfoForReturnCode(self):
		return str(self.DescrInfoForReturnCode, 'GB2312')

	def __str__(self):
		return 'ReturnCode=\'{0}\', DescrInfoForReturnCode=\'{1}\''.format(str(self.ReturnCode, 'GB2312'), str(self.DescrInfoForReturnCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'ReturnCode':str(self.ReturnCode, 'GB2312'),'DescrInfoForReturnCode':str(self.DescrInfoForReturnCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReturnResultField()
		obj.ReturnCode=self.ReturnCode
		obj.DescrInfoForReturnCode=self.DescrInfoForReturnCode
		return obj

class CThostFtdcVerifyFuturePasswordField(Structure):
	"""验证期货资金密码"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#交易ID
		("TID",c_int32),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getTID(self):
		return self.TID
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, AccountID=\'{12}\', Password=\'{13}\', BankAccount=\'{14}\', BankPassWord=\'{15}\', InstallID={16}, TID={17}, CurrencyID=\'{18}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), self.InstallID, self.TID, str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'InstallID':self.InstallID,'TID':self.TID,'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcVerifyFuturePasswordField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.InstallID=self.InstallID
		obj.TID=self.TID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcVerifyCustInfoField(Structure):
	"""验证客户信息"""
	_fields_ = [
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'CustomerName=\'{0}\', IdCardType=IdCardTypeType.{1}, IdentifiedCardNo=\'{2}\', CustType=CustTypeType.{3}, LongCustomerName=\'{4}\''.format(str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcVerifyCustInfoField()
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
	"""验证期货资金密码和客户信息"""
	_fields_ = [
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#币种代码
		("CurrencyID",c_char*4),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'CustomerName=\'{0}\', IdCardType=IdCardTypeType.{1}, IdentifiedCardNo=\'{2}\', CustType=CustTypeType.{3}, AccountID=\'{4}\', Password=\'{5}\', CurrencyID=\'{6}\', LongCustomerName=\'{7}\''.format(str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcVerifyFuturePasswordAndCustInfoField()
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.CurrencyID=self.CurrencyID
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcDepositResultInformField(Structure):
	"""验证期货资金密码和客户信息"""
	_fields_ = [
		#出入金流水号，该流水号为银期报盘返回的流水号
		("DepositSeqNo",c_char*15),
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者代码
		("InvestorID",c_char*13),
		#入金金额
		("Deposit",c_double),
		#请求编号
		("RequestID",c_int32),
		#返回代码
		("ReturnCode",c_char*7),
		#返回码描述
		("DescrInfoForReturnCode",c_char*129),
		]

	def getDepositSeqNo(self):
		return str(self.DepositSeqNo, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getDeposit(self):
		return self.Deposit
	def getRequestID(self):
		return self.RequestID
	def getReturnCode(self):
		return str(self.ReturnCode, 'GB2312')
	def getDescrInfoForReturnCode(self):
		return str(self.DescrInfoForReturnCode, 'GB2312')

	def __str__(self):
		return 'DepositSeqNo=\'{0}\', BrokerID=\'{1}\', InvestorID=\'{2}\', Deposit={3}, RequestID={4}, ReturnCode=\'{5}\', DescrInfoForReturnCode=\'{6}\''.format(str(self.DepositSeqNo, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.Deposit, self.RequestID, str(self.ReturnCode, 'GB2312'), str(self.DescrInfoForReturnCode, 'GB2312'))

	@property
	def __dict__(self):
		return {'DepositSeqNo':str(self.DepositSeqNo, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'Deposit':self.Deposit,'RequestID':self.RequestID,'ReturnCode':str(self.ReturnCode, 'GB2312'),'DescrInfoForReturnCode':str(self.DescrInfoForReturnCode, 'GB2312')}

	def clone(self):
		obj=CThostFtdcDepositResultInformField()
		obj.DepositSeqNo=self.DepositSeqNo
		obj.BrokerID=self.BrokerID
		obj.InvestorID=self.InvestorID
		obj.Deposit=self.Deposit
		obj.RequestID=self.RequestID
		obj.ReturnCode=self.ReturnCode
		obj.DescrInfoForReturnCode=self.DescrInfoForReturnCode
		return obj

class CThostFtdcReqSyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Message=\'{14}\', DeviceID=\'{15}\', BrokerIDByBank=\'{16}\', OperNo=\'{17}\', RequestID={18}, TID={19}'.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Message, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID)

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Message':str(self.Message, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID}

	def clone(self):
		obj=CThostFtdcReqSyncKeyField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Message=self.Message
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		return obj

class CThostFtdcRspSyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步响应"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Message=\'{14}\', DeviceID=\'{15}\', BrokerIDByBank=\'{16}\', OperNo=\'{17}\', RequestID={18}, TID={19}, ErrorID={20}, ErrorMsg=\'{21}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Message, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Message':str(self.Message, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcRspSyncKeyField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Message=self.Message
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcNotifyQueryAccountField(Structure):
	"""查询账户信息通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户类型
		("CustType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#期货公司流水号
		("FutureSerial",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#银行可用金额
		("BankUseAmount",c_double),
		#银行可取金额
		("BankFetchAmount",c_double),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getFutureSerial(self):
		return self.FutureSerial
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getBankUseAmount(self):
		return self.BankUseAmount
	def getBankFetchAmount(self):
		return self.BankFetchAmount
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', CustType=CustTypeType.{15}, BankAccount=\'{16}\', BankPassWord=\'{17}\', AccountID=\'{18}\', Password=\'{19}\', FutureSerial={20}, InstallID={21}, UserID=\'{22}\', VerifyCertNoFlag=YesNoIndicatorType.{23}, CurrencyID=\'{24}\', Digest=\'{25}\', BankAccType=BankAccTypeType.{26}, DeviceID=\'{27}\', BankSecuAccType=BankAccTypeType.{28}, BrokerIDByBank=\'{29}\', BankSecuAcc=\'{30}\', BankPwdFlag=PwdFlagType.{31}, SecuPwdFlag=PwdFlagType.{32}, OperNo=\'{33}\', RequestID={34}, TID={35}, BankUseAmount={36}, BankFetchAmount={37}, ErrorID={38}, ErrorMsg=\'{39}\', LongCustomerName=\'{40}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.FutureSerial, self.InstallID, str(self.UserID, 'GB2312'), '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.BankUseAmount, self.BankFetchAmount, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'FutureSerial':self.FutureSerial,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'BankUseAmount':self.BankUseAmount,'BankFetchAmount':self.BankFetchAmount,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcNotifyQueryAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustType=self.CustType
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.FutureSerial=self.FutureSerial
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.BankUseAmount=self.BankUseAmount
		obj.BankFetchAmount=self.BankFetchAmount
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcTransferSerialField(Structure):
	"""银期转账交易流水表"""
	_fields_ = [
		#平台流水号
		("PlateSerial",c_int32),
		#交易发起方日期
		("TradeDate",c_char*9),
		#交易日期
		("TradingDay",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#交易代码
		("TradeCode",c_char*7),
		#会话编号
		("SessionID",c_int32),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#银行帐号类型
		("BankAccType",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行流水号
		("BankSerial",c_char*13),
		#期货公司编码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#期货公司帐号类型
		("FutureAccType",c_char),
		#投资者帐号
		("AccountID",c_char*13),
		#投资者代码
		("InvestorID",c_char*13),
		#期货公司流水号
		("FutureSerial",c_int32),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#币种代码
		("CurrencyID",c_char*4),
		#交易金额
		("TradeAmount",c_double),
		#应收客户费用
		("CustFee",c_double),
		#应收期货公司费用
		("BrokerFee",c_double),
		#有效标志
		("AvailabilityFlag",c_char),
		#操作员
		("OperatorCode",c_char*17),
		#新银行帐号
		("BankNewAccount",c_char*41),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getPlateSerial(self):
		return self.PlateSerial
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getSessionID(self):
		return self.SessionID
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getFutureAccType(self):
		return FutureAccTypeType(ord(self.FutureAccType))
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getInvestorID(self):
		return str(self.InvestorID, 'GB2312')
	def getFutureSerial(self):
		return self.FutureSerial
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getTradeAmount(self):
		return self.TradeAmount
	def getCustFee(self):
		return self.CustFee
	def getBrokerFee(self):
		return self.BrokerFee
	def getAvailabilityFlag(self):
		return AvailabilityFlagType(ord(self.AvailabilityFlag))
	def getOperatorCode(self):
		return str(self.OperatorCode, 'GB2312')
	def getBankNewAccount(self):
		return str(self.BankNewAccount, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'PlateSerial={0}, TradeDate=\'{1}\', TradingDay=\'{2}\', TradeTime=\'{3}\', TradeCode=\'{4}\', SessionID={5}, BankID=\'{6}\', BankBranchID=\'{7}\', BankAccType=BankAccTypeType.{8}, BankAccount=\'{9}\', BankSerial=\'{10}\', BrokerID=\'{11}\', BrokerBranchID=\'{12}\', FutureAccType=FutureAccTypeType.{13}, AccountID=\'{14}\', InvestorID=\'{15}\', FutureSerial={16}, IdCardType=IdCardTypeType.{17}, IdentifiedCardNo=\'{18}\', CurrencyID=\'{19}\', TradeAmount={20}, CustFee={21}, BrokerFee={22}, AvailabilityFlag=AvailabilityFlagType.{23}, OperatorCode=\'{24}\', BankNewAccount=\'{25}\', ErrorID={26}, ErrorMsg=\'{27}\''.format(self.PlateSerial, str(self.TradeDate, 'GB2312'), str(self.TradingDay, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.TradeCode, 'GB2312'), self.SessionID, str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.BankAccount, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), '' if ord(self.FutureAccType) == 0 else FutureAccTypeType(ord(self.FutureAccType)).name, str(self.AccountID, 'GB2312'), str(self.InvestorID, 'GB2312'), self.FutureSerial, '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), str(self.CurrencyID, 'GB2312'), self.TradeAmount, self.CustFee, self.BrokerFee, '' if ord(self.AvailabilityFlag) == 0 else AvailabilityFlagType(ord(self.AvailabilityFlag)).name, str(self.OperatorCode, 'GB2312'), str(self.BankNewAccount, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'PlateSerial':self.PlateSerial,'TradeDate':str(self.TradeDate, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'TradeCode':str(self.TradeCode, 'GB2312'),'SessionID':self.SessionID,'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'FutureAccType':'' if ord(self.FutureAccType) == 0 else FutureAccTypeType(ord(self.FutureAccType)).name,'AccountID':str(self.AccountID, 'GB2312'),'InvestorID':str(self.InvestorID, 'GB2312'),'FutureSerial':self.FutureSerial,'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'TradeAmount':self.TradeAmount,'CustFee':self.CustFee,'BrokerFee':self.BrokerFee,'AvailabilityFlag':'' if ord(self.AvailabilityFlag) == 0 else AvailabilityFlagType(ord(self.AvailabilityFlag)).name,'OperatorCode':str(self.OperatorCode, 'GB2312'),'BankNewAccount':str(self.BankNewAccount, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTransferSerialField()
		obj.PlateSerial=self.PlateSerial
		obj.TradeDate=self.TradeDate
		obj.TradingDay=self.TradingDay
		obj.TradeTime=self.TradeTime
		obj.TradeCode=self.TradeCode
		obj.SessionID=self.SessionID
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BankAccType=self.BankAccType
		obj.BankAccount=self.BankAccount
		obj.BankSerial=self.BankSerial
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.FutureAccType=self.FutureAccType
		obj.AccountID=self.AccountID
		obj.InvestorID=self.InvestorID
		obj.FutureSerial=self.FutureSerial
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CurrencyID=self.CurrencyID
		obj.TradeAmount=self.TradeAmount
		obj.CustFee=self.CustFee
		obj.BrokerFee=self.BrokerFee
		obj.AvailabilityFlag=self.AvailabilityFlag
		obj.OperatorCode=self.OperatorCode
		obj.BankNewAccount=self.BankNewAccount
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcQryTransferSerialField(Structure):
	"""请求查询转帐流水"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#银行编码
		("BankID",c_char*4),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', BankID=\'{2}\', CurrencyID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.BankID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryTransferSerialField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.BankID=self.BankID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcNotifyFutureSignInField(Structure):
	"""期商签到通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#PIN密钥
		("PinKey",c_char*129),
		#MAC密钥
		("MacKey",c_char*129),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getPinKey(self):
		return str(self.PinKey, 'GB2312')
	def getMacKey(self):
		return str(self.MacKey, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}, ErrorID={21}, ErrorMsg=\'{22}\', PinKey=\'{23}\', MacKey=\'{24}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.PinKey, 'GB2312'), str(self.MacKey, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'PinKey':str(self.PinKey, 'GB2312'),'MacKey':str(self.MacKey, 'GB2312')}

	def clone(self):
		obj=CThostFtdcNotifyFutureSignInField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.PinKey=self.PinKey
		obj.MacKey=self.MacKey
		return obj

class CThostFtdcNotifyFutureSignOutField(Structure):
	"""期商签退通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#摘要
		("Digest",c_char*36),
		#币种代码
		("CurrencyID",c_char*4),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Digest=\'{14}\', CurrencyID=\'{15}\', DeviceID=\'{16}\', BrokerIDByBank=\'{17}\', OperNo=\'{18}\', RequestID={19}, TID={20}, ErrorID={21}, ErrorMsg=\'{22}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Digest, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcNotifyFutureSignOutField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Digest=self.Digest
		obj.CurrencyID=self.CurrencyID
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcNotifySyncKeyField(Structure):
	"""交易核心向银期报盘发出密钥同步处理结果的通知"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#安装编号
		("InstallID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#交易核心给银期报盘的消息
		("Message",c_char*129),
		#渠道标志
		("DeviceID",c_char*3),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易柜员
		("OperNo",c_char*17),
		#请求编号
		("RequestID",c_int32),
		#交易ID
		("TID",c_int32),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getInstallID(self):
		return self.InstallID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getMessage(self):
		return str(self.Message, 'GB2312')
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getRequestID(self):
		return self.RequestID
	def getTID(self):
		return self.TID
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, InstallID={12}, UserID=\'{13}\', Message=\'{14}\', DeviceID=\'{15}\', BrokerIDByBank=\'{16}\', OperNo=\'{17}\', RequestID={18}, TID={19}, ErrorID={20}, ErrorMsg=\'{21}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, self.InstallID, str(self.UserID, 'GB2312'), str(self.Message, 'GB2312'), str(self.DeviceID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), str(self.OperNo, 'GB2312'), self.RequestID, self.TID, self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'InstallID':self.InstallID,'UserID':str(self.UserID, 'GB2312'),'Message':str(self.Message, 'GB2312'),'DeviceID':str(self.DeviceID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'OperNo':str(self.OperNo, 'GB2312'),'RequestID':self.RequestID,'TID':self.TID,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcNotifySyncKeyField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.InstallID=self.InstallID
		obj.UserID=self.UserID
		obj.Message=self.Message
		obj.DeviceID=self.DeviceID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.OperNo=self.OperNo
		obj.RequestID=self.RequestID
		obj.TID=self.TID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcQryAccountregisterField(Structure):
	"""请求查询银期签约关系"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', BankID=\'{2}\', BankBranchID=\'{3}\', CurrencyID=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryAccountregisterField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcAccountregisterField(Structure):
	"""客户开销户信息表"""
	_fields_ = [
		#交易日期
		("TradeDay",c_char*9),
		#银行编码
		("BankID",c_char*4),
		#银行分支机构编码
		("BankBranchID",c_char*5),
		#银行帐号
		("BankAccount",c_char*41),
		#期货公司编码
		("BrokerID",c_char*11),
		#期货公司分支机构编码
		("BrokerBranchID",c_char*31),
		#投资者帐号
		("AccountID",c_char*13),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#客户姓名
		("CustomerName",c_char*51),
		#币种代码
		("CurrencyID",c_char*4),
		#开销户类别
		("OpenOrDestroy",c_char),
		#签约日期
		("RegDate",c_char*9),
		#解约日期
		("OutDate",c_char*9),
		#交易ID
		("TID",c_int32),
		#客户类型
		("CustType",c_char),
		#银行帐号类型
		("BankAccType",c_char),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeDay(self):
		return str(self.TradeDay, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getOpenOrDestroy(self):
		return OpenOrDestroyType(ord(self.OpenOrDestroy))
	def getRegDate(self):
		return str(self.RegDate, 'GB2312')
	def getOutDate(self):
		return str(self.OutDate, 'GB2312')
	def getTID(self):
		return self.TID
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeDay=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BankAccount=\'{3}\', BrokerID=\'{4}\', BrokerBranchID=\'{5}\', AccountID=\'{6}\', IdCardType=IdCardTypeType.{7}, IdentifiedCardNo=\'{8}\', CustomerName=\'{9}\', CurrencyID=\'{10}\', OpenOrDestroy=OpenOrDestroyType.{11}, RegDate=\'{12}\', OutDate=\'{13}\', TID={14}, CustType=CustTypeType.{15}, BankAccType=BankAccTypeType.{16}, LongCustomerName=\'{17}\''.format(str(self.TradeDay, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BankAccount, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.AccountID, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), str(self.CustomerName, 'GB2312'), str(self.CurrencyID, 'GB2312'), '' if ord(self.OpenOrDestroy) == 0 else OpenOrDestroyType(ord(self.OpenOrDestroy)).name, str(self.RegDate, 'GB2312'), str(self.OutDate, 'GB2312'), self.TID, '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeDay':str(self.TradeDay, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BankAccount':str(self.BankAccount, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'CustomerName':str(self.CustomerName, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'OpenOrDestroy':'' if ord(self.OpenOrDestroy) == 0 else OpenOrDestroyType(ord(self.OpenOrDestroy)).name,'RegDate':str(self.RegDate, 'GB2312'),'OutDate':str(self.OutDate, 'GB2312'),'TID':self.TID,'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcAccountregisterField()
		obj.TradeDay=self.TradeDay
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BankAccount=self.BankAccount
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.AccountID=self.AccountID
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.CustomerName=self.CustomerName
		obj.CurrencyID=self.CurrencyID
		obj.OpenOrDestroy=self.OpenOrDestroy
		obj.RegDate=self.RegDate
		obj.OutDate=self.OutDate
		obj.TID=self.TID
		obj.CustType=self.CustType
		obj.BankAccType=self.BankAccType
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcOpenAccountField(Structure):
	"""银期开户信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', AccountID=\'{27}\', Password=\'{28}\', InstallID={29}, VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', CashExchangeCode=CashExchangeCodeType.{32}, Digest=\'{33}\', BankAccType=BankAccTypeType.{34}, DeviceID=\'{35}\', BankSecuAccType=BankAccTypeType.{36}, BrokerIDByBank=\'{37}\', BankSecuAcc=\'{38}\', BankPwdFlag=PwdFlagType.{39}, SecuPwdFlag=PwdFlagType.{40}, OperNo=\'{41}\', TID={42}, UserID=\'{43}\', ErrorID={44}, ErrorMsg=\'{45}\', LongCustomerName=\'{46}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), '' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name, str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.TID, str(self.UserID, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'CashExchangeCode':'' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name,'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'TID':self.TID,'UserID':str(self.UserID, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcOpenAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.CashExchangeCode=self.CashExchangeCode
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.TID=self.TID
		obj.UserID=self.UserID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcCancelAccountField(Structure):
	"""银期销户信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#汇钞标志
		("CashExchangeCode",c_char),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#渠道标志
		("DeviceID",c_char*3),
		#期货单位帐号类型
		("BankSecuAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#期货单位帐号
		("BankSecuAcc",c_char*41),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易柜员
		("OperNo",c_char*17),
		#交易ID
		("TID",c_int32),
		#用户标识
		("UserID",c_char*16),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getCashExchangeCode(self):
		return CashExchangeCodeType(ord(self.CashExchangeCode))
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getDeviceID(self):
		return str(self.DeviceID, 'GB2312')
	def getBankSecuAccType(self):
		return BankAccTypeType(ord(self.BankSecuAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankSecuAcc(self):
		return str(self.BankSecuAcc, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getOperNo(self):
		return str(self.OperNo, 'GB2312')
	def getTID(self):
		return self.TID
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', AccountID=\'{27}\', Password=\'{28}\', InstallID={29}, VerifyCertNoFlag=YesNoIndicatorType.{30}, CurrencyID=\'{31}\', CashExchangeCode=CashExchangeCodeType.{32}, Digest=\'{33}\', BankAccType=BankAccTypeType.{34}, DeviceID=\'{35}\', BankSecuAccType=BankAccTypeType.{36}, BrokerIDByBank=\'{37}\', BankSecuAcc=\'{38}\', BankPwdFlag=PwdFlagType.{39}, SecuPwdFlag=PwdFlagType.{40}, OperNo=\'{41}\', TID={42}, UserID=\'{43}\', ErrorID={44}, ErrorMsg=\'{45}\', LongCustomerName=\'{46}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), '' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name, str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.DeviceID, 'GB2312'), '' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name, str(self.BrokerIDByBank, 'GB2312'), str(self.BankSecuAcc, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, str(self.OperNo, 'GB2312'), self.TID, str(self.UserID, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'CashExchangeCode':'' if ord(self.CashExchangeCode) == 0 else CashExchangeCodeType(ord(self.CashExchangeCode)).name,'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'DeviceID':str(self.DeviceID, 'GB2312'),'BankSecuAccType':'' if ord(self.BankSecuAccType) == 0 else BankAccTypeType(ord(self.BankSecuAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankSecuAcc':str(self.BankSecuAcc, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'OperNo':str(self.OperNo, 'GB2312'),'TID':self.TID,'UserID':str(self.UserID, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcCancelAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.CashExchangeCode=self.CashExchangeCode
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.DeviceID=self.DeviceID
		obj.BankSecuAccType=self.BankSecuAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankSecuAcc=self.BankSecuAcc
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.OperNo=self.OperNo
		obj.TID=self.TID
		obj.UserID=self.UserID
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcChangeAccountField(Structure):
	"""银期变更银行账号信息"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*51),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#新银行帐号
		("NewBankAccount",c_char*41),
		#新银行密码
		("NewBankPassWord",c_char*41),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#银行帐号类型
		("BankAccType",c_char),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#银行密码标志
		("BankPwdFlag",c_char),
		#期货资金密码核对标志
		("SecuPwdFlag",c_char),
		#交易ID
		("TID",c_int32),
		#摘要
		("Digest",c_char*36),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		#长客户姓名
		("LongCustomerName",c_char*161),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getNewBankAccount(self):
		return str(self.NewBankAccount, 'GB2312')
	def getNewBankPassWord(self):
		return str(self.NewBankPassWord, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getBankPwdFlag(self):
		return PwdFlagType(ord(self.BankPwdFlag))
	def getSecuPwdFlag(self):
		return PwdFlagType(ord(self.SecuPwdFlag))
	def getTID(self):
		return self.TID
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')
	def getLongCustomerName(self):
		return str(self.LongCustomerName, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', NewBankAccount=\'{27}\', NewBankPassWord=\'{28}\', AccountID=\'{29}\', Password=\'{30}\', BankAccType=BankAccTypeType.{31}, InstallID={32}, VerifyCertNoFlag=YesNoIndicatorType.{33}, CurrencyID=\'{34}\', BrokerIDByBank=\'{35}\', BankPwdFlag=PwdFlagType.{36}, SecuPwdFlag=PwdFlagType.{37}, TID={38}, Digest=\'{39}\', ErrorID={40}, ErrorMsg=\'{41}\', LongCustomerName=\'{42}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), str(self.NewBankAccount, 'GB2312'), str(self.NewBankPassWord, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.BrokerIDByBank, 'GB2312'), '' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name, '' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name, self.TID, str(self.Digest, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'), str(self.LongCustomerName, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'NewBankAccount':str(self.NewBankAccount, 'GB2312'),'NewBankPassWord':str(self.NewBankPassWord, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'BankPwdFlag':'' if ord(self.BankPwdFlag) == 0 else PwdFlagType(ord(self.BankPwdFlag)).name,'SecuPwdFlag':'' if ord(self.SecuPwdFlag) == 0 else PwdFlagType(ord(self.SecuPwdFlag)).name,'TID':self.TID,'Digest':str(self.Digest, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312'),'LongCustomerName':str(self.LongCustomerName, 'GB2312')}

	def clone(self):
		obj=CThostFtdcChangeAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.NewBankAccount=self.NewBankAccount
		obj.NewBankPassWord=self.NewBankPassWord
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.BankAccType=self.BankAccType
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.BankPwdFlag=self.BankPwdFlag
		obj.SecuPwdFlag=self.SecuPwdFlag
		obj.TID=self.TID
		obj.Digest=self.Digest
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		obj.LongCustomerName=self.LongCustomerName
		return obj

class CThostFtdcSecAgentACIDMapField(Structure):
	"""二级代理操作员银期权限"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#资金账户
		("AccountID",c_char*13),
		#币种
		("CurrencyID",c_char*4),
		#境外中介机构资金帐号
		("BrokerSecAgentID",c_char*13),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getBrokerSecAgentID(self):
		return str(self.BrokerSecAgentID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', AccountID=\'{2}\', CurrencyID=\'{3}\', BrokerSecAgentID=\'{4}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'), str(self.BrokerSecAgentID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312'),'BrokerSecAgentID':str(self.BrokerSecAgentID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcSecAgentACIDMapField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		obj.BrokerSecAgentID=self.BrokerSecAgentID
		return obj

class CThostFtdcQrySecAgentACIDMapField(Structure):
	"""二级代理操作员银期权限查询"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#资金账户
		("AccountID",c_char*13),
		#币种
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', AccountID=\'{2}\', CurrencyID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.AccountID, 'GB2312'), str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQrySecAgentACIDMapField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.AccountID=self.AccountID
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcUserRightsAssignField(Structure):
	"""灾备中心交易权限"""
	_fields_ = [
		#应用单元代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#交易中心代码
		("DRIdentityID",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getDRIdentityID(self):
		return self.DRIdentityID

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', DRIdentityID={2}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), self.DRIdentityID)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'DRIdentityID':self.DRIdentityID}

	def clone(self):
		obj=CThostFtdcUserRightsAssignField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.DRIdentityID=self.DRIdentityID
		return obj

class CThostFtdcBrokerUserRightAssignField(Structure):
	"""经济公司是否有在本标示的交易权限"""
	_fields_ = [
		#应用单元代码
		("BrokerID",c_char*11),
		#交易中心代码
		("DRIdentityID",c_int32),
		#能否交易
		("Tradeable",c_int32),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getDRIdentityID(self):
		return self.DRIdentityID
	def getTradeable(self):
		return self.Tradeable

	def __str__(self):
		return 'BrokerID=\'{0}\', DRIdentityID={1}, Tradeable={2}'.format(str(self.BrokerID, 'GB2312'), self.DRIdentityID, self.Tradeable)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'DRIdentityID':self.DRIdentityID,'Tradeable':self.Tradeable}

	def clone(self):
		obj=CThostFtdcBrokerUserRightAssignField()
		obj.BrokerID=self.BrokerID
		obj.DRIdentityID=self.DRIdentityID
		obj.Tradeable=self.Tradeable
		return obj

class CThostFtdcDRTransferField(Structure):
	"""灾备交易转换报文"""
	_fields_ = [
		#原交易中心代码
		("OrigDRIdentityID",c_int32),
		#目标交易中心代码
		("DestDRIdentityID",c_int32),
		#原应用单元代码
		("OrigBrokerID",c_char*11),
		#目标易用单元代码
		("DestBrokerID",c_char*11),
		]

	def getOrigDRIdentityID(self):
		return self.OrigDRIdentityID
	def getDestDRIdentityID(self):
		return self.DestDRIdentityID
	def getOrigBrokerID(self):
		return str(self.OrigBrokerID, 'GB2312')
	def getDestBrokerID(self):
		return str(self.DestBrokerID, 'GB2312')

	def __str__(self):
		return 'OrigDRIdentityID={0}, DestDRIdentityID={1}, OrigBrokerID=\'{2}\', DestBrokerID=\'{3}\''.format(self.OrigDRIdentityID, self.DestDRIdentityID, str(self.OrigBrokerID, 'GB2312'), str(self.DestBrokerID, 'GB2312'))

	@property
	def __dict__(self):
		return {'OrigDRIdentityID':self.OrigDRIdentityID,'DestDRIdentityID':self.DestDRIdentityID,'OrigBrokerID':str(self.OrigBrokerID, 'GB2312'),'DestBrokerID':str(self.DestBrokerID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcDRTransferField()
		obj.OrigDRIdentityID=self.OrigDRIdentityID
		obj.DestDRIdentityID=self.DestDRIdentityID
		obj.OrigBrokerID=self.OrigBrokerID
		obj.DestBrokerID=self.DestBrokerID
		return obj

class CThostFtdcFensUserInfoField(Structure):
	"""Fens用户信息"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#登录模式
		("LoginMode",c_char),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getLoginMode(self):
		return LoginModeType(ord(self.LoginMode))

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', LoginMode=LoginModeType.{2}'.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), '' if ord(self.LoginMode) == 0 else LoginModeType(ord(self.LoginMode)).name)

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'LoginMode':'' if ord(self.LoginMode) == 0 else LoginModeType(ord(self.LoginMode)).name}

	def clone(self):
		obj=CThostFtdcFensUserInfoField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.LoginMode=self.LoginMode
		return obj

class CThostFtdcCurrTransferIdentityField(Structure):
	"""当前银期所属交易中心"""
	_fields_ = [
		#交易中心代码
		("IdentityID",c_int32),
		]

	def getIdentityID(self):
		return self.IdentityID

	def __str__(self):
		return 'IdentityID={0}'.format(self.IdentityID)

	@property
	def __dict__(self):
		return {'IdentityID':self.IdentityID}

	def clone(self):
		obj=CThostFtdcCurrTransferIdentityField()
		obj.IdentityID=self.IdentityID
		return obj

class CThostFtdcLoginForbiddenUserField(Structure):
	"""禁止登录用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		#IP地址
		("IPAddress",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')
	def getIPAddress(self):
		return str(self.IPAddress, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\', IPAddress=\'{2}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'), str(self.IPAddress, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312'),'IPAddress':str(self.IPAddress, 'GB2312')}

	def clone(self):
		obj=CThostFtdcLoginForbiddenUserField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		obj.IPAddress=self.IPAddress
		return obj

class CThostFtdcQryLoginForbiddenUserField(Structure):
	"""查询禁止登录用户"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#用户代码
		("UserID",c_char*16),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getUserID(self):
		return str(self.UserID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', UserID=\'{1}\''.format(str(self.BrokerID, 'GB2312'), str(self.UserID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'UserID':str(self.UserID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcQryLoginForbiddenUserField()
		obj.BrokerID=self.BrokerID
		obj.UserID=self.UserID
		return obj

class CThostFtdcMulticastGroupInfoField(Structure):
	"""UDP组播组信息"""
	_fields_ = [
		#组播组IP地址
		("GroupIP",c_char*16),
		#组播组IP端口
		("GroupPort",c_int32),
		#源地址
		("SourceIP",c_char*16),
		]

	def getGroupIP(self):
		return str(self.GroupIP, 'GB2312')
	def getGroupPort(self):
		return self.GroupPort
	def getSourceIP(self):
		return str(self.SourceIP, 'GB2312')

	def __str__(self):
		return 'GroupIP=\'{0}\', GroupPort={1}, SourceIP=\'{2}\''.format(str(self.GroupIP, 'GB2312'), self.GroupPort, str(self.SourceIP, 'GB2312'))

	@property
	def __dict__(self):
		return {'GroupIP':str(self.GroupIP, 'GB2312'),'GroupPort':self.GroupPort,'SourceIP':str(self.SourceIP, 'GB2312')}

	def clone(self):
		obj=CThostFtdcMulticastGroupInfoField()
		obj.GroupIP=self.GroupIP
		obj.GroupPort=self.GroupPort
		obj.SourceIP=self.SourceIP
		return obj

class CThostFtdcTradingAccountReserveField(Structure):
	"""资金账户基本准备金"""
	_fields_ = [
		#经纪公司代码
		("BrokerID",c_char*11),
		#投资者帐号
		("AccountID",c_char*13),
		#基本准备金
		("Reserve",c_double),
		#币种代码
		("CurrencyID",c_char*4),
		]

	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getReserve(self):
		return self.Reserve
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')

	def __str__(self):
		return 'BrokerID=\'{0}\', AccountID=\'{1}\', Reserve={2}, CurrencyID=\'{3}\''.format(str(self.BrokerID, 'GB2312'), str(self.AccountID, 'GB2312'), self.Reserve, str(self.CurrencyID, 'GB2312'))

	@property
	def __dict__(self):
		return {'BrokerID':str(self.BrokerID, 'GB2312'),'AccountID':str(self.AccountID, 'GB2312'),'Reserve':self.Reserve,'CurrencyID':str(self.CurrencyID, 'GB2312')}

	def clone(self):
		obj=CThostFtdcTradingAccountReserveField()
		obj.BrokerID=self.BrokerID
		obj.AccountID=self.AccountID
		obj.Reserve=self.Reserve
		obj.CurrencyID=self.CurrencyID
		return obj

class CThostFtdcReserveOpenAccountConfirmField(Structure):
	"""银期预约开户确认请求"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*161),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易ID
		("TID",c_int32),
		#投资者帐号
		("AccountID",c_char*13),
		#期货密码
		("Password",c_char*41),
		#预约开户银行流水号
		("BankReserveOpenSeq",c_char*13),
		#预约开户日期
		("BookDate",c_char*9),
		#预约开户验证密码
		("BookPsw",c_char*41),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getTID(self):
		return self.TID
	def getAccountID(self):
		return str(self.AccountID, 'GB2312')
	def getPassword(self):
		return str(self.Password, 'GB2312')
	def getBankReserveOpenSeq(self):
		return str(self.BankReserveOpenSeq, 'GB2312')
	def getBookDate(self):
		return str(self.BookDate, 'GB2312')
	def getBookPsw(self):
		return str(self.BookPsw, 'GB2312')
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', InstallID={27}, VerifyCertNoFlag=YesNoIndicatorType.{28}, CurrencyID=\'{29}\', Digest=\'{30}\', BankAccType=BankAccTypeType.{31}, BrokerIDByBank=\'{32}\', TID={33}, AccountID=\'{34}\', Password=\'{35}\', BankReserveOpenSeq=\'{36}\', BookDate=\'{37}\', BookPsw=\'{38}\', ErrorID={39}, ErrorMsg=\'{40}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.BrokerIDByBank, 'GB2312'), self.TID, str(self.AccountID, 'GB2312'), str(self.Password, 'GB2312'), str(self.BankReserveOpenSeq, 'GB2312'), str(self.BookDate, 'GB2312'), str(self.BookPsw, 'GB2312'), self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'TID':self.TID,'AccountID':str(self.AccountID, 'GB2312'),'Password':str(self.Password, 'GB2312'),'BankReserveOpenSeq':str(self.BankReserveOpenSeq, 'GB2312'),'BookDate':str(self.BookDate, 'GB2312'),'BookPsw':str(self.BookPsw, 'GB2312'),'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReserveOpenAccountConfirmField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.TID=self.TID
		obj.AccountID=self.AccountID
		obj.Password=self.Password
		obj.BankReserveOpenSeq=self.BankReserveOpenSeq
		obj.BookDate=self.BookDate
		obj.BookPsw=self.BookPsw
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

class CThostFtdcReserveOpenAccountField(Structure):
	"""银期预约开户"""
	_fields_ = [
		#业务功能码
		("TradeCode",c_char*7),
		#银行代码
		("BankID",c_char*4),
		#银行分支机构代码
		("BankBranchID",c_char*5),
		#期商代码
		("BrokerID",c_char*11),
		#期商分支机构代码
		("BrokerBranchID",c_char*31),
		#交易日期
		("TradeDate",c_char*9),
		#交易时间
		("TradeTime",c_char*9),
		#银行流水号
		("BankSerial",c_char*13),
		#交易系统日期 
		("TradingDay",c_char*9),
		#银期平台消息流水号
		("PlateSerial",c_int32),
		#最后分片标志
		("LastFragment",c_char),
		#会话号
		("SessionID",c_int32),
		#客户姓名
		("CustomerName",c_char*161),
		#证件类型
		("IdCardType",c_char),
		#证件号码
		("IdentifiedCardNo",c_char*51),
		#性别
		("Gender",c_char),
		#国家代码
		("CountryCode",c_char*21),
		#客户类型
		("CustType",c_char),
		#地址
		("Address",c_char*101),
		#邮编
		("ZipCode",c_char*7),
		#电话号码
		("Telephone",c_char*41),
		#手机
		("MobilePhone",c_char*21),
		#传真
		("Fax",c_char*41),
		#电子邮件
		("EMail",c_char*41),
		#资金账户状态
		("MoneyAccountStatus",c_char),
		#银行帐号
		("BankAccount",c_char*41),
		#银行密码
		("BankPassWord",c_char*41),
		#安装编号
		("InstallID",c_int32),
		#验证客户证件号码标志
		("VerifyCertNoFlag",c_char),
		#币种代码
		("CurrencyID",c_char*4),
		#摘要
		("Digest",c_char*36),
		#银行帐号类型
		("BankAccType",c_char),
		#期货公司银行编码
		("BrokerIDByBank",c_char*33),
		#交易ID
		("TID",c_int32),
		#预约开户状态
		("ReserveOpenAccStas",c_char),
		#错误代码
		("ErrorID",c_int32),
		#错误信息
		("ErrorMsg",c_char*81),
		]

	def getTradeCode(self):
		return str(self.TradeCode, 'GB2312')
	def getBankID(self):
		return str(self.BankID, 'GB2312')
	def getBankBranchID(self):
		return str(self.BankBranchID, 'GB2312')
	def getBrokerID(self):
		return str(self.BrokerID, 'GB2312')
	def getBrokerBranchID(self):
		return str(self.BrokerBranchID, 'GB2312')
	def getTradeDate(self):
		return str(self.TradeDate, 'GB2312')
	def getTradeTime(self):
		return str(self.TradeTime, 'GB2312')
	def getBankSerial(self):
		return str(self.BankSerial, 'GB2312')
	def getTradingDay(self):
		return str(self.TradingDay, 'GB2312')
	def getPlateSerial(self):
		return self.PlateSerial
	def getLastFragment(self):
		return LastFragmentType(ord(self.LastFragment))
	def getSessionID(self):
		return self.SessionID
	def getCustomerName(self):
		return str(self.CustomerName, 'GB2312')
	def getIdCardType(self):
		return IdCardTypeType(ord(self.IdCardType))
	def getIdentifiedCardNo(self):
		return str(self.IdentifiedCardNo, 'GB2312')
	def getGender(self):
		return GenderType(ord(self.Gender))
	def getCountryCode(self):
		return str(self.CountryCode, 'GB2312')
	def getCustType(self):
		return CustTypeType(ord(self.CustType))
	def getAddress(self):
		return str(self.Address, 'GB2312')
	def getZipCode(self):
		return str(self.ZipCode, 'GB2312')
	def getTelephone(self):
		return str(self.Telephone, 'GB2312')
	def getMobilePhone(self):
		return str(self.MobilePhone, 'GB2312')
	def getFax(self):
		return str(self.Fax, 'GB2312')
	def getEMail(self):
		return str(self.EMail, 'GB2312')
	def getMoneyAccountStatus(self):
		return MoneyAccountStatusType(ord(self.MoneyAccountStatus))
	def getBankAccount(self):
		return str(self.BankAccount, 'GB2312')
	def getBankPassWord(self):
		return str(self.BankPassWord, 'GB2312')
	def getInstallID(self):
		return self.InstallID
	def getVerifyCertNoFlag(self):
		return YesNoIndicatorType(ord(self.VerifyCertNoFlag))
	def getCurrencyID(self):
		return str(self.CurrencyID, 'GB2312')
	def getDigest(self):
		return str(self.Digest, 'GB2312')
	def getBankAccType(self):
		return BankAccTypeType(ord(self.BankAccType))
	def getBrokerIDByBank(self):
		return str(self.BrokerIDByBank, 'GB2312')
	def getTID(self):
		return self.TID
	def getReserveOpenAccStas(self):
		return ReserveOpenAccStasType(ord(self.ReserveOpenAccStas))
	def getErrorID(self):
		return self.ErrorID
	def getErrorMsg(self):
		return str(self.ErrorMsg, 'GB2312')

	def __str__(self):
		return 'TradeCode=\'{0}\', BankID=\'{1}\', BankBranchID=\'{2}\', BrokerID=\'{3}\', BrokerBranchID=\'{4}\', TradeDate=\'{5}\', TradeTime=\'{6}\', BankSerial=\'{7}\', TradingDay=\'{8}\', PlateSerial={9}, LastFragment=LastFragmentType.{10}, SessionID={11}, CustomerName=\'{12}\', IdCardType=IdCardTypeType.{13}, IdentifiedCardNo=\'{14}\', Gender=GenderType.{15}, CountryCode=\'{16}\', CustType=CustTypeType.{17}, Address=\'{18}\', ZipCode=\'{19}\', Telephone=\'{20}\', MobilePhone=\'{21}\', Fax=\'{22}\', EMail=\'{23}\', MoneyAccountStatus=MoneyAccountStatusType.{24}, BankAccount=\'{25}\', BankPassWord=\'{26}\', InstallID={27}, VerifyCertNoFlag=YesNoIndicatorType.{28}, CurrencyID=\'{29}\', Digest=\'{30}\', BankAccType=BankAccTypeType.{31}, BrokerIDByBank=\'{32}\', TID={33}, ReserveOpenAccStas=ReserveOpenAccStasType.{34}, ErrorID={35}, ErrorMsg=\'{36}\''.format(str(self.TradeCode, 'GB2312'), str(self.BankID, 'GB2312'), str(self.BankBranchID, 'GB2312'), str(self.BrokerID, 'GB2312'), str(self.BrokerBranchID, 'GB2312'), str(self.TradeDate, 'GB2312'), str(self.TradeTime, 'GB2312'), str(self.BankSerial, 'GB2312'), str(self.TradingDay, 'GB2312'), self.PlateSerial, '' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name, self.SessionID, str(self.CustomerName, 'GB2312'), '' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name, str(self.IdentifiedCardNo, 'GB2312'), '' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name, str(self.CountryCode, 'GB2312'), '' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name, str(self.Address, 'GB2312'), str(self.ZipCode, 'GB2312'), str(self.Telephone, 'GB2312'), str(self.MobilePhone, 'GB2312'), str(self.Fax, 'GB2312'), str(self.EMail, 'GB2312'), '' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name, str(self.BankAccount, 'GB2312'), str(self.BankPassWord, 'GB2312'), self.InstallID, '' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name, str(self.CurrencyID, 'GB2312'), str(self.Digest, 'GB2312'), '' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name, str(self.BrokerIDByBank, 'GB2312'), self.TID, '' if ord(self.ReserveOpenAccStas) == 0 else ReserveOpenAccStasType(ord(self.ReserveOpenAccStas)).name, self.ErrorID, str(self.ErrorMsg, 'GB2312'))

	@property
	def __dict__(self):
		return {'TradeCode':str(self.TradeCode, 'GB2312'),'BankID':str(self.BankID, 'GB2312'),'BankBranchID':str(self.BankBranchID, 'GB2312'),'BrokerID':str(self.BrokerID, 'GB2312'),'BrokerBranchID':str(self.BrokerBranchID, 'GB2312'),'TradeDate':str(self.TradeDate, 'GB2312'),'TradeTime':str(self.TradeTime, 'GB2312'),'BankSerial':str(self.BankSerial, 'GB2312'),'TradingDay':str(self.TradingDay, 'GB2312'),'PlateSerial':self.PlateSerial,'LastFragment':'' if ord(self.LastFragment) == 0 else LastFragmentType(ord(self.LastFragment)).name,'SessionID':self.SessionID,'CustomerName':str(self.CustomerName, 'GB2312'),'IdCardType':'' if ord(self.IdCardType) == 0 else IdCardTypeType(ord(self.IdCardType)).name,'IdentifiedCardNo':str(self.IdentifiedCardNo, 'GB2312'),'Gender':'' if ord(self.Gender) == 0 else GenderType(ord(self.Gender)).name,'CountryCode':str(self.CountryCode, 'GB2312'),'CustType':'' if ord(self.CustType) == 0 else CustTypeType(ord(self.CustType)).name,'Address':str(self.Address, 'GB2312'),'ZipCode':str(self.ZipCode, 'GB2312'),'Telephone':str(self.Telephone, 'GB2312'),'MobilePhone':str(self.MobilePhone, 'GB2312'),'Fax':str(self.Fax, 'GB2312'),'EMail':str(self.EMail, 'GB2312'),'MoneyAccountStatus':'' if ord(self.MoneyAccountStatus) == 0 else MoneyAccountStatusType(ord(self.MoneyAccountStatus)).name,'BankAccount':str(self.BankAccount, 'GB2312'),'BankPassWord':str(self.BankPassWord, 'GB2312'),'InstallID':self.InstallID,'VerifyCertNoFlag':'' if ord(self.VerifyCertNoFlag) == 0 else YesNoIndicatorType(ord(self.VerifyCertNoFlag)).name,'CurrencyID':str(self.CurrencyID, 'GB2312'),'Digest':str(self.Digest, 'GB2312'),'BankAccType':'' if ord(self.BankAccType) == 0 else BankAccTypeType(ord(self.BankAccType)).name,'BrokerIDByBank':str(self.BrokerIDByBank, 'GB2312'),'TID':self.TID,'ReserveOpenAccStas':'' if ord(self.ReserveOpenAccStas) == 0 else ReserveOpenAccStasType(ord(self.ReserveOpenAccStas)).name,'ErrorID':self.ErrorID,'ErrorMsg':str(self.ErrorMsg, 'GB2312')}

	def clone(self):
		obj=CThostFtdcReserveOpenAccountField()
		obj.TradeCode=self.TradeCode
		obj.BankID=self.BankID
		obj.BankBranchID=self.BankBranchID
		obj.BrokerID=self.BrokerID
		obj.BrokerBranchID=self.BrokerBranchID
		obj.TradeDate=self.TradeDate
		obj.TradeTime=self.TradeTime
		obj.BankSerial=self.BankSerial
		obj.TradingDay=self.TradingDay
		obj.PlateSerial=self.PlateSerial
		obj.LastFragment=self.LastFragment
		obj.SessionID=self.SessionID
		obj.CustomerName=self.CustomerName
		obj.IdCardType=self.IdCardType
		obj.IdentifiedCardNo=self.IdentifiedCardNo
		obj.Gender=self.Gender
		obj.CountryCode=self.CountryCode
		obj.CustType=self.CustType
		obj.Address=self.Address
		obj.ZipCode=self.ZipCode
		obj.Telephone=self.Telephone
		obj.MobilePhone=self.MobilePhone
		obj.Fax=self.Fax
		obj.EMail=self.EMail
		obj.MoneyAccountStatus=self.MoneyAccountStatus
		obj.BankAccount=self.BankAccount
		obj.BankPassWord=self.BankPassWord
		obj.InstallID=self.InstallID
		obj.VerifyCertNoFlag=self.VerifyCertNoFlag
		obj.CurrencyID=self.CurrencyID
		obj.Digest=self.Digest
		obj.BankAccType=self.BankAccType
		obj.BrokerIDByBank=self.BrokerIDByBank
		obj.TID=self.TID
		obj.ReserveOpenAccStas=self.ReserveOpenAccStas
		obj.ErrorID=self.ErrorID
		obj.ErrorMsg=self.ErrorMsg
		return obj

