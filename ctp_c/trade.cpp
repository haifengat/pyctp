#include "trade.h"
#include <string.h>
int nReq;

Trade::Trade(void)
{	
	_FrontConnected = NULL;
	_FrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_RspAuthenticate = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RspUserPasswordUpdate = NULL;
	_RspTradingAccountPasswordUpdate = NULL;
	_RspUserAuthMethod = NULL;
	_RspGenUserCaptcha = NULL;
	_RspGenUserText = NULL;
	_RspOrderInsert = NULL;
	_RspParkedOrderInsert = NULL;
	_RspParkedOrderAction = NULL;
	_RspOrderAction = NULL;
	_RspQryMaxOrderVolume = NULL;
	_RspSettlementInfoConfirm = NULL;
	_RspRemoveParkedOrder = NULL;
	_RspRemoveParkedOrderAction = NULL;
	_RspExecOrderInsert = NULL;
	_RspExecOrderAction = NULL;
	_RspForQuoteInsert = NULL;
	_RspQuoteInsert = NULL;
	_RspQuoteAction = NULL;
	_RspBatchOrderAction = NULL;
	_RspOptionSelfCloseInsert = NULL;
	_RspOptionSelfCloseAction = NULL;
	_RspCombActionInsert = NULL;
	_RspQryOrder = NULL;
	_RspQryTrade = NULL;
	_RspQryInvestorPosition = NULL;
	_RspQryTradingAccount = NULL;
	_RspQryInvestor = NULL;
	_RspQryTradingCode = NULL;
	_RspQryInstrumentMarginRate = NULL;
	_RspQryInstrumentCommissionRate = NULL;
	_RspQryExchange = NULL;
	_RspQryProduct = NULL;
	_RspQryInstrument = NULL;
	_RspQryDepthMarketData = NULL;
	_RspQrySettlementInfo = NULL;
	_RspQryTransferBank = NULL;
	_RspQryInvestorPositionDetail = NULL;
	_RspQryNotice = NULL;
	_RspQrySettlementInfoConfirm = NULL;
	_RspQryInvestorPositionCombineDetail = NULL;
	_RspQryCFMMCTradingAccountKey = NULL;
	_RspQryEWarrantOffset = NULL;
	_RspQryInvestorProductGroupMargin = NULL;
	_RspQryExchangeMarginRate = NULL;
	_RspQryExchangeMarginRateAdjust = NULL;
	_RspQryExchangeRate = NULL;
	_RspQrySecAgentACIDMap = NULL;
	_RspQryProductExchRate = NULL;
	_RspQryProductGroup = NULL;
	_RspQryMMInstrumentCommissionRate = NULL;
	_RspQryMMOptionInstrCommRate = NULL;
	_RspQryInstrumentOrderCommRate = NULL;
	_RspQrySecAgentTradingAccount = NULL;
	_RspQrySecAgentCheckMode = NULL;
	_RspQrySecAgentTradeInfo = NULL;
	_RspQryOptionInstrTradeCost = NULL;
	_RspQryOptionInstrCommRate = NULL;
	_RspQryExecOrder = NULL;
	_RspQryForQuote = NULL;
	_RspQryQuote = NULL;
	_RspQryOptionSelfClose = NULL;
	_RspQryInvestUnit = NULL;
	_RspQryCombInstrumentGuard = NULL;
	_RspQryCombAction = NULL;
	_RspQryTransferSerial = NULL;
	_RspQryAccountregister = NULL;
	_RspError = NULL;
	_RtnOrder = NULL;
	_RtnTrade = NULL;
	_ErrRtnOrderInsert = NULL;
	_ErrRtnOrderAction = NULL;
	_RtnInstrumentStatus = NULL;
	_RtnBulletin = NULL;
	_RtnTradingNotice = NULL;
	_RtnErrorConditionalOrder = NULL;
	_RtnExecOrder = NULL;
	_ErrRtnExecOrderInsert = NULL;
	_ErrRtnExecOrderAction = NULL;
	_ErrRtnForQuoteInsert = NULL;
	_RtnQuote = NULL;
	_ErrRtnQuoteInsert = NULL;
	_ErrRtnQuoteAction = NULL;
	_RtnForQuoteRsp = NULL;
	_RtnCFMMCTradingAccountToken = NULL;
	_ErrRtnBatchOrderAction = NULL;
	_RtnOptionSelfClose = NULL;
	_ErrRtnOptionSelfCloseInsert = NULL;
	_ErrRtnOptionSelfCloseAction = NULL;
	_RtnCombAction = NULL;
	_ErrRtnCombActionInsert = NULL;
	_RspQryContractBank = NULL;
	_RspQryParkedOrder = NULL;
	_RspQryParkedOrderAction = NULL;
	_RspQryTradingNotice = NULL;
	_RspQryBrokerTradingParams = NULL;
	_RspQryBrokerTradingAlgos = NULL;
	_RspQueryCFMMCTradingAccountToken = NULL;
	_RtnFromBankToFutureByBank = NULL;
	_RtnFromFutureToBankByBank = NULL;
	_RtnRepealFromBankToFutureByBank = NULL;
	_RtnRepealFromFutureToBankByBank = NULL;
	_RtnFromBankToFutureByFuture = NULL;
	_RtnFromFutureToBankByFuture = NULL;
	_RtnRepealFromBankToFutureByFutureManual = NULL;
	_RtnRepealFromFutureToBankByFutureManual = NULL;
	_RtnQueryBankBalanceByFuture = NULL;
	_ErrRtnBankToFutureByFuture = NULL;
	_ErrRtnFutureToBankByFuture = NULL;
	_ErrRtnRepealBankToFutureByFutureManual = NULL;
	_ErrRtnRepealFutureToBankByFutureManual = NULL;
	_ErrRtnQueryBankBalanceByFuture = NULL;
	_RtnRepealFromBankToFutureByFuture = NULL;
	_RtnRepealFromFutureToBankByFuture = NULL;
	_RspFromBankToFutureByFuture = NULL;
	_RspFromFutureToBankByFuture = NULL;
	_RspQueryBankAccountMoneyByFuture = NULL;
	_RtnOpenAccountByBank = NULL;
	_RtnCancelAccountByBank = NULL;
	_RtnChangeAccountByBank = NULL;
	_RspQryClassifiedInstrument = NULL;
	_RspQryCombPromotionParam = NULL;
}

DLL_EXPORT_C_DECL void WINAPI SetOnFrontConnected(Trade* spi, void* func){spi->_FrontConnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnFrontDisconnected(Trade* spi, void* func){spi->_FrontDisconnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnHeartBeatWarning(Trade* spi, void* func){spi->_HeartBeatWarning = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspAuthenticate(Trade* spi, void* func){spi->_RspAuthenticate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogin(Trade* spi, void* func){spi->_RspUserLogin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogout(Trade* spi, void* func){spi->_RspUserLogout = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserPasswordUpdate(Trade* spi, void* func){spi->_RspUserPasswordUpdate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspTradingAccountPasswordUpdate(Trade* spi, void* func){spi->_RspTradingAccountPasswordUpdate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserAuthMethod(Trade* spi, void* func){spi->_RspUserAuthMethod = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspGenUserCaptcha(Trade* spi, void* func){spi->_RspGenUserCaptcha = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspGenUserText(Trade* spi, void* func){spi->_RspGenUserText = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOrderInsert(Trade* spi, void* func){spi->_RspOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspParkedOrderInsert(Trade* spi, void* func){spi->_RspParkedOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspParkedOrderAction(Trade* spi, void* func){spi->_RspParkedOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOrderAction(Trade* spi, void* func){spi->_RspOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryMaxOrderVolume(Trade* spi, void* func){spi->_RspQryMaxOrderVolume = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspSettlementInfoConfirm(Trade* spi, void* func){spi->_RspSettlementInfoConfirm = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspRemoveParkedOrder(Trade* spi, void* func){spi->_RspRemoveParkedOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspRemoveParkedOrderAction(Trade* spi, void* func){spi->_RspRemoveParkedOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspExecOrderInsert(Trade* spi, void* func){spi->_RspExecOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspExecOrderAction(Trade* spi, void* func){spi->_RspExecOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspForQuoteInsert(Trade* spi, void* func){spi->_RspForQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQuoteInsert(Trade* spi, void* func){spi->_RspQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQuoteAction(Trade* spi, void* func){spi->_RspQuoteAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspBatchOrderAction(Trade* spi, void* func){spi->_RspBatchOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOptionSelfCloseInsert(Trade* spi, void* func){spi->_RspOptionSelfCloseInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOptionSelfCloseAction(Trade* spi, void* func){spi->_RspOptionSelfCloseAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspCombActionInsert(Trade* spi, void* func){spi->_RspCombActionInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryOrder(Trade* spi, void* func){spi->_RspQryOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTrade(Trade* spi, void* func){spi->_RspQryTrade = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorPosition(Trade* spi, void* func){spi->_RspQryInvestorPosition = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTradingAccount(Trade* spi, void* func){spi->_RspQryTradingAccount = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestor(Trade* spi, void* func){spi->_RspQryInvestor = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTradingCode(Trade* spi, void* func){spi->_RspQryTradingCode = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrumentMarginRate(Trade* spi, void* func){spi->_RspQryInstrumentMarginRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrumentCommissionRate(Trade* spi, void* func){spi->_RspQryInstrumentCommissionRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExchange(Trade* spi, void* func){spi->_RspQryExchange = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryProduct(Trade* spi, void* func){spi->_RspQryProduct = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrument(Trade* spi, void* func){spi->_RspQryInstrument = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryDepthMarketData(Trade* spi, void* func){spi->_RspQryDepthMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySettlementInfo(Trade* spi, void* func){spi->_RspQrySettlementInfo = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTransferBank(Trade* spi, void* func){spi->_RspQryTransferBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorPositionDetail(Trade* spi, void* func){spi->_RspQryInvestorPositionDetail = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryNotice(Trade* spi, void* func){spi->_RspQryNotice = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySettlementInfoConfirm(Trade* spi, void* func){spi->_RspQrySettlementInfoConfirm = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorPositionCombineDetail(Trade* spi, void* func){spi->_RspQryInvestorPositionCombineDetail = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryCFMMCTradingAccountKey(Trade* spi, void* func){spi->_RspQryCFMMCTradingAccountKey = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryEWarrantOffset(Trade* spi, void* func){spi->_RspQryEWarrantOffset = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorProductGroupMargin(Trade* spi, void* func){spi->_RspQryInvestorProductGroupMargin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExchangeMarginRate(Trade* spi, void* func){spi->_RspQryExchangeMarginRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExchangeMarginRateAdjust(Trade* spi, void* func){spi->_RspQryExchangeMarginRateAdjust = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExchangeRate(Trade* spi, void* func){spi->_RspQryExchangeRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySecAgentACIDMap(Trade* spi, void* func){spi->_RspQrySecAgentACIDMap = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryProductExchRate(Trade* spi, void* func){spi->_RspQryProductExchRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryProductGroup(Trade* spi, void* func){spi->_RspQryProductGroup = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryMMInstrumentCommissionRate(Trade* spi, void* func){spi->_RspQryMMInstrumentCommissionRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryMMOptionInstrCommRate(Trade* spi, void* func){spi->_RspQryMMOptionInstrCommRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrumentOrderCommRate(Trade* spi, void* func){spi->_RspQryInstrumentOrderCommRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySecAgentTradingAccount(Trade* spi, void* func){spi->_RspQrySecAgentTradingAccount = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySecAgentCheckMode(Trade* spi, void* func){spi->_RspQrySecAgentCheckMode = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySecAgentTradeInfo(Trade* spi, void* func){spi->_RspQrySecAgentTradeInfo = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryOptionInstrTradeCost(Trade* spi, void* func){spi->_RspQryOptionInstrTradeCost = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryOptionInstrCommRate(Trade* spi, void* func){spi->_RspQryOptionInstrCommRate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExecOrder(Trade* spi, void* func){spi->_RspQryExecOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryForQuote(Trade* spi, void* func){spi->_RspQryForQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryQuote(Trade* spi, void* func){spi->_RspQryQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryOptionSelfClose(Trade* spi, void* func){spi->_RspQryOptionSelfClose = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestUnit(Trade* spi, void* func){spi->_RspQryInvestUnit = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryCombInstrumentGuard(Trade* spi, void* func){spi->_RspQryCombInstrumentGuard = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryCombAction(Trade* spi, void* func){spi->_RspQryCombAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTransferSerial(Trade* spi, void* func){spi->_RspQryTransferSerial = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryAccountregister(Trade* spi, void* func){spi->_RspQryAccountregister = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspError(Trade* spi, void* func){spi->_RspError = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnOrder(Trade* spi, void* func){spi->_RtnOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnTrade(Trade* spi, void* func){spi->_RtnTrade = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOrderInsert(Trade* spi, void* func){spi->_ErrRtnOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOrderAction(Trade* spi, void* func){spi->_ErrRtnOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnInstrumentStatus(Trade* spi, void* func){spi->_RtnInstrumentStatus = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnBulletin(Trade* spi, void* func){spi->_RtnBulletin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnTradingNotice(Trade* spi, void* func){spi->_RtnTradingNotice = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnErrorConditionalOrder(Trade* spi, void* func){spi->_RtnErrorConditionalOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnExecOrder(Trade* spi, void* func){spi->_RtnExecOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnExecOrderInsert(Trade* spi, void* func){spi->_ErrRtnExecOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnExecOrderAction(Trade* spi, void* func){spi->_ErrRtnExecOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnForQuoteInsert(Trade* spi, void* func){spi->_ErrRtnForQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnQuote(Trade* spi, void* func){spi->_RtnQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnQuoteInsert(Trade* spi, void* func){spi->_ErrRtnQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnQuoteAction(Trade* spi, void* func){spi->_ErrRtnQuoteAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnForQuoteRsp(Trade* spi, void* func){spi->_RtnForQuoteRsp = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnCFMMCTradingAccountToken(Trade* spi, void* func){spi->_RtnCFMMCTradingAccountToken = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnBatchOrderAction(Trade* spi, void* func){spi->_ErrRtnBatchOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnOptionSelfClose(Trade* spi, void* func){spi->_RtnOptionSelfClose = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOptionSelfCloseInsert(Trade* spi, void* func){spi->_ErrRtnOptionSelfCloseInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOptionSelfCloseAction(Trade* spi, void* func){spi->_ErrRtnOptionSelfCloseAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnCombAction(Trade* spi, void* func){spi->_RtnCombAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnCombActionInsert(Trade* spi, void* func){spi->_ErrRtnCombActionInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryContractBank(Trade* spi, void* func){spi->_RspQryContractBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryParkedOrder(Trade* spi, void* func){spi->_RspQryParkedOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryParkedOrderAction(Trade* spi, void* func){spi->_RspQryParkedOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTradingNotice(Trade* spi, void* func){spi->_RspQryTradingNotice = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryBrokerTradingParams(Trade* spi, void* func){spi->_RspQryBrokerTradingParams = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryBrokerTradingAlgos(Trade* spi, void* func){spi->_RspQryBrokerTradingAlgos = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQueryCFMMCTradingAccountToken(Trade* spi, void* func){spi->_RspQueryCFMMCTradingAccountToken = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnFromBankToFutureByBank(Trade* spi, void* func){spi->_RtnFromBankToFutureByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnFromFutureToBankByBank(Trade* spi, void* func){spi->_RtnFromFutureToBankByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromBankToFutureByBank(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromFutureToBankByBank(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnFromBankToFutureByFuture(Trade* spi, void* func){spi->_RtnFromBankToFutureByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnFromFutureToBankByFuture(Trade* spi, void* func){spi->_RtnFromFutureToBankByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromBankToFutureByFutureManual(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByFutureManual = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromFutureToBankByFutureManual(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByFutureManual = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnQueryBankBalanceByFuture(Trade* spi, void* func){spi->_RtnQueryBankBalanceByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnBankToFutureByFuture(Trade* spi, void* func){spi->_ErrRtnBankToFutureByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnFutureToBankByFuture(Trade* spi, void* func){spi->_ErrRtnFutureToBankByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnRepealBankToFutureByFutureManual(Trade* spi, void* func){spi->_ErrRtnRepealBankToFutureByFutureManual = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnRepealFutureToBankByFutureManual(Trade* spi, void* func){spi->_ErrRtnRepealFutureToBankByFutureManual = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnQueryBankBalanceByFuture(Trade* spi, void* func){spi->_ErrRtnQueryBankBalanceByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromBankToFutureByFuture(Trade* spi, void* func){spi->_RtnRepealFromBankToFutureByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnRepealFromFutureToBankByFuture(Trade* spi, void* func){spi->_RtnRepealFromFutureToBankByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspFromBankToFutureByFuture(Trade* spi, void* func){spi->_RspFromBankToFutureByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspFromFutureToBankByFuture(Trade* spi, void* func){spi->_RspFromFutureToBankByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQueryBankAccountMoneyByFuture(Trade* spi, void* func){spi->_RspQueryBankAccountMoneyByFuture = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnOpenAccountByBank(Trade* spi, void* func){spi->_RtnOpenAccountByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnCancelAccountByBank(Trade* spi, void* func){spi->_RtnCancelAccountByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnChangeAccountByBank(Trade* spi, void* func){spi->_RtnChangeAccountByBank = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryClassifiedInstrument(Trade* spi, void* func){spi->_RspQryClassifiedInstrument = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryCombPromotionParam(Trade* spi, void* func){spi->_RspQryCombPromotionParam = func;}

DLL_EXPORT_C_DECL void* WINAPI CreateApi(){return CThostFtdcTraderApi::CreateFtdcTraderApi("./log/");}
DLL_EXPORT_C_DECL void* WINAPI CreateSpi(){return new Trade();}

DLL_EXPORT_C_DECL void* WINAPI GetVersion() { return (void*)CThostFtdcTraderApi::GetApiVersion(); }
DLL_EXPORT_C_DECL void* WINAPI Release(CThostFtdcTraderApi *api){api->Release(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Init(CThostFtdcTraderApi *api){api->Init(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Join(CThostFtdcTraderApi *api){api->Join(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFront(CThostFtdcTraderApi *api, char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterNameServer(CThostFtdcTraderApi *api, char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFensUserInfo(CThostFtdcTraderApi *api, CThostFtdcFensUserInfoField * pFensUserInfo){api->RegisterFensUserInfo(pFensUserInfo); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterSpi(CThostFtdcTraderApi *api, CThostFtdcTraderSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribePrivateTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType){api->SubscribePrivateTopic(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribePublicTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType){api->SubscribePublicTopic(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqAuthenticate(CThostFtdcTraderApi *api, CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID){api->ReqAuthenticate(pReqAuthenticateField, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo){api->RegisterUserSystemInfo(pUserSystemInfo); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubmitUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo){api->SubmitUserSystemInfo(pUserSystemInfo); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogin(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){api->ReqUserLogin(pReqUserLoginField, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogout(CThostFtdcTraderApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID){api->ReqUserLogout(pUserLogout, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID){api->ReqUserPasswordUpdate(pUserPasswordUpdate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqTradingAccountPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID){api->ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserAuthMethod(CThostFtdcTraderApi *api, CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID){api->ReqUserAuthMethod(pReqUserAuthMethod, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqGenUserCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID){api->ReqGenUserCaptcha(pReqGenUserCaptcha, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqGenUserText(CThostFtdcTraderApi *api, CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID){api->ReqGenUserText(pReqGenUserText, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLoginWithCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID){api->ReqUserLoginWithCaptcha(pReqUserLoginWithCaptcha, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLoginWithText(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID){api->ReqUserLoginWithText(pReqUserLoginWithText, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLoginWithOTP(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID){api->ReqUserLoginWithOTP(pReqUserLoginWithOTP, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputOrderField *pInputOrder, int nRequestID){api->ReqOrderInsert(pInputOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqParkedOrderInsert(CThostFtdcTraderApi *api, CThostFtdcParkedOrderField *pParkedOrder, int nRequestID){api->ReqParkedOrderInsert(pParkedOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID){api->ReqParkedOrderAction(pParkedOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID){api->ReqOrderAction(pInputOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryMaxOrderVolume(CThostFtdcTraderApi *api, CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID){api->ReqQryMaxOrderVolume(pQryMaxOrderVolume, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqSettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID){api->ReqSettlementInfoConfirm(pSettlementInfoConfirm, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqRemoveParkedOrder(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID){api->ReqRemoveParkedOrder(pRemoveParkedOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqRemoveParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID){api->ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqExecOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID){api->ReqExecOrderInsert(pInputExecOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqExecOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID){api->ReqExecOrderAction(pInputExecOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqForQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID){api->ReqForQuoteInsert(pInputForQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputQuoteField *pInputQuote, int nRequestID){api->ReqQuoteInsert(pInputQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQuoteAction(CThostFtdcTraderApi *api, CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID){api->ReqQuoteAction(pInputQuoteAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqBatchOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID){api->ReqBatchOrderAction(pInputBatchOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOptionSelfCloseInsert(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID){api->ReqOptionSelfCloseInsert(pInputOptionSelfClose, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOptionSelfCloseAction(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID){api->ReqOptionSelfCloseAction(pInputOptionSelfCloseAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqCombActionInsert(CThostFtdcTraderApi *api, CThostFtdcInputCombActionField *pInputCombAction, int nRequestID){api->ReqCombActionInsert(pInputCombAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryOrder(CThostFtdcTraderApi *api, CThostFtdcQryOrderField *pQryOrder, int nRequestID){api->ReqQryOrder(pQryOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTrade(CThostFtdcTraderApi *api, CThostFtdcQryTradeField *pQryTrade, int nRequestID){api->ReqQryTrade(pQryTrade, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorPosition(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID){api->ReqQryInvestorPosition(pQryInvestorPosition, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID){api->ReqQryTradingAccount(pQryTradingAccount, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestor(CThostFtdcTraderApi *api, CThostFtdcQryInvestorField *pQryInvestor, int nRequestID){api->ReqQryInvestor(pQryInvestor, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTradingCode(CThostFtdcTraderApi *api, CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID){api->ReqQryTradingCode(pQryTradingCode, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrumentMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID){api->ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID){api->ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExchange(CThostFtdcTraderApi *api, CThostFtdcQryExchangeField *pQryExchange, int nRequestID){api->ReqQryExchange(pQryExchange, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryProduct(CThostFtdcTraderApi *api, CThostFtdcQryProductField *pQryProduct, int nRequestID){api->ReqQryProduct(pQryProduct, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrument(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID){api->ReqQryInstrument(pQryInstrument, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryDepthMarketData(CThostFtdcTraderApi *api, CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID){api->ReqQryDepthMarketData(pQryDepthMarketData, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySettlementInfo(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID){api->ReqQrySettlementInfo(pQrySettlementInfo, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTransferBank(CThostFtdcTraderApi *api, CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID){api->ReqQryTransferBank(pQryTransferBank, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorPositionDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID){api->ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryNotice(CThostFtdcTraderApi *api, CThostFtdcQryNoticeField *pQryNotice, int nRequestID){api->ReqQryNotice(pQryNotice, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID){api->ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorPositionCombineDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID){api->ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryCFMMCTradingAccountKey(CThostFtdcTraderApi *api, CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID){api->ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryEWarrantOffset(CThostFtdcTraderApi *api, CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID){api->ReqQryEWarrantOffset(pQryEWarrantOffset, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorProductGroupMargin(CThostFtdcTraderApi *api, CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID){api->ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExchangeMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID){api->ReqQryExchangeMarginRate(pQryExchangeMarginRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExchangeMarginRateAdjust(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID){api->ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExchangeRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID){api->ReqQryExchangeRate(pQryExchangeRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySecAgentACIDMap(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID){api->ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryProductExchRate(CThostFtdcTraderApi *api, CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID){api->ReqQryProductExchRate(pQryProductExchRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryProductGroup(CThostFtdcTraderApi *api, CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID){api->ReqQryProductGroup(pQryProductGroup, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryMMInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID){api->ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryMMOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID){api->ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrumentOrderCommRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID){api->ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySecAgentTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID){api->ReqQrySecAgentTradingAccount(pQryTradingAccount, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySecAgentCheckMode(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID){api->ReqQrySecAgentCheckMode(pQrySecAgentCheckMode, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySecAgentTradeInfo(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID){api->ReqQrySecAgentTradeInfo(pQrySecAgentTradeInfo, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryOptionInstrTradeCost(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID){api->ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID){api->ReqQryOptionInstrCommRate(pQryOptionInstrCommRate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExecOrder(CThostFtdcTraderApi *api, CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID){api->ReqQryExecOrder(pQryExecOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryForQuote(CThostFtdcTraderApi *api, CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID){api->ReqQryForQuote(pQryForQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryQuote(CThostFtdcTraderApi *api, CThostFtdcQryQuoteField *pQryQuote, int nRequestID){api->ReqQryQuote(pQryQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryOptionSelfClose(CThostFtdcTraderApi *api, CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID){api->ReqQryOptionSelfClose(pQryOptionSelfClose, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestUnit(CThostFtdcTraderApi *api, CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID){api->ReqQryInvestUnit(pQryInvestUnit, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryCombInstrumentGuard(CThostFtdcTraderApi *api, CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID){api->ReqQryCombInstrumentGuard(pQryCombInstrumentGuard, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryCombAction(CThostFtdcTraderApi *api, CThostFtdcQryCombActionField *pQryCombAction, int nRequestID){api->ReqQryCombAction(pQryCombAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTransferSerial(CThostFtdcTraderApi *api, CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID){api->ReqQryTransferSerial(pQryTransferSerial, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryAccountregister(CThostFtdcTraderApi *api, CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID){api->ReqQryAccountregister(pQryAccountregister, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryContractBank(CThostFtdcTraderApi *api, CThostFtdcQryContractBankField *pQryContractBank, int nRequestID){api->ReqQryContractBank(pQryContractBank, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryParkedOrder(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID){api->ReqQryParkedOrder(pQryParkedOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID){api->ReqQryParkedOrderAction(pQryParkedOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTradingNotice(CThostFtdcTraderApi *api, CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID){api->ReqQryTradingNotice(pQryTradingNotice, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryBrokerTradingParams(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID){api->ReqQryBrokerTradingParams(pQryBrokerTradingParams, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryBrokerTradingAlgos(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID){api->ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQueryCFMMCTradingAccountToken(CThostFtdcTraderApi *api, CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID){api->ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqFromBankToFutureByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID){api->ReqFromBankToFutureByFuture(pReqTransfer, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqFromFutureToBankByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID){api->ReqFromFutureToBankByFuture(pReqTransfer, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQueryBankAccountMoneyByFuture(CThostFtdcTraderApi *api, CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID){api->ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryClassifiedInstrument(CThostFtdcTraderApi *api, CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID){api->ReqQryClassifiedInstrument(pQryClassifiedInstrument, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryCombPromotionParam(CThostFtdcTraderApi *api, CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID){api->ReqQryCombPromotionParam(pQryCombPromotionParam, nRequestID); return 0;}