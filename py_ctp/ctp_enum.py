#!/usr/bin/env python
#coding:utf-8

from ctypes import *
from enum import Enum
class ExchangePropertyType(Enum):
	"""交易所属性类型"""
	Normal = 48
	GenOrderByTrade = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class IdCardTypeType(Enum):
	"""证件类型类型"""
	EID = 48
	IDCard = 49
	OfficerIDCard = 50
	PoliceIDCard = 51
	SoldierIDCard = 52
	HouseholdRegister = 53
	Passport = 54
	TaiwanCompatriotIDCard = 55
	HomeComingCard = 56
	LicenseNo = 57
	TaxNo = 65
	HMMainlandTravelPermit = 66
	TwMainlandTravelPermit = 67
	DrivingLicense = 68
	SocialID = 70
	LocalID = 71
	BusinessRegistration = 72
	HKMCIDCard = 73
	AccountsPermits = 74
	OtherCard = 120

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InvestorRangeType(Enum):
	"""投资者范围类型"""
	All = 49
	Group = 50
	Single = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DepartmentRangeType(Enum):
	"""投资者范围类型"""
	All = 49
	Group = 50
	Single = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DataSyncStatusType(Enum):
	"""数据同步状态类型"""
	Asynchronous = 49
	Synchronizing = 50
	Synchronized = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BrokerDataSyncStatusType(Enum):
	"""经纪公司数据同步状态类型"""
	Synchronized = 49
	Synchronizing = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExchangeConnectStatusType(Enum):
	"""交易所连接状态类型"""
	NoConnection = 49
	QryInstrumentSent = 50
	GotInformation = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TraderConnectStatusType(Enum):
	"""交易所交易员连接状态类型"""
	NotConnected = 49
	Connected = 50
	QryInstrumentSent = 51
	SubPrivateFlow = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FunctionCodeType(Enum):
	"""功能代码类型"""
	DataAsync = 49
	ForceUserLogout = 50
	UserPasswordUpdate = 51
	BrokerPasswordUpdate = 52
	InvestorPasswordUpdate = 53
	OrderInsert = 54
	OrderAction = 55
	SyncSystemData = 56
	SyncBrokerData = 57
	BachSyncBrokerData = 65
	SuperQuery = 66
	ParkedOrderInsert = 67
	ParkedOrderAction = 68
	SyncOTP = 69
	DeleteOrder = 70

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BrokerFunctionCodeType(Enum):
	"""经纪公司功能代码类型"""
	ForceUserLogout = 49
	UserPasswordUpdate = 50
	SyncBrokerData = 51
	BachSyncBrokerData = 52
	OrderInsert = 53
	OrderAction = 54
	AllQuery = 55
	log = 97
	BaseQry = 98
	TradeQry = 99
	Trade = 100
	Virement = 101
	Risk = 102
	Session = 103
	RiskNoticeCtl = 104
	RiskNotice = 105
	BrokerDeposit = 106
	QueryFund = 107
	QueryOrder = 108
	QueryTrade = 109
	QueryPosition = 110
	QueryMarketData = 111
	QueryUserEvent = 112
	QueryRiskNotify = 113
	QueryFundChange = 114
	QueryInvestor = 115
	QueryTradingCode = 116
	ForceClose = 117
	PressTest = 118
	RemainCalc = 119
	NetPositionInd = 120
	RiskPredict = 121
	DataExport = 122
	RiskTargetSetup = 65
	MarketDataWarn = 66
	QryBizNotice = 67
	CfgBizNotice = 68
	SyncOTP = 69
	SendBizNotice = 70
	CfgRiskLevelStd = 71
	TbCommand = 72
	DeleteOrder = 74
	ParkedOrderInsert = 75
	ParkedOrderAction = 76
	ExecOrderNoCheck = 77

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderActionStatusType(Enum):
	"""报单操作状态类型"""
	Submitted = 97
	Accepted = 98
	Rejected = 99

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderStatusType(Enum):
	"""报单状态类型"""
	AllTraded = 48
	PartTradedQueueing = 49
	PartTradedNotQueueing = 50
	NoTradeQueueing = 51
	NoTradeNotQueueing = 52
	Canceled = 53
	Unknown = 97
	NotTouched = 98
	Touched = 99

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderSubmitStatusType(Enum):
	"""报单提交状态类型"""
	InsertSubmitted = 48
	CancelSubmitted = 49
	ModifySubmitted = 50
	Accepted = 51
	InsertRejected = 52
	CancelRejected = 53
	ModifyRejected = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PositionDateType(Enum):
	"""持仓日期类型"""
	Today = 49
	History = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PositionDateTypeType(Enum):
	"""持仓日期类型类型"""
	UseHistory = 49
	NoUseHistory = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradingRoleType(Enum):
	"""交易角色类型"""
	Broker = 49
	Host = 50
	Maker = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ProductClassType(Enum):
	"""产品类型类型"""
	Futures = 49
	Options = 50
	Combination = 51
	Spot = 52
	EFP = 53
	SpotOption = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InstLifePhaseType(Enum):
	"""合约生命周期状态类型"""
	NotStart = 48
	Started = 49
	Pause = 50
	Expired = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DirectionType(Enum):
	"""买卖方向类型"""
	Buy = 48
	Sell = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PositionTypeType(Enum):
	"""持仓类型类型"""
	Net = 49
	Gross = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PosiDirectionType(Enum):
	"""持仓多空方向类型"""
	Net = 49
	Long = 50
	Short = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SysSettlementStatusType(Enum):
	"""系统结算状态类型"""
	NonActive = 49
	Startup = 50
	Operating = 51
	Settlement = 52
	SettlementFinished = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RatioAttrType(Enum):
	"""费率属性类型"""
	Trade = 48
	Settlement = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HedgeFlagType(Enum):
	"""投机套保标志类型"""
	Speculation = 49
	Arbitrage = 50
	Hedge = 51
	MarketMaker = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BillHedgeFlagType(Enum):
	"""投机套保标志类型"""
	Speculation = 49
	Arbitrage = 50
	Hedge = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ClientIDTypeType(Enum):
	"""交易编码类型类型"""
	Speculation = 49
	Arbitrage = 50
	Hedge = 51
	MarketMaker = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderPriceTypeType(Enum):
	"""报单价格条件类型"""
	AnyPrice = 49
	LimitPrice = 50
	BestPrice = 51
	LastPrice = 52
	LastPricePlusOneTicks = 53
	LastPricePlusTwoTicks = 54
	LastPricePlusThreeTicks = 55
	AskPrice1 = 56
	AskPrice1PlusOneTicks = 57
	AskPrice1PlusTwoTicks = 65
	AskPrice1PlusThreeTicks = 66
	BidPrice1 = 67
	BidPrice1PlusOneTicks = 68
	BidPrice1PlusTwoTicks = 69
	BidPrice1PlusThreeTicks = 70
	FiveLevelPrice = 71

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OffsetFlagType(Enum):
	"""开平标志类型"""
	Open = 48
	Close = 49
	ForceClose = 50
	CloseToday = 51
	CloseYesterday = 52
	ForceOff = 53
	LocalForceClose = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ForceCloseReasonType(Enum):
	"""强平原因类型"""
	NotForceClose = 48
	LackDeposit = 49
	ClientOverPositionLimit = 50
	MemberOverPositionLimit = 51
	NotMultiple = 52
	Violation = 53
	Other = 54
	PersonDeliv = 55

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderTypeType(Enum):
	"""报单类型类型"""
	Normal = 48
	DeriveFromQuote = 49
	DeriveFromCombination = 50
	Combination = 51
	ConditionalOrder = 52
	Swap = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TimeConditionType(Enum):
	"""有效期类型类型"""
	IOC = 49
	GFS = 50
	GFD = 51
	GTD = 52
	GTC = 53
	GFA = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VolumeConditionType(Enum):
	"""成交量类型类型"""
	AV = 49
	MV = 50
	CV = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ContingentConditionType(Enum):
	"""触发条件类型"""
	Immediately = 49
	Touch = 50
	TouchProfit = 51
	ParkedOrder = 52
	LastPriceGreaterThanStopPrice = 53
	LastPriceGreaterEqualStopPrice = 54
	LastPriceLesserThanStopPrice = 55
	LastPriceLesserEqualStopPrice = 56
	AskPriceGreaterThanStopPrice = 57
	AskPriceGreaterEqualStopPrice = 65
	AskPriceLesserThanStopPrice = 66
	AskPriceLesserEqualStopPrice = 67
	BidPriceGreaterThanStopPrice = 68
	BidPriceGreaterEqualStopPrice = 69
	BidPriceLesserThanStopPrice = 70
	BidPriceLesserEqualStopPrice = 72

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ActionFlagType(Enum):
	"""操作标志类型"""
	Delete = 48
	Modify = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradingRightType(Enum):
	"""交易权限类型"""
	Allow = 48
	CloseOnly = 49
	Forbidden = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrderSourceType(Enum):
	"""报单来源类型"""
	Participant = 48
	Administrator = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradeTypeType(Enum):
	"""成交类型类型"""
	SplitCombination = 35
	Common = 48
	OptionsExecution = 49
	OTC = 50
	EFPDerived = 51
	CombinationDerived = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PriceSourceType(Enum):
	"""成交价来源类型"""
	LastPrice = 48
	Buy = 49
	Sell = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InstrumentStatusType(Enum):
	"""合约交易状态类型"""
	BeforeTrading = 48
	NoTrading = 49
	Continous = 50
	AuctionOrdering = 51
	AuctionBalance = 52
	AuctionMatch = 53
	Closed = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InstStatusEnterReasonType(Enum):
	"""品种进入交易状态原因类型"""
	Automatic = 49
	Manual = 50
	Fuse = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BatchStatusType(Enum):
	"""处理状态类型"""
	NoUpload = 49
	Uploaded = 50
	Failed = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReturnStyleType(Enum):
	"""按品种返还方式类型"""
	All = 49
	ByProduct = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReturnPatternType(Enum):
	"""返还模式类型"""
	ByVolume = 49
	ByFeeOnHand = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReturnLevelType(Enum):
	"""返还级别类型"""
	Level1 = 49
	Level2 = 50
	Level3 = 51
	Level4 = 52
	Level5 = 53
	Level6 = 54
	Level7 = 55
	Level8 = 56
	Level9 = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReturnStandardType(Enum):
	"""返还标准类型"""
	ByPeriod = 49
	ByStandard = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MortgageTypeType(Enum):
	"""质押类型类型"""
	Out = 48
	In = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InvestorSettlementParamIDType(Enum):
	"""投资者结算参数代码类型"""
	MortgageRatio = 52
	MarginWay = 53
	BillDeposit = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExchangeSettlementParamIDType(Enum):
	"""交易所结算参数代码类型"""
	MortgageRatio = 49
	OtherFundItem = 50
	OtherFundImport = 51
	CFFEXMinPrepa = 54
	CZCESettlementType = 55
	ExchDelivFeeMode = 57
	DelivFeeMode = 48
	CZCEComMarginType = 65
	DceComMarginType = 66
	OptOutDisCountRate = 97
	OptMiniGuarantee = 98

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SystemParamIDType(Enum):
	"""系统参数代码类型"""
	InvestorIDMinLength = 49
	AccountIDMinLength = 50
	UserRightLogon = 51
	SettlementBillTrade = 52
	TradingCode = 53
	CheckFund = 54
	CommModelRight = 55
	MarginModelRight = 57
	IsStandardActive = 56
	UploadSettlementFile = 85
	DownloadCSRCFile = 68
	SettlementBillFile = 83
	CSRCOthersFile = 67
	InvestorPhoto = 80
	CSRCData = 82
	InvestorPwdModel = 73
	CFFEXInvestorSettleFile = 70
	InvestorIDType = 97
	FreezeMaxReMain = 114
	IsSync = 65
	RelieveOpenLimit = 79
	IsStandardFreeze = 88
	CZCENormalProductHedge = 66

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradeParamIDType(Enum):
	"""交易系统参数代码类型"""
	EncryptionStandard = 69
	RiskMode = 82
	RiskModeGlobal = 71
	modeEncode = 80
	tickMode = 84
	SingleUserSessionMaxNum = 83
	LoginFailMaxNum = 76
	IsAuthForce = 65
	IsPosiFreeze = 70
	IsPosiLimit = 77
	ForQuoteTimeInterval = 81
	IsFuturePosiLimit = 66
	IsFutureOrderFreq = 67
	IsExecOrderProfit = 72

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileIDType(Enum):
	"""文件标识类型"""
	SettlementFund = 70
	Trade = 84
	InvestorPosition = 80
	SubEntryFund = 79
	CZCECombinationPos = 67
	CSRCData = 82
	CZCEClose = 76
	CZCENoClose = 78
	PositionDtl = 68
	OptionStrike = 83
	SettlementPriceComparison = 77
	NonTradePosChange = 66

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileTypeType(Enum):
	"""文件上传类型类型"""
	Settlement = 48
	Check = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileFormatType(Enum):
	"""文件格式类型"""
	Txt = 48
	Zip = 49
	DBF = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileUploadStatusType(Enum):
	"""文件状态类型"""
	SucceedUpload = 49
	FailedUpload = 50
	SucceedLoad = 51
	PartSucceedLoad = 52
	FailedLoad = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TransferDirectionType(Enum):
	"""移仓方向类型"""
	Out = 48
	In = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SpecialCreateRuleType(Enum):
	"""特殊的创建规则类型"""
	NoSpecialRule = 48
	NoSpringFestival = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BasisPriceTypeType(Enum):
	"""挂牌基准价类型类型"""
	LastSettlement = 49
	LaseClose = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ProductLifePhaseType(Enum):
	"""产品生命周期状态类型"""
	Active = 49
	NonActive = 50
	Canceled = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DeliveryModeType(Enum):
	"""交割方式类型"""
	CashDeliv = 49
	CommodityDeliv = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundIOTypeType(Enum):
	"""出入金类型类型"""
	FundIO = 49
	Transfer = 50
	SwapCurrency = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundTypeType(Enum):
	"""资金类型类型"""
	Deposite = 49
	ItemFund = 50
	Company = 51
	InnerTransfer = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundDirectionType(Enum):
	"""出入金方向类型"""
	In = 49
	Out = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundStatusType(Enum):
	"""资金状态类型"""
	Record = 49
	Check = 50
	Charge = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PublishStatusType(Enum):
	"""发布状态类型"""
	Zero = 49
	Publishing = 50
	Published = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SystemStatusType(Enum):
	"""系统状态类型"""
	NonActive = 49
	Startup = 50
	Initialize = 51
	Initialized = 52
	Close = 53
	Closed = 54
	Settlement = 55

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettlementStatusType(Enum):
	"""结算状态类型"""
	Initialize = 48
	Settlementing = 49
	Settlemented = 50
	Finished = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InvestorTypeType(Enum):
	"""投资者类型类型"""
	Person = 48
	Company = 49
	Fund = 50
	SpecialOrgan = 51
	Asset = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BrokerTypeType(Enum):
	"""经纪公司类型类型"""
	Trade = 48
	TradeSettle = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RiskLevelType(Enum):
	"""风险等级类型"""
	Low = 49
	Normal = 50
	Focus = 51
	Risk = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FeeAcceptStyleType(Enum):
	"""手续费收取方式类型"""
	ByTrade = 49
	ByDeliv = 50
	Zero = 51
	FixFee = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PasswordTypeType(Enum):
	"""密码类型类型"""
	Trade = 49
	Account = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AlgorithmType(Enum):
	"""盈亏算法类型"""
	All = 49
	OnlyLost = 50
	OnlyGain = 51
	Zero = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class IncludeCloseProfitType(Enum):
	"""是否包含平仓盈利类型"""
	Include = 48
	NotInclude = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AllWithoutTradeType(Enum):
	"""是否受可提比例限制类型"""
	Enable = 48
	Disable = 50
	NoHoldEnable = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FuturePwdFlagType(Enum):
	"""资金密码核对标志类型"""
	UnCheck = 48
	Check = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TransferTypeType(Enum):
	"""银期转账类型类型"""
	BankToFuture = 48
	FutureToBank = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TransferValidFlagType(Enum):
	"""转账有效标志类型"""
	Invalid = 48
	Valid = 49
	Reverse = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReasonType(Enum):
	"""事由类型"""
	CD = 48
	ZT = 49
	QT = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SexType(Enum):
	"""性别类型"""
	Zero = 48
	Man = 49
	Woman = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UserTypeType(Enum):
	"""用户类型类型"""
	Investor = 48
	Operator = 49
	SuperUser = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RateTypeType(Enum):
	"""费率类型类型"""
	MarginRate = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class NoteTypeType(Enum):
	"""通知类型类型"""
	TradeSettleBill = 49
	TradeSettleMonth = 50
	CallMarginNotes = 51
	ForceCloseNotes = 52
	TradeNotes = 53
	DelivNotes = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettlementStyleType(Enum):
	"""结算单方式类型"""
	Day = 49
	Volume = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettlementBillTypeType(Enum):
	"""结算单类型类型"""
	Day = 48
	Month = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UserRightTypeType(Enum):
	"""客户权限类型类型"""
	Logon = 49
	Transfer = 50
	EMail = 51
	Fax = 52
	ConditionOrder = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MarginPriceTypeType(Enum):
	"""保证金价格类型类型"""
	PreSettlementPrice = 49
	SettlementPrice = 50
	AveragePrice = 51
	OpenPrice = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BillGenStatusType(Enum):
	"""结算单生成状态类型"""
	Zero = 48
	NoGenerated = 49
	Generated = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AlgoTypeType(Enum):
	"""算法类型类型"""
	HandlePositionAlgo = 49
	FindMarginRateAlgo = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HandlePositionAlgoIDType(Enum):
	"""持仓处理算法编号类型"""
	Base = 49
	DCE = 50
	CZCE = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FindMarginRateAlgoIDType(Enum):
	"""寻找保证金率算法编号类型"""
	Base = 49
	DCE = 50
	CZCE = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HandleTradingAccountAlgoIDType(Enum):
	"""资金处理算法编号类型"""
	Base = 49
	DCE = 50
	CZCE = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PersonTypeType(Enum):
	"""联系人类型类型"""
	Order = 49
	Open = 50
	Fund = 51
	Settlement = 52
	Company = 53
	Corporation = 54
	LinkMan = 55
	Ledger = 56
	Trustee = 57
	TrusteeCorporation = 65
	TrusteeOpen = 66
	TrusteeContact = 67
	ForeignerRefer = 68
	CorporationRefer = 69

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class QueryInvestorRangeType(Enum):
	"""查询范围类型"""
	All = 49
	Group = 50
	Single = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InvestorRiskStatusType(Enum):
	"""投资者风险状态类型"""
	Normal = 49
	Warn = 50
	Call = 51
	Force = 52
	Exception = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UserEventTypeType(Enum):
	"""用户事件类型类型"""
	Login = 49
	Logout = 50
	Trading = 51
	TradingError = 52
	UpdatePassword = 53
	Authenticate = 54
	Other = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CloseStyleType(Enum):
	"""平仓方式类型"""
	Close = 48
	CloseToday = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StatModeType(Enum):
	"""统计方式类型"""
	Non = 48
	Instrument = 49
	Product = 50
	Investor = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ParkedOrderStatusType(Enum):
	"""预埋单状态类型"""
	NotSend = 49
	Send = 50
	Deleted = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirDealStatusType(Enum):
	"""处理状态类型"""
	Dealing = 49
	DeaclSucceed = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrgSystemIDType(Enum):
	"""原有系统代码类型"""
	Standard = 48
	ESunny = 49
	KingStarV6 = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirTradeStatusType(Enum):
	"""交易状态类型"""
	NaturalDeal = 48
	SucceedEnd = 49
	FailedEND = 50
	Exception = 51
	ManualDeal = 52
	MesException = 53
	SysException = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirBankAccTypeType(Enum):
	"""银行帐户类型类型"""
	BankBook = 49
	BankCard = 50
	CreditCard = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirementStatusType(Enum):
	"""银行帐户类型类型"""
	Natural = 48
	Canceled = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirementAvailAbilityType(Enum):
	"""有效标志类型"""
	NoAvailAbility = 48
	AvailAbility = 49
	Repeal = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class VirementTradeCodeType(Enum):
	"""交易代码类型"""
	BankBankToFuture = 102001
	BankFutureToBank = 102002
	FutureBankToFuture = 202001
	FutureFutureToBank = 202002

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AMLGenStatusType(Enum):
	"""Aml生成方式类型"""
	Program = 48
	HandWork = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CFMMCKeyKindType(Enum):
	"""动态密钥类别(保证金监管)类型"""
	REQUEST = 82
	AUTO = 65
	MANUAL = 77

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CertificationTypeType(Enum):
	"""证件类型类型"""
	IDCard = 48
	Passport = 49
	OfficerIDCard = 50
	SoldierIDCard = 51
	HomeComingCard = 52
	HouseholdRegister = 53
	LicenseNo = 54
	InstitutionCodeCard = 55
	TempLicenseNo = 56
	NoEnterpriseLicenseNo = 57
	OtherCard = 120
	SuperDepAgree = 97

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileBusinessCodeType(Enum):
	"""文件业务功能类型"""
	Others = 48
	TransferDetails = 49
	CustAccStatus = 50
	AccountTradeDetails = 51
	FutureAccountChangeInfoDetails = 52
	CustMoneyDetail = 53
	CustCancelAccountInfo = 54
	CustMoneyResult = 55
	OthersExceptionResult = 56
	CustInterestNetMoneyDetails = 57
	CustMoneySendAndReceiveDetails = 97
	CorporationMoneyTotal = 98
	MainbodyMoneyTotal = 99
	MainPartMonitorData = 100
	PreparationMoney = 101
	BankMoneyMonitorData = 102

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CashExchangeCodeType(Enum):
	"""汇钞标志类型"""
	Exchange = 49
	Cash = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class YesNoIndicatorType(Enum):
	"""是或否标识类型"""
	Yes = 48
	No = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BanlanceTypeType(Enum):
	"""余额类型类型"""
	CurrentMoney = 48
	UsableMoney = 49
	FetchableMoney = 50
	FreezeMoney = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class GenderType(Enum):
	"""性别类型"""
	Unknown = 48
	Male = 49
	Female = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FeePayFlagType(Enum):
	"""费用支付标志类型"""
	BEN = 48
	OUR = 49
	SHA = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PassWordKeyTypeType(Enum):
	"""密钥类型类型"""
	ExchangeKey = 48
	PassWordKey = 49
	MACKey = 50
	MessageKey = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBTPassWordTypeType(Enum):
	"""密码类型类型"""
	Query = 48
	Fetch = 49
	Transfer = 50
	Trade = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBTEncryModeType(Enum):
	"""加密方式类型"""
	NoEncry = 48
	DES = 49
	DES3 = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BankRepealFlagType(Enum):
	"""银行冲正标志类型"""
	BankNotNeedRepeal = 48
	BankWaitingRepeal = 49
	BankBeenRepealed = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BrokerRepealFlagType(Enum):
	"""期商冲正标志类型"""
	BrokerNotNeedRepeal = 48
	BrokerWaitingRepeal = 49
	BrokerBeenRepealed = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InstitutionTypeType(Enum):
	"""机构类别类型"""
	Bank = 48
	Future = 49
	Store = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class LastFragmentType(Enum):
	"""最后分片标志类型"""
	Yes = 48
	No = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BankAccStatusType(Enum):
	"""银行账户状态类型"""
	Normal = 48
	Freeze = 49
	ReportLoss = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MoneyAccountStatusType(Enum):
	"""资金账户状态类型"""
	Normal = 48
	Cancel = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ManageStatusType(Enum):
	"""存管状态类型"""
	Point = 48
	PrePoint = 49
	CancelPoint = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SystemTypeType(Enum):
	"""应用系统类型类型"""
	FutureBankTransfer = 48
	StockBankTransfer = 49
	TheThirdPartStore = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TxnEndFlagType(Enum):
	"""银期转帐划转结果标志类型"""
	NormalProcessing = 48
	Success = 49
	Failed = 50
	Abnormal = 51
	ManualProcessedForException = 52
	CommuFailedNeedManualProcess = 53
	SysErrorNeedManualProcess = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ProcessStatusType(Enum):
	"""银期转帐服务处理状态类型"""
	NotProcess = 48
	StartProcess = 49
	Finished = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CustTypeType(Enum):
	"""客户类型类型"""
	Person = 48
	Institution = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBTTransferDirectionType(Enum):
	"""银期转帐方向类型"""
	FromBankToFuture = 49
	FromFutureToBank = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OpenOrDestroyType(Enum):
	"""开销户类别类型"""
	Open = 49
	Destroy = 48

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AvailabilityFlagType(Enum):
	"""有效标志类型"""
	Invalid = 48
	Valid = 49
	Repeal = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrganTypeType(Enum):
	"""机构类型类型"""
	Bank = 49
	Future = 50
	PlateForm = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrganLevelType(Enum):
	"""机构级别类型"""
	HeadQuarters = 49
	Branch = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ProtocalIDType(Enum):
	"""协议类型类型"""
	FutureProtocal = 48
	ICBCProtocal = 49
	ABCProtocal = 50
	CBCProtocal = 51
	CCBProtocal = 52
	BOCOMProtocal = 53
	FBTPlateFormProtocal = 88

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ConnectModeType(Enum):
	"""套接字连接方式类型"""
	ShortConnect = 48
	LongConnect = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SyncModeType(Enum):
	"""套接字通信方式类型"""
	ASync = 48
	Sync = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BankAccTypeType(Enum):
	"""银行帐号类型类型"""
	BankBook = 49
	SavingCard = 50
	CreditCard = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FutureAccTypeType(Enum):
	"""期货公司帐号类型类型"""
	BankBook = 49
	SavingCard = 50
	CreditCard = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OrganStatusType(Enum):
	"""接入机构状态类型"""
	Ready = 48
	CheckIn = 49
	CheckOut = 50
	CheckFileArrived = 51
	CheckDetail = 52
	DayEndClean = 53
	Invalid = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CCBFeeModeType(Enum):
	"""建行收费模式类型"""
	ByAmount = 49
	ByMonth = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CommApiTypeType(Enum):
	"""通讯API类型类型"""
	Client = 49
	Server = 50
	UserApi = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class LinkStatusType(Enum):
	"""连接状态类型"""
	Connected = 49
	Disconnected = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PwdFlagType(Enum):
	"""密码核对标志类型"""
	NoCheck = 48
	BlankCheck = 49
	EncryptCheck = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SecuAccTypeType(Enum):
	"""期货帐号类型类型"""
	AccountID = 49
	CardID = 50
	SHStockholderID = 51
	SZStockholderID = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TransferStatusType(Enum):
	"""转账交易状态类型"""
	Normal = 48
	Repealed = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SponsorTypeType(Enum):
	"""发起方类型"""
	Broker = 48
	Bank = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReqRspTypeType(Enum):
	"""请求响应类别类型"""
	Request = 48
	Response = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBTUserEventTypeType(Enum):
	"""银期转帐用户事件类型类型"""
	SignIn = 48
	FromBankToFuture = 49
	FromFutureToBank = 50
	OpenAccount = 51
	CancelAccount = 52
	ChangeAccount = 53
	RepealFromBankToFuture = 54
	RepealFromFutureToBank = 55
	QueryBankAccount = 56
	QueryFutureAccount = 57
	SignOut = 65
	SyncKey = 66
	ReserveOpenAccount = 67
	CancelReserveOpenAccount = 68
	ReserveOpenAccountConfirm = 69
	Other = 90

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DBOperationType(Enum):
	"""记录操作类型类型"""
	Insert = 48
	Update = 49
	Delete = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SyncFlagType(Enum):
	"""同步标记类型"""
	Yes = 48
	No = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SyncTypeType(Enum):
	"""同步类型类型"""
	OneOffSync = 48
	TimerSync = 49
	TimerFullSync = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExDirectionType(Enum):
	"""换汇方向类型"""
	Settlement = 48
	Sale = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEResultFlagType(Enum):
	"""换汇成功标志类型"""
	Success = 48
	InsufficientBalance = 49
	UnknownTrading = 56
	Fail = 120

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEExchStatusType(Enum):
	"""换汇交易状态类型"""
	Normal = 48
	ReExchange = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEFileFlagType(Enum):
	"""换汇文件标志类型"""
	DataPackage = 48
	File = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEAlreadyTradeType(Enum):
	"""换汇已交易标志类型"""
	NotTrade = 48
	Trade = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEUserEventTypeType(Enum):
	"""银期换汇用户事件类型类型"""
	SignIn = 48
	Exchange = 49
	ReExchange = 50
	QueryBankAccount = 51
	QueryExchDetial = 52
	QueryExchSummary = 53
	QueryExchRate = 54
	CheckBankAccount = 55
	SignOut = 56
	Other = 90

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBEReqFlagType(Enum):
	"""换汇发送标志类型"""
	UnProcessed = 48
	WaitSend = 49
	SendSuccess = 50
	SendFailed = 51
	WaitReSend = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class NotifyClassType(Enum):
	"""风险通知类型类型"""
	NOERROR = 48
	Warn = 49
	Call = 50
	Force = 51
	CHUANCANG = 52
	Exception = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ForceCloseTypeType(Enum):
	"""强平单类型类型"""
	Manual = 48
	Single = 49
	Group = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RiskNotifyMethodType(Enum):
	"""风险通知途径类型"""
	System = 48
	SMS = 49
	EMail = 50
	Manual = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RiskNotifyStatusType(Enum):
	"""风险通知状态类型"""
	NotGen = 48
	Generated = 49
	SendError = 50
	SendOk = 51
	Received = 52
	Confirmed = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RiskUserEventType(Enum):
	"""风控用户操作事件类型"""
	ExportData = 48

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ConditionalOrderSortTypeType(Enum):
	"""条件单索引条件类型"""
	LastPriceAsc = 48
	LastPriceDesc = 49
	AskPriceAsc = 50
	AskPriceDesc = 51
	BidPriceAsc = 52
	BidPriceDesc = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SendTypeType(Enum):
	"""报送状态类型"""
	NoSend = 48
	Sended = 49
	Generated = 50
	SendFail = 51
	Success = 52
	Fail = 53
	Cancel = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ClientIDStatusType(Enum):
	"""交易编码状态类型"""
	NoApply = 49
	Submited = 50
	Sended = 51
	Success = 52
	Refuse = 53
	Cancel = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class QuestionTypeType(Enum):
	"""特有信息类型类型"""
	Radio = 49
	Option = 50
	Blank = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BusinessTypeType(Enum):
	"""业务类型类型"""
	Request = 49
	Response = 50
	Notice = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CfmmcReturnCodeType(Enum):
	"""监控中心返回码类型"""
	Success = 48
	Working = 49
	InfoFail = 50
	IDCardFail = 51
	OtherFail = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ClientTypeType(Enum):
	"""客户类型类型"""
	All = 48
	Person = 49
	Company = 50
	Other = 51
	SpecialOrgan = 52
	Asset = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExchangeIDTypeType(Enum):
	"""交易所编号类型"""
	SHFE = 83
	CZCE = 90
	DCE = 68
	CFFEX = 74
	INE = 78

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExClientIDTypeType(Enum):
	"""交易编码类型类型"""
	Hedge = 49
	Arbitrage = 50
	Speculation = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UpdateFlagType(Enum):
	"""更新状态类型"""
	NoUpdate = 48
	Success = 49
	Fail = 50
	TCSuccess = 51
	TCFail = 52
	Cancel = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ApplyOperateIDType(Enum):
	"""申请动作类型"""
	OpenInvestor = 49
	ModifyIDCard = 50
	ModifyNoIDCard = 51
	ApplyTradingCode = 52
	CancelTradingCode = 53
	CancelInvestor = 54
	FreezeAccount = 56
	ActiveFreezeAccount = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ApplyStatusIDType(Enum):
	"""申请状态类型"""
	NoComplete = 49
	Submited = 50
	Checked = 51
	Refused = 52
	Deleted = 53

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SendMethodType(Enum):
	"""发送方式类型"""
	ByAPI = 49
	ByFile = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class EventModeType(Enum):
	"""操作方法类型"""
	ADD = 49
	UPDATE = 50
	DELETE = 51
	CHECK = 52
	COPY = 53
	CANCEL = 54
	Reverse = 55

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UOAAutoSendType(Enum):
	"""统一开户申请自动发送类型"""
	ASR = 49
	ASNR = 50
	NSAR = 51
	NSR = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FlowIDType(Enum):
	"""流程ID类型"""
	InvestorGroupFlow = 49
	InvestorRate = 50
	InvestorCommRateModel = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CheckLevelType(Enum):
	"""复核级别类型"""
	Zero = 48
	One = 49
	Two = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CheckStatusType(Enum):
	"""复核级别类型"""
	Init = 48
	Checking = 49
	Checked = 50
	Refuse = 51
	Cancel = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UsedStatusType(Enum):
	"""生效状态类型"""
	Unused = 48
	Used = 49
	Fail = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BankAcountOriginType(Enum):
	"""账户来源类型"""
	ByAccProperty = 48
	ByFBTransfer = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MonthBillTradeSumType(Enum):
	"""结算单月报成交汇总方式类型"""
	ByInstrument = 48
	ByDayInsPrc = 49
	ByDayIns = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FBTTradeCodeEnumType(Enum):
	"""银期交易代码枚举类型"""
	BankLaunchBankToBroker = 102001
	BrokerLaunchBankToBroker = 202001
	BankLaunchBrokerToBank = 102002
	BrokerLaunchBrokerToBank = 202002

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OTPTypeType(Enum):
	"""动态令牌类型类型"""
	NONE = 48
	TOTP = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OTPStatusType(Enum):
	"""动态令牌状态类型"""
	Unused = 48
	Used = 49
	Disuse = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BrokerUserTypeType(Enum):
	"""经济公司用户类型类型"""
	Investor = 49
	BrokerUser = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FutureTypeType(Enum):
	"""期货类型类型"""
	Commodity = 49
	Financial = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundEventTypeType(Enum):
	"""资金管理操作类型类型"""
	Restriction = 48
	TodayRestriction = 49
	Transfer = 50
	Credit = 51
	InvestorWithdrawAlm = 52
	BankRestriction = 53
	Accountregister = 54
	ExchangeFundIO = 55
	InvestorFundIO = 56

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AccountSourceTypeType(Enum):
	"""资金账户来源类型"""
	FBTransfer = 48
	ManualEntry = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CodeSourceTypeType(Enum):
	"""交易编码来源类型"""
	UnifyAccount = 48
	ManualEntry = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UserRangeType(Enum):
	"""操作员范围类型"""
	All = 48
	Single = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ByGroupType(Enum):
	"""交易统计表按客户统计方式类型"""
	Investor = 50
	Group = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradeSumStatModeType(Enum):
	"""交易统计表按范围统计方式类型"""
	Instrument = 49
	Product = 50
	Exchange = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExprSetModeType(Enum):
	"""日期表达式设置类型类型"""
	Relative = 49
	Typical = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RateInvestorRangeType(Enum):
	"""投资者范围类型"""
	All = 49
	Model = 50
	Single = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SyncDataStatusType(Enum):
	"""主次用系统数据同步状态类型"""
	Initialize = 48
	Settlementing = 49
	Settlemented = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TradeSourceType(Enum):
	"""成交来源类型"""
	NORMAL = 48
	QUERY = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FlexStatModeType(Enum):
	"""产品合约统计方式类型"""
	Product = 49
	Exchange = 50
	All = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ByInvestorRangeType(Enum):
	"""投资者范围统计方式类型"""
	Property = 49
	All = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PropertyInvestorRangeType(Enum):
	"""投资者范围类型"""
	All = 49
	Property = 50
	Single = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileStatusType(Enum):
	"""文件状态类型"""
	NoCreate = 48
	Created = 49
	Failed = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FileGenStyleType(Enum):
	"""文件生成方式类型"""
	FileTransmit = 48
	FileGen = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SysOperModeType(Enum):
	"""系统日志操作方法类型"""
	Add = 49
	Update = 50
	Delete = 51
	Copy = 52
	AcTive = 53
	CanCel = 54
	ReSet = 55

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SysOperTypeType(Enum):
	"""系统日志操作类型类型"""
	UpdatePassword = 48
	UserDepartment = 49
	RoleManager = 50
	RoleFunction = 51
	BaseParam = 52
	SetUserID = 53
	SetUserRole = 54
	UserIpRestriction = 55
	DepartmentManager = 56
	DepartmentCopy = 57
	Tradingcode = 65
	InvestorStatus = 66
	InvestorAuthority = 67
	PropertySet = 68
	ReSetInvestorPasswd = 69
	InvestorPersonalityInfo = 70

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CSRCDataQueyTypeType(Enum):
	"""上报数据查询类型类型"""
	Current = 48
	History = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FreezeStatusType(Enum):
	"""休眠状态类型"""
	Normal = 49
	Freeze = 48

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StandardStatusType(Enum):
	"""规范状态类型"""
	Standard = 48
	NonStandard = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class RightParamTypeType(Enum):
	"""配置类型类型"""
	Freeze = 49
	FreezeActive = 50
	OpenLimit = 51
	RelieveOpenLimit = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DataStatusType(Enum):
	"""反洗钱审核表数据状态类型"""
	Normal = 48
	Deleted = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AMLCheckStatusType(Enum):
	"""审核状态类型"""
	Init = 48
	Checking = 49
	Checked = 50
	RefuseReport = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AmlDateTypeType(Enum):
	"""日期类型类型"""
	DrawDay = 48
	TouchDay = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AmlCheckLevelType(Enum):
	"""审核级别类型"""
	CheckLevel0 = 48
	CheckLevel1 = 49
	CheckLevel2 = 50
	CheckLevel3 = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExportFileTypeType(Enum):
	"""导出文件类型类型"""
	CSV = 48
	EXCEL = 49
	DBF = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettleManagerTypeType(Enum):
	"""结算配置类型类型"""
	Before = 49
	Settlement = 50
	After = 51
	Settlemented = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettleManagerLevelType(Enum):
	"""结算配置等级类型"""
	Must = 49
	Alarm = 50
	Prompt = 51
	Ignore = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettleManagerGroupType(Enum):
	"""模块分组类型"""
	Exhcange = 49
	ASP = 50
	CSRC = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class LimitUseTypeType(Enum):
	"""保值额度使用类型类型"""
	Repeatable = 49
	Unrepeatable = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DataResourceType(Enum):
	"""数据来源类型"""
	Settle = 49
	Exchange = 50
	CSRC = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MarginTypeType(Enum):
	"""保证金类型类型"""
	ExchMarginRate = 48
	InstrMarginRate = 49
	InstrMarginRateTrade = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ActiveTypeType(Enum):
	"""生效类型类型"""
	Intraday = 49
	Long = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MarginRateTypeType(Enum):
	"""冲突保证金率类型类型"""
	Exchange = 49
	Investor = 50
	InvestorTrade = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BackUpStatusType(Enum):
	"""备份数据状态类型"""
	UnBak = 48
	BakUp = 49
	BakUped = 50
	BakFail = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class InitSettlementType(Enum):
	"""结算初始化状态类型"""
	UnInitialize = 48
	Initialize = 49
	Initialized = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReportStatusType(Enum):
	"""报表数据生成状态类型"""
	NoCreate = 48
	Create = 49
	Created = 50
	CreateFail = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SaveStatusType(Enum):
	"""数据归档状态类型"""
	UnSaveData = 48
	SaveDatad = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SettArchiveStatusType(Enum):
	"""结算确认数据归档状态类型"""
	UnArchived = 48
	Archiving = 49
	Archived = 50
	ArchiveFail = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CTPTypeType(Enum):
	"""CTP交易系统类型类型"""
	Unkown = 48
	MainCenter = 49
	BackUp = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CloseDealTypeType(Enum):
	"""平仓处理类型类型"""
	Normal = 48
	SpecFirst = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MortgageFundUseRangeType(Enum):
	"""货币质押资金可用范围类型"""
	Zero = 48
	Margin = 49
	All = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SpecProductTypeType(Enum):
	"""特殊产品类型类型"""
	CzceHedge = 49
	IneForeignCurrency = 50
	DceOpenClose = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundMortgageTypeType(Enum):
	"""货币质押类型类型"""
	Mortgage = 49
	Redemption = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AccountSettlementParamIDType(Enum):
	"""投资者账户结算参数代码类型"""
	BaseMargin = 49
	LowestInterest = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundMortDirectionType(Enum):
	"""货币质押方向类型"""
	In = 49
	Out = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BusinessClassType(Enum):
	"""换汇类别类型"""
	Profit = 48
	Loss = 49
	Other = 90

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SwapSourceTypeType(Enum):
	"""换汇数据来源类型"""
	Manual = 48
	Automatic = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CurrExDirectionType(Enum):
	"""换汇类型类型"""
	Settlement = 48
	Sale = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CurrencySwapStatusType(Enum):
	"""申请状态类型"""
	Entry = 49
	Approve = 50
	Refuse = 51
	Revoke = 52
	Send = 53
	Success = 54
	Failure = 55

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReqFlagType(Enum):
	"""换汇发送标志类型"""
	NoSend = 48
	SendSuccess = 49
	SendFailed = 50
	WaitReSend = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ResFlagType(Enum):
	"""换汇返回成功标志类型"""
	Success = 48
	InsuffiCient = 49
	UnKnown = 56

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExStatusType(Enum):
	"""修改状态类型"""
	Before = 48
	After = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ClientRegionType(Enum):
	"""开户客户地域类型"""
	Domestic = 49
	GMT = 50
	Foreign = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HasBoardType(Enum):
	"""是否有董事会类型"""
	No = 48
	Yes = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StartModeType(Enum):
	"""启动模式类型"""
	Normal = 49
	Emerge = 50
	Restore = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class TemplateTypeType(Enum):
	"""模型类型类型"""
	Full = 49
	Increment = 50
	BackUp = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class LoginModeType(Enum):
	"""登录模式类型"""
	Trade = 48
	Transfer = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class PromptTypeType(Enum):
	"""日历提示类型类型"""
	Instrument = 49
	Margin = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HasTrusteeType(Enum):
	"""是否有托管人类型"""
	Yes = 49
	No = 48

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AmTypeType(Enum):
	"""机构类型类型"""
	Bank = 49
	Securities = 50
	Fund = 51
	Insurance = 52
	Trust = 53
	Other = 57

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CSRCFundIOTypeType(Enum):
	"""出入金类型类型"""
	FundIO = 48
	SwapCurrency = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CusAccountTypeType(Enum):
	"""结算账户类型类型"""
	Futures = 49
	AssetmgrFuture = 50
	AssetmgrTrustee = 51
	AssetmgrTransfer = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class LanguageTypeType(Enum):
	"""通知语言类型类型"""
	Chinese = 49
	English = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AssetmgrClientTypeType(Enum):
	"""资产管理客户类型类型"""
	Person = 49
	Organ = 50
	SpecialOrgan = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class AssetmgrTypeType(Enum):
	"""投资类型类型"""
	Futures = 51
	SpecialOrgan = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CheckInstrTypeType(Enum):
	"""合约比较类型类型"""
	HasExch = 48
	HasATP = 49
	HasDiff = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DeliveryTypeType(Enum):
	"""交割类型类型"""
	HandDeliv = 49
	PersonDeliv = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class MaxMarginSideAlgorithmType(Enum):
	"""大额单边保证金算法类型"""
	NO = 48
	YES = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DAClientTypeType(Enum):
	"""资产管理客户类型类型"""
	Person = 48
	Company = 49
	Other = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class UOAAssetmgrTypeType(Enum):
	"""投资类型类型"""
	Futures = 49
	SpecialOrgan = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DirectionEnType(Enum):
	"""买卖方向类型"""
	Buy = 48
	Sell = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OffsetFlagEnType(Enum):
	"""开平标志类型"""
	Open = 48
	Close = 49
	ForceClose = 50
	CloseToday = 51
	CloseYesterday = 52
	ForceOff = 53
	LocalForceClose = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class HedgeFlagEnType(Enum):
	"""投机套保标志类型"""
	Speculation = 49
	Arbitrage = 50
	Hedge = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundIOTypeEnType(Enum):
	"""出入金类型类型"""
	FundIO = 49
	Transfer = 50
	SwapCurrency = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundTypeEnType(Enum):
	"""资金类型类型"""
	Deposite = 49
	ItemFund = 50
	Company = 51
	InnerTransfer = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundDirectionEnType(Enum):
	"""出入金方向类型"""
	In = 49
	Out = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class FundMortDirectionEnType(Enum):
	"""货币质押方向类型"""
	In = 49
	Out = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OptionsTypeType(Enum):
	"""期权类型类型"""
	CallOptions = 49
	PutOptions = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StrikeModeType(Enum):
	"""执行方式类型"""
	Continental = 48
	American = 49
	Bermuda = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StrikeTypeType(Enum):
	"""执行类型类型"""
	Hedge = 48
	Match = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ApplyTypeType(Enum):
	"""中金所期权放弃执行申请类型类型"""
	NotStrikeNum = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class GiveUpDataSourceType(Enum):
	"""放弃执行申请数据来源类型"""
	Gen = 48
	Hand = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExecResultType(Enum):
	"""执行结果类型"""
	NoExec = 110
	Canceled = 99
	OK = 48
	NoPosition = 49
	NoDeposit = 50
	NoParticipant = 51
	NoClient = 52
	NoInstrument = 54
	NoRight = 55
	InvalidVolume = 56
	NoEnoughHistoryTrade = 57
	Unknown = 97

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CombinationTypeType(Enum):
	"""组合类型类型"""
	Future = 48
	BUL = 49
	BER = 50
	STD = 51
	STG = 52
	PRT = 53
	CLD = 54

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class OptionRoyaltyPriceTypeType(Enum):
	"""期权权利金价格类型类型"""
	PreSettlementPrice = 49
	OpenPrice = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class BalanceAlgorithmType(Enum):
	"""权益算法类型"""
	Default = 49
	IncludeOptValLost = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ActionTypeType(Enum):
	"""执行类型类型"""
	Exec = 49
	Abandon = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ForQuoteStatusType(Enum):
	"""询价状态类型"""
	Submitted = 97
	Accepted = 98
	Rejected = 99

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ValueMethodType(Enum):
	"""取值方式类型"""
	Absolute = 48
	Ratio = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExecOrderPositionFlagType(Enum):
	"""期权行权后是否保留期货头寸的标记类型"""
	Reserve = 48
	UnReserve = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ExecOrderCloseFlagType(Enum):
	"""期权行权后生成的头寸是否自动平仓类型"""
	AutoClose = 48
	NotToClose = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ProductTypeType(Enum):
	"""产品类型类型"""
	Futures = 49
	Options = 50

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CZCEUploadFileNameType(Enum):
	"""郑商所结算文件名类型"""
	CUFN_O = 79
	CUFN_T = 84
	CUFN_P = 80
	CUFN_N = 78
	CUFN_L = 76
	CUFN_F = 70
	CUFN_C = 67
	CUFN_M = 77

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class DCEUploadFileNameType(Enum):
	"""大商所结算文件名类型"""
	DUFN_O = 79
	DUFN_T = 84
	DUFN_P = 80
	DUFN_F = 70
	DUFN_C = 67
	DUFN_D = 68
	DUFN_M = 77
	DUFN_S = 83

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class SHFEUploadFileNameType(Enum):
	"""上期所结算文件名类型"""
	SUFN_O = 79
	SUFN_T = 84
	SUFN_P = 80
	SUFN_F = 70

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CFFEXUploadFileNameType(Enum):
	"""中金所结算文件名类型"""
	SUFN_T = 84
	SUFN_P = 80
	SUFN_F = 70
	SUFN_S = 83

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class CombDirectionType(Enum):
	"""组合指令方向类型"""
	Comb = 48
	UnComb = 49

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class StrikeOffsetTypeType(Enum):
	"""行权偏移类型类型"""
	RealValue = 49
	ProfitValue = 50
	RealRatio = 51
	ProfitRatio = 52

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class ReserveOpenAccStasType(Enum):
	"""预约开户状态类型"""
	Processing = 48
	Cancelled = 49
	Opened = 50
	Invalid = 51

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

class NewsUrgencyType(Enum):
	"""紧急程度类型"""

	#----------------------------------------------------------------------
	def __int__(self):
		"""return int value"""
		return self.value

	#----------------------------------------------------------------------
	def __char__(self):
		"""return char value"""
		return chr(self.value)

