
from py_ctp.ctp_struct import *
import os
import sys
import platform

def isWindowsSystem():
	return 'Windows' in platform.system()

class Quote:

	def __init__(self):

		# make log dir for api log
		logdir = os.path.join(sys.path[0], "log")
		if not os.path.exists(logdir):
			os.mkdir(logdir)

		dlldir = os.path.join(os.path.split(os.path.realpath(__file__))[0], "dll")
		if not os.path.exists(dlldir):
			print('缺少DLL借口文件')
			return

		# change work directory
		cur_path = os.getcwd()
		os.chdir(dlldir)

		if isWindowsSystem():
			self.h = CDLL("ctp_Quote.dll")
		else:
			self.h = cdll.LoadLibrary("ctp_quote.so")

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
		self.h.GetTradingDay.argtypes = [c_void_p]
		self.h.GetTradingDay.restype = c_void_p
		self.h.RegisterFront.argtypes = [c_void_p , c_char_p]
		self.h.RegisterFront.restype = c_void_p
		self.h.RegisterNameServer.argtypes = [c_void_p , c_char_p]
		self.h.RegisterNameServer.restype = c_void_p
		self.h.RegisterFensUserInfo.argtypes = [c_void_p , c_void_p]
		self.h.RegisterFensUserInfo.restype = c_void_p
		self.h.RegisterSpi.argtypes = [c_void_p , c_void_p]
		self.h.RegisterSpi.restype = c_void_p
		self.h.ReqUserLogin.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogin.restype = c_void_p
		self.h.ReqUserLogout.argtypes = [c_void_p , c_void_p , c_int32]
		self.h.ReqUserLogout.restype = c_void_p

		# restore work directory
		os.chdir(cur_path)


	def RegCB(self):
		"""在createapi, createspi后调用"""

		self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontConnected.restype = c_void_p
		self.evOnFrontConnected = CFUNCTYPE(c_void_p)(self.__OnFrontConnected)
		self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

		self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
		self.h.SetOnFrontDisconnected.restype = c_void_p
		self.evOnFrontDisconnected = CFUNCTYPE(c_void_p, c_int32)(self.__OnFrontDisconnected)
		self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

		self.h.SetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
		self.h.SetOnHeartBeatWarning.restype = c_void_p
		self.evOnHeartBeatWarning = CFUNCTYPE(c_void_p, c_int32)(self.__OnHeartBeatWarning)
		self.h.SetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)

		self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogin.restype = c_void_p
		self.evOnRspUserLogin = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
		self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

		self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUserLogout.restype = c_void_p
		self.evOnRspUserLogout = CFUNCTYPE(c_void_p, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
		self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

		self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspError.restype = c_void_p
		self.evOnRspError = CFUNCTYPE(c_void_p, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
		self.h.SetOnRspError(self.spi, self.evOnRspError)

		self.h.SetOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspSubMarketData.restype = c_void_p
		self.evOnRspSubMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
		self.h.SetOnRspSubMarketData(self.spi, self.evOnRspSubMarketData)

		self.h.SetOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUnSubMarketData.restype = c_void_p
		self.evOnRspUnSubMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
		self.h.SetOnRspUnSubMarketData(self.spi, self.evOnRspUnSubMarketData)

		self.h.SetOnRspSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspSubForQuoteRsp.restype = c_void_p
		self.evOnRspSubForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubForQuoteRsp)
		self.h.SetOnRspSubForQuoteRsp(self.spi, self.evOnRspSubForQuoteRsp)

		self.h.SetOnRspUnSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRspUnSubForQuoteRsp.restype = c_void_p
		self.evOnRspUnSubForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubForQuoteRsp)
		self.h.SetOnRspUnSubForQuoteRsp(self.spi, self.evOnRspUnSubForQuoteRsp)

		self.h.SetOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnDepthMarketData.restype = c_void_p
		self.evOnRtnDepthMarketData = CFUNCTYPE(c_void_p, POINTER(CThostFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
		self.h.SetOnRtnDepthMarketData(self.spi, self.evOnRtnDepthMarketData)

		self.h.SetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
		self.h.SetOnRtnForQuoteRsp.restype = c_void_p
		self.evOnRtnForQuoteRsp = CFUNCTYPE(c_void_p, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
		self.h.SetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)

	def __OnFrontConnected(self):
		self.OnFrontConnected()
	
	def __OnFrontDisconnected(self, nReason):
		self.OnFrontDisconnected(nReason)
	
	def __OnHeartBeatWarning(self, nTimeLapse):
		self.OnHeartBeatWarning(nTimeLapse)
	
	def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
		self.OnRspUserLogin(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
		self.OnRspUserLogout(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
		self.OnRspError(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
		self.OnRspSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
		self.OnRspUnSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
		self.OnRspSubForQuoteRsp(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
		self.OnRspUnSubForQuoteRsp(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents.clone(), POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents.clone(), nRequestID, bIsLast)
	
	def __OnRtnDepthMarketData(self, pDepthMarketData):
		self.OnRtnDepthMarketData(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents.clone())
	
	def __OnRtnForQuoteRsp(self, pForQuoteRsp):
		self.OnRtnForQuoteRsp(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents.clone())
	
	def OnFrontConnected(self):
		print('OnFrontConnected:')

	def OnFrontDisconnected(self, nReason = int):
		print('OnFrontDisconnected:, nReason = int')
		print(nReason)

	def OnHeartBeatWarning(self, nTimeLapse = int):
		print('OnHeartBeatWarning:, nTimeLapse = int')
		print(nTimeLapse)

	def OnRspUserLogin(self, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspUserLogin:, pRspUserLogin = CThostFtdcRspUserLoginField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pRspUserLogin)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspUserLogout(self, pUserLogout = CThostFtdcUserLogoutField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspUserLogout:, pUserLogout = CThostFtdcUserLogoutField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pUserLogout)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspError(self, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspError:, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspSubMarketData(self, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspSubMarketData:, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pSpecificInstrument)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspUnSubMarketData(self, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspUnSubMarketData:, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pSpecificInstrument)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspSubForQuoteRsp(self, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspSubForQuoteRsp:, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pSpecificInstrument)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRspUnSubForQuoteRsp(self, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool):
		print('OnRspUnSubForQuoteRsp:, pSpecificInstrument = CThostFtdcSpecificInstrumentField, pRspInfo = CThostFtdcRspInfoField, nRequestID = int, bIsLast = bool')
		print(pSpecificInstrument)
		print(pRspInfo)
		print(nRequestID)
		print(bIsLast)

	def OnRtnDepthMarketData(self, pDepthMarketData = CThostFtdcDepthMarketDataField):
		print('OnRtnDepthMarketData:, pDepthMarketData = CThostFtdcDepthMarketDataField')
		print(pDepthMarketData)

	def OnRtnForQuoteRsp(self, pForQuoteRsp = CThostFtdcForQuoteRspField):
		print('OnRtnForQuoteRsp:, pForQuoteRsp = CThostFtdcForQuoteRspField')
		print(pForQuoteRsp)

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
			
	def GetTradingDay(self):
		self.h.GetTradingDay(self.api)
			
	def RegisterFront(self, pszFrontAddress):
		self.h.RegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))
			
	def RegisterNameServer(self, pszNsAddress):
		self.h.RegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))
			
	def RegisterFensUserInfo(self, BrokerID = '', UserID = '', LoginMode = ''):
		struc = CThostFtdcFensUserInfoField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.LoginMode = list(LoginModeType)[0].value if LoginMode=='' else LoginMode.value

		self.nRequestID += 1
		self.h.RegisterFensUserInfo(self.api, byref(struc), self.nRequestID)
			
	def RegisterSpi(self, pSpi):
		self.h.RegisterSpi(self.api, pSpi)
			
	def SubscribeMarketData(self, pInstrumentID):
		self.h.SubscribeMarketData.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.SubscribeMarketData.restype = c_void_p
		self.h.SubscribeMarketData(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def UnSubscribeMarketData(self, pInstrumentID):
		self.h.UnSubscribeMarketData.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.UnSubscribeMarketData.restype = c_void_p
		self.h.UnSubscribeMarketData(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def SubscribeForQuoteRsp(self, pInstrumentID):
		self.h.SubscribeForQuoteRsp.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.SubscribeForQuoteRsp.restype = c_void_p
		self.h.SubscribeForQuoteRsp(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def UnSubscribeForQuoteRsp(self, pInstrumentID):
		self.h.UnSubscribeForQuoteRsp.argtypes = [c_void_p , c_char_p*1, c_int32]
		self.h.UnSubscribeForQuoteRsp.restype = c_void_p
		self.h.UnSubscribeForQuoteRsp(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)

	def ReqUserLogin(self, TradingDay = '', BrokerID = '', UserID = '', Password = '', UserProductInfo = '', InterfaceProductInfo = '', ProtocolInfo = '', MacAddress = '', OneTimePassword = '', ClientIPAddress = '', LoginRemark = ''):
		struc = CThostFtdcReqUserLoginField()
		struc.TradingDay = bytes(TradingDay, encoding='ascii')
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')
		struc.Password = bytes(Password, encoding='ascii')
		struc.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
		struc.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
		struc.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
		struc.MacAddress = bytes(MacAddress, encoding='ascii')
		struc.OneTimePassword = bytes(OneTimePassword, encoding='ascii')
		struc.ClientIPAddress = bytes(ClientIPAddress, encoding='ascii')
		struc.LoginRemark = bytes(LoginRemark, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqUserLogin(self.api, byref(struc), self.nRequestID)
			
	def ReqUserLogout(self, BrokerID = '', UserID = ''):
		struc = CThostFtdcUserLogoutField()
		struc.BrokerID = bytes(BrokerID, encoding='ascii')
		struc.UserID = bytes(UserID, encoding='ascii')

		self.nRequestID += 1
		self.h.ReqUserLogout(self.api, byref(struc), self.nRequestID)
			