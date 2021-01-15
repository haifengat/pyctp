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
#include "../v6.5.1/ThostFtdcTraderApi.h"
#pragma comment(lib, "../v6.5.1/win/thosttraderapi_se.lib")
#else
#define WINAPI      __stdcall
#include "../v6.5.1/ThostFtdcTraderApi.h"
#pragma comment(lib, "../v6.5.1/win/thosttraderapi_se.lib")
#endif
#else
#define WINAPI
#include "../v6.5.1/ThostFtdcTraderApi.h"
#endif

#include <string.h>

class Trade: CThostFtdcTraderSpi
{
public:
    Trade(void);
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

	///客户端认证响应
	typedef int (WINAPI *RspAuthenticate)(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspAuthenticate;
	virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspAuthenticate)
        {
            if (pRspAuthenticateField)
                ((RspAuthenticate)_RspAuthenticate)(pRspAuthenticateField, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspAuthenticateField f = {};
                ((RspAuthenticate)_RspAuthenticate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

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

	///用户口令更新请求响应
	typedef int (WINAPI *RspUserPasswordUpdate)(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserPasswordUpdate;
	virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserPasswordUpdate)
        {
            if (pUserPasswordUpdate)
                ((RspUserPasswordUpdate)_RspUserPasswordUpdate)(pUserPasswordUpdate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcUserPasswordUpdateField f = {};
                ((RspUserPasswordUpdate)_RspUserPasswordUpdate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///资金账户口令更新请求响应
	typedef int (WINAPI *RspTradingAccountPasswordUpdate)(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspTradingAccountPasswordUpdate;
	virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspTradingAccountPasswordUpdate)
        {
            if (pTradingAccountPasswordUpdate)
                ((RspTradingAccountPasswordUpdate)_RspTradingAccountPasswordUpdate)(pTradingAccountPasswordUpdate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradingAccountPasswordUpdateField f = {};
                ((RspTradingAccountPasswordUpdate)_RspTradingAccountPasswordUpdate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///查询用户当前支持的认证模式的回复
	typedef int (WINAPI *RspUserAuthMethod)(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserAuthMethod;
	virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserAuthMethod)
        {
            if (pRspUserAuthMethod)
                ((RspUserAuthMethod)_RspUserAuthMethod)(pRspUserAuthMethod, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspUserAuthMethodField f = {};
                ((RspUserAuthMethod)_RspUserAuthMethod)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///获取图形验证码请求的回复
	typedef int (WINAPI *RspGenUserCaptcha)(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspGenUserCaptcha;
	virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspGenUserCaptcha)
        {
            if (pRspGenUserCaptcha)
                ((RspGenUserCaptcha)_RspGenUserCaptcha)(pRspGenUserCaptcha, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspGenUserCaptchaField f = {};
                ((RspGenUserCaptcha)_RspGenUserCaptcha)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///获取短信验证码请求的回复
	typedef int (WINAPI *RspGenUserText)(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspGenUserText;
	virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspGenUserText)
        {
            if (pRspGenUserText)
                ((RspGenUserText)_RspGenUserText)(pRspGenUserText, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRspGenUserTextField f = {};
                ((RspGenUserText)_RspGenUserText)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报单录入请求响应
	typedef int (WINAPI *RspOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOrderInsert;
	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOrderInsert)
        {
            if (pInputOrder)
                ((RspOrderInsert)_RspOrderInsert)(pInputOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputOrderField f = {};
                ((RspOrderInsert)_RspOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///预埋单录入请求响应
	typedef int (WINAPI *RspParkedOrderInsert)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspParkedOrderInsert;
	virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspParkedOrderInsert)
        {
            if (pParkedOrder)
                ((RspParkedOrderInsert)_RspParkedOrderInsert)(pParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcParkedOrderField f = {};
                ((RspParkedOrderInsert)_RspParkedOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///预埋撤单录入请求响应
	typedef int (WINAPI *RspParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspParkedOrderAction;
	virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspParkedOrderAction)
        {
            if (pParkedOrderAction)
                ((RspParkedOrderAction)_RspParkedOrderAction)(pParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcParkedOrderActionField f = {};
                ((RspParkedOrderAction)_RspParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报单操作请求响应
	typedef int (WINAPI *RspOrderAction)(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOrderAction;
	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOrderAction)
        {
            if (pInputOrderAction)
                ((RspOrderAction)_RspOrderAction)(pInputOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputOrderActionField f = {};
                ((RspOrderAction)_RspOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///查询最大报单数量响应
	typedef int (WINAPI *RspQryMaxOrderVolume)(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryMaxOrderVolume;
	virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryMaxOrderVolume)
        {
            if (pQryMaxOrderVolume)
                ((RspQryMaxOrderVolume)_RspQryMaxOrderVolume)(pQryMaxOrderVolume, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcQryMaxOrderVolumeField f = {};
                ((RspQryMaxOrderVolume)_RspQryMaxOrderVolume)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者结算结果确认响应
	typedef int (WINAPI *RspSettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspSettlementInfoConfirm;
	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspSettlementInfoConfirm)
        {
            if (pSettlementInfoConfirm)
                ((RspSettlementInfoConfirm)_RspSettlementInfoConfirm)(pSettlementInfoConfirm, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSettlementInfoConfirmField f = {};
                ((RspSettlementInfoConfirm)_RspSettlementInfoConfirm)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///删除预埋单响应
	typedef int (WINAPI *RspRemoveParkedOrder)(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspRemoveParkedOrder;
	virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspRemoveParkedOrder)
        {
            if (pRemoveParkedOrder)
                ((RspRemoveParkedOrder)_RspRemoveParkedOrder)(pRemoveParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRemoveParkedOrderField f = {};
                ((RspRemoveParkedOrder)_RspRemoveParkedOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///删除预埋撤单响应
	typedef int (WINAPI *RspRemoveParkedOrderAction)(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspRemoveParkedOrderAction;
	virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspRemoveParkedOrderAction)
        {
            if (pRemoveParkedOrderAction)
                ((RspRemoveParkedOrderAction)_RspRemoveParkedOrderAction)(pRemoveParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcRemoveParkedOrderActionField f = {};
                ((RspRemoveParkedOrderAction)_RspRemoveParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///执行宣告录入请求响应
	typedef int (WINAPI *RspExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspExecOrderInsert;
	virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspExecOrderInsert)
        {
            if (pInputExecOrder)
                ((RspExecOrderInsert)_RspExecOrderInsert)(pInputExecOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputExecOrderField f = {};
                ((RspExecOrderInsert)_RspExecOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///执行宣告操作请求响应
	typedef int (WINAPI *RspExecOrderAction)(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspExecOrderAction;
	virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspExecOrderAction)
        {
            if (pInputExecOrderAction)
                ((RspExecOrderAction)_RspExecOrderAction)(pInputExecOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputExecOrderActionField f = {};
                ((RspExecOrderAction)_RspExecOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///询价录入请求响应
	typedef int (WINAPI *RspForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspForQuoteInsert;
	virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspForQuoteInsert)
        {
            if (pInputForQuote)
                ((RspForQuoteInsert)_RspForQuoteInsert)(pInputForQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputForQuoteField f = {};
                ((RspForQuoteInsert)_RspForQuoteInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报价录入请求响应
	typedef int (WINAPI *RspQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQuoteInsert;
	virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQuoteInsert)
        {
            if (pInputQuote)
                ((RspQuoteInsert)_RspQuoteInsert)(pInputQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputQuoteField f = {};
                ((RspQuoteInsert)_RspQuoteInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报价操作请求响应
	typedef int (WINAPI *RspQuoteAction)(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQuoteAction;
	virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQuoteAction)
        {
            if (pInputQuoteAction)
                ((RspQuoteAction)_RspQuoteAction)(pInputQuoteAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputQuoteActionField f = {};
                ((RspQuoteAction)_RspQuoteAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///批量报单操作请求响应
	typedef int (WINAPI *RspBatchOrderAction)(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspBatchOrderAction;
	virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspBatchOrderAction)
        {
            if (pInputBatchOrderAction)
                ((RspBatchOrderAction)_RspBatchOrderAction)(pInputBatchOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputBatchOrderActionField f = {};
                ((RspBatchOrderAction)_RspBatchOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///期权自对冲录入请求响应
	typedef int (WINAPI *RspOptionSelfCloseInsert)(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOptionSelfCloseInsert;
	virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOptionSelfCloseInsert)
        {
            if (pInputOptionSelfClose)
                ((RspOptionSelfCloseInsert)_RspOptionSelfCloseInsert)(pInputOptionSelfClose, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputOptionSelfCloseField f = {};
                ((RspOptionSelfCloseInsert)_RspOptionSelfCloseInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///期权自对冲操作请求响应
	typedef int (WINAPI *RspOptionSelfCloseAction)(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOptionSelfCloseAction;
	virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOptionSelfCloseAction)
        {
            if (pInputOptionSelfCloseAction)
                ((RspOptionSelfCloseAction)_RspOptionSelfCloseAction)(pInputOptionSelfCloseAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputOptionSelfCloseActionField f = {};
                ((RspOptionSelfCloseAction)_RspOptionSelfCloseAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///申请组合录入请求响应
	typedef int (WINAPI *RspCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspCombActionInsert;
	virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspCombActionInsert)
        {
            if (pInputCombAction)
                ((RspCombActionInsert)_RspCombActionInsert)(pInputCombAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInputCombActionField f = {};
                ((RspCombActionInsert)_RspCombActionInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询报单响应
	typedef int (WINAPI *RspQryOrder)(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryOrder;
	virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryOrder)
        {
            if (pOrder)
                ((RspQryOrder)_RspQryOrder)(pOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcOrderField f = {};
                ((RspQryOrder)_RspQryOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询成交响应
	typedef int (WINAPI *RspQryTrade)(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTrade;
	virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTrade)
        {
            if (pTrade)
                ((RspQryTrade)_RspQryTrade)(pTrade, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradeField f = {};
                ((RspQryTrade)_RspQryTrade)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者持仓响应
	typedef int (WINAPI *RspQryInvestorPosition)(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorPosition;
	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorPosition)
        {
            if (pInvestorPosition)
                ((RspQryInvestorPosition)_RspQryInvestorPosition)(pInvestorPosition, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestorPositionField f = {};
                ((RspQryInvestorPosition)_RspQryInvestorPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询资金账户响应
	typedef int (WINAPI *RspQryTradingAccount)(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTradingAccount;
	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTradingAccount)
        {
            if (pTradingAccount)
                ((RspQryTradingAccount)_RspQryTradingAccount)(pTradingAccount, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradingAccountField f = {};
                ((RspQryTradingAccount)_RspQryTradingAccount)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者响应
	typedef int (WINAPI *RspQryInvestor)(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestor;
	virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestor)
        {
            if (pInvestor)
                ((RspQryInvestor)_RspQryInvestor)(pInvestor, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestorField f = {};
                ((RspQryInvestor)_RspQryInvestor)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询交易编码响应
	typedef int (WINAPI *RspQryTradingCode)(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTradingCode;
	virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTradingCode)
        {
            if (pTradingCode)
                ((RspQryTradingCode)_RspQryTradingCode)(pTradingCode, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradingCodeField f = {};
                ((RspQryTradingCode)_RspQryTradingCode)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询合约保证金率响应
	typedef int (WINAPI *RspQryInstrumentMarginRate)(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrumentMarginRate;
	virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrumentMarginRate)
        {
            if (pInstrumentMarginRate)
                ((RspQryInstrumentMarginRate)_RspQryInstrumentMarginRate)(pInstrumentMarginRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInstrumentMarginRateField f = {};
                ((RspQryInstrumentMarginRate)_RspQryInstrumentMarginRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询合约手续费率响应
	typedef int (WINAPI *RspQryInstrumentCommissionRate)(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrumentCommissionRate;
	virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrumentCommissionRate)
        {
            if (pInstrumentCommissionRate)
                ((RspQryInstrumentCommissionRate)_RspQryInstrumentCommissionRate)(pInstrumentCommissionRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInstrumentCommissionRateField f = {};
                ((RspQryInstrumentCommissionRate)_RspQryInstrumentCommissionRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询交易所响应
	typedef int (WINAPI *RspQryExchange)(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExchange;
	virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExchange)
        {
            if (pExchange)
                ((RspQryExchange)_RspQryExchange)(pExchange, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcExchangeField f = {};
                ((RspQryExchange)_RspQryExchange)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询产品响应
	typedef int (WINAPI *RspQryProduct)(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryProduct;
	virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryProduct)
        {
            if (pProduct)
                ((RspQryProduct)_RspQryProduct)(pProduct, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcProductField f = {};
                ((RspQryProduct)_RspQryProduct)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询合约响应
	typedef int (WINAPI *RspQryInstrument)(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrument;
	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrument)
        {
            if (pInstrument)
                ((RspQryInstrument)_RspQryInstrument)(pInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInstrumentField f = {};
                ((RspQryInstrument)_RspQryInstrument)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询行情响应
	typedef int (WINAPI *RspQryDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryDepthMarketData;
	virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryDepthMarketData)
        {
            if (pDepthMarketData)
                ((RspQryDepthMarketData)_RspQryDepthMarketData)(pDepthMarketData, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcDepthMarketDataField f = {};
                ((RspQryDepthMarketData)_RspQryDepthMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者结算结果响应
	typedef int (WINAPI *RspQrySettlementInfo)(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySettlementInfo;
	virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySettlementInfo)
        {
            if (pSettlementInfo)
                ((RspQrySettlementInfo)_RspQrySettlementInfo)(pSettlementInfo, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSettlementInfoField f = {};
                ((RspQrySettlementInfo)_RspQrySettlementInfo)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询转帐银行响应
	typedef int (WINAPI *RspQryTransferBank)(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTransferBank;
	virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTransferBank)
        {
            if (pTransferBank)
                ((RspQryTransferBank)_RspQryTransferBank)(pTransferBank, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTransferBankField f = {};
                ((RspQryTransferBank)_RspQryTransferBank)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者持仓明细响应
	typedef int (WINAPI *RspQryInvestorPositionDetail)(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorPositionDetail;
	virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorPositionDetail)
        {
            if (pInvestorPositionDetail)
                ((RspQryInvestorPositionDetail)_RspQryInvestorPositionDetail)(pInvestorPositionDetail, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestorPositionDetailField f = {};
                ((RspQryInvestorPositionDetail)_RspQryInvestorPositionDetail)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询客户通知响应
	typedef int (WINAPI *RspQryNotice)(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryNotice;
	virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryNotice)
        {
            if (pNotice)
                ((RspQryNotice)_RspQryNotice)(pNotice, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcNoticeField f = {};
                ((RspQryNotice)_RspQryNotice)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询结算信息确认响应
	typedef int (WINAPI *RspQrySettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySettlementInfoConfirm;
	virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySettlementInfoConfirm)
        {
            if (pSettlementInfoConfirm)
                ((RspQrySettlementInfoConfirm)_RspQrySettlementInfoConfirm)(pSettlementInfoConfirm, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSettlementInfoConfirmField f = {};
                ((RspQrySettlementInfoConfirm)_RspQrySettlementInfoConfirm)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者持仓明细响应
	typedef int (WINAPI *RspQryInvestorPositionCombineDetail)(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorPositionCombineDetail;
	virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorPositionCombineDetail)
        {
            if (pInvestorPositionCombineDetail)
                ((RspQryInvestorPositionCombineDetail)_RspQryInvestorPositionCombineDetail)(pInvestorPositionCombineDetail, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestorPositionCombineDetailField f = {};
                ((RspQryInvestorPositionCombineDetail)_RspQryInvestorPositionCombineDetail)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///查询保证金监管系统经纪公司资金账户密钥响应
	typedef int (WINAPI *RspQryCFMMCTradingAccountKey)(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryCFMMCTradingAccountKey;
	virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryCFMMCTradingAccountKey)
        {
            if (pCFMMCTradingAccountKey)
                ((RspQryCFMMCTradingAccountKey)_RspQryCFMMCTradingAccountKey)(pCFMMCTradingAccountKey, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcCFMMCTradingAccountKeyField f = {};
                ((RspQryCFMMCTradingAccountKey)_RspQryCFMMCTradingAccountKey)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询仓单折抵信息响应
	typedef int (WINAPI *RspQryEWarrantOffset)(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryEWarrantOffset;
	virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryEWarrantOffset)
        {
            if (pEWarrantOffset)
                ((RspQryEWarrantOffset)_RspQryEWarrantOffset)(pEWarrantOffset, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcEWarrantOffsetField f = {};
                ((RspQryEWarrantOffset)_RspQryEWarrantOffset)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资者品种/跨品种保证金响应
	typedef int (WINAPI *RspQryInvestorProductGroupMargin)(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorProductGroupMargin;
	virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorProductGroupMargin)
        {
            if (pInvestorProductGroupMargin)
                ((RspQryInvestorProductGroupMargin)_RspQryInvestorProductGroupMargin)(pInvestorProductGroupMargin, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestorProductGroupMarginField f = {};
                ((RspQryInvestorProductGroupMargin)_RspQryInvestorProductGroupMargin)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询交易所保证金率响应
	typedef int (WINAPI *RspQryExchangeMarginRate)(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExchangeMarginRate;
	virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExchangeMarginRate)
        {
            if (pExchangeMarginRate)
                ((RspQryExchangeMarginRate)_RspQryExchangeMarginRate)(pExchangeMarginRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcExchangeMarginRateField f = {};
                ((RspQryExchangeMarginRate)_RspQryExchangeMarginRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询交易所调整保证金率响应
	typedef int (WINAPI *RspQryExchangeMarginRateAdjust)(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExchangeMarginRateAdjust;
	virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExchangeMarginRateAdjust)
        {
            if (pExchangeMarginRateAdjust)
                ((RspQryExchangeMarginRateAdjust)_RspQryExchangeMarginRateAdjust)(pExchangeMarginRateAdjust, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcExchangeMarginRateAdjustField f = {};
                ((RspQryExchangeMarginRateAdjust)_RspQryExchangeMarginRateAdjust)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询汇率响应
	typedef int (WINAPI *RspQryExchangeRate)(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExchangeRate;
	virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExchangeRate)
        {
            if (pExchangeRate)
                ((RspQryExchangeRate)_RspQryExchangeRate)(pExchangeRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcExchangeRateField f = {};
                ((RspQryExchangeRate)_RspQryExchangeRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询二级代理操作员银期权限响应
	typedef int (WINAPI *RspQrySecAgentACIDMap)(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySecAgentACIDMap;
	virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySecAgentACIDMap)
        {
            if (pSecAgentACIDMap)
                ((RspQrySecAgentACIDMap)_RspQrySecAgentACIDMap)(pSecAgentACIDMap, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSecAgentACIDMapField f = {};
                ((RspQrySecAgentACIDMap)_RspQrySecAgentACIDMap)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询产品报价汇率
	typedef int (WINAPI *RspQryProductExchRate)(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryProductExchRate;
	virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryProductExchRate)
        {
            if (pProductExchRate)
                ((RspQryProductExchRate)_RspQryProductExchRate)(pProductExchRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcProductExchRateField f = {};
                ((RspQryProductExchRate)_RspQryProductExchRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询产品组
	typedef int (WINAPI *RspQryProductGroup)(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryProductGroup;
	virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryProductGroup)
        {
            if (pProductGroup)
                ((RspQryProductGroup)_RspQryProductGroup)(pProductGroup, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcProductGroupField f = {};
                ((RspQryProductGroup)_RspQryProductGroup)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询做市商合约手续费率响应
	typedef int (WINAPI *RspQryMMInstrumentCommissionRate)(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryMMInstrumentCommissionRate;
	virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryMMInstrumentCommissionRate)
        {
            if (pMMInstrumentCommissionRate)
                ((RspQryMMInstrumentCommissionRate)_RspQryMMInstrumentCommissionRate)(pMMInstrumentCommissionRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcMMInstrumentCommissionRateField f = {};
                ((RspQryMMInstrumentCommissionRate)_RspQryMMInstrumentCommissionRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询做市商期权合约手续费响应
	typedef int (WINAPI *RspQryMMOptionInstrCommRate)(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryMMOptionInstrCommRate;
	virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryMMOptionInstrCommRate)
        {
            if (pMMOptionInstrCommRate)
                ((RspQryMMOptionInstrCommRate)_RspQryMMOptionInstrCommRate)(pMMOptionInstrCommRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcMMOptionInstrCommRateField f = {};
                ((RspQryMMOptionInstrCommRate)_RspQryMMOptionInstrCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询报单手续费响应
	typedef int (WINAPI *RspQryInstrumentOrderCommRate)(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrumentOrderCommRate;
	virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrumentOrderCommRate)
        {
            if (pInstrumentOrderCommRate)
                ((RspQryInstrumentOrderCommRate)_RspQryInstrumentOrderCommRate)(pInstrumentOrderCommRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInstrumentOrderCommRateField f = {};
                ((RspQryInstrumentOrderCommRate)_RspQryInstrumentOrderCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询资金账户响应
	typedef int (WINAPI *RspQrySecAgentTradingAccount)(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySecAgentTradingAccount;
	virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySecAgentTradingAccount)
        {
            if (pTradingAccount)
                ((RspQrySecAgentTradingAccount)_RspQrySecAgentTradingAccount)(pTradingAccount, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradingAccountField f = {};
                ((RspQrySecAgentTradingAccount)_RspQrySecAgentTradingAccount)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询二级代理商资金校验模式响应
	typedef int (WINAPI *RspQrySecAgentCheckMode)(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySecAgentCheckMode;
	virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySecAgentCheckMode)
        {
            if (pSecAgentCheckMode)
                ((RspQrySecAgentCheckMode)_RspQrySecAgentCheckMode)(pSecAgentCheckMode, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSecAgentCheckModeField f = {};
                ((RspQrySecAgentCheckMode)_RspQrySecAgentCheckMode)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询二级代理商信息响应
	typedef int (WINAPI *RspQrySecAgentTradeInfo)(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySecAgentTradeInfo;
	virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySecAgentTradeInfo)
        {
            if (pSecAgentTradeInfo)
                ((RspQrySecAgentTradeInfo)_RspQrySecAgentTradeInfo)(pSecAgentTradeInfo, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcSecAgentTradeInfoField f = {};
                ((RspQrySecAgentTradeInfo)_RspQrySecAgentTradeInfo)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询期权交易成本响应
	typedef int (WINAPI *RspQryOptionInstrTradeCost)(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryOptionInstrTradeCost;
	virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryOptionInstrTradeCost)
        {
            if (pOptionInstrTradeCost)
                ((RspQryOptionInstrTradeCost)_RspQryOptionInstrTradeCost)(pOptionInstrTradeCost, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcOptionInstrTradeCostField f = {};
                ((RspQryOptionInstrTradeCost)_RspQryOptionInstrTradeCost)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询期权合约手续费响应
	typedef int (WINAPI *RspQryOptionInstrCommRate)(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryOptionInstrCommRate;
	virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryOptionInstrCommRate)
        {
            if (pOptionInstrCommRate)
                ((RspQryOptionInstrCommRate)_RspQryOptionInstrCommRate)(pOptionInstrCommRate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcOptionInstrCommRateField f = {};
                ((RspQryOptionInstrCommRate)_RspQryOptionInstrCommRate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询执行宣告响应
	typedef int (WINAPI *RspQryExecOrder)(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExecOrder;
	virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExecOrder)
        {
            if (pExecOrder)
                ((RspQryExecOrder)_RspQryExecOrder)(pExecOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcExecOrderField f = {};
                ((RspQryExecOrder)_RspQryExecOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询询价响应
	typedef int (WINAPI *RspQryForQuote)(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryForQuote;
	virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryForQuote)
        {
            if (pForQuote)
                ((RspQryForQuote)_RspQryForQuote)(pForQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcForQuoteField f = {};
                ((RspQryForQuote)_RspQryForQuote)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询报价响应
	typedef int (WINAPI *RspQryQuote)(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryQuote;
	virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryQuote)
        {
            if (pQuote)
                ((RspQryQuote)_RspQryQuote)(pQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcQuoteField f = {};
                ((RspQryQuote)_RspQryQuote)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询期权自对冲响应
	typedef int (WINAPI *RspQryOptionSelfClose)(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryOptionSelfClose;
	virtual void OnRspQryOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryOptionSelfClose)
        {
            if (pOptionSelfClose)
                ((RspQryOptionSelfClose)_RspQryOptionSelfClose)(pOptionSelfClose, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcOptionSelfCloseField f = {};
                ((RspQryOptionSelfClose)_RspQryOptionSelfClose)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询投资单元响应
	typedef int (WINAPI *RspQryInvestUnit)(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestUnit;
	virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestUnit)
        {
            if (pInvestUnit)
                ((RspQryInvestUnit)_RspQryInvestUnit)(pInvestUnit, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInvestUnitField f = {};
                ((RspQryInvestUnit)_RspQryInvestUnit)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询组合合约安全系数响应
	typedef int (WINAPI *RspQryCombInstrumentGuard)(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryCombInstrumentGuard;
	virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryCombInstrumentGuard)
        {
            if (pCombInstrumentGuard)
                ((RspQryCombInstrumentGuard)_RspQryCombInstrumentGuard)(pCombInstrumentGuard, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcCombInstrumentGuardField f = {};
                ((RspQryCombInstrumentGuard)_RspQryCombInstrumentGuard)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询申请组合响应
	typedef int (WINAPI *RspQryCombAction)(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryCombAction;
	virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryCombAction)
        {
            if (pCombAction)
                ((RspQryCombAction)_RspQryCombAction)(pCombAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcCombActionField f = {};
                ((RspQryCombAction)_RspQryCombAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询转帐流水响应
	typedef int (WINAPI *RspQryTransferSerial)(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTransferSerial;
	virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTransferSerial)
        {
            if (pTransferSerial)
                ((RspQryTransferSerial)_RspQryTransferSerial)(pTransferSerial, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTransferSerialField f = {};
                ((RspQryTransferSerial)_RspQryTransferSerial)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询银期签约关系响应
	typedef int (WINAPI *RspQryAccountregister)(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryAccountregister;
	virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryAccountregister)
        {
            if (pAccountregister)
                ((RspQryAccountregister)_RspQryAccountregister)(pAccountregister, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcAccountregisterField f = {};
                ((RspQryAccountregister)_RspQryAccountregister)(&f, repare(pRspInfo), nRequestID, bIsLast);
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

	///报单通知
	typedef int (WINAPI *RtnOrder)(CThostFtdcOrderField *pOrder);
	void *_RtnOrder;
	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder)
    {
        if (_RtnOrder)
        {
            if (pOrder)
                ((RtnOrder)_RtnOrder)(pOrder);
            else
            {
                CThostFtdcOrderField f = {};
                ((RtnOrder)_RtnOrder)(&f);
            }
        }
    }

	///成交通知
	typedef int (WINAPI *RtnTrade)(CThostFtdcTradeField *pTrade);
	void *_RtnTrade;
	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade)
    {
        if (_RtnTrade)
        {
            if (pTrade)
                ((RtnTrade)_RtnTrade)(pTrade);
            else
            {
                CThostFtdcTradeField f = {};
                ((RtnTrade)_RtnTrade)(&f);
            }
        }
    }

	///报单录入错误回报
	typedef int (WINAPI *ErrRtnOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOrderInsert;
	virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOrderInsert)
        {
            if (pInputOrder)
                ((ErrRtnOrderInsert)_ErrRtnOrderInsert)(pInputOrder, repare(pRspInfo));
            else
            {
                CThostFtdcInputOrderField f = {};
                ((ErrRtnOrderInsert)_ErrRtnOrderInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///报单操作错误回报
	typedef int (WINAPI *ErrRtnOrderAction)(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOrderAction;
	virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOrderAction)
        {
            if (pOrderAction)
                ((ErrRtnOrderAction)_ErrRtnOrderAction)(pOrderAction, repare(pRspInfo));
            else
            {
                CThostFtdcOrderActionField f = {};
                ((ErrRtnOrderAction)_ErrRtnOrderAction)(&f, repare(pRspInfo));
            }
        }
    }

	///合约交易状态通知
	typedef int (WINAPI *RtnInstrumentStatus)(CThostFtdcInstrumentStatusField *pInstrumentStatus);
	void *_RtnInstrumentStatus;
	virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus)
    {
        if (_RtnInstrumentStatus)
        {
            if (pInstrumentStatus)
                ((RtnInstrumentStatus)_RtnInstrumentStatus)(pInstrumentStatus);
            else
            {
                CThostFtdcInstrumentStatusField f = {};
                ((RtnInstrumentStatus)_RtnInstrumentStatus)(&f);
            }
        }
    }

	///交易所公告通知
	typedef int (WINAPI *RtnBulletin)(CThostFtdcBulletinField *pBulletin);
	void *_RtnBulletin;
	virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin)
    {
        if (_RtnBulletin)
        {
            if (pBulletin)
                ((RtnBulletin)_RtnBulletin)(pBulletin);
            else
            {
                CThostFtdcBulletinField f = {};
                ((RtnBulletin)_RtnBulletin)(&f);
            }
        }
    }

	///交易通知
	typedef int (WINAPI *RtnTradingNotice)(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo);
	void *_RtnTradingNotice;
	virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo)
    {
        if (_RtnTradingNotice)
        {
            if (pTradingNoticeInfo)
                ((RtnTradingNotice)_RtnTradingNotice)(pTradingNoticeInfo);
            else
            {
                CThostFtdcTradingNoticeInfoField f = {};
                ((RtnTradingNotice)_RtnTradingNotice)(&f);
            }
        }
    }

	///提示条件单校验错误
	typedef int (WINAPI *RtnErrorConditionalOrder)(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder);
	void *_RtnErrorConditionalOrder;
	virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder)
    {
        if (_RtnErrorConditionalOrder)
        {
            if (pErrorConditionalOrder)
                ((RtnErrorConditionalOrder)_RtnErrorConditionalOrder)(pErrorConditionalOrder);
            else
            {
                CThostFtdcErrorConditionalOrderField f = {};
                ((RtnErrorConditionalOrder)_RtnErrorConditionalOrder)(&f);
            }
        }
    }

	///执行宣告通知
	typedef int (WINAPI *RtnExecOrder)(CThostFtdcExecOrderField *pExecOrder);
	void *_RtnExecOrder;
	virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder)
    {
        if (_RtnExecOrder)
        {
            if (pExecOrder)
                ((RtnExecOrder)_RtnExecOrder)(pExecOrder);
            else
            {
                CThostFtdcExecOrderField f = {};
                ((RtnExecOrder)_RtnExecOrder)(&f);
            }
        }
    }

	///执行宣告录入错误回报
	typedef int (WINAPI *ErrRtnExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnExecOrderInsert;
	virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnExecOrderInsert)
        {
            if (pInputExecOrder)
                ((ErrRtnExecOrderInsert)_ErrRtnExecOrderInsert)(pInputExecOrder, repare(pRspInfo));
            else
            {
                CThostFtdcInputExecOrderField f = {};
                ((ErrRtnExecOrderInsert)_ErrRtnExecOrderInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///执行宣告操作错误回报
	typedef int (WINAPI *ErrRtnExecOrderAction)(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnExecOrderAction;
	virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnExecOrderAction)
        {
            if (pExecOrderAction)
                ((ErrRtnExecOrderAction)_ErrRtnExecOrderAction)(pExecOrderAction, repare(pRspInfo));
            else
            {
                CThostFtdcExecOrderActionField f = {};
                ((ErrRtnExecOrderAction)_ErrRtnExecOrderAction)(&f, repare(pRspInfo));
            }
        }
    }

	///询价录入错误回报
	typedef int (WINAPI *ErrRtnForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnForQuoteInsert;
	virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnForQuoteInsert)
        {
            if (pInputForQuote)
                ((ErrRtnForQuoteInsert)_ErrRtnForQuoteInsert)(pInputForQuote, repare(pRspInfo));
            else
            {
                CThostFtdcInputForQuoteField f = {};
                ((ErrRtnForQuoteInsert)_ErrRtnForQuoteInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///报价通知
	typedef int (WINAPI *RtnQuote)(CThostFtdcQuoteField *pQuote);
	void *_RtnQuote;
	virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote)
    {
        if (_RtnQuote)
        {
            if (pQuote)
                ((RtnQuote)_RtnQuote)(pQuote);
            else
            {
                CThostFtdcQuoteField f = {};
                ((RtnQuote)_RtnQuote)(&f);
            }
        }
    }

	///报价录入错误回报
	typedef int (WINAPI *ErrRtnQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnQuoteInsert;
	virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnQuoteInsert)
        {
            if (pInputQuote)
                ((ErrRtnQuoteInsert)_ErrRtnQuoteInsert)(pInputQuote, repare(pRspInfo));
            else
            {
                CThostFtdcInputQuoteField f = {};
                ((ErrRtnQuoteInsert)_ErrRtnQuoteInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///报价操作错误回报
	typedef int (WINAPI *ErrRtnQuoteAction)(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnQuoteAction;
	virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnQuoteAction)
        {
            if (pQuoteAction)
                ((ErrRtnQuoteAction)_ErrRtnQuoteAction)(pQuoteAction, repare(pRspInfo));
            else
            {
                CThostFtdcQuoteActionField f = {};
                ((ErrRtnQuoteAction)_ErrRtnQuoteAction)(&f, repare(pRspInfo));
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

	///保证金监控中心用户令牌
	typedef int (WINAPI *RtnCFMMCTradingAccountToken)(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken);
	void *_RtnCFMMCTradingAccountToken;
	virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken)
    {
        if (_RtnCFMMCTradingAccountToken)
        {
            if (pCFMMCTradingAccountToken)
                ((RtnCFMMCTradingAccountToken)_RtnCFMMCTradingAccountToken)(pCFMMCTradingAccountToken);
            else
            {
                CThostFtdcCFMMCTradingAccountTokenField f = {};
                ((RtnCFMMCTradingAccountToken)_RtnCFMMCTradingAccountToken)(&f);
            }
        }
    }

	///批量报单操作错误回报
	typedef int (WINAPI *ErrRtnBatchOrderAction)(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnBatchOrderAction;
	virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnBatchOrderAction)
        {
            if (pBatchOrderAction)
                ((ErrRtnBatchOrderAction)_ErrRtnBatchOrderAction)(pBatchOrderAction, repare(pRspInfo));
            else
            {
                CThostFtdcBatchOrderActionField f = {};
                ((ErrRtnBatchOrderAction)_ErrRtnBatchOrderAction)(&f, repare(pRspInfo));
            }
        }
    }

	///期权自对冲通知
	typedef int (WINAPI *RtnOptionSelfClose)(CThostFtdcOptionSelfCloseField *pOptionSelfClose);
	void *_RtnOptionSelfClose;
	virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose)
    {
        if (_RtnOptionSelfClose)
        {
            if (pOptionSelfClose)
                ((RtnOptionSelfClose)_RtnOptionSelfClose)(pOptionSelfClose);
            else
            {
                CThostFtdcOptionSelfCloseField f = {};
                ((RtnOptionSelfClose)_RtnOptionSelfClose)(&f);
            }
        }
    }

	///期权自对冲录入错误回报
	typedef int (WINAPI *ErrRtnOptionSelfCloseInsert)(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOptionSelfCloseInsert;
	virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOptionSelfCloseInsert)
        {
            if (pInputOptionSelfClose)
                ((ErrRtnOptionSelfCloseInsert)_ErrRtnOptionSelfCloseInsert)(pInputOptionSelfClose, repare(pRspInfo));
            else
            {
                CThostFtdcInputOptionSelfCloseField f = {};
                ((ErrRtnOptionSelfCloseInsert)_ErrRtnOptionSelfCloseInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///期权自对冲操作错误回报
	typedef int (WINAPI *ErrRtnOptionSelfCloseAction)(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOptionSelfCloseAction;
	virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOptionSelfCloseAction)
        {
            if (pOptionSelfCloseAction)
                ((ErrRtnOptionSelfCloseAction)_ErrRtnOptionSelfCloseAction)(pOptionSelfCloseAction, repare(pRspInfo));
            else
            {
                CThostFtdcOptionSelfCloseActionField f = {};
                ((ErrRtnOptionSelfCloseAction)_ErrRtnOptionSelfCloseAction)(&f, repare(pRspInfo));
            }
        }
    }

	///申请组合通知
	typedef int (WINAPI *RtnCombAction)(CThostFtdcCombActionField *pCombAction);
	void *_RtnCombAction;
	virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction)
    {
        if (_RtnCombAction)
        {
            if (pCombAction)
                ((RtnCombAction)_RtnCombAction)(pCombAction);
            else
            {
                CThostFtdcCombActionField f = {};
                ((RtnCombAction)_RtnCombAction)(&f);
            }
        }
    }

	///申请组合录入错误回报
	typedef int (WINAPI *ErrRtnCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnCombActionInsert;
	virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnCombActionInsert)
        {
            if (pInputCombAction)
                ((ErrRtnCombActionInsert)_ErrRtnCombActionInsert)(pInputCombAction, repare(pRspInfo));
            else
            {
                CThostFtdcInputCombActionField f = {};
                ((ErrRtnCombActionInsert)_ErrRtnCombActionInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///请求查询签约银行响应
	typedef int (WINAPI *RspQryContractBank)(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryContractBank;
	virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryContractBank)
        {
            if (pContractBank)
                ((RspQryContractBank)_RspQryContractBank)(pContractBank, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcContractBankField f = {};
                ((RspQryContractBank)_RspQryContractBank)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询预埋单响应
	typedef int (WINAPI *RspQryParkedOrder)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryParkedOrder;
	virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryParkedOrder)
        {
            if (pParkedOrder)
                ((RspQryParkedOrder)_RspQryParkedOrder)(pParkedOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcParkedOrderField f = {};
                ((RspQryParkedOrder)_RspQryParkedOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询预埋撤单响应
	typedef int (WINAPI *RspQryParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryParkedOrderAction;
	virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryParkedOrderAction)
        {
            if (pParkedOrderAction)
                ((RspQryParkedOrderAction)_RspQryParkedOrderAction)(pParkedOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcParkedOrderActionField f = {};
                ((RspQryParkedOrderAction)_RspQryParkedOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询交易通知响应
	typedef int (WINAPI *RspQryTradingNotice)(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTradingNotice;
	virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTradingNotice)
        {
            if (pTradingNotice)
                ((RspQryTradingNotice)_RspQryTradingNotice)(pTradingNotice, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcTradingNoticeField f = {};
                ((RspQryTradingNotice)_RspQryTradingNotice)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询经纪公司交易参数响应
	typedef int (WINAPI *RspQryBrokerTradingParams)(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryBrokerTradingParams;
	virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryBrokerTradingParams)
        {
            if (pBrokerTradingParams)
                ((RspQryBrokerTradingParams)_RspQryBrokerTradingParams)(pBrokerTradingParams, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcBrokerTradingParamsField f = {};
                ((RspQryBrokerTradingParams)_RspQryBrokerTradingParams)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询经纪公司交易算法响应
	typedef int (WINAPI *RspQryBrokerTradingAlgos)(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryBrokerTradingAlgos;
	virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryBrokerTradingAlgos)
        {
            if (pBrokerTradingAlgos)
                ((RspQryBrokerTradingAlgos)_RspQryBrokerTradingAlgos)(pBrokerTradingAlgos, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcBrokerTradingAlgosField f = {};
                ((RspQryBrokerTradingAlgos)_RspQryBrokerTradingAlgos)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求查询监控中心用户令牌
	typedef int (WINAPI *RspQueryCFMMCTradingAccountToken)(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQueryCFMMCTradingAccountToken;
	virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQueryCFMMCTradingAccountToken)
        {
            if (pQueryCFMMCTradingAccountToken)
                ((RspQueryCFMMCTradingAccountToken)_RspQueryCFMMCTradingAccountToken)(pQueryCFMMCTradingAccountToken, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcQueryCFMMCTradingAccountTokenField f = {};
                ((RspQueryCFMMCTradingAccountToken)_RspQueryCFMMCTradingAccountToken)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///银行发起银行资金转期货通知
	typedef int (WINAPI *RtnFromBankToFutureByBank)(CThostFtdcRspTransferField *pRspTransfer);
	void *_RtnFromBankToFutureByBank;
	virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer)
    {
        if (_RtnFromBankToFutureByBank)
        {
            if (pRspTransfer)
                ((RtnFromBankToFutureByBank)_RtnFromBankToFutureByBank)(pRspTransfer);
            else
            {
                CThostFtdcRspTransferField f = {};
                ((RtnFromBankToFutureByBank)_RtnFromBankToFutureByBank)(&f);
            }
        }
    }

	///银行发起期货资金转银行通知
	typedef int (WINAPI *RtnFromFutureToBankByBank)(CThostFtdcRspTransferField *pRspTransfer);
	void *_RtnFromFutureToBankByBank;
	virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer)
    {
        if (_RtnFromFutureToBankByBank)
        {
            if (pRspTransfer)
                ((RtnFromFutureToBankByBank)_RtnFromFutureToBankByBank)(pRspTransfer);
            else
            {
                CThostFtdcRspTransferField f = {};
                ((RtnFromFutureToBankByBank)_RtnFromFutureToBankByBank)(&f);
            }
        }
    }

	///银行发起冲正银行转期货通知
	typedef int (WINAPI *RtnRepealFromBankToFutureByBank)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromBankToFutureByBank;
	virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromBankToFutureByBank)
        {
            if (pRspRepeal)
                ((RtnRepealFromBankToFutureByBank)_RtnRepealFromBankToFutureByBank)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromBankToFutureByBank)_RtnRepealFromBankToFutureByBank)(&f);
            }
        }
    }

	///银行发起冲正期货转银行通知
	typedef int (WINAPI *RtnRepealFromFutureToBankByBank)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromFutureToBankByBank;
	virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromFutureToBankByBank)
        {
            if (pRspRepeal)
                ((RtnRepealFromFutureToBankByBank)_RtnRepealFromFutureToBankByBank)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromFutureToBankByBank)_RtnRepealFromFutureToBankByBank)(&f);
            }
        }
    }

	///期货发起银行资金转期货通知
	typedef int (WINAPI *RtnFromBankToFutureByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	void *_RtnFromBankToFutureByFuture;
	virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer)
    {
        if (_RtnFromBankToFutureByFuture)
        {
            if (pRspTransfer)
                ((RtnFromBankToFutureByFuture)_RtnFromBankToFutureByFuture)(pRspTransfer);
            else
            {
                CThostFtdcRspTransferField f = {};
                ((RtnFromBankToFutureByFuture)_RtnFromBankToFutureByFuture)(&f);
            }
        }
    }

	///期货发起期货资金转银行通知
	typedef int (WINAPI *RtnFromFutureToBankByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	void *_RtnFromFutureToBankByFuture;
	virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer)
    {
        if (_RtnFromFutureToBankByFuture)
        {
            if (pRspTransfer)
                ((RtnFromFutureToBankByFuture)_RtnFromFutureToBankByFuture)(pRspTransfer);
            else
            {
                CThostFtdcRspTransferField f = {};
                ((RtnFromFutureToBankByFuture)_RtnFromFutureToBankByFuture)(&f);
            }
        }
    }

	///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
	typedef int (WINAPI *RtnRepealFromBankToFutureByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromBankToFutureByFutureManual;
	virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromBankToFutureByFutureManual)
        {
            if (pRspRepeal)
                ((RtnRepealFromBankToFutureByFutureManual)_RtnRepealFromBankToFutureByFutureManual)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromBankToFutureByFutureManual)_RtnRepealFromBankToFutureByFutureManual)(&f);
            }
        }
    }

	///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
	typedef int (WINAPI *RtnRepealFromFutureToBankByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromFutureToBankByFutureManual;
	virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromFutureToBankByFutureManual)
        {
            if (pRspRepeal)
                ((RtnRepealFromFutureToBankByFutureManual)_RtnRepealFromFutureToBankByFutureManual)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromFutureToBankByFutureManual)_RtnRepealFromFutureToBankByFutureManual)(&f);
            }
        }
    }

	///期货发起查询银行余额通知
	typedef int (WINAPI *RtnQueryBankBalanceByFuture)(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount);
	void *_RtnQueryBankBalanceByFuture;
	virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount)
    {
        if (_RtnQueryBankBalanceByFuture)
        {
            if (pNotifyQueryAccount)
                ((RtnQueryBankBalanceByFuture)_RtnQueryBankBalanceByFuture)(pNotifyQueryAccount);
            else
            {
                CThostFtdcNotifyQueryAccountField f = {};
                ((RtnQueryBankBalanceByFuture)_RtnQueryBankBalanceByFuture)(&f);
            }
        }
    }

	///期货发起银行资金转期货错误回报
	typedef int (WINAPI *ErrRtnBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnBankToFutureByFuture;
	virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnBankToFutureByFuture)
        {
            if (pReqTransfer)
                ((ErrRtnBankToFutureByFuture)_ErrRtnBankToFutureByFuture)(pReqTransfer, repare(pRspInfo));
            else
            {
                CThostFtdcReqTransferField f = {};
                ((ErrRtnBankToFutureByFuture)_ErrRtnBankToFutureByFuture)(&f, repare(pRspInfo));
            }
        }
    }

	///期货发起期货资金转银行错误回报
	typedef int (WINAPI *ErrRtnFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnFutureToBankByFuture;
	virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnFutureToBankByFuture)
        {
            if (pReqTransfer)
                ((ErrRtnFutureToBankByFuture)_ErrRtnFutureToBankByFuture)(pReqTransfer, repare(pRspInfo));
            else
            {
                CThostFtdcReqTransferField f = {};
                ((ErrRtnFutureToBankByFuture)_ErrRtnFutureToBankByFuture)(&f, repare(pRspInfo));
            }
        }
    }

	///系统运行时期货端手工发起冲正银行转期货错误回报
	typedef int (WINAPI *ErrRtnRepealBankToFutureByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnRepealBankToFutureByFutureManual;
	virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnRepealBankToFutureByFutureManual)
        {
            if (pReqRepeal)
                ((ErrRtnRepealBankToFutureByFutureManual)_ErrRtnRepealBankToFutureByFutureManual)(pReqRepeal, repare(pRspInfo));
            else
            {
                CThostFtdcReqRepealField f = {};
                ((ErrRtnRepealBankToFutureByFutureManual)_ErrRtnRepealBankToFutureByFutureManual)(&f, repare(pRspInfo));
            }
        }
    }

	///系统运行时期货端手工发起冲正期货转银行错误回报
	typedef int (WINAPI *ErrRtnRepealFutureToBankByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnRepealFutureToBankByFutureManual;
	virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnRepealFutureToBankByFutureManual)
        {
            if (pReqRepeal)
                ((ErrRtnRepealFutureToBankByFutureManual)_ErrRtnRepealFutureToBankByFutureManual)(pReqRepeal, repare(pRspInfo));
            else
            {
                CThostFtdcReqRepealField f = {};
                ((ErrRtnRepealFutureToBankByFutureManual)_ErrRtnRepealFutureToBankByFutureManual)(&f, repare(pRspInfo));
            }
        }
    }

	///期货发起查询银行余额错误回报
	typedef int (WINAPI *ErrRtnQueryBankBalanceByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo);
	void *_ErrRtnQueryBankBalanceByFuture;
	virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnQueryBankBalanceByFuture)
        {
            if (pReqQueryAccount)
                ((ErrRtnQueryBankBalanceByFuture)_ErrRtnQueryBankBalanceByFuture)(pReqQueryAccount, repare(pRspInfo));
            else
            {
                CThostFtdcReqQueryAccountField f = {};
                ((ErrRtnQueryBankBalanceByFuture)_ErrRtnQueryBankBalanceByFuture)(&f, repare(pRspInfo));
            }
        }
    }

	///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
	typedef int (WINAPI *RtnRepealFromBankToFutureByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromBankToFutureByFuture;
	virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromBankToFutureByFuture)
        {
            if (pRspRepeal)
                ((RtnRepealFromBankToFutureByFuture)_RtnRepealFromBankToFutureByFuture)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromBankToFutureByFuture)_RtnRepealFromBankToFutureByFuture)(&f);
            }
        }
    }

	///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
	typedef int (WINAPI *RtnRepealFromFutureToBankByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	void *_RtnRepealFromFutureToBankByFuture;
	virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal)
    {
        if (_RtnRepealFromFutureToBankByFuture)
        {
            if (pRspRepeal)
                ((RtnRepealFromFutureToBankByFuture)_RtnRepealFromFutureToBankByFuture)(pRspRepeal);
            else
            {
                CThostFtdcRspRepealField f = {};
                ((RtnRepealFromFutureToBankByFuture)_RtnRepealFromFutureToBankByFuture)(&f);
            }
        }
    }

	///期货发起银行资金转期货应答
	typedef int (WINAPI *RspFromBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspFromBankToFutureByFuture;
	virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspFromBankToFutureByFuture)
        {
            if (pReqTransfer)
                ((RspFromBankToFutureByFuture)_RspFromBankToFutureByFuture)(pReqTransfer, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcReqTransferField f = {};
                ((RspFromBankToFutureByFuture)_RspFromBankToFutureByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///期货发起期货资金转银行应答
	typedef int (WINAPI *RspFromFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspFromFutureToBankByFuture;
	virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspFromFutureToBankByFuture)
        {
            if (pReqTransfer)
                ((RspFromFutureToBankByFuture)_RspFromFutureToBankByFuture)(pReqTransfer, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcReqTransferField f = {};
                ((RspFromFutureToBankByFuture)_RspFromFutureToBankByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///期货发起查询银行余额应答
	typedef int (WINAPI *RspQueryBankAccountMoneyByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQueryBankAccountMoneyByFuture;
	virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQueryBankAccountMoneyByFuture)
        {
            if (pReqQueryAccount)
                ((RspQueryBankAccountMoneyByFuture)_RspQueryBankAccountMoneyByFuture)(pReqQueryAccount, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcReqQueryAccountField f = {};
                ((RspQueryBankAccountMoneyByFuture)_RspQueryBankAccountMoneyByFuture)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///银行发起银期开户通知
	typedef int (WINAPI *RtnOpenAccountByBank)(CThostFtdcOpenAccountField *pOpenAccount);
	void *_RtnOpenAccountByBank;
	virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount)
    {
        if (_RtnOpenAccountByBank)
        {
            if (pOpenAccount)
                ((RtnOpenAccountByBank)_RtnOpenAccountByBank)(pOpenAccount);
            else
            {
                CThostFtdcOpenAccountField f = {};
                ((RtnOpenAccountByBank)_RtnOpenAccountByBank)(&f);
            }
        }
    }

	///银行发起银期销户通知
	typedef int (WINAPI *RtnCancelAccountByBank)(CThostFtdcCancelAccountField *pCancelAccount);
	void *_RtnCancelAccountByBank;
	virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount)
    {
        if (_RtnCancelAccountByBank)
        {
            if (pCancelAccount)
                ((RtnCancelAccountByBank)_RtnCancelAccountByBank)(pCancelAccount);
            else
            {
                CThostFtdcCancelAccountField f = {};
                ((RtnCancelAccountByBank)_RtnCancelAccountByBank)(&f);
            }
        }
    }

	///银行发起变更银行账号通知
	typedef int (WINAPI *RtnChangeAccountByBank)(CThostFtdcChangeAccountField *pChangeAccount);
	void *_RtnChangeAccountByBank;
	virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount)
    {
        if (_RtnChangeAccountByBank)
        {
            if (pChangeAccount)
                ((RtnChangeAccountByBank)_RtnChangeAccountByBank)(pChangeAccount);
            else
            {
                CThostFtdcChangeAccountField f = {};
                ((RtnChangeAccountByBank)_RtnChangeAccountByBank)(&f);
            }
        }
    }

	///请求查询分类合约响应
	typedef int (WINAPI *RspQryClassifiedInstrument)(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryClassifiedInstrument;
	virtual void OnRspQryClassifiedInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryClassifiedInstrument)
        {
            if (pInstrument)
                ((RspQryClassifiedInstrument)_RspQryClassifiedInstrument)(pInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcInstrumentField f = {};
                ((RspQryClassifiedInstrument)_RspQryClassifiedInstrument)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///请求组合优惠比例响应
	typedef int (WINAPI *RspQryCombPromotionParam)(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryCombPromotionParam;
	virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryCombPromotionParam)
        {
            if (pCombPromotionParam)
                ((RspQryCombPromotionParam)_RspQryCombPromotionParam)(pCombPromotionParam, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CThostFtdcCombPromotionParamField f = {};
                ((RspQryCombPromotionParam)_RspQryCombPromotionParam)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }
};
