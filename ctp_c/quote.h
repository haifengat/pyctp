#pragma once
#ifdef _WINDOWS  //64位系统没有预定义 WIN32
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT_DECL __declspec(dllexport)
#endif
#else
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C"
#else
#define DLL_EXPORT_DECL extern
#endif
#endif

#ifdef _WINDOWS
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WINAPI      __cdecl
#include "../v6.5.1/ThostFtdcMdApi.h"
#pragma comment(lib, "../v6.5.1/win/thostmduserapi_se.lib")
#else
#define WINAPI      __stdcall
#include "../v6.5.1/ThostFtdcMdApi.h"
#pragma comment(lib, "../v6.5.1/win/thostmduserapi_se.lib")
#endif
#else
#define WINAPI
#include "../v6.5.1/ThostFtdcMdApi.h"
#endif

#include <string.h>

class Quote: CThostFtdcMdSpi
{
public:
    Quote(void);
    //针对收到空反馈的处理
    CThostFtdcRspInfoField rif;
    CThostFtdcRspInfoField* repare(CThostFtdcRspInfoField *pRspInfo)
    {
        if (pRspInfo == NULL)
        {
            memset(&rif, 0, sizeof(rif));
            return &rif;
        }
        else
            return pRspInfo;
    }

	///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
	typedef int (WINAPI *FrontConnected)();
	void *_FrontConnected;
	virtual void OnFrontConnected(){if (_FrontConnected) ((FrontConnected)_FrontConnected)();}

	///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
		///@param nReason 错误原因
		///        0x1001 网络读失败
		///        0x1002 网络写失败
		///        0x2001 接收心跳超时
		///        0x2002 发送心跳失败
		///        0x2003 收到错误报文
	typedef int (WINAPI *FrontDisconnected)(int nReason);
	void *_FrontDisconnected;
	virtual void OnFrontDisconnected(int nReason){if (_FrontDisconnected) ((FrontDisconnected)_FrontDisconnected)(nReason);}

	///心跳超时警告。当长时间未收到报文时，该方法被调用。
		///@param nTimeLapse 距离上次接收报文的时间
	typedef int (WINAPI *HeartBeatWarning)(int nTimeLapse);
	void *_HeartBeatWarning;
	virtual void OnHeartBeatWarning(int nTimeLapse){if (_HeartBeatWarning) ((HeartBeatWarning)_HeartBeatWarning)(nTimeLapse);}

	///登录请求响应
	typedef int (WINAPI *RspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserLogin;
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserLogin)
        {
            if (pRspUserLogin)
                ((RspUserLogin)_RspUserLogin)(pRspUserLogin, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspUserLoginField f = {};
                ((RspUserLogin)_RspUserLogin)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///登出请求响应
	typedef int (WINAPI *RspUserLogout)(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserLogout;
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserLogout)
        {
            if (pUserLogout)
                ((RspUserLogout)_RspUserLogout)(pUserLogout, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcUserLogoutField f = {};
                ((RspUserLogout)_RspUserLogout)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询组播合约响应
	typedef int (WINAPI *RspQryMulticastInstrument)(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryMulticastInstrument;
	virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryMulticastInstrument)
        {
            if (pMulticastInstrument)
                ((RspQryMulticastInstrument)_RspQryMulticastInstrument)(pMulticastInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcMulticastInstrumentField f = {};
                ((RspQryMulticastInstrument)_RspQryMulticastInstrument)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///错误应答
	typedef int (WINAPI *RspError)(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspError;
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspError)
        {
            if (pRspInfo)
                ((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspInfoField f = {};
                ((RspError)_RspError)(repare(&f), nRequestID, bIsLast);
            }
        }
    }

	///订阅行情应答
	typedef int (WINAPI *RspSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspSubMarketData;
	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspSubMarketData)
        {
            if (pSpecificInstrument)
                ((RspSubMarketData)_RspSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSpecificInstrumentField f = {};
                ((RspSubMarketData)_RspSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///取消订阅行情应答
	typedef int (WINAPI *RspUnSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUnSubMarketData;
	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUnSubMarketData)
        {
            if (pSpecificInstrument)
                ((RspUnSubMarketData)_RspUnSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSpecificInstrumentField f = {};
                ((RspUnSubMarketData)_RspUnSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///订阅询价应答
	typedef int (WINAPI *RspSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspSubForQuoteRsp;
	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspSubForQuoteRsp)
        {
            if (pSpecificInstrument)
                ((RspSubForQuoteRsp)_RspSubForQuoteRsp)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSpecificInstrumentField f = {};
                ((RspSubForQuoteRsp)_RspSubForQuoteRsp)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///取消订阅询价应答
	typedef int (WINAPI *RspUnSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUnSubForQuoteRsp;
	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUnSubForQuoteRsp)
        {
            if (pSpecificInstrument)
                ((RspUnSubForQuoteRsp)_RspUnSubForQuoteRsp)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSpecificInstrumentField f = {};
                ((RspUnSubForQuoteRsp)_RspUnSubForQuoteRsp)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///深度行情通知
	typedef int (WINAPI *RtnDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData);
	void *_RtnDepthMarketData;
	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData)
    {
        if (_RtnDepthMarketData)
        {
            if (pDepthMarketData)
                ((RtnDepthMarketData)_RtnDepthMarketData)(pDepthMarketData);
            else
            {
                CThostFtdcDepthMarketDataField f = {};
                ((RtnDepthMarketData)_RtnDepthMarketData)(&f);
            }
        }
    }

	///询价通知
	typedef int (WINAPI *RtnForQuoteRsp)(CThostFtdcForQuoteRspField *pForQuoteRsp);
	void *_RtnForQuoteRsp;
	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp)
    {
        if (_RtnForQuoteRsp)
        {
            if (pForQuoteRsp)
                ((RtnForQuoteRsp)_RtnForQuoteRsp)(pForQuoteRsp);
            else
            {
                CThostFtdcForQuoteRspField f = {};
                ((RtnForQuoteRsp)_RtnForQuoteRsp)(&f);
            }
        }
    }
};
