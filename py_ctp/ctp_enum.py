#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class THOST_TE_RESUME_TYPE(Enum):
	TERT_RESTART = 0
	TERT_RESUME = 1
	TERT_QUICK = 2


class TThostFtdcExchangePropertyType(Enum):
    """交易所属性类型"""
    THOST_FTDC_EXP_Normal = 48
    """正常"""
    THOST_FTDC_EXP_GenOrderByTrade = 49
    """根据成交生成报单"""


class TThostFtdcIdCardTypeType(Enum):
    """证件类型类型"""
    THOST_FTDC_ICT_EID = 48
    """组织机构代码"""
    THOST_FTDC_ICT_IDCard = 49
    """中国公民身份证"""
    THOST_FTDC_ICT_OfficerIDCard = 50
    """军官证"""
    THOST_FTDC_ICT_PoliceIDCard = 51
    """警官证"""
    THOST_FTDC_ICT_SoldierIDCard = 52
    """士兵证"""
    THOST_FTDC_ICT_HouseholdRegister = 53
    """户口簿"""
    THOST_FTDC_ICT_Passport = 54
    """护照"""
    THOST_FTDC_ICT_TaiwanCompatriotIDCard = 55
    """台胞证"""
    THOST_FTDC_ICT_HomeComingCard = 56
    """回乡证"""
    THOST_FTDC_ICT_LicenseNo = 57
    """营业执照号"""
    THOST_FTDC_ICT_TaxNo = 65
    """税务登记号/当地纳税ID"""
    THOST_FTDC_ICT_HMMainlandTravelPermit = 66
    """港澳居民来往内地通行证"""
    THOST_FTDC_ICT_TwMainlandTravelPermit = 67
    """台湾居民来往大陆通行证"""
    THOST_FTDC_ICT_DrivingLicense = 68
    """驾照"""
    THOST_FTDC_ICT_SocialID = 70
    """当地社保ID"""
    THOST_FTDC_ICT_LocalID = 71
    """当地身份证"""
    THOST_FTDC_ICT_BusinessRegistration = 72
    """商业登记证"""
    THOST_FTDC_ICT_HKMCIDCard = 73
    """港澳永久性居民身份证"""
    THOST_FTDC_ICT_AccountsPermits = 74
    """人行开户许可证"""
    THOST_FTDC_ICT_FrgPrmtRdCard = 75
    """外国人永久居留证"""
    THOST_FTDC_ICT_CptMngPrdLetter = 76
    """资管产品备案函"""
    THOST_FTDC_ICT_UniformSocialCreditCode = 78
    """统一社会信用代码"""
    THOST_FTDC_ICT_CorporationCertNo = 79
    """机构成立证明文件"""
    THOST_FTDC_ICT_OtherCard = 120
    """其他证件"""


class TThostFtdcInvestorRangeType(Enum):
    """投资者范围类型"""
    THOST_FTDC_IR_All = 49
    """所有"""
    THOST_FTDC_IR_Group = 50
    """投资者组"""
    THOST_FTDC_IR_Single = 51
    """单一投资者"""


class TThostFtdcDepartmentRangeType(Enum):
    """投资者范围类型"""
    THOST_FTDC_DR_All = 49
    """所有"""
    THOST_FTDC_DR_Group = 50
    """组织架构"""
    THOST_FTDC_DR_Single = 51
    """单一投资者"""


class TThostFtdcDataSyncStatusType(Enum):
    """数据同步状态类型"""
    THOST_FTDC_DS_Asynchronous = 49
    """未同步"""
    THOST_FTDC_DS_Synchronizing = 50
    """同步中"""
    THOST_FTDC_DS_Synchronized = 51
    """已同步"""


class TThostFtdcBrokerDataSyncStatusType(Enum):
    """经纪公司数据同步状态类型"""
    THOST_FTDC_BDS_Synchronized = 49
    """已同步"""
    THOST_FTDC_BDS_Synchronizing = 50
    """同步中"""


class TThostFtdcExchangeConnectStatusType(Enum):
    """交易所连接状态类型"""
    THOST_FTDC_ECS_NoConnection = 49
    """没有任何连接"""
    THOST_FTDC_ECS_QryInstrumentSent = 50
    """已经发出合约查询请求"""
    THOST_FTDC_ECS_GotInformation = 57
    """已经获取信息"""


class TThostFtdcTraderConnectStatusType(Enum):
    """交易所交易员连接状态类型"""
    THOST_FTDC_TCS_NotConnected = 49
    """没有任何连接"""
    THOST_FTDC_TCS_Connected = 50
    """已经连接"""
    THOST_FTDC_TCS_QryInstrumentSent = 51
    """已经发出合约查询请求"""
    THOST_FTDC_TCS_SubPrivateFlow = 52
    """订阅私有流"""


class TThostFtdcFunctionCodeType(Enum):
    """功能代码类型"""
    THOST_FTDC_FC_DataAsync = 49
    """数据异步化"""
    THOST_FTDC_FC_ForceUserLogout = 50
    """强制用户登出"""
    THOST_FTDC_FC_UserPasswordUpdate = 51
    """变更管理用户口令"""
    THOST_FTDC_FC_BrokerPasswordUpdate = 52
    """变更经纪公司口令"""
    THOST_FTDC_FC_InvestorPasswordUpdate = 53
    """变更投资者口令"""
    THOST_FTDC_FC_OrderInsert = 54
    """报单插入"""
    THOST_FTDC_FC_OrderAction = 55
    """报单操作"""
    THOST_FTDC_FC_SyncSystemData = 56
    """同步系统数据"""
    THOST_FTDC_FC_SyncBrokerData = 57
    """同步经纪公司数据"""
    THOST_FTDC_FC_BachSyncBrokerData = 65
    """批量同步经纪公司数据"""
    THOST_FTDC_FC_SuperQuery = 66
    """超级查询"""
    THOST_FTDC_FC_ParkedOrderInsert = 67
    """预埋报单插入"""
    THOST_FTDC_FC_ParkedOrderAction = 68
    """预埋报单操作"""
    THOST_FTDC_FC_SyncOTP = 69
    """同步动态令牌"""
    THOST_FTDC_FC_DeleteOrder = 70
    """删除未知单"""


class TThostFtdcBrokerFunctionCodeType(Enum):
    """经纪公司功能代码类型"""
    THOST_FTDC_BFC_ForceUserLogout = 49
    """强制用户登出"""
    THOST_FTDC_BFC_UserPasswordUpdate = 50
    """变更用户口令"""
    THOST_FTDC_BFC_SyncBrokerData = 51
    """同步经纪公司数据"""
    THOST_FTDC_BFC_BachSyncBrokerData = 52
    """批量同步经纪公司数据"""
    THOST_FTDC_BFC_OrderInsert = 53
    """报单插入"""
    THOST_FTDC_BFC_OrderAction = 54
    """报单操作"""
    THOST_FTDC_BFC_AllQuery = 55
    """全部查询"""
    THOST_FTDC_BFC_log = 97
    """系统功能：登入/登出/修改密码等"""
    THOST_FTDC_BFC_BaseQry = 98
    """基本查询：查询基础数据，如合约，交易所等常量"""
    THOST_FTDC_BFC_TradeQry = 99
    """交易查询：如查成交，委托"""
    THOST_FTDC_BFC_Trade = 100
    """交易功能：报单，撤单"""
    THOST_FTDC_BFC_Virement = 101
    """银期转账"""
    THOST_FTDC_BFC_Risk = 102
    """风险监控"""
    THOST_FTDC_BFC_Session = 103
    """查询/管理：查询会话，踢人等"""
    THOST_FTDC_BFC_RiskNoticeCtl = 104
    """风控通知控制"""
    THOST_FTDC_BFC_RiskNotice = 105
    """风控通知发送"""
    THOST_FTDC_BFC_BrokerDeposit = 106
    """察看经纪公司资金权限"""
    THOST_FTDC_BFC_QueryFund = 107
    """资金查询"""
    THOST_FTDC_BFC_QueryOrder = 108
    """报单查询"""
    THOST_FTDC_BFC_QueryTrade = 109
    """成交查询"""
    THOST_FTDC_BFC_QueryPosition = 110
    """持仓查询"""
    THOST_FTDC_BFC_QueryMarketData = 111
    """行情查询"""
    THOST_FTDC_BFC_QueryUserEvent = 112
    """用户事件查询"""
    THOST_FTDC_BFC_QueryRiskNotify = 113
    """风险通知查询"""
    THOST_FTDC_BFC_QueryFundChange = 114
    """出入金查询"""
    THOST_FTDC_BFC_QueryInvestor = 115
    """投资者信息查询"""
    THOST_FTDC_BFC_QueryTradingCode = 116
    """交易编码查询"""
    THOST_FTDC_BFC_ForceClose = 117
    """强平"""
    THOST_FTDC_BFC_PressTest = 118
    """压力测试"""
    THOST_FTDC_BFC_RemainCalc = 119
    """权益反算"""
    THOST_FTDC_BFC_NetPositionInd = 120
    """净持仓保证金指标"""
    THOST_FTDC_BFC_RiskPredict = 121
    """风险预算"""
    THOST_FTDC_BFC_DataExport = 122
    """数据导出"""
    THOST_FTDC_BFC_RiskTargetSetup = 65
    """风控指标设置"""
    THOST_FTDC_BFC_MarketDataWarn = 66
    """行情预警"""
    THOST_FTDC_BFC_QryBizNotice = 67
    """业务通知查询"""
    THOST_FTDC_BFC_CfgBizNotice = 68
    """业务通知模板设置"""
    THOST_FTDC_BFC_SyncOTP = 69
    """同步动态令牌"""
    THOST_FTDC_BFC_SendBizNotice = 70
    """发送业务通知"""
    THOST_FTDC_BFC_CfgRiskLevelStd = 71
    """风险级别标准设置"""
    THOST_FTDC_BFC_TbCommand = 72
    """交易终端应急功能"""
    THOST_FTDC_BFC_DeleteOrder = 74
    """删除未知单"""
    THOST_FTDC_BFC_ParkedOrderInsert = 75
    """预埋报单插入"""
    THOST_FTDC_BFC_ParkedOrderAction = 76
    """预埋报单操作"""
    THOST_FTDC_BFC_ExecOrderNoCheck = 77
    """资金不够仍允许行权"""
    THOST_FTDC_BFC_Designate = 78
    """指定"""
    THOST_FTDC_BFC_StockDisposal = 79
    """证券处置"""
    THOST_FTDC_BFC_BrokerDepositWarn = 81
    """席位资金预警"""
    THOST_FTDC_BFC_CoverWarn = 83
    """备兑不足预警"""
    THOST_FTDC_BFC_PreExecOrder = 84
    """行权试算"""
    THOST_FTDC_BFC_ExecOrderRisk = 80
    """行权交收风险"""
    THOST_FTDC_BFC_PosiLimitWarn = 85
    """持仓限额预警"""
    THOST_FTDC_BFC_QryPosiLimit = 86
    """持仓限额查询"""
    THOST_FTDC_BFC_FBSign = 87
    """银期签到签退"""
    THOST_FTDC_BFC_FBAccount = 88
    """银期签约解约"""


class TThostFtdcOrderActionStatusType(Enum):
    """报单操作状态类型"""
    THOST_FTDC_OAS_Submitted = 97
    """已经提交"""
    THOST_FTDC_OAS_Accepted = 98
    """已经接受"""
    THOST_FTDC_OAS_Rejected = 99
    """已经被拒绝"""


class TThostFtdcOrderStatusType(Enum):
    """报单状态类型"""
    THOST_FTDC_OST_AllTraded = 48
    """全部成交"""
    THOST_FTDC_OST_PartTradedQueueing = 49
    """部分成交还在队列中"""
    THOST_FTDC_OST_PartTradedNotQueueing = 50
    """部分成交不在队列中"""
    THOST_FTDC_OST_NoTradeQueueing = 51
    """未成交还在队列中"""
    THOST_FTDC_OST_NoTradeNotQueueing = 52
    """未成交不在队列中"""
    THOST_FTDC_OST_Canceled = 53
    """撤单"""
    THOST_FTDC_OST_Unknown = 97
    """未知"""
    THOST_FTDC_OST_NotTouched = 98
    """尚未触发"""
    THOST_FTDC_OST_Touched = 99
    """已触发"""


class TThostFtdcOrderSubmitStatusType(Enum):
    """报单提交状态类型"""
    THOST_FTDC_OSS_InsertSubmitted = 48
    """已经提交"""
    THOST_FTDC_OSS_CancelSubmitted = 49
    """撤单已经提交"""
    THOST_FTDC_OSS_ModifySubmitted = 50
    """修改已经提交"""
    THOST_FTDC_OSS_Accepted = 51
    """已经接受"""
    THOST_FTDC_OSS_InsertRejected = 52
    """报单已经被拒绝"""
    THOST_FTDC_OSS_CancelRejected = 53
    """撤单已经被拒绝"""
    THOST_FTDC_OSS_ModifyRejected = 54
    """改单已经被拒绝"""


class TThostFtdcPositionDateType(Enum):
    """持仓日期类型"""
    THOST_FTDC_PSD_Today = 49
    """今日持仓"""
    THOST_FTDC_PSD_History = 50
    """历史持仓"""


class TThostFtdcPositionDateTypeType(Enum):
    """持仓日期类型类型"""
    THOST_FTDC_PDT_UseHistory = 49
    """使用历史持仓"""
    THOST_FTDC_PDT_NoUseHistory = 50
    """不使用历史持仓"""


class TThostFtdcTradingRoleType(Enum):
    """交易角色类型"""
    THOST_FTDC_ER_Broker = 49
    """代理"""
    THOST_FTDC_ER_Host = 50
    """自营"""
    THOST_FTDC_ER_Maker = 51
    """做市商"""


class TThostFtdcProductClassType(Enum):
    """产品类型类型"""
    THOST_FTDC_PC_Futures = 49
    """期货"""
    THOST_FTDC_PC_Options = 50
    """期货期权"""
    THOST_FTDC_PC_Combination = 51
    """组合"""
    THOST_FTDC_PC_Spot = 52
    """即期"""
    THOST_FTDC_PC_EFP = 53
    """期转现"""
    THOST_FTDC_PC_SpotOption = 54
    """现货期权"""
    THOST_FTDC_PC_TAS = 55
    """TAS合约"""
    THOST_FTDC_PC_MI = 73
    """金属指数"""


class TThostFtdcAPIProductClassType(Enum):
    """产品类型类型"""
    THOST_FTDC_APC_FutureSingle = 49
    """期货单一合约"""
    THOST_FTDC_APC_OptionSingle = 50
    """期权单一合约"""
    THOST_FTDC_APC_Futures = 51
    """可交易期货(含期货组合和期货单一合约)"""
    THOST_FTDC_APC_Options = 52
    """可交易期权(含期权组合和期权单一合约)"""
    THOST_FTDC_APC_TradingComb = 53
    """可下单组合（目前包含DCE和ZCE的期货组合）"""
    THOST_FTDC_APC_UnTradingComb = 54
    """可申请的组合（dce可以申请的组合合约 包含dce可以交易的合约）"""
    THOST_FTDC_APC_AllTrading = 55
    """所有可以交易合约"""
    THOST_FTDC_APC_All = 56
    """所有合约（包含不能交易合约 慎用）"""


class TThostFtdcInstLifePhaseType(Enum):
    """合约生命周期状态类型"""
    THOST_FTDC_IP_NotStart = 48
    """未上市"""
    THOST_FTDC_IP_Started = 49
    """上市"""
    THOST_FTDC_IP_Pause = 50
    """停牌"""
    THOST_FTDC_IP_Expired = 51
    """到期"""


class TThostFtdcDirectionType(Enum):
    """买卖方向类型"""
    THOST_FTDC_D_Buy = 48
    """买"""
    THOST_FTDC_D_Sell = 49
    """卖"""


class TThostFtdcPositionTypeType(Enum):
    """持仓类型类型"""
    THOST_FTDC_PT_Net = 49
    """净持仓"""
    THOST_FTDC_PT_Gross = 50
    """综合持仓"""


class TThostFtdcPosiDirectionType(Enum):
    """持仓多空方向类型"""
    THOST_FTDC_PD_Net = 49
    """净"""
    THOST_FTDC_PD_Long = 50
    """多头"""
    THOST_FTDC_PD_Short = 51
    """空头"""


class TThostFtdcSysSettlementStatusType(Enum):
    """系统结算状态类型"""
    THOST_FTDC_SS_NonActive = 49
    """不活跃"""
    THOST_FTDC_SS_Startup = 50
    """启动"""
    THOST_FTDC_SS_Operating = 51
    """操作"""
    THOST_FTDC_SS_Settlement = 52
    """结算"""
    THOST_FTDC_SS_SettlementFinished = 53
    """结算完成"""


class TThostFtdcRatioAttrType(Enum):
    """费率属性类型"""
    THOST_FTDC_RA_Trade = 48
    """交易费率"""
    THOST_FTDC_RA_Settlement = 49
    """结算费率"""


class TThostFtdcHedgeFlagType(Enum):
    """投机套保标志类型"""
    THOST_FTDC_HF_Speculation = 49
    """投机"""
    THOST_FTDC_HF_Arbitrage = 50
    """套利"""
    THOST_FTDC_HF_Hedge = 51
    """套保"""
    THOST_FTDC_HF_MarketMaker = 53
    """做市商"""
    THOST_FTDC_HF_SpecHedge = 54
    """第一腿投机第二腿套保 大商所专用"""
    THOST_FTDC_HF_HedgeSpec = 55
    """第一腿套保第二腿投机  大商所专用"""


class TThostFtdcBillHedgeFlagType(Enum):
    """投机套保标志类型"""
    THOST_FTDC_BHF_Speculation = 49
    """投机"""
    THOST_FTDC_BHF_Arbitrage = 50
    """套利"""
    THOST_FTDC_BHF_Hedge = 51
    """套保"""


class TThostFtdcClientIDTypeType(Enum):
    """交易编码类型类型"""
    THOST_FTDC_CIDT_Speculation = 49
    """投机"""
    THOST_FTDC_CIDT_Arbitrage = 50
    """套利"""
    THOST_FTDC_CIDT_Hedge = 51
    """套保"""
    THOST_FTDC_CIDT_MarketMaker = 53
    """做市商"""


class TThostFtdcOrderPriceTypeType(Enum):
    """报单价格条件类型"""
    THOST_FTDC_OPT_AnyPrice = 49
    """任意价"""
    THOST_FTDC_OPT_LimitPrice = 50
    """限价"""
    THOST_FTDC_OPT_BestPrice = 51
    """最优价"""
    THOST_FTDC_OPT_LastPrice = 52
    """最新价"""
    THOST_FTDC_OPT_LastPricePlusOneTicks = 53
    """最新价浮动上浮1个ticks"""
    THOST_FTDC_OPT_LastPricePlusTwoTicks = 54
    """最新价浮动上浮2个ticks"""
    THOST_FTDC_OPT_LastPricePlusThreeTicks = 55
    """最新价浮动上浮3个ticks"""
    THOST_FTDC_OPT_AskPrice1 = 56
    """卖一价"""
    THOST_FTDC_OPT_AskPrice1PlusOneTicks = 57
    """卖一价浮动上浮1个ticks"""
    THOST_FTDC_OPT_AskPrice1PlusTwoTicks = 65
    """卖一价浮动上浮2个ticks"""
    THOST_FTDC_OPT_AskPrice1PlusThreeTicks = 66
    """卖一价浮动上浮3个ticks"""
    THOST_FTDC_OPT_BidPrice1 = 67
    """买一价"""
    THOST_FTDC_OPT_BidPrice1PlusOneTicks = 68
    """买一价浮动上浮1个ticks"""
    THOST_FTDC_OPT_BidPrice1PlusTwoTicks = 69
    """买一价浮动上浮2个ticks"""
    THOST_FTDC_OPT_BidPrice1PlusThreeTicks = 70
    """买一价浮动上浮3个ticks"""
    THOST_FTDC_OPT_FiveLevelPrice = 71
    """五档价"""


class TThostFtdcOffsetFlagType(Enum):
    """开平标志类型"""
    THOST_FTDC_OF_Open = 48
    """开仓"""
    THOST_FTDC_OF_Close = 49
    """平仓"""
    THOST_FTDC_OF_ForceClose = 50
    """强平"""
    THOST_FTDC_OF_CloseToday = 51
    """平今"""
    THOST_FTDC_OF_CloseYesterday = 52
    """平昨"""
    THOST_FTDC_OF_ForceOff = 53
    """强减"""
    THOST_FTDC_OF_LocalForceClose = 54
    """本地强平"""


class TThostFtdcForceCloseReasonType(Enum):
    """强平原因类型"""
    THOST_FTDC_FCC_NotForceClose = 48
    """非强平"""
    THOST_FTDC_FCC_LackDeposit = 49
    """资金不足"""
    THOST_FTDC_FCC_ClientOverPositionLimit = 50
    """客户超仓"""
    THOST_FTDC_FCC_MemberOverPositionLimit = 51
    """会员超仓"""
    THOST_FTDC_FCC_NotMultiple = 52
    """持仓非整数倍"""
    THOST_FTDC_FCC_Violation = 53
    """违规"""
    THOST_FTDC_FCC_Other = 54
    """其它"""
    THOST_FTDC_FCC_PersonDeliv = 55
    """自然人临近交割"""


class TThostFtdcOrderTypeType(Enum):
    """报单类型类型"""
    THOST_FTDC_ORDT_Normal = 48
    """正常"""
    THOST_FTDC_ORDT_DeriveFromQuote = 49
    """报价衍生"""
    THOST_FTDC_ORDT_DeriveFromCombination = 50
    """组合衍生"""
    THOST_FTDC_ORDT_Combination = 51
    """组合报单"""
    THOST_FTDC_ORDT_ConditionalOrder = 52
    """条件单"""
    THOST_FTDC_ORDT_Swap = 53
    """互换单"""
    THOST_FTDC_ORDT_DeriveFromBlockTrade = 54
    """大宗交易成交衍生"""
    THOST_FTDC_ORDT_DeriveFromEFPTrade = 55
    """期转现成交衍生"""


class TThostFtdcTimeConditionType(Enum):
    """有效期类型类型"""
    THOST_FTDC_TC_IOC = 49
    """立即完成，否则撤销"""
    THOST_FTDC_TC_GFS = 50
    """本节有效"""
    THOST_FTDC_TC_GFD = 51
    """当日有效"""
    THOST_FTDC_TC_GTD = 52
    """指定日期前有效"""
    THOST_FTDC_TC_GTC = 53
    """撤销前有效"""
    THOST_FTDC_TC_GFA = 54
    """集合竞价有效"""


class TThostFtdcVolumeConditionType(Enum):
    """成交量类型类型"""
    THOST_FTDC_VC_AV = 49
    """任何数量"""
    THOST_FTDC_VC_MV = 50
    """最小数量"""
    THOST_FTDC_VC_CV = 51
    """全部数量"""


class TThostFtdcContingentConditionType(Enum):
    """触发条件类型"""
    THOST_FTDC_CC_Immediately = 49
    """立即"""
    THOST_FTDC_CC_Touch = 50
    """止损"""
    THOST_FTDC_CC_TouchProfit = 51
    """止赢"""
    THOST_FTDC_CC_ParkedOrder = 52
    """预埋单"""
    THOST_FTDC_CC_LastPriceGreaterThanStopPrice = 53
    """最新价大于条件价"""
    THOST_FTDC_CC_LastPriceGreaterEqualStopPrice = 54
    """最新价大于等于条件价"""
    THOST_FTDC_CC_LastPriceLesserThanStopPrice = 55
    """最新价小于条件价"""
    THOST_FTDC_CC_LastPriceLesserEqualStopPrice = 56
    """最新价小于等于条件价"""
    THOST_FTDC_CC_AskPriceGreaterThanStopPrice = 57
    """卖一价大于条件价"""
    THOST_FTDC_CC_AskPriceGreaterEqualStopPrice = 65
    """卖一价大于等于条件价"""
    THOST_FTDC_CC_AskPriceLesserThanStopPrice = 66
    """卖一价小于条件价"""
    THOST_FTDC_CC_AskPriceLesserEqualStopPrice = 67
    """卖一价小于等于条件价"""
    THOST_FTDC_CC_BidPriceGreaterThanStopPrice = 68
    """买一价大于条件价"""
    THOST_FTDC_CC_BidPriceGreaterEqualStopPrice = 69
    """买一价大于等于条件价"""
    THOST_FTDC_CC_BidPriceLesserThanStopPrice = 70
    """买一价小于条件价"""
    THOST_FTDC_CC_BidPriceLesserEqualStopPrice = 72
    """买一价小于等于条件价"""


class TThostFtdcActionFlagType(Enum):
    """操作标志类型"""
    THOST_FTDC_AF_Delete = 48
    """删除"""
    THOST_FTDC_AF_Modify = 51
    """修改"""


class TThostFtdcTradingRightType(Enum):
    """交易权限类型"""
    THOST_FTDC_TR_Allow = 48
    """可以交易"""
    THOST_FTDC_TR_CloseOnly = 49
    """只能平仓"""
    THOST_FTDC_TR_Forbidden = 50
    """不能交易"""


class TThostFtdcOrderSourceType(Enum):
    """报单来源类型"""
    THOST_FTDC_OSRC_Participant = 48
    """来自参与者"""
    THOST_FTDC_OSRC_Administrator = 49
    """来自管理员"""


class TThostFtdcTradeTypeType(Enum):
    """成交类型类型"""
    THOST_FTDC_TRDT_SplitCombinatio = 110
    """组合持仓拆分为单一持仓,初始化不应包含该类型的持仓"""
    THOST_FTDC_TRDT_Common = 48
    """普通成交"""
    THOST_FTDC_TRDT_OptionsExecution = 49
    """期权执行"""
    THOST_FTDC_TRDT_OTC = 50
    """OTC成交"""
    THOST_FTDC_TRDT_EFPDerived = 51
    """期转现衍生成交"""
    THOST_FTDC_TRDT_CombinationDerived = 52
    """组合衍生成交"""
    THOST_FTDC_TRDT_BlockTrade = 53
    """大宗交易成交"""


class TThostFtdcSpecPosiTypeType(Enum):
    """特殊持仓明细标识类型"""
    THOST_FTDC_SPOST_Commo = 110
    """普通持仓明细"""
    THOST_FTDC_SPOST_Tas = 48
    """TAS合约成交产生的标的合约持仓明细"""


class TThostFtdcPriceSourceType(Enum):
    """成交价来源类型"""
    THOST_FTDC_PSRC_LastPrice = 48
    """前成交价"""
    THOST_FTDC_PSRC_Buy = 49
    """买委托价"""
    THOST_FTDC_PSRC_Sell = 50
    """卖委托价"""
    THOST_FTDC_PSRC_OTC = 51
    """场外成交价"""


class TThostFtdcInstrumentStatusType(Enum):
    """合约交易状态类型"""
    THOST_FTDC_IS_BeforeTrading = 48
    """开盘前"""
    THOST_FTDC_IS_NoTrading = 49
    """非交易"""
    THOST_FTDC_IS_Continous = 50
    """连续交易"""
    THOST_FTDC_IS_AuctionOrdering = 51
    """集合竞价报单"""
    THOST_FTDC_IS_AuctionBalance = 52
    """集合竞价价格平衡"""
    THOST_FTDC_IS_AuctionMatch = 53
    """集合竞价撮合"""
    THOST_FTDC_IS_Closed = 54
    """收盘"""


class TThostFtdcInstStatusEnterReasonType(Enum):
    """品种进入交易状态原因类型"""
    THOST_FTDC_IER_Automatic = 49
    """自动切换"""
    THOST_FTDC_IER_Manual = 50
    """手动切换"""
    THOST_FTDC_IER_Fuse = 51
    """熔断"""


class TThostFtdcBatchStatusType(Enum):
    """处理状态类型"""
    THOST_FTDC_BS_NoUpload = 49
    """未上传"""
    THOST_FTDC_BS_Uploaded = 50
    """已上传"""
    THOST_FTDC_BS_Failed = 51
    """审核失败"""


class TThostFtdcReturnStyleType(Enum):
    """按品种返还方式类型"""
    THOST_FTDC_RS_All = 49
    """按所有品种"""
    THOST_FTDC_RS_ByProduct = 50
    """按品种"""


class TThostFtdcReturnPatternType(Enum):
    """返还模式类型"""
    THOST_FTDC_RP_ByVolume = 49
    """按成交手数"""
    THOST_FTDC_RP_ByFeeOnHand = 50
    """按留存手续费"""


class TThostFtdcReturnLevelType(Enum):
    """返还级别类型"""
    THOST_FTDC_RL_Level1 = 49
    """级别1"""
    THOST_FTDC_RL_Level2 = 50
    """级别2"""
    THOST_FTDC_RL_Level3 = 51
    """级别3"""
    THOST_FTDC_RL_Level4 = 52
    """级别4"""
    THOST_FTDC_RL_Level5 = 53
    """级别5"""
    THOST_FTDC_RL_Level6 = 54
    """级别6"""
    THOST_FTDC_RL_Level7 = 55
    """级别7"""
    THOST_FTDC_RL_Level8 = 56
    """级别8"""
    THOST_FTDC_RL_Level9 = 57
    """级别9"""


class TThostFtdcReturnStandardType(Enum):
    """返还标准类型"""
    THOST_FTDC_RSD_ByPeriod = 49
    """分阶段返还"""
    THOST_FTDC_RSD_ByStandard = 50
    """按某一标准"""


class TThostFtdcMortgageTypeType(Enum):
    """质押类型类型"""
    THOST_FTDC_MT_Out = 48
    """质出"""
    THOST_FTDC_MT_In = 49
    """质入"""


class TThostFtdcInvestorSettlementParamIDType(Enum):
    """投资者结算参数代码类型"""
    THOST_FTDC_ISPI_MortgageRatio = 52
    """质押比例"""
    THOST_FTDC_ISPI_MarginWay = 53
    """保证金算法"""
    THOST_FTDC_ISPI_BillDeposit = 57
    """结算单结存是否包含质押"""


class TThostFtdcExchangeSettlementParamIDType(Enum):
    """交易所结算参数代码类型"""
    THOST_FTDC_ESPI_MortgageRatio = 49
    """质押比例"""
    THOST_FTDC_ESPI_OtherFundItem = 50
    """分项资金导入项"""
    THOST_FTDC_ESPI_OtherFundImport = 51
    """分项资金入交易所出入金"""
    THOST_FTDC_ESPI_CFFEXMinPrepa = 54
    """中金所开户最低可用金额"""
    THOST_FTDC_ESPI_CZCESettlementType = 55
    """郑商所结算方式"""
    THOST_FTDC_ESPI_ExchDelivFeeMode = 57
    """交易所交割手续费收取方式"""
    THOST_FTDC_ESPI_DelivFeeMode = 48
    """投资者交割手续费收取方式"""
    THOST_FTDC_ESPI_CZCEComMarginType = 65
    """郑商所组合持仓保证金收取方式"""
    THOST_FTDC_ESPI_DceComMarginType = 66
    """大商所套利保证金是否优惠"""
    THOST_FTDC_ESPI_OptOutDisCountRate = 97
    """虚值期权保证金优惠比率"""
    THOST_FTDC_ESPI_OptMiniGuarantee = 98
    """最低保障系数"""


class TThostFtdcSystemParamIDType(Enum):
    """系统参数代码类型"""
    THOST_FTDC_SPI_InvestorIDMinLength = 49
    """投资者代码最小长度"""
    THOST_FTDC_SPI_AccountIDMinLength = 50
    """投资者帐号代码最小长度"""
    THOST_FTDC_SPI_UserRightLogon = 51
    """投资者开户默认登录权限"""
    THOST_FTDC_SPI_SettlementBillTrade = 52
    """投资者交易结算单成交汇总方式"""
    THOST_FTDC_SPI_TradingCode = 53
    """统一开户更新交易编码方式"""
    THOST_FTDC_SPI_CheckFund = 54
    """结算是否判断存在未复核的出入金和分项资金"""
    THOST_FTDC_SPI_CommModelRight = 55
    """是否启用手续费模板数据权限"""
    THOST_FTDC_SPI_MarginModelRight = 57
    """是否启用保证金率模板数据权限"""
    THOST_FTDC_SPI_IsStandardActive = 56
    """是否规范用户才能激活"""
    THOST_FTDC_SPI_UploadSettlementFile = 85
    """上传的交易所结算文件路径"""
    THOST_FTDC_SPI_DownloadCSRCFile = 68
    """上报保证金监控中心文件路径"""
    THOST_FTDC_SPI_SettlementBillFile = 83
    """生成的结算单文件路径"""
    THOST_FTDC_SPI_CSRCOthersFile = 67
    """证监会文件标识"""
    THOST_FTDC_SPI_InvestorPhoto = 80
    """投资者照片路径"""
    THOST_FTDC_SPI_CSRCData = 82
    """全结经纪公司上传文件路径"""
    THOST_FTDC_SPI_InvestorPwdModel = 73
    """开户密码录入方式"""
    THOST_FTDC_SPI_CFFEXInvestorSettleFile = 70
    """投资者中金所结算文件下载路径"""
    THOST_FTDC_SPI_InvestorIDType = 97
    """投资者代码编码方式"""
    THOST_FTDC_SPI_FreezeMaxReMain = 114
    """休眠户最高权益"""
    THOST_FTDC_SPI_IsSync = 65
    """手续费相关操作实时上场开关"""
    THOST_FTDC_SPI_RelieveOpenLimit = 79
    """解除开仓权限限制"""
    THOST_FTDC_SPI_IsStandardFreeze = 88
    """是否规范用户才能休眠"""
    THOST_FTDC_SPI_CZCENormalProductHedge = 66
    """郑商所是否开放所有品种套保交易"""


class TThostFtdcTradeParamIDType(Enum):
    """交易系统参数代码类型"""
    THOST_FTDC_TPID_EncryptionStandard = 69
    """系统加密算法"""
    THOST_FTDC_TPID_RiskMode = 82
    """系统风险算法"""
    THOST_FTDC_TPID_RiskModeGlobal = 71
    """系统风险算法是否全局 0-否 1-是"""
    THOST_FTDC_TPID_modeEncode = 80
    """密码加密算法"""
    THOST_FTDC_TPID_tickMode = 84
    """价格小数位数参数"""
    THOST_FTDC_TPID_SingleUserSessionMaxNum = 83
    """用户最大会话数"""
    THOST_FTDC_TPID_LoginFailMaxNum = 76
    """最大连续登录失败数"""
    THOST_FTDC_TPID_IsAuthForce = 65
    """是否强制认证"""
    THOST_FTDC_TPID_IsPosiFreeze = 70
    """是否冻结证券持仓"""
    THOST_FTDC_TPID_IsPosiLimit = 77
    """是否限仓"""
    THOST_FTDC_TPID_ForQuoteTimeInterval = 81
    """郑商所询价时间间隔"""
    THOST_FTDC_TPID_IsFuturePosiLimit = 66
    """是否期货限仓"""
    THOST_FTDC_TPID_IsFutureOrderFreq = 67
    """是否期货下单频率限制"""
    THOST_FTDC_TPID_IsExecOrderProfit = 72
    """行权冻结是否计算盈利"""
    THOST_FTDC_TPID_IsCheckBankAcc = 73
    """银期开户是否验证开户银行卡号是否是预留银行账户"""
    THOST_FTDC_TPID_PasswordDeadLine = 74
    """弱密码最后修改日期"""
    THOST_FTDC_TPID_IsStrongPassword = 75
    """强密码校验"""
    THOST_FTDC_TPID_BalanceMorgage = 97
    """自有资金质押比"""
    THOST_FTDC_TPID_MinPwdLen = 79
    """最小密码长度"""
    THOST_FTDC_TPID_LoginFailMaxNumForIP = 85
    """IP当日最大登陆失败次数"""
    THOST_FTDC_TPID_PasswordPeriod = 86
    """密码有效期"""


class TThostFtdcFileIDType(Enum):
    """文件标识类型"""
    THOST_FTDC_FI_SettlementFund = 70
    """资金数据"""
    THOST_FTDC_FI_Trade = 84
    """成交数据"""
    THOST_FTDC_FI_InvestorPosition = 80
    """投资者持仓数据"""
    THOST_FTDC_FI_SubEntryFund = 79
    """投资者分项资金数据"""
    THOST_FTDC_FI_CZCECombinationPos = 67
    """组合持仓数据"""
    THOST_FTDC_FI_CSRCData = 82
    """上报保证金监控中心数据"""
    THOST_FTDC_FI_CZCEClose = 76
    """郑商所平仓了结数据"""
    THOST_FTDC_FI_CZCENoClose = 78
    """郑商所非平仓了结数据"""
    THOST_FTDC_FI_PositionDtl = 68
    """持仓明细数据"""
    THOST_FTDC_FI_OptionStrike = 83
    """期权执行文件"""
    THOST_FTDC_FI_SettlementPriceComparison = 77
    """结算价比对文件"""
    THOST_FTDC_FI_NonTradePosChange = 66
    """上期所非持仓变动明细"""


class TThostFtdcFileTypeType(Enum):
    """文件上传类型类型"""
    THOST_FTDC_FUT_Settlement = 48
    """结算"""
    THOST_FTDC_FUT_Check = 49
    """核对"""


class TThostFtdcFileFormatType(Enum):
    """文件格式类型"""
    THOST_FTDC_FFT_Txt = 48
    """文本文件(.txt)"""
    THOST_FTDC_FFT_Zip = 49
    """压缩文件(.zip)"""
    THOST_FTDC_FFT_DBF = 50
    """DBF文件(.dbf)"""


class TThostFtdcFileUploadStatusType(Enum):
    """文件状态类型"""
    THOST_FTDC_FUS_SucceedUpload = 49
    """上传成功"""
    THOST_FTDC_FUS_FailedUpload = 50
    """上传失败"""
    THOST_FTDC_FUS_SucceedLoad = 51
    """导入成功"""
    THOST_FTDC_FUS_PartSucceedLoad = 52
    """导入部分成功"""
    THOST_FTDC_FUS_FailedLoad = 53
    """导入失败"""


class TThostFtdcTransferDirectionType(Enum):
    """移仓方向类型"""
    THOST_FTDC_TD_Out = 48
    """移出"""
    THOST_FTDC_TD_In = 49
    """移入"""


class TThostFtdcSpecialCreateRuleType(Enum):
    """特殊的创建规则类型"""
    THOST_FTDC_SC_NoSpecialRule = 48
    """没有特殊创建规则"""
    THOST_FTDC_SC_NoSpringFestival = 49
    """不包含春节"""


class TThostFtdcBasisPriceTypeType(Enum):
    """挂牌基准价类型类型"""
    THOST_FTDC_IPT_LastSettlement = 49
    """上一合约结算价"""
    THOST_FTDC_IPT_LaseClose = 50
    """上一合约收盘价"""


class TThostFtdcProductLifePhaseType(Enum):
    """产品生命周期状态类型"""
    THOST_FTDC_PLP_Active = 49
    """活跃"""
    THOST_FTDC_PLP_NonActive = 50
    """不活跃"""
    THOST_FTDC_PLP_Canceled = 51
    """注销"""


class TThostFtdcDeliveryModeType(Enum):
    """交割方式类型"""
    THOST_FTDC_DM_CashDeliv = 49
    """现金交割"""
    THOST_FTDC_DM_CommodityDeliv = 50
    """实物交割"""


class TThostFtdcFundIOTypeType(Enum):
    """出入金类型类型"""
    THOST_FTDC_FIOT_FundIO = 49
    """出入金"""
    THOST_FTDC_FIOT_Transfer = 50
    """银期转帐"""
    THOST_FTDC_FIOT_SwapCurrency = 51
    """银期换汇"""


class TThostFtdcFundTypeType(Enum):
    """资金类型类型"""
    THOST_FTDC_FT_Deposite = 49
    """银行存款"""
    THOST_FTDC_FT_ItemFund = 50
    """分项资金"""
    THOST_FTDC_FT_Company = 51
    """公司调整"""
    THOST_FTDC_FT_InnerTransfer = 52
    """资金内转"""


class TThostFtdcFundDirectionType(Enum):
    """出入金方向类型"""
    THOST_FTDC_FD_In = 49
    """入金"""
    THOST_FTDC_FD_Out = 50
    """出金"""


class TThostFtdcFundStatusType(Enum):
    """资金状态类型"""
    THOST_FTDC_FS_Record = 49
    """已录入"""
    THOST_FTDC_FS_Check = 50
    """已复核"""
    THOST_FTDC_FS_Charge = 51
    """已冲销"""


class TThostFtdcPublishStatusType(Enum):
    """发布状态类型"""
    THOST_FTDC_PS_None = 49
    """未发布"""
    THOST_FTDC_PS_Publishing = 50
    """正在发布"""
    THOST_FTDC_PS_Published = 51
    """已发布"""


class TThostFtdcSystemStatusType(Enum):
    """系统状态类型"""
    THOST_FTDC_ES_NonActive = 49
    """不活跃"""
    THOST_FTDC_ES_Startup = 50
    """启动"""
    THOST_FTDC_ES_Initialize = 51
    """交易开始初始化"""
    THOST_FTDC_ES_Initialized = 52
    """交易完成初始化"""
    THOST_FTDC_ES_Close = 53
    """收市开始"""
    THOST_FTDC_ES_Closed = 54
    """收市完成"""
    THOST_FTDC_ES_Settlement = 55
    """结算"""


class TThostFtdcSettlementStatusType(Enum):
    """结算状态类型"""
    THOST_FTDC_STS_Initialize = 48
    """初始"""
    THOST_FTDC_STS_Settlementing = 49
    """结算中"""
    THOST_FTDC_STS_Settlemented = 50
    """已结算"""
    THOST_FTDC_STS_Finished = 51
    """结算完成"""


class TThostFtdcInvestorTypeType(Enum):
    """投资者类型类型"""
    THOST_FTDC_CT_Person = 48
    """自然人"""
    THOST_FTDC_CT_Company = 49
    """法人"""
    THOST_FTDC_CT_Fund = 50
    """投资基金"""
    THOST_FTDC_CT_SpecialOrgan = 51
    """特殊法人"""
    THOST_FTDC_CT_Asset = 52
    """资管户"""


class TThostFtdcBrokerTypeType(Enum):
    """经纪公司类型类型"""
    THOST_FTDC_BT_Trade = 48
    """交易会员"""
    THOST_FTDC_BT_TradeSettle = 49
    """交易结算会员"""


class TThostFtdcRiskLevelType(Enum):
    """风险等级类型"""
    THOST_FTDC_FAS_Low = 49
    """低风险客户"""
    THOST_FTDC_FAS_Normal = 50
    """普通客户"""
    THOST_FTDC_FAS_Focus = 51
    """关注客户"""
    THOST_FTDC_FAS_Risk = 52
    """风险客户"""


class TThostFtdcFeeAcceptStyleType(Enum):
    """手续费收取方式类型"""
    THOST_FTDC_FAS_ByTrade = 49
    """按交易收取"""
    THOST_FTDC_FAS_ByDeliv = 50
    """按交割收取"""
    THOST_FTDC_FAS_None = 51
    """不收"""
    THOST_FTDC_FAS_FixFee = 52
    """按指定手续费收取"""


class TThostFtdcPasswordTypeType(Enum):
    """密码类型类型"""
    THOST_FTDC_PWDT_Trade = 49
    """交易密码"""
    THOST_FTDC_PWDT_Account = 50
    """资金密码"""


class TThostFtdcAlgorithmType(Enum):
    """盈亏算法类型"""
    THOST_FTDC_AG_All = 49
    """浮盈浮亏都计算"""
    THOST_FTDC_AG_OnlyLost = 50
    """浮盈不计，浮亏计"""
    THOST_FTDC_AG_OnlyGain = 51
    """浮盈计，浮亏不计"""
    THOST_FTDC_AG_None = 52
    """浮盈浮亏都不计算"""


class TThostFtdcIncludeCloseProfitType(Enum):
    """是否包含平仓盈利类型"""
    THOST_FTDC_ICP_Include = 48
    """包含平仓盈利"""
    THOST_FTDC_ICP_NotInclude = 50
    """不包含平仓盈利"""


class TThostFtdcAllWithoutTradeType(Enum):
    """是否受可提比例限制类型"""
    THOST_FTDC_AWT_Enable = 48
    """无仓无成交不受可提比例限制"""
    THOST_FTDC_AWT_Disable = 50
    """受可提比例限制"""
    THOST_FTDC_AWT_NoHoldEnable = 51
    """无仓不受可提比例限制"""


class TThostFtdcFuturePwdFlagType(Enum):
    """资金密码核对标志类型"""
    THOST_FTDC_FPWD_UnCheck = 48
    """不核对"""
    THOST_FTDC_FPWD_Check = 49
    """核对"""


class TThostFtdcTransferTypeType(Enum):
    """银期转账类型类型"""
    THOST_FTDC_TT_BankToFuture = 48
    """银行转期货"""
    THOST_FTDC_TT_FutureToBank = 49
    """期货转银行"""


class TThostFtdcTransferValidFlagType(Enum):
    """转账有效标志类型"""
    THOST_FTDC_TVF_Invalid = 48
    """无效或失败"""
    THOST_FTDC_TVF_Valid = 49
    """有效"""
    THOST_FTDC_TVF_Reverse = 50
    """冲正"""


class TThostFtdcReasonType(Enum):
    """事由类型"""
    THOST_FTDC_RN_CD = 48
    """错单"""
    THOST_FTDC_RN_ZT = 49
    """资金在途"""
    THOST_FTDC_RN_QT = 50
    """其它"""


class TThostFtdcSexType(Enum):
    """性别类型"""
    THOST_FTDC_SEX_None = 48
    """未知"""
    THOST_FTDC_SEX_Man = 49
    """男"""
    THOST_FTDC_SEX_Woman = 50
    """女"""


class TThostFtdcUserTypeType(Enum):
    """用户类型类型"""
    THOST_FTDC_UT_Investor = 48
    """投资者"""
    THOST_FTDC_UT_Operator = 49
    """操作员"""
    THOST_FTDC_UT_SuperUser = 50
    """管理员"""


class TThostFtdcRateTypeType(Enum):
    """费率类型类型"""
    THOST_FTDC_RATETYPE_MarginRate = 50
    """保证金率"""


class TThostFtdcNoteTypeType(Enum):
    """通知类型类型"""
    THOST_FTDC_NOTETYPE_TradeSettleBill = 49
    """交易结算单"""
    THOST_FTDC_NOTETYPE_TradeSettleMonth = 50
    """交易结算月报"""
    THOST_FTDC_NOTETYPE_CallMarginNotes = 51
    """追加保证金通知书"""
    THOST_FTDC_NOTETYPE_ForceCloseNotes = 52
    """强行平仓通知书"""
    THOST_FTDC_NOTETYPE_TradeNotes = 53
    """成交通知书"""
    THOST_FTDC_NOTETYPE_DelivNotes = 54
    """交割通知书"""


class TThostFtdcSettlementStyleType(Enum):
    """结算单方式类型"""
    THOST_FTDC_SBS_Day = 49
    """逐日盯市"""
    THOST_FTDC_SBS_Volume = 50
    """逐笔对冲"""


class TThostFtdcSettlementBillTypeType(Enum):
    """结算单类型类型"""
    THOST_FTDC_ST_Day = 48
    """日报"""
    THOST_FTDC_ST_Month = 49
    """月报"""


class TThostFtdcUserRightTypeType(Enum):
    """客户权限类型类型"""
    THOST_FTDC_URT_Logon = 49
    """登录"""
    THOST_FTDC_URT_Transfer = 50
    """银期转帐"""
    THOST_FTDC_URT_EMail = 51
    """邮寄结算单"""
    THOST_FTDC_URT_Fax = 52
    """传真结算单"""
    THOST_FTDC_URT_ConditionOrder = 53
    """条件单"""


class TThostFtdcMarginPriceTypeType(Enum):
    """保证金价格类型类型"""
    THOST_FTDC_MPT_PreSettlementPrice = 49
    """昨结算价"""
    THOST_FTDC_MPT_SettlementPrice = 50
    """最新价"""
    THOST_FTDC_MPT_AveragePrice = 51
    """成交均价"""
    THOST_FTDC_MPT_OpenPrice = 52
    """开仓价"""


class TThostFtdcBillGenStatusType(Enum):
    """结算单生成状态类型"""
    THOST_FTDC_BGS_None = 48
    """未生成"""
    THOST_FTDC_BGS_NoGenerated = 49
    """生成中"""
    THOST_FTDC_BGS_Generated = 50
    """已生成"""


class TThostFtdcAlgoTypeType(Enum):
    """算法类型类型"""
    THOST_FTDC_AT_HandlePositionAlgo = 49
    """持仓处理算法"""
    THOST_FTDC_AT_FindMarginRateAlgo = 50
    """寻找保证金率算法"""


class TThostFtdcHandlePositionAlgoIDType(Enum):
    """持仓处理算法编号类型"""
    THOST_FTDC_HPA_Base = 49
    """基本"""
    THOST_FTDC_HPA_DCE = 50
    """大连商品交易所"""
    THOST_FTDC_HPA_CZCE = 51
    """郑州商品交易所"""


class TThostFtdcFindMarginRateAlgoIDType(Enum):
    """寻找保证金率算法编号类型"""
    THOST_FTDC_FMRA_Base = 49
    """基本"""
    THOST_FTDC_FMRA_DCE = 50
    """大连商品交易所"""
    THOST_FTDC_FMRA_CZCE = 51
    """郑州商品交易所"""


class TThostFtdcHandleTradingAccountAlgoIDType(Enum):
    """资金处理算法编号类型"""
    THOST_FTDC_HTAA_Base = 49
    """基本"""
    THOST_FTDC_HTAA_DCE = 50
    """大连商品交易所"""
    THOST_FTDC_HTAA_CZCE = 51
    """郑州商品交易所"""


class TThostFtdcPersonTypeType(Enum):
    """联系人类型类型"""
    THOST_FTDC_PST_Order = 49
    """指定下单人"""
    THOST_FTDC_PST_Open = 50
    """开户授权人"""
    THOST_FTDC_PST_Fund = 51
    """资金调拨人"""
    THOST_FTDC_PST_Settlement = 52
    """结算单确认人"""
    THOST_FTDC_PST_Company = 53
    """法人"""
    THOST_FTDC_PST_Corporation = 54
    """法人代表"""
    THOST_FTDC_PST_LinkMan = 55
    """投资者联系人"""
    THOST_FTDC_PST_Ledger = 56
    """分户管理资产负责人"""
    THOST_FTDC_PST_Trustee = 57
    """托（保）管人"""
    THOST_FTDC_PST_TrusteeCorporation = 65
    """托（保）管机构法人代表"""
    THOST_FTDC_PST_TrusteeOpen = 66
    """托（保）管机构开户授权人"""
    THOST_FTDC_PST_TrusteeContact = 67
    """托（保）管机构联系人"""
    THOST_FTDC_PST_ForeignerRefer = 68
    """境外自然人参考证件"""
    THOST_FTDC_PST_CorporationRefer = 69
    """法人代表参考证件"""


class TThostFtdcQueryInvestorRangeType(Enum):
    """查询范围类型"""
    THOST_FTDC_QIR_All = 49
    """所有"""
    THOST_FTDC_QIR_Group = 50
    """查询分类"""
    THOST_FTDC_QIR_Single = 51
    """单一投资者"""


class TThostFtdcInvestorRiskStatusType(Enum):
    """投资者风险状态类型"""
    THOST_FTDC_IRS_Normal = 49
    """正常"""
    THOST_FTDC_IRS_Warn = 50
    """警告"""
    THOST_FTDC_IRS_Call = 51
    """追保"""
    THOST_FTDC_IRS_Force = 52
    """强平"""
    THOST_FTDC_IRS_Exception = 53
    """异常"""


class TThostFtdcUserEventTypeType(Enum):
    """用户事件类型类型"""
    THOST_FTDC_UET_Login = 49
    """登录"""
    THOST_FTDC_UET_Logout = 50
    """登出"""
    THOST_FTDC_UET_Trading = 51
    """交易成功"""
    THOST_FTDC_UET_TradingError = 52
    """交易失败"""
    THOST_FTDC_UET_UpdatePassword = 53
    """修改密码"""
    THOST_FTDC_UET_Authenticate = 54
    """客户端认证"""
    THOST_FTDC_UET_SubmitSysInfo = 55
    """终端信息上报"""
    THOST_FTDC_UET_Transfer = 56
    """转账"""
    THOST_FTDC_UET_Other = 57
    """其他"""


class TThostFtdcCloseStyleType(Enum):
    """平仓方式类型"""
    THOST_FTDC_ICS_Close = 48
    """先开先平"""
    THOST_FTDC_ICS_CloseToday = 49
    """先平今再平昨"""


class TThostFtdcStatModeType(Enum):
    """统计方式类型"""
    THOST_FTDC_SM_Non = 48
    """----"""
    THOST_FTDC_SM_Instrument = 49
    """按合约统计"""
    THOST_FTDC_SM_Product = 50
    """按产品统计"""
    THOST_FTDC_SM_Investor = 51
    """按投资者统计"""


class TThostFtdcParkedOrderStatusType(Enum):
    """预埋单状态类型"""
    THOST_FTDC_PAOS_NotSend = 49
    """未发送"""
    THOST_FTDC_PAOS_Send = 50
    """已发送"""
    THOST_FTDC_PAOS_Deleted = 51
    """已删除"""


class TThostFtdcVirDealStatusType(Enum):
    """处理状态类型"""
    THOST_FTDC_VDS_Dealing = 49
    """正在处理"""
    THOST_FTDC_VDS_DeaclSucceed = 50
    """处理成功"""


class TThostFtdcOrgSystemIDType(Enum):
    """原有系统代码类型"""
    THOST_FTDC_ORGS_Standard = 48
    """综合交易平台"""
    THOST_FTDC_ORGS_ESunny = 49
    """易盛系统"""
    THOST_FTDC_ORGS_KingStarV6 = 50
    """金仕达V6系统"""


class TThostFtdcVirTradeStatusType(Enum):
    """交易状态类型"""
    THOST_FTDC_VTS_NaturalDeal = 48
    """正常处理中"""
    THOST_FTDC_VTS_SucceedEnd = 49
    """成功结束"""
    THOST_FTDC_VTS_FailedEND = 50
    """失败结束"""
    THOST_FTDC_VTS_Exception = 51
    """异常中"""
    THOST_FTDC_VTS_ManualDeal = 52
    """已人工异常处理"""
    THOST_FTDC_VTS_MesException = 53
    """通讯异常 ，请人工处理"""
    THOST_FTDC_VTS_SysException = 54
    """系统出错，请人工处理"""


class TThostFtdcVirBankAccTypeType(Enum):
    """银行帐户类型类型"""
    THOST_FTDC_VBAT_BankBook = 49
    """存折"""
    THOST_FTDC_VBAT_BankCard = 50
    """储蓄卡"""
    THOST_FTDC_VBAT_CreditCard = 51
    """信用卡"""


class TThostFtdcVirementStatusType(Enum):
    """银行帐户类型类型"""
    THOST_FTDC_VMS_Natural = 48
    """正常"""
    THOST_FTDC_VMS_Canceled = 57
    """销户"""


class TThostFtdcVirementAvailAbilityType(Enum):
    """有效标志类型"""
    THOST_FTDC_VAA_NoAvailAbility = 48
    """未确认"""
    THOST_FTDC_VAA_AvailAbility = 49
    """有效"""
    THOST_FTDC_VAA_Repeal = 50
    """冲正"""


class TThostFtdcVirementTradeCodeType(Enum):
    """交易代码类型"""
    THOST_FTDC_VTC_BankBankToFuture = 49
    """银行发起银行资金转期货"""
    THOST_FTDC_VTC_BankFutureToBank = 50
    """银行发起期货资金转银行"""
    THOST_FTDC_VTC_FutureBankToFuture = 49
    """期货发起银行资金转期货"""
    THOST_FTDC_VTC_FutureFutureToBank = 50
    """期货发起期货资金转银行"""


class TThostFtdcAMLGenStatusType(Enum):
    """Aml生成方式类型"""
    THOST_FTDC_GEN_Program = 48
    """程序生成"""
    THOST_FTDC_GEN_HandWork = 49
    """人工生成"""


class TThostFtdcCFMMCKeyKindType(Enum):
    """动态密钥类别(保证金监管)类型"""
    THOST_FTDC_CFMMCKK_REQUEST = 82
    """主动请求更新"""
    THOST_FTDC_CFMMCKK_AUTO = 65
    """CFMMC自动更新"""
    THOST_FTDC_CFMMCKK_MANUAL = 77
    """CFMMC手动更新"""


class TThostFtdcCertificationTypeType(Enum):
    """证件类型类型"""
    THOST_FTDC_CFT_IDCard = 48
    """身份证"""
    THOST_FTDC_CFT_Passport = 49
    """护照"""
    THOST_FTDC_CFT_OfficerIDCard = 50
    """军官证"""
    THOST_FTDC_CFT_SoldierIDCard = 51
    """士兵证"""
    THOST_FTDC_CFT_HomeComingCard = 52
    """回乡证"""
    THOST_FTDC_CFT_HouseholdRegister = 53
    """户口簿"""
    THOST_FTDC_CFT_LicenseNo = 54
    """营业执照号"""
    THOST_FTDC_CFT_InstitutionCodeCard = 55
    """组织机构代码证"""
    THOST_FTDC_CFT_TempLicenseNo = 56
    """临时营业执照号"""
    THOST_FTDC_CFT_NoEnterpriseLicenseNo = 57
    """民办非企业登记证书"""
    THOST_FTDC_CFT_OtherCard = 120
    """其他证件"""
    THOST_FTDC_CFT_SuperDepAgree = 97
    """主管部门批文"""


class TThostFtdcFileBusinessCodeType(Enum):
    """文件业务功能类型"""
    THOST_FTDC_FBC_Others = 48
    """其他"""
    THOST_FTDC_FBC_TransferDetails = 49
    """转账交易明细对账"""
    THOST_FTDC_FBC_CustAccStatus = 50
    """客户账户状态对账"""
    THOST_FTDC_FBC_AccountTradeDetails = 51
    """账户类交易明细对账"""
    THOST_FTDC_FBC_FutureAccountChangeInfoDetails = 52
    """期货账户信息变更明细对账"""
    THOST_FTDC_FBC_CustMoneyDetail = 53
    """客户资金台账余额明细对账"""
    THOST_FTDC_FBC_CustCancelAccountInfo = 54
    """客户销户结息明细对账"""
    THOST_FTDC_FBC_CustMoneyResult = 55
    """客户资金余额对账结果"""
    THOST_FTDC_FBC_OthersExceptionResult = 56
    """其它对账异常结果文件"""
    THOST_FTDC_FBC_CustInterestNetMoneyDetails = 57
    """客户结息净额明细"""
    THOST_FTDC_FBC_CustMoneySendAndReceiveDetails = 97
    """客户资金交收明细"""
    THOST_FTDC_FBC_CorporationMoneyTotal = 98
    """法人存管银行资金交收汇总"""
    THOST_FTDC_FBC_MainbodyMoneyTotal = 99
    """主体间资金交收汇总"""
    THOST_FTDC_FBC_MainPartMonitorData = 100
    """总分平衡监管数据"""
    THOST_FTDC_FBC_PreparationMoney = 101
    """存管银行备付金余额"""
    THOST_FTDC_FBC_BankMoneyMonitorData = 102
    """协办存管银行资金监管数据"""


class TThostFtdcCashExchangeCodeType(Enum):
    """汇钞标志类型"""
    THOST_FTDC_CEC_Exchange = 49
    """汇"""
    THOST_FTDC_CEC_Cash = 50
    """钞"""


class TThostFtdcYesNoIndicatorType(Enum):
    """是或否标识类型"""
    THOST_FTDC_YNI_Yes = 48
    """是"""
    THOST_FTDC_YNI_No = 49
    """否"""


class TThostFtdcBanlanceTypeType(Enum):
    """余额类型类型"""
    THOST_FTDC_BLT_CurrentMoney = 48
    """当前余额"""
    THOST_FTDC_BLT_UsableMoney = 49
    """可用余额"""
    THOST_FTDC_BLT_FetchableMoney = 50
    """可取余额"""
    THOST_FTDC_BLT_FreezeMoney = 51
    """冻结余额"""


class TThostFtdcGenderType(Enum):
    """性别类型"""
    THOST_FTDC_GD_Unknown = 48
    """未知状态"""
    THOST_FTDC_GD_Male = 49
    """男"""
    THOST_FTDC_GD_Female = 50
    """女"""


class TThostFtdcFeePayFlagType(Enum):
    """费用支付标志类型"""
    THOST_FTDC_FPF_BEN = 48
    """由受益方支付费用"""
    THOST_FTDC_FPF_OUR = 49
    """由发送方支付费用"""
    THOST_FTDC_FPF_SHA = 50
    """由发送方支付发起的费用，受益方支付接受的费用"""


class TThostFtdcPassWordKeyTypeType(Enum):
    """密钥类型类型"""
    THOST_FTDC_PWKT_ExchangeKey = 48
    """交换密钥"""
    THOST_FTDC_PWKT_PassWordKey = 49
    """密码密钥"""
    THOST_FTDC_PWKT_MACKey = 50
    """MAC密钥"""
    THOST_FTDC_PWKT_MessageKey = 51
    """报文密钥"""


class TThostFtdcFBTPassWordTypeType(Enum):
    """密码类型类型"""
    THOST_FTDC_PWT_Query = 48
    """查询"""
    THOST_FTDC_PWT_Fetch = 49
    """取款"""
    THOST_FTDC_PWT_Transfer = 50
    """转帐"""
    THOST_FTDC_PWT_Trade = 51
    """交易"""


class TThostFtdcFBTEncryModeType(Enum):
    """加密方式类型"""
    THOST_FTDC_EM_NoEncry = 48
    """不加密"""
    THOST_FTDC_EM_DES = 49
    """DES"""
    THOST_FTDC_EM_3DES = 50
    """3DES"""


class TThostFtdcBankRepealFlagType(Enum):
    """银行冲正标志类型"""
    THOST_FTDC_BRF_BankNotNeedRepeal = 48
    """银行无需自动冲正"""
    THOST_FTDC_BRF_BankWaitingRepeal = 49
    """银行待自动冲正"""
    THOST_FTDC_BRF_BankBeenRepealed = 50
    """银行已自动冲正"""


class TThostFtdcBrokerRepealFlagType(Enum):
    """期商冲正标志类型"""
    THOST_FTDC_BRORF_BrokerNotNeedRepeal = 48
    """期商无需自动冲正"""
    THOST_FTDC_BRORF_BrokerWaitingRepeal = 49
    """期商待自动冲正"""
    THOST_FTDC_BRORF_BrokerBeenRepealed = 50
    """期商已自动冲正"""


class TThostFtdcInstitutionTypeType(Enum):
    """机构类别类型"""
    THOST_FTDC_TS_Bank = 48
    """银行"""
    THOST_FTDC_TS_Future = 49
    """期商"""
    THOST_FTDC_TS_Store = 50
    """券商"""


class TThostFtdcLastFragmentType(Enum):
    """最后分片标志类型"""
    THOST_FTDC_LF_Yes = 48
    """是最后分片"""
    THOST_FTDC_LF_No = 49
    """不是最后分片"""


class TThostFtdcBankAccStatusType(Enum):
    """银行账户状态类型"""
    THOST_FTDC_BAS_Normal = 48
    """正常"""
    THOST_FTDC_BAS_Freeze = 49
    """冻结"""
    THOST_FTDC_BAS_ReportLoss = 50
    """挂失"""


class TThostFtdcMoneyAccountStatusType(Enum):
    """资金账户状态类型"""
    THOST_FTDC_MAS_Normal = 48
    """正常"""
    THOST_FTDC_MAS_Cancel = 49
    """销户"""


class TThostFtdcManageStatusType(Enum):
    """存管状态类型"""
    THOST_FTDC_MSS_Point = 48
    """指定存管"""
    THOST_FTDC_MSS_PrePoint = 49
    """预指定"""
    THOST_FTDC_MSS_CancelPoint = 50
    """撤销指定"""


class TThostFtdcSystemTypeType(Enum):
    """应用系统类型类型"""
    THOST_FTDC_SYT_FutureBankTransfer = 48
    """银期转帐"""
    THOST_FTDC_SYT_StockBankTransfer = 49
    """银证转帐"""
    THOST_FTDC_SYT_TheThirdPartStore = 50
    """第三方存管"""


class TThostFtdcTxnEndFlagType(Enum):
    """银期转帐划转结果标志类型"""
    THOST_FTDC_TEF_NormalProcessing = 48
    """正常处理中"""
    THOST_FTDC_TEF_Success = 49
    """成功结束"""
    THOST_FTDC_TEF_Failed = 50
    """失败结束"""
    THOST_FTDC_TEF_Abnormal = 51
    """异常中"""
    THOST_FTDC_TEF_ManualProcessedForException = 52
    """已人工异常处理"""
    THOST_FTDC_TEF_CommuFailedNeedManualProcess = 53
    """通讯异常 ，请人工处理"""
    THOST_FTDC_TEF_SysErrorNeedManualProcess = 54
    """系统出错，请人工处理"""


class TThostFtdcProcessStatusType(Enum):
    """银期转帐服务处理状态类型"""
    THOST_FTDC_PSS_NotProcess = 48
    """未处理"""
    THOST_FTDC_PSS_StartProcess = 49
    """开始处理"""
    THOST_FTDC_PSS_Finished = 50
    """处理完成"""


class TThostFtdcCustTypeType(Enum):
    """客户类型类型"""
    THOST_FTDC_CUSTT_Person = 48
    """自然人"""
    THOST_FTDC_CUSTT_Institution = 49
    """机构户"""


class TThostFtdcFBTTransferDirectionType(Enum):
    """银期转帐方向类型"""
    THOST_FTDC_FBTTD_FromBankToFuture = 49
    """入金，银行转期货"""
    THOST_FTDC_FBTTD_FromFutureToBank = 50
    """出金，期货转银行"""


class TThostFtdcOpenOrDestroyType(Enum):
    """开销户类别类型"""
    THOST_FTDC_OOD_Open = 49
    """开户"""
    THOST_FTDC_OOD_Destroy = 48
    """销户"""


class TThostFtdcAvailabilityFlagType(Enum):
    """有效标志类型"""
    THOST_FTDC_AVAF_Invalid = 48
    """未确认"""
    THOST_FTDC_AVAF_Valid = 49
    """有效"""
    THOST_FTDC_AVAF_Repeal = 50
    """冲正"""


class TThostFtdcOrganTypeType(Enum):
    """机构类型类型"""
    THOST_FTDC_OT_Bank = 49
    """银行代理"""
    THOST_FTDC_OT_Future = 50
    """交易前置"""
    THOST_FTDC_OT_PlateForm = 57
    """银期转帐平台管理"""


class TThostFtdcOrganLevelType(Enum):
    """机构级别类型"""
    THOST_FTDC_OL_HeadQuarters = 49
    """银行总行或期商总部"""
    THOST_FTDC_OL_Branch = 50
    """银行分中心或期货公司营业部"""


class TThostFtdcProtocalIDType(Enum):
    """协议类型类型"""
    THOST_FTDC_PID_FutureProtocal = 48
    """期商协议"""
    THOST_FTDC_PID_ICBCProtocal = 49
    """工行协议"""
    THOST_FTDC_PID_ABCProtocal = 50
    """农行协议"""
    THOST_FTDC_PID_CBCProtocal = 51
    """中国银行协议"""
    THOST_FTDC_PID_CCBProtocal = 52
    """建行协议"""
    THOST_FTDC_PID_BOCOMProtocal = 53
    """交行协议"""
    THOST_FTDC_PID_FBTPlateFormProtocal = 88
    """银期转帐平台协议"""


class TThostFtdcConnectModeType(Enum):
    """套接字连接方式类型"""
    THOST_FTDC_CM_ShortConnect = 48
    """短连接"""
    THOST_FTDC_CM_LongConnect = 49
    """长连接"""


class TThostFtdcSyncModeType(Enum):
    """套接字通信方式类型"""
    THOST_FTDC_SRM_ASync = 48
    """异步"""
    THOST_FTDC_SRM_Sync = 49
    """同步"""


class TThostFtdcBankAccTypeType(Enum):
    """银行帐号类型类型"""
    THOST_FTDC_BAT_BankBook = 49
    """银行存折"""
    THOST_FTDC_BAT_SavingCard = 50
    """储蓄卡"""
    THOST_FTDC_BAT_CreditCard = 51
    """信用卡"""


class TThostFtdcFutureAccTypeType(Enum):
    """期货公司帐号类型类型"""
    THOST_FTDC_FAT_BankBook = 49
    """银行存折"""
    THOST_FTDC_FAT_SavingCard = 50
    """储蓄卡"""
    THOST_FTDC_FAT_CreditCard = 51
    """信用卡"""


class TThostFtdcOrganStatusType(Enum):
    """接入机构状态类型"""
    THOST_FTDC_OS_Ready = 48
    """启用"""
    THOST_FTDC_OS_CheckIn = 49
    """签到"""
    THOST_FTDC_OS_CheckOut = 50
    """签退"""
    THOST_FTDC_OS_CheckFileArrived = 51
    """对帐文件到达"""
    THOST_FTDC_OS_CheckDetail = 52
    """对帐"""
    THOST_FTDC_OS_DayEndClean = 53
    """日终清理"""
    THOST_FTDC_OS_Invalid = 57
    """注销"""


class TThostFtdcCCBFeeModeType(Enum):
    """建行收费模式类型"""
    THOST_FTDC_CCBFM_ByAmount = 49
    """按金额扣收"""
    THOST_FTDC_CCBFM_ByMonth = 50
    """按月扣收"""


class TThostFtdcCommApiTypeType(Enum):
    """通讯API类型类型"""
    THOST_FTDC_CAPIT_Client = 49
    """客户端"""
    THOST_FTDC_CAPIT_Server = 50
    """服务端"""
    THOST_FTDC_CAPIT_UserApi = 51
    """交易系统的UserApi"""


class TThostFtdcLinkStatusType(Enum):
    """连接状态类型"""
    THOST_FTDC_LS_Connected = 49
    """已经连接"""
    THOST_FTDC_LS_Disconnected = 50
    """没有连接"""


class TThostFtdcPwdFlagType(Enum):
    """密码核对标志类型"""
    THOST_FTDC_BPWDF_NoCheck = 48
    """不核对"""
    THOST_FTDC_BPWDF_BlankCheck = 49
    """明文核对"""
    THOST_FTDC_BPWDF_EncryptCheck = 50
    """密文核对"""


class TThostFtdcSecuAccTypeType(Enum):
    """期货帐号类型类型"""
    THOST_FTDC_SAT_AccountID = 49
    """资金帐号"""
    THOST_FTDC_SAT_CardID = 50
    """资金卡号"""
    THOST_FTDC_SAT_SHStockholderID = 51
    """上海股东帐号"""
    THOST_FTDC_SAT_SZStockholderID = 52
    """深圳股东帐号"""


class TThostFtdcTransferStatusType(Enum):
    """转账交易状态类型"""
    THOST_FTDC_TRFS_Normal = 48
    """正常"""
    THOST_FTDC_TRFS_Repealed = 49
    """被冲正"""


class TThostFtdcSponsorTypeType(Enum):
    """发起方类型"""
    THOST_FTDC_SPTYPE_Broker = 48
    """期商"""
    THOST_FTDC_SPTYPE_Bank = 49
    """银行"""


class TThostFtdcReqRspTypeType(Enum):
    """请求响应类别类型"""
    THOST_FTDC_REQRSP_Request = 48
    """请求"""
    THOST_FTDC_REQRSP_Response = 49
    """响应"""


class TThostFtdcFBTUserEventTypeType(Enum):
    """银期转帐用户事件类型类型"""
    THOST_FTDC_FBTUET_SignIn = 48
    """签到"""
    THOST_FTDC_FBTUET_FromBankToFuture = 49
    """银行转期货"""
    THOST_FTDC_FBTUET_FromFutureToBank = 50
    """期货转银行"""
    THOST_FTDC_FBTUET_OpenAccount = 51
    """开户"""
    THOST_FTDC_FBTUET_CancelAccount = 52
    """销户"""
    THOST_FTDC_FBTUET_ChangeAccount = 53
    """变更银行账户"""
    THOST_FTDC_FBTUET_RepealFromBankToFuture = 54
    """冲正银行转期货"""
    THOST_FTDC_FBTUET_RepealFromFutureToBank = 55
    """冲正期货转银行"""
    THOST_FTDC_FBTUET_QueryBankAccount = 56
    """查询银行账户"""
    THOST_FTDC_FBTUET_QueryFutureAccount = 57
    """查询期货账户"""
    THOST_FTDC_FBTUET_SignOut = 65
    """签退"""
    THOST_FTDC_FBTUET_SyncKey = 66
    """密钥同步"""
    THOST_FTDC_FBTUET_ReserveOpenAccount = 67
    """预约开户"""
    THOST_FTDC_FBTUET_CancelReserveOpenAccount = 68
    """撤销预约开户"""
    THOST_FTDC_FBTUET_ReserveOpenAccountConfirm = 69
    """预约开户确认"""
    THOST_FTDC_FBTUET_Other = 90
    """其他"""


class TThostFtdcDBOperationType(Enum):
    """记录操作类型类型"""
    THOST_FTDC_DBOP_Insert = 48
    """插入"""
    THOST_FTDC_DBOP_Update = 49
    """更新"""
    THOST_FTDC_DBOP_Delete = 50
    """删除"""


class TThostFtdcSyncFlagType(Enum):
    """同步标记类型"""
    THOST_FTDC_SYNF_Yes = 48
    """已同步"""
    THOST_FTDC_SYNF_No = 49
    """未同步"""


class TThostFtdcSyncTypeType(Enum):
    """同步类型类型"""
    THOST_FTDC_SYNT_OneOffSync = 48
    """一次同步"""
    THOST_FTDC_SYNT_TimerSync = 49
    """定时同步"""
    THOST_FTDC_SYNT_TimerFullSync = 50
    """定时完全同步"""


class TThostFtdcExDirectionType(Enum):
    """换汇方向类型"""
    THOST_FTDC_FBEDIR_Settlement = 48
    """结汇"""
    THOST_FTDC_FBEDIR_Sale = 49
    """售汇"""


class TThostFtdcFBEResultFlagType(Enum):
    """换汇成功标志类型"""
    THOST_FTDC_FBERES_Success = 48
    """成功"""
    THOST_FTDC_FBERES_InsufficientBalance = 49
    """账户余额不足"""
    THOST_FTDC_FBERES_UnknownTrading = 56
    """交易结果未知"""
    THOST_FTDC_FBERES_Fail = 120
    """失败"""


class TThostFtdcFBEExchStatusType(Enum):
    """换汇交易状态类型"""
    THOST_FTDC_FBEES_Normal = 48
    """正常"""
    THOST_FTDC_FBEES_ReExchange = 49
    """交易重发"""


class TThostFtdcFBEFileFlagType(Enum):
    """换汇文件标志类型"""
    THOST_FTDC_FBEFG_DataPackage = 48
    """数据包"""
    THOST_FTDC_FBEFG_File = 49
    """文件"""


class TThostFtdcFBEAlreadyTradeType(Enum):
    """换汇已交易标志类型"""
    THOST_FTDC_FBEAT_NotTrade = 48
    """未交易"""
    THOST_FTDC_FBEAT_Trade = 49
    """已交易"""


class TThostFtdcFBEUserEventTypeType(Enum):
    """银期换汇用户事件类型类型"""
    THOST_FTDC_FBEUET_SignIn = 48
    """签到"""
    THOST_FTDC_FBEUET_Exchange = 49
    """换汇"""
    THOST_FTDC_FBEUET_ReExchange = 50
    """换汇重发"""
    THOST_FTDC_FBEUET_QueryBankAccount = 51
    """银行账户查询"""
    THOST_FTDC_FBEUET_QueryExchDetial = 52
    """换汇明细查询"""
    THOST_FTDC_FBEUET_QueryExchSummary = 53
    """换汇汇总查询"""
    THOST_FTDC_FBEUET_QueryExchRate = 54
    """换汇汇率查询"""
    THOST_FTDC_FBEUET_CheckBankAccount = 55
    """对账文件通知"""
    THOST_FTDC_FBEUET_SignOut = 56
    """签退"""
    THOST_FTDC_FBEUET_Other = 90
    """其他"""


class TThostFtdcFBEReqFlagType(Enum):
    """换汇发送标志类型"""
    THOST_FTDC_FBERF_UnProcessed = 48
    """未处理"""
    THOST_FTDC_FBERF_WaitSend = 49
    """等待发送"""
    THOST_FTDC_FBERF_SendSuccess = 50
    """发送成功"""
    THOST_FTDC_FBERF_SendFailed = 51
    """发送失败"""
    THOST_FTDC_FBERF_WaitReSend = 52
    """等待重发"""


class TThostFtdcNotifyClassType(Enum):
    """风险通知类型类型"""
    THOST_FTDC_NC_NOERROR = 48
    """正常"""
    THOST_FTDC_NC_Warn = 49
    """警示"""
    THOST_FTDC_NC_Call = 50
    """追保"""
    THOST_FTDC_NC_Force = 51
    """强平"""
    THOST_FTDC_NC_CHUANCANG = 52
    """穿仓"""
    THOST_FTDC_NC_Exception = 53
    """异常"""


class TThostFtdcForceCloseTypeType(Enum):
    """强平单类型类型"""
    THOST_FTDC_FCT_Manual = 48
    """手工强平"""
    THOST_FTDC_FCT_Single = 49
    """单一投资者辅助强平"""
    THOST_FTDC_FCT_Group = 50
    """批量投资者辅助强平"""


class TThostFtdcRiskNotifyMethodType(Enum):
    """风险通知途径类型"""
    THOST_FTDC_RNM_System = 48
    """系统通知"""
    THOST_FTDC_RNM_SMS = 49
    """短信通知"""
    THOST_FTDC_RNM_EMail = 50
    """邮件通知"""
    THOST_FTDC_RNM_Manual = 51
    """人工通知"""


class TThostFtdcRiskNotifyStatusType(Enum):
    """风险通知状态类型"""
    THOST_FTDC_RNS_NotGen = 48
    """未生成"""
    THOST_FTDC_RNS_Generated = 49
    """已生成未发送"""
    THOST_FTDC_RNS_SendError = 50
    """发送失败"""
    THOST_FTDC_RNS_SendOk = 51
    """已发送未接收"""
    THOST_FTDC_RNS_Received = 52
    """已接收未确认"""
    THOST_FTDC_RNS_Confirmed = 53
    """已确认"""


class TThostFtdcRiskUserEventType(Enum):
    """风控用户操作事件类型"""
    THOST_FTDC_RUE_ExportData = 48
    """导出数据"""


class TThostFtdcConditionalOrderSortTypeType(Enum):
    """条件单索引条件类型"""
    THOST_FTDC_COST_LastPriceAsc = 48
    """使用最新价升序"""
    THOST_FTDC_COST_LastPriceDesc = 49
    """使用最新价降序"""
    THOST_FTDC_COST_AskPriceAsc = 50
    """使用卖价升序"""
    THOST_FTDC_COST_AskPriceDesc = 51
    """使用卖价降序"""
    THOST_FTDC_COST_BidPriceAsc = 52
    """使用买价升序"""
    THOST_FTDC_COST_BidPriceDesc = 53
    """使用买价降序"""


class TThostFtdcSendTypeType(Enum):
    """报送状态类型"""
    THOST_FTDC_UOAST_NoSend = 48
    """未发送"""
    THOST_FTDC_UOAST_Sended = 49
    """已发送"""
    THOST_FTDC_UOAST_Generated = 50
    """已生成"""
    THOST_FTDC_UOAST_SendFail = 51
    """报送失败"""
    THOST_FTDC_UOAST_Success = 52
    """接收成功"""
    THOST_FTDC_UOAST_Fail = 53
    """接收失败"""
    THOST_FTDC_UOAST_Cancel = 54
    """取消报送"""


class TThostFtdcClientIDStatusType(Enum):
    """交易编码状态类型"""
    THOST_FTDC_UOACS_NoApply = 49
    """未申请"""
    THOST_FTDC_UOACS_Submited = 50
    """已提交申请"""
    THOST_FTDC_UOACS_Sended = 51
    """已发送申请"""
    THOST_FTDC_UOACS_Success = 52
    """完成"""
    THOST_FTDC_UOACS_Refuse = 53
    """拒绝"""
    THOST_FTDC_UOACS_Cancel = 54
    """已撤销编码"""


class TThostFtdcQuestionTypeType(Enum):
    """特有信息类型类型"""
    THOST_FTDC_QT_Radio = 49
    """单选"""
    THOST_FTDC_QT_Option = 50
    """多选"""
    THOST_FTDC_QT_Blank = 51
    """填空"""


class TThostFtdcBusinessTypeType(Enum):
    """业务类型类型"""
    THOST_FTDC_BT_Request = 49
    """请求"""
    THOST_FTDC_BT_Response = 50
    """应答"""
    THOST_FTDC_BT_Notice = 51
    """通知"""


class TThostFtdcCfmmcReturnCodeType(Enum):
    """监控中心返回码类型"""
    THOST_FTDC_CRC_Success = 48
    """成功"""
    THOST_FTDC_CRC_Working = 49
    """该客户已经有流程在处理中"""
    THOST_FTDC_CRC_InfoFail = 50
    """监控中客户资料检查失败"""
    THOST_FTDC_CRC_IDCardFail = 51
    """监控中实名制检查失败"""
    THOST_FTDC_CRC_OtherFail = 52
    """其他错误"""


class TThostFtdcClientTypeType(Enum):
    """客户类型类型"""
    THOST_FTDC_CfMMCCT_All = 48
    """所有"""
    THOST_FTDC_CfMMCCT_Person = 49
    """个人"""
    THOST_FTDC_CfMMCCT_Company = 50
    """单位"""
    THOST_FTDC_CfMMCCT_Other = 51
    """其他"""
    THOST_FTDC_CfMMCCT_SpecialOrgan = 52
    """特殊法人"""
    THOST_FTDC_CfMMCCT_Asset = 53
    """资管户"""


class TThostFtdcExchangeIDTypeType(Enum):
    """交易所编号类型"""
    THOST_FTDC_EIDT_SHFE = 83
    """上海期货交易所"""
    THOST_FTDC_EIDT_CZCE = 90
    """郑州商品交易所"""
    THOST_FTDC_EIDT_DCE = 68
    """大连商品交易所"""
    THOST_FTDC_EIDT_CFFEX = 74
    """中国金融期货交易所"""
    THOST_FTDC_EIDT_INE = 78
    """上海国际能源交易中心股份有限公司"""


class TThostFtdcExClientIDTypeType(Enum):
    """交易编码类型类型"""
    THOST_FTDC_ECIDT_Hedge = 49
    """套保"""
    THOST_FTDC_ECIDT_Arbitrage = 50
    """套利"""
    THOST_FTDC_ECIDT_Speculation = 51
    """投机"""


class TThostFtdcUpdateFlagType(Enum):
    """更新状态类型"""
    THOST_FTDC_UF_NoUpdate = 48
    """未更新"""
    THOST_FTDC_UF_Success = 49
    """更新全部信息成功"""
    THOST_FTDC_UF_Fail = 50
    """更新全部信息失败"""
    THOST_FTDC_UF_TCSuccess = 51
    """更新交易编码成功"""
    THOST_FTDC_UF_TCFail = 52
    """更新交易编码失败"""
    THOST_FTDC_UF_Cancel = 53
    """已丢弃"""


class TThostFtdcApplyOperateIDType(Enum):
    """申请动作类型"""
    THOST_FTDC_AOID_OpenInvestor = 49
    """开户"""
    THOST_FTDC_AOID_ModifyIDCard = 50
    """修改身份信息"""
    THOST_FTDC_AOID_ModifyNoIDCard = 51
    """修改一般信息"""
    THOST_FTDC_AOID_ApplyTradingCode = 52
    """申请交易编码"""
    THOST_FTDC_AOID_CancelTradingCode = 53
    """撤销交易编码"""
    THOST_FTDC_AOID_CancelInvestor = 54
    """销户"""
    THOST_FTDC_AOID_FreezeAccount = 56
    """账户休眠"""
    THOST_FTDC_AOID_ActiveFreezeAccount = 57
    """激活休眠账户"""


class TThostFtdcApplyStatusIDType(Enum):
    """申请状态类型"""
    THOST_FTDC_ASID_NoComplete = 49
    """未补全"""
    THOST_FTDC_ASID_Submited = 50
    """已提交"""
    THOST_FTDC_ASID_Checked = 51
    """已审核"""
    THOST_FTDC_ASID_Refused = 52
    """已拒绝"""
    THOST_FTDC_ASID_Deleted = 53
    """已删除"""


class TThostFtdcSendMethodType(Enum):
    """发送方式类型"""
    THOST_FTDC_UOASM_ByAPI = 49
    """文件发送"""
    THOST_FTDC_UOASM_ByFile = 50
    """电子发送"""


class TThostFtdcEventModeType(Enum):
    """操作方法类型"""
    THOST_FTDC_EvM_ADD = 49
    """增加"""
    THOST_FTDC_EvM_UPDATE = 50
    """修改"""
    THOST_FTDC_EvM_DELETE = 51
    """删除"""
    THOST_FTDC_EvM_CHECK = 52
    """复核"""
    THOST_FTDC_EvM_COPY = 53
    """复制"""
    THOST_FTDC_EvM_CANCEL = 54
    """注销"""
    THOST_FTDC_EvM_Reverse = 55
    """冲销"""


class TThostFtdcUOAAutoSendType(Enum):
    """统一开户申请自动发送类型"""
    THOST_FTDC_UOAA_ASR = 49
    """自动发送并接收"""
    THOST_FTDC_UOAA_ASNR = 50
    """自动发送，不自动接收"""
    THOST_FTDC_UOAA_NSAR = 51
    """不自动发送，自动接收"""
    THOST_FTDC_UOAA_NSR = 52
    """不自动发送，也不自动接收"""


class TThostFtdcFlowIDType(Enum):
    """流程ID类型"""
    THOST_FTDC_EvM_InvestorGroupFlow = 49
    """投资者对应投资者组设置"""
    THOST_FTDC_EvM_InvestorRate = 50
    """投资者手续费率设置"""
    THOST_FTDC_EvM_InvestorCommRateModel = 51
    """投资者手续费率模板关系设置"""


class TThostFtdcCheckLevelType(Enum):
    """复核级别类型"""
    THOST_FTDC_CL_Zero = 48
    """零级复核"""
    THOST_FTDC_CL_One = 49
    """一级复核"""
    THOST_FTDC_CL_Two = 50
    """二级复核"""


class TThostFtdcCheckStatusType(Enum):
    """复核级别类型"""
    THOST_FTDC_CHS_Init = 48
    """未复核"""
    THOST_FTDC_CHS_Checking = 49
    """复核中"""
    THOST_FTDC_CHS_Checked = 50
    """已复核"""
    THOST_FTDC_CHS_Refuse = 51
    """拒绝"""
    THOST_FTDC_CHS_Cancel = 52
    """作废"""


class TThostFtdcUsedStatusType(Enum):
    """生效状态类型"""
    THOST_FTDC_CHU_Unused = 48
    """未生效"""
    THOST_FTDC_CHU_Used = 49
    """已生效"""
    THOST_FTDC_CHU_Fail = 50
    """生效失败"""


class TThostFtdcBankAcountOriginType(Enum):
    """账户来源类型"""
    THOST_FTDC_BAO_ByAccProperty = 48
    """手工录入"""
    THOST_FTDC_BAO_ByFBTransfer = 49
    """银期转账"""


class TThostFtdcMonthBillTradeSumType(Enum):
    """结算单月报成交汇总方式类型"""
    THOST_FTDC_MBTS_ByInstrument = 48
    """同日同合约"""
    THOST_FTDC_MBTS_ByDayInsPrc = 49
    """同日同合约同价格"""
    THOST_FTDC_MBTS_ByDayIns = 50
    """同合约"""


class TThostFtdcFBTTradeCodeEnumType(Enum):
    """银期交易代码枚举类型"""
    THOST_FTDC_FTC_BankLaunchBankToBroker = 49
    """银行发起银行转期货"""
    THOST_FTDC_FTC_BrokerLaunchBankToBroker = 49
    """期货发起银行转期货"""
    THOST_FTDC_FTC_BankLaunchBrokerToBank = 50
    """银行发起期货转银行"""
    THOST_FTDC_FTC_BrokerLaunchBrokerToBank = 50
    """期货发起期货转银行"""


class TThostFtdcOTPTypeType(Enum):
    """动态令牌类型类型"""
    THOST_FTDC_OTP_NONE = 48
    """无动态令牌"""
    THOST_FTDC_OTP_TOTP = 49
    """时间令牌"""


class TThostFtdcOTPStatusType(Enum):
    """动态令牌状态类型"""
    THOST_FTDC_OTPS_Unused = 48
    """未使用"""
    THOST_FTDC_OTPS_Used = 49
    """已使用"""
    THOST_FTDC_OTPS_Disuse = 50
    """注销"""


class TThostFtdcBrokerUserTypeType(Enum):
    """经济公司用户类型类型"""
    THOST_FTDC_BUT_Investor = 49
    """投资者"""
    THOST_FTDC_BUT_BrokerUser = 50
    """操作员"""


class TThostFtdcFutureTypeType(Enum):
    """期货类型类型"""
    THOST_FTDC_FUTT_Commodity = 49
    """商品期货"""
    THOST_FTDC_FUTT_Financial = 50
    """金融期货"""


class TThostFtdcFundEventTypeType(Enum):
    """资金管理操作类型类型"""
    THOST_FTDC_FET_Restriction = 48
    """转账限额"""
    THOST_FTDC_FET_TodayRestriction = 49
    """当日转账限额"""
    THOST_FTDC_FET_Transfer = 50
    """期商流水"""
    THOST_FTDC_FET_Credit = 51
    """资金冻结"""
    THOST_FTDC_FET_InvestorWithdrawAlm = 52
    """投资者可提资金比例"""
    THOST_FTDC_FET_BankRestriction = 53
    """单个银行帐户转账限额"""
    THOST_FTDC_FET_Accountregister = 54
    """银期签约账户"""
    THOST_FTDC_FET_ExchangeFundIO = 55
    """交易所出入金"""
    THOST_FTDC_FET_InvestorFundIO = 56
    """投资者出入金"""


class TThostFtdcAccountSourceTypeType(Enum):
    """资金账户来源类型"""
    THOST_FTDC_AST_FBTransfer = 48
    """银期同步"""
    THOST_FTDC_AST_ManualEntry = 49
    """手工录入"""


class TThostFtdcCodeSourceTypeType(Enum):
    """交易编码来源类型"""
    THOST_FTDC_CST_UnifyAccount = 48
    """统一开户(已规范)"""
    THOST_FTDC_CST_ManualEntry = 49
    """手工录入(未规范)"""


class TThostFtdcUserRangeType(Enum):
    """操作员范围类型"""
    THOST_FTDC_UR_All = 48
    """所有"""
    THOST_FTDC_UR_Single = 49
    """单一操作员"""


class TThostFtdcByGroupType(Enum):
    """交易统计表按客户统计方式类型"""
    THOST_FTDC_BG_Investor = 50
    """按投资者统计"""
    THOST_FTDC_BG_Group = 49
    """按类统计"""


class TThostFtdcTradeSumStatModeType(Enum):
    """交易统计表按范围统计方式类型"""
    THOST_FTDC_TSSM_Instrument = 49
    """按合约统计"""
    THOST_FTDC_TSSM_Product = 50
    """按产品统计"""
    THOST_FTDC_TSSM_Exchange = 51
    """按交易所统计"""


class TThostFtdcExprSetModeType(Enum):
    """日期表达式设置类型类型"""
    THOST_FTDC_ESM_Relative = 49
    """相对已有规则设置"""
    THOST_FTDC_ESM_Typical = 50
    """典型设置"""


class TThostFtdcRateInvestorRangeType(Enum):
    """投资者范围类型"""
    THOST_FTDC_RIR_All = 49
    """公司标准"""
    THOST_FTDC_RIR_Model = 50
    """模板"""
    THOST_FTDC_RIR_Single = 51
    """单一投资者"""


class TThostFtdcSyncDataStatusType(Enum):
    """主次用系统数据同步状态类型"""
    THOST_FTDC_SDS_Initialize = 48
    """未同步"""
    THOST_FTDC_SDS_Settlementing = 49
    """同步中"""
    THOST_FTDC_SDS_Settlemented = 50
    """已同步"""


class TThostFtdcTradeSourceType(Enum):
    """成交来源类型"""
    THOST_FTDC_TSRC_NORMAL = 48
    """来自交易所普通回报"""
    THOST_FTDC_TSRC_QUERY = 49
    """来自查询"""


class TThostFtdcFlexStatModeType(Enum):
    """产品合约统计方式类型"""
    THOST_FTDC_FSM_Product = 49
    """产品统计"""
    THOST_FTDC_FSM_Exchange = 50
    """交易所统计"""
    THOST_FTDC_FSM_All = 51
    """统计所有"""


class TThostFtdcByInvestorRangeType(Enum):
    """投资者范围统计方式类型"""
    THOST_FTDC_BIR_Property = 49
    """属性统计"""
    THOST_FTDC_BIR_All = 50
    """统计所有"""


class TThostFtdcPropertyInvestorRangeType(Enum):
    """投资者范围类型"""
    THOST_FTDC_PIR_All = 49
    """所有"""
    THOST_FTDC_PIR_Property = 50
    """投资者属性"""
    THOST_FTDC_PIR_Single = 51
    """单一投资者"""


class TThostFtdcFileStatusType(Enum):
    """文件状态类型"""
    THOST_FTDC_FIS_NoCreate = 48
    """未生成"""
    THOST_FTDC_FIS_Created = 49
    """已生成"""
    THOST_FTDC_FIS_Failed = 50
    """生成失败"""


class TThostFtdcFileGenStyleType(Enum):
    """文件生成方式类型"""
    THOST_FTDC_FGS_FileTransmit = 48
    """下发"""
    THOST_FTDC_FGS_FileGen = 49
    """生成"""


class TThostFtdcSysOperModeType(Enum):
    """系统日志操作方法类型"""
    THOST_FTDC_SoM_Add = 49
    """增加"""
    THOST_FTDC_SoM_Update = 50
    """修改"""
    THOST_FTDC_SoM_Delete = 51
    """删除"""
    THOST_FTDC_SoM_Copy = 52
    """复制"""
    THOST_FTDC_SoM_AcTive = 53
    """激活"""
    THOST_FTDC_SoM_CanCel = 54
    """注销"""
    THOST_FTDC_SoM_ReSet = 55
    """重置"""


class TThostFtdcSysOperTypeType(Enum):
    """系统日志操作类型类型"""
    THOST_FTDC_SoT_UpdatePassword = 48
    """修改操作员密码"""
    THOST_FTDC_SoT_UserDepartment = 49
    """操作员组织架构关系"""
    THOST_FTDC_SoT_RoleManager = 50
    """角色管理"""
    THOST_FTDC_SoT_RoleFunction = 51
    """角色功能设置"""
    THOST_FTDC_SoT_BaseParam = 52
    """基础参数设置"""
    THOST_FTDC_SoT_SetUserID = 53
    """设置操作员"""
    THOST_FTDC_SoT_SetUserRole = 54
    """用户角色设置"""
    THOST_FTDC_SoT_UserIpRestriction = 55
    """用户IP限制"""
    THOST_FTDC_SoT_DepartmentManager = 56
    """组织架构管理"""
    THOST_FTDC_SoT_DepartmentCopy = 57
    """组织架构向查询分类复制"""
    THOST_FTDC_SoT_Tradingcode = 65
    """交易编码管理"""
    THOST_FTDC_SoT_InvestorStatus = 66
    """投资者状态维护"""
    THOST_FTDC_SoT_InvestorAuthority = 67
    """投资者权限管理"""
    THOST_FTDC_SoT_PropertySet = 68
    """属性设置"""
    THOST_FTDC_SoT_ReSetInvestorPasswd = 69
    """重置投资者密码"""
    THOST_FTDC_SoT_InvestorPersonalityInfo = 70
    """投资者个性信息维护"""


class TThostFtdcCSRCDataQueyTypeType(Enum):
    """上报数据查询类型类型"""
    THOST_FTDC_CSRCQ_Current = 48
    """查询当前交易日报送的数据"""
    THOST_FTDC_CSRCQ_History = 49
    """查询历史报送的代理经纪公司的数据"""


class TThostFtdcFreezeStatusType(Enum):
    """休眠状态类型"""
    THOST_FTDC_FRS_Normal = 49
    """活跃"""
    THOST_FTDC_FRS_Freeze = 48
    """休眠"""


class TThostFtdcStandardStatusType(Enum):
    """规范状态类型"""
    THOST_FTDC_STST_Standard = 48
    """已规范"""
    THOST_FTDC_STST_NonStandard = 49
    """未规范"""


class TThostFtdcRightParamTypeType(Enum):
    """配置类型类型"""
    THOST_FTDC_RPT_Freeze = 49
    """休眠户"""
    THOST_FTDC_RPT_FreezeActive = 50
    """激活休眠户"""
    THOST_FTDC_RPT_OpenLimit = 51
    """开仓权限限制"""
    THOST_FTDC_RPT_RelieveOpenLimit = 52
    """解除开仓权限限制"""


class TThostFtdcDataStatusType(Enum):
    """反洗钱审核表数据状态类型"""
    THOST_FTDC_AMLDS_Normal = 48
    """正常"""
    THOST_FTDC_AMLDS_Deleted = 49
    """已删除"""


class TThostFtdcAMLCheckStatusType(Enum):
    """审核状态类型"""
    THOST_FTDC_AMLCHS_Init = 48
    """未复核"""
    THOST_FTDC_AMLCHS_Checking = 49
    """复核中"""
    THOST_FTDC_AMLCHS_Checked = 50
    """已复核"""
    THOST_FTDC_AMLCHS_RefuseReport = 51
    """拒绝上报"""


class TThostFtdcAmlDateTypeType(Enum):
    """日期类型类型"""
    THOST_FTDC_AMLDT_DrawDay = 48
    """检查日期"""
    THOST_FTDC_AMLDT_TouchDay = 49
    """发生日期"""


class TThostFtdcAmlCheckLevelType(Enum):
    """审核级别类型"""
    THOST_FTDC_AMLCL_CheckLevel0 = 48
    """零级审核"""
    THOST_FTDC_AMLCL_CheckLevel1 = 49
    """一级审核"""
    THOST_FTDC_AMLCL_CheckLevel2 = 50
    """二级审核"""
    THOST_FTDC_AMLCL_CheckLevel3 = 51
    """三级审核"""


class TThostFtdcExportFileTypeType(Enum):
    """导出文件类型类型"""
    THOST_FTDC_EFT_CSV = 48
    """CSV"""
    THOST_FTDC_EFT_EXCEL = 49
    """Excel"""
    THOST_FTDC_EFT_DBF = 50
    """DBF"""


class TThostFtdcSettleManagerTypeType(Enum):
    """结算配置类型类型"""
    THOST_FTDC_SMT_Before = 49
    """结算前准备"""
    THOST_FTDC_SMT_Settlement = 50
    """结算"""
    THOST_FTDC_SMT_After = 51
    """结算后核对"""
    THOST_FTDC_SMT_Settlemented = 52
    """结算后处理"""


class TThostFtdcSettleManagerLevelType(Enum):
    """结算配置等级类型"""
    THOST_FTDC_SML_Must = 49
    """必要"""
    THOST_FTDC_SML_Alarm = 50
    """警告"""
    THOST_FTDC_SML_Prompt = 51
    """提示"""
    THOST_FTDC_SML_Ignore = 52
    """不检查"""


class TThostFtdcSettleManagerGroupType(Enum):
    """模块分组类型"""
    THOST_FTDC_SMG_Exhcange = 49
    """交易所核对"""
    THOST_FTDC_SMG_ASP = 50
    """内部核对"""
    THOST_FTDC_SMG_CSRC = 51
    """上报数据核对"""


class TThostFtdcLimitUseTypeType(Enum):
    """保值额度使用类型类型"""
    THOST_FTDC_LUT_Repeatable = 49
    """可重复使用"""
    THOST_FTDC_LUT_Unrepeatable = 50
    """不可重复使用"""


class TThostFtdcDataResourceType(Enum):
    """数据来源类型"""
    THOST_FTDC_DAR_Settle = 49
    """本系统"""
    THOST_FTDC_DAR_Exchange = 50
    """交易所"""
    THOST_FTDC_DAR_CSRC = 51
    """报送数据"""


class TThostFtdcMarginTypeType(Enum):
    """保证金类型类型"""
    THOST_FTDC_MGT_ExchMarginRate = 48
    """交易所保证金率"""
    THOST_FTDC_MGT_InstrMarginRate = 49
    """投资者保证金率"""
    THOST_FTDC_MGT_InstrMarginRateTrade = 50
    """投资者交易保证金率"""


class TThostFtdcActiveTypeType(Enum):
    """生效类型类型"""
    THOST_FTDC_ACT_Intraday = 49
    """仅当日生效"""
    THOST_FTDC_ACT_Long = 50
    """长期生效"""


class TThostFtdcMarginRateTypeType(Enum):
    """冲突保证金率类型类型"""
    THOST_FTDC_MRT_Exchange = 49
    """交易所保证金率"""
    THOST_FTDC_MRT_Investor = 50
    """投资者保证金率"""
    THOST_FTDC_MRT_InvestorTrade = 51
    """投资者交易保证金率"""


class TThostFtdcBackUpStatusType(Enum):
    """备份数据状态类型"""
    THOST_FTDC_BUS_UnBak = 48
    """未生成备份数据"""
    THOST_FTDC_BUS_BakUp = 49
    """备份数据生成中"""
    THOST_FTDC_BUS_BakUped = 50
    """已生成备份数据"""
    THOST_FTDC_BUS_BakFail = 51
    """备份数据失败"""


class TThostFtdcInitSettlementType(Enum):
    """结算初始化状态类型"""
    THOST_FTDC_SIS_UnInitialize = 48
    """结算初始化未开始"""
    THOST_FTDC_SIS_Initialize = 49
    """结算初始化中"""
    THOST_FTDC_SIS_Initialized = 50
    """结算初始化完成"""


class TThostFtdcReportStatusType(Enum):
    """报表数据生成状态类型"""
    THOST_FTDC_SRS_NoCreate = 48
    """未生成报表数据"""
    THOST_FTDC_SRS_Create = 49
    """报表数据生成中"""
    THOST_FTDC_SRS_Created = 50
    """已生成报表数据"""
    THOST_FTDC_SRS_CreateFail = 51
    """生成报表数据失败"""


class TThostFtdcSaveStatusType(Enum):
    """数据归档状态类型"""
    THOST_FTDC_SSS_UnSaveData = 48
    """归档未完成"""
    THOST_FTDC_SSS_SaveDatad = 49
    """归档完成"""


class TThostFtdcSettArchiveStatusType(Enum):
    """结算确认数据归档状态类型"""
    THOST_FTDC_SAS_UnArchived = 48
    """未归档数据"""
    THOST_FTDC_SAS_Archiving = 49
    """数据归档中"""
    THOST_FTDC_SAS_Archived = 50
    """已归档数据"""
    THOST_FTDC_SAS_ArchiveFail = 51
    """归档数据失败"""


class TThostFtdcCTPTypeType(Enum):
    """CTP交易系统类型类型"""
    THOST_FTDC_CTPT_Unkown = 48
    """未知类型"""
    THOST_FTDC_CTPT_MainCenter = 49
    """主中心"""
    THOST_FTDC_CTPT_BackUp = 50
    """备中心"""


class TThostFtdcCloseDealTypeType(Enum):
    """平仓处理类型类型"""
    THOST_FTDC_CDT_Normal = 48
    """正常"""
    THOST_FTDC_CDT_SpecFirst = 49
    """投机平仓优先"""


class TThostFtdcMortgageFundUseRangeType(Enum):
    """货币质押资金可用范围类型"""
    THOST_FTDC_MFUR_None = 48
    """不能使用"""
    THOST_FTDC_MFUR_Margin = 49
    """用于保证金"""
    THOST_FTDC_MFUR_All = 50
    """用于手续费、盈亏、保证金"""
    THOST_FTDC_MFUR_CNY3 = 51
    """人民币方案3"""


class TThostFtdcSpecProductTypeType(Enum):
    """特殊产品类型类型"""
    THOST_FTDC_SPT_CzceHedge = 49
    """郑商所套保产品"""
    THOST_FTDC_SPT_IneForeignCurrency = 50
    """货币质押产品"""
    THOST_FTDC_SPT_DceOpenClose = 51
    """大连短线开平仓产品"""


class TThostFtdcFundMortgageTypeType(Enum):
    """货币质押类型类型"""
    THOST_FTDC_FMT_Mortgage = 49
    """质押"""
    THOST_FTDC_FMT_Redemption = 50
    """解质"""


class TThostFtdcAccountSettlementParamIDType(Enum):
    """投资者账户结算参数代码类型"""
    THOST_FTDC_ASPI_BaseMargin = 49
    """基础保证金"""
    THOST_FTDC_ASPI_LowestInterest = 50
    """最低权益标准"""


class TThostFtdcFundMortDirectionType(Enum):
    """货币质押方向类型"""
    THOST_FTDC_FMD_In = 49
    """货币质入"""
    THOST_FTDC_FMD_Out = 50
    """货币质出"""


class TThostFtdcBusinessClassType(Enum):
    """换汇类别类型"""
    THOST_FTDC_BT_Profit = 48
    """盈利"""
    THOST_FTDC_BT_Loss = 49
    """亏损"""
    THOST_FTDC_BT_Other = 90
    """其他"""


class TThostFtdcSwapSourceTypeType(Enum):
    """换汇数据来源类型"""
    THOST_FTDC_SST_Manual = 48
    """手工"""
    THOST_FTDC_SST_Automatic = 49
    """自动生成"""


class TThostFtdcCurrExDirectionType(Enum):
    """换汇类型类型"""
    THOST_FTDC_CED_Settlement = 48
    """结汇"""
    THOST_FTDC_CED_Sale = 49
    """售汇"""


class TThostFtdcCurrencySwapStatusType(Enum):
    """申请状态类型"""
    THOST_FTDC_CSS_Entry = 49
    """已录入"""
    THOST_FTDC_CSS_Approve = 50
    """已审核"""
    THOST_FTDC_CSS_Refuse = 51
    """已拒绝"""
    THOST_FTDC_CSS_Revoke = 52
    """已撤销"""
    THOST_FTDC_CSS_Send = 53
    """已发送"""
    THOST_FTDC_CSS_Success = 54
    """换汇成功"""
    THOST_FTDC_CSS_Failure = 55
    """换汇失败"""


class TThostFtdcReqFlagType(Enum):
    """换汇发送标志类型"""
    THOST_FTDC_REQF_NoSend = 48
    """未发送"""
    THOST_FTDC_REQF_SendSuccess = 49
    """发送成功"""
    THOST_FTDC_REQF_SendFailed = 50
    """发送失败"""
    THOST_FTDC_REQF_WaitReSend = 51
    """等待重发"""


class TThostFtdcResFlagType(Enum):
    """换汇返回成功标志类型"""
    THOST_FTDC_RESF_Success = 48
    """成功"""
    THOST_FTDC_RESF_InsuffiCient = 49
    """账户余额不足"""
    THOST_FTDC_RESF_UnKnown = 56
    """交易结果未知"""


class TThostFtdcExStatusType(Enum):
    """修改状态类型"""
    THOST_FTDC_EXS_Before = 48
    """修改前"""
    THOST_FTDC_EXS_After = 49
    """修改后"""


class TThostFtdcClientRegionType(Enum):
    """开户客户地域类型"""
    THOST_FTDC_CR_Domestic = 49
    """国内客户"""
    THOST_FTDC_CR_GMT = 50
    """港澳台客户"""
    THOST_FTDC_CR_Foreign = 51
    """国外客户"""


class TThostFtdcHasBoardType(Enum):
    """是否有董事会类型"""
    THOST_FTDC_HB_No = 48
    """没有"""
    THOST_FTDC_HB_Yes = 49
    """有"""


class TThostFtdcStartModeType(Enum):
    """启动模式类型"""
    THOST_FTDC_SM_Normal = 49
    """正常"""
    THOST_FTDC_SM_Emerge = 50
    """应急"""
    THOST_FTDC_SM_Restore = 51
    """恢复"""


class TThostFtdcTemplateTypeType(Enum):
    """模型类型类型"""
    THOST_FTDC_TPT_Full = 49
    """全量"""
    THOST_FTDC_TPT_Increment = 50
    """增量"""
    THOST_FTDC_TPT_BackUp = 51
    """备份"""


class TThostFtdcLoginModeType(Enum):
    """登录模式类型"""
    THOST_FTDC_LM_Trade = 48
    """交易"""
    THOST_FTDC_LM_Transfer = 49
    """转账"""


class TThostFtdcPromptTypeType(Enum):
    """日历提示类型类型"""
    THOST_FTDC_CPT_Instrument = 49
    """合约上下市"""
    THOST_FTDC_CPT_Margin = 50
    """保证金分段生效"""


class TThostFtdcHasTrusteeType(Enum):
    """是否有托管人类型"""
    THOST_FTDC_HT_Yes = 49
    """有"""
    THOST_FTDC_HT_No = 48
    """没有"""


class TThostFtdcAmTypeType(Enum):
    """机构类型类型"""
    THOST_FTDC_AMT_Bank = 49
    """银行"""
    THOST_FTDC_AMT_Securities = 50
    """证券公司"""
    THOST_FTDC_AMT_Fund = 51
    """基金公司"""
    THOST_FTDC_AMT_Insurance = 52
    """保险公司"""
    THOST_FTDC_AMT_Trust = 53
    """信托公司"""
    THOST_FTDC_AMT_Other = 57
    """其他"""


class TThostFtdcCSRCFundIOTypeType(Enum):
    """出入金类型类型"""
    THOST_FTDC_CFIOT_FundIO = 48
    """出入金"""
    THOST_FTDC_CFIOT_SwapCurrency = 49
    """银期换汇"""


class TThostFtdcCusAccountTypeType(Enum):
    """结算账户类型类型"""
    THOST_FTDC_CAT_Futures = 49
    """期货结算账户"""
    THOST_FTDC_CAT_AssetmgrFuture = 50
    """纯期货资管业务下的资管结算账户"""
    THOST_FTDC_CAT_AssetmgrTrustee = 51
    """综合类资管业务下的期货资管托管账户"""
    THOST_FTDC_CAT_AssetmgrTransfer = 52
    """综合类资管业务下的资金中转账户"""


class TThostFtdcLanguageTypeType(Enum):
    """通知语言类型类型"""
    THOST_FTDC_LT_Chinese = 49
    """中文"""
    THOST_FTDC_LT_English = 50
    """英文"""


class TThostFtdcAssetmgrClientTypeType(Enum):
    """资产管理客户类型类型"""
    THOST_FTDC_AMCT_Person = 49
    """个人资管客户"""
    THOST_FTDC_AMCT_Organ = 50
    """单位资管客户"""
    THOST_FTDC_AMCT_SpecialOrgan = 52
    """特殊单位资管客户"""


class TThostFtdcAssetmgrTypeType(Enum):
    """投资类型类型"""
    THOST_FTDC_ASST_Futures = 51
    """期货类"""
    THOST_FTDC_ASST_SpecialOrgan = 52
    """综合类"""


class TThostFtdcCheckInstrTypeType(Enum):
    """合约比较类型类型"""
    THOST_FTDC_CIT_HasExch = 48
    """合约交易所不存在"""
    THOST_FTDC_CIT_HasATP = 49
    """合约本系统不存在"""
    THOST_FTDC_CIT_HasDiff = 50
    """合约比较不一致"""


class TThostFtdcDeliveryTypeType(Enum):
    """交割类型类型"""
    THOST_FTDC_DT_HandDeliv = 49
    """手工交割"""
    THOST_FTDC_DT_PersonDeliv = 50
    """到期交割"""


class TThostFtdcMaxMarginSideAlgorithmType(Enum):
    """大额单边保证金算法类型"""
    THOST_FTDC_MMSA_NO = 48
    """不使用大额单边保证金算法"""
    THOST_FTDC_MMSA_YES = 49
    """使用大额单边保证金算法"""


class TThostFtdcDAClientTypeType(Enum):
    """资产管理客户类型类型"""
    THOST_FTDC_CACT_Person = 48
    """自然人"""
    THOST_FTDC_CACT_Company = 49
    """法人"""
    THOST_FTDC_CACT_Other = 50
    """其他"""


class TThostFtdcUOAAssetmgrTypeType(Enum):
    """投资类型类型"""
    THOST_FTDC_UOAAT_Futures = 49
    """期货类"""
    THOST_FTDC_UOAAT_SpecialOrgan = 50
    """综合类"""


class TThostFtdcDirectionEnType(Enum):
    """买卖方向类型"""
    THOST_FTDC_DEN_Buy = 48
    """Buy"""
    THOST_FTDC_DEN_Sell = 49
    """Sell"""


class TThostFtdcOffsetFlagEnType(Enum):
    """开平标志类型"""
    THOST_FTDC_OFEN_Open = 48
    """Position Opening"""
    THOST_FTDC_OFEN_Close = 49
    """Position Close"""
    THOST_FTDC_OFEN_ForceClose = 50
    """Forced Liquidation"""
    THOST_FTDC_OFEN_CloseToday = 51
    """Close Today"""
    THOST_FTDC_OFEN_CloseYesterday = 52
    """Close Prev."""
    THOST_FTDC_OFEN_ForceOff = 53
    """Forced Reduction"""
    THOST_FTDC_OFEN_LocalForceClose = 54
    """Local Forced Liquidation"""


class TThostFtdcHedgeFlagEnType(Enum):
    """投机套保标志类型"""
    THOST_FTDC_HFEN_Speculation = 49
    """Speculation"""
    THOST_FTDC_HFEN_Arbitrage = 50
    """Arbitrage"""
    THOST_FTDC_HFEN_Hedge = 51
    """Hedge"""


class TThostFtdcFundIOTypeEnType(Enum):
    """出入金类型类型"""
    THOST_FTDC_FIOTEN_FundIO = 49
    """Deposit/Withdrawal"""
    THOST_FTDC_FIOTEN_Transfer = 50
    """Bank-Futures Transfer"""
    THOST_FTDC_FIOTEN_SwapCurrency = 51
    """Bank-Futures FX Exchange"""


class TThostFtdcFundTypeEnType(Enum):
    """资金类型类型"""
    THOST_FTDC_FTEN_Deposite = 49
    """Bank Deposit"""
    THOST_FTDC_FTEN_ItemFund = 50
    """Payment/Fee"""
    THOST_FTDC_FTEN_Company = 51
    """Brokerage Adj"""
    THOST_FTDC_FTEN_InnerTransfer = 52
    """Internal Transfer"""


class TThostFtdcFundDirectionEnType(Enum):
    """出入金方向类型"""
    THOST_FTDC_FDEN_In = 49
    """Deposit"""
    THOST_FTDC_FDEN_Out = 50
    """Withdrawal"""


class TThostFtdcFundMortDirectionEnType(Enum):
    """货币质押方向类型"""
    THOST_FTDC_FMDEN_In = 49
    """Pledge"""
    THOST_FTDC_FMDEN_Out = 50
    """Redemption"""


class TThostFtdcOptionsTypeType(Enum):
    """期权类型类型"""
    THOST_FTDC_CP_CallOptions = 49
    """看涨"""
    THOST_FTDC_CP_PutOptions = 50
    """看跌"""


class TThostFtdcStrikeModeType(Enum):
    """执行方式类型"""
    THOST_FTDC_STM_Continental = 48
    """欧式"""
    THOST_FTDC_STM_American = 49
    """美式"""
    THOST_FTDC_STM_Bermuda = 50
    """百慕大"""


class TThostFtdcStrikeTypeType(Enum):
    """执行类型类型"""
    THOST_FTDC_STT_Hedge = 48
    """自身对冲"""
    THOST_FTDC_STT_Match = 49
    """匹配执行"""


class TThostFtdcApplyTypeType(Enum):
    """中金所期权放弃执行申请类型类型"""
    THOST_FTDC_APPT_NotStrikeNum = 52
    """不执行数量"""


class TThostFtdcGiveUpDataSourceType(Enum):
    """放弃执行申请数据来源类型"""
    THOST_FTDC_GUDS_Gen = 48
    """系统生成"""
    THOST_FTDC_GUDS_Hand = 49
    """手工添加"""


class TThostFtdcExecResultType(Enum):
    """执行结果类型"""
    THOST_FTDC_OER_NoExec = 110
    """没有执行"""
    THOST_FTDC_OER_Canceled = 99
    """已经取消"""
    THOST_FTDC_OER_OK = 48
    """执行成功"""
    THOST_FTDC_OER_NoPosition = 49
    """期权持仓不够"""
    THOST_FTDC_OER_NoDeposit = 50
    """资金不够"""
    THOST_FTDC_OER_NoParticipant = 51
    """会员不存在"""
    THOST_FTDC_OER_NoClient = 52
    """客户不存在"""
    THOST_FTDC_OER_NoInstrument = 54
    """合约不存在"""
    THOST_FTDC_OER_NoRight = 55
    """没有执行权限"""
    THOST_FTDC_OER_InvalidVolume = 56
    """不合理的数量"""
    THOST_FTDC_OER_NoEnoughHistoryTrade = 57
    """没有足够的历史成交"""
    THOST_FTDC_OER_Unknown = 97
    """未知"""


class TThostFtdcCombinationTypeType(Enum):
    """组合类型类型"""
    THOST_FTDC_COMBT_Future = 48
    """期货组合"""
    THOST_FTDC_COMBT_BUL = 49
    """垂直价差BUL"""
    THOST_FTDC_COMBT_BER = 50
    """垂直价差BER"""
    THOST_FTDC_COMBT_STD = 51
    """跨式组合"""
    THOST_FTDC_COMBT_STG = 52
    """宽跨式组合"""
    THOST_FTDC_COMBT_PRT = 53
    """备兑组合"""
    THOST_FTDC_COMBT_CAS = 54
    """时间价差组合"""
    THOST_FTDC_COMBT_OPL = 55
    """期权对锁组合"""
    THOST_FTDC_COMBT_BFO = 56
    """买备兑组合"""
    THOST_FTDC_COMBT_BLS = 57
    """买入期权垂直价差组合"""
    THOST_FTDC_COMBT_BES = 97
    """卖出期权垂直价差组合"""


class TThostFtdcDceCombinationTypeType(Enum):
    """组合类型类型"""
    THOST_FTDC_DCECOMBT_SPL = 48
    """期货对锁组合"""
    THOST_FTDC_DCECOMBT_OPL = 49
    """期权对锁组合"""
    THOST_FTDC_DCECOMBT_SP = 50
    """期货跨期组合"""
    THOST_FTDC_DCECOMBT_SPC = 51
    """期货跨品种组合"""
    THOST_FTDC_DCECOMBT_BLS = 52
    """买入期权垂直价差组合"""
    THOST_FTDC_DCECOMBT_BES = 53
    """卖出期权垂直价差组合"""
    THOST_FTDC_DCECOMBT_CAS = 54
    """期权日历价差组合"""
    THOST_FTDC_DCECOMBT_STD = 55
    """期权跨式组合"""
    THOST_FTDC_DCECOMBT_STG = 56
    """期权宽跨式组合"""
    THOST_FTDC_DCECOMBT_BFO = 57
    """买入期货期权组合"""
    THOST_FTDC_DCECOMBT_SFO = 97
    """卖出期货期权组合"""


class TThostFtdcOptionRoyaltyPriceTypeType(Enum):
    """期权权利金价格类型类型"""
    THOST_FTDC_ORPT_PreSettlementPrice = 49
    """昨结算价"""
    THOST_FTDC_ORPT_OpenPrice = 52
    """开仓价"""
    THOST_FTDC_ORPT_MaxPreSettlementPrice = 53
    """最新价与昨结算价较大值"""


class TThostFtdcBalanceAlgorithmType(Enum):
    """权益算法类型"""
    THOST_FTDC_BLAG_Default = 49
    """不计算期权市值盈亏"""
    THOST_FTDC_BLAG_IncludeOptValLost = 50
    """计算期权市值亏损"""


class TThostFtdcActionTypeType(Enum):
    """执行类型类型"""
    THOST_FTDC_ACTP_Exec = 49
    """执行"""
    THOST_FTDC_ACTP_Abandon = 50
    """放弃"""


class TThostFtdcForQuoteStatusType(Enum):
    """询价状态类型"""
    THOST_FTDC_FQST_Submitted = 97
    """已经提交"""
    THOST_FTDC_FQST_Accepted = 98
    """已经接受"""
    THOST_FTDC_FQST_Rejected = 99
    """已经被拒绝"""


class TThostFtdcValueMethodType(Enum):
    """取值方式类型"""
    THOST_FTDC_VM_Absolute = 48
    """按绝对值"""
    THOST_FTDC_VM_Ratio = 49
    """按比率"""


class TThostFtdcExecOrderPositionFlagType(Enum):
    """期权行权后是否保留期货头寸的标记类型"""
    THOST_FTDC_EOPF_Reserve = 48
    """保留"""
    THOST_FTDC_EOPF_UnReserve = 49
    """不保留"""


class TThostFtdcExecOrderCloseFlagType(Enum):
    """期权行权后生成的头寸是否自动平仓类型"""
    THOST_FTDC_EOCF_AutoClose = 48
    """自动平仓"""
    THOST_FTDC_EOCF_NotToClose = 49
    """免于自动平仓"""


class TThostFtdcProductTypeType(Enum):
    """产品类型类型"""
    THOST_FTDC_PTE_Futures = 49
    """期货"""
    THOST_FTDC_PTE_Options = 50
    """期权"""


class TThostFtdcCZCEUploadFileNameType(Enum):
    """郑商所结算文件名类型"""
    THOST_FTDC_CUFN_CUFN_O = 79
    """^\d{8}_zz_\d{4}"""
    THOST_FTDC_CUFN_CUFN_T = 84
    """^\d{8}成交表"""
    THOST_FTDC_CUFN_CUFN_P = 80
    """^\d{8}单腿持仓表new"""
    THOST_FTDC_CUFN_CUFN_N = 78
    """^\d{8}非平仓了结表"""
    THOST_FTDC_CUFN_CUFN_L = 76
    """^\d{8}平仓表"""
    THOST_FTDC_CUFN_CUFN_F = 70
    """^\d{8}资金表"""
    THOST_FTDC_CUFN_CUFN_C = 67
    """^\d{8}组合持仓表"""
    THOST_FTDC_CUFN_CUFN_M = 77
    """^\d{8}保证金参数表"""


class TThostFtdcDCEUploadFileNameType(Enum):
    """大商所结算文件名类型"""
    THOST_FTDC_DUFN_DUFN_O = 79
    """^\d{8}_dl_\d{3}"""
    THOST_FTDC_DUFN_DUFN_T = 84
    """^\d{8}_成交表"""
    THOST_FTDC_DUFN_DUFN_P = 80
    """^\d{8}_持仓表"""
    THOST_FTDC_DUFN_DUFN_F = 70
    """^\d{8}_资金结算表"""
    THOST_FTDC_DUFN_DUFN_C = 67
    """^\d{8}_优惠组合持仓明细表"""
    THOST_FTDC_DUFN_DUFN_D = 68
    """^\d{8}_持仓明细表"""
    THOST_FTDC_DUFN_DUFN_M = 77
    """^\d{8}_保证金参数表"""
    THOST_FTDC_DUFN_DUFN_S = 83
    """^\d{8}_期权执行表"""


class TThostFtdcSHFEUploadFileNameType(Enum):
    """上期所结算文件名类型"""
    THOST_FTDC_SUFN_SUFN_O = 79
    """^\d{4}_\d{8}_\d{8}_DailyFundChg"""
    THOST_FTDC_SUFN_SUFN_T = 84
    """^\d{4}_\d{8}_\d{8}_Trade"""
    THOST_FTDC_SUFN_SUFN_P = 80
    """^\d{4}_\d{8}_\d{8}_SettlementDetail"""
    THOST_FTDC_SUFN_SUFN_F = 70
    """^\d{4}_\d{8}_\d{8}_Capital"""


class TThostFtdcCFFEXUploadFileNameType(Enum):
    """中金所结算文件名类型"""
    THOST_FTDC_CFUFN_SUFN_T = 84
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade"""
    THOST_FTDC_CFUFN_SUFN_P = 80
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail"""
    THOST_FTDC_CFUFN_SUFN_F = 70
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital"""
    THOST_FTDC_CFUFN_SUFN_S = 83
    """^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec"""


class TThostFtdcCombDirectionType(Enum):
    """组合指令方向类型"""
    THOST_FTDC_CMDR_Comb = 48
    """申请组合"""
    THOST_FTDC_CMDR_UnComb = 49
    """申请拆分"""
    THOST_FTDC_CMDR_DelComb = 50
    """操作员删组合单"""


class TThostFtdcStrikeOffsetTypeType(Enum):
    """行权偏移类型类型"""
    THOST_FTDC_STOV_RealValue = 49
    """实值额"""
    THOST_FTDC_STOV_ProfitValue = 50
    """盈利额"""
    THOST_FTDC_STOV_RealRatio = 51
    """实值比例"""
    THOST_FTDC_STOV_ProfitRatio = 52
    """盈利比例"""


class TThostFtdcReserveOpenAccStasType(Enum):
    """预约开户状态类型"""
    THOST_FTDC_ROAST_Processing = 48
    """等待处理中"""
    THOST_FTDC_ROAST_Cancelled = 49
    """已撤销"""
    THOST_FTDC_ROAST_Opened = 50
    """已开户"""
    THOST_FTDC_ROAST_Invalid = 51
    """无效请求"""


class TThostFtdcNewsUrgencyType(Enum):
    """紧急程度类型"""


class TThostFtdcWeakPasswordSourceType(Enum):
    """弱密码来源类型"""
    THOST_FTDC_WPSR_Lib = 49
    """弱密码库"""
    THOST_FTDC_WPSR_Manual = 50
    """手工录入"""


class TThostFtdcOptSelfCloseFlagType(Enum):
    """期权行权的头寸是否自对冲类型"""
    THOST_FTDC_OSCF_CloseSelfOptionPosition = 49
    """自对冲期权仓位"""
    THOST_FTDC_OSCF_ReserveOptionPosition = 50
    """保留期权仓位"""
    THOST_FTDC_OSCF_SellCloseSelfFuturePosition = 51
    """自对冲卖方履约后的期货仓位"""
    THOST_FTDC_OSCF_ReserveFuturePosition = 52
    """保留卖方履约后的期货仓位"""


class TThostFtdcBizTypeType(Enum):
    """业务类型类型"""
    THOST_FTDC_BZTP_Future = 49
    """期货"""
    THOST_FTDC_BZTP_Stock = 50
    """证券"""


class TThostFtdcAppTypeType(Enum):
    """用户App类型类型"""
    THOST_FTDC_APP_TYPE_Investor = 49
    """直连的投资者"""
    THOST_FTDC_APP_TYPE_InvestorRelay = 50
    """为每个投资者都创建连接的中继"""
    THOST_FTDC_APP_TYPE_OperatorRelay = 51
    """所有投资者共享一个操作员连接的中继"""
    THOST_FTDC_APP_TYPE_UnKnown = 52
    """未知"""


class TThostFtdcResponseValueType(Enum):
    """应答类型类型"""
    THOST_FTDC_RV_Right = 48
    """检查成功"""
    THOST_FTDC_RV_Refuse = 49
    """检查失败"""


class TThostFtdcOTCTradeTypeType(Enum):
    """OTC成交类型类型"""
    THOST_FTDC_OTC_TRDT_Block = 48
    """大宗交易"""
    THOST_FTDC_OTC_TRDT_EFP = 49
    """期转现"""


class TThostFtdcMatchTypeType(Enum):
    """期现风险匹配方式类型"""
    THOST_FTDC_OTC_MT_DV01 = 49
    """基点价值"""
    THOST_FTDC_OTC_MT_ParValue = 50
    """面值"""


class TThostFtdcAuthTypeType(Enum):
    """用户终端认证方式类型"""
    THOST_FTDC_AU_WHITE = 48
    """白名单校验"""
    THOST_FTDC_AU_BLACK = 49
    """黑名单校验"""


class TThostFtdcClassTypeType(Enum):
    """合约分类方式类型"""
    THOST_FTDC_INS_ALL = 48
    """所有合约"""
    THOST_FTDC_INS_FUTURE = 49
    """期货、即期、期转现、Tas、金属指数合约"""
    THOST_FTDC_INS_OPTION = 50
    """期货、现货期权合约"""
    THOST_FTDC_INS_COMB = 51
    """组合合约"""


class TThostFtdcTradingTypeType(Enum):
    """合约交易状态分类方式类型"""
    THOST_FTDC_TD_ALL = 48
    """所有状态"""
    THOST_FTDC_TD_TRADE = 49
    """交易"""
    THOST_FTDC_TD_UNTRADE = 50
    """非交易"""


