#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2022/09/11


import os
import sys
import platform
import ctypes
import copy
from .struct import *


class Trade:

    def __init__(self):
        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "lib64")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_trade.dll' if 'Windows' in platform.system() else 'libctp_trade.so')
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

        self.h.tCreateApi.argtypes = []
        self.h.tCreateApi.restype = c_void_p

        self.h.tCreateSpi.argtypes = []
        self.h.tCreateSpi.restype = c_void_p

        self.h.tGetVersion.argtypes = []
        self.h.tGetVersion.restype = c_char_p

        self.api = None
        self.spi = None

        #################### 请求函数 #######################
        # 创建TraderApi
        self.h.tRelease.argtypes = [c_void_p]
        self.h.tRelease.restype = c_void_p
        # 初始化
        self.h.tInit.argtypes = [c_void_p]
        self.h.tInit.restype = c_void_p
        # 等待接口线程结束运行
        self.h.tJoin.argtypes = [c_void_p]
        self.h.tJoin.restype = c_void_p
        # 注册前置机网络地址
        self.h.tRegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterFront.restype = c_void_p
        # @remark RegisterNameServer优先于RegisterFront
        self.h.tRegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterNameServer.restype = c_void_p
        # 注册名字服务器用户信息
        self.h.tRegisterFensUserInfo.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterFensUserInfo.restype = c_void_p
        # 注册回调接口
        self.h.tRegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterSpi.restype = c_void_p
        # 订阅私有流。
        self.h.tSubscribePrivateTopic.argtypes = [c_void_p, c_void_p]
        self.h.tSubscribePrivateTopic.restype = c_void_p
        # 订阅公共流。
        self.h.tSubscribePublicTopic.argtypes = [c_void_p, c_void_p]
        self.h.tSubscribePublicTopic.restype = c_void_p
        # 客户端认证请求
        self.h.tReqAuthenticate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqAuthenticate.restype = c_void_p
        # 注册用户终端信息，用于中继服务器多连接模式
        self.h.tRegisterUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterUserSystemInfo.restype = c_void_p
        # 上报用户终端信息，用于中继服务器操作员登录模式
        self.h.tSubmitUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.tSubmitUserSystemInfo.restype = c_void_p
        # 用户登录请求
        self.h.tReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLogin.restype = c_void_p
        # 登出请求
        self.h.tReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLogout.restype = c_void_p
        # 用户口令更新请求
        self.h.tReqUserPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserPasswordUpdate.restype = c_void_p
        # 资金账户口令更新请求
        self.h.tReqTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqTradingAccountPasswordUpdate.restype = c_void_p
        # 查询用户当前支持的认证模式
        self.h.tReqUserAuthMethod.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserAuthMethod.restype = c_void_p
        # 用户发出获取图形验证码请求
        self.h.tReqGenUserCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqGenUserCaptcha.restype = c_void_p
        # 用户发出获取短信验证码请求
        self.h.tReqGenUserText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqGenUserText.restype = c_void_p
        # 用户发出带有图片验证码的登陆请求
        self.h.tReqUserLoginWithCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithCaptcha.restype = c_void_p
        # 用户发出带有短信验证码的登陆请求
        self.h.tReqUserLoginWithText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithText.restype = c_void_p
        # 用户发出带有动态口令的登陆请求
        self.h.tReqUserLoginWithOTP.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithOTP.restype = c_void_p
        # 报单录入请求
        self.h.tReqOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOrderInsert.restype = c_void_p
        # 预埋单录入请求
        self.h.tReqParkedOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqParkedOrderInsert.restype = c_void_p
        # 预埋撤单录入请求
        self.h.tReqParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqParkedOrderAction.restype = c_void_p
        # 报单操作请求
        self.h.tReqOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOrderAction.restype = c_void_p
        # 查询最大报单数量请求
        self.h.tReqQryMaxOrderVolume.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMaxOrderVolume.restype = c_void_p
        # 投资者结算结果确认
        self.h.tReqSettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqSettlementInfoConfirm.restype = c_void_p
        # 请求删除预埋单
        self.h.tReqRemoveParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqRemoveParkedOrder.restype = c_void_p
        # 请求删除预埋撤单
        self.h.tReqRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqRemoveParkedOrderAction.restype = c_void_p
        # 执行宣告录入请求
        self.h.tReqExecOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqExecOrderInsert.restype = c_void_p
        # 执行宣告操作请求
        self.h.tReqExecOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqExecOrderAction.restype = c_void_p
        # 询价录入请求
        self.h.tReqForQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqForQuoteInsert.restype = c_void_p
        # 报价录入请求
        self.h.tReqQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQuoteInsert.restype = c_void_p
        # 报价操作请求
        self.h.tReqQuoteAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQuoteAction.restype = c_void_p
        # 批量报单操作请求
        self.h.tReqBatchOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqBatchOrderAction.restype = c_void_p
        # 期权自对冲录入请求
        self.h.tReqOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOptionSelfCloseInsert.restype = c_void_p
        # 期权自对冲操作请求
        self.h.tReqOptionSelfCloseAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOptionSelfCloseAction.restype = c_void_p
        # 申请组合录入请求
        self.h.tReqCombActionInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqCombActionInsert.restype = c_void_p
        # 请求查询报单
        self.h.tReqQryOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOrder.restype = c_void_p
        # 请求查询成交
        self.h.tReqQryTrade.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTrade.restype = c_void_p
        # 请求查询投资者持仓
        self.h.tReqQryInvestorPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPosition.restype = c_void_p
        # 请求查询资金账户
        self.h.tReqQryTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingAccount.restype = c_void_p
        # 请求查询投资者
        self.h.tReqQryInvestor.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestor.restype = c_void_p
        # 请求查询交易编码
        self.h.tReqQryTradingCode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingCode.restype = c_void_p
        # 请求查询合约保证金率
        self.h.tReqQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentMarginRate.restype = c_void_p
        # 请求查询合约手续费率
        self.h.tReqQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentCommissionRate.restype = c_void_p
        # 请求查询交易所
        self.h.tReqQryExchange.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchange.restype = c_void_p
        # 请求查询产品
        self.h.tReqQryProduct.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProduct.restype = c_void_p
        # 请求查询合约
        self.h.tReqQryInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrument.restype = c_void_p
        # 请求查询行情
        self.h.tReqQryDepthMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryDepthMarketData.restype = c_void_p
        # 请求查询交易员报盘机
        self.h.tReqQryTraderOffer.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTraderOffer.restype = c_void_p
        # 请求查询投资者结算结果
        self.h.tReqQrySettlementInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySettlementInfo.restype = c_void_p
        # 请求查询转帐银行
        self.h.tReqQryTransferBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTransferBank.restype = c_void_p
        # 请求查询投资者持仓明细
        self.h.tReqQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPositionDetail.restype = c_void_p
        # 请求查询客户通知
        self.h.tReqQryNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryNotice.restype = c_void_p
        # 请求查询结算信息确认
        self.h.tReqQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySettlementInfoConfirm.restype = c_void_p
        # 请求查询投资者持仓明细
        self.h.tReqQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPositionCombineDetail.restype = c_void_p
        # 请求查询保证金监管系统经纪公司资金账户密钥
        self.h.tReqQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCFMMCTradingAccountKey.restype = c_void_p
        # 请求查询仓单折抵信息
        self.h.tReqQryEWarrantOffset.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryEWarrantOffset.restype = c_void_p
        # 请求查询投资者品种/跨品种保证金
        self.h.tReqQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorProductGroupMargin.restype = c_void_p
        # 请求查询交易所保证金率
        self.h.tReqQryExchangeMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeMarginRate.restype = c_void_p
        # 请求查询交易所调整保证金率
        self.h.tReqQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeMarginRateAdjust.restype = c_void_p
        # 请求查询汇率
        self.h.tReqQryExchangeRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeRate.restype = c_void_p
        # 请求查询二级代理操作员银期权限
        self.h.tReqQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentACIDMap.restype = c_void_p
        # 请求查询产品报价汇率
        self.h.tReqQryProductExchRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProductExchRate.restype = c_void_p
        # 请求查询产品组
        self.h.tReqQryProductGroup.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProductGroup.restype = c_void_p
        # 请求查询做市商合约手续费率
        self.h.tReqQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMMInstrumentCommissionRate.restype = c_void_p
        # 请求查询做市商期权合约手续费
        self.h.tReqQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMMOptionInstrCommRate.restype = c_void_p
        # 请求查询报单手续费
        self.h.tReqQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentOrderCommRate.restype = c_void_p
        # 请求查询资金账户
        self.h.tReqQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentTradingAccount.restype = c_void_p
        # 请求查询二级代理商资金校验模式
        self.h.tReqQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentCheckMode.restype = c_void_p
        # 请求查询二级代理商信息
        self.h.tReqQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentTradeInfo.restype = c_void_p
        # 请求查询期权交易成本
        self.h.tReqQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionInstrTradeCost.restype = c_void_p
        # 请求查询期权合约手续费
        self.h.tReqQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionInstrCommRate.restype = c_void_p
        # 请求查询执行宣告
        self.h.tReqQryExecOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExecOrder.restype = c_void_p
        # 请求查询询价
        self.h.tReqQryForQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryForQuote.restype = c_void_p
        # 请求查询报价
        self.h.tReqQryQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryQuote.restype = c_void_p
        # 请求查询期权自对冲
        self.h.tReqQryOptionSelfClose.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionSelfClose.restype = c_void_p
        # 请求查询投资单元
        self.h.tReqQryInvestUnit.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestUnit.restype = c_void_p
        # 请求查询组合合约安全系数
        self.h.tReqQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombInstrumentGuard.restype = c_void_p
        # 请求查询申请组合
        self.h.tReqQryCombAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombAction.restype = c_void_p
        # 请求查询转帐流水
        self.h.tReqQryTransferSerial.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTransferSerial.restype = c_void_p
        # 请求查询银期签约关系
        self.h.tReqQryAccountregister.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryAccountregister.restype = c_void_p
        # 请求查询签约银行
        self.h.tReqQryContractBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryContractBank.restype = c_void_p
        # 请求查询预埋单
        self.h.tReqQryParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryParkedOrder.restype = c_void_p
        # 请求查询预埋撤单
        self.h.tReqQryParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryParkedOrderAction.restype = c_void_p
        # 请求查询交易通知
        self.h.tReqQryTradingNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingNotice.restype = c_void_p
        # 请求查询经纪公司交易参数
        self.h.tReqQryBrokerTradingParams.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryBrokerTradingParams.restype = c_void_p
        # 请求查询经纪公司交易算法
        self.h.tReqQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryBrokerTradingAlgos.restype = c_void_p
        # 请求查询监控中心用户令牌
        self.h.tReqQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQueryCFMMCTradingAccountToken.restype = c_void_p
        # 期货发起银行资金转期货请求
        self.h.tReqFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqFromBankToFutureByFuture.restype = c_void_p
        # 期货发起期货资金转银行请求
        self.h.tReqFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqFromFutureToBankByFuture.restype = c_void_p
        # 期货发起查询银行余额请求
        self.h.tReqQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQueryBankAccountMoneyByFuture.restype = c_void_p
        # 请求查询分类合约
        self.h.tReqQryClassifiedInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryClassifiedInstrument.restype = c_void_p
        # 请求组合优惠比例
        self.h.tReqQryCombPromotionParam.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombPromotionParam.restype = c_void_p
        # 投资者风险结算持仓查询
        self.h.tReqQryRiskSettleInvstPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryRiskSettleInvstPosition.restype = c_void_p
        # 风险结算产品查询
        self.h.tReqQryRiskSettleProductStatus.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryRiskSettleProductStatus.restype = c_void_p
        
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.tCreateApi()
        return self.api

    def CreateSpi(self):
        self.spi = self.h.tCreateSpi()
        #################### 响应函数 #########################
        # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        self.h.tSetOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnFrontConnected.restype = None
        self.evOnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.tSetOnFrontConnected(self.spi, self.evOnFrontConnected)
        # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        self.h.tSetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnFrontDisconnected.restype = None
        self.evOnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.tSetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)
        # 心跳超时警告。当长时间未收到报文时，该方法被调用。
        self.h.tSetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnHeartBeatWarning.restype = None
        self.evOnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.tSetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)
        # 客户端认证响应
        self.h.tSetOnRspAuthenticate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspAuthenticate.restype = None
        self.evOnRspAuthenticate = CFUNCTYPE(None, POINTER(CThostFtdcRspAuthenticateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspAuthenticate)
        self.h.tSetOnRspAuthenticate(self.spi, self.evOnRspAuthenticate)
        # 登录请求响应
        self.h.tSetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspUserLogin.restype = None
        self.evOnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.tSetOnRspUserLogin(self.spi, self.evOnRspUserLogin)
        # 登出请求响应
        self.h.tSetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspUserLogout.restype = None
        self.evOnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.tSetOnRspUserLogout(self.spi, self.evOnRspUserLogout)
        # 用户口令更新请求响应
        self.h.tSetOnRspUserPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspUserPasswordUpdate.restype = None
        self.evOnRspUserPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcUserPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserPasswordUpdate)
        self.h.tSetOnRspUserPasswordUpdate(self.spi, self.evOnRspUserPasswordUpdate)
        # 资金账户口令更新请求响应
        self.h.tSetOnRspTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspTradingAccountPasswordUpdate.restype = None
        self.evOnRspTradingAccountPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspTradingAccountPasswordUpdate)
        self.h.tSetOnRspTradingAccountPasswordUpdate(self.spi, self.evOnRspTradingAccountPasswordUpdate)
        # 查询用户当前支持的认证模式的回复
        self.h.tSetOnRspUserAuthMethod.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspUserAuthMethod.restype = None
        self.evOnRspUserAuthMethod = CFUNCTYPE(None, POINTER(CThostFtdcRspUserAuthMethodField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserAuthMethod)
        self.h.tSetOnRspUserAuthMethod(self.spi, self.evOnRspUserAuthMethod)
        # 获取图形验证码请求的回复
        self.h.tSetOnRspGenUserCaptcha.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspGenUserCaptcha.restype = None
        self.evOnRspGenUserCaptcha = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserCaptchaField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserCaptcha)
        self.h.tSetOnRspGenUserCaptcha(self.spi, self.evOnRspGenUserCaptcha)
        # 获取短信验证码请求的回复
        self.h.tSetOnRspGenUserText.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspGenUserText.restype = None
        self.evOnRspGenUserText = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserTextField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserText)
        self.h.tSetOnRspGenUserText(self.spi, self.evOnRspGenUserText)
        # 报单录入请求响应
        self.h.tSetOnRspOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspOrderInsert.restype = None
        self.evOnRspOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderInsert)
        self.h.tSetOnRspOrderInsert(self.spi, self.evOnRspOrderInsert)
        # 预埋单录入请求响应
        self.h.tSetOnRspParkedOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspParkedOrderInsert.restype = None
        self.evOnRspParkedOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderInsert)
        self.h.tSetOnRspParkedOrderInsert(self.spi, self.evOnRspParkedOrderInsert)
        # 预埋撤单录入请求响应
        self.h.tSetOnRspParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspParkedOrderAction.restype = None
        self.evOnRspParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderAction)
        self.h.tSetOnRspParkedOrderAction(self.spi, self.evOnRspParkedOrderAction)
        # 报单操作请求响应
        self.h.tSetOnRspOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspOrderAction.restype = None
        self.evOnRspOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderAction)
        self.h.tSetOnRspOrderAction(self.spi, self.evOnRspOrderAction)
        # 查询最大报单数量响应
        self.h.tSetOnRspQryMaxOrderVolume.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryMaxOrderVolume.restype = None
        self.evOnRspQryMaxOrderVolume = CFUNCTYPE(None, POINTER(CThostFtdcQryMaxOrderVolumeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMaxOrderVolume)
        self.h.tSetOnRspQryMaxOrderVolume(self.spi, self.evOnRspQryMaxOrderVolume)
        # 投资者结算结果确认响应
        self.h.tSetOnRspSettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspSettlementInfoConfirm.restype = None
        self.evOnRspSettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSettlementInfoConfirm)
        self.h.tSetOnRspSettlementInfoConfirm(self.spi, self.evOnRspSettlementInfoConfirm)
        # 删除预埋单响应
        self.h.tSetOnRspRemoveParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspRemoveParkedOrder.restype = None
        self.evOnRspRemoveParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrder)
        self.h.tSetOnRspRemoveParkedOrder(self.spi, self.evOnRspRemoveParkedOrder)
        # 删除预埋撤单响应
        self.h.tSetOnRspRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspRemoveParkedOrderAction.restype = None
        self.evOnRspRemoveParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrderAction)
        self.h.tSetOnRspRemoveParkedOrderAction(self.spi, self.evOnRspRemoveParkedOrderAction)
        # 执行宣告录入请求响应
        self.h.tSetOnRspExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspExecOrderInsert.restype = None
        self.evOnRspExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderInsert)
        self.h.tSetOnRspExecOrderInsert(self.spi, self.evOnRspExecOrderInsert)
        # 执行宣告操作请求响应
        self.h.tSetOnRspExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspExecOrderAction.restype = None
        self.evOnRspExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderAction)
        self.h.tSetOnRspExecOrderAction(self.spi, self.evOnRspExecOrderAction)
        # 询价录入请求响应
        self.h.tSetOnRspForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspForQuoteInsert.restype = None
        self.evOnRspForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspForQuoteInsert)
        self.h.tSetOnRspForQuoteInsert(self.spi, self.evOnRspForQuoteInsert)
        # 报价录入请求响应
        self.h.tSetOnRspQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQuoteInsert.restype = None
        self.evOnRspQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteInsert)
        self.h.tSetOnRspQuoteInsert(self.spi, self.evOnRspQuoteInsert)
        # 报价操作请求响应
        self.h.tSetOnRspQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQuoteAction.restype = None
        self.evOnRspQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteAction)
        self.h.tSetOnRspQuoteAction(self.spi, self.evOnRspQuoteAction)
        # 批量报单操作请求响应
        self.h.tSetOnRspBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspBatchOrderAction.restype = None
        self.evOnRspBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputBatchOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspBatchOrderAction)
        self.h.tSetOnRspBatchOrderAction(self.spi, self.evOnRspBatchOrderAction)
        # 期权自对冲录入请求响应
        self.h.tSetOnRspOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspOptionSelfCloseInsert.restype = None
        self.evOnRspOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseInsert)
        self.h.tSetOnRspOptionSelfCloseInsert(self.spi, self.evOnRspOptionSelfCloseInsert)
        # 期权自对冲操作请求响应
        self.h.tSetOnRspOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspOptionSelfCloseAction.restype = None
        self.evOnRspOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseAction)
        self.h.tSetOnRspOptionSelfCloseAction(self.spi, self.evOnRspOptionSelfCloseAction)
        # 申请组合录入请求响应
        self.h.tSetOnRspCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspCombActionInsert.restype = None
        self.evOnRspCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspCombActionInsert)
        self.h.tSetOnRspCombActionInsert(self.spi, self.evOnRspCombActionInsert)
        # 请求查询报单响应
        self.h.tSetOnRspQryOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryOrder.restype = None
        self.evOnRspQryOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOrder)
        self.h.tSetOnRspQryOrder(self.spi, self.evOnRspQryOrder)
        # 请求查询成交响应
        self.h.tSetOnRspQryTrade.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTrade.restype = None
        self.evOnRspQryTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTrade)
        self.h.tSetOnRspQryTrade(self.spi, self.evOnRspQryTrade)
        # 请求查询投资者持仓响应
        self.h.tSetOnRspQryInvestorPosition.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestorPosition.restype = None
        self.evOnRspQryInvestorPosition = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPosition)
        self.h.tSetOnRspQryInvestorPosition(self.spi, self.evOnRspQryInvestorPosition)
        # 请求查询资金账户响应
        self.h.tSetOnRspQryTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTradingAccount.restype = None
        self.evOnRspQryTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingAccount)
        self.h.tSetOnRspQryTradingAccount(self.spi, self.evOnRspQryTradingAccount)
        # 请求查询投资者响应
        self.h.tSetOnRspQryInvestor.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestor.restype = None
        self.evOnRspQryInvestor = CFUNCTYPE(None, POINTER(CThostFtdcInvestorField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestor)
        self.h.tSetOnRspQryInvestor(self.spi, self.evOnRspQryInvestor)
        # 请求查询交易编码响应
        self.h.tSetOnRspQryTradingCode.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTradingCode.restype = None
        self.evOnRspQryTradingCode = CFUNCTYPE(None, POINTER(CThostFtdcTradingCodeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingCode)
        self.h.tSetOnRspQryTradingCode(self.spi, self.evOnRspQryTradingCode)
        # 请求查询合约保证金率响应
        self.h.tSetOnRspQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInstrumentMarginRate.restype = None
        self.evOnRspQryInstrumentMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentMarginRate)
        self.h.tSetOnRspQryInstrumentMarginRate(self.spi, self.evOnRspQryInstrumentMarginRate)
        # 请求查询合约手续费率响应
        self.h.tSetOnRspQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInstrumentCommissionRate.restype = None
        self.evOnRspQryInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentCommissionRate)
        self.h.tSetOnRspQryInstrumentCommissionRate(self.spi, self.evOnRspQryInstrumentCommissionRate)
        # 请求查询交易所响应
        self.h.tSetOnRspQryExchange.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryExchange.restype = None
        self.evOnRspQryExchange = CFUNCTYPE(None, POINTER(CThostFtdcExchangeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchange)
        self.h.tSetOnRspQryExchange(self.spi, self.evOnRspQryExchange)
        # 请求查询产品响应
        self.h.tSetOnRspQryProduct.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryProduct.restype = None
        self.evOnRspQryProduct = CFUNCTYPE(None, POINTER(CThostFtdcProductField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProduct)
        self.h.tSetOnRspQryProduct(self.spi, self.evOnRspQryProduct)
        # 请求查询合约响应
        self.h.tSetOnRspQryInstrument.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInstrument.restype = None
        self.evOnRspQryInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrument)
        self.h.tSetOnRspQryInstrument(self.spi, self.evOnRspQryInstrument)
        # 请求查询行情响应
        self.h.tSetOnRspQryDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryDepthMarketData.restype = None
        self.evOnRspQryDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryDepthMarketData)
        self.h.tSetOnRspQryDepthMarketData(self.spi, self.evOnRspQryDepthMarketData)
        # 请求查询交易员报盘机响应
        self.h.tSetOnRspQryTraderOffer.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTraderOffer.restype = None
        self.evOnRspQryTraderOffer = CFUNCTYPE(None, POINTER(CThostFtdcTraderOfferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTraderOffer)
        self.h.tSetOnRspQryTraderOffer(self.spi, self.evOnRspQryTraderOffer)
        # 请求查询投资者结算结果响应
        self.h.tSetOnRspQrySettlementInfo.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySettlementInfo.restype = None
        self.evOnRspQrySettlementInfo = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfo)
        self.h.tSetOnRspQrySettlementInfo(self.spi, self.evOnRspQrySettlementInfo)
        # 请求查询转帐银行响应
        self.h.tSetOnRspQryTransferBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTransferBank.restype = None
        self.evOnRspQryTransferBank = CFUNCTYPE(None, POINTER(CThostFtdcTransferBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferBank)
        self.h.tSetOnRspQryTransferBank(self.spi, self.evOnRspQryTransferBank)
        # 请求查询投资者持仓明细响应
        self.h.tSetOnRspQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestorPositionDetail.restype = None
        self.evOnRspQryInvestorPositionDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionDetail)
        self.h.tSetOnRspQryInvestorPositionDetail(self.spi, self.evOnRspQryInvestorPositionDetail)
        # 请求查询客户通知响应
        self.h.tSetOnRspQryNotice.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryNotice.restype = None
        self.evOnRspQryNotice = CFUNCTYPE(None, POINTER(CThostFtdcNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryNotice)
        self.h.tSetOnRspQryNotice(self.spi, self.evOnRspQryNotice)
        # 请求查询结算信息确认响应
        self.h.tSetOnRspQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySettlementInfoConfirm.restype = None
        self.evOnRspQrySettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfoConfirm)
        self.h.tSetOnRspQrySettlementInfoConfirm(self.spi, self.evOnRspQrySettlementInfoConfirm)
        # 请求查询投资者持仓明细响应
        self.h.tSetOnRspQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestorPositionCombineDetail.restype = None
        self.evOnRspQryInvestorPositionCombineDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionCombineDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionCombineDetail)
        self.h.tSetOnRspQryInvestorPositionCombineDetail(self.spi, self.evOnRspQryInvestorPositionCombineDetail)
        # 查询保证金监管系统经纪公司资金账户密钥响应
        self.h.tSetOnRspQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryCFMMCTradingAccountKey.restype = None
        self.evOnRspQryCFMMCTradingAccountKey = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountKeyField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCFMMCTradingAccountKey)
        self.h.tSetOnRspQryCFMMCTradingAccountKey(self.spi, self.evOnRspQryCFMMCTradingAccountKey)
        # 请求查询仓单折抵信息响应
        self.h.tSetOnRspQryEWarrantOffset.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryEWarrantOffset.restype = None
        self.evOnRspQryEWarrantOffset = CFUNCTYPE(None, POINTER(CThostFtdcEWarrantOffsetField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryEWarrantOffset)
        self.h.tSetOnRspQryEWarrantOffset(self.spi, self.evOnRspQryEWarrantOffset)
        # 请求查询投资者品种/跨品种保证金响应
        self.h.tSetOnRspQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestorProductGroupMargin.restype = None
        self.evOnRspQryInvestorProductGroupMargin = CFUNCTYPE(None, POINTER(CThostFtdcInvestorProductGroupMarginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorProductGroupMargin)
        self.h.tSetOnRspQryInvestorProductGroupMargin(self.spi, self.evOnRspQryInvestorProductGroupMargin)
        # 请求查询交易所保证金率响应
        self.h.tSetOnRspQryExchangeMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryExchangeMarginRate.restype = None
        self.evOnRspQryExchangeMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRate)
        self.h.tSetOnRspQryExchangeMarginRate(self.spi, self.evOnRspQryExchangeMarginRate)
        # 请求查询交易所调整保证金率响应
        self.h.tSetOnRspQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryExchangeMarginRateAdjust.restype = None
        self.evOnRspQryExchangeMarginRateAdjust = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateAdjustField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRateAdjust)
        self.h.tSetOnRspQryExchangeMarginRateAdjust(self.spi, self.evOnRspQryExchangeMarginRateAdjust)
        # 请求查询汇率响应
        self.h.tSetOnRspQryExchangeRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryExchangeRate.restype = None
        self.evOnRspQryExchangeRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeRate)
        self.h.tSetOnRspQryExchangeRate(self.spi, self.evOnRspQryExchangeRate)
        # 请求查询二级代理操作员银期权限响应
        self.h.tSetOnRspQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySecAgentACIDMap.restype = None
        self.evOnRspQrySecAgentACIDMap = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentACIDMapField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentACIDMap)
        self.h.tSetOnRspQrySecAgentACIDMap(self.spi, self.evOnRspQrySecAgentACIDMap)
        # 请求查询产品报价汇率
        self.h.tSetOnRspQryProductExchRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryProductExchRate.restype = None
        self.evOnRspQryProductExchRate = CFUNCTYPE(None, POINTER(CThostFtdcProductExchRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductExchRate)
        self.h.tSetOnRspQryProductExchRate(self.spi, self.evOnRspQryProductExchRate)
        # 请求查询产品组
        self.h.tSetOnRspQryProductGroup.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryProductGroup.restype = None
        self.evOnRspQryProductGroup = CFUNCTYPE(None, POINTER(CThostFtdcProductGroupField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductGroup)
        self.h.tSetOnRspQryProductGroup(self.spi, self.evOnRspQryProductGroup)
        # 请求查询做市商合约手续费率响应
        self.h.tSetOnRspQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryMMInstrumentCommissionRate.restype = None
        self.evOnRspQryMMInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcMMInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMInstrumentCommissionRate)
        self.h.tSetOnRspQryMMInstrumentCommissionRate(self.spi, self.evOnRspQryMMInstrumentCommissionRate)
        # 请求查询做市商期权合约手续费响应
        self.h.tSetOnRspQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryMMOptionInstrCommRate.restype = None
        self.evOnRspQryMMOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcMMOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMOptionInstrCommRate)
        self.h.tSetOnRspQryMMOptionInstrCommRate(self.spi, self.evOnRspQryMMOptionInstrCommRate)
        # 请求查询报单手续费响应
        self.h.tSetOnRspQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInstrumentOrderCommRate.restype = None
        self.evOnRspQryInstrumentOrderCommRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentOrderCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentOrderCommRate)
        self.h.tSetOnRspQryInstrumentOrderCommRate(self.spi, self.evOnRspQryInstrumentOrderCommRate)
        # 请求查询资金账户响应
        self.h.tSetOnRspQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySecAgentTradingAccount.restype = None
        self.evOnRspQrySecAgentTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradingAccount)
        self.h.tSetOnRspQrySecAgentTradingAccount(self.spi, self.evOnRspQrySecAgentTradingAccount)
        # 请求查询二级代理商资金校验模式响应
        self.h.tSetOnRspQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySecAgentCheckMode.restype = None
        self.evOnRspQrySecAgentCheckMode = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentCheckModeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentCheckMode)
        self.h.tSetOnRspQrySecAgentCheckMode(self.spi, self.evOnRspQrySecAgentCheckMode)
        # 请求查询二级代理商信息响应
        self.h.tSetOnRspQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQrySecAgentTradeInfo.restype = None
        self.evOnRspQrySecAgentTradeInfo = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentTradeInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradeInfo)
        self.h.tSetOnRspQrySecAgentTradeInfo(self.spi, self.evOnRspQrySecAgentTradeInfo)
        # 请求查询期权交易成本响应
        self.h.tSetOnRspQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryOptionInstrTradeCost.restype = None
        self.evOnRspQryOptionInstrTradeCost = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrTradeCostField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrTradeCost)
        self.h.tSetOnRspQryOptionInstrTradeCost(self.spi, self.evOnRspQryOptionInstrTradeCost)
        # 请求查询期权合约手续费响应
        self.h.tSetOnRspQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryOptionInstrCommRate.restype = None
        self.evOnRspQryOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrCommRate)
        self.h.tSetOnRspQryOptionInstrCommRate(self.spi, self.evOnRspQryOptionInstrCommRate)
        # 请求查询执行宣告响应
        self.h.tSetOnRspQryExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryExecOrder.restype = None
        self.evOnRspQryExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExecOrder)
        self.h.tSetOnRspQryExecOrder(self.spi, self.evOnRspQryExecOrder)
        # 请求查询询价响应
        self.h.tSetOnRspQryForQuote.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryForQuote.restype = None
        self.evOnRspQryForQuote = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryForQuote)
        self.h.tSetOnRspQryForQuote(self.spi, self.evOnRspQryForQuote)
        # 请求查询报价响应
        self.h.tSetOnRspQryQuote.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryQuote.restype = None
        self.evOnRspQryQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryQuote)
        self.h.tSetOnRspQryQuote(self.spi, self.evOnRspQryQuote)
        # 请求查询期权自对冲响应
        self.h.tSetOnRspQryOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryOptionSelfClose.restype = None
        self.evOnRspQryOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionSelfClose)
        self.h.tSetOnRspQryOptionSelfClose(self.spi, self.evOnRspQryOptionSelfClose)
        # 请求查询投资单元响应
        self.h.tSetOnRspQryInvestUnit.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryInvestUnit.restype = None
        self.evOnRspQryInvestUnit = CFUNCTYPE(None, POINTER(CThostFtdcInvestUnitField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestUnit)
        self.h.tSetOnRspQryInvestUnit(self.spi, self.evOnRspQryInvestUnit)
        # 请求查询组合合约安全系数响应
        self.h.tSetOnRspQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryCombInstrumentGuard.restype = None
        self.evOnRspQryCombInstrumentGuard = CFUNCTYPE(None, POINTER(CThostFtdcCombInstrumentGuardField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombInstrumentGuard)
        self.h.tSetOnRspQryCombInstrumentGuard(self.spi, self.evOnRspQryCombInstrumentGuard)
        # 请求查询申请组合响应
        self.h.tSetOnRspQryCombAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryCombAction.restype = None
        self.evOnRspQryCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombAction)
        self.h.tSetOnRspQryCombAction(self.spi, self.evOnRspQryCombAction)
        # 请求查询转帐流水响应
        self.h.tSetOnRspQryTransferSerial.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTransferSerial.restype = None
        self.evOnRspQryTransferSerial = CFUNCTYPE(None, POINTER(CThostFtdcTransferSerialField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferSerial)
        self.h.tSetOnRspQryTransferSerial(self.spi, self.evOnRspQryTransferSerial)
        # 请求查询银期签约关系响应
        self.h.tSetOnRspQryAccountregister.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryAccountregister.restype = None
        self.evOnRspQryAccountregister = CFUNCTYPE(None, POINTER(CThostFtdcAccountregisterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryAccountregister)
        self.h.tSetOnRspQryAccountregister(self.spi, self.evOnRspQryAccountregister)
        # 错误应答
        self.h.tSetOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspError.restype = None
        self.evOnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.tSetOnRspError(self.spi, self.evOnRspError)
        # 报单通知
        self.h.tSetOnRtnOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnOrder.restype = None
        self.evOnRtnOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField))(self.__OnRtnOrder)
        self.h.tSetOnRtnOrder(self.spi, self.evOnRtnOrder)
        # 成交通知
        self.h.tSetOnRtnTrade.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnTrade.restype = None
        self.evOnRtnTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField))(self.__OnRtnTrade)
        self.h.tSetOnRtnTrade(self.spi, self.evOnRtnTrade)
        # 报单录入错误回报
        self.h.tSetOnErrRtnOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnOrderInsert.restype = None
        self.evOnErrRtnOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderInsert)
        self.h.tSetOnErrRtnOrderInsert(self.spi, self.evOnErrRtnOrderInsert)
        # 报单操作错误回报
        self.h.tSetOnErrRtnOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnOrderAction.restype = None
        self.evOnErrRtnOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderAction)
        self.h.tSetOnErrRtnOrderAction(self.spi, self.evOnErrRtnOrderAction)
        # 合约交易状态通知
        self.h.tSetOnRtnInstrumentStatus.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnInstrumentStatus.restype = None
        self.evOnRtnInstrumentStatus = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentStatusField))(self.__OnRtnInstrumentStatus)
        self.h.tSetOnRtnInstrumentStatus(self.spi, self.evOnRtnInstrumentStatus)
        # 交易所公告通知
        self.h.tSetOnRtnBulletin.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnBulletin.restype = None
        self.evOnRtnBulletin = CFUNCTYPE(None, POINTER(CThostFtdcBulletinField))(self.__OnRtnBulletin)
        self.h.tSetOnRtnBulletin(self.spi, self.evOnRtnBulletin)
        # 交易通知
        self.h.tSetOnRtnTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnTradingNotice.restype = None
        self.evOnRtnTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeInfoField))(self.__OnRtnTradingNotice)
        self.h.tSetOnRtnTradingNotice(self.spi, self.evOnRtnTradingNotice)
        # 提示条件单校验错误
        self.h.tSetOnRtnErrorConditionalOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnErrorConditionalOrder.restype = None
        self.evOnRtnErrorConditionalOrder = CFUNCTYPE(None, POINTER(CThostFtdcErrorConditionalOrderField))(self.__OnRtnErrorConditionalOrder)
        self.h.tSetOnRtnErrorConditionalOrder(self.spi, self.evOnRtnErrorConditionalOrder)
        # 执行宣告通知
        self.h.tSetOnRtnExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnExecOrder.restype = None
        self.evOnRtnExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField))(self.__OnRtnExecOrder)
        self.h.tSetOnRtnExecOrder(self.spi, self.evOnRtnExecOrder)
        # 执行宣告录入错误回报
        self.h.tSetOnErrRtnExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnExecOrderInsert.restype = None
        self.evOnErrRtnExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderInsert)
        self.h.tSetOnErrRtnExecOrderInsert(self.spi, self.evOnErrRtnExecOrderInsert)
        # 执行宣告操作错误回报
        self.h.tSetOnErrRtnExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnExecOrderAction.restype = None
        self.evOnErrRtnExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderAction)
        self.h.tSetOnErrRtnExecOrderAction(self.spi, self.evOnErrRtnExecOrderAction)
        # 询价录入错误回报
        self.h.tSetOnErrRtnForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnForQuoteInsert.restype = None
        self.evOnErrRtnForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnForQuoteInsert)
        self.h.tSetOnErrRtnForQuoteInsert(self.spi, self.evOnErrRtnForQuoteInsert)
        # 报价通知
        self.h.tSetOnRtnQuote.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnQuote.restype = None
        self.evOnRtnQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField))(self.__OnRtnQuote)
        self.h.tSetOnRtnQuote(self.spi, self.evOnRtnQuote)
        # 报价录入错误回报
        self.h.tSetOnErrRtnQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnQuoteInsert.restype = None
        self.evOnErrRtnQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteInsert)
        self.h.tSetOnErrRtnQuoteInsert(self.spi, self.evOnErrRtnQuoteInsert)
        # 报价操作错误回报
        self.h.tSetOnErrRtnQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnQuoteAction.restype = None
        self.evOnErrRtnQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcQuoteActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteAction)
        self.h.tSetOnErrRtnQuoteAction(self.spi, self.evOnErrRtnQuoteAction)
        # 询价通知
        self.h.tSetOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnForQuoteRsp.restype = None
        self.evOnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.tSetOnRtnForQuoteRsp(self.spi, self.evOnRtnForQuoteRsp)
        # 保证金监控中心用户令牌
        self.h.tSetOnRtnCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnCFMMCTradingAccountToken.restype = None
        self.evOnRtnCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountTokenField))(self.__OnRtnCFMMCTradingAccountToken)
        self.h.tSetOnRtnCFMMCTradingAccountToken(self.spi, self.evOnRtnCFMMCTradingAccountToken)
        # 批量报单操作错误回报
        self.h.tSetOnErrRtnBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnBatchOrderAction.restype = None
        self.evOnErrRtnBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcBatchOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBatchOrderAction)
        self.h.tSetOnErrRtnBatchOrderAction(self.spi, self.evOnErrRtnBatchOrderAction)
        # 期权自对冲通知
        self.h.tSetOnRtnOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnOptionSelfClose.restype = None
        self.evOnRtnOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField))(self.__OnRtnOptionSelfClose)
        self.h.tSetOnRtnOptionSelfClose(self.spi, self.evOnRtnOptionSelfClose)
        # 期权自对冲录入错误回报
        self.h.tSetOnErrRtnOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnOptionSelfCloseInsert.restype = None
        self.evOnErrRtnOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseInsert)
        self.h.tSetOnErrRtnOptionSelfCloseInsert(self.spi, self.evOnErrRtnOptionSelfCloseInsert)
        # 期权自对冲操作错误回报
        self.h.tSetOnErrRtnOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnOptionSelfCloseAction.restype = None
        self.evOnErrRtnOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseAction)
        self.h.tSetOnErrRtnOptionSelfCloseAction(self.spi, self.evOnErrRtnOptionSelfCloseAction)
        # 申请组合通知
        self.h.tSetOnRtnCombAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnCombAction.restype = None
        self.evOnRtnCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField))(self.__OnRtnCombAction)
        self.h.tSetOnRtnCombAction(self.spi, self.evOnRtnCombAction)
        # 申请组合录入错误回报
        self.h.tSetOnErrRtnCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnCombActionInsert.restype = None
        self.evOnErrRtnCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnCombActionInsert)
        self.h.tSetOnErrRtnCombActionInsert(self.spi, self.evOnErrRtnCombActionInsert)
        # 请求查询签约银行响应
        self.h.tSetOnRspQryContractBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryContractBank.restype = None
        self.evOnRspQryContractBank = CFUNCTYPE(None, POINTER(CThostFtdcContractBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryContractBank)
        self.h.tSetOnRspQryContractBank(self.spi, self.evOnRspQryContractBank)
        # 请求查询预埋单响应
        self.h.tSetOnRspQryParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryParkedOrder.restype = None
        self.evOnRspQryParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrder)
        self.h.tSetOnRspQryParkedOrder(self.spi, self.evOnRspQryParkedOrder)
        # 请求查询预埋撤单响应
        self.h.tSetOnRspQryParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryParkedOrderAction.restype = None
        self.evOnRspQryParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrderAction)
        self.h.tSetOnRspQryParkedOrderAction(self.spi, self.evOnRspQryParkedOrderAction)
        # 请求查询交易通知响应
        self.h.tSetOnRspQryTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryTradingNotice.restype = None
        self.evOnRspQryTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingNotice)
        self.h.tSetOnRspQryTradingNotice(self.spi, self.evOnRspQryTradingNotice)
        # 请求查询经纪公司交易参数响应
        self.h.tSetOnRspQryBrokerTradingParams.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryBrokerTradingParams.restype = None
        self.evOnRspQryBrokerTradingParams = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingParamsField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingParams)
        self.h.tSetOnRspQryBrokerTradingParams(self.spi, self.evOnRspQryBrokerTradingParams)
        # 请求查询经纪公司交易算法响应
        self.h.tSetOnRspQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryBrokerTradingAlgos.restype = None
        self.evOnRspQryBrokerTradingAlgos = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingAlgosField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingAlgos)
        self.h.tSetOnRspQryBrokerTradingAlgos(self.spi, self.evOnRspQryBrokerTradingAlgos)
        # 请求查询监控中心用户令牌
        self.h.tSetOnRspQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQueryCFMMCTradingAccountToken.restype = None
        self.evOnRspQueryCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryCFMMCTradingAccountToken)
        self.h.tSetOnRspQueryCFMMCTradingAccountToken(self.spi, self.evOnRspQueryCFMMCTradingAccountToken)
        # 银行发起银行资金转期货通知
        self.h.tSetOnRtnFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnFromBankToFutureByBank.restype = None
        self.evOnRtnFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByBank)
        self.h.tSetOnRtnFromBankToFutureByBank(self.spi, self.evOnRtnFromBankToFutureByBank)
        # 银行发起期货资金转银行通知
        self.h.tSetOnRtnFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnFromFutureToBankByBank.restype = None
        self.evOnRtnFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByBank)
        self.h.tSetOnRtnFromFutureToBankByBank(self.spi, self.evOnRtnFromFutureToBankByBank)
        # 银行发起冲正银行转期货通知
        self.h.tSetOnRtnRepealFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromBankToFutureByBank.restype = None
        self.evOnRtnRepealFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByBank)
        self.h.tSetOnRtnRepealFromBankToFutureByBank(self.spi, self.evOnRtnRepealFromBankToFutureByBank)
        # 银行发起冲正期货转银行通知
        self.h.tSetOnRtnRepealFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromFutureToBankByBank.restype = None
        self.evOnRtnRepealFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByBank)
        self.h.tSetOnRtnRepealFromFutureToBankByBank(self.spi, self.evOnRtnRepealFromFutureToBankByBank)
        # 期货发起银行资金转期货通知
        self.h.tSetOnRtnFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnFromBankToFutureByFuture.restype = None
        self.evOnRtnFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByFuture)
        self.h.tSetOnRtnFromBankToFutureByFuture(self.spi, self.evOnRtnFromBankToFutureByFuture)
        # 期货发起期货资金转银行通知
        self.h.tSetOnRtnFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnFromFutureToBankByFuture.restype = None
        self.evOnRtnFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByFuture)
        self.h.tSetOnRtnFromFutureToBankByFuture(self.spi, self.evOnRtnFromFutureToBankByFuture)
        # 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        self.h.tSetOnRtnRepealFromBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromBankToFutureByFutureManual.restype = None
        self.evOnRtnRepealFromBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFutureManual)
        self.h.tSetOnRtnRepealFromBankToFutureByFutureManual(self.spi, self.evOnRtnRepealFromBankToFutureByFutureManual)
        # 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        self.h.tSetOnRtnRepealFromFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromFutureToBankByFutureManual.restype = None
        self.evOnRtnRepealFromFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFutureManual)
        self.h.tSetOnRtnRepealFromFutureToBankByFutureManual(self.spi, self.evOnRtnRepealFromFutureToBankByFutureManual)
        # 期货发起查询银行余额通知
        self.h.tSetOnRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnQueryBankBalanceByFuture.restype = None
        self.evOnRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcNotifyQueryAccountField))(self.__OnRtnQueryBankBalanceByFuture)
        self.h.tSetOnRtnQueryBankBalanceByFuture(self.spi, self.evOnRtnQueryBankBalanceByFuture)
        # 期货发起银行资金转期货错误回报
        self.h.tSetOnErrRtnBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnBankToFutureByFuture.restype = None
        self.evOnErrRtnBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBankToFutureByFuture)
        self.h.tSetOnErrRtnBankToFutureByFuture(self.spi, self.evOnErrRtnBankToFutureByFuture)
        # 期货发起期货资金转银行错误回报
        self.h.tSetOnErrRtnFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnFutureToBankByFuture.restype = None
        self.evOnErrRtnFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnFutureToBankByFuture)
        self.h.tSetOnErrRtnFutureToBankByFuture(self.spi, self.evOnErrRtnFutureToBankByFuture)
        # 系统运行时期货端手工发起冲正银行转期货错误回报
        self.h.tSetOnErrRtnRepealBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnRepealBankToFutureByFutureManual.restype = None
        self.evOnErrRtnRepealBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealBankToFutureByFutureManual)
        self.h.tSetOnErrRtnRepealBankToFutureByFutureManual(self.spi, self.evOnErrRtnRepealBankToFutureByFutureManual)
        # 系统运行时期货端手工发起冲正期货转银行错误回报
        self.h.tSetOnErrRtnRepealFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnRepealFutureToBankByFutureManual.restype = None
        self.evOnErrRtnRepealFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealFutureToBankByFutureManual)
        self.h.tSetOnErrRtnRepealFutureToBankByFutureManual(self.spi, self.evOnErrRtnRepealFutureToBankByFutureManual)
        # 期货发起查询银行余额错误回报
        self.h.tSetOnErrRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnErrRtnQueryBankBalanceByFuture.restype = None
        self.evOnErrRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQueryBankBalanceByFuture)
        self.h.tSetOnErrRtnQueryBankBalanceByFuture(self.spi, self.evOnErrRtnQueryBankBalanceByFuture)
        # 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        self.h.tSetOnRtnRepealFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromBankToFutureByFuture.restype = None
        self.evOnRtnRepealFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFuture)
        self.h.tSetOnRtnRepealFromBankToFutureByFuture(self.spi, self.evOnRtnRepealFromBankToFutureByFuture)
        # 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        self.h.tSetOnRtnRepealFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnRepealFromFutureToBankByFuture.restype = None
        self.evOnRtnRepealFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFuture)
        self.h.tSetOnRtnRepealFromFutureToBankByFuture(self.spi, self.evOnRtnRepealFromFutureToBankByFuture)
        # 期货发起银行资金转期货应答
        self.h.tSetOnRspFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspFromBankToFutureByFuture.restype = None
        self.evOnRspFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromBankToFutureByFuture)
        self.h.tSetOnRspFromBankToFutureByFuture(self.spi, self.evOnRspFromBankToFutureByFuture)
        # 期货发起期货资金转银行应答
        self.h.tSetOnRspFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspFromFutureToBankByFuture.restype = None
        self.evOnRspFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromFutureToBankByFuture)
        self.h.tSetOnRspFromFutureToBankByFuture(self.spi, self.evOnRspFromFutureToBankByFuture)
        # 期货发起查询银行余额应答
        self.h.tSetOnRspQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQueryBankAccountMoneyByFuture.restype = None
        self.evOnRspQueryBankAccountMoneyByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryBankAccountMoneyByFuture)
        self.h.tSetOnRspQueryBankAccountMoneyByFuture(self.spi, self.evOnRspQueryBankAccountMoneyByFuture)
        # 银行发起银期开户通知
        self.h.tSetOnRtnOpenAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnOpenAccountByBank.restype = None
        self.evOnRtnOpenAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcOpenAccountField))(self.__OnRtnOpenAccountByBank)
        self.h.tSetOnRtnOpenAccountByBank(self.spi, self.evOnRtnOpenAccountByBank)
        # 银行发起银期销户通知
        self.h.tSetOnRtnCancelAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnCancelAccountByBank.restype = None
        self.evOnRtnCancelAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcCancelAccountField))(self.__OnRtnCancelAccountByBank)
        self.h.tSetOnRtnCancelAccountByBank(self.spi, self.evOnRtnCancelAccountByBank)
        # 银行发起变更银行账号通知
        self.h.tSetOnRtnChangeAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRtnChangeAccountByBank.restype = None
        self.evOnRtnChangeAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcChangeAccountField))(self.__OnRtnChangeAccountByBank)
        self.h.tSetOnRtnChangeAccountByBank(self.spi, self.evOnRtnChangeAccountByBank)
        # 请求查询分类合约响应
        self.h.tSetOnRspQryClassifiedInstrument.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryClassifiedInstrument.restype = None
        self.evOnRspQryClassifiedInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryClassifiedInstrument)
        self.h.tSetOnRspQryClassifiedInstrument(self.spi, self.evOnRspQryClassifiedInstrument)
        # 请求组合优惠比例响应
        self.h.tSetOnRspQryCombPromotionParam.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryCombPromotionParam.restype = None
        self.evOnRspQryCombPromotionParam = CFUNCTYPE(None, POINTER(CThostFtdcCombPromotionParamField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombPromotionParam)
        self.h.tSetOnRspQryCombPromotionParam(self.spi, self.evOnRspQryCombPromotionParam)
        # 投资者风险结算持仓查询响应
        self.h.tSetOnRspQryRiskSettleInvstPosition.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryRiskSettleInvstPosition.restype = None
        self.evOnRspQryRiskSettleInvstPosition = CFUNCTYPE(None, POINTER(CThostFtdcRiskSettleInvstPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryRiskSettleInvstPosition)
        self.h.tSetOnRspQryRiskSettleInvstPosition(self.spi, self.evOnRspQryRiskSettleInvstPosition)
        # 风险结算产品查询响应
        self.h.tSetOnRspQryRiskSettleProductStatus.argtypes = [c_void_p, c_void_p]
        self.h.tSetOnRspQryRiskSettleProductStatus.restype = None
        self.evOnRspQryRiskSettleProductStatus = CFUNCTYPE(None, POINTER(CThostFtdcRiskSettleProductStatusField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryRiskSettleProductStatus)
        self.h.tSetOnRspQryRiskSettleProductStatus(self.spi, self.evOnRspQryRiskSettleProductStatus)
        
        return self.spi

    def GetVersion(self):
        v = str(self.h.tGetVersion(), encoding='ascii')
        return str(v)

    #################### 请求函数 #######################
    
    def Release(self):
        """ 创建TraderApi """
        self.h.tRelease(self.api)
    
    def Init(self):
        """ 初始化 """
        self.h.tInit(self.api)
    
    def Join(self):
        """ 等待接口线程结束运行 """
        self.h.tJoin(self.api)
    
    def RegisterFront(self, pszFrontAddress:str):
        """ 注册前置机网络地址 """
        self.h.tRegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))
    
    def RegisterNameServer(self, pszNsAddress:str):
        """ @remark RegisterNameServer优先于RegisterFront """
        self.h.tRegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))
    
    def RegisterFensUserInfo(self,  pFensUserInfo:CThostFtdcFensUserInfoField):
        """ 注册名字服务器用户信息 """
        self.h.tRegisterFensUserInfo(self.api, byref( pFensUserInfo))
    
    def RegisterSpi(self, pSpi:c_void_p):
        """ 注册回调接口 """
        self.h.tRegisterSpi(self.api, pSpi)
    
    def SubscribePrivateTopic(self, nResumeType:THOST_TE_RESUME_TYPE):
        """ 订阅私有流。 """
        self.h.tSubscribePrivateTopic(self.api, nResumeType)
    
    def SubscribePublicTopic(self, nResumeType:THOST_TE_RESUME_TYPE):
        """ 订阅公共流。 """
        self.h.tSubscribePublicTopic(self.api, nResumeType)
    
    def ReqAuthenticate(self, pReqAuthenticateField:CThostFtdcReqAuthenticateField, nRequestID:int):
        """ 客户端认证请求 """
        self.h.tReqAuthenticate(self.api, byref(pReqAuthenticateField), nRequestID)
    
    def RegisterUserSystemInfo(self, pUserSystemInfo:CThostFtdcUserSystemInfoField):
        """ 注册用户终端信息，用于中继服务器多连接模式 """
        self.h.tRegisterUserSystemInfo(self.api, byref(pUserSystemInfo))
    
    def SubmitUserSystemInfo(self, pUserSystemInfo:CThostFtdcUserSystemInfoField):
        """ 上报用户终端信息，用于中继服务器操作员登录模式 """
        self.h.tSubmitUserSystemInfo(self.api, byref(pUserSystemInfo))
    
    def ReqUserLogin(self, pReqUserLoginField:CThostFtdcReqUserLoginField, nRequestID:int):
        """ 用户登录请求 """
        self.h.tReqUserLogin(self.api, byref(pReqUserLoginField), nRequestID)
    
    def ReqUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, nRequestID:int):
        """ 登出请求 """
        self.h.tReqUserLogout(self.api, byref(pUserLogout), nRequestID)
    
    def ReqUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, nRequestID:int):
        """ 用户口令更新请求 """
        self.h.tReqUserPasswordUpdate(self.api, byref(pUserPasswordUpdate), nRequestID)
    
    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, nRequestID:int):
        """ 资金账户口令更新请求 """
        self.h.tReqTradingAccountPasswordUpdate(self.api, byref(pTradingAccountPasswordUpdate), nRequestID)
    
    def ReqUserAuthMethod(self, pReqUserAuthMethod:CThostFtdcReqUserAuthMethodField, nRequestID:int):
        """ 查询用户当前支持的认证模式 """
        self.h.tReqUserAuthMethod(self.api, byref(pReqUserAuthMethod), nRequestID)
    
    def ReqGenUserCaptcha(self, pReqGenUserCaptcha:CThostFtdcReqGenUserCaptchaField, nRequestID:int):
        """ 用户发出获取图形验证码请求 """
        self.h.tReqGenUserCaptcha(self.api, byref(pReqGenUserCaptcha), nRequestID)
    
    def ReqGenUserText(self, pReqGenUserText:CThostFtdcReqGenUserTextField, nRequestID:int):
        """ 用户发出获取短信验证码请求 """
        self.h.tReqGenUserText(self.api, byref(pReqGenUserText), nRequestID)
    
    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha:CThostFtdcReqUserLoginWithCaptchaField, nRequestID:int):
        """ 用户发出带有图片验证码的登陆请求 """
        self.h.tReqUserLoginWithCaptcha(self.api, byref(pReqUserLoginWithCaptcha), nRequestID)
    
    def ReqUserLoginWithText(self, pReqUserLoginWithText:CThostFtdcReqUserLoginWithTextField, nRequestID:int):
        """ 用户发出带有短信验证码的登陆请求 """
        self.h.tReqUserLoginWithText(self.api, byref(pReqUserLoginWithText), nRequestID)
    
    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP:CThostFtdcReqUserLoginWithOTPField, nRequestID:int):
        """ 用户发出带有动态口令的登陆请求 """
        self.h.tReqUserLoginWithOTP(self.api, byref(pReqUserLoginWithOTP), nRequestID)
    
    def ReqOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, nRequestID:int):
        """ 报单录入请求 """
        self.h.tReqOrderInsert(self.api, byref(pInputOrder), nRequestID)
    
    def ReqParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, nRequestID:int):
        """ 预埋单录入请求 """
        self.h.tReqParkedOrderInsert(self.api, byref(pParkedOrder), nRequestID)
    
    def ReqParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, nRequestID:int):
        """ 预埋撤单录入请求 """
        self.h.tReqParkedOrderAction(self.api, byref(pParkedOrderAction), nRequestID)
    
    def ReqOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, nRequestID:int):
        """ 报单操作请求 """
        self.h.tReqOrderAction(self.api, byref(pInputOrderAction), nRequestID)
    
    def ReqQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, nRequestID:int):
        """ 查询最大报单数量请求 """
        self.h.tReqQryMaxOrderVolume(self.api, byref(pQryMaxOrderVolume), nRequestID)
    
    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, nRequestID:int):
        """ 投资者结算结果确认 """
        self.h.tReqSettlementInfoConfirm(self.api, byref(pSettlementInfoConfirm), nRequestID)
    
    def ReqRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, nRequestID:int):
        """ 请求删除预埋单 """
        self.h.tReqRemoveParkedOrder(self.api, byref(pRemoveParkedOrder), nRequestID)
    
    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, nRequestID:int):
        """ 请求删除预埋撤单 """
        self.h.tReqRemoveParkedOrderAction(self.api, byref(pRemoveParkedOrderAction), nRequestID)
    
    def ReqExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, nRequestID:int):
        """ 执行宣告录入请求 """
        self.h.tReqExecOrderInsert(self.api, byref(pInputExecOrder), nRequestID)
    
    def ReqExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, nRequestID:int):
        """ 执行宣告操作请求 """
        self.h.tReqExecOrderAction(self.api, byref(pInputExecOrderAction), nRequestID)
    
    def ReqForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, nRequestID:int):
        """ 询价录入请求 """
        self.h.tReqForQuoteInsert(self.api, byref(pInputForQuote), nRequestID)
    
    def ReqQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, nRequestID:int):
        """ 报价录入请求 """
        self.h.tReqQuoteInsert(self.api, byref(pInputQuote), nRequestID)
    
    def ReqQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, nRequestID:int):
        """ 报价操作请求 """
        self.h.tReqQuoteAction(self.api, byref(pInputQuoteAction), nRequestID)
    
    def ReqBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, nRequestID:int):
        """ 批量报单操作请求 """
        self.h.tReqBatchOrderAction(self.api, byref(pInputBatchOrderAction), nRequestID)
    
    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, nRequestID:int):
        """ 期权自对冲录入请求 """
        self.h.tReqOptionSelfCloseInsert(self.api, byref(pInputOptionSelfClose), nRequestID)
    
    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, nRequestID:int):
        """ 期权自对冲操作请求 """
        self.h.tReqOptionSelfCloseAction(self.api, byref(pInputOptionSelfCloseAction), nRequestID)
    
    def ReqCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, nRequestID:int):
        """ 申请组合录入请求 """
        self.h.tReqCombActionInsert(self.api, byref(pInputCombAction), nRequestID)
    
    def ReqQryOrder(self, pQryOrder:CThostFtdcQryOrderField, nRequestID:int):
        """ 请求查询报单 """
        self.h.tReqQryOrder(self.api, byref(pQryOrder), nRequestID)
    
    def ReqQryTrade(self, pQryTrade:CThostFtdcQryTradeField, nRequestID:int):
        """ 请求查询成交 """
        self.h.tReqQryTrade(self.api, byref(pQryTrade), nRequestID)
    
    def ReqQryInvestorPosition(self, pQryInvestorPosition:CThostFtdcQryInvestorPositionField, nRequestID:int):
        """ 请求查询投资者持仓 """
        self.h.tReqQryInvestorPosition(self.api, byref(pQryInvestorPosition), nRequestID)
    
    def ReqQryTradingAccount(self, pQryTradingAccount:CThostFtdcQryTradingAccountField, nRequestID:int):
        """ 请求查询资金账户 """
        self.h.tReqQryTradingAccount(self.api, byref(pQryTradingAccount), nRequestID)
    
    def ReqQryInvestor(self, pQryInvestor:CThostFtdcQryInvestorField, nRequestID:int):
        """ 请求查询投资者 """
        self.h.tReqQryInvestor(self.api, byref(pQryInvestor), nRequestID)
    
    def ReqQryTradingCode(self, pQryTradingCode:CThostFtdcQryTradingCodeField, nRequestID:int):
        """ 请求查询交易编码 """
        self.h.tReqQryTradingCode(self.api, byref(pQryTradingCode), nRequestID)
    
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate:CThostFtdcQryInstrumentMarginRateField, nRequestID:int):
        """ 请求查询合约保证金率 """
        self.h.tReqQryInstrumentMarginRate(self.api, byref(pQryInstrumentMarginRate), nRequestID)
    
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate:CThostFtdcQryInstrumentCommissionRateField, nRequestID:int):
        """ 请求查询合约手续费率 """
        self.h.tReqQryInstrumentCommissionRate(self.api, byref(pQryInstrumentCommissionRate), nRequestID)
    
    def ReqQryExchange(self, pQryExchange:CThostFtdcQryExchangeField, nRequestID:int):
        """ 请求查询交易所 """
        self.h.tReqQryExchange(self.api, byref(pQryExchange), nRequestID)
    
    def ReqQryProduct(self, pQryProduct:CThostFtdcQryProductField, nRequestID:int):
        """ 请求查询产品 """
        self.h.tReqQryProduct(self.api, byref(pQryProduct), nRequestID)
    
    def ReqQryInstrument(self, pQryInstrument:CThostFtdcQryInstrumentField, nRequestID:int):
        """ 请求查询合约 """
        self.h.tReqQryInstrument(self.api, byref(pQryInstrument), nRequestID)
    
    def ReqQryDepthMarketData(self, pQryDepthMarketData:CThostFtdcQryDepthMarketDataField, nRequestID:int):
        """ 请求查询行情 """
        self.h.tReqQryDepthMarketData(self.api, byref(pQryDepthMarketData), nRequestID)
    
    def ReqQryTraderOffer(self, pQryTraderOffer:CThostFtdcQryTraderOfferField, nRequestID:int):
        """ 请求查询交易员报盘机 """
        self.h.tReqQryTraderOffer(self.api, byref(pQryTraderOffer), nRequestID)
    
    def ReqQrySettlementInfo(self, pQrySettlementInfo:CThostFtdcQrySettlementInfoField, nRequestID:int):
        """ 请求查询投资者结算结果 """
        self.h.tReqQrySettlementInfo(self.api, byref(pQrySettlementInfo), nRequestID)
    
    def ReqQryTransferBank(self, pQryTransferBank:CThostFtdcQryTransferBankField, nRequestID:int):
        """ 请求查询转帐银行 """
        self.h.tReqQryTransferBank(self.api, byref(pQryTransferBank), nRequestID)
    
    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail:CThostFtdcQryInvestorPositionDetailField, nRequestID:int):
        """ 请求查询投资者持仓明细 """
        self.h.tReqQryInvestorPositionDetail(self.api, byref(pQryInvestorPositionDetail), nRequestID)
    
    def ReqQryNotice(self, pQryNotice:CThostFtdcQryNoticeField, nRequestID:int):
        """ 请求查询客户通知 """
        self.h.tReqQryNotice(self.api, byref(pQryNotice), nRequestID)
    
    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm:CThostFtdcQrySettlementInfoConfirmField, nRequestID:int):
        """ 请求查询结算信息确认 """
        self.h.tReqQrySettlementInfoConfirm(self.api, byref(pQrySettlementInfoConfirm), nRequestID)
    
    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail:CThostFtdcQryInvestorPositionCombineDetailField, nRequestID:int):
        """ 请求查询投资者持仓明细 """
        self.h.tReqQryInvestorPositionCombineDetail(self.api, byref(pQryInvestorPositionCombineDetail), nRequestID)
    
    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey:CThostFtdcQryCFMMCTradingAccountKeyField, nRequestID:int):
        """ 请求查询保证金监管系统经纪公司资金账户密钥 """
        self.h.tReqQryCFMMCTradingAccountKey(self.api, byref(pQryCFMMCTradingAccountKey), nRequestID)
    
    def ReqQryEWarrantOffset(self, pQryEWarrantOffset:CThostFtdcQryEWarrantOffsetField, nRequestID:int):
        """ 请求查询仓单折抵信息 """
        self.h.tReqQryEWarrantOffset(self.api, byref(pQryEWarrantOffset), nRequestID)
    
    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin:CThostFtdcQryInvestorProductGroupMarginField, nRequestID:int):
        """ 请求查询投资者品种/跨品种保证金 """
        self.h.tReqQryInvestorProductGroupMargin(self.api, byref(pQryInvestorProductGroupMargin), nRequestID)
    
    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate:CThostFtdcQryExchangeMarginRateField, nRequestID:int):
        """ 请求查询交易所保证金率 """
        self.h.tReqQryExchangeMarginRate(self.api, byref(pQryExchangeMarginRate), nRequestID)
    
    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust:CThostFtdcQryExchangeMarginRateAdjustField, nRequestID:int):
        """ 请求查询交易所调整保证金率 """
        self.h.tReqQryExchangeMarginRateAdjust(self.api, byref(pQryExchangeMarginRateAdjust), nRequestID)
    
    def ReqQryExchangeRate(self, pQryExchangeRate:CThostFtdcQryExchangeRateField, nRequestID:int):
        """ 请求查询汇率 """
        self.h.tReqQryExchangeRate(self.api, byref(pQryExchangeRate), nRequestID)
    
    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap:CThostFtdcQrySecAgentACIDMapField, nRequestID:int):
        """ 请求查询二级代理操作员银期权限 """
        self.h.tReqQrySecAgentACIDMap(self.api, byref(pQrySecAgentACIDMap), nRequestID)
    
    def ReqQryProductExchRate(self, pQryProductExchRate:CThostFtdcQryProductExchRateField, nRequestID:int):
        """ 请求查询产品报价汇率 """
        self.h.tReqQryProductExchRate(self.api, byref(pQryProductExchRate), nRequestID)
    
    def ReqQryProductGroup(self, pQryProductGroup:CThostFtdcQryProductGroupField, nRequestID:int):
        """ 请求查询产品组 """
        self.h.tReqQryProductGroup(self.api, byref(pQryProductGroup), nRequestID)
    
    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate:CThostFtdcQryMMInstrumentCommissionRateField, nRequestID:int):
        """ 请求查询做市商合约手续费率 """
        self.h.tReqQryMMInstrumentCommissionRate(self.api, byref(pQryMMInstrumentCommissionRate), nRequestID)
    
    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate:CThostFtdcQryMMOptionInstrCommRateField, nRequestID:int):
        """ 请求查询做市商期权合约手续费 """
        self.h.tReqQryMMOptionInstrCommRate(self.api, byref(pQryMMOptionInstrCommRate), nRequestID)
    
    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate:CThostFtdcQryInstrumentOrderCommRateField, nRequestID:int):
        """ 请求查询报单手续费 """
        self.h.tReqQryInstrumentOrderCommRate(self.api, byref(pQryInstrumentOrderCommRate), nRequestID)
    
    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount:CThostFtdcQryTradingAccountField, nRequestID:int):
        """ 请求查询资金账户 """
        self.h.tReqQrySecAgentTradingAccount(self.api, byref(pQryTradingAccount), nRequestID)
    
    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode:CThostFtdcQrySecAgentCheckModeField, nRequestID:int):
        """ 请求查询二级代理商资金校验模式 """
        self.h.tReqQrySecAgentCheckMode(self.api, byref(pQrySecAgentCheckMode), nRequestID)
    
    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo:CThostFtdcQrySecAgentTradeInfoField, nRequestID:int):
        """ 请求查询二级代理商信息 """
        self.h.tReqQrySecAgentTradeInfo(self.api, byref(pQrySecAgentTradeInfo), nRequestID)
    
    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost:CThostFtdcQryOptionInstrTradeCostField, nRequestID:int):
        """ 请求查询期权交易成本 """
        self.h.tReqQryOptionInstrTradeCost(self.api, byref(pQryOptionInstrTradeCost), nRequestID)
    
    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate:CThostFtdcQryOptionInstrCommRateField, nRequestID:int):
        """ 请求查询期权合约手续费 """
        self.h.tReqQryOptionInstrCommRate(self.api, byref(pQryOptionInstrCommRate), nRequestID)
    
    def ReqQryExecOrder(self, pQryExecOrder:CThostFtdcQryExecOrderField, nRequestID:int):
        """ 请求查询执行宣告 """
        self.h.tReqQryExecOrder(self.api, byref(pQryExecOrder), nRequestID)
    
    def ReqQryForQuote(self, pQryForQuote:CThostFtdcQryForQuoteField, nRequestID:int):
        """ 请求查询询价 """
        self.h.tReqQryForQuote(self.api, byref(pQryForQuote), nRequestID)
    
    def ReqQryQuote(self, pQryQuote:CThostFtdcQryQuoteField, nRequestID:int):
        """ 请求查询报价 """
        self.h.tReqQryQuote(self.api, byref(pQryQuote), nRequestID)
    
    def ReqQryOptionSelfClose(self, pQryOptionSelfClose:CThostFtdcQryOptionSelfCloseField, nRequestID:int):
        """ 请求查询期权自对冲 """
        self.h.tReqQryOptionSelfClose(self.api, byref(pQryOptionSelfClose), nRequestID)
    
    def ReqQryInvestUnit(self, pQryInvestUnit:CThostFtdcQryInvestUnitField, nRequestID:int):
        """ 请求查询投资单元 """
        self.h.tReqQryInvestUnit(self.api, byref(pQryInvestUnit), nRequestID)
    
    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard:CThostFtdcQryCombInstrumentGuardField, nRequestID:int):
        """ 请求查询组合合约安全系数 """
        self.h.tReqQryCombInstrumentGuard(self.api, byref(pQryCombInstrumentGuard), nRequestID)
    
    def ReqQryCombAction(self, pQryCombAction:CThostFtdcQryCombActionField, nRequestID:int):
        """ 请求查询申请组合 """
        self.h.tReqQryCombAction(self.api, byref(pQryCombAction), nRequestID)
    
    def ReqQryTransferSerial(self, pQryTransferSerial:CThostFtdcQryTransferSerialField, nRequestID:int):
        """ 请求查询转帐流水 """
        self.h.tReqQryTransferSerial(self.api, byref(pQryTransferSerial), nRequestID)
    
    def ReqQryAccountregister(self, pQryAccountregister:CThostFtdcQryAccountregisterField, nRequestID:int):
        """ 请求查询银期签约关系 """
        self.h.tReqQryAccountregister(self.api, byref(pQryAccountregister), nRequestID)
    
    def ReqQryContractBank(self, pQryContractBank:CThostFtdcQryContractBankField, nRequestID:int):
        """ 请求查询签约银行 """
        self.h.tReqQryContractBank(self.api, byref(pQryContractBank), nRequestID)
    
    def ReqQryParkedOrder(self, pQryParkedOrder:CThostFtdcQryParkedOrderField, nRequestID:int):
        """ 请求查询预埋单 """
        self.h.tReqQryParkedOrder(self.api, byref(pQryParkedOrder), nRequestID)
    
    def ReqQryParkedOrderAction(self, pQryParkedOrderAction:CThostFtdcQryParkedOrderActionField, nRequestID:int):
        """ 请求查询预埋撤单 """
        self.h.tReqQryParkedOrderAction(self.api, byref(pQryParkedOrderAction), nRequestID)
    
    def ReqQryTradingNotice(self, pQryTradingNotice:CThostFtdcQryTradingNoticeField, nRequestID:int):
        """ 请求查询交易通知 """
        self.h.tReqQryTradingNotice(self.api, byref(pQryTradingNotice), nRequestID)
    
    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams:CThostFtdcQryBrokerTradingParamsField, nRequestID:int):
        """ 请求查询经纪公司交易参数 """
        self.h.tReqQryBrokerTradingParams(self.api, byref(pQryBrokerTradingParams), nRequestID)
    
    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos:CThostFtdcQryBrokerTradingAlgosField, nRequestID:int):
        """ 请求查询经纪公司交易算法 """
        self.h.tReqQryBrokerTradingAlgos(self.api, byref(pQryBrokerTradingAlgos), nRequestID)
    
    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, nRequestID:int):
        """ 请求查询监控中心用户令牌 """
        self.h.tReqQueryCFMMCTradingAccountToken(self.api, byref(pQueryCFMMCTradingAccountToken), nRequestID)
    
    def ReqFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, nRequestID:int):
        """ 期货发起银行资金转期货请求 """
        self.h.tReqFromBankToFutureByFuture(self.api, byref(pReqTransfer), nRequestID)
    
    def ReqFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, nRequestID:int):
        """ 期货发起期货资金转银行请求 """
        self.h.tReqFromFutureToBankByFuture(self.api, byref(pReqTransfer), nRequestID)
    
    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, nRequestID:int):
        """ 期货发起查询银行余额请求 """
        self.h.tReqQueryBankAccountMoneyByFuture(self.api, byref(pReqQueryAccount), nRequestID)
    
    def ReqQryClassifiedInstrument(self, pQryClassifiedInstrument:CThostFtdcQryClassifiedInstrumentField, nRequestID:int):
        """ 请求查询分类合约 """
        self.h.tReqQryClassifiedInstrument(self.api, byref(pQryClassifiedInstrument), nRequestID)
    
    def ReqQryCombPromotionParam(self, pQryCombPromotionParam:CThostFtdcQryCombPromotionParamField, nRequestID:int):
        """ 请求组合优惠比例 """
        self.h.tReqQryCombPromotionParam(self.api, byref(pQryCombPromotionParam), nRequestID)
    
    def ReqQryRiskSettleInvstPosition(self, pQryRiskSettleInvstPosition:CThostFtdcQryRiskSettleInvstPositionField, nRequestID:int):
        """ 投资者风险结算持仓查询 """
        self.h.tReqQryRiskSettleInvstPosition(self.api, byref(pQryRiskSettleInvstPosition), nRequestID)
    
    def ReqQryRiskSettleProductStatus(self, pQryRiskSettleProductStatus:CThostFtdcQryRiskSettleProductStatusField, nRequestID:int):
        """ 风险结算产品查询 """
        self.h.tReqQryRiskSettleProductStatus(self.api, byref(pQryRiskSettleProductStatus), nRequestID)
    
    #################### 响应函数 #########################
    
    def __OnFrontConnected(self):
        self.OnFrontConnected()
    def OnFrontConnected(self):
        """ 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。 """
        print('===OnFrontConnected===:')
    
    def __OnFrontDisconnected(self, nReason:int):
        self.OnFrontDisconnected(nReason)
    def OnFrontDisconnected(self, nReason:int):
        """ 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。 """
        print('===OnFrontDisconnected===:nReason:int')
    
    def __OnHeartBeatWarning(self, nTimeLapse:int):
        self.OnHeartBeatWarning(nTimeLapse)
    def OnHeartBeatWarning(self, nTimeLapse:int):
        """ 心跳超时警告。当长时间未收到报文时，该方法被调用。 """
        print('===OnHeartBeatWarning===:nTimeLapse:int')
    
    def __OnRspAuthenticate(self, pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspAuthenticate(copy.deepcopy(POINTER(CThostFtdcRspAuthenticateField).from_param(pRspAuthenticateField).contents) if pRspAuthenticateField else CThostFtdcRspAuthenticateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspAuthenticate(self, pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 客户端认证响应 """
        print('===OnRspAuthenticate===:pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents) if pRspUserLogin else CThostFtdcRspUserLoginField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登录请求响应 """
        print('===OnRspUserLogin===:pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents) if pUserLogout else CThostFtdcUserLogoutField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登出请求响应 """
        print('===OnRspUserLogout===:pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcUserPasswordUpdateField).from_param(pUserPasswordUpdate).contents) if pUserPasswordUpdate else CThostFtdcUserPasswordUpdateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 用户口令更新请求响应 """
        print('===OnRspUserPasswordUpdate===:pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspTradingAccountPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcTradingAccountPasswordUpdateField).from_param(pTradingAccountPasswordUpdate).contents) if pTradingAccountPasswordUpdate else CThostFtdcTradingAccountPasswordUpdateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 资金账户口令更新请求响应 """
        print('===OnRspTradingAccountPasswordUpdate===:pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserAuthMethod(self, pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserAuthMethod(copy.deepcopy(POINTER(CThostFtdcRspUserAuthMethodField).from_param(pRspUserAuthMethod).contents) if pRspUserAuthMethod else CThostFtdcRspUserAuthMethodField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserAuthMethod(self, pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询用户当前支持的认证模式的回复 """
        print('===OnRspUserAuthMethod===:pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspGenUserCaptcha(self, pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspGenUserCaptcha(copy.deepcopy(POINTER(CThostFtdcRspGenUserCaptchaField).from_param(pRspGenUserCaptcha).contents) if pRspGenUserCaptcha else CThostFtdcRspGenUserCaptchaField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 获取图形验证码请求的回复 """
        print('===OnRspGenUserCaptcha===:pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspGenUserText(self, pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspGenUserText(copy.deepcopy(POINTER(CThostFtdcRspGenUserTextField).from_param(pRspGenUserText).contents) if pRspGenUserText else CThostFtdcRspGenUserTextField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspGenUserText(self, pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 获取短信验证码请求的回复 """
        print('===OnRspGenUserText===:pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents) if pInputOrder else CThostFtdcInputOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报单录入请求响应 """
        print('===OnRspOrderInsert===:pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspParkedOrderInsert(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents) if pParkedOrder else CThostFtdcParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 预埋单录入请求响应 """
        print('===OnRspParkedOrderInsert===:pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents) if pParkedOrderAction else CThostFtdcParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 预埋撤单录入请求响应 """
        print('===OnRspParkedOrderAction===:pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOrderAction(copy.deepcopy(POINTER(CThostFtdcInputOrderActionField).from_param(pInputOrderAction).contents) if pInputOrderAction else CThostFtdcInputOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报单操作请求响应 """
        print('===OnRspOrderAction===:pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMaxOrderVolume(copy.deepcopy(POINTER(CThostFtdcQryMaxOrderVolumeField).from_param(pQryMaxOrderVolume).contents) if pQryMaxOrderVolume else CThostFtdcQryMaxOrderVolumeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询最大报单数量响应 """
        print('===OnRspQryMaxOrderVolume===:pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents) if pSettlementInfoConfirm else CThostFtdcSettlementInfoConfirmField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者结算结果确认响应 """
        print('===OnRspSettlementInfoConfirm===:pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspRemoveParkedOrder(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderField).from_param(pRemoveParkedOrder).contents) if pRemoveParkedOrder else CThostFtdcRemoveParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 删除预埋单响应 """
        print('===OnRspRemoveParkedOrder===:pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspRemoveParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderActionField).from_param(pRemoveParkedOrderAction).contents) if pRemoveParkedOrderAction else CThostFtdcRemoveParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 删除预埋撤单响应 """
        print('===OnRspRemoveParkedOrderAction===:pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents) if pInputExecOrder else CThostFtdcInputExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 执行宣告录入请求响应 """
        print('===OnRspExecOrderInsert===:pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspExecOrderAction(copy.deepcopy(POINTER(CThostFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents) if pInputExecOrderAction else CThostFtdcInputExecOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 执行宣告操作请求响应 """
        print('===OnRspExecOrderAction===:pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents) if pInputForQuote else CThostFtdcInputForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 询价录入请求响应 """
        print('===OnRspForQuoteInsert===:pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents) if pInputQuote else CThostFtdcInputQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报价录入请求响应 """
        print('===OnRspQuoteInsert===:pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQuoteAction(copy.deepcopy(POINTER(CThostFtdcInputQuoteActionField).from_param(pInputQuoteAction).contents) if pInputQuoteAction else CThostFtdcInputQuoteActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报价操作请求响应 """
        print('===OnRspQuoteAction===:pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcInputBatchOrderActionField).from_param(pInputBatchOrderAction).contents) if pInputBatchOrderAction else CThostFtdcInputBatchOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 批量报单操作请求响应 """
        print('===OnRspBatchOrderAction===:pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents) if pInputOptionSelfClose else CThostFtdcInputOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期权自对冲录入请求响应 """
        print('===OnRspOptionSelfCloseInsert===:pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseActionField).from_param(pInputOptionSelfCloseAction).contents) if pInputOptionSelfCloseAction else CThostFtdcInputOptionSelfCloseActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期权自对冲操作请求响应 """
        print('===OnRspOptionSelfCloseAction===:pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents) if pInputCombAction else CThostFtdcInputCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 申请组合录入请求响应 """
        print('===OnRspCombActionInsert===:pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOrder(self, pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents) if pOrder else CThostFtdcOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOrder(self, pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报单响应 """
        print('===OnRspQryOrder===:pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTrade(self, pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents) if pTrade else CThostFtdcTradeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTrade(self, pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询成交响应 """
        print('===OnRspQryTrade===:pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPosition(self, pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPosition(copy.deepcopy(POINTER(CThostFtdcInvestorPositionField).from_param(pInvestorPosition).contents) if pInvestorPosition else CThostFtdcInvestorPositionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPosition(self, pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓响应 """
        print('===OnRspQryInvestorPosition===:pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents) if pTradingAccount else CThostFtdcTradingAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询资金账户响应 """
        print('===OnRspQryTradingAccount===:pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestor(self, pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestor(copy.deepcopy(POINTER(CThostFtdcInvestorField).from_param(pInvestor).contents) if pInvestor else CThostFtdcInvestorField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestor(self, pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者响应 """
        print('===OnRspQryInvestor===:pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingCode(self, pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingCode(copy.deepcopy(POINTER(CThostFtdcTradingCodeField).from_param(pTradingCode).contents) if pTradingCode else CThostFtdcTradingCodeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingCode(self, pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易编码响应 """
        print('===OnRspQryTradingCode===:pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentMarginRate(copy.deepcopy(POINTER(CThostFtdcInstrumentMarginRateField).from_param(pInstrumentMarginRate).contents) if pInstrumentMarginRate else CThostFtdcInstrumentMarginRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约保证金率响应 """
        print('===OnRspQryInstrumentMarginRate===:pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcInstrumentCommissionRateField).from_param(pInstrumentCommissionRate).contents) if pInstrumentCommissionRate else CThostFtdcInstrumentCommissionRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约手续费率响应 """
        print('===OnRspQryInstrumentCommissionRate===:pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchange(self, pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchange(copy.deepcopy(POINTER(CThostFtdcExchangeField).from_param(pExchange).contents) if pExchange else CThostFtdcExchangeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchange(self, pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所响应 """
        print('===OnRspQryExchange===:pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProduct(self, pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProduct(copy.deepcopy(POINTER(CThostFtdcProductField).from_param(pProduct).contents) if pProduct else CThostFtdcProductField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProduct(self, pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品响应 """
        print('===OnRspQryProduct===:pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents) if pInstrument else CThostFtdcInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约响应 """
        print('===OnRspQryInstrument===:pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents) if pDepthMarketData else CThostFtdcDepthMarketDataField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询行情响应 """
        print('===OnRspQryDepthMarketData===:pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTraderOffer(self, pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTraderOffer(copy.deepcopy(POINTER(CThostFtdcTraderOfferField).from_param(pTraderOffer).contents) if pTraderOffer else CThostFtdcTraderOfferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTraderOffer(self, pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易员报盘机响应 """
        print('===OnRspQryTraderOffer===:pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySettlementInfo(self, pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySettlementInfo(copy.deepcopy(POINTER(CThostFtdcSettlementInfoField).from_param(pSettlementInfo).contents) if pSettlementInfo else CThostFtdcSettlementInfoField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySettlementInfo(self, pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者结算结果响应 """
        print('===OnRspQrySettlementInfo===:pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTransferBank(self, pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTransferBank(copy.deepcopy(POINTER(CThostFtdcTransferBankField).from_param(pTransferBank).contents) if pTransferBank else CThostFtdcTransferBankField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTransferBank(self, pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询转帐银行响应 """
        print('===OnRspQryTransferBank===:pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPositionDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionDetailField).from_param(pInvestorPositionDetail).contents) if pInvestorPositionDetail else CThostFtdcInvestorPositionDetailField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓明细响应 """
        print('===OnRspQryInvestorPositionDetail===:pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryNotice(self, pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryNotice(copy.deepcopy(POINTER(CThostFtdcNoticeField).from_param(pNotice).contents) if pNotice else CThostFtdcNoticeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryNotice(self, pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询客户通知响应 """
        print('===OnRspQryNotice===:pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents) if pSettlementInfoConfirm else CThostFtdcSettlementInfoConfirmField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询结算信息确认响应 """
        print('===OnRspQrySettlementInfoConfirm===:pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPositionCombineDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionCombineDetailField).from_param(pInvestorPositionCombineDetail).contents) if pInvestorPositionCombineDetail else CThostFtdcInvestorPositionCombineDetailField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓明细响应 """
        print('===OnRspQryInvestorPositionCombineDetail===:pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCFMMCTradingAccountKey(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountKeyField).from_param(pCFMMCTradingAccountKey).contents) if pCFMMCTradingAccountKey else CThostFtdcCFMMCTradingAccountKeyField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询保证金监管系统经纪公司资金账户密钥响应 """
        print('===OnRspQryCFMMCTradingAccountKey===:pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryEWarrantOffset(self, pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryEWarrantOffset(copy.deepcopy(POINTER(CThostFtdcEWarrantOffsetField).from_param(pEWarrantOffset).contents) if pEWarrantOffset else CThostFtdcEWarrantOffsetField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryEWarrantOffset(self, pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询仓单折抵信息响应 """
        print('===OnRspQryEWarrantOffset===:pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorProductGroupMargin(copy.deepcopy(POINTER(CThostFtdcInvestorProductGroupMarginField).from_param(pInvestorProductGroupMargin).contents) if pInvestorProductGroupMargin else CThostFtdcInvestorProductGroupMarginField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者品种/跨品种保证金响应 """
        print('===OnRspQryInvestorProductGroupMargin===:pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeMarginRate(self, pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeMarginRate(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateField).from_param(pExchangeMarginRate).contents) if pExchangeMarginRate else CThostFtdcExchangeMarginRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所保证金率响应 """
        print('===OnRspQryExchangeMarginRate===:pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeMarginRateAdjust(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateAdjustField).from_param(pExchangeMarginRateAdjust).contents) if pExchangeMarginRateAdjust else CThostFtdcExchangeMarginRateAdjustField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所调整保证金率响应 """
        print('===OnRspQryExchangeMarginRateAdjust===:pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeRate(self, pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeRate(copy.deepcopy(POINTER(CThostFtdcExchangeRateField).from_param(pExchangeRate).contents) if pExchangeRate else CThostFtdcExchangeRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeRate(self, pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询汇率响应 """
        print('===OnRspQryExchangeRate===:pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentACIDMap(copy.deepcopy(POINTER(CThostFtdcSecAgentACIDMapField).from_param(pSecAgentACIDMap).contents) if pSecAgentACIDMap else CThostFtdcSecAgentACIDMapField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理操作员银期权限响应 """
        print('===OnRspQrySecAgentACIDMap===:pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProductExchRate(self, pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProductExchRate(copy.deepcopy(POINTER(CThostFtdcProductExchRateField).from_param(pProductExchRate).contents) if pProductExchRate else CThostFtdcProductExchRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProductExchRate(self, pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品报价汇率 """
        print('===OnRspQryProductExchRate===:pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProductGroup(self, pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProductGroup(copy.deepcopy(POINTER(CThostFtdcProductGroupField).from_param(pProductGroup).contents) if pProductGroup else CThostFtdcProductGroupField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProductGroup(self, pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品组 """
        print('===OnRspQryProductGroup===:pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMMInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcMMInstrumentCommissionRateField).from_param(pMMInstrumentCommissionRate).contents) if pMMInstrumentCommissionRate else CThostFtdcMMInstrumentCommissionRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询做市商合约手续费率响应 """
        print('===OnRspQryMMInstrumentCommissionRate===:pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMMOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcMMOptionInstrCommRateField).from_param(pMMOptionInstrCommRate).contents) if pMMOptionInstrCommRate else CThostFtdcMMOptionInstrCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询做市商期权合约手续费响应 """
        print('===OnRspQryMMOptionInstrCommRate===:pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentOrderCommRate(copy.deepcopy(POINTER(CThostFtdcInstrumentOrderCommRateField).from_param(pInstrumentOrderCommRate).contents) if pInstrumentOrderCommRate else CThostFtdcInstrumentOrderCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报单手续费响应 """
        print('===OnRspQryInstrumentOrderCommRate===:pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents) if pTradingAccount else CThostFtdcTradingAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询资金账户响应 """
        print('===OnRspQrySecAgentTradingAccount===:pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentCheckMode(copy.deepcopy(POINTER(CThostFtdcSecAgentCheckModeField).from_param(pSecAgentCheckMode).contents) if pSecAgentCheckMode else CThostFtdcSecAgentCheckModeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理商资金校验模式响应 """
        print('===OnRspQrySecAgentCheckMode===:pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentTradeInfo(copy.deepcopy(POINTER(CThostFtdcSecAgentTradeInfoField).from_param(pSecAgentTradeInfo).contents) if pSecAgentTradeInfo else CThostFtdcSecAgentTradeInfoField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理商信息响应 """
        print('===OnRspQrySecAgentTradeInfo===:pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionInstrTradeCost(copy.deepcopy(POINTER(CThostFtdcOptionInstrTradeCostField).from_param(pOptionInstrTradeCost).contents) if pOptionInstrTradeCost else CThostFtdcOptionInstrTradeCostField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权交易成本响应 """
        print('===OnRspQryOptionInstrTradeCost===:pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcOptionInstrCommRateField).from_param(pOptionInstrCommRate).contents) if pOptionInstrCommRate else CThostFtdcOptionInstrCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权合约手续费响应 """
        print('===OnRspQryOptionInstrCommRate===:pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExecOrder(self, pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents) if pExecOrder else CThostFtdcExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExecOrder(self, pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询执行宣告响应 """
        print('===OnRspQryExecOrder===:pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryForQuote(self, pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryForQuote(copy.deepcopy(POINTER(CThostFtdcForQuoteField).from_param(pForQuote).contents) if pForQuote else CThostFtdcForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryForQuote(self, pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询询价响应 """
        print('===OnRspQryForQuote===:pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryQuote(self, pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents) if pQuote else CThostFtdcQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryQuote(self, pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报价响应 """
        print('===OnRspQryQuote===:pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents) if pOptionSelfClose else CThostFtdcOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权自对冲响应 """
        print('===OnRspQryOptionSelfClose===:pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestUnit(self, pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestUnit(copy.deepcopy(POINTER(CThostFtdcInvestUnitField).from_param(pInvestUnit).contents) if pInvestUnit else CThostFtdcInvestUnitField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestUnit(self, pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资单元响应 """
        print('===OnRspQryInvestUnit===:pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombInstrumentGuard(copy.deepcopy(POINTER(CThostFtdcCombInstrumentGuardField).from_param(pCombInstrumentGuard).contents) if pCombInstrumentGuard else CThostFtdcCombInstrumentGuardField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询组合合约安全系数响应 """
        print('===OnRspQryCombInstrumentGuard===:pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombAction(self, pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents) if pCombAction else CThostFtdcCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombAction(self, pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询申请组合响应 """
        print('===OnRspQryCombAction===:pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTransferSerial(self, pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTransferSerial(copy.deepcopy(POINTER(CThostFtdcTransferSerialField).from_param(pTransferSerial).contents) if pTransferSerial else CThostFtdcTransferSerialField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTransferSerial(self, pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询转帐流水响应 """
        print('===OnRspQryTransferSerial===:pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryAccountregister(self, pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryAccountregister(copy.deepcopy(POINTER(CThostFtdcAccountregisterField).from_param(pAccountregister).contents) if pAccountregister else CThostFtdcAccountregisterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryAccountregister(self, pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询银期签约关系响应 """
        print('===OnRspQryAccountregister===:pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 错误应答 """
        print('===OnRspError===:pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnOrder(self, pOrder:CThostFtdcOrderField):
        self.OnRtnOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents) if pOrder else CThostFtdcOrderField())
    def OnRtnOrder(self, pOrder:CThostFtdcOrderField):
        """ 报单通知 """
        print('===OnRtnOrder===:pOrder:CThostFtdcOrderField')
    
    def __OnRtnTrade(self, pTrade:CThostFtdcTradeField):
        self.OnRtnTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents) if pTrade else CThostFtdcTradeField())
    def OnRtnTrade(self, pTrade:CThostFtdcTradeField):
        """ 成交通知 """
        print('===OnRtnTrade===:pTrade:CThostFtdcTradeField')
    
    def __OnErrRtnOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents) if pInputOrder else CThostFtdcInputOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField):
        """ 报单录入错误回报 """
        print('===OnErrRtnOrderInsert===:pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnOrderAction(self, pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOrderAction(copy.deepcopy(POINTER(CThostFtdcOrderActionField).from_param(pOrderAction).contents) if pOrderAction else CThostFtdcOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOrderAction(self, pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 报单操作错误回报 """
        print('===OnErrRtnOrderAction===:pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnInstrumentStatus(self, pInstrumentStatus:CThostFtdcInstrumentStatusField):
        self.OnRtnInstrumentStatus(copy.deepcopy(POINTER(CThostFtdcInstrumentStatusField).from_param(pInstrumentStatus).contents) if pInstrumentStatus else CThostFtdcInstrumentStatusField())
    def OnRtnInstrumentStatus(self, pInstrumentStatus:CThostFtdcInstrumentStatusField):
        """ 合约交易状态通知 """
        print('===OnRtnInstrumentStatus===:pInstrumentStatus:CThostFtdcInstrumentStatusField')
    
    def __OnRtnBulletin(self, pBulletin:CThostFtdcBulletinField):
        self.OnRtnBulletin(copy.deepcopy(POINTER(CThostFtdcBulletinField).from_param(pBulletin).contents) if pBulletin else CThostFtdcBulletinField())
    def OnRtnBulletin(self, pBulletin:CThostFtdcBulletinField):
        """ 交易所公告通知 """
        print('===OnRtnBulletin===:pBulletin:CThostFtdcBulletinField')
    
    def __OnRtnTradingNotice(self, pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField):
        self.OnRtnTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeInfoField).from_param(pTradingNoticeInfo).contents) if pTradingNoticeInfo else CThostFtdcTradingNoticeInfoField())
    def OnRtnTradingNotice(self, pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField):
        """ 交易通知 """
        print('===OnRtnTradingNotice===:pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField')
    
    def __OnRtnErrorConditionalOrder(self, pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField):
        self.OnRtnErrorConditionalOrder(copy.deepcopy(POINTER(CThostFtdcErrorConditionalOrderField).from_param(pErrorConditionalOrder).contents) if pErrorConditionalOrder else CThostFtdcErrorConditionalOrderField())
    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField):
        """ 提示条件单校验错误 """
        print('===OnRtnErrorConditionalOrder===:pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField')
    
    def __OnRtnExecOrder(self, pExecOrder:CThostFtdcExecOrderField):
        self.OnRtnExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents) if pExecOrder else CThostFtdcExecOrderField())
    def OnRtnExecOrder(self, pExecOrder:CThostFtdcExecOrderField):
        """ 执行宣告通知 """
        print('===OnRtnExecOrder===:pExecOrder:CThostFtdcExecOrderField')
    
    def __OnErrRtnExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents) if pInputExecOrder else CThostFtdcInputExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField):
        """ 执行宣告录入错误回报 """
        print('===OnErrRtnExecOrderInsert===:pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnExecOrderAction(self, pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnExecOrderAction(copy.deepcopy(POINTER(CThostFtdcExecOrderActionField).from_param(pExecOrderAction).contents) if pExecOrderAction else CThostFtdcExecOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnExecOrderAction(self, pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 执行宣告操作错误回报 """
        print('===OnErrRtnExecOrderAction===:pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents) if pInputForQuote else CThostFtdcInputForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField):
        """ 询价录入错误回报 """
        print('===OnErrRtnForQuoteInsert===:pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnQuote(self, pQuote:CThostFtdcQuoteField):
        self.OnRtnQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents) if pQuote else CThostFtdcQuoteField())
    def OnRtnQuote(self, pQuote:CThostFtdcQuoteField):
        """ 报价通知 """
        print('===OnRtnQuote===:pQuote:CThostFtdcQuoteField')
    
    def __OnErrRtnQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents) if pInputQuote else CThostFtdcInputQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField):
        """ 报价录入错误回报 """
        print('===OnErrRtnQuoteInsert===:pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnQuoteAction(self, pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQuoteAction(copy.deepcopy(POINTER(CThostFtdcQuoteActionField).from_param(pQuoteAction).contents) if pQuoteAction else CThostFtdcQuoteActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQuoteAction(self, pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 报价操作错误回报 """
        print('===OnErrRtnQuoteAction===:pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents) if pForQuoteRsp else CThostFtdcForQuoteRspField())
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        """ 询价通知 """
        print('===OnRtnForQuoteRsp===:pForQuoteRsp:CThostFtdcForQuoteRspField')
    
    def __OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField):
        self.OnRtnCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountTokenField).from_param(pCFMMCTradingAccountToken).contents) if pCFMMCTradingAccountToken else CThostFtdcCFMMCTradingAccountTokenField())
    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField):
        """ 保证金监控中心用户令牌 """
        print('===OnRtnCFMMCTradingAccountToken===:pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField')
    
    def __OnErrRtnBatchOrderAction(self, pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcBatchOrderActionField).from_param(pBatchOrderAction).contents) if pBatchOrderAction else CThostFtdcBatchOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnBatchOrderAction(self, pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 批量报单操作错误回报 """
        print('===OnErrRtnBatchOrderAction===:pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField):
        self.OnRtnOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents) if pOptionSelfClose else CThostFtdcOptionSelfCloseField())
    def OnRtnOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField):
        """ 期权自对冲通知 """
        print('===OnRtnOptionSelfClose===:pOptionSelfClose:CThostFtdcOptionSelfCloseField')
    
    def __OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents) if pInputOptionSelfClose else CThostFtdcInputOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField):
        """ 期权自对冲录入错误回报 """
        print('===OnErrRtnOptionSelfCloseInsert===:pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseActionField).from_param(pOptionSelfCloseAction).contents) if pOptionSelfCloseAction else CThostFtdcOptionSelfCloseActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 期权自对冲操作错误回报 """
        print('===OnErrRtnOptionSelfCloseAction===:pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnCombAction(self, pCombAction:CThostFtdcCombActionField):
        self.OnRtnCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents) if pCombAction else CThostFtdcCombActionField())
    def OnRtnCombAction(self, pCombAction:CThostFtdcCombActionField):
        """ 申请组合通知 """
        print('===OnRtnCombAction===:pCombAction:CThostFtdcCombActionField')
    
    def __OnErrRtnCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents) if pInputCombAction else CThostFtdcInputCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 申请组合录入错误回报 """
        print('===OnErrRtnCombActionInsert===:pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRspQryContractBank(self, pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryContractBank(copy.deepcopy(POINTER(CThostFtdcContractBankField).from_param(pContractBank).contents) if pContractBank else CThostFtdcContractBankField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryContractBank(self, pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询签约银行响应 """
        print('===OnRspQryContractBank===:pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryParkedOrder(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryParkedOrder(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents) if pParkedOrder else CThostFtdcParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryParkedOrder(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询预埋单响应 """
        print('===OnRspQryParkedOrder===:pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents) if pParkedOrderAction else CThostFtdcParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询预埋撤单响应 """
        print('===OnRspQryParkedOrderAction===:pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingNotice(self, pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeField).from_param(pTradingNotice).contents) if pTradingNotice else CThostFtdcTradingNoticeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingNotice(self, pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易通知响应 """
        print('===OnRspQryTradingNotice===:pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryBrokerTradingParams(self, pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryBrokerTradingParams(copy.deepcopy(POINTER(CThostFtdcBrokerTradingParamsField).from_param(pBrokerTradingParams).contents) if pBrokerTradingParams else CThostFtdcBrokerTradingParamsField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询经纪公司交易参数响应 """
        print('===OnRspQryBrokerTradingParams===:pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryBrokerTradingAlgos(copy.deepcopy(POINTER(CThostFtdcBrokerTradingAlgosField).from_param(pBrokerTradingAlgos).contents) if pBrokerTradingAlgos else CThostFtdcBrokerTradingAlgosField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询经纪公司交易算法响应 """
        print('===OnRspQryBrokerTradingAlgos===:pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQueryCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField).from_param(pQueryCFMMCTradingAccountToken).contents) if pQueryCFMMCTradingAccountToken else CThostFtdcQueryCFMMCTradingAccountTokenField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询监控中心用户令牌 """
        print('===OnRspQueryCFMMCTradingAccountToken===:pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnFromBankToFutureByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromBankToFutureByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 银行发起银行资金转期货通知 """
        print('===OnRtnFromBankToFutureByBank===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnFromFutureToBankByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromFutureToBankByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 银行发起期货资金转银行通知 """
        print('===OnRtnFromFutureToBankByBank===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnRepealFromBankToFutureByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 银行发起冲正银行转期货通知 """
        print('===OnRtnRepealFromBankToFutureByBank===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 银行发起冲正期货转银行通知 """
        print('===OnRtnRepealFromFutureToBankByBank===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnFromBankToFutureByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromBankToFutureByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 期货发起银行资金转期货通知 """
        print('===OnRtnFromBankToFutureByFuture===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnFromFutureToBankByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromFutureToBankByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 期货发起期货资金转银行通知 """
        print('===OnRtnFromFutureToBankByFuture===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromBankToFutureByFutureManual===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromFutureToBankByFutureManual===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField):
        self.OnRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcNotifyQueryAccountField).from_param(pNotifyQueryAccount).contents) if pNotifyQueryAccount else CThostFtdcNotifyQueryAccountField())
    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField):
        """ 期货发起查询银行余额通知 """
        print('===OnRtnQueryBankBalanceByFuture===:pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField')
    
    def __OnErrRtnBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起银行资金转期货错误回报 """
        print('===OnErrRtnBankToFutureByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起期货资金转银行错误回报 """
        print('===OnErrRtnFutureToBankByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnRepealBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents) if pReqRepeal else CThostFtdcReqRepealField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        """ 系统运行时期货端手工发起冲正银行转期货错误回报 """
        print('===OnErrRtnRepealBankToFutureByFutureManual===:pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnRepealFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents) if pReqRepeal else CThostFtdcReqRepealField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        """ 系统运行时期货端手工发起冲正期货转银行错误回报 """
        print('===OnErrRtnRepealFutureToBankByFutureManual===:pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents) if pReqQueryAccount else CThostFtdcReqQueryAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起查询银行余额错误回报 """
        print('===OnErrRtnQueryBankBalanceByFuture===:pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromBankToFutureByFuture===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromFutureToBankByFuture===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRspFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起银行资金转期货应答 """
        print('===OnRspFromBankToFutureByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起期货资金转银行应答 """
        print('===OnRspFromFutureToBankByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQueryBankAccountMoneyByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents) if pReqQueryAccount else CThostFtdcReqQueryAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起查询银行余额应答 """
        print('===OnRspQueryBankAccountMoneyByFuture===:pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnOpenAccountByBank(self, pOpenAccount:CThostFtdcOpenAccountField):
        self.OnRtnOpenAccountByBank(copy.deepcopy(POINTER(CThostFtdcOpenAccountField).from_param(pOpenAccount).contents) if pOpenAccount else CThostFtdcOpenAccountField())
    def OnRtnOpenAccountByBank(self, pOpenAccount:CThostFtdcOpenAccountField):
        """ 银行发起银期开户通知 """
        print('===OnRtnOpenAccountByBank===:pOpenAccount:CThostFtdcOpenAccountField')
    
    def __OnRtnCancelAccountByBank(self, pCancelAccount:CThostFtdcCancelAccountField):
        self.OnRtnCancelAccountByBank(copy.deepcopy(POINTER(CThostFtdcCancelAccountField).from_param(pCancelAccount).contents) if pCancelAccount else CThostFtdcCancelAccountField())
    def OnRtnCancelAccountByBank(self, pCancelAccount:CThostFtdcCancelAccountField):
        """ 银行发起银期销户通知 """
        print('===OnRtnCancelAccountByBank===:pCancelAccount:CThostFtdcCancelAccountField')
    
    def __OnRtnChangeAccountByBank(self, pChangeAccount:CThostFtdcChangeAccountField):
        self.OnRtnChangeAccountByBank(copy.deepcopy(POINTER(CThostFtdcChangeAccountField).from_param(pChangeAccount).contents) if pChangeAccount else CThostFtdcChangeAccountField())
    def OnRtnChangeAccountByBank(self, pChangeAccount:CThostFtdcChangeAccountField):
        """ 银行发起变更银行账号通知 """
        print('===OnRtnChangeAccountByBank===:pChangeAccount:CThostFtdcChangeAccountField')
    
    def __OnRspQryClassifiedInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryClassifiedInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents) if pInstrument else CThostFtdcInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryClassifiedInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询分类合约响应 """
        print('===OnRspQryClassifiedInstrument===:pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombPromotionParam(self, pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombPromotionParam(copy.deepcopy(POINTER(CThostFtdcCombPromotionParamField).from_param(pCombPromotionParam).contents) if pCombPromotionParam else CThostFtdcCombPromotionParamField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombPromotionParam(self, pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求组合优惠比例响应 """
        print('===OnRspQryCombPromotionParam===:pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryRiskSettleInvstPosition(self, pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryRiskSettleInvstPosition(copy.deepcopy(POINTER(CThostFtdcRiskSettleInvstPositionField).from_param(pRiskSettleInvstPosition).contents) if pRiskSettleInvstPosition else CThostFtdcRiskSettleInvstPositionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryRiskSettleInvstPosition(self, pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者风险结算持仓查询响应 """
        print('===OnRspQryRiskSettleInvstPosition===:pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryRiskSettleProductStatus(self, pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryRiskSettleProductStatus(copy.deepcopy(POINTER(CThostFtdcRiskSettleProductStatusField).from_param(pRiskSettleProductStatus).contents) if pRiskSettleProductStatus else CThostFtdcRiskSettleProductStatusField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryRiskSettleProductStatus(self, pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 风险结算产品查询响应 """
        print('===OnRspQryRiskSettleProductStatus===:pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    