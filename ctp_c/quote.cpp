#include "quote.h"
#include <string.h>
int nReq;

Quote::Quote(void)
{	
	_FrontConnected = NULL;
	_FrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RspQryMulticastInstrument = NULL;
	_RspError = NULL;
	_RspSubMarketData = NULL;
	_RspUnSubMarketData = NULL;
	_RspSubForQuoteRsp = NULL;
	_RspUnSubForQuoteRsp = NULL;
	_RtnDepthMarketData = NULL;
	_RtnForQuoteRsp = NULL;
}

DLL_EXPORT_C_DECL void WINAPI SetOnFrontConnected(Quote* spi, void* func){spi->_FrontConnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnFrontDisconnected(Quote* spi, void* func){spi->_FrontDisconnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnHeartBeatWarning(Quote* spi, void* func){spi->_HeartBeatWarning = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogin(Quote* spi, void* func){spi->_RspUserLogin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogout(Quote* spi, void* func){spi->_RspUserLogout = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryMulticastInstrument(Quote* spi, void* func){spi->_RspQryMulticastInstrument = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspError(Quote* spi, void* func){spi->_RspError = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspSubMarketData(Quote* spi, void* func){spi->_RspSubMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUnSubMarketData(Quote* spi, void* func){spi->_RspUnSubMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspSubForQuoteRsp(Quote* spi, void* func){spi->_RspSubForQuoteRsp = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUnSubForQuoteRsp(Quote* spi, void* func){spi->_RspUnSubForQuoteRsp = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnDepthMarketData(Quote* spi, void* func){spi->_RtnDepthMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnForQuoteRsp(Quote* spi, void* func){spi->_RtnForQuoteRsp = func;}

DLL_EXPORT_C_DECL void* WINAPI CreateApi(){return CThostFtdcMdApi::CreateFtdcMdApi("./log/");}
DLL_EXPORT_C_DECL void* WINAPI CreateSpi(){return new Quote();}

DLL_EXPORT_C_DECL void* WINAPI Release(CThostFtdcMdApi *api){api->Release(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Init(CThostFtdcMdApi *api){api->Init(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Join(CThostFtdcMdApi *api){api->Join(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFront(CThostFtdcMdApi *api, char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterNameServer(CThostFtdcMdApi *api, char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFensUserInfo(CThostFtdcMdApi *api, CThostFtdcFensUserInfoField * pFensUserInfo){api->RegisterFensUserInfo(pFensUserInfo); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterSpi(CThostFtdcMdApi *api, CThostFtdcMdSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){api->SubscribeMarketData(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI UnSubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){api->UnSubscribeMarketData(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){api->SubscribeForQuoteRsp(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI UnSubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){api->UnSubscribeForQuoteRsp(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogin(CThostFtdcMdApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){api->ReqUserLogin(pReqUserLoginField, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogout(CThostFtdcMdApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID){api->ReqUserLogout(pUserLogout, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryMulticastInstrument(CThostFtdcMdApi *api, CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID){api->ReqQryMulticastInstrument(pQryMulticastInstrument, nRequestID); return 0;}