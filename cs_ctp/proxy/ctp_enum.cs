
/// <summary>
/// 
/// </summary>
public enum THOST_TE_RESUME_TYPE
{
    /// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESTART = 0,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESUME,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_QUICK
}

/// <summary>
/// 交易所属性类型
///</summary>
public enum TThostFtdcExchangePropertyType : byte
{
	/// <summary>
	/// 根据成交生成报单
	///</summary>
	THOST_FTDC_EXP_GenOrderByTrade = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_EXP_Normal = (byte)'0',
}

/// <summary>
/// 证件类型类型
///</summary>
public enum TThostFtdcIdCardTypeType : byte
{
	/// <summary>
	/// 其他证件
	///</summary>
	THOST_FTDC_ICT_OtherCard = (byte)'x',
	/// <summary>
	/// 资管产品备案函
	///</summary>
	THOST_FTDC_ICT_CptMngPrdLetter = (byte)'L',
	/// <summary>
	/// 外国人永久居留证
	///</summary>
	THOST_FTDC_ICT_FrgPrmtRdCard = (byte)'K',
	/// <summary>
	/// 人行开户许可证
	///</summary>
	THOST_FTDC_ICT_AccountsPermits = (byte)'J',
	/// <summary>
	/// 港澳永久性居民身份证
	///</summary>
	THOST_FTDC_ICT_HKMCIDCard = (byte)'I',
	/// <summary>
	/// 商业登记证
	///</summary>
	THOST_FTDC_ICT_BusinessRegistration = (byte)'H',
	/// <summary>
	/// 当地身份证
	///</summary>
	THOST_FTDC_ICT_LocalID = (byte)'G',
	/// <summary>
	/// 当地社保ID
	///</summary>
	THOST_FTDC_ICT_SocialID = (byte)'F',
	/// <summary>
	/// 驾照
	///</summary>
	THOST_FTDC_ICT_DrivingLicense = (byte)'D',
	/// <summary>
	/// 台湾居民来往大陆通行证
	///</summary>
	THOST_FTDC_ICT_TwMainlandTravelPermit = (byte)'C',
	/// <summary>
	/// 港澳居民来往内地通行证
	///</summary>
	THOST_FTDC_ICT_HMMainlandTravelPermit = (byte)'B',
	/// <summary>
	/// 税务登记号/当地纳税ID
	///</summary>
	THOST_FTDC_ICT_TaxNo = (byte)'A',
	/// <summary>
	/// 营业执照号
	///</summary>
	THOST_FTDC_ICT_LicenseNo = (byte)'9',
	/// <summary>
	/// 回乡证
	///</summary>
	THOST_FTDC_ICT_HomeComingCard = (byte)'8',
	/// <summary>
	/// 台胞证
	///</summary>
	THOST_FTDC_ICT_TaiwanCompatriotIDCard = (byte)'7',
	/// <summary>
	/// 护照
	///</summary>
	THOST_FTDC_ICT_Passport = (byte)'6',
	/// <summary>
	/// 户口簿
	///</summary>
	THOST_FTDC_ICT_HouseholdRegister = (byte)'5',
	/// <summary>
	/// 士兵证
	///</summary>
	THOST_FTDC_ICT_SoldierIDCard = (byte)'4',
	/// <summary>
	/// 警官证
	///</summary>
	THOST_FTDC_ICT_PoliceIDCard = (byte)'3',
	/// <summary>
	/// 军官证
	///</summary>
	THOST_FTDC_ICT_OfficerIDCard = (byte)'2',
	/// <summary>
	/// 中国公民身份证
	///</summary>
	THOST_FTDC_ICT_IDCard = (byte)'1',
	/// <summary>
	/// 组织机构代码
	///</summary>
	THOST_FTDC_ICT_EID = (byte)'0',
}

/// <summary>
/// 投资者范围类型
///</summary>
public enum TThostFtdcInvestorRangeType : byte
{
	/// <summary>
	/// 单一投资者
	///</summary>
	THOST_FTDC_IR_Single = (byte)'3',
	/// <summary>
	/// 投资者组
	///</summary>
	THOST_FTDC_IR_Group = (byte)'2',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_IR_All = (byte)'1',
}

/// <summary>
/// 投资者范围类型
///</summary>
public enum TThostFtdcDepartmentRangeType : byte
{
	/// <summary>
	/// 单一投资者
	///</summary>
	THOST_FTDC_DR_Single = (byte)'3',
	/// <summary>
	/// 组织架构
	///</summary>
	THOST_FTDC_DR_Group = (byte)'2',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_DR_All = (byte)'1',
}

/// <summary>
/// 数据同步状态类型
///</summary>
public enum TThostFtdcDataSyncStatusType : byte
{
	/// <summary>
	/// 已同步
	///</summary>
	THOST_FTDC_DS_Synchronized = (byte)'3',
	/// <summary>
	/// 同步中
	///</summary>
	THOST_FTDC_DS_Synchronizing = (byte)'2',
	/// <summary>
	/// 未同步
	///</summary>
	THOST_FTDC_DS_Asynchronous = (byte)'1',
}

/// <summary>
/// 经纪公司数据同步状态类型
///</summary>
public enum TThostFtdcBrokerDataSyncStatusType : byte
{
	/// <summary>
	/// 同步中
	///</summary>
	THOST_FTDC_BDS_Synchronizing = (byte)'2',
	/// <summary>
	/// 已同步
	///</summary>
	THOST_FTDC_BDS_Synchronized = (byte)'1',
}

/// <summary>
/// 交易所连接状态类型
///</summary>
public enum TThostFtdcExchangeConnectStatusType : byte
{
	/// <summary>
	/// 已经获取信息
	///</summary>
	THOST_FTDC_ECS_GotInformation = (byte)'9',
	/// <summary>
	/// 已经发出合约查询请求
	///</summary>
	THOST_FTDC_ECS_QryInstrumentSent = (byte)'2',
	/// <summary>
	/// 没有任何连接
	///</summary>
	THOST_FTDC_ECS_NoConnection = (byte)'1',
}

/// <summary>
/// 交易所交易员连接状态类型
///</summary>
public enum TThostFtdcTraderConnectStatusType : byte
{
	/// <summary>
	/// 订阅私有流
	///</summary>
	THOST_FTDC_TCS_SubPrivateFlow = (byte)'4',
	/// <summary>
	/// 已经发出合约查询请求
	///</summary>
	THOST_FTDC_TCS_QryInstrumentSent = (byte)'3',
	/// <summary>
	/// 已经连接
	///</summary>
	THOST_FTDC_TCS_Connected = (byte)'2',
	/// <summary>
	/// 没有任何连接
	///</summary>
	THOST_FTDC_TCS_NotConnected = (byte)'1',
}

/// <summary>
/// 功能代码类型
///</summary>
public enum TThostFtdcFunctionCodeType : byte
{
	/// <summary>
	/// 删除未知单
	///</summary>
	THOST_FTDC_FC_DeleteOrder = (byte)'F',
	/// <summary>
	/// 同步动态令牌
	///</summary>
	THOST_FTDC_FC_SyncOTP = (byte)'E',
	/// <summary>
	/// 预埋报单操作
	///</summary>
	THOST_FTDC_FC_ParkedOrderAction = (byte)'D',
	/// <summary>
	/// 预埋报单插入
	///</summary>
	THOST_FTDC_FC_ParkedOrderInsert = (byte)'C',
	/// <summary>
	/// 超级查询
	///</summary>
	THOST_FTDC_FC_SuperQuery = (byte)'B',
	/// <summary>
	/// 批量同步经纪公司数据
	///</summary>
	THOST_FTDC_FC_BachSyncBrokerData = (byte)'A',
	/// <summary>
	/// 同步经纪公司数据
	///</summary>
	THOST_FTDC_FC_SyncBrokerData = (byte)'9',
	/// <summary>
	/// 同步系统数据
	///</summary>
	THOST_FTDC_FC_SyncSystemData = (byte)'8',
	/// <summary>
	/// 报单操作
	///</summary>
	THOST_FTDC_FC_OrderAction = (byte)'7',
	/// <summary>
	/// 报单插入
	///</summary>
	THOST_FTDC_FC_OrderInsert = (byte)'6',
	/// <summary>
	/// 变更投资者口令
	///</summary>
	THOST_FTDC_FC_InvestorPasswordUpdate = (byte)'5',
	/// <summary>
	/// 变更经纪公司口令
	///</summary>
	THOST_FTDC_FC_BrokerPasswordUpdate = (byte)'4',
	/// <summary>
	/// 变更管理用户口令
	///</summary>
	THOST_FTDC_FC_UserPasswordUpdate = (byte)'3',
	/// <summary>
	/// 强制用户登出
	///</summary>
	THOST_FTDC_FC_ForceUserLogout = (byte)'2',
	/// <summary>
	/// 数据异步化
	///</summary>
	THOST_FTDC_FC_DataAsync = (byte)'1',
}

/// <summary>
/// 经纪公司功能代码类型
///</summary>
public enum TThostFtdcBrokerFunctionCodeType : byte
{
	/// <summary>
	/// 银期签约解约
	///</summary>
	THOST_FTDC_BFC_FBAccount = (byte)'X',
	/// <summary>
	/// 银期签到签退
	///</summary>
	THOST_FTDC_BFC_FBSign = (byte)'W',
	/// <summary>
	/// 持仓限额查询
	///</summary>
	THOST_FTDC_BFC_QryPosiLimit = (byte)'V',
	/// <summary>
	/// 持仓限额预警
	///</summary>
	THOST_FTDC_BFC_PosiLimitWarn = (byte)'U',
	/// <summary>
	/// 行权交收风险
	///</summary>
	THOST_FTDC_BFC_ExecOrderRisk = (byte)'P',
	/// <summary>
	/// 行权试算
	///</summary>
	THOST_FTDC_BFC_PreExecOrder = (byte)'T',
	/// <summary>
	/// 备兑不足预警
	///</summary>
	THOST_FTDC_BFC_CoverWarn = (byte)'S',
	/// <summary>
	/// 席位资金预警
	///</summary>
	THOST_FTDC_BFC_BrokerDepositWarn = (byte)'Q',
	/// <summary>
	/// 证券处置
	///</summary>
	THOST_FTDC_BFC_StockDisposal = (byte)'O',
	/// <summary>
	/// 指定
	///</summary>
	THOST_FTDC_BFC_Designate = (byte)'N',
	/// <summary>
	/// 资金不够仍允许行权
	///</summary>
	THOST_FTDC_BFC_ExecOrderNoCheck = (byte)'M',
	/// <summary>
	/// 预埋报单操作
	///</summary>
	THOST_FTDC_BFC_ParkedOrderAction = (byte)'L',
	/// <summary>
	/// 预埋报单插入
	///</summary>
	THOST_FTDC_BFC_ParkedOrderInsert = (byte)'K',
	/// <summary>
	/// 删除未知单
	///</summary>
	THOST_FTDC_BFC_DeleteOrder = (byte)'J',
	/// <summary>
	/// 交易终端应急功能
	///</summary>
	THOST_FTDC_BFC_TbCommand = (byte)'H',
	/// <summary>
	/// 风险级别标准设置
	///</summary>
	THOST_FTDC_BFC_CfgRiskLevelStd = (byte)'G',
	/// <summary>
	/// 发送业务通知
	///</summary>
	THOST_FTDC_BFC_SendBizNotice = (byte)'F',
	/// <summary>
	/// 同步动态令牌
	///</summary>
	THOST_FTDC_BFC_SyncOTP = (byte)'E',
	/// <summary>
	/// 业务通知模板设置
	///</summary>
	THOST_FTDC_BFC_CfgBizNotice = (byte)'D',
	/// <summary>
	/// 业务通知查询
	///</summary>
	THOST_FTDC_BFC_QryBizNotice = (byte)'C',
	/// <summary>
	/// 行情预警
	///</summary>
	THOST_FTDC_BFC_MarketDataWarn = (byte)'B',
	/// <summary>
	/// 风控指标设置
	///</summary>
	THOST_FTDC_BFC_RiskTargetSetup = (byte)'A',
	/// <summary>
	/// 数据导出
	///</summary>
	THOST_FTDC_BFC_DataExport = (byte)'z',
	/// <summary>
	/// 风险预算
	///</summary>
	THOST_FTDC_BFC_RiskPredict = (byte)'y',
	/// <summary>
	/// 净持仓保证金指标
	///</summary>
	THOST_FTDC_BFC_NetPositionInd = (byte)'x',
	/// <summary>
	/// 权益反算
	///</summary>
	THOST_FTDC_BFC_RemainCalc = (byte)'w',
	/// <summary>
	/// 压力测试
	///</summary>
	THOST_FTDC_BFC_PressTest = (byte)'v',
	/// <summary>
	/// 强平
	///</summary>
	THOST_FTDC_BFC_ForceClose = (byte)'u',
	/// <summary>
	/// 交易编码查询
	///</summary>
	THOST_FTDC_BFC_QueryTradingCode = (byte)'t',
	/// <summary>
	/// 投资者信息查询
	///</summary>
	THOST_FTDC_BFC_QueryInvestor = (byte)'s',
	/// <summary>
	/// 出入金查询
	///</summary>
	THOST_FTDC_BFC_QueryFundChange = (byte)'r',
	/// <summary>
	/// 风险通知查询
	///</summary>
	THOST_FTDC_BFC_QueryRiskNotify = (byte)'q',
	/// <summary>
	/// 用户事件查询
	///</summary>
	THOST_FTDC_BFC_QueryUserEvent = (byte)'p',
	/// <summary>
	/// 行情查询
	///</summary>
	THOST_FTDC_BFC_QueryMarketData = (byte)'o',
	/// <summary>
	/// 持仓查询
	///</summary>
	THOST_FTDC_BFC_QueryPosition = (byte)'n',
	/// <summary>
	/// 成交查询
	///</summary>
	THOST_FTDC_BFC_QueryTrade = (byte)'m',
	/// <summary>
	/// 报单查询
	///</summary>
	THOST_FTDC_BFC_QueryOrder = (byte)'l',
	/// <summary>
	/// 资金查询
	///</summary>
	THOST_FTDC_BFC_QueryFund = (byte)'k',
	/// <summary>
	/// 察看经纪公司资金权限
	///</summary>
	THOST_FTDC_BFC_BrokerDeposit = (byte)'j',
	/// <summary>
	/// 风控通知发送
	///</summary>
	THOST_FTDC_BFC_RiskNotice = (byte)'i',
	/// <summary>
	/// 风控通知控制
	///</summary>
	THOST_FTDC_BFC_RiskNoticeCtl = (byte)'h',
	/// <summary>
	/// 查询/管理：查询会话，踢人等
	///</summary>
	THOST_FTDC_BFC_Session = (byte)'g',
	/// <summary>
	/// 风险监控
	///</summary>
	THOST_FTDC_BFC_Risk = (byte)'f',
	/// <summary>
	/// 银期转账
	///</summary>
	THOST_FTDC_BFC_Virement = (byte)'e',
	/// <summary>
	/// 交易功能：报单，撤单
	///</summary>
	THOST_FTDC_BFC_Trade = (byte)'d',
	/// <summary>
	/// 交易查询：如查成交，委托
	///</summary>
	THOST_FTDC_BFC_TradeQry = (byte)'c',
	/// <summary>
	/// 基本查询：查询基础数据，如合约，交易所等常量
	///</summary>
	THOST_FTDC_BFC_BaseQry = (byte)'b',
	/// <summary>
	/// 系统功能：登入/登出/修改密码等
	///</summary>
	THOST_FTDC_BFC_log = (byte)'a',
	/// <summary>
	/// 全部查询
	///</summary>
	THOST_FTDC_BFC_AllQuery = (byte)'7',
	/// <summary>
	/// 报单操作
	///</summary>
	THOST_FTDC_BFC_OrderAction = (byte)'6',
	/// <summary>
	/// 报单插入
	///</summary>
	THOST_FTDC_BFC_OrderInsert = (byte)'5',
	/// <summary>
	/// 批量同步经纪公司数据
	///</summary>
	THOST_FTDC_BFC_BachSyncBrokerData = (byte)'4',
	/// <summary>
	/// 同步经纪公司数据
	///</summary>
	THOST_FTDC_BFC_SyncBrokerData = (byte)'3',
	/// <summary>
	/// 变更用户口令
	///</summary>
	THOST_FTDC_BFC_UserPasswordUpdate = (byte)'2',
	/// <summary>
	/// 强制用户登出
	///</summary>
	THOST_FTDC_BFC_ForceUserLogout = (byte)'1',
}

/// <summary>
/// 报单操作状态类型
///</summary>
public enum TThostFtdcOrderActionStatusType : byte
{
	/// <summary>
	/// 已经被拒绝
	///</summary>
	THOST_FTDC_OAS_Rejected = (byte)'c',
	/// <summary>
	/// 已经接受
	///</summary>
	THOST_FTDC_OAS_Accepted = (byte)'b',
	/// <summary>
	/// 已经提交
	///</summary>
	THOST_FTDC_OAS_Submitted = (byte)'a',
}

/// <summary>
/// 报单状态类型
///</summary>
public enum TThostFtdcOrderStatusType : byte
{
	/// <summary>
	/// 已触发
	///</summary>
	THOST_FTDC_OST_Touched = (byte)'c',
	/// <summary>
	/// 尚未触发
	///</summary>
	THOST_FTDC_OST_NotTouched = (byte)'b',
	/// <summary>
	/// 未知
	///</summary>
	THOST_FTDC_OST_Unknown = (byte)'a',
	/// <summary>
	/// 撤单
	///</summary>
	THOST_FTDC_OST_Canceled = (byte)'5',
	/// <summary>
	/// 未成交不在队列中
	///</summary>
	THOST_FTDC_OST_NoTradeNotQueueing = (byte)'4',
	/// <summary>
	/// 未成交还在队列中
	///</summary>
	THOST_FTDC_OST_NoTradeQueueing = (byte)'3',
	/// <summary>
	/// 部分成交不在队列中
	///</summary>
	THOST_FTDC_OST_PartTradedNotQueueing = (byte)'2',
	/// <summary>
	/// 部分成交还在队列中
	///</summary>
	THOST_FTDC_OST_PartTradedQueueing = (byte)'1',
	/// <summary>
	/// 全部成交
	///</summary>
	THOST_FTDC_OST_AllTraded = (byte)'0',
}

/// <summary>
/// 报单提交状态类型
///</summary>
public enum TThostFtdcOrderSubmitStatusType : byte
{
	/// <summary>
	/// 改单已经被拒绝
	///</summary>
	THOST_FTDC_OSS_ModifyRejected = (byte)'6',
	/// <summary>
	/// 撤单已经被拒绝
	///</summary>
	THOST_FTDC_OSS_CancelRejected = (byte)'5',
	/// <summary>
	/// 报单已经被拒绝
	///</summary>
	THOST_FTDC_OSS_InsertRejected = (byte)'4',
	/// <summary>
	/// 已经接受
	///</summary>
	THOST_FTDC_OSS_Accepted = (byte)'3',
	/// <summary>
	/// 修改已经提交
	///</summary>
	THOST_FTDC_OSS_ModifySubmitted = (byte)'2',
	/// <summary>
	/// 撤单已经提交
	///</summary>
	THOST_FTDC_OSS_CancelSubmitted = (byte)'1',
	/// <summary>
	/// 已经提交
	///</summary>
	THOST_FTDC_OSS_InsertSubmitted = (byte)'0',
}

/// <summary>
/// 持仓日期类型
///</summary>
public enum TThostFtdcPositionDateType : byte
{
	/// <summary>
	/// 历史持仓
	///</summary>
	THOST_FTDC_PSD_History = (byte)'2',
	/// <summary>
	/// 今日持仓
	///</summary>
	THOST_FTDC_PSD_Today = (byte)'1',
}

/// <summary>
/// 持仓日期类型类型
///</summary>
public enum TThostFtdcPositionDateTypeType : byte
{
	/// <summary>
	/// 不使用历史持仓
	///</summary>
	THOST_FTDC_PDT_NoUseHistory = (byte)'2',
	/// <summary>
	/// 使用历史持仓
	///</summary>
	THOST_FTDC_PDT_UseHistory = (byte)'1',
}

/// <summary>
/// 交易角色类型
///</summary>
public enum TThostFtdcTradingRoleType : byte
{
	/// <summary>
	/// 做市商
	///</summary>
	THOST_FTDC_ER_Maker = (byte)'3',
	/// <summary>
	/// 自营
	///</summary>
	THOST_FTDC_ER_Host = (byte)'2',
	/// <summary>
	/// 代理
	///</summary>
	THOST_FTDC_ER_Broker = (byte)'1',
}

/// <summary>
/// 产品类型类型
///</summary>
public enum TThostFtdcProductClassType : byte
{
	/// <summary>
	/// 现货期权
	///</summary>
	THOST_FTDC_PC_SpotOption = (byte)'6',
	/// <summary>
	/// 期转现
	///</summary>
	THOST_FTDC_PC_EFP = (byte)'5',
	/// <summary>
	/// 即期
	///</summary>
	THOST_FTDC_PC_Spot = (byte)'4',
	/// <summary>
	/// 组合
	///</summary>
	THOST_FTDC_PC_Combination = (byte)'3',
	/// <summary>
	/// 期货期权
	///</summary>
	THOST_FTDC_PC_Options = (byte)'2',
	/// <summary>
	/// 期货
	///</summary>
	THOST_FTDC_PC_Futures = (byte)'1',
}

/// <summary>
/// 合约生命周期状态类型
///</summary>
public enum TThostFtdcInstLifePhaseType : byte
{
	/// <summary>
	/// 到期
	///</summary>
	THOST_FTDC_IP_Expired = (byte)'3',
	/// <summary>
	/// 停牌
	///</summary>
	THOST_FTDC_IP_Pause = (byte)'2',
	/// <summary>
	/// 上市
	///</summary>
	THOST_FTDC_IP_Started = (byte)'1',
	/// <summary>
	/// 未上市
	///</summary>
	THOST_FTDC_IP_NotStart = (byte)'0',
}

/// <summary>
/// 买卖方向类型
///</summary>
public enum TThostFtdcDirectionType : byte
{
	/// <summary>
	/// 卖
	///</summary>
	THOST_FTDC_D_Sell = (byte)'1',
	/// <summary>
	/// 买
	///</summary>
	THOST_FTDC_D_Buy = (byte)'0',
}

/// <summary>
/// 持仓类型类型
///</summary>
public enum TThostFtdcPositionTypeType : byte
{
	/// <summary>
	/// 综合持仓
	///</summary>
	THOST_FTDC_PT_Gross = (byte)'2',
	/// <summary>
	/// 净持仓
	///</summary>
	THOST_FTDC_PT_Net = (byte)'1',
}

/// <summary>
/// 持仓多空方向类型
///</summary>
public enum TThostFtdcPosiDirectionType : byte
{
	/// <summary>
	/// 空头
	///</summary>
	THOST_FTDC_PD_Short = (byte)'3',
	/// <summary>
	/// 多头
	///</summary>
	THOST_FTDC_PD_Long = (byte)'2',
	/// <summary>
	/// 净
	///</summary>
	THOST_FTDC_PD_Net = (byte)'1',
}

/// <summary>
/// 系统结算状态类型
///</summary>
public enum TThostFtdcSysSettlementStatusType : byte
{
	/// <summary>
	/// 结算完成
	///</summary>
	THOST_FTDC_SS_SettlementFinished = (byte)'5',
	/// <summary>
	/// 结算
	///</summary>
	THOST_FTDC_SS_Settlement = (byte)'4',
	/// <summary>
	/// 操作
	///</summary>
	THOST_FTDC_SS_Operating = (byte)'3',
	/// <summary>
	/// 启动
	///</summary>
	THOST_FTDC_SS_Startup = (byte)'2',
	/// <summary>
	/// 不活跃
	///</summary>
	THOST_FTDC_SS_NonActive = (byte)'1',
}

/// <summary>
/// 费率属性类型
///</summary>
public enum TThostFtdcRatioAttrType : byte
{
	/// <summary>
	/// 结算费率
	///</summary>
	THOST_FTDC_RA_Settlement = (byte)'1',
	/// <summary>
	/// 交易费率
	///</summary>
	THOST_FTDC_RA_Trade = (byte)'0',
}

/// <summary>
/// 投机套保标志类型
///</summary>
public enum TThostFtdcHedgeFlagType : byte
{
	/// <summary>
	/// 第一腿套保第二腿投机  大商所专用
	///</summary>
	THOST_FTDC_HF_HedgeSpec = (byte)'7',
	/// <summary>
	/// 第一腿投机第二腿套保 大商所专用
	///</summary>
	THOST_FTDC_HF_SpecHedge = (byte)'6',
	/// <summary>
	/// 做市商
	///</summary>
	THOST_FTDC_HF_MarketMaker = (byte)'5',
	/// <summary>
	/// 套保
	///</summary>
	THOST_FTDC_HF_Hedge = (byte)'3',
	/// <summary>
	/// 套利
	///</summary>
	THOST_FTDC_HF_Arbitrage = (byte)'2',
	/// <summary>
	/// 投机
	///</summary>
	THOST_FTDC_HF_Speculation = (byte)'1',
}

/// <summary>
/// 投机套保标志类型
///</summary>
public enum TThostFtdcBillHedgeFlagType : byte
{
	/// <summary>
	/// 套保
	///</summary>
	THOST_FTDC_BHF_Hedge = (byte)'3',
	/// <summary>
	/// 套利
	///</summary>
	THOST_FTDC_BHF_Arbitrage = (byte)'2',
	/// <summary>
	/// 投机
	///</summary>
	THOST_FTDC_BHF_Speculation = (byte)'1',
}

/// <summary>
/// 交易编码类型类型
///</summary>
public enum TThostFtdcClientIDTypeType : byte
{
	/// <summary>
	/// 做市商
	///</summary>
	THOST_FTDC_CIDT_MarketMaker = (byte)'5',
	/// <summary>
	/// 套保
	///</summary>
	THOST_FTDC_CIDT_Hedge = (byte)'3',
	/// <summary>
	/// 套利
	///</summary>
	THOST_FTDC_CIDT_Arbitrage = (byte)'2',
	/// <summary>
	/// 投机
	///</summary>
	THOST_FTDC_CIDT_Speculation = (byte)'1',
}

/// <summary>
/// 报单价格条件类型
///</summary>
public enum TThostFtdcOrderPriceTypeType : byte
{
	/// <summary>
	/// 五档价
	///</summary>
	THOST_FTDC_OPT_FiveLevelPrice = (byte)'G',
	/// <summary>
	/// 买一价浮动上浮3个ticks
	///</summary>
	THOST_FTDC_OPT_BidPrice1PlusThreeTicks = (byte)'F',
	/// <summary>
	/// 买一价浮动上浮2个ticks
	///</summary>
	THOST_FTDC_OPT_BidPrice1PlusTwoTicks = (byte)'E',
	/// <summary>
	/// 买一价浮动上浮1个ticks
	///</summary>
	THOST_FTDC_OPT_BidPrice1PlusOneTicks = (byte)'D',
	/// <summary>
	/// 买一价
	///</summary>
	THOST_FTDC_OPT_BidPrice1 = (byte)'C',
	/// <summary>
	/// 卖一价浮动上浮3个ticks
	///</summary>
	THOST_FTDC_OPT_AskPrice1PlusThreeTicks = (byte)'B',
	/// <summary>
	/// 卖一价浮动上浮2个ticks
	///</summary>
	THOST_FTDC_OPT_AskPrice1PlusTwoTicks = (byte)'A',
	/// <summary>
	/// 卖一价浮动上浮1个ticks
	///</summary>
	THOST_FTDC_OPT_AskPrice1PlusOneTicks = (byte)'9',
	/// <summary>
	/// 卖一价
	///</summary>
	THOST_FTDC_OPT_AskPrice1 = (byte)'8',
	/// <summary>
	/// 最新价浮动上浮3个ticks
	///</summary>
	THOST_FTDC_OPT_LastPricePlusThreeTicks = (byte)'7',
	/// <summary>
	/// 最新价浮动上浮2个ticks
	///</summary>
	THOST_FTDC_OPT_LastPricePlusTwoTicks = (byte)'6',
	/// <summary>
	/// 最新价浮动上浮1个ticks
	///</summary>
	THOST_FTDC_OPT_LastPricePlusOneTicks = (byte)'5',
	/// <summary>
	/// 最新价
	///</summary>
	THOST_FTDC_OPT_LastPrice = (byte)'4',
	/// <summary>
	/// 最优价
	///</summary>
	THOST_FTDC_OPT_BestPrice = (byte)'3',
	/// <summary>
	/// 限价
	///</summary>
	THOST_FTDC_OPT_LimitPrice = (byte)'2',
	/// <summary>
	/// 任意价
	///</summary>
	THOST_FTDC_OPT_AnyPrice = (byte)'1',
}

/// <summary>
/// 开平标志类型
///</summary>
public enum TThostFtdcOffsetFlagType : byte
{
	/// <summary>
	/// 本地强平
	///</summary>
	THOST_FTDC_OF_LocalForceClose = (byte)'6',
	/// <summary>
	/// 强减
	///</summary>
	THOST_FTDC_OF_ForceOff = (byte)'5',
	/// <summary>
	/// 平昨
	///</summary>
	THOST_FTDC_OF_CloseYesterday = (byte)'4',
	/// <summary>
	/// 平今
	///</summary>
	THOST_FTDC_OF_CloseToday = (byte)'3',
	/// <summary>
	/// 强平
	///</summary>
	THOST_FTDC_OF_ForceClose = (byte)'2',
	/// <summary>
	/// 平仓
	///</summary>
	THOST_FTDC_OF_Close = (byte)'1',
	/// <summary>
	/// 开仓
	///</summary>
	THOST_FTDC_OF_Open = (byte)'0',
}

/// <summary>
/// 强平原因类型
///</summary>
public enum TThostFtdcForceCloseReasonType : byte
{
	/// <summary>
	/// 自然人临近交割
	///</summary>
	THOST_FTDC_FCC_PersonDeliv = (byte)'7',
	/// <summary>
	/// 其它
	///</summary>
	THOST_FTDC_FCC_Other = (byte)'6',
	/// <summary>
	/// 违规
	///</summary>
	THOST_FTDC_FCC_Violation = (byte)'5',
	/// <summary>
	/// 持仓非整数倍
	///</summary>
	THOST_FTDC_FCC_NotMultiple = (byte)'4',
	/// <summary>
	/// 会员超仓
	///</summary>
	THOST_FTDC_FCC_MemberOverPositionLimit = (byte)'3',
	/// <summary>
	/// 客户超仓
	///</summary>
	THOST_FTDC_FCC_ClientOverPositionLimit = (byte)'2',
	/// <summary>
	/// 资金不足
	///</summary>
	THOST_FTDC_FCC_LackDeposit = (byte)'1',
	/// <summary>
	/// 非强平
	///</summary>
	THOST_FTDC_FCC_NotForceClose = (byte)'0',
}

/// <summary>
/// 报单类型类型
///</summary>
public enum TThostFtdcOrderTypeType : byte
{
	/// <summary>
	/// 期转现成交衍生
	///</summary>
	THOST_FTDC_ORDT_DeriveFromEFPTrade = (byte)'7',
	/// <summary>
	/// 大宗交易成交衍生
	///</summary>
	THOST_FTDC_ORDT_DeriveFromBlockTrade = (byte)'6',
	/// <summary>
	/// 互换单
	///</summary>
	THOST_FTDC_ORDT_Swap = (byte)'5',
	/// <summary>
	/// 条件单
	///</summary>
	THOST_FTDC_ORDT_ConditionalOrder = (byte)'4',
	/// <summary>
	/// 组合报单
	///</summary>
	THOST_FTDC_ORDT_Combination = (byte)'3',
	/// <summary>
	/// 组合衍生
	///</summary>
	THOST_FTDC_ORDT_DeriveFromCombination = (byte)'2',
	/// <summary>
	/// 报价衍生
	///</summary>
	THOST_FTDC_ORDT_DeriveFromQuote = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_ORDT_Normal = (byte)'0',
}

/// <summary>
/// 有效期类型类型
///</summary>
public enum TThostFtdcTimeConditionType : byte
{
	/// <summary>
	/// 集合竞价有效
	///</summary>
	THOST_FTDC_TC_GFA = (byte)'6',
	/// <summary>
	/// 撤销前有效
	///</summary>
	THOST_FTDC_TC_GTC = (byte)'5',
	/// <summary>
	/// 指定日期前有效
	///</summary>
	THOST_FTDC_TC_GTD = (byte)'4',
	/// <summary>
	/// 当日有效
	///</summary>
	THOST_FTDC_TC_GFD = (byte)'3',
	/// <summary>
	/// 本节有效
	///</summary>
	THOST_FTDC_TC_GFS = (byte)'2',
	/// <summary>
	/// 立即完成，否则撤销
	///</summary>
	THOST_FTDC_TC_IOC = (byte)'1',
}

/// <summary>
/// 成交量类型类型
///</summary>
public enum TThostFtdcVolumeConditionType : byte
{
	/// <summary>
	/// 全部数量
	///</summary>
	THOST_FTDC_VC_CV = (byte)'3',
	/// <summary>
	/// 最小数量
	///</summary>
	THOST_FTDC_VC_MV = (byte)'2',
	/// <summary>
	/// 任何数量
	///</summary>
	THOST_FTDC_VC_AV = (byte)'1',
}

/// <summary>
/// 触发条件类型
///</summary>
public enum TThostFtdcContingentConditionType : byte
{
	/// <summary>
	/// 买一价小于等于条件价
	///</summary>
	THOST_FTDC_CC_BidPriceLesserEqualStopPrice = (byte)'H',
	/// <summary>
	/// 买一价小于条件价
	///</summary>
	THOST_FTDC_CC_BidPriceLesserThanStopPrice = (byte)'F',
	/// <summary>
	/// 买一价大于等于条件价
	///</summary>
	THOST_FTDC_CC_BidPriceGreaterEqualStopPrice = (byte)'E',
	/// <summary>
	/// 买一价大于条件价
	///</summary>
	THOST_FTDC_CC_BidPriceGreaterThanStopPrice = (byte)'D',
	/// <summary>
	/// 卖一价小于等于条件价
	///</summary>
	THOST_FTDC_CC_AskPriceLesserEqualStopPrice = (byte)'C',
	/// <summary>
	/// 卖一价小于条件价
	///</summary>
	THOST_FTDC_CC_AskPriceLesserThanStopPrice = (byte)'B',
	/// <summary>
	/// 卖一价大于等于条件价
	///</summary>
	THOST_FTDC_CC_AskPriceGreaterEqualStopPrice = (byte)'A',
	/// <summary>
	/// 卖一价大于条件价
	///</summary>
	THOST_FTDC_CC_AskPriceGreaterThanStopPrice = (byte)'9',
	/// <summary>
	/// 最新价小于等于条件价
	///</summary>
	THOST_FTDC_CC_LastPriceLesserEqualStopPrice = (byte)'8',
	/// <summary>
	/// 最新价小于条件价
	///</summary>
	THOST_FTDC_CC_LastPriceLesserThanStopPrice = (byte)'7',
	/// <summary>
	/// 最新价大于等于条件价
	///</summary>
	THOST_FTDC_CC_LastPriceGreaterEqualStopPrice = (byte)'6',
	/// <summary>
	/// 最新价大于条件价
	///</summary>
	THOST_FTDC_CC_LastPriceGreaterThanStopPrice = (byte)'5',
	/// <summary>
	/// 预埋单
	///</summary>
	THOST_FTDC_CC_ParkedOrder = (byte)'4',
	/// <summary>
	/// 止赢
	///</summary>
	THOST_FTDC_CC_TouchProfit = (byte)'3',
	/// <summary>
	/// 止损
	///</summary>
	THOST_FTDC_CC_Touch = (byte)'2',
	/// <summary>
	/// 立即
	///</summary>
	THOST_FTDC_CC_Immediately = (byte)'1',
}

/// <summary>
/// 操作标志类型
///</summary>
public enum TThostFtdcActionFlagType : byte
{
	/// <summary>
	/// 修改
	///</summary>
	THOST_FTDC_AF_Modify = (byte)'3',
	/// <summary>
	/// 删除
	///</summary>
	THOST_FTDC_AF_Delete = (byte)'0',
}

/// <summary>
/// 交易权限类型
///</summary>
public enum TThostFtdcTradingRightType : byte
{
	/// <summary>
	/// 不能交易
	///</summary>
	THOST_FTDC_TR_Forbidden = (byte)'2',
	/// <summary>
	/// 只能平仓
	///</summary>
	THOST_FTDC_TR_CloseOnly = (byte)'1',
	/// <summary>
	/// 可以交易
	///</summary>
	THOST_FTDC_TR_Allow = (byte)'0',
}

/// <summary>
/// 报单来源类型
///</summary>
public enum TThostFtdcOrderSourceType : byte
{
	/// <summary>
	/// 来自管理员
	///</summary>
	THOST_FTDC_OSRC_Administrator = (byte)'1',
	/// <summary>
	/// 来自参与者
	///</summary>
	THOST_FTDC_OSRC_Participant = (byte)'0',
}

/// <summary>
/// 成交类型类型
///</summary>
public enum TThostFtdcTradeTypeType : byte
{
	/// <summary>
	/// 大宗交易成交
	///</summary>
	THOST_FTDC_TRDT_BlockTrade = (byte)'5',
	/// <summary>
	/// 组合衍生成交
	///</summary>
	THOST_FTDC_TRDT_CombinationDerived = (byte)'4',
	/// <summary>
	/// 期转现衍生成交
	///</summary>
	THOST_FTDC_TRDT_EFPDerived = (byte)'3',
	/// <summary>
	/// OTC成交
	///</summary>
	THOST_FTDC_TRDT_OTC = (byte)'2',
	/// <summary>
	/// 期权执行
	///</summary>
	THOST_FTDC_TRDT_OptionsExecution = (byte)'1',
	/// <summary>
	/// 普通成交
	///</summary>
	THOST_FTDC_TRDT_Common = (byte)'0',
	/// <summary>
	/// 组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
	///</summary>
	THOST_FTDC_TRDT_SplitCombinatio = (byte)'n',
}

/// <summary>
/// 成交价来源类型
///</summary>
public enum TThostFtdcPriceSourceType : byte
{
	/// <summary>
	/// 场外成交价
	///</summary>
	THOST_FTDC_PSRC_OTC = (byte)'3',
	/// <summary>
	/// 卖委托价
	///</summary>
	THOST_FTDC_PSRC_Sell = (byte)'2',
	/// <summary>
	/// 买委托价
	///</summary>
	THOST_FTDC_PSRC_Buy = (byte)'1',
	/// <summary>
	/// 前成交价
	///</summary>
	THOST_FTDC_PSRC_LastPrice = (byte)'0',
}

/// <summary>
/// 合约交易状态类型
///</summary>
public enum TThostFtdcInstrumentStatusType : byte
{
	/// <summary>
	/// 收盘
	///</summary>
	THOST_FTDC_IS_Closed = (byte)'6',
	/// <summary>
	/// 集合竞价撮合
	///</summary>
	THOST_FTDC_IS_AuctionMatch = (byte)'5',
	/// <summary>
	/// 集合竞价价格平衡
	///</summary>
	THOST_FTDC_IS_AuctionBalance = (byte)'4',
	/// <summary>
	/// 集合竞价报单
	///</summary>
	THOST_FTDC_IS_AuctionOrdering = (byte)'3',
	/// <summary>
	/// 连续交易
	///</summary>
	THOST_FTDC_IS_Continous = (byte)'2',
	/// <summary>
	/// 非交易
	///</summary>
	THOST_FTDC_IS_NoTrading = (byte)'1',
	/// <summary>
	/// 开盘前
	///</summary>
	THOST_FTDC_IS_BeforeTrading = (byte)'0',
}

/// <summary>
/// 品种进入交易状态原因类型
///</summary>
public enum TThostFtdcInstStatusEnterReasonType : byte
{
	/// <summary>
	/// 熔断
	///</summary>
	THOST_FTDC_IER_Fuse = (byte)'3',
	/// <summary>
	/// 手动切换
	///</summary>
	THOST_FTDC_IER_Manual = (byte)'2',
	/// <summary>
	/// 自动切换
	///</summary>
	THOST_FTDC_IER_Automatic = (byte)'1',
}

/// <summary>
/// 处理状态类型
///</summary>
public enum TThostFtdcBatchStatusType : byte
{
	/// <summary>
	/// 审核失败
	///</summary>
	THOST_FTDC_BS_Failed = (byte)'3',
	/// <summary>
	/// 已上传
	///</summary>
	THOST_FTDC_BS_Uploaded = (byte)'2',
	/// <summary>
	/// 未上传
	///</summary>
	THOST_FTDC_BS_NoUpload = (byte)'1',
}

/// <summary>
/// 按品种返还方式类型
///</summary>
public enum TThostFtdcReturnStyleType : byte
{
	/// <summary>
	/// 按品种
	///</summary>
	THOST_FTDC_RS_ByProduct = (byte)'2',
	/// <summary>
	/// 按所有品种
	///</summary>
	THOST_FTDC_RS_All = (byte)'1',
}

/// <summary>
/// 返还模式类型
///</summary>
public enum TThostFtdcReturnPatternType : byte
{
	/// <summary>
	/// 按留存手续费
	///</summary>
	THOST_FTDC_RP_ByFeeOnHand = (byte)'2',
	/// <summary>
	/// 按成交手数
	///</summary>
	THOST_FTDC_RP_ByVolume = (byte)'1',
}

/// <summary>
/// 返还级别类型
///</summary>
public enum TThostFtdcReturnLevelType : byte
{
	/// <summary>
	/// 级别9
	///</summary>
	THOST_FTDC_RL_Level9 = (byte)'9',
	/// <summary>
	/// 级别8
	///</summary>
	THOST_FTDC_RL_Level8 = (byte)'8',
	/// <summary>
	/// 级别7
	///</summary>
	THOST_FTDC_RL_Level7 = (byte)'7',
	/// <summary>
	/// 级别6
	///</summary>
	THOST_FTDC_RL_Level6 = (byte)'6',
	/// <summary>
	/// 级别5
	///</summary>
	THOST_FTDC_RL_Level5 = (byte)'5',
	/// <summary>
	/// 级别4
	///</summary>
	THOST_FTDC_RL_Level4 = (byte)'4',
	/// <summary>
	/// 级别3
	///</summary>
	THOST_FTDC_RL_Level3 = (byte)'3',
	/// <summary>
	/// 级别2
	///</summary>
	THOST_FTDC_RL_Level2 = (byte)'2',
	/// <summary>
	/// 级别1
	///</summary>
	THOST_FTDC_RL_Level1 = (byte)'1',
}

/// <summary>
/// 返还标准类型
///</summary>
public enum TThostFtdcReturnStandardType : byte
{
	/// <summary>
	/// 按某一标准
	///</summary>
	THOST_FTDC_RSD_ByStandard = (byte)'2',
	/// <summary>
	/// 分阶段返还
	///</summary>
	THOST_FTDC_RSD_ByPeriod = (byte)'1',
}

/// <summary>
/// 质押类型类型
///</summary>
public enum TThostFtdcMortgageTypeType : byte
{
	/// <summary>
	/// 质入
	///</summary>
	THOST_FTDC_MT_In = (byte)'1',
	/// <summary>
	/// 质出
	///</summary>
	THOST_FTDC_MT_Out = (byte)'0',
}

/// <summary>
/// 投资者结算参数代码类型
///</summary>
public enum TThostFtdcInvestorSettlementParamIDType : byte
{
	/// <summary>
	/// 结算单结存是否包含质押
	///</summary>
	THOST_FTDC_ISPI_BillDeposit = (byte)'9',
	/// <summary>
	/// 保证金算法
	///</summary>
	THOST_FTDC_ISPI_MarginWay = (byte)'5',
	/// <summary>
	/// 质押比例
	///</summary>
	THOST_FTDC_ISPI_MortgageRatio = (byte)'4',
}

/// <summary>
/// 交易所结算参数代码类型
///</summary>
public enum TThostFtdcExchangeSettlementParamIDType : byte
{
	/// <summary>
	/// 最低保障系数
	///</summary>
	THOST_FTDC_ESPI_OptMiniGuarantee = (byte)'b',
	/// <summary>
	/// 虚值期权保证金优惠比率
	///</summary>
	THOST_FTDC_ESPI_OptOutDisCountRate = (byte)'a',
	/// <summary>
	/// 大商所套利保证金是否优惠
	///</summary>
	THOST_FTDC_ESPI_DceComMarginType = (byte)'B',
	/// <summary>
	/// 郑商所组合持仓保证金收取方式
	///</summary>
	THOST_FTDC_ESPI_CZCEComMarginType = (byte)'A',
	/// <summary>
	/// 投资者交割手续费收取方式
	///</summary>
	THOST_FTDC_ESPI_DelivFeeMode = (byte)'0',
	/// <summary>
	/// 交易所交割手续费收取方式
	///</summary>
	THOST_FTDC_ESPI_ExchDelivFeeMode = (byte)'9',
	/// <summary>
	/// 郑商所结算方式
	///</summary>
	THOST_FTDC_ESPI_CZCESettlementType = (byte)'7',
	/// <summary>
	/// 中金所开户最低可用金额
	///</summary>
	THOST_FTDC_ESPI_CFFEXMinPrepa = (byte)'6',
	/// <summary>
	/// 分项资金入交易所出入金
	///</summary>
	THOST_FTDC_ESPI_OtherFundImport = (byte)'3',
	/// <summary>
	/// 分项资金导入项
	///</summary>
	THOST_FTDC_ESPI_OtherFundItem = (byte)'2',
	/// <summary>
	/// 质押比例
	///</summary>
	THOST_FTDC_ESPI_MortgageRatio = (byte)'1',
}

/// <summary>
/// 系统参数代码类型
///</summary>
public enum TThostFtdcSystemParamIDType : byte
{
	/// <summary>
	/// 郑商所是否开放所有品种套保交易
	///</summary>
	THOST_FTDC_SPI_CZCENormalProductHedge = (byte)'B',
	/// <summary>
	/// 是否规范用户才能休眠
	///</summary>
	THOST_FTDC_SPI_IsStandardFreeze = (byte)'X',
	/// <summary>
	/// 解除开仓权限限制
	///</summary>
	THOST_FTDC_SPI_RelieveOpenLimit = (byte)'O',
	/// <summary>
	/// 手续费相关操作实时上场开关
	///</summary>
	THOST_FTDC_SPI_IsSync = (byte)'A',
	/// <summary>
	/// 休眠户最高权益
	///</summary>
	THOST_FTDC_SPI_FreezeMaxReMain = (byte)'r',
	/// <summary>
	/// 投资者代码编码方式
	///</summary>
	THOST_FTDC_SPI_InvestorIDType = (byte)'a',
	/// <summary>
	/// 投资者中金所结算文件下载路径
	///</summary>
	THOST_FTDC_SPI_CFFEXInvestorSettleFile = (byte)'F',
	/// <summary>
	/// 开户密码录入方式
	///</summary>
	THOST_FTDC_SPI_InvestorPwdModel = (byte)'I',
	/// <summary>
	/// 全结经纪公司上传文件路径
	///</summary>
	THOST_FTDC_SPI_CSRCData = (byte)'R',
	/// <summary>
	/// 投资者照片路径
	///</summary>
	THOST_FTDC_SPI_InvestorPhoto = (byte)'P',
	/// <summary>
	/// 证监会文件标识
	///</summary>
	THOST_FTDC_SPI_CSRCOthersFile = (byte)'C',
	/// <summary>
	/// 生成的结算单文件路径
	///</summary>
	THOST_FTDC_SPI_SettlementBillFile = (byte)'S',
	/// <summary>
	/// 上报保证金监控中心文件路径
	///</summary>
	THOST_FTDC_SPI_DownloadCSRCFile = (byte)'D',
	/// <summary>
	/// 上传的交易所结算文件路径
	///</summary>
	THOST_FTDC_SPI_UploadSettlementFile = (byte)'U',
	/// <summary>
	/// 是否规范用户才能激活
	///</summary>
	THOST_FTDC_SPI_IsStandardActive = (byte)'8',
	/// <summary>
	/// 是否启用保证金率模板数据权限
	///</summary>
	THOST_FTDC_SPI_MarginModelRight = (byte)'9',
	/// <summary>
	/// 是否启用手续费模板数据权限
	///</summary>
	THOST_FTDC_SPI_CommModelRight = (byte)'7',
	/// <summary>
	/// 结算是否判断存在未复核的出入金和分项资金
	///</summary>
	THOST_FTDC_SPI_CheckFund = (byte)'6',
	/// <summary>
	/// 统一开户更新交易编码方式
	///</summary>
	THOST_FTDC_SPI_TradingCode = (byte)'5',
	/// <summary>
	/// 投资者交易结算单成交汇总方式
	///</summary>
	THOST_FTDC_SPI_SettlementBillTrade = (byte)'4',
	/// <summary>
	/// 投资者开户默认登录权限
	///</summary>
	THOST_FTDC_SPI_UserRightLogon = (byte)'3',
	/// <summary>
	/// 投资者帐号代码最小长度
	///</summary>
	THOST_FTDC_SPI_AccountIDMinLength = (byte)'2',
	/// <summary>
	/// 投资者代码最小长度
	///</summary>
	THOST_FTDC_SPI_InvestorIDMinLength = (byte)'1',
}

/// <summary>
/// 交易系统参数代码类型
///</summary>
public enum TThostFtdcTradeParamIDType : byte
{
	/// <summary>
	/// 密码有效期
	///</summary>
	THOST_FTDC_TPID_PasswordPeriod = (byte)'V',
	/// <summary>
	/// IP当日最大登陆失败次数
	///</summary>
	THOST_FTDC_TPID_LoginFailMaxNumForIP = (byte)'U',
	/// <summary>
	/// 最小密码长度
	///</summary>
	THOST_FTDC_TPID_MinPwdLen = (byte)'O',
	/// <summary>
	/// 自有资金质押比
	///</summary>
	THOST_FTDC_TPID_BalanceMorgage = (byte)'a',
	/// <summary>
	/// 强密码校验
	///</summary>
	THOST_FTDC_TPID_IsStrongPassword = (byte)'K',
	/// <summary>
	/// 弱密码最后修改日期
	///</summary>
	THOST_FTDC_TPID_PasswordDeadLine = (byte)'J',
	/// <summary>
	/// 银期开户是否验证开户银行卡号是否是预留银行账户
	///</summary>
	THOST_FTDC_TPID_IsCheckBankAcc = (byte)'I',
	/// <summary>
	/// 行权冻结是否计算盈利
	///</summary>
	THOST_FTDC_TPID_IsExecOrderProfit = (byte)'H',
	/// <summary>
	/// 是否期货下单频率限制
	///</summary>
	THOST_FTDC_TPID_IsFutureOrderFreq = (byte)'C',
	/// <summary>
	/// 是否期货限仓
	///</summary>
	THOST_FTDC_TPID_IsFuturePosiLimit = (byte)'B',
	/// <summary>
	/// 郑商所询价时间间隔
	///</summary>
	THOST_FTDC_TPID_ForQuoteTimeInterval = (byte)'Q',
	/// <summary>
	/// 是否限仓
	///</summary>
	THOST_FTDC_TPID_IsPosiLimit = (byte)'M',
	/// <summary>
	/// 是否冻结证券持仓
	///</summary>
	THOST_FTDC_TPID_IsPosiFreeze = (byte)'F',
	/// <summary>
	/// 是否强制认证
	///</summary>
	THOST_FTDC_TPID_IsAuthForce = (byte)'A',
	/// <summary>
	/// 最大连续登录失败数
	///</summary>
	THOST_FTDC_TPID_LoginFailMaxNum = (byte)'L',
	/// <summary>
	/// 用户最大会话数
	///</summary>
	THOST_FTDC_TPID_SingleUserSessionMaxNum = (byte)'S',
	/// <summary>
	/// 价格小数位数参数
	///</summary>
	THOST_FTDC_TPID_tickMode = (byte)'T',
	/// <summary>
	/// 密码加密算法
	///</summary>
	THOST_FTDC_TPID_modeEncode = (byte)'P',
	/// <summary>
	/// 系统风险算法是否全局 0-否 1-是
	///</summary>
	THOST_FTDC_TPID_RiskModeGlobal = (byte)'G',
	/// <summary>
	/// 系统风险算法
	///</summary>
	THOST_FTDC_TPID_RiskMode = (byte)'R',
	/// <summary>
	/// 系统加密算法
	///</summary>
	THOST_FTDC_TPID_EncryptionStandard = (byte)'E',
}

/// <summary>
/// 文件标识类型
///</summary>
public enum TThostFtdcFileIDType : byte
{
	/// <summary>
	/// 上期所非持仓变动明细
	///</summary>
	THOST_FTDC_FI_NonTradePosChange = (byte)'B',
	/// <summary>
	/// 结算价比对文件
	///</summary>
	THOST_FTDC_FI_SettlementPriceComparison = (byte)'M',
	/// <summary>
	/// 期权执行文件
	///</summary>
	THOST_FTDC_FI_OptionStrike = (byte)'S',
	/// <summary>
	/// 持仓明细数据
	///</summary>
	THOST_FTDC_FI_PositionDtl = (byte)'D',
	/// <summary>
	/// 郑商所非平仓了结数据
	///</summary>
	THOST_FTDC_FI_CZCENoClose = (byte)'N',
	/// <summary>
	/// 郑商所平仓了结数据
	///</summary>
	THOST_FTDC_FI_CZCEClose = (byte)'L',
	/// <summary>
	/// 上报保证金监控中心数据
	///</summary>
	THOST_FTDC_FI_CSRCData = (byte)'R',
	/// <summary>
	/// 组合持仓数据
	///</summary>
	THOST_FTDC_FI_CZCECombinationPos = (byte)'C',
	/// <summary>
	/// 投资者分项资金数据
	///</summary>
	THOST_FTDC_FI_SubEntryFund = (byte)'O',
	/// <summary>
	/// 投资者持仓数据
	///</summary>
	THOST_FTDC_FI_InvestorPosition = (byte)'P',
	/// <summary>
	/// 成交数据
	///</summary>
	THOST_FTDC_FI_Trade = (byte)'T',
	/// <summary>
	/// 资金数据
	///</summary>
	THOST_FTDC_FI_SettlementFund = (byte)'F',
}

/// <summary>
/// 文件上传类型类型
///</summary>
public enum TThostFtdcFileTypeType : byte
{
	/// <summary>
	/// 核对
	///</summary>
	THOST_FTDC_FUT_Check = (byte)'1',
	/// <summary>
	/// 结算
	///</summary>
	THOST_FTDC_FUT_Settlement = (byte)'0',
}

/// <summary>
/// 文件格式类型
///</summary>
public enum TThostFtdcFileFormatType : byte
{
	/// <summary>
	/// DBF文件(.dbf)
	///</summary>
	THOST_FTDC_FFT_DBF = (byte)'2',
	/// <summary>
	/// 压缩文件(.zip)
	///</summary>
	THOST_FTDC_FFT_Zip = (byte)'1',
	/// <summary>
	/// 文本文件(.txt)
	///</summary>
	THOST_FTDC_FFT_Txt = (byte)'0',
}

/// <summary>
/// 文件状态类型
///</summary>
public enum TThostFtdcFileUploadStatusType : byte
{
	/// <summary>
	/// 导入失败
	///</summary>
	THOST_FTDC_FUS_FailedLoad = (byte)'5',
	/// <summary>
	/// 导入部分成功
	///</summary>
	THOST_FTDC_FUS_PartSucceedLoad = (byte)'4',
	/// <summary>
	/// 导入成功
	///</summary>
	THOST_FTDC_FUS_SucceedLoad = (byte)'3',
	/// <summary>
	/// 上传失败
	///</summary>
	THOST_FTDC_FUS_FailedUpload = (byte)'2',
	/// <summary>
	/// 上传成功
	///</summary>
	THOST_FTDC_FUS_SucceedUpload = (byte)'1',
}

/// <summary>
/// 移仓方向类型
///</summary>
public enum TThostFtdcTransferDirectionType : byte
{
	/// <summary>
	/// 移入
	///</summary>
	THOST_FTDC_TD_In = (byte)'1',
	/// <summary>
	/// 移出
	///</summary>
	THOST_FTDC_TD_Out = (byte)'0',
}

/// <summary>
/// 特殊的创建规则类型
///</summary>
public enum TThostFtdcSpecialCreateRuleType : byte
{
	/// <summary>
	/// 不包含春节
	///</summary>
	THOST_FTDC_SC_NoSpringFestival = (byte)'1',
	/// <summary>
	/// 没有特殊创建规则
	///</summary>
	THOST_FTDC_SC_NoSpecialRule = (byte)'0',
}

/// <summary>
/// 挂牌基准价类型类型
///</summary>
public enum TThostFtdcBasisPriceTypeType : byte
{
	/// <summary>
	/// 上一合约收盘价
	///</summary>
	THOST_FTDC_IPT_LaseClose = (byte)'2',
	/// <summary>
	/// 上一合约结算价
	///</summary>
	THOST_FTDC_IPT_LastSettlement = (byte)'1',
}

/// <summary>
/// 产品生命周期状态类型
///</summary>
public enum TThostFtdcProductLifePhaseType : byte
{
	/// <summary>
	/// 注销
	///</summary>
	THOST_FTDC_PLP_Canceled = (byte)'3',
	/// <summary>
	/// 不活跃
	///</summary>
	THOST_FTDC_PLP_NonActive = (byte)'2',
	/// <summary>
	/// 活跃
	///</summary>
	THOST_FTDC_PLP_Active = (byte)'1',
}

/// <summary>
/// 交割方式类型
///</summary>
public enum TThostFtdcDeliveryModeType : byte
{
	/// <summary>
	/// 实物交割
	///</summary>
	THOST_FTDC_DM_CommodityDeliv = (byte)'2',
	/// <summary>
	/// 现金交割
	///</summary>
	THOST_FTDC_DM_CashDeliv = (byte)'1',
}

/// <summary>
/// 出入金类型类型
///</summary>
public enum TThostFtdcFundIOTypeType : byte
{
	/// <summary>
	/// 银期换汇
	///</summary>
	THOST_FTDC_FIOT_SwapCurrency = (byte)'3',
	/// <summary>
	/// 银期转帐
	///</summary>
	THOST_FTDC_FIOT_Transfer = (byte)'2',
	/// <summary>
	/// 出入金
	///</summary>
	THOST_FTDC_FIOT_FundIO = (byte)'1',
}

/// <summary>
/// 资金类型类型
///</summary>
public enum TThostFtdcFundTypeType : byte
{
	/// <summary>
	/// 资金内转
	///</summary>
	THOST_FTDC_FT_InnerTransfer = (byte)'4',
	/// <summary>
	/// 公司调整
	///</summary>
	THOST_FTDC_FT_Company = (byte)'3',
	/// <summary>
	/// 分项资金
	///</summary>
	THOST_FTDC_FT_ItemFund = (byte)'2',
	/// <summary>
	/// 银行存款
	///</summary>
	THOST_FTDC_FT_Deposite = (byte)'1',
}

/// <summary>
/// 出入金方向类型
///</summary>
public enum TThostFtdcFundDirectionType : byte
{
	/// <summary>
	/// 出金
	///</summary>
	THOST_FTDC_FD_Out = (byte)'2',
	/// <summary>
	/// 入金
	///</summary>
	THOST_FTDC_FD_In = (byte)'1',
}

/// <summary>
/// 资金状态类型
///</summary>
public enum TThostFtdcFundStatusType : byte
{
	/// <summary>
	/// 已冲销
	///</summary>
	THOST_FTDC_FS_Charge = (byte)'3',
	/// <summary>
	/// 已复核
	///</summary>
	THOST_FTDC_FS_Check = (byte)'2',
	/// <summary>
	/// 已录入
	///</summary>
	THOST_FTDC_FS_Record = (byte)'1',
}

/// <summary>
/// 发布状态类型
///</summary>
public enum TThostFtdcPublishStatusType : byte
{
	/// <summary>
	/// 已发布
	///</summary>
	THOST_FTDC_PS_Published = (byte)'3',
	/// <summary>
	/// 正在发布
	///</summary>
	THOST_FTDC_PS_Publishing = (byte)'2',
	/// <summary>
	/// 未发布
	///</summary>
	THOST_FTDC_PS_None = (byte)'1',
}

/// <summary>
/// 系统状态类型
///</summary>
public enum TThostFtdcSystemStatusType : byte
{
	/// <summary>
	/// 结算
	///</summary>
	THOST_FTDC_ES_Settlement = (byte)'7',
	/// <summary>
	/// 收市完成
	///</summary>
	THOST_FTDC_ES_Closed = (byte)'6',
	/// <summary>
	/// 收市开始
	///</summary>
	THOST_FTDC_ES_Close = (byte)'5',
	/// <summary>
	/// 交易完成初始化
	///</summary>
	THOST_FTDC_ES_Initialized = (byte)'4',
	/// <summary>
	/// 交易开始初始化
	///</summary>
	THOST_FTDC_ES_Initialize = (byte)'3',
	/// <summary>
	/// 启动
	///</summary>
	THOST_FTDC_ES_Startup = (byte)'2',
	/// <summary>
	/// 不活跃
	///</summary>
	THOST_FTDC_ES_NonActive = (byte)'1',
}

/// <summary>
/// 结算状态类型
///</summary>
public enum TThostFtdcSettlementStatusType : byte
{
	/// <summary>
	/// 结算完成
	///</summary>
	THOST_FTDC_STS_Finished = (byte)'3',
	/// <summary>
	/// 已结算
	///</summary>
	THOST_FTDC_STS_Settlemented = (byte)'2',
	/// <summary>
	/// 结算中
	///</summary>
	THOST_FTDC_STS_Settlementing = (byte)'1',
	/// <summary>
	/// 初始
	///</summary>
	THOST_FTDC_STS_Initialize = (byte)'0',
}

/// <summary>
/// 投资者类型类型
///</summary>
public enum TThostFtdcInvestorTypeType : byte
{
	/// <summary>
	/// 资管户
	///</summary>
	THOST_FTDC_CT_Asset = (byte)'4',
	/// <summary>
	/// 特殊法人
	///</summary>
	THOST_FTDC_CT_SpecialOrgan = (byte)'3',
	/// <summary>
	/// 投资基金
	///</summary>
	THOST_FTDC_CT_Fund = (byte)'2',
	/// <summary>
	/// 法人
	///</summary>
	THOST_FTDC_CT_Company = (byte)'1',
	/// <summary>
	/// 自然人
	///</summary>
	THOST_FTDC_CT_Person = (byte)'0',
}

/// <summary>
/// 经纪公司类型类型
///</summary>
public enum TThostFtdcBrokerTypeType : byte
{
	/// <summary>
	/// 交易结算会员
	///</summary>
	THOST_FTDC_BT_TradeSettle = (byte)'1',
	/// <summary>
	/// 交易会员
	///</summary>
	THOST_FTDC_BT_Trade = (byte)'0',
}

/// <summary>
/// 风险等级类型
///</summary>
public enum TThostFtdcRiskLevelType : byte
{
	/// <summary>
	/// 风险客户
	///</summary>
	THOST_FTDC_FAS_Risk = (byte)'4',
	/// <summary>
	/// 关注客户
	///</summary>
	THOST_FTDC_FAS_Focus = (byte)'3',
	/// <summary>
	/// 普通客户
	///</summary>
	THOST_FTDC_FAS_Normal = (byte)'2',
	/// <summary>
	/// 低风险客户
	///</summary>
	THOST_FTDC_FAS_Low = (byte)'1',
}

/// <summary>
/// 手续费收取方式类型
///</summary>
public enum TThostFtdcFeeAcceptStyleType : byte
{
	/// <summary>
	/// 按指定手续费收取
	///</summary>
	THOST_FTDC_FAS_FixFee = (byte)'4',
	/// <summary>
	/// 不收
	///</summary>
	THOST_FTDC_FAS_None = (byte)'3',
	/// <summary>
	/// 按交割收取
	///</summary>
	THOST_FTDC_FAS_ByDeliv = (byte)'2',
	/// <summary>
	/// 按交易收取
	///</summary>
	THOST_FTDC_FAS_ByTrade = (byte)'1',
}

/// <summary>
/// 密码类型类型
///</summary>
public enum TThostFtdcPasswordTypeType : byte
{
	/// <summary>
	/// 资金密码
	///</summary>
	THOST_FTDC_PWDT_Account = (byte)'2',
	/// <summary>
	/// 交易密码
	///</summary>
	THOST_FTDC_PWDT_Trade = (byte)'1',
}

/// <summary>
/// 盈亏算法类型
///</summary>
public enum TThostFtdcAlgorithmType : byte
{
	/// <summary>
	/// 浮盈浮亏都不计算
	///</summary>
	THOST_FTDC_AG_None = (byte)'4',
	/// <summary>
	/// 浮盈计，浮亏不计
	///</summary>
	THOST_FTDC_AG_OnlyGain = (byte)'3',
	/// <summary>
	/// 浮盈不计，浮亏计
	///</summary>
	THOST_FTDC_AG_OnlyLost = (byte)'2',
	/// <summary>
	/// 浮盈浮亏都计算
	///</summary>
	THOST_FTDC_AG_All = (byte)'1',
}

/// <summary>
/// 是否包含平仓盈利类型
///</summary>
public enum TThostFtdcIncludeCloseProfitType : byte
{
	/// <summary>
	/// 不包含平仓盈利
	///</summary>
	THOST_FTDC_ICP_NotInclude = (byte)'2',
	/// <summary>
	/// 包含平仓盈利
	///</summary>
	THOST_FTDC_ICP_Include = (byte)'0',
}

/// <summary>
/// 是否受可提比例限制类型
///</summary>
public enum TThostFtdcAllWithoutTradeType : byte
{
	/// <summary>
	/// 无仓不受可提比例限制
	///</summary>
	THOST_FTDC_AWT_NoHoldEnable = (byte)'3',
	/// <summary>
	/// 受可提比例限制
	///</summary>
	THOST_FTDC_AWT_Disable = (byte)'2',
	/// <summary>
	/// 无仓无成交不受可提比例限制
	///</summary>
	THOST_FTDC_AWT_Enable = (byte)'0',
}

/// <summary>
/// 资金密码核对标志类型
///</summary>
public enum TThostFtdcFuturePwdFlagType : byte
{
	/// <summary>
	/// 核对
	///</summary>
	THOST_FTDC_FPWD_Check = (byte)'1',
	/// <summary>
	/// 不核对
	///</summary>
	THOST_FTDC_FPWD_UnCheck = (byte)'0',
}

/// <summary>
/// 银期转账类型类型
///</summary>
public enum TThostFtdcTransferTypeType : byte
{
	/// <summary>
	/// 期货转银行
	///</summary>
	THOST_FTDC_TT_FutureToBank = (byte)'1',
	/// <summary>
	/// 银行转期货
	///</summary>
	THOST_FTDC_TT_BankToFuture = (byte)'0',
}

/// <summary>
/// 转账有效标志类型
///</summary>
public enum TThostFtdcTransferValidFlagType : byte
{
	/// <summary>
	/// 冲正
	///</summary>
	THOST_FTDC_TVF_Reverse = (byte)'2',
	/// <summary>
	/// 有效
	///</summary>
	THOST_FTDC_TVF_Valid = (byte)'1',
	/// <summary>
	/// 无效或失败
	///</summary>
	THOST_FTDC_TVF_Invalid = (byte)'0',
}

/// <summary>
/// 事由类型
///</summary>
public enum TThostFtdcReasonType : byte
{
	/// <summary>
	/// 其它
	///</summary>
	THOST_FTDC_RN_QT = (byte)'2',
	/// <summary>
	/// 资金在途
	///</summary>
	THOST_FTDC_RN_ZT = (byte)'1',
	/// <summary>
	/// 错单
	///</summary>
	THOST_FTDC_RN_CD = (byte)'0',
}

/// <summary>
/// 性别类型
///</summary>
public enum TThostFtdcSexType : byte
{
	/// <summary>
	/// 女
	///</summary>
	THOST_FTDC_SEX_Woman = (byte)'2',
	/// <summary>
	/// 男
	///</summary>
	THOST_FTDC_SEX_Man = (byte)'1',
	/// <summary>
	/// 未知
	///</summary>
	THOST_FTDC_SEX_None = (byte)'0',
}

/// <summary>
/// 用户类型类型
///</summary>
public enum TThostFtdcUserTypeType : byte
{
	/// <summary>
	/// 管理员
	///</summary>
	THOST_FTDC_UT_SuperUser = (byte)'2',
	/// <summary>
	/// 操作员
	///</summary>
	THOST_FTDC_UT_Operator = (byte)'1',
	/// <summary>
	/// 投资者
	///</summary>
	THOST_FTDC_UT_Investor = (byte)'0',
}

/// <summary>
/// 费率类型类型
///</summary>
public enum TThostFtdcRateTypeType : byte
{
	/// <summary>
	/// 保证金率
	///</summary>
	THOST_FTDC_RATETYPE_MarginRate = (byte)'2',
}

/// <summary>
/// 通知类型类型
///</summary>
public enum TThostFtdcNoteTypeType : byte
{
	/// <summary>
	/// 交割通知书
	///</summary>
	THOST_FTDC_NOTETYPE_DelivNotes = (byte)'6',
	/// <summary>
	/// 成交通知书
	///</summary>
	THOST_FTDC_NOTETYPE_TradeNotes = (byte)'5',
	/// <summary>
	/// 强行平仓通知书
	///</summary>
	THOST_FTDC_NOTETYPE_ForceCloseNotes = (byte)'4',
	/// <summary>
	/// 追加保证金通知书
	///</summary>
	THOST_FTDC_NOTETYPE_CallMarginNotes = (byte)'3',
	/// <summary>
	/// 交易结算月报
	///</summary>
	THOST_FTDC_NOTETYPE_TradeSettleMonth = (byte)'2',
	/// <summary>
	/// 交易结算单
	///</summary>
	THOST_FTDC_NOTETYPE_TradeSettleBill = (byte)'1',
}

/// <summary>
/// 结算单方式类型
///</summary>
public enum TThostFtdcSettlementStyleType : byte
{
	/// <summary>
	/// 逐笔对冲
	///</summary>
	THOST_FTDC_SBS_Volume = (byte)'2',
	/// <summary>
	/// 逐日盯市
	///</summary>
	THOST_FTDC_SBS_Day = (byte)'1',
}

/// <summary>
/// 结算单类型类型
///</summary>
public enum TThostFtdcSettlementBillTypeType : byte
{
	/// <summary>
	/// 月报
	///</summary>
	THOST_FTDC_ST_Month = (byte)'1',
	/// <summary>
	/// 日报
	///</summary>
	THOST_FTDC_ST_Day = (byte)'0',
}

/// <summary>
/// 客户权限类型类型
///</summary>
public enum TThostFtdcUserRightTypeType : byte
{
	/// <summary>
	/// 条件单
	///</summary>
	THOST_FTDC_URT_ConditionOrder = (byte)'5',
	/// <summary>
	/// 传真结算单
	///</summary>
	THOST_FTDC_URT_Fax = (byte)'4',
	/// <summary>
	/// 邮寄结算单
	///</summary>
	THOST_FTDC_URT_EMail = (byte)'3',
	/// <summary>
	/// 银期转帐
	///</summary>
	THOST_FTDC_URT_Transfer = (byte)'2',
	/// <summary>
	/// 登录
	///</summary>
	THOST_FTDC_URT_Logon = (byte)'1',
}

/// <summary>
/// 保证金价格类型类型
///</summary>
public enum TThostFtdcMarginPriceTypeType : byte
{
	/// <summary>
	/// 开仓价
	///</summary>
	THOST_FTDC_MPT_OpenPrice = (byte)'4',
	/// <summary>
	/// 成交均价
	///</summary>
	THOST_FTDC_MPT_AveragePrice = (byte)'3',
	/// <summary>
	/// 最新价
	///</summary>
	THOST_FTDC_MPT_SettlementPrice = (byte)'2',
	/// <summary>
	/// 昨结算价
	///</summary>
	THOST_FTDC_MPT_PreSettlementPrice = (byte)'1',
}

/// <summary>
/// 结算单生成状态类型
///</summary>
public enum TThostFtdcBillGenStatusType : byte
{
	/// <summary>
	/// 已生成
	///</summary>
	THOST_FTDC_BGS_Generated = (byte)'2',
	/// <summary>
	/// 生成中
	///</summary>
	THOST_FTDC_BGS_NoGenerated = (byte)'1',
	/// <summary>
	/// 未生成
	///</summary>
	THOST_FTDC_BGS_None = (byte)'0',
}

/// <summary>
/// 算法类型类型
///</summary>
public enum TThostFtdcAlgoTypeType : byte
{
	/// <summary>
	/// 寻找保证金率算法
	///</summary>
	THOST_FTDC_AT_FindMarginRateAlgo = (byte)'2',
	/// <summary>
	/// 持仓处理算法
	///</summary>
	THOST_FTDC_AT_HandlePositionAlgo = (byte)'1',
}

/// <summary>
/// 持仓处理算法编号类型
///</summary>
public enum TThostFtdcHandlePositionAlgoIDType : byte
{
	/// <summary>
	/// 郑州商品交易所
	///</summary>
	THOST_FTDC_HPA_CZCE = (byte)'3',
	/// <summary>
	/// 大连商品交易所
	///</summary>
	THOST_FTDC_HPA_DCE = (byte)'2',
	/// <summary>
	/// 基本
	///</summary>
	THOST_FTDC_HPA_Base = (byte)'1',
}

/// <summary>
/// 寻找保证金率算法编号类型
///</summary>
public enum TThostFtdcFindMarginRateAlgoIDType : byte
{
	/// <summary>
	/// 郑州商品交易所
	///</summary>
	THOST_FTDC_FMRA_CZCE = (byte)'3',
	/// <summary>
	/// 大连商品交易所
	///</summary>
	THOST_FTDC_FMRA_DCE = (byte)'2',
	/// <summary>
	/// 基本
	///</summary>
	THOST_FTDC_FMRA_Base = (byte)'1',
}

/// <summary>
/// 资金处理算法编号类型
///</summary>
public enum TThostFtdcHandleTradingAccountAlgoIDType : byte
{
	/// <summary>
	/// 郑州商品交易所
	///</summary>
	THOST_FTDC_HTAA_CZCE = (byte)'3',
	/// <summary>
	/// 大连商品交易所
	///</summary>
	THOST_FTDC_HTAA_DCE = (byte)'2',
	/// <summary>
	/// 基本
	///</summary>
	THOST_FTDC_HTAA_Base = (byte)'1',
}

/// <summary>
/// 联系人类型类型
///</summary>
public enum TThostFtdcPersonTypeType : byte
{
	/// <summary>
	/// 法人代表参考证件
	///</summary>
	THOST_FTDC_PST_CorporationRefer = (byte)'E',
	/// <summary>
	/// 境外自然人参考证件
	///</summary>
	THOST_FTDC_PST_ForeignerRefer = (byte)'D',
	/// <summary>
	/// 托（保）管机构联系人
	///</summary>
	THOST_FTDC_PST_TrusteeContact = (byte)'C',
	/// <summary>
	/// 托（保）管机构开户授权人
	///</summary>
	THOST_FTDC_PST_TrusteeOpen = (byte)'B',
	/// <summary>
	/// 托（保）管机构法人代表
	///</summary>
	THOST_FTDC_PST_TrusteeCorporation = (byte)'A',
	/// <summary>
	/// 托（保）管人
	///</summary>
	THOST_FTDC_PST_Trustee = (byte)'9',
	/// <summary>
	/// 分户管理资产负责人
	///</summary>
	THOST_FTDC_PST_Ledger = (byte)'8',
	/// <summary>
	/// 投资者联系人
	///</summary>
	THOST_FTDC_PST_LinkMan = (byte)'7',
	/// <summary>
	/// 法人代表
	///</summary>
	THOST_FTDC_PST_Corporation = (byte)'6',
	/// <summary>
	/// 法人
	///</summary>
	THOST_FTDC_PST_Company = (byte)'5',
	/// <summary>
	/// 结算单确认人
	///</summary>
	THOST_FTDC_PST_Settlement = (byte)'4',
	/// <summary>
	/// 资金调拨人
	///</summary>
	THOST_FTDC_PST_Fund = (byte)'3',
	/// <summary>
	/// 开户授权人
	///</summary>
	THOST_FTDC_PST_Open = (byte)'2',
	/// <summary>
	/// 指定下单人
	///</summary>
	THOST_FTDC_PST_Order = (byte)'1',
}

/// <summary>
/// 查询范围类型
///</summary>
public enum TThostFtdcQueryInvestorRangeType : byte
{
	/// <summary>
	/// 单一投资者
	///</summary>
	THOST_FTDC_QIR_Single = (byte)'3',
	/// <summary>
	/// 查询分类
	///</summary>
	THOST_FTDC_QIR_Group = (byte)'2',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_QIR_All = (byte)'1',
}

/// <summary>
/// 投资者风险状态类型
///</summary>
public enum TThostFtdcInvestorRiskStatusType : byte
{
	/// <summary>
	/// 异常
	///</summary>
	THOST_FTDC_IRS_Exception = (byte)'5',
	/// <summary>
	/// 强平
	///</summary>
	THOST_FTDC_IRS_Force = (byte)'4',
	/// <summary>
	/// 追保
	///</summary>
	THOST_FTDC_IRS_Call = (byte)'3',
	/// <summary>
	/// 警告
	///</summary>
	THOST_FTDC_IRS_Warn = (byte)'2',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_IRS_Normal = (byte)'1',
}

/// <summary>
/// 用户事件类型类型
///</summary>
public enum TThostFtdcUserEventTypeType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_UET_Other = (byte)'9',
	/// <summary>
	/// 客户端认证
	///</summary>
	THOST_FTDC_UET_Authenticate = (byte)'6',
	/// <summary>
	/// 修改密码
	///</summary>
	THOST_FTDC_UET_UpdatePassword = (byte)'5',
	/// <summary>
	/// 交易失败
	///</summary>
	THOST_FTDC_UET_TradingError = (byte)'4',
	/// <summary>
	/// 交易成功
	///</summary>
	THOST_FTDC_UET_Trading = (byte)'3',
	/// <summary>
	/// 登出
	///</summary>
	THOST_FTDC_UET_Logout = (byte)'2',
	/// <summary>
	/// 登录
	///</summary>
	THOST_FTDC_UET_Login = (byte)'1',
}

/// <summary>
/// 平仓方式类型
///</summary>
public enum TThostFtdcCloseStyleType : byte
{
	/// <summary>
	/// 先平今再平昨
	///</summary>
	THOST_FTDC_ICS_CloseToday = (byte)'1',
	/// <summary>
	/// 先开先平
	///</summary>
	THOST_FTDC_ICS_Close = (byte)'0',
}

/// <summary>
/// 统计方式类型
///</summary>
public enum TThostFtdcStatModeType : byte
{
	/// <summary>
	/// 按投资者统计
	///</summary>
	THOST_FTDC_SM_Investor = (byte)'3',
	/// <summary>
	/// 按产品统计
	///</summary>
	THOST_FTDC_SM_Product = (byte)'2',
	/// <summary>
	/// 按合约统计
	///</summary>
	THOST_FTDC_SM_Instrument = (byte)'1',
	/// <summary>
	/// ----
	///</summary>
	THOST_FTDC_SM_Non = (byte)'0',
}

/// <summary>
/// 预埋单状态类型
///</summary>
public enum TThostFtdcParkedOrderStatusType : byte
{
	/// <summary>
	/// 已删除
	///</summary>
	THOST_FTDC_PAOS_Deleted = (byte)'3',
	/// <summary>
	/// 已发送
	///</summary>
	THOST_FTDC_PAOS_Send = (byte)'2',
	/// <summary>
	/// 未发送
	///</summary>
	THOST_FTDC_PAOS_NotSend = (byte)'1',
}

/// <summary>
/// 处理状态类型
///</summary>
public enum TThostFtdcVirDealStatusType : byte
{
	/// <summary>
	/// 处理成功
	///</summary>
	THOST_FTDC_VDS_DeaclSucceed = (byte)'2',
	/// <summary>
	/// 正在处理
	///</summary>
	THOST_FTDC_VDS_Dealing = (byte)'1',
}

/// <summary>
/// 原有系统代码类型
///</summary>
public enum TThostFtdcOrgSystemIDType : byte
{
	/// <summary>
	/// 金仕达V6系统
	///</summary>
	THOST_FTDC_ORGS_KingStarV6 = (byte)'2',
	/// <summary>
	/// 易盛系统
	///</summary>
	THOST_FTDC_ORGS_ESunny = (byte)'1',
	/// <summary>
	/// 综合交易平台
	///</summary>
	THOST_FTDC_ORGS_Standard = (byte)'0',
}

/// <summary>
/// 交易状态类型
///</summary>
public enum TThostFtdcVirTradeStatusType : byte
{
	/// <summary>
	/// 系统出错，请人工处理
	///</summary>
	THOST_FTDC_VTS_SysException = (byte)'6',
	/// <summary>
	/// 通讯异常 ，请人工处理
	///</summary>
	THOST_FTDC_VTS_MesException = (byte)'5',
	/// <summary>
	/// 已人工异常处理
	///</summary>
	THOST_FTDC_VTS_ManualDeal = (byte)'4',
	/// <summary>
	/// 异常中
	///</summary>
	THOST_FTDC_VTS_Exception = (byte)'3',
	/// <summary>
	/// 失败结束
	///</summary>
	THOST_FTDC_VTS_FailedEND = (byte)'2',
	/// <summary>
	/// 成功结束
	///</summary>
	THOST_FTDC_VTS_SucceedEnd = (byte)'1',
	/// <summary>
	/// 正常处理中
	///</summary>
	THOST_FTDC_VTS_NaturalDeal = (byte)'0',
}

/// <summary>
/// 银行帐户类型类型
///</summary>
public enum TThostFtdcVirBankAccTypeType : byte
{
	/// <summary>
	/// 信用卡
	///</summary>
	THOST_FTDC_VBAT_CreditCard = (byte)'3',
	/// <summary>
	/// 储蓄卡
	///</summary>
	THOST_FTDC_VBAT_BankCard = (byte)'2',
	/// <summary>
	/// 存折
	///</summary>
	THOST_FTDC_VBAT_BankBook = (byte)'1',
}

/// <summary>
/// 银行帐户类型类型
///</summary>
public enum TThostFtdcVirementStatusType : byte
{
	/// <summary>
	/// 销户
	///</summary>
	THOST_FTDC_VMS_Canceled = (byte)'9',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_VMS_Natural = (byte)'0',
}

/// <summary>
/// 有效标志类型
///</summary>
public enum TThostFtdcVirementAvailAbilityType : byte
{
	/// <summary>
	/// 冲正
	///</summary>
	THOST_FTDC_VAA_Repeal = (byte)'2',
	/// <summary>
	/// 有效
	///</summary>
	THOST_FTDC_VAA_AvailAbility = (byte)'1',
	/// <summary>
	/// 未确认
	///</summary>
	THOST_FTDC_VAA_NoAvailAbility = (byte)'0',
}

/// <summary>
/// 交易代码类型
///</summary>
public enum TThostFtdcVirementTradeCodeType : byte
{
	/// <summary>
	/// 期货发起期货资金转银行
	///</summary>
	THOST_FTDC_VTC_FutureFutureToBank = (byte)'2',
	/// <summary>
	/// 期货发起银行资金转期货
	///</summary>
	THOST_FTDC_VTC_FutureBankToFuture = (byte)'1',
	/// <summary>
	/// 银行发起期货资金转银行
	///</summary>
	THOST_FTDC_VTC_BankFutureToBank = (byte)'2',
	/// <summary>
	/// 银行发起银行资金转期货
	///</summary>
	THOST_FTDC_VTC_BankBankToFuture = (byte)'1',
}

/// <summary>
/// Aml生成方式类型
///</summary>
public enum TThostFtdcAMLGenStatusType : byte
{
	/// <summary>
	/// 人工生成
	///</summary>
	THOST_FTDC_GEN_HandWork = (byte)'1',
	/// <summary>
	/// 程序生成
	///</summary>
	THOST_FTDC_GEN_Program = (byte)'0',
}

/// <summary>
/// 动态密钥类别(保证金监管)类型
///</summary>
public enum TThostFtdcCFMMCKeyKindType : byte
{
	/// <summary>
	/// CFMMC手动更新
	///</summary>
	THOST_FTDC_CFMMCKK_MANUAL = (byte)'M',
	/// <summary>
	/// CFMMC自动更新
	///</summary>
	THOST_FTDC_CFMMCKK_AUTO = (byte)'A',
	/// <summary>
	/// 主动请求更新
	///</summary>
	THOST_FTDC_CFMMCKK_REQUEST = (byte)'R',
}

/// <summary>
/// 证件类型类型
///</summary>
public enum TThostFtdcCertificationTypeType : byte
{
	/// <summary>
	/// 主管部门批文
	///</summary>
	THOST_FTDC_CFT_SuperDepAgree = (byte)'a',
	/// <summary>
	/// 其他证件
	///</summary>
	THOST_FTDC_CFT_OtherCard = (byte)'x',
	/// <summary>
	/// 民办非企业登记证书
	///</summary>
	THOST_FTDC_CFT_NoEnterpriseLicenseNo = (byte)'9',
	/// <summary>
	/// 临时营业执照号
	///</summary>
	THOST_FTDC_CFT_TempLicenseNo = (byte)'8',
	/// <summary>
	/// 组织机构代码证
	///</summary>
	THOST_FTDC_CFT_InstitutionCodeCard = (byte)'7',
	/// <summary>
	/// 营业执照号
	///</summary>
	THOST_FTDC_CFT_LicenseNo = (byte)'6',
	/// <summary>
	/// 户口簿
	///</summary>
	THOST_FTDC_CFT_HouseholdRegister = (byte)'5',
	/// <summary>
	/// 回乡证
	///</summary>
	THOST_FTDC_CFT_HomeComingCard = (byte)'4',
	/// <summary>
	/// 士兵证
	///</summary>
	THOST_FTDC_CFT_SoldierIDCard = (byte)'3',
	/// <summary>
	/// 军官证
	///</summary>
	THOST_FTDC_CFT_OfficerIDCard = (byte)'2',
	/// <summary>
	/// 护照
	///</summary>
	THOST_FTDC_CFT_Passport = (byte)'1',
	/// <summary>
	/// 身份证
	///</summary>
	THOST_FTDC_CFT_IDCard = (byte)'0',
}

/// <summary>
/// 文件业务功能类型
///</summary>
public enum TThostFtdcFileBusinessCodeType : byte
{
	/// <summary>
	/// 协办存管银行资金监管数据
	///</summary>
	THOST_FTDC_FBC_BankMoneyMonitorData = (byte)'f',
	/// <summary>
	/// 存管银行备付金余额
	///</summary>
	THOST_FTDC_FBC_PreparationMoney = (byte)'e',
	/// <summary>
	/// 总分平衡监管数据
	///</summary>
	THOST_FTDC_FBC_MainPartMonitorData = (byte)'d',
	/// <summary>
	/// 主体间资金交收汇总
	///</summary>
	THOST_FTDC_FBC_MainbodyMoneyTotal = (byte)'c',
	/// <summary>
	/// 法人存管银行资金交收汇总
	///</summary>
	THOST_FTDC_FBC_CorporationMoneyTotal = (byte)'b',
	/// <summary>
	/// 客户资金交收明细
	///</summary>
	THOST_FTDC_FBC_CustMoneySendAndReceiveDetails = (byte)'a',
	/// <summary>
	/// 客户结息净额明细
	///</summary>
	THOST_FTDC_FBC_CustInterestNetMoneyDetails = (byte)'9',
	/// <summary>
	/// 其它对账异常结果文件
	///</summary>
	THOST_FTDC_FBC_OthersExceptionResult = (byte)'8',
	/// <summary>
	/// 客户资金余额对账结果
	///</summary>
	THOST_FTDC_FBC_CustMoneyResult = (byte)'7',
	/// <summary>
	/// 客户销户结息明细对账
	///</summary>
	THOST_FTDC_FBC_CustCancelAccountInfo = (byte)'6',
	/// <summary>
	/// 客户资金台账余额明细对账
	///</summary>
	THOST_FTDC_FBC_CustMoneyDetail = (byte)'5',
	/// <summary>
	/// 期货账户信息变更明细对账
	///</summary>
	THOST_FTDC_FBC_FutureAccountChangeInfoDetails = (byte)'4',
	/// <summary>
	/// 账户类交易明细对账
	///</summary>
	THOST_FTDC_FBC_AccountTradeDetails = (byte)'3',
	/// <summary>
	/// 客户账户状态对账
	///</summary>
	THOST_FTDC_FBC_CustAccStatus = (byte)'2',
	/// <summary>
	/// 转账交易明细对账
	///</summary>
	THOST_FTDC_FBC_TransferDetails = (byte)'1',
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_FBC_Others = (byte)'0',
}

/// <summary>
/// 汇钞标志类型
///</summary>
public enum TThostFtdcCashExchangeCodeType : byte
{
	/// <summary>
	/// 钞
	///</summary>
	THOST_FTDC_CEC_Cash = (byte)'2',
	/// <summary>
	/// 汇
	///</summary>
	THOST_FTDC_CEC_Exchange = (byte)'1',
}

/// <summary>
/// 是或否标识类型
///</summary>
public enum TThostFtdcYesNoIndicatorType : byte
{
	/// <summary>
	/// 否
	///</summary>
	THOST_FTDC_YNI_No = (byte)'1',
	/// <summary>
	/// 是
	///</summary>
	THOST_FTDC_YNI_Yes = (byte)'0',
}

/// <summary>
/// 余额类型类型
///</summary>
public enum TThostFtdcBanlanceTypeType : byte
{
	/// <summary>
	/// 冻结余额
	///</summary>
	THOST_FTDC_BLT_FreezeMoney = (byte)'3',
	/// <summary>
	/// 可取余额
	///</summary>
	THOST_FTDC_BLT_FetchableMoney = (byte)'2',
	/// <summary>
	/// 可用余额
	///</summary>
	THOST_FTDC_BLT_UsableMoney = (byte)'1',
	/// <summary>
	/// 当前余额
	///</summary>
	THOST_FTDC_BLT_CurrentMoney = (byte)'0',
}

/// <summary>
/// 性别类型
///</summary>
public enum TThostFtdcGenderType : byte
{
	/// <summary>
	/// 女
	///</summary>
	THOST_FTDC_GD_Female = (byte)'2',
	/// <summary>
	/// 男
	///</summary>
	THOST_FTDC_GD_Male = (byte)'1',
	/// <summary>
	/// 未知状态
	///</summary>
	THOST_FTDC_GD_Unknown = (byte)'0',
}

/// <summary>
/// 费用支付标志类型
///</summary>
public enum TThostFtdcFeePayFlagType : byte
{
	/// <summary>
	/// 由发送方支付发起的费用，受益方支付接受的费用
	///</summary>
	THOST_FTDC_FPF_SHA = (byte)'2',
	/// <summary>
	/// 由发送方支付费用
	///</summary>
	THOST_FTDC_FPF_OUR = (byte)'1',
	/// <summary>
	/// 由受益方支付费用
	///</summary>
	THOST_FTDC_FPF_BEN = (byte)'0',
}

/// <summary>
/// 密钥类型类型
///</summary>
public enum TThostFtdcPassWordKeyTypeType : byte
{
	/// <summary>
	/// 报文密钥
	///</summary>
	THOST_FTDC_PWKT_MessageKey = (byte)'3',
	/// <summary>
	/// MAC密钥
	///</summary>
	THOST_FTDC_PWKT_MACKey = (byte)'2',
	/// <summary>
	/// 密码密钥
	///</summary>
	THOST_FTDC_PWKT_PassWordKey = (byte)'1',
	/// <summary>
	/// 交换密钥
	///</summary>
	THOST_FTDC_PWKT_ExchangeKey = (byte)'0',
}

/// <summary>
/// 密码类型类型
///</summary>
public enum TThostFtdcFBTPassWordTypeType : byte
{
	/// <summary>
	/// 交易
	///</summary>
	THOST_FTDC_PWT_Trade = (byte)'3',
	/// <summary>
	/// 转帐
	///</summary>
	THOST_FTDC_PWT_Transfer = (byte)'2',
	/// <summary>
	/// 取款
	///</summary>
	THOST_FTDC_PWT_Fetch = (byte)'1',
	/// <summary>
	/// 查询
	///</summary>
	THOST_FTDC_PWT_Query = (byte)'0',
}

/// <summary>
/// 加密方式类型
///</summary>
public enum TThostFtdcFBTEncryModeType : byte
{
	/// <summary>
	/// 3DES
	///</summary>
	THOST_FTDC_EM_3DES = (byte)'2',
	/// <summary>
	/// DES
	///</summary>
	THOST_FTDC_EM_DES = (byte)'1',
	/// <summary>
	/// 不加密
	///</summary>
	THOST_FTDC_EM_NoEncry = (byte)'0',
}

/// <summary>
/// 银行冲正标志类型
///</summary>
public enum TThostFtdcBankRepealFlagType : byte
{
	/// <summary>
	/// 银行已自动冲正
	///</summary>
	THOST_FTDC_BRF_BankBeenRepealed = (byte)'2',
	/// <summary>
	/// 银行待自动冲正
	///</summary>
	THOST_FTDC_BRF_BankWaitingRepeal = (byte)'1',
	/// <summary>
	/// 银行无需自动冲正
	///</summary>
	THOST_FTDC_BRF_BankNotNeedRepeal = (byte)'0',
}

/// <summary>
/// 期商冲正标志类型
///</summary>
public enum TThostFtdcBrokerRepealFlagType : byte
{
	/// <summary>
	/// 期商已自动冲正
	///</summary>
	THOST_FTDC_BRORF_BrokerBeenRepealed = (byte)'2',
	/// <summary>
	/// 期商待自动冲正
	///</summary>
	THOST_FTDC_BRORF_BrokerWaitingRepeal = (byte)'1',
	/// <summary>
	/// 期商无需自动冲正
	///</summary>
	THOST_FTDC_BRORF_BrokerNotNeedRepeal = (byte)'0',
}

/// <summary>
/// 机构类别类型
///</summary>
public enum TThostFtdcInstitutionTypeType : byte
{
	/// <summary>
	/// 券商
	///</summary>
	THOST_FTDC_TS_Store = (byte)'2',
	/// <summary>
	/// 期商
	///</summary>
	THOST_FTDC_TS_Future = (byte)'1',
	/// <summary>
	/// 银行
	///</summary>
	THOST_FTDC_TS_Bank = (byte)'0',
}

/// <summary>
/// 最后分片标志类型
///</summary>
public enum TThostFtdcLastFragmentType : byte
{
	/// <summary>
	/// 不是最后分片
	///</summary>
	THOST_FTDC_LF_No = (byte)'1',
	/// <summary>
	/// 是最后分片
	///</summary>
	THOST_FTDC_LF_Yes = (byte)'0',
}

/// <summary>
/// 银行账户状态类型
///</summary>
public enum TThostFtdcBankAccStatusType : byte
{
	/// <summary>
	/// 挂失
	///</summary>
	THOST_FTDC_BAS_ReportLoss = (byte)'2',
	/// <summary>
	/// 冻结
	///</summary>
	THOST_FTDC_BAS_Freeze = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_BAS_Normal = (byte)'0',
}

/// <summary>
/// 资金账户状态类型
///</summary>
public enum TThostFtdcMoneyAccountStatusType : byte
{
	/// <summary>
	/// 销户
	///</summary>
	THOST_FTDC_MAS_Cancel = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_MAS_Normal = (byte)'0',
}

/// <summary>
/// 存管状态类型
///</summary>
public enum TThostFtdcManageStatusType : byte
{
	/// <summary>
	/// 撤销指定
	///</summary>
	THOST_FTDC_MSS_CancelPoint = (byte)'2',
	/// <summary>
	/// 预指定
	///</summary>
	THOST_FTDC_MSS_PrePoint = (byte)'1',
	/// <summary>
	/// 指定存管
	///</summary>
	THOST_FTDC_MSS_Point = (byte)'0',
}

/// <summary>
/// 应用系统类型类型
///</summary>
public enum TThostFtdcSystemTypeType : byte
{
	/// <summary>
	/// 第三方存管
	///</summary>
	THOST_FTDC_SYT_TheThirdPartStore = (byte)'2',
	/// <summary>
	/// 银证转帐
	///</summary>
	THOST_FTDC_SYT_StockBankTransfer = (byte)'1',
	/// <summary>
	/// 银期转帐
	///</summary>
	THOST_FTDC_SYT_FutureBankTransfer = (byte)'0',
}

/// <summary>
/// 银期转帐划转结果标志类型
///</summary>
public enum TThostFtdcTxnEndFlagType : byte
{
	/// <summary>
	/// 系统出错，请人工处理
	///</summary>
	THOST_FTDC_TEF_SysErrorNeedManualProcess = (byte)'6',
	/// <summary>
	/// 通讯异常 ，请人工处理
	///</summary>
	THOST_FTDC_TEF_CommuFailedNeedManualProcess = (byte)'5',
	/// <summary>
	/// 已人工异常处理
	///</summary>
	THOST_FTDC_TEF_ManualProcessedForException = (byte)'4',
	/// <summary>
	/// 异常中
	///</summary>
	THOST_FTDC_TEF_Abnormal = (byte)'3',
	/// <summary>
	/// 失败结束
	///</summary>
	THOST_FTDC_TEF_Failed = (byte)'2',
	/// <summary>
	/// 成功结束
	///</summary>
	THOST_FTDC_TEF_Success = (byte)'1',
	/// <summary>
	/// 正常处理中
	///</summary>
	THOST_FTDC_TEF_NormalProcessing = (byte)'0',
}

/// <summary>
/// 银期转帐服务处理状态类型
///</summary>
public enum TThostFtdcProcessStatusType : byte
{
	/// <summary>
	/// 处理完成
	///</summary>
	THOST_FTDC_PSS_Finished = (byte)'2',
	/// <summary>
	/// 开始处理
	///</summary>
	THOST_FTDC_PSS_StartProcess = (byte)'1',
	/// <summary>
	/// 未处理
	///</summary>
	THOST_FTDC_PSS_NotProcess = (byte)'0',
}

/// <summary>
/// 客户类型类型
///</summary>
public enum TThostFtdcCustTypeType : byte
{
	/// <summary>
	/// 机构户
	///</summary>
	THOST_FTDC_CUSTT_Institution = (byte)'1',
	/// <summary>
	/// 自然人
	///</summary>
	THOST_FTDC_CUSTT_Person = (byte)'0',
}

/// <summary>
/// 银期转帐方向类型
///</summary>
public enum TThostFtdcFBTTransferDirectionType : byte
{
	/// <summary>
	/// 出金，期货转银行
	///</summary>
	THOST_FTDC_FBTTD_FromFutureToBank = (byte)'2',
	/// <summary>
	/// 入金，银行转期货
	///</summary>
	THOST_FTDC_FBTTD_FromBankToFuture = (byte)'1',
}

/// <summary>
/// 开销户类别类型
///</summary>
public enum TThostFtdcOpenOrDestroyType : byte
{
	/// <summary>
	/// 销户
	///</summary>
	THOST_FTDC_OOD_Destroy = (byte)'0',
	/// <summary>
	/// 开户
	///</summary>
	THOST_FTDC_OOD_Open = (byte)'1',
}

/// <summary>
/// 有效标志类型
///</summary>
public enum TThostFtdcAvailabilityFlagType : byte
{
	/// <summary>
	/// 冲正
	///</summary>
	THOST_FTDC_AVAF_Repeal = (byte)'2',
	/// <summary>
	/// 有效
	///</summary>
	THOST_FTDC_AVAF_Valid = (byte)'1',
	/// <summary>
	/// 未确认
	///</summary>
	THOST_FTDC_AVAF_Invalid = (byte)'0',
}

/// <summary>
/// 机构类型类型
///</summary>
public enum TThostFtdcOrganTypeType : byte
{
	/// <summary>
	/// 银期转帐平台管理
	///</summary>
	THOST_FTDC_OT_PlateForm = (byte)'9',
	/// <summary>
	/// 交易前置
	///</summary>
	THOST_FTDC_OT_Future = (byte)'2',
	/// <summary>
	/// 银行代理
	///</summary>
	THOST_FTDC_OT_Bank = (byte)'1',
}

/// <summary>
/// 机构级别类型
///</summary>
public enum TThostFtdcOrganLevelType : byte
{
	/// <summary>
	/// 银行分中心或期货公司营业部
	///</summary>
	THOST_FTDC_OL_Branch = (byte)'2',
	/// <summary>
	/// 银行总行或期商总部
	///</summary>
	THOST_FTDC_OL_HeadQuarters = (byte)'1',
}

/// <summary>
/// 协议类型类型
///</summary>
public enum TThostFtdcProtocalIDType : byte
{
	/// <summary>
	/// 银期转帐平台协议
	///</summary>
	THOST_FTDC_PID_FBTPlateFormProtocal = (byte)'X',
	/// <summary>
	/// 交行协议
	///</summary>
	THOST_FTDC_PID_BOCOMProtocal = (byte)'5',
	/// <summary>
	/// 建行协议
	///</summary>
	THOST_FTDC_PID_CCBProtocal = (byte)'4',
	/// <summary>
	/// 中国银行协议
	///</summary>
	THOST_FTDC_PID_CBCProtocal = (byte)'3',
	/// <summary>
	/// 农行协议
	///</summary>
	THOST_FTDC_PID_ABCProtocal = (byte)'2',
	/// <summary>
	/// 工行协议
	///</summary>
	THOST_FTDC_PID_ICBCProtocal = (byte)'1',
	/// <summary>
	/// 期商协议
	///</summary>
	THOST_FTDC_PID_FutureProtocal = (byte)'0',
}

/// <summary>
/// 套接字连接方式类型
///</summary>
public enum TThostFtdcConnectModeType : byte
{
	/// <summary>
	/// 长连接
	///</summary>
	THOST_FTDC_CM_LongConnect = (byte)'1',
	/// <summary>
	/// 短连接
	///</summary>
	THOST_FTDC_CM_ShortConnect = (byte)'0',
}

/// <summary>
/// 套接字通信方式类型
///</summary>
public enum TThostFtdcSyncModeType : byte
{
	/// <summary>
	/// 同步
	///</summary>
	THOST_FTDC_SRM_Sync = (byte)'1',
	/// <summary>
	/// 异步
	///</summary>
	THOST_FTDC_SRM_ASync = (byte)'0',
}

/// <summary>
/// 银行帐号类型类型
///</summary>
public enum TThostFtdcBankAccTypeType : byte
{
	/// <summary>
	/// 信用卡
	///</summary>
	THOST_FTDC_BAT_CreditCard = (byte)'3',
	/// <summary>
	/// 储蓄卡
	///</summary>
	THOST_FTDC_BAT_SavingCard = (byte)'2',
	/// <summary>
	/// 银行存折
	///</summary>
	THOST_FTDC_BAT_BankBook = (byte)'1',
}

/// <summary>
/// 期货公司帐号类型类型
///</summary>
public enum TThostFtdcFutureAccTypeType : byte
{
	/// <summary>
	/// 信用卡
	///</summary>
	THOST_FTDC_FAT_CreditCard = (byte)'3',
	/// <summary>
	/// 储蓄卡
	///</summary>
	THOST_FTDC_FAT_SavingCard = (byte)'2',
	/// <summary>
	/// 银行存折
	///</summary>
	THOST_FTDC_FAT_BankBook = (byte)'1',
}

/// <summary>
/// 接入机构状态类型
///</summary>
public enum TThostFtdcOrganStatusType : byte
{
	/// <summary>
	/// 注销
	///</summary>
	THOST_FTDC_OS_Invalid = (byte)'9',
	/// <summary>
	/// 日终清理
	///</summary>
	THOST_FTDC_OS_DayEndClean = (byte)'5',
	/// <summary>
	/// 对帐
	///</summary>
	THOST_FTDC_OS_CheckDetail = (byte)'4',
	/// <summary>
	/// 对帐文件到达
	///</summary>
	THOST_FTDC_OS_CheckFileArrived = (byte)'3',
	/// <summary>
	/// 签退
	///</summary>
	THOST_FTDC_OS_CheckOut = (byte)'2',
	/// <summary>
	/// 签到
	///</summary>
	THOST_FTDC_OS_CheckIn = (byte)'1',
	/// <summary>
	/// 启用
	///</summary>
	THOST_FTDC_OS_Ready = (byte)'0',
}

/// <summary>
/// 建行收费模式类型
///</summary>
public enum TThostFtdcCCBFeeModeType : byte
{
	/// <summary>
	/// 按月扣收
	///</summary>
	THOST_FTDC_CCBFM_ByMonth = (byte)'2',
	/// <summary>
	/// 按金额扣收
	///</summary>
	THOST_FTDC_CCBFM_ByAmount = (byte)'1',
}

/// <summary>
/// 通讯API类型类型
///</summary>
public enum TThostFtdcCommApiTypeType : byte
{
	/// <summary>
	/// 交易系统的UserApi
	///</summary>
	THOST_FTDC_CAPIT_UserApi = (byte)'3',
	/// <summary>
	/// 服务端
	///</summary>
	THOST_FTDC_CAPIT_Server = (byte)'2',
	/// <summary>
	/// 客户端
	///</summary>
	THOST_FTDC_CAPIT_Client = (byte)'1',
}

/// <summary>
/// 连接状态类型
///</summary>
public enum TThostFtdcLinkStatusType : byte
{
	/// <summary>
	/// 没有连接
	///</summary>
	THOST_FTDC_LS_Disconnected = (byte)'2',
	/// <summary>
	/// 已经连接
	///</summary>
	THOST_FTDC_LS_Connected = (byte)'1',
}

/// <summary>
/// 密码核对标志类型
///</summary>
public enum TThostFtdcPwdFlagType : byte
{
	/// <summary>
	/// 密文核对
	///</summary>
	THOST_FTDC_BPWDF_EncryptCheck = (byte)'2',
	/// <summary>
	/// 明文核对
	///</summary>
	THOST_FTDC_BPWDF_BlankCheck = (byte)'1',
	/// <summary>
	/// 不核对
	///</summary>
	THOST_FTDC_BPWDF_NoCheck = (byte)'0',
}

/// <summary>
/// 期货帐号类型类型
///</summary>
public enum TThostFtdcSecuAccTypeType : byte
{
	/// <summary>
	/// 深圳股东帐号
	///</summary>
	THOST_FTDC_SAT_SZStockholderID = (byte)'4',
	/// <summary>
	/// 上海股东帐号
	///</summary>
	THOST_FTDC_SAT_SHStockholderID = (byte)'3',
	/// <summary>
	/// 资金卡号
	///</summary>
	THOST_FTDC_SAT_CardID = (byte)'2',
	/// <summary>
	/// 资金帐号
	///</summary>
	THOST_FTDC_SAT_AccountID = (byte)'1',
}

/// <summary>
/// 转账交易状态类型
///</summary>
public enum TThostFtdcTransferStatusType : byte
{
	/// <summary>
	/// 被冲正
	///</summary>
	THOST_FTDC_TRFS_Repealed = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_TRFS_Normal = (byte)'0',
}

/// <summary>
/// 发起方类型
///</summary>
public enum TThostFtdcSponsorTypeType : byte
{
	/// <summary>
	/// 银行
	///</summary>
	THOST_FTDC_SPTYPE_Bank = (byte)'1',
	/// <summary>
	/// 期商
	///</summary>
	THOST_FTDC_SPTYPE_Broker = (byte)'0',
}

/// <summary>
/// 请求响应类别类型
///</summary>
public enum TThostFtdcReqRspTypeType : byte
{
	/// <summary>
	/// 响应
	///</summary>
	THOST_FTDC_REQRSP_Response = (byte)'1',
	/// <summary>
	/// 请求
	///</summary>
	THOST_FTDC_REQRSP_Request = (byte)'0',
}

/// <summary>
/// 银期转帐用户事件类型类型
///</summary>
public enum TThostFtdcFBTUserEventTypeType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_FBTUET_Other = (byte)'Z',
	/// <summary>
	/// 预约开户确认
	///</summary>
	THOST_FTDC_FBTUET_ReserveOpenAccountConfirm = (byte)'E',
	/// <summary>
	/// 撤销预约开户
	///</summary>
	THOST_FTDC_FBTUET_CancelReserveOpenAccount = (byte)'D',
	/// <summary>
	/// 预约开户
	///</summary>
	THOST_FTDC_FBTUET_ReserveOpenAccount = (byte)'C',
	/// <summary>
	/// 密钥同步
	///</summary>
	THOST_FTDC_FBTUET_SyncKey = (byte)'B',
	/// <summary>
	/// 签退
	///</summary>
	THOST_FTDC_FBTUET_SignOut = (byte)'A',
	/// <summary>
	/// 查询期货账户
	///</summary>
	THOST_FTDC_FBTUET_QueryFutureAccount = (byte)'9',
	/// <summary>
	/// 查询银行账户
	///</summary>
	THOST_FTDC_FBTUET_QueryBankAccount = (byte)'8',
	/// <summary>
	/// 冲正期货转银行
	///</summary>
	THOST_FTDC_FBTUET_RepealFromFutureToBank = (byte)'7',
	/// <summary>
	/// 冲正银行转期货
	///</summary>
	THOST_FTDC_FBTUET_RepealFromBankToFuture = (byte)'6',
	/// <summary>
	/// 变更银行账户
	///</summary>
	THOST_FTDC_FBTUET_ChangeAccount = (byte)'5',
	/// <summary>
	/// 销户
	///</summary>
	THOST_FTDC_FBTUET_CancelAccount = (byte)'4',
	/// <summary>
	/// 开户
	///</summary>
	THOST_FTDC_FBTUET_OpenAccount = (byte)'3',
	/// <summary>
	/// 期货转银行
	///</summary>
	THOST_FTDC_FBTUET_FromFutureToBank = (byte)'2',
	/// <summary>
	/// 银行转期货
	///</summary>
	THOST_FTDC_FBTUET_FromBankToFuture = (byte)'1',
	/// <summary>
	/// 签到
	///</summary>
	THOST_FTDC_FBTUET_SignIn = (byte)'0',
}

/// <summary>
/// 记录操作类型类型
///</summary>
public enum TThostFtdcDBOperationType : byte
{
	/// <summary>
	/// 删除
	///</summary>
	THOST_FTDC_DBOP_Delete = (byte)'2',
	/// <summary>
	/// 更新
	///</summary>
	THOST_FTDC_DBOP_Update = (byte)'1',
	/// <summary>
	/// 插入
	///</summary>
	THOST_FTDC_DBOP_Insert = (byte)'0',
}

/// <summary>
/// 同步标记类型
///</summary>
public enum TThostFtdcSyncFlagType : byte
{
	/// <summary>
	/// 未同步
	///</summary>
	THOST_FTDC_SYNF_No = (byte)'1',
	/// <summary>
	/// 已同步
	///</summary>
	THOST_FTDC_SYNF_Yes = (byte)'0',
}

/// <summary>
/// 同步类型类型
///</summary>
public enum TThostFtdcSyncTypeType : byte
{
	/// <summary>
	/// 定时完全同步
	///</summary>
	THOST_FTDC_SYNT_TimerFullSync = (byte)'2',
	/// <summary>
	/// 定时同步
	///</summary>
	THOST_FTDC_SYNT_TimerSync = (byte)'1',
	/// <summary>
	/// 一次同步
	///</summary>
	THOST_FTDC_SYNT_OneOffSync = (byte)'0',
}

/// <summary>
/// 换汇方向类型
///</summary>
public enum TThostFtdcExDirectionType : byte
{
	/// <summary>
	/// 售汇
	///</summary>
	THOST_FTDC_FBEDIR_Sale = (byte)'1',
	/// <summary>
	/// 结汇
	///</summary>
	THOST_FTDC_FBEDIR_Settlement = (byte)'0',
}

/// <summary>
/// 换汇成功标志类型
///</summary>
public enum TThostFtdcFBEResultFlagType : byte
{
	/// <summary>
	/// 失败
	///</summary>
	THOST_FTDC_FBERES_Fail = (byte)'x',
	/// <summary>
	/// 交易结果未知
	///</summary>
	THOST_FTDC_FBERES_UnknownTrading = (byte)'8',
	/// <summary>
	/// 账户余额不足
	///</summary>
	THOST_FTDC_FBERES_InsufficientBalance = (byte)'1',
	/// <summary>
	/// 成功
	///</summary>
	THOST_FTDC_FBERES_Success = (byte)'0',
}

/// <summary>
/// 换汇交易状态类型
///</summary>
public enum TThostFtdcFBEExchStatusType : byte
{
	/// <summary>
	/// 交易重发
	///</summary>
	THOST_FTDC_FBEES_ReExchange = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_FBEES_Normal = (byte)'0',
}

/// <summary>
/// 换汇文件标志类型
///</summary>
public enum TThostFtdcFBEFileFlagType : byte
{
	/// <summary>
	/// 文件
	///</summary>
	THOST_FTDC_FBEFG_File = (byte)'1',
	/// <summary>
	/// 数据包
	///</summary>
	THOST_FTDC_FBEFG_DataPackage = (byte)'0',
}

/// <summary>
/// 换汇已交易标志类型
///</summary>
public enum TThostFtdcFBEAlreadyTradeType : byte
{
	/// <summary>
	/// 已交易
	///</summary>
	THOST_FTDC_FBEAT_Trade = (byte)'1',
	/// <summary>
	/// 未交易
	///</summary>
	THOST_FTDC_FBEAT_NotTrade = (byte)'0',
}

/// <summary>
/// 银期换汇用户事件类型类型
///</summary>
public enum TThostFtdcFBEUserEventTypeType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_FBEUET_Other = (byte)'Z',
	/// <summary>
	/// 签退
	///</summary>
	THOST_FTDC_FBEUET_SignOut = (byte)'8',
	/// <summary>
	/// 对账文件通知
	///</summary>
	THOST_FTDC_FBEUET_CheckBankAccount = (byte)'7',
	/// <summary>
	/// 换汇汇率查询
	///</summary>
	THOST_FTDC_FBEUET_QueryExchRate = (byte)'6',
	/// <summary>
	/// 换汇汇总查询
	///</summary>
	THOST_FTDC_FBEUET_QueryExchSummary = (byte)'5',
	/// <summary>
	/// 换汇明细查询
	///</summary>
	THOST_FTDC_FBEUET_QueryExchDetial = (byte)'4',
	/// <summary>
	/// 银行账户查询
	///</summary>
	THOST_FTDC_FBEUET_QueryBankAccount = (byte)'3',
	/// <summary>
	/// 换汇重发
	///</summary>
	THOST_FTDC_FBEUET_ReExchange = (byte)'2',
	/// <summary>
	/// 换汇
	///</summary>
	THOST_FTDC_FBEUET_Exchange = (byte)'1',
	/// <summary>
	/// 签到
	///</summary>
	THOST_FTDC_FBEUET_SignIn = (byte)'0',
}

/// <summary>
/// 换汇发送标志类型
///</summary>
public enum TThostFtdcFBEReqFlagType : byte
{
	/// <summary>
	/// 等待重发
	///</summary>
	THOST_FTDC_FBERF_WaitReSend = (byte)'4',
	/// <summary>
	/// 发送失败
	///</summary>
	THOST_FTDC_FBERF_SendFailed = (byte)'3',
	/// <summary>
	/// 发送成功
	///</summary>
	THOST_FTDC_FBERF_SendSuccess = (byte)'2',
	/// <summary>
	/// 等待发送
	///</summary>
	THOST_FTDC_FBERF_WaitSend = (byte)'1',
	/// <summary>
	/// 未处理
	///</summary>
	THOST_FTDC_FBERF_UnProcessed = (byte)'0',
}

/// <summary>
/// 风险通知类型类型
///</summary>
public enum TThostFtdcNotifyClassType : byte
{
	/// <summary>
	/// 异常
	///</summary>
	THOST_FTDC_NC_Exception = (byte)'5',
	/// <summary>
	/// 穿仓
	///</summary>
	THOST_FTDC_NC_CHUANCANG = (byte)'4',
	/// <summary>
	/// 强平
	///</summary>
	THOST_FTDC_NC_Force = (byte)'3',
	/// <summary>
	/// 追保
	///</summary>
	THOST_FTDC_NC_Call = (byte)'2',
	/// <summary>
	/// 警示
	///</summary>
	THOST_FTDC_NC_Warn = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_NC_NOERROR = (byte)'0',
}

/// <summary>
/// 强平单类型类型
///</summary>
public enum TThostFtdcForceCloseTypeType : byte
{
	/// <summary>
	/// 批量投资者辅助强平
	///</summary>
	THOST_FTDC_FCT_Group = (byte)'2',
	/// <summary>
	/// 单一投资者辅助强平
	///</summary>
	THOST_FTDC_FCT_Single = (byte)'1',
	/// <summary>
	/// 手工强平
	///</summary>
	THOST_FTDC_FCT_Manual = (byte)'0',
}

/// <summary>
/// 风险通知途径类型
///</summary>
public enum TThostFtdcRiskNotifyMethodType : byte
{
	/// <summary>
	/// 人工通知
	///</summary>
	THOST_FTDC_RNM_Manual = (byte)'3',
	/// <summary>
	/// 邮件通知
	///</summary>
	THOST_FTDC_RNM_EMail = (byte)'2',
	/// <summary>
	/// 短信通知
	///</summary>
	THOST_FTDC_RNM_SMS = (byte)'1',
	/// <summary>
	/// 系统通知
	///</summary>
	THOST_FTDC_RNM_System = (byte)'0',
}

/// <summary>
/// 风险通知状态类型
///</summary>
public enum TThostFtdcRiskNotifyStatusType : byte
{
	/// <summary>
	/// 已确认
	///</summary>
	THOST_FTDC_RNS_Confirmed = (byte)'5',
	/// <summary>
	/// 已接收未确认
	///</summary>
	THOST_FTDC_RNS_Received = (byte)'4',
	/// <summary>
	/// 已发送未接收
	///</summary>
	THOST_FTDC_RNS_SendOk = (byte)'3',
	/// <summary>
	/// 发送失败
	///</summary>
	THOST_FTDC_RNS_SendError = (byte)'2',
	/// <summary>
	/// 已生成未发送
	///</summary>
	THOST_FTDC_RNS_Generated = (byte)'1',
	/// <summary>
	/// 未生成
	///</summary>
	THOST_FTDC_RNS_NotGen = (byte)'0',
}

/// <summary>
/// 风控用户操作事件类型
///</summary>
public enum TThostFtdcRiskUserEventType : byte
{
	/// <summary>
	/// 导出数据
	///</summary>
	THOST_FTDC_RUE_ExportData = (byte)'0',
}

/// <summary>
/// 条件单索引条件类型
///</summary>
public enum TThostFtdcConditionalOrderSortTypeType : byte
{
	/// <summary>
	/// 使用买价降序
	///</summary>
	THOST_FTDC_COST_BidPriceDesc = (byte)'5',
	/// <summary>
	/// 使用买价升序
	///</summary>
	THOST_FTDC_COST_BidPriceAsc = (byte)'4',
	/// <summary>
	/// 使用卖价降序
	///</summary>
	THOST_FTDC_COST_AskPriceDesc = (byte)'3',
	/// <summary>
	/// 使用卖价升序
	///</summary>
	THOST_FTDC_COST_AskPriceAsc = (byte)'2',
	/// <summary>
	/// 使用最新价降序
	///</summary>
	THOST_FTDC_COST_LastPriceDesc = (byte)'1',
	/// <summary>
	/// 使用最新价升序
	///</summary>
	THOST_FTDC_COST_LastPriceAsc = (byte)'0',
}

/// <summary>
/// 报送状态类型
///</summary>
public enum TThostFtdcSendTypeType : byte
{
	/// <summary>
	/// 取消报送
	///</summary>
	THOST_FTDC_UOAST_Cancel = (byte)'6',
	/// <summary>
	/// 接收失败
	///</summary>
	THOST_FTDC_UOAST_Fail = (byte)'5',
	/// <summary>
	/// 接收成功
	///</summary>
	THOST_FTDC_UOAST_Success = (byte)'4',
	/// <summary>
	/// 报送失败
	///</summary>
	THOST_FTDC_UOAST_SendFail = (byte)'3',
	/// <summary>
	/// 已生成
	///</summary>
	THOST_FTDC_UOAST_Generated = (byte)'2',
	/// <summary>
	/// 已发送
	///</summary>
	THOST_FTDC_UOAST_Sended = (byte)'1',
	/// <summary>
	/// 未发送
	///</summary>
	THOST_FTDC_UOAST_NoSend = (byte)'0',
}

/// <summary>
/// 交易编码状态类型
///</summary>
public enum TThostFtdcClientIDStatusType : byte
{
	/// <summary>
	/// 已撤销编码
	///</summary>
	THOST_FTDC_UOACS_Cancel = (byte)'6',
	/// <summary>
	/// 拒绝
	///</summary>
	THOST_FTDC_UOACS_Refuse = (byte)'5',
	/// <summary>
	/// 完成
	///</summary>
	THOST_FTDC_UOACS_Success = (byte)'4',
	/// <summary>
	/// 已发送申请
	///</summary>
	THOST_FTDC_UOACS_Sended = (byte)'3',
	/// <summary>
	/// 已提交申请
	///</summary>
	THOST_FTDC_UOACS_Submited = (byte)'2',
	/// <summary>
	/// 未申请
	///</summary>
	THOST_FTDC_UOACS_NoApply = (byte)'1',
}

/// <summary>
/// 特有信息类型类型
///</summary>
public enum TThostFtdcQuestionTypeType : byte
{
	/// <summary>
	/// 填空
	///</summary>
	THOST_FTDC_QT_Blank = (byte)'3',
	/// <summary>
	/// 多选
	///</summary>
	THOST_FTDC_QT_Option = (byte)'2',
	/// <summary>
	/// 单选
	///</summary>
	THOST_FTDC_QT_Radio = (byte)'1',
}

/// <summary>
/// 业务类型类型
///</summary>
public enum TThostFtdcBusinessTypeType : byte
{
	/// <summary>
	/// 通知
	///</summary>
	THOST_FTDC_BT_Notice = (byte)'3',
	/// <summary>
	/// 应答
	///</summary>
	THOST_FTDC_BT_Response = (byte)'2',
	/// <summary>
	/// 请求
	///</summary>
	THOST_FTDC_BT_Request = (byte)'1',
}

/// <summary>
/// 监控中心返回码类型
///</summary>
public enum TThostFtdcCfmmcReturnCodeType : byte
{
	/// <summary>
	/// 其他错误
	///</summary>
	THOST_FTDC_CRC_OtherFail = (byte)'4',
	/// <summary>
	/// 监控中实名制检查失败
	///</summary>
	THOST_FTDC_CRC_IDCardFail = (byte)'3',
	/// <summary>
	/// 监控中客户资料检查失败
	///</summary>
	THOST_FTDC_CRC_InfoFail = (byte)'2',
	/// <summary>
	/// 该客户已经有流程在处理中
	///</summary>
	THOST_FTDC_CRC_Working = (byte)'1',
	/// <summary>
	/// 成功
	///</summary>
	THOST_FTDC_CRC_Success = (byte)'0',
}

/// <summary>
/// 客户类型类型
///</summary>
public enum TThostFtdcClientTypeType : byte
{
	/// <summary>
	/// 资管户
	///</summary>
	THOST_FTDC_CfMMCCT_Asset = (byte)'5',
	/// <summary>
	/// 特殊法人
	///</summary>
	THOST_FTDC_CfMMCCT_SpecialOrgan = (byte)'4',
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_CfMMCCT_Other = (byte)'3',
	/// <summary>
	/// 单位
	///</summary>
	THOST_FTDC_CfMMCCT_Company = (byte)'2',
	/// <summary>
	/// 个人
	///</summary>
	THOST_FTDC_CfMMCCT_Person = (byte)'1',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_CfMMCCT_All = (byte)'0',
}

/// <summary>
/// 交易所编号类型
///</summary>
public enum TThostFtdcExchangeIDTypeType : byte
{
	/// <summary>
	/// 上海国际能源交易中心股份有限公司
	///</summary>
	THOST_FTDC_EIDT_INE = (byte)'N',
	/// <summary>
	/// 中国金融期货交易所
	///</summary>
	THOST_FTDC_EIDT_CFFEX = (byte)'J',
	/// <summary>
	/// 大连商品交易所
	///</summary>
	THOST_FTDC_EIDT_DCE = (byte)'D',
	/// <summary>
	/// 郑州商品交易所
	///</summary>
	THOST_FTDC_EIDT_CZCE = (byte)'Z',
	/// <summary>
	/// 上海期货交易所
	///</summary>
	THOST_FTDC_EIDT_SHFE = (byte)'S',
}

/// <summary>
/// 交易编码类型类型
///</summary>
public enum TThostFtdcExClientIDTypeType : byte
{
	/// <summary>
	/// 投机
	///</summary>
	THOST_FTDC_ECIDT_Speculation = (byte)'3',
	/// <summary>
	/// 套利
	///</summary>
	THOST_FTDC_ECIDT_Arbitrage = (byte)'2',
	/// <summary>
	/// 套保
	///</summary>
	THOST_FTDC_ECIDT_Hedge = (byte)'1',
}

/// <summary>
/// 更新状态类型
///</summary>
public enum TThostFtdcUpdateFlagType : byte
{
	/// <summary>
	/// 已丢弃
	///</summary>
	THOST_FTDC_UF_Cancel = (byte)'5',
	/// <summary>
	/// 更新交易编码失败
	///</summary>
	THOST_FTDC_UF_TCFail = (byte)'4',
	/// <summary>
	/// 更新交易编码成功
	///</summary>
	THOST_FTDC_UF_TCSuccess = (byte)'3',
	/// <summary>
	/// 更新全部信息失败
	///</summary>
	THOST_FTDC_UF_Fail = (byte)'2',
	/// <summary>
	/// 更新全部信息成功
	///</summary>
	THOST_FTDC_UF_Success = (byte)'1',
	/// <summary>
	/// 未更新
	///</summary>
	THOST_FTDC_UF_NoUpdate = (byte)'0',
}

/// <summary>
/// 申请动作类型
///</summary>
public enum TThostFtdcApplyOperateIDType : byte
{
	/// <summary>
	/// 激活休眠账户
	///</summary>
	THOST_FTDC_AOID_ActiveFreezeAccount = (byte)'9',
	/// <summary>
	/// 账户休眠
	///</summary>
	THOST_FTDC_AOID_FreezeAccount = (byte)'8',
	/// <summary>
	/// 销户
	///</summary>
	THOST_FTDC_AOID_CancelInvestor = (byte)'6',
	/// <summary>
	/// 撤销交易编码
	///</summary>
	THOST_FTDC_AOID_CancelTradingCode = (byte)'5',
	/// <summary>
	/// 申请交易编码
	///</summary>
	THOST_FTDC_AOID_ApplyTradingCode = (byte)'4',
	/// <summary>
	/// 修改一般信息
	///</summary>
	THOST_FTDC_AOID_ModifyNoIDCard = (byte)'3',
	/// <summary>
	/// 修改身份信息
	///</summary>
	THOST_FTDC_AOID_ModifyIDCard = (byte)'2',
	/// <summary>
	/// 开户
	///</summary>
	THOST_FTDC_AOID_OpenInvestor = (byte)'1',
}

/// <summary>
/// 申请状态类型
///</summary>
public enum TThostFtdcApplyStatusIDType : byte
{
	/// <summary>
	/// 已删除
	///</summary>
	THOST_FTDC_ASID_Deleted = (byte)'5',
	/// <summary>
	/// 已拒绝
	///</summary>
	THOST_FTDC_ASID_Refused = (byte)'4',
	/// <summary>
	/// 已审核
	///</summary>
	THOST_FTDC_ASID_Checked = (byte)'3',
	/// <summary>
	/// 已提交
	///</summary>
	THOST_FTDC_ASID_Submited = (byte)'2',
	/// <summary>
	/// 未补全
	///</summary>
	THOST_FTDC_ASID_NoComplete = (byte)'1',
}

/// <summary>
/// 发送方式类型
///</summary>
public enum TThostFtdcSendMethodType : byte
{
	/// <summary>
	/// 电子发送
	///</summary>
	THOST_FTDC_UOASM_ByFile = (byte)'2',
	/// <summary>
	/// 文件发送
	///</summary>
	THOST_FTDC_UOASM_ByAPI = (byte)'1',
}

/// <summary>
/// 操作方法类型
///</summary>
public enum TThostFtdcEventModeType : byte
{
	/// <summary>
	/// 冲销
	///</summary>
	THOST_FTDC_EvM_Reverse = (byte)'7',
	/// <summary>
	/// 注销
	///</summary>
	THOST_FTDC_EvM_CANCEL = (byte)'6',
	/// <summary>
	/// 复制
	///</summary>
	THOST_FTDC_EvM_COPY = (byte)'5',
	/// <summary>
	/// 复核
	///</summary>
	THOST_FTDC_EvM_CHECK = (byte)'4',
	/// <summary>
	/// 删除
	///</summary>
	THOST_FTDC_EvM_DELETE = (byte)'3',
	/// <summary>
	/// 修改
	///</summary>
	THOST_FTDC_EvM_UPDATE = (byte)'2',
	/// <summary>
	/// 增加
	///</summary>
	THOST_FTDC_EvM_ADD = (byte)'1',
}

/// <summary>
/// 统一开户申请自动发送类型
///</summary>
public enum TThostFtdcUOAAutoSendType : byte
{
	/// <summary>
	/// 不自动发送，也不自动接收
	///</summary>
	THOST_FTDC_UOAA_NSR = (byte)'4',
	/// <summary>
	/// 不自动发送，自动接收
	///</summary>
	THOST_FTDC_UOAA_NSAR = (byte)'3',
	/// <summary>
	/// 自动发送，不自动接收
	///</summary>
	THOST_FTDC_UOAA_ASNR = (byte)'2',
	/// <summary>
	/// 自动发送并接收
	///</summary>
	THOST_FTDC_UOAA_ASR = (byte)'1',
}

/// <summary>
/// 流程ID类型
///</summary>
public enum TThostFtdcFlowIDType : byte
{
	/// <summary>
	/// 投资者手续费率模板关系设置
	///</summary>
	THOST_FTDC_EvM_InvestorCommRateModel = (byte)'3',
	/// <summary>
	/// 投资者手续费率设置
	///</summary>
	THOST_FTDC_EvM_InvestorRate = (byte)'2',
	/// <summary>
	/// 投资者对应投资者组设置
	///</summary>
	THOST_FTDC_EvM_InvestorGroupFlow = (byte)'1',
}

/// <summary>
/// 复核级别类型
///</summary>
public enum TThostFtdcCheckLevelType : byte
{
	/// <summary>
	/// 二级复核
	///</summary>
	THOST_FTDC_CL_Two = (byte)'2',
	/// <summary>
	/// 一级复核
	///</summary>
	THOST_FTDC_CL_One = (byte)'1',
	/// <summary>
	/// 零级复核
	///</summary>
	THOST_FTDC_CL_Zero = (byte)'0',
}

/// <summary>
/// 复核级别类型
///</summary>
public enum TThostFtdcCheckStatusType : byte
{
	/// <summary>
	/// 作废
	///</summary>
	THOST_FTDC_CHS_Cancel = (byte)'4',
	/// <summary>
	/// 拒绝
	///</summary>
	THOST_FTDC_CHS_Refuse = (byte)'3',
	/// <summary>
	/// 已复核
	///</summary>
	THOST_FTDC_CHS_Checked = (byte)'2',
	/// <summary>
	/// 复核中
	///</summary>
	THOST_FTDC_CHS_Checking = (byte)'1',
	/// <summary>
	/// 未复核
	///</summary>
	THOST_FTDC_CHS_Init = (byte)'0',
}

/// <summary>
/// 生效状态类型
///</summary>
public enum TThostFtdcUsedStatusType : byte
{
	/// <summary>
	/// 生效失败
	///</summary>
	THOST_FTDC_CHU_Fail = (byte)'2',
	/// <summary>
	/// 已生效
	///</summary>
	THOST_FTDC_CHU_Used = (byte)'1',
	/// <summary>
	/// 未生效
	///</summary>
	THOST_FTDC_CHU_Unused = (byte)'0',
}

/// <summary>
/// 账户来源类型
///</summary>
public enum TThostFtdcBankAcountOriginType : byte
{
	/// <summary>
	/// 银期转账
	///</summary>
	THOST_FTDC_BAO_ByFBTransfer = (byte)'1',
	/// <summary>
	/// 手工录入
	///</summary>
	THOST_FTDC_BAO_ByAccProperty = (byte)'0',
}

/// <summary>
/// 结算单月报成交汇总方式类型
///</summary>
public enum TThostFtdcMonthBillTradeSumType : byte
{
	/// <summary>
	/// 同合约
	///</summary>
	THOST_FTDC_MBTS_ByDayIns = (byte)'2',
	/// <summary>
	/// 同日同合约同价格
	///</summary>
	THOST_FTDC_MBTS_ByDayInsPrc = (byte)'1',
	/// <summary>
	/// 同日同合约
	///</summary>
	THOST_FTDC_MBTS_ByInstrument = (byte)'0',
}

/// <summary>
/// 银期交易代码枚举类型
///</summary>
public enum TThostFtdcFBTTradeCodeEnumType : byte
{
	/// <summary>
	/// 期货发起期货转银行
	///</summary>
	THOST_FTDC_FTC_BrokerLaunchBrokerToBank = (byte)'2',
	/// <summary>
	/// 银行发起期货转银行
	///</summary>
	THOST_FTDC_FTC_BankLaunchBrokerToBank = (byte)'2',
	/// <summary>
	/// 期货发起银行转期货
	///</summary>
	THOST_FTDC_FTC_BrokerLaunchBankToBroker = (byte)'1',
	/// <summary>
	/// 银行发起银行转期货
	///</summary>
	THOST_FTDC_FTC_BankLaunchBankToBroker = (byte)'1',
}

/// <summary>
/// 动态令牌类型类型
///</summary>
public enum TThostFtdcOTPTypeType : byte
{
	/// <summary>
	/// 时间令牌
	///</summary>
	THOST_FTDC_OTP_TOTP = (byte)'1',
	/// <summary>
	/// 无动态令牌
	///</summary>
	THOST_FTDC_OTP_NONE = (byte)'0',
}

/// <summary>
/// 动态令牌状态类型
///</summary>
public enum TThostFtdcOTPStatusType : byte
{
	/// <summary>
	/// 注销
	///</summary>
	THOST_FTDC_OTPS_Disuse = (byte)'2',
	/// <summary>
	/// 已使用
	///</summary>
	THOST_FTDC_OTPS_Used = (byte)'1',
	/// <summary>
	/// 未使用
	///</summary>
	THOST_FTDC_OTPS_Unused = (byte)'0',
}

/// <summary>
/// 经济公司用户类型类型
///</summary>
public enum TThostFtdcBrokerUserTypeType : byte
{
	/// <summary>
	/// 操作员
	///</summary>
	THOST_FTDC_BUT_BrokerUser = (byte)'2',
	/// <summary>
	/// 投资者
	///</summary>
	THOST_FTDC_BUT_Investor = (byte)'1',
}

/// <summary>
/// 期货类型类型
///</summary>
public enum TThostFtdcFutureTypeType : byte
{
	/// <summary>
	/// 金融期货
	///</summary>
	THOST_FTDC_FUTT_Financial = (byte)'2',
	/// <summary>
	/// 商品期货
	///</summary>
	THOST_FTDC_FUTT_Commodity = (byte)'1',
}

/// <summary>
/// 资金管理操作类型类型
///</summary>
public enum TThostFtdcFundEventTypeType : byte
{
	/// <summary>
	/// 投资者出入金
	///</summary>
	THOST_FTDC_FET_InvestorFundIO = (byte)'8',
	/// <summary>
	/// 交易所出入金
	///</summary>
	THOST_FTDC_FET_ExchangeFundIO = (byte)'7',
	/// <summary>
	/// 银期签约账户
	///</summary>
	THOST_FTDC_FET_Accountregister = (byte)'6',
	/// <summary>
	/// 单个银行帐户转账限额
	///</summary>
	THOST_FTDC_FET_BankRestriction = (byte)'5',
	/// <summary>
	/// 投资者可提资金比例
	///</summary>
	THOST_FTDC_FET_InvestorWithdrawAlm = (byte)'4',
	/// <summary>
	/// 资金冻结
	///</summary>
	THOST_FTDC_FET_Credit = (byte)'3',
	/// <summary>
	/// 期商流水
	///</summary>
	THOST_FTDC_FET_Transfer = (byte)'2',
	/// <summary>
	/// 当日转账限额
	///</summary>
	THOST_FTDC_FET_TodayRestriction = (byte)'1',
	/// <summary>
	/// 转账限额
	///</summary>
	THOST_FTDC_FET_Restriction = (byte)'0',
}

/// <summary>
/// 资金账户来源类型
///</summary>
public enum TThostFtdcAccountSourceTypeType : byte
{
	/// <summary>
	/// 手工录入
	///</summary>
	THOST_FTDC_AST_ManualEntry = (byte)'1',
	/// <summary>
	/// 银期同步
	///</summary>
	THOST_FTDC_AST_FBTransfer = (byte)'0',
}

/// <summary>
/// 交易编码来源类型
///</summary>
public enum TThostFtdcCodeSourceTypeType : byte
{
	/// <summary>
	/// 手工录入(未规范)
	///</summary>
	THOST_FTDC_CST_ManualEntry = (byte)'1',
	/// <summary>
	/// 统一开户(已规范)
	///</summary>
	THOST_FTDC_CST_UnifyAccount = (byte)'0',
}

/// <summary>
/// 操作员范围类型
///</summary>
public enum TThostFtdcUserRangeType : byte
{
	/// <summary>
	/// 单一操作员
	///</summary>
	THOST_FTDC_UR_Single = (byte)'1',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_UR_All = (byte)'0',
}

/// <summary>
/// 交易统计表按客户统计方式类型
///</summary>
public enum TThostFtdcByGroupType : byte
{
	/// <summary>
	/// 按类统计
	///</summary>
	THOST_FTDC_BG_Group = (byte)'1',
	/// <summary>
	/// 按投资者统计
	///</summary>
	THOST_FTDC_BG_Investor = (byte)'2',
}

/// <summary>
/// 交易统计表按范围统计方式类型
///</summary>
public enum TThostFtdcTradeSumStatModeType : byte
{
	/// <summary>
	/// 按交易所统计
	///</summary>
	THOST_FTDC_TSSM_Exchange = (byte)'3',
	/// <summary>
	/// 按产品统计
	///</summary>
	THOST_FTDC_TSSM_Product = (byte)'2',
	/// <summary>
	/// 按合约统计
	///</summary>
	THOST_FTDC_TSSM_Instrument = (byte)'1',
}

/// <summary>
/// 日期表达式设置类型类型
///</summary>
public enum TThostFtdcExprSetModeType : byte
{
	/// <summary>
	/// 典型设置
	///</summary>
	THOST_FTDC_ESM_Typical = (byte)'2',
	/// <summary>
	/// 相对已有规则设置
	///</summary>
	THOST_FTDC_ESM_Relative = (byte)'1',
}

/// <summary>
/// 投资者范围类型
///</summary>
public enum TThostFtdcRateInvestorRangeType : byte
{
	/// <summary>
	/// 单一投资者
	///</summary>
	THOST_FTDC_RIR_Single = (byte)'3',
	/// <summary>
	/// 模板
	///</summary>
	THOST_FTDC_RIR_Model = (byte)'2',
	/// <summary>
	/// 公司标准
	///</summary>
	THOST_FTDC_RIR_All = (byte)'1',
}

/// <summary>
/// 主次用系统数据同步状态类型
///</summary>
public enum TThostFtdcSyncDataStatusType : byte
{
	/// <summary>
	/// 已同步
	///</summary>
	THOST_FTDC_SDS_Settlemented = (byte)'2',
	/// <summary>
	/// 同步中
	///</summary>
	THOST_FTDC_SDS_Settlementing = (byte)'1',
	/// <summary>
	/// 未同步
	///</summary>
	THOST_FTDC_SDS_Initialize = (byte)'0',
}

/// <summary>
/// 成交来源类型
///</summary>
public enum TThostFtdcTradeSourceType : byte
{
	/// <summary>
	/// 来自查询
	///</summary>
	THOST_FTDC_TSRC_QUERY = (byte)'1',
	/// <summary>
	/// 来自交易所普通回报
	///</summary>
	THOST_FTDC_TSRC_NORMAL = (byte)'0',
}

/// <summary>
/// 产品合约统计方式类型
///</summary>
public enum TThostFtdcFlexStatModeType : byte
{
	/// <summary>
	/// 统计所有
	///</summary>
	THOST_FTDC_FSM_All = (byte)'3',
	/// <summary>
	/// 交易所统计
	///</summary>
	THOST_FTDC_FSM_Exchange = (byte)'2',
	/// <summary>
	/// 产品统计
	///</summary>
	THOST_FTDC_FSM_Product = (byte)'1',
}

/// <summary>
/// 投资者范围统计方式类型
///</summary>
public enum TThostFtdcByInvestorRangeType : byte
{
	/// <summary>
	/// 统计所有
	///</summary>
	THOST_FTDC_BIR_All = (byte)'2',
	/// <summary>
	/// 属性统计
	///</summary>
	THOST_FTDC_BIR_Property = (byte)'1',
}

/// <summary>
/// 投资者范围类型
///</summary>
public enum TThostFtdcPropertyInvestorRangeType : byte
{
	/// <summary>
	/// 单一投资者
	///</summary>
	THOST_FTDC_PIR_Single = (byte)'3',
	/// <summary>
	/// 投资者属性
	///</summary>
	THOST_FTDC_PIR_Property = (byte)'2',
	/// <summary>
	/// 所有
	///</summary>
	THOST_FTDC_PIR_All = (byte)'1',
}

/// <summary>
/// 文件状态类型
///</summary>
public enum TThostFtdcFileStatusType : byte
{
	/// <summary>
	/// 生成失败
	///</summary>
	THOST_FTDC_FIS_Failed = (byte)'2',
	/// <summary>
	/// 已生成
	///</summary>
	THOST_FTDC_FIS_Created = (byte)'1',
	/// <summary>
	/// 未生成
	///</summary>
	THOST_FTDC_FIS_NoCreate = (byte)'0',
}

/// <summary>
/// 文件生成方式类型
///</summary>
public enum TThostFtdcFileGenStyleType : byte
{
	/// <summary>
	/// 生成
	///</summary>
	THOST_FTDC_FGS_FileGen = (byte)'1',
	/// <summary>
	/// 下发
	///</summary>
	THOST_FTDC_FGS_FileTransmit = (byte)'0',
}

/// <summary>
/// 系统日志操作方法类型
///</summary>
public enum TThostFtdcSysOperModeType : byte
{
	/// <summary>
	/// 重置
	///</summary>
	THOST_FTDC_SoM_ReSet = (byte)'7',
	/// <summary>
	/// 注销
	///</summary>
	THOST_FTDC_SoM_CanCel = (byte)'6',
	/// <summary>
	/// 激活
	///</summary>
	THOST_FTDC_SoM_AcTive = (byte)'5',
	/// <summary>
	/// 复制
	///</summary>
	THOST_FTDC_SoM_Copy = (byte)'4',
	/// <summary>
	/// 删除
	///</summary>
	THOST_FTDC_SoM_Delete = (byte)'3',
	/// <summary>
	/// 修改
	///</summary>
	THOST_FTDC_SoM_Update = (byte)'2',
	/// <summary>
	/// 增加
	///</summary>
	THOST_FTDC_SoM_Add = (byte)'1',
}

/// <summary>
/// 系统日志操作类型类型
///</summary>
public enum TThostFtdcSysOperTypeType : byte
{
	/// <summary>
	/// 投资者个性信息维护
	///</summary>
	THOST_FTDC_SoT_InvestorPersonalityInfo = (byte)'F',
	/// <summary>
	/// 重置投资者密码
	///</summary>
	THOST_FTDC_SoT_ReSetInvestorPasswd = (byte)'E',
	/// <summary>
	/// 属性设置
	///</summary>
	THOST_FTDC_SoT_PropertySet = (byte)'D',
	/// <summary>
	/// 投资者权限管理
	///</summary>
	THOST_FTDC_SoT_InvestorAuthority = (byte)'C',
	/// <summary>
	/// 投资者状态维护
	///</summary>
	THOST_FTDC_SoT_InvestorStatus = (byte)'B',
	/// <summary>
	/// 交易编码管理
	///</summary>
	THOST_FTDC_SoT_Tradingcode = (byte)'A',
	/// <summary>
	/// 组织架构向查询分类复制
	///</summary>
	THOST_FTDC_SoT_DepartmentCopy = (byte)'9',
	/// <summary>
	/// 组织架构管理
	///</summary>
	THOST_FTDC_SoT_DepartmentManager = (byte)'8',
	/// <summary>
	/// 用户IP限制
	///</summary>
	THOST_FTDC_SoT_UserIpRestriction = (byte)'7',
	/// <summary>
	/// 用户角色设置
	///</summary>
	THOST_FTDC_SoT_SetUserRole = (byte)'6',
	/// <summary>
	/// 设置操作员
	///</summary>
	THOST_FTDC_SoT_SetUserID = (byte)'5',
	/// <summary>
	/// 基础参数设置
	///</summary>
	THOST_FTDC_SoT_BaseParam = (byte)'4',
	/// <summary>
	/// 角色功能设置
	///</summary>
	THOST_FTDC_SoT_RoleFunction = (byte)'3',
	/// <summary>
	/// 角色管理
	///</summary>
	THOST_FTDC_SoT_RoleManager = (byte)'2',
	/// <summary>
	/// 操作员组织架构关系
	///</summary>
	THOST_FTDC_SoT_UserDepartment = (byte)'1',
	/// <summary>
	/// 修改操作员密码
	///</summary>
	THOST_FTDC_SoT_UpdatePassword = (byte)'0',
}

/// <summary>
/// 上报数据查询类型类型
///</summary>
public enum TThostFtdcCSRCDataQueyTypeType : byte
{
	/// <summary>
	/// 查询历史报送的代理经纪公司的数据
	///</summary>
	THOST_FTDC_CSRCQ_History = (byte)'1',
	/// <summary>
	/// 查询当前交易日报送的数据
	///</summary>
	THOST_FTDC_CSRCQ_Current = (byte)'0',
}

/// <summary>
/// 休眠状态类型
///</summary>
public enum TThostFtdcFreezeStatusType : byte
{
	/// <summary>
	/// 休眠
	///</summary>
	THOST_FTDC_FRS_Freeze = (byte)'0',
	/// <summary>
	/// 活跃
	///</summary>
	THOST_FTDC_FRS_Normal = (byte)'1',
}

/// <summary>
/// 规范状态类型
///</summary>
public enum TThostFtdcStandardStatusType : byte
{
	/// <summary>
	/// 未规范
	///</summary>
	THOST_FTDC_STST_NonStandard = (byte)'1',
	/// <summary>
	/// 已规范
	///</summary>
	THOST_FTDC_STST_Standard = (byte)'0',
}

/// <summary>
/// 配置类型类型
///</summary>
public enum TThostFtdcRightParamTypeType : byte
{
	/// <summary>
	/// 解除开仓权限限制
	///</summary>
	THOST_FTDC_RPT_RelieveOpenLimit = (byte)'4',
	/// <summary>
	/// 开仓权限限制
	///</summary>
	THOST_FTDC_RPT_OpenLimit = (byte)'3',
	/// <summary>
	/// 激活休眠户
	///</summary>
	THOST_FTDC_RPT_FreezeActive = (byte)'2',
	/// <summary>
	/// 休眠户
	///</summary>
	THOST_FTDC_RPT_Freeze = (byte)'1',
}

/// <summary>
/// 反洗钱审核表数据状态类型
///</summary>
public enum TThostFtdcDataStatusType : byte
{
	/// <summary>
	/// 已删除
	///</summary>
	THOST_FTDC_AMLDS_Deleted = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_AMLDS_Normal = (byte)'0',
}

/// <summary>
/// 审核状态类型
///</summary>
public enum TThostFtdcAMLCheckStatusType : byte
{
	/// <summary>
	/// 拒绝上报
	///</summary>
	THOST_FTDC_AMLCHS_RefuseReport = (byte)'3',
	/// <summary>
	/// 已复核
	///</summary>
	THOST_FTDC_AMLCHS_Checked = (byte)'2',
	/// <summary>
	/// 复核中
	///</summary>
	THOST_FTDC_AMLCHS_Checking = (byte)'1',
	/// <summary>
	/// 未复核
	///</summary>
	THOST_FTDC_AMLCHS_Init = (byte)'0',
}

/// <summary>
/// 日期类型类型
///</summary>
public enum TThostFtdcAmlDateTypeType : byte
{
	/// <summary>
	/// 发生日期
	///</summary>
	THOST_FTDC_AMLDT_TouchDay = (byte)'1',
	/// <summary>
	/// 检查日期
	///</summary>
	THOST_FTDC_AMLDT_DrawDay = (byte)'0',
}

/// <summary>
/// 审核级别类型
///</summary>
public enum TThostFtdcAmlCheckLevelType : byte
{
	/// <summary>
	/// 三级审核
	///</summary>
	THOST_FTDC_AMLCL_CheckLevel3 = (byte)'3',
	/// <summary>
	/// 二级审核
	///</summary>
	THOST_FTDC_AMLCL_CheckLevel2 = (byte)'2',
	/// <summary>
	/// 一级审核
	///</summary>
	THOST_FTDC_AMLCL_CheckLevel1 = (byte)'1',
	/// <summary>
	/// 零级审核
	///</summary>
	THOST_FTDC_AMLCL_CheckLevel0 = (byte)'0',
}

/// <summary>
/// 导出文件类型类型
///</summary>
public enum TThostFtdcExportFileTypeType : byte
{
	/// <summary>
	/// DBF
	///</summary>
	THOST_FTDC_EFT_DBF = (byte)'2',
	/// <summary>
	/// Excel
	///</summary>
	THOST_FTDC_EFT_EXCEL = (byte)'1',
	/// <summary>
	/// CSV
	///</summary>
	THOST_FTDC_EFT_CSV = (byte)'0',
}

/// <summary>
/// 结算配置类型类型
///</summary>
public enum TThostFtdcSettleManagerTypeType : byte
{
	/// <summary>
	/// 结算后处理
	///</summary>
	THOST_FTDC_SMT_Settlemented = (byte)'4',
	/// <summary>
	/// 结算后核对
	///</summary>
	THOST_FTDC_SMT_After = (byte)'3',
	/// <summary>
	/// 结算
	///</summary>
	THOST_FTDC_SMT_Settlement = (byte)'2',
	/// <summary>
	/// 结算前准备
	///</summary>
	THOST_FTDC_SMT_Before = (byte)'1',
}

/// <summary>
/// 结算配置等级类型
///</summary>
public enum TThostFtdcSettleManagerLevelType : byte
{
	/// <summary>
	/// 不检查
	///</summary>
	THOST_FTDC_SML_Ignore = (byte)'4',
	/// <summary>
	/// 提示
	///</summary>
	THOST_FTDC_SML_Prompt = (byte)'3',
	/// <summary>
	/// 警告
	///</summary>
	THOST_FTDC_SML_Alarm = (byte)'2',
	/// <summary>
	/// 必要
	///</summary>
	THOST_FTDC_SML_Must = (byte)'1',
}

/// <summary>
/// 模块分组类型
///</summary>
public enum TThostFtdcSettleManagerGroupType : byte
{
	/// <summary>
	/// 上报数据核对
	///</summary>
	THOST_FTDC_SMG_CSRC = (byte)'3',
	/// <summary>
	/// 内部核对
	///</summary>
	THOST_FTDC_SMG_ASP = (byte)'2',
	/// <summary>
	/// 交易所核对
	///</summary>
	THOST_FTDC_SMG_Exhcange = (byte)'1',
}

/// <summary>
/// 保值额度使用类型类型
///</summary>
public enum TThostFtdcLimitUseTypeType : byte
{
	/// <summary>
	/// 不可重复使用
	///</summary>
	THOST_FTDC_LUT_Unrepeatable = (byte)'2',
	/// <summary>
	/// 可重复使用
	///</summary>
	THOST_FTDC_LUT_Repeatable = (byte)'1',
}

/// <summary>
/// 数据来源类型
///</summary>
public enum TThostFtdcDataResourceType : byte
{
	/// <summary>
	/// 报送数据
	///</summary>
	THOST_FTDC_DAR_CSRC = (byte)'3',
	/// <summary>
	/// 交易所
	///</summary>
	THOST_FTDC_DAR_Exchange = (byte)'2',
	/// <summary>
	/// 本系统
	///</summary>
	THOST_FTDC_DAR_Settle = (byte)'1',
}

/// <summary>
/// 保证金类型类型
///</summary>
public enum TThostFtdcMarginTypeType : byte
{
	/// <summary>
	/// 投资者交易保证金率
	///</summary>
	THOST_FTDC_MGT_InstrMarginRateTrade = (byte)'2',
	/// <summary>
	/// 投资者保证金率
	///</summary>
	THOST_FTDC_MGT_InstrMarginRate = (byte)'1',
	/// <summary>
	/// 交易所保证金率
	///</summary>
	THOST_FTDC_MGT_ExchMarginRate = (byte)'0',
}

/// <summary>
/// 生效类型类型
///</summary>
public enum TThostFtdcActiveTypeType : byte
{
	/// <summary>
	/// 长期生效
	///</summary>
	THOST_FTDC_ACT_Long = (byte)'2',
	/// <summary>
	/// 仅当日生效
	///</summary>
	THOST_FTDC_ACT_Intraday = (byte)'1',
}

/// <summary>
/// 冲突保证金率类型类型
///</summary>
public enum TThostFtdcMarginRateTypeType : byte
{
	/// <summary>
	/// 投资者交易保证金率
	///</summary>
	THOST_FTDC_MRT_InvestorTrade = (byte)'3',
	/// <summary>
	/// 投资者保证金率
	///</summary>
	THOST_FTDC_MRT_Investor = (byte)'2',
	/// <summary>
	/// 交易所保证金率
	///</summary>
	THOST_FTDC_MRT_Exchange = (byte)'1',
}

/// <summary>
/// 备份数据状态类型
///</summary>
public enum TThostFtdcBackUpStatusType : byte
{
	/// <summary>
	/// 备份数据失败
	///</summary>
	THOST_FTDC_BUS_BakFail = (byte)'3',
	/// <summary>
	/// 已生成备份数据
	///</summary>
	THOST_FTDC_BUS_BakUped = (byte)'2',
	/// <summary>
	/// 备份数据生成中
	///</summary>
	THOST_FTDC_BUS_BakUp = (byte)'1',
	/// <summary>
	/// 未生成备份数据
	///</summary>
	THOST_FTDC_BUS_UnBak = (byte)'0',
}

/// <summary>
/// 结算初始化状态类型
///</summary>
public enum TThostFtdcInitSettlementType : byte
{
	/// <summary>
	/// 结算初始化完成
	///</summary>
	THOST_FTDC_SIS_Initialized = (byte)'2',
	/// <summary>
	/// 结算初始化中
	///</summary>
	THOST_FTDC_SIS_Initialize = (byte)'1',
	/// <summary>
	/// 结算初始化未开始
	///</summary>
	THOST_FTDC_SIS_UnInitialize = (byte)'0',
}

/// <summary>
/// 报表数据生成状态类型
///</summary>
public enum TThostFtdcReportStatusType : byte
{
	/// <summary>
	/// 生成报表数据失败
	///</summary>
	THOST_FTDC_SRS_CreateFail = (byte)'3',
	/// <summary>
	/// 已生成报表数据
	///</summary>
	THOST_FTDC_SRS_Created = (byte)'2',
	/// <summary>
	/// 报表数据生成中
	///</summary>
	THOST_FTDC_SRS_Create = (byte)'1',
	/// <summary>
	/// 未生成报表数据
	///</summary>
	THOST_FTDC_SRS_NoCreate = (byte)'0',
}

/// <summary>
/// 数据归档状态类型
///</summary>
public enum TThostFtdcSaveStatusType : byte
{
	/// <summary>
	/// 归档完成
	///</summary>
	THOST_FTDC_SSS_SaveDatad = (byte)'1',
	/// <summary>
	/// 归档未完成
	///</summary>
	THOST_FTDC_SSS_UnSaveData = (byte)'0',
}

/// <summary>
/// 结算确认数据归档状态类型
///</summary>
public enum TThostFtdcSettArchiveStatusType : byte
{
	/// <summary>
	/// 归档数据失败
	///</summary>
	THOST_FTDC_SAS_ArchiveFail = (byte)'3',
	/// <summary>
	/// 已归档数据
	///</summary>
	THOST_FTDC_SAS_Archived = (byte)'2',
	/// <summary>
	/// 数据归档中
	///</summary>
	THOST_FTDC_SAS_Archiving = (byte)'1',
	/// <summary>
	/// 未归档数据
	///</summary>
	THOST_FTDC_SAS_UnArchived = (byte)'0',
}

/// <summary>
/// CTP交易系统类型类型
///</summary>
public enum TThostFtdcCTPTypeType : byte
{
	/// <summary>
	/// 备中心
	///</summary>
	THOST_FTDC_CTPT_BackUp = (byte)'2',
	/// <summary>
	/// 主中心
	///</summary>
	THOST_FTDC_CTPT_MainCenter = (byte)'1',
	/// <summary>
	/// 未知类型
	///</summary>
	THOST_FTDC_CTPT_Unkown = (byte)'0',
}

/// <summary>
/// 平仓处理类型类型
///</summary>
public enum TThostFtdcCloseDealTypeType : byte
{
	/// <summary>
	/// 投机平仓优先
	///</summary>
	THOST_FTDC_CDT_SpecFirst = (byte)'1',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_CDT_Normal = (byte)'0',
}

/// <summary>
/// 货币质押资金可用范围类型
///</summary>
public enum TThostFtdcMortgageFundUseRangeType : byte
{
	/// <summary>
	/// 人民币方案3
	///</summary>
	THOST_FTDC_MFUR_CNY3 = (byte)'3',
	/// <summary>
	/// 用于手续费、盈亏、保证金
	///</summary>
	THOST_FTDC_MFUR_All = (byte)'2',
	/// <summary>
	/// 用于保证金
	///</summary>
	THOST_FTDC_MFUR_Margin = (byte)'1',
	/// <summary>
	/// 不能使用
	///</summary>
	THOST_FTDC_MFUR_None = (byte)'0',
}

/// <summary>
/// 特殊产品类型类型
///</summary>
public enum TThostFtdcSpecProductTypeType : byte
{
	/// <summary>
	/// 大连短线开平仓产品
	///</summary>
	THOST_FTDC_SPT_DceOpenClose = (byte)'3',
	/// <summary>
	/// 货币质押产品
	///</summary>
	THOST_FTDC_SPT_IneForeignCurrency = (byte)'2',
	/// <summary>
	/// 郑商所套保产品
	///</summary>
	THOST_FTDC_SPT_CzceHedge = (byte)'1',
}

/// <summary>
/// 货币质押类型类型
///</summary>
public enum TThostFtdcFundMortgageTypeType : byte
{
	/// <summary>
	/// 解质
	///</summary>
	THOST_FTDC_FMT_Redemption = (byte)'2',
	/// <summary>
	/// 质押
	///</summary>
	THOST_FTDC_FMT_Mortgage = (byte)'1',
}

/// <summary>
/// 投资者账户结算参数代码类型
///</summary>
public enum TThostFtdcAccountSettlementParamIDType : byte
{
	/// <summary>
	/// 最低权益标准
	///</summary>
	THOST_FTDC_ASPI_LowestInterest = (byte)'2',
	/// <summary>
	/// 基础保证金
	///</summary>
	THOST_FTDC_ASPI_BaseMargin = (byte)'1',
}

/// <summary>
/// 货币质押方向类型
///</summary>
public enum TThostFtdcFundMortDirectionType : byte
{
	/// <summary>
	/// 货币质出
	///</summary>
	THOST_FTDC_FMD_Out = (byte)'2',
	/// <summary>
	/// 货币质入
	///</summary>
	THOST_FTDC_FMD_In = (byte)'1',
}

/// <summary>
/// 换汇类别类型
///</summary>
public enum TThostFtdcBusinessClassType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_BT_Other = (byte)'Z',
	/// <summary>
	/// 亏损
	///</summary>
	THOST_FTDC_BT_Loss = (byte)'1',
	/// <summary>
	/// 盈利
	///</summary>
	THOST_FTDC_BT_Profit = (byte)'0',
}

/// <summary>
/// 换汇数据来源类型
///</summary>
public enum TThostFtdcSwapSourceTypeType : byte
{
	/// <summary>
	/// 自动生成
	///</summary>
	THOST_FTDC_SST_Automatic = (byte)'1',
	/// <summary>
	/// 手工
	///</summary>
	THOST_FTDC_SST_Manual = (byte)'0',
}

/// <summary>
/// 换汇类型类型
///</summary>
public enum TThostFtdcCurrExDirectionType : byte
{
	/// <summary>
	/// 售汇
	///</summary>
	THOST_FTDC_CED_Sale = (byte)'1',
	/// <summary>
	/// 结汇
	///</summary>
	THOST_FTDC_CED_Settlement = (byte)'0',
}

/// <summary>
/// 申请状态类型
///</summary>
public enum TThostFtdcCurrencySwapStatusType : byte
{
	/// <summary>
	/// 换汇失败
	///</summary>
	THOST_FTDC_CSS_Failure = (byte)'7',
	/// <summary>
	/// 换汇成功
	///</summary>
	THOST_FTDC_CSS_Success = (byte)'6',
	/// <summary>
	/// 已发送
	///</summary>
	THOST_FTDC_CSS_Send = (byte)'5',
	/// <summary>
	/// 已撤销
	///</summary>
	THOST_FTDC_CSS_Revoke = (byte)'4',
	/// <summary>
	/// 已拒绝
	///</summary>
	THOST_FTDC_CSS_Refuse = (byte)'3',
	/// <summary>
	/// 已审核
	///</summary>
	THOST_FTDC_CSS_Approve = (byte)'2',
	/// <summary>
	/// 已录入
	///</summary>
	THOST_FTDC_CSS_Entry = (byte)'1',
}

/// <summary>
/// 换汇发送标志类型
///</summary>
public enum TThostFtdcReqFlagType : byte
{
	/// <summary>
	/// 等待重发
	///</summary>
	THOST_FTDC_REQF_WaitReSend = (byte)'3',
	/// <summary>
	/// 发送失败
	///</summary>
	THOST_FTDC_REQF_SendFailed = (byte)'2',
	/// <summary>
	/// 发送成功
	///</summary>
	THOST_FTDC_REQF_SendSuccess = (byte)'1',
	/// <summary>
	/// 未发送
	///</summary>
	THOST_FTDC_REQF_NoSend = (byte)'0',
}

/// <summary>
/// 换汇返回成功标志类型
///</summary>
public enum TThostFtdcResFlagType : byte
{
	/// <summary>
	/// 交易结果未知
	///</summary>
	THOST_FTDC_RESF_UnKnown = (byte)'8',
	/// <summary>
	/// 账户余额不足
	///</summary>
	THOST_FTDC_RESF_InsuffiCient = (byte)'1',
	/// <summary>
	/// 成功
	///</summary>
	THOST_FTDC_RESF_Success = (byte)'0',
}

/// <summary>
/// 修改状态类型
///</summary>
public enum TThostFtdcExStatusType : byte
{
	/// <summary>
	/// 修改后
	///</summary>
	THOST_FTDC_EXS_After = (byte)'1',
	/// <summary>
	/// 修改前
	///</summary>
	THOST_FTDC_EXS_Before = (byte)'0',
}

/// <summary>
/// 开户客户地域类型
///</summary>
public enum TThostFtdcClientRegionType : byte
{
	/// <summary>
	/// 国外客户
	///</summary>
	THOST_FTDC_CR_Foreign = (byte)'3',
	/// <summary>
	/// 港澳台客户
	///</summary>
	THOST_FTDC_CR_GMT = (byte)'2',
	/// <summary>
	/// 国内客户
	///</summary>
	THOST_FTDC_CR_Domestic = (byte)'1',
}

/// <summary>
/// 是否有董事会类型
///</summary>
public enum TThostFtdcHasBoardType : byte
{
	/// <summary>
	/// 有
	///</summary>
	THOST_FTDC_HB_Yes = (byte)'1',
	/// <summary>
	/// 没有
	///</summary>
	THOST_FTDC_HB_No = (byte)'0',
}

/// <summary>
/// 启动模式类型
///</summary>
public enum TThostFtdcStartModeType : byte
{
	/// <summary>
	/// 恢复
	///</summary>
	THOST_FTDC_SM_Restore = (byte)'3',
	/// <summary>
	/// 应急
	///</summary>
	THOST_FTDC_SM_Emerge = (byte)'2',
	/// <summary>
	/// 正常
	///</summary>
	THOST_FTDC_SM_Normal = (byte)'1',
}

/// <summary>
/// 模型类型类型
///</summary>
public enum TThostFtdcTemplateTypeType : byte
{
	/// <summary>
	/// 备份
	///</summary>
	THOST_FTDC_TPT_BackUp = (byte)'3',
	/// <summary>
	/// 增量
	///</summary>
	THOST_FTDC_TPT_Increment = (byte)'2',
	/// <summary>
	/// 全量
	///</summary>
	THOST_FTDC_TPT_Full = (byte)'1',
}

/// <summary>
/// 登录模式类型
///</summary>
public enum TThostFtdcLoginModeType : byte
{
	/// <summary>
	/// 转账
	///</summary>
	THOST_FTDC_LM_Transfer = (byte)'1',
	/// <summary>
	/// 交易
	///</summary>
	THOST_FTDC_LM_Trade = (byte)'0',
}

/// <summary>
/// 日历提示类型类型
///</summary>
public enum TThostFtdcPromptTypeType : byte
{
	/// <summary>
	/// 保证金分段生效
	///</summary>
	THOST_FTDC_CPT_Margin = (byte)'2',
	/// <summary>
	/// 合约上下市
	///</summary>
	THOST_FTDC_CPT_Instrument = (byte)'1',
}

/// <summary>
/// 是否有托管人类型
///</summary>
public enum TThostFtdcHasTrusteeType : byte
{
	/// <summary>
	/// 没有
	///</summary>
	THOST_FTDC_HT_No = (byte)'0',
	/// <summary>
	/// 有
	///</summary>
	THOST_FTDC_HT_Yes = (byte)'1',
}

/// <summary>
/// 机构类型类型
///</summary>
public enum TThostFtdcAmTypeType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_AMT_Other = (byte)'9',
	/// <summary>
	/// 信托公司
	///</summary>
	THOST_FTDC_AMT_Trust = (byte)'5',
	/// <summary>
	/// 保险公司
	///</summary>
	THOST_FTDC_AMT_Insurance = (byte)'4',
	/// <summary>
	/// 基金公司
	///</summary>
	THOST_FTDC_AMT_Fund = (byte)'3',
	/// <summary>
	/// 证券公司
	///</summary>
	THOST_FTDC_AMT_Securities = (byte)'2',
	/// <summary>
	/// 银行
	///</summary>
	THOST_FTDC_AMT_Bank = (byte)'1',
}

/// <summary>
/// 出入金类型类型
///</summary>
public enum TThostFtdcCSRCFundIOTypeType : byte
{
	/// <summary>
	/// 银期换汇
	///</summary>
	THOST_FTDC_CFIOT_SwapCurrency = (byte)'1',
	/// <summary>
	/// 出入金
	///</summary>
	THOST_FTDC_CFIOT_FundIO = (byte)'0',
}

/// <summary>
/// 结算账户类型类型
///</summary>
public enum TThostFtdcCusAccountTypeType : byte
{
	/// <summary>
	/// 综合类资管业务下的资金中转账户
	///</summary>
	THOST_FTDC_CAT_AssetmgrTransfer = (byte)'4',
	/// <summary>
	/// 综合类资管业务下的期货资管托管账户
	///</summary>
	THOST_FTDC_CAT_AssetmgrTrustee = (byte)'3',
	/// <summary>
	/// 纯期货资管业务下的资管结算账户
	///</summary>
	THOST_FTDC_CAT_AssetmgrFuture = (byte)'2',
	/// <summary>
	/// 期货结算账户
	///</summary>
	THOST_FTDC_CAT_Futures = (byte)'1',
}

/// <summary>
/// 通知语言类型类型
///</summary>
public enum TThostFtdcLanguageTypeType : byte
{
	/// <summary>
	/// 英文
	///</summary>
	THOST_FTDC_LT_English = (byte)'2',
	/// <summary>
	/// 中文
	///</summary>
	THOST_FTDC_LT_Chinese = (byte)'1',
}

/// <summary>
/// 资产管理客户类型类型
///</summary>
public enum TThostFtdcAssetmgrClientTypeType : byte
{
	/// <summary>
	/// 特殊单位资管客户
	///</summary>
	THOST_FTDC_AMCT_SpecialOrgan = (byte)'4',
	/// <summary>
	/// 单位资管客户
	///</summary>
	THOST_FTDC_AMCT_Organ = (byte)'2',
	/// <summary>
	/// 个人资管客户
	///</summary>
	THOST_FTDC_AMCT_Person = (byte)'1',
}

/// <summary>
/// 投资类型类型
///</summary>
public enum TThostFtdcAssetmgrTypeType : byte
{
	/// <summary>
	/// 综合类
	///</summary>
	THOST_FTDC_ASST_SpecialOrgan = (byte)'4',
	/// <summary>
	/// 期货类
	///</summary>
	THOST_FTDC_ASST_Futures = (byte)'3',
}

/// <summary>
/// 合约比较类型类型
///</summary>
public enum TThostFtdcCheckInstrTypeType : byte
{
	/// <summary>
	/// 合约比较不一致
	///</summary>
	THOST_FTDC_CIT_HasDiff = (byte)'2',
	/// <summary>
	/// 合约本系统不存在
	///</summary>
	THOST_FTDC_CIT_HasATP = (byte)'1',
	/// <summary>
	/// 合约交易所不存在
	///</summary>
	THOST_FTDC_CIT_HasExch = (byte)'0',
}

/// <summary>
/// 交割类型类型
///</summary>
public enum TThostFtdcDeliveryTypeType : byte
{
	/// <summary>
	/// 到期交割
	///</summary>
	THOST_FTDC_DT_PersonDeliv = (byte)'2',
	/// <summary>
	/// 手工交割
	///</summary>
	THOST_FTDC_DT_HandDeliv = (byte)'1',
}

/// <summary>
/// 大额单边保证金算法类型
///</summary>
public enum TThostFtdcMaxMarginSideAlgorithmType : byte
{
	/// <summary>
	/// 使用大额单边保证金算法
	///</summary>
	THOST_FTDC_MMSA_YES = (byte)'1',
	/// <summary>
	/// 不使用大额单边保证金算法
	///</summary>
	THOST_FTDC_MMSA_NO = (byte)'0',
}

/// <summary>
/// 资产管理客户类型类型
///</summary>
public enum TThostFtdcDAClientTypeType : byte
{
	/// <summary>
	/// 其他
	///</summary>
	THOST_FTDC_CACT_Other = (byte)'2',
	/// <summary>
	/// 法人
	///</summary>
	THOST_FTDC_CACT_Company = (byte)'1',
	/// <summary>
	/// 自然人
	///</summary>
	THOST_FTDC_CACT_Person = (byte)'0',
}

/// <summary>
/// 投资类型类型
///</summary>
public enum TThostFtdcUOAAssetmgrTypeType : byte
{
	/// <summary>
	/// 综合类
	///</summary>
	THOST_FTDC_UOAAT_SpecialOrgan = (byte)'2',
	/// <summary>
	/// 期货类
	///</summary>
	THOST_FTDC_UOAAT_Futures = (byte)'1',
}

/// <summary>
/// 买卖方向类型
///</summary>
public enum TThostFtdcDirectionEnType : byte
{
	/// <summary>
	/// Sell
	///</summary>
	THOST_FTDC_DEN_Sell = (byte)'1',
	/// <summary>
	/// Buy
	///</summary>
	THOST_FTDC_DEN_Buy = (byte)'0',
}

/// <summary>
/// 开平标志类型
///</summary>
public enum TThostFtdcOffsetFlagEnType : byte
{
	/// <summary>
	/// Local Forced Liquidation
	///</summary>
	THOST_FTDC_OFEN_LocalForceClose = (byte)'6',
	/// <summary>
	/// Forced Reduction
	///</summary>
	THOST_FTDC_OFEN_ForceOff = (byte)'5',
	/// <summary>
	/// Close Prev.
	///</summary>
	THOST_FTDC_OFEN_CloseYesterday = (byte)'4',
	/// <summary>
	/// Close Today
	///</summary>
	THOST_FTDC_OFEN_CloseToday = (byte)'3',
	/// <summary>
	/// Forced Liquidation
	///</summary>
	THOST_FTDC_OFEN_ForceClose = (byte)'2',
	/// <summary>
	/// Position Close
	///</summary>
	THOST_FTDC_OFEN_Close = (byte)'1',
	/// <summary>
	/// Position Opening
	///</summary>
	THOST_FTDC_OFEN_Open = (byte)'0',
}

/// <summary>
/// 投机套保标志类型
///</summary>
public enum TThostFtdcHedgeFlagEnType : byte
{
	/// <summary>
	/// Hedge
	///</summary>
	THOST_FTDC_HFEN_Hedge = (byte)'3',
	/// <summary>
	/// Arbitrage
	///</summary>
	THOST_FTDC_HFEN_Arbitrage = (byte)'2',
	/// <summary>
	/// Speculation
	///</summary>
	THOST_FTDC_HFEN_Speculation = (byte)'1',
}

/// <summary>
/// 出入金类型类型
///</summary>
public enum TThostFtdcFundIOTypeEnType : byte
{
	/// <summary>
	/// Bank-Futures FX Exchange
	///</summary>
	THOST_FTDC_FIOTEN_SwapCurrency = (byte)'3',
	/// <summary>
	/// Bank-Futures Transfer
	///</summary>
	THOST_FTDC_FIOTEN_Transfer = (byte)'2',
	/// <summary>
	/// Deposit/Withdrawal
	///</summary>
	THOST_FTDC_FIOTEN_FundIO = (byte)'1',
}

/// <summary>
/// 资金类型类型
///</summary>
public enum TThostFtdcFundTypeEnType : byte
{
	/// <summary>
	/// Internal Transfer
	///</summary>
	THOST_FTDC_FTEN_InnerTransfer = (byte)'4',
	/// <summary>
	/// Brokerage Adj
	///</summary>
	THOST_FTDC_FTEN_Company = (byte)'3',
	/// <summary>
	/// Payment/Fee
	///</summary>
	THOST_FTDC_FTEN_ItemFund = (byte)'2',
	/// <summary>
	/// Bank Deposit
	///</summary>
	THOST_FTDC_FTEN_Deposite = (byte)'1',
}

/// <summary>
/// 出入金方向类型
///</summary>
public enum TThostFtdcFundDirectionEnType : byte
{
	/// <summary>
	/// Withdrawal
	///</summary>
	THOST_FTDC_FDEN_Out = (byte)'2',
	/// <summary>
	/// Deposit
	///</summary>
	THOST_FTDC_FDEN_In = (byte)'1',
}

/// <summary>
/// 货币质押方向类型
///</summary>
public enum TThostFtdcFundMortDirectionEnType : byte
{
	/// <summary>
	/// Redemption
	///</summary>
	THOST_FTDC_FMDEN_Out = (byte)'2',
	/// <summary>
	/// Pledge
	///</summary>
	THOST_FTDC_FMDEN_In = (byte)'1',
}

/// <summary>
/// 期权类型类型
///</summary>
public enum TThostFtdcOptionsTypeType : byte
{
	/// <summary>
	/// 看跌
	///</summary>
	THOST_FTDC_CP_PutOptions = (byte)'2',
	/// <summary>
	/// 看涨
	///</summary>
	THOST_FTDC_CP_CallOptions = (byte)'1',
}

/// <summary>
/// 执行方式类型
///</summary>
public enum TThostFtdcStrikeModeType : byte
{
	/// <summary>
	/// 百慕大
	///</summary>
	THOST_FTDC_STM_Bermuda = (byte)'2',
	/// <summary>
	/// 美式
	///</summary>
	THOST_FTDC_STM_American = (byte)'1',
	/// <summary>
	/// 欧式
	///</summary>
	THOST_FTDC_STM_Continental = (byte)'0',
}

/// <summary>
/// 执行类型类型
///</summary>
public enum TThostFtdcStrikeTypeType : byte
{
	/// <summary>
	/// 匹配执行
	///</summary>
	THOST_FTDC_STT_Match = (byte)'1',
	/// <summary>
	/// 自身对冲
	///</summary>
	THOST_FTDC_STT_Hedge = (byte)'0',
}

/// <summary>
/// 中金所期权放弃执行申请类型类型
///</summary>
public enum TThostFtdcApplyTypeType : byte
{
	/// <summary>
	/// 不执行数量
	///</summary>
	THOST_FTDC_APPT_NotStrikeNum = (byte)'4',
}

/// <summary>
/// 放弃执行申请数据来源类型
///</summary>
public enum TThostFtdcGiveUpDataSourceType : byte
{
	/// <summary>
	/// 手工添加
	///</summary>
	THOST_FTDC_GUDS_Hand = (byte)'1',
	/// <summary>
	/// 系统生成
	///</summary>
	THOST_FTDC_GUDS_Gen = (byte)'0',
}

/// <summary>
/// 执行结果类型
///</summary>
public enum TThostFtdcExecResultType : byte
{
	/// <summary>
	/// 未知
	///</summary>
	THOST_FTDC_OER_Unknown = (byte)'a',
	/// <summary>
	/// 没有足够的历史成交
	///</summary>
	THOST_FTDC_OER_NoEnoughHistoryTrade = (byte)'9',
	/// <summary>
	/// 不合理的数量
	///</summary>
	THOST_FTDC_OER_InvalidVolume = (byte)'8',
	/// <summary>
	/// 没有执行权限
	///</summary>
	THOST_FTDC_OER_NoRight = (byte)'7',
	/// <summary>
	/// 合约不存在
	///</summary>
	THOST_FTDC_OER_NoInstrument = (byte)'6',
	/// <summary>
	/// 客户不存在
	///</summary>
	THOST_FTDC_OER_NoClient = (byte)'4',
	/// <summary>
	/// 会员不存在
	///</summary>
	THOST_FTDC_OER_NoParticipant = (byte)'3',
	/// <summary>
	/// 资金不够
	///</summary>
	THOST_FTDC_OER_NoDeposit = (byte)'2',
	/// <summary>
	/// 期权持仓不够
	///</summary>
	THOST_FTDC_OER_NoPosition = (byte)'1',
	/// <summary>
	/// 执行成功
	///</summary>
	THOST_FTDC_OER_OK = (byte)'0',
	/// <summary>
	/// 已经取消
	///</summary>
	THOST_FTDC_OER_Canceled = (byte)'c',
	/// <summary>
	/// 没有执行
	///</summary>
	THOST_FTDC_OER_NoExec = (byte)'n',
}

/// <summary>
/// 组合类型类型
///</summary>
public enum TThostFtdcCombinationTypeType : byte
{
	/// <summary>
	/// 时间价差组合
	///</summary>
	THOST_FTDC_COMBT_CLD = (byte)'6',
	/// <summary>
	/// 备兑组合
	///</summary>
	THOST_FTDC_COMBT_PRT = (byte)'5',
	/// <summary>
	/// 宽跨式组合
	///</summary>
	THOST_FTDC_COMBT_STG = (byte)'4',
	/// <summary>
	/// 跨式组合
	///</summary>
	THOST_FTDC_COMBT_STD = (byte)'3',
	/// <summary>
	/// 垂直价差BER
	///</summary>
	THOST_FTDC_COMBT_BER = (byte)'2',
	/// <summary>
	/// 垂直价差BUL
	///</summary>
	THOST_FTDC_COMBT_BUL = (byte)'1',
	/// <summary>
	/// 期货组合
	///</summary>
	THOST_FTDC_COMBT_Future = (byte)'0',
}

/// <summary>
/// 组合类型类型
///</summary>
public enum TThostFtdcDceCombinationTypeType : byte
{
	/// <summary>
	/// 卖出期货期权组合
	///</summary>
	THOST_FTDC_DCECOMBT_SFO = (byte)'a',
	/// <summary>
	/// 买入期货期权组合
	///</summary>
	THOST_FTDC_DCECOMBT_BFO = (byte)'9',
	/// <summary>
	/// 期权宽跨式组合
	///</summary>
	THOST_FTDC_DCECOMBT_STG = (byte)'8',
	/// <summary>
	/// 期权跨式组合
	///</summary>
	THOST_FTDC_DCECOMBT_STD = (byte)'7',
	/// <summary>
	/// 期权日历价差组合
	///</summary>
	THOST_FTDC_DCECOMBT_CAS = (byte)'6',
	/// <summary>
	/// 卖出期权垂直价差组合
	///</summary>
	THOST_FTDC_DCECOMBT_BES = (byte)'5',
	/// <summary>
	/// 买入期权垂直价差组合
	///</summary>
	THOST_FTDC_DCECOMBT_BLS = (byte)'4',
	/// <summary>
	/// 期货跨品种组合
	///</summary>
	THOST_FTDC_DCECOMBT_SPC = (byte)'3',
	/// <summary>
	/// 期货跨期组合
	///</summary>
	THOST_FTDC_DCECOMBT_SP = (byte)'2',
	/// <summary>
	/// 期权对锁组合
	///</summary>
	THOST_FTDC_DCECOMBT_OPL = (byte)'1',
	/// <summary>
	/// 期货对锁组合
	///</summary>
	THOST_FTDC_DCECOMBT_SPL = (byte)'0',
}

/// <summary>
/// 期权权利金价格类型类型
///</summary>
public enum TThostFtdcOptionRoyaltyPriceTypeType : byte
{
	/// <summary>
	/// 最新价与昨结算价较大值
	///</summary>
	THOST_FTDC_ORPT_MaxPreSettlementPrice = (byte)'5',
	/// <summary>
	/// 开仓价
	///</summary>
	THOST_FTDC_ORPT_OpenPrice = (byte)'4',
	/// <summary>
	/// 昨结算价
	///</summary>
	THOST_FTDC_ORPT_PreSettlementPrice = (byte)'1',
}

/// <summary>
/// 权益算法类型
///</summary>
public enum TThostFtdcBalanceAlgorithmType : byte
{
	/// <summary>
	/// 计算期权市值亏损
	///</summary>
	THOST_FTDC_BLAG_IncludeOptValLost = (byte)'2',
	/// <summary>
	/// 不计算期权市值盈亏
	///</summary>
	THOST_FTDC_BLAG_Default = (byte)'1',
}

/// <summary>
/// 执行类型类型
///</summary>
public enum TThostFtdcActionTypeType : byte
{
	/// <summary>
	/// 放弃
	///</summary>
	THOST_FTDC_ACTP_Abandon = (byte)'2',
	/// <summary>
	/// 执行
	///</summary>
	THOST_FTDC_ACTP_Exec = (byte)'1',
}

/// <summary>
/// 询价状态类型
///</summary>
public enum TThostFtdcForQuoteStatusType : byte
{
	/// <summary>
	/// 已经被拒绝
	///</summary>
	THOST_FTDC_FQST_Rejected = (byte)'c',
	/// <summary>
	/// 已经接受
	///</summary>
	THOST_FTDC_FQST_Accepted = (byte)'b',
	/// <summary>
	/// 已经提交
	///</summary>
	THOST_FTDC_FQST_Submitted = (byte)'a',
}

/// <summary>
/// 取值方式类型
///</summary>
public enum TThostFtdcValueMethodType : byte
{
	/// <summary>
	/// 按比率
	///</summary>
	THOST_FTDC_VM_Ratio = (byte)'1',
	/// <summary>
	/// 按绝对值
	///</summary>
	THOST_FTDC_VM_Absolute = (byte)'0',
}

/// <summary>
/// 期权行权后是否保留期货头寸的标记类型
///</summary>
public enum TThostFtdcExecOrderPositionFlagType : byte
{
	/// <summary>
	/// 不保留
	///</summary>
	THOST_FTDC_EOPF_UnReserve = (byte)'1',
	/// <summary>
	/// 保留
	///</summary>
	THOST_FTDC_EOPF_Reserve = (byte)'0',
}

/// <summary>
/// 期权行权后生成的头寸是否自动平仓类型
///</summary>
public enum TThostFtdcExecOrderCloseFlagType : byte
{
	/// <summary>
	/// 免于自动平仓
	///</summary>
	THOST_FTDC_EOCF_NotToClose = (byte)'1',
	/// <summary>
	/// 自动平仓
	///</summary>
	THOST_FTDC_EOCF_AutoClose = (byte)'0',
}

/// <summary>
/// 产品类型类型
///</summary>
public enum TThostFtdcProductTypeType : byte
{
	/// <summary>
	/// 期权
	///</summary>
	THOST_FTDC_PTE_Options = (byte)'2',
	/// <summary>
	/// 期货
	///</summary>
	THOST_FTDC_PTE_Futures = (byte)'1',
}

/// <summary>
/// 郑商所结算文件名类型
///</summary>
public enum TThostFtdcCZCEUploadFileNameType : byte
{
	/// <summary>
	/// ^\d{8}保证金参数表
	///</summary>
	THOST_FTDC_CUFN_CUFN_M = (byte)'M',
	/// <summary>
	/// ^\d{8}组合持仓表
	///</summary>
	THOST_FTDC_CUFN_CUFN_C = (byte)'C',
	/// <summary>
	/// ^\d{8}资金表
	///</summary>
	THOST_FTDC_CUFN_CUFN_F = (byte)'F',
	/// <summary>
	/// ^\d{8}平仓表
	///</summary>
	THOST_FTDC_CUFN_CUFN_L = (byte)'L',
	/// <summary>
	/// ^\d{8}非平仓了结表
	///</summary>
	THOST_FTDC_CUFN_CUFN_N = (byte)'N',
	/// <summary>
	/// ^\d{8}单腿持仓表new
	///</summary>
	THOST_FTDC_CUFN_CUFN_P = (byte)'P',
	/// <summary>
	/// ^\d{8}成交表
	///</summary>
	THOST_FTDC_CUFN_CUFN_T = (byte)'T',
	/// <summary>
	/// ^\d{8}_zz_\d{4}
	///</summary>
	THOST_FTDC_CUFN_CUFN_O = (byte)'O',
}

/// <summary>
/// 大商所结算文件名类型
///</summary>
public enum TThostFtdcDCEUploadFileNameType : byte
{
	/// <summary>
	/// ^\d{8}_期权执行表
	///</summary>
	THOST_FTDC_DUFN_DUFN_S = (byte)'S',
	/// <summary>
	/// ^\d{8}_保证金参数表
	///</summary>
	THOST_FTDC_DUFN_DUFN_M = (byte)'M',
	/// <summary>
	/// ^\d{8}_持仓明细表
	///</summary>
	THOST_FTDC_DUFN_DUFN_D = (byte)'D',
	/// <summary>
	/// ^\d{8}_优惠组合持仓明细表
	///</summary>
	THOST_FTDC_DUFN_DUFN_C = (byte)'C',
	/// <summary>
	/// ^\d{8}_资金结算表
	///</summary>
	THOST_FTDC_DUFN_DUFN_F = (byte)'F',
	/// <summary>
	/// ^\d{8}_持仓表
	///</summary>
	THOST_FTDC_DUFN_DUFN_P = (byte)'P',
	/// <summary>
	/// ^\d{8}_成交表
	///</summary>
	THOST_FTDC_DUFN_DUFN_T = (byte)'T',
	/// <summary>
	/// ^\d{8}_dl_\d{3}
	///</summary>
	THOST_FTDC_DUFN_DUFN_O = (byte)'O',
}

/// <summary>
/// 上期所结算文件名类型
///</summary>
public enum TThostFtdcSHFEUploadFileNameType : byte
{
	/// <summary>
	/// ^\d{4}_\d{8}_\d{8}_Capital
	///</summary>
	THOST_FTDC_SUFN_SUFN_F = (byte)'F',
	/// <summary>
	/// ^\d{4}_\d{8}_\d{8}_SettlementDetail
	///</summary>
	THOST_FTDC_SUFN_SUFN_P = (byte)'P',
	/// <summary>
	/// ^\d{4}_\d{8}_\d{8}_Trade
	///</summary>
	THOST_FTDC_SUFN_SUFN_T = (byte)'T',
	/// <summary>
	/// ^\d{4}_\d{8}_\d{8}_DailyFundChg
	///</summary>
	THOST_FTDC_SUFN_SUFN_O = (byte)'O',
}

/// <summary>
/// 中金所结算文件名类型
///</summary>
public enum TThostFtdcCFFEXUploadFileNameType : byte
{
	/// <summary>
	/// ^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec
	///</summary>
	THOST_FTDC_CFUFN_SUFN_S = (byte)'S',
	/// <summary>
	/// ^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
	///</summary>
	THOST_FTDC_CFUFN_SUFN_F = (byte)'F',
	/// <summary>
	/// ^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
	///</summary>
	THOST_FTDC_CFUFN_SUFN_P = (byte)'P',
	/// <summary>
	/// ^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
	///</summary>
	THOST_FTDC_CFUFN_SUFN_T = (byte)'T',
}

/// <summary>
/// 组合指令方向类型
///</summary>
public enum TThostFtdcCombDirectionType : byte
{
	/// <summary>
	/// 申请拆分
	///</summary>
	THOST_FTDC_CMDR_UnComb = (byte)'1',
	/// <summary>
	/// 申请组合
	///</summary>
	THOST_FTDC_CMDR_Comb = (byte)'0',
}

/// <summary>
/// 行权偏移类型类型
///</summary>
public enum TThostFtdcStrikeOffsetTypeType : byte
{
	/// <summary>
	/// 盈利比例
	///</summary>
	THOST_FTDC_STOV_ProfitRatio = (byte)'4',
	/// <summary>
	/// 实值比例
	///</summary>
	THOST_FTDC_STOV_RealRatio = (byte)'3',
	/// <summary>
	/// 盈利额
	///</summary>
	THOST_FTDC_STOV_ProfitValue = (byte)'2',
	/// <summary>
	/// 实值额
	///</summary>
	THOST_FTDC_STOV_RealValue = (byte)'1',
}

/// <summary>
/// 预约开户状态类型
///</summary>
public enum TThostFtdcReserveOpenAccStasType : byte
{
	/// <summary>
	/// 无效请求
	///</summary>
	THOST_FTDC_ROAST_Invalid = (byte)'3',
	/// <summary>
	/// 已开户
	///</summary>
	THOST_FTDC_ROAST_Opened = (byte)'2',
	/// <summary>
	/// 已撤销
	///</summary>
	THOST_FTDC_ROAST_Cancelled = (byte)'1',
	/// <summary>
	/// 等待处理中
	///</summary>
	THOST_FTDC_ROAST_Processing = (byte)'0',
}

/// <summary>
/// 紧急程度类型
///</summary>
public enum TThostFtdcNewsUrgencyType : byte
{
}

/// <summary>
/// 弱密码来源类型
///</summary>
public enum TThostFtdcWeakPasswordSourceType : byte
{
	/// <summary>
	/// 手工录入
	///</summary>
	THOST_FTDC_WPSR_Manual = (byte)'2',
	/// <summary>
	/// 弱密码库
	///</summary>
	THOST_FTDC_WPSR_Lib = (byte)'1',
}

/// <summary>
/// 期权行权的头寸是否自对冲类型
///</summary>
public enum TThostFtdcOptSelfCloseFlagType : byte
{
	/// <summary>
	/// 保留卖方履约后的期货仓位
	///</summary>
	THOST_FTDC_OSCF_ReserveFuturePosition = (byte)'4',
	/// <summary>
	/// 自对冲卖方履约后的期货仓位
	///</summary>
	THOST_FTDC_OSCF_SellCloseSelfFuturePosition = (byte)'3',
	/// <summary>
	/// 保留期权仓位
	///</summary>
	THOST_FTDC_OSCF_ReserveOptionPosition = (byte)'2',
	/// <summary>
	/// 自对冲期权仓位
	///</summary>
	THOST_FTDC_OSCF_CloseSelfOptionPosition = (byte)'1',
}

/// <summary>
/// 业务类型类型
///</summary>
public enum TThostFtdcBizTypeType : byte
{
	/// <summary>
	/// 证券
	///</summary>
	THOST_FTDC_BZTP_Stock = (byte)'2',
	/// <summary>
	/// 期货
	///</summary>
	THOST_FTDC_BZTP_Future = (byte)'1',
}

/// <summary>
/// 用户App类型类型
///</summary>
public enum TThostFtdcAppTypeType : byte
{
	/// <summary>
	/// 未知
	///</summary>
	THOST_FTDC_APP_TYPE_UnKnown = (byte)'4',
	/// <summary>
	/// 所有投资者共享一个操作员连接的中继
	///</summary>
	THOST_FTDC_APP_TYPE_OperatorRelay = (byte)'3',
	/// <summary>
	/// 为每个投资者都创建连接的中继
	///</summary>
	THOST_FTDC_APP_TYPE_InvestorRelay = (byte)'2',
	/// <summary>
	/// 直连的投资者
	///</summary>
	THOST_FTDC_APP_TYPE_Investor = (byte)'1',
}

/// <summary>
/// 应答类型类型
///</summary>
public enum TThostFtdcResponseValueType : byte
{
	/// <summary>
	/// 检查失败
	///</summary>
	THOST_FTDC_RV_Refuse = (byte)'1',
	/// <summary>
	/// 检查成功
	///</summary>
	THOST_FTDC_RV_Right = (byte)'0',
}

/// <summary>
/// OTC成交类型类型
///</summary>
public enum TThostFtdcOTCTradeTypeType : byte
{
	/// <summary>
	/// 期转现
	///</summary>
	THOST_FTDC_OTC_TRDT_EFP = (byte)'1',
	/// <summary>
	/// 大宗交易
	///</summary>
	THOST_FTDC_OTC_TRDT_Block = (byte)'0',
}

/// <summary>
/// 期现风险匹配方式类型
///</summary>
public enum TThostFtdcMatchTypeType : byte
{
	/// <summary>
	/// 面值
	///</summary>
	THOST_FTDC_OTC_MT_ParValue = (byte)'2',
	/// <summary>
	/// 基点价值
	///</summary>
	THOST_FTDC_OTC_MT_DV01 = (byte)'1',
}

