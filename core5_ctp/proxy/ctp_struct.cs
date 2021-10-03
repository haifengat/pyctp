using System.Runtime.InteropServices;
using PureCode.CtpCSharp;

/// <summary>
/// 信息分发
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDisseminationField
{

	/// <summary>
	/// 序列系列号
	/// </summary>
	public short SequenceSeries;

	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;
}

/// <summary>
/// 用户登录请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqUserLoginField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OneTimePassword;

	/// <summary>
	/// 动态密码
	/// </summary>
	public string OneTimePassword
	{
		get { return StringExtend.GetString(_OneTimePassword); }
		set { _OneTimePassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ClientIPAddress;

	/// <summary>
	/// 终端IP地址
	/// </summary>
	public string ClientIPAddress
	{
		get { return StringExtend.GetString(_ClientIPAddress); }
		set { _ClientIPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 终端IP端口
	/// </summary>
	public int ClientIPPort;
}

/// <summary>
/// 用户登录应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspUserLoginField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginTime;

	/// <summary>
	/// 登录成功时间
	/// </summary>
	public string LoginTime
	{
		get { return StringExtend.GetString(_LoginTime); }
		set { _LoginTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _SystemName;

	/// <summary>
	/// 交易系统名称
	/// </summary>
	public string SystemName
	{
		get { return StringExtend.GetString(_SystemName); }
		set { _SystemName = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MaxOrderRef;

	/// <summary>
	/// 最大报单引用
	/// </summary>
	public string MaxOrderRef
	{
		get { return StringExtend.GetString(_MaxOrderRef); }
		set { _MaxOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SHFETime;

	/// <summary>
	/// 上期所时间
	/// </summary>
	public string SHFETime
	{
		get { return StringExtend.GetString(_SHFETime); }
		set { _SHFETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _DCETime;

	/// <summary>
	/// 大商所时间
	/// </summary>
	public string DCETime
	{
		get { return StringExtend.GetString(_DCETime); }
		set { _DCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CZCETime;

	/// <summary>
	/// 郑商所时间
	/// </summary>
	public string CZCETime
	{
		get { return StringExtend.GetString(_CZCETime); }
		set { _CZCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _FFEXTime;

	/// <summary>
	/// 中金所时间
	/// </summary>
	public string FFEXTime
	{
		get { return StringExtend.GetString(_FFEXTime); }
		set { _FFEXTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _INETime;

	/// <summary>
	/// 能源中心时间
	/// </summary>
	public string INETime
	{
		get { return StringExtend.GetString(_INETime); }
		set { _INETime = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 用户登出请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserLogoutField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 强制交易员退出
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcForceUserLogoutField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 客户端认证请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqAuthenticateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _AuthCode;

	/// <summary>
	/// 认证码
	/// </summary>
	public string AuthCode
	{
		get { return StringExtend.GetString(_AuthCode); }
		set { _AuthCode = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _AppID;

	/// <summary>
	/// App代码
	/// </summary>
	public string AppID
	{
		get { return StringExtend.GetString(_AppID); }
		set { _AppID = StringExtend.GetBytes(value, 33); }
	}
}

/// <summary>
/// 客户端认证响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspAuthenticateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _AppID;

	/// <summary>
	/// App代码
	/// </summary>
	public string AppID
	{
		get { return StringExtend.GetString(_AppID); }
		set { _AppID = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// App类型
	/// </summary>
	public TThostFtdcAppTypeType AppType;
}

/// <summary>
/// 客户端认证信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcAuthenticationInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _AuthInfo;

	/// <summary>
	/// 认证信息
	/// </summary>
	public string AuthInfo
	{
		get { return StringExtend.GetString(_AuthInfo); }
		set { _AuthInfo = StringExtend.GetBytes(value, 129); }
	}

	/// <summary>
	/// 是否为认证结果
	/// </summary>
	public int IsResult;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _AppID;

	/// <summary>
	/// App代码
	/// </summary>
	public string AppID
	{
		get { return StringExtend.GetString(_AppID); }
		set { _AppID = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// App类型
	/// </summary>
	public TThostFtdcAppTypeType AppType;
}

/// <summary>
/// 用户登录应答2
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspUserLogin2Field
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginTime;

	/// <summary>
	/// 登录成功时间
	/// </summary>
	public string LoginTime
	{
		get { return StringExtend.GetString(_LoginTime); }
		set { _LoginTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _SystemName;

	/// <summary>
	/// 交易系统名称
	/// </summary>
	public string SystemName
	{
		get { return StringExtend.GetString(_SystemName); }
		set { _SystemName = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MaxOrderRef;

	/// <summary>
	/// 最大报单引用
	/// </summary>
	public string MaxOrderRef
	{
		get { return StringExtend.GetString(_MaxOrderRef); }
		set { _MaxOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SHFETime;

	/// <summary>
	/// 上期所时间
	/// </summary>
	public string SHFETime
	{
		get { return StringExtend.GetString(_SHFETime); }
		set { _SHFETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _DCETime;

	/// <summary>
	/// 大商所时间
	/// </summary>
	public string DCETime
	{
		get { return StringExtend.GetString(_DCETime); }
		set { _DCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CZCETime;

	/// <summary>
	/// 郑商所时间
	/// </summary>
	public string CZCETime
	{
		get { return StringExtend.GetString(_CZCETime); }
		set { _CZCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _FFEXTime;

	/// <summary>
	/// 中金所时间
	/// </summary>
	public string FFEXTime
	{
		get { return StringExtend.GetString(_FFEXTime); }
		set { _FFEXTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _INETime;

	/// <summary>
	/// 能源中心时间
	/// </summary>
	public string INETime
	{
		get { return StringExtend.GetString(_INETime); }
		set { _INETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _RandomString;

	/// <summary>
	/// 随机串
	/// </summary>
	public string RandomString
	{
		get { return StringExtend.GetString(_RandomString); }
		set { _RandomString = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 银期转帐报文头
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferHeaderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _Version;

	/// <summary>
	/// 版本号，常量，1.0
	/// </summary>
	public string Version
	{
		get { return StringExtend.GetString(_Version); }
		set { _Version = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 交易代码，必填
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期，必填，格式：yyyymmdd
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间，必填，格式：hhmmss
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeSerial;

	/// <summary>
	/// 发起方流水号，N/A
	/// </summary>
	public string TradeSerial
	{
		get { return StringExtend.GetString(_TradeSerial); }
		set { _TradeSerial = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _FutureID;

	/// <summary>
	/// 期货公司代码，必填
	/// </summary>
	public string FutureID
	{
		get { return StringExtend.GetString(_FutureID); }
		set { _FutureID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码，根据查询银行得到，必填
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码，根据查询银行得到，必填
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 操作员，N/A
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 交易设备类型，N/A
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _RecordNum;

	/// <summary>
	/// 记录数，N/A
	/// </summary>
	public string RecordNum
	{
		get { return StringExtend.GetString(_RecordNum); }
		set { _RecordNum = StringExtend.GetBytes(value, 7); }
	}

	/// <summary>
	/// 会话编号，N/A
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 请求编号，N/A
	/// </summary>
	public int RequestID;
}

/// <summary>
/// 银行资金转期货请求，TradeCode=202001
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferBankToFutureReqField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 期货资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 密码标志
	/// </summary>
	public TThostFtdcFuturePwdFlagType FuturePwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _FutureAccPwd;

	/// <summary>
	/// 密码
	/// </summary>
	public string FutureAccPwd
	{
		get { return StringExtend.GetString(_FutureAccPwd); }
		set { _FutureAccPwd = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 转账金额
	/// </summary>
	public double TradeAmt;

	/// <summary>
	/// 客户手续费
	/// </summary>
	public double CustFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种：RMB-人民币 USD-美圆 HKD-港元
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 银行资金转期货请求响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferBankToFutureRspField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _RetCode;

	/// <summary>
	/// 响应代码
	/// </summary>
	public string RetCode
	{
		get { return StringExtend.GetString(_RetCode); }
		set { _RetCode = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _RetInfo;

	/// <summary>
	/// 响应信息
	/// </summary>
	public string RetInfo
	{
		get { return StringExtend.GetString(_RetInfo); }
		set { _RetInfo = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmt;

	/// <summary>
	/// 应收客户手续费
	/// </summary>
	public double CustFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 期货资金转银行请求，TradeCode=202002
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferFutureToBankReqField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 期货资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 密码标志
	/// </summary>
	public TThostFtdcFuturePwdFlagType FuturePwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _FutureAccPwd;

	/// <summary>
	/// 密码
	/// </summary>
	public string FutureAccPwd
	{
		get { return StringExtend.GetString(_FutureAccPwd); }
		set { _FutureAccPwd = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 转账金额
	/// </summary>
	public double TradeAmt;

	/// <summary>
	/// 客户手续费
	/// </summary>
	public double CustFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种：RMB-人民币 USD-美圆 HKD-港元
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 期货资金转银行请求响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferFutureToBankRspField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _RetCode;

	/// <summary>
	/// 响应代码
	/// </summary>
	public string RetCode
	{
		get { return StringExtend.GetString(_RetCode); }
		set { _RetCode = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _RetInfo;

	/// <summary>
	/// 响应信息
	/// </summary>
	public string RetInfo
	{
		get { return StringExtend.GetString(_RetInfo); }
		set { _RetInfo = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmt;

	/// <summary>
	/// 应收客户手续费
	/// </summary>
	public double CustFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询银行资金请求，TradeCode=204002
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferQryBankReqField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 期货资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 密码标志
	/// </summary>
	public TThostFtdcFuturePwdFlagType FuturePwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _FutureAccPwd;

	/// <summary>
	/// 密码
	/// </summary>
	public string FutureAccPwd
	{
		get { return StringExtend.GetString(_FutureAccPwd); }
		set { _FutureAccPwd = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种：RMB-人民币 USD-美圆 HKD-港元
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询银行资金请求响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferQryBankRspField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _RetCode;

	/// <summary>
	/// 响应代码
	/// </summary>
	public string RetCode
	{
		get { return StringExtend.GetString(_RetCode); }
		set { _RetCode = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _RetInfo;

	/// <summary>
	/// 响应信息
	/// </summary>
	public string RetInfo
	{
		get { return StringExtend.GetString(_RetInfo); }
		set { _RetInfo = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 银行余额
	/// </summary>
	public double TradeAmt;

	/// <summary>
	/// 银行可用余额
	/// </summary>
	public double UseAmt;

	/// <summary>
	/// 银行可取余额
	/// </summary>
	public double FetchAmt;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询银行交易明细请求，TradeCode=204999
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferQryDetailReqField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 期货资金账户
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询银行交易明细请求响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferQryDetailRspField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 交易代码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	/// <summary>
	/// 期货流水号
	/// </summary>
	public int FutureSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _FutureID;

	/// <summary>
	/// 期货公司代码
	/// </summary>
	public string FutureID
	{
		get { return StringExtend.GetString(_FutureID); }
		set { _FutureID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=22)]
	private byte[] _FutureAccount;

	/// <summary>
	/// 资金帐号
	/// </summary>
	public string FutureAccount
	{
		get { return StringExtend.GetString(_FutureAccount); }
		set { _FutureAccount = StringExtend.GetBytes(value, 22); }
	}

	/// <summary>
	/// 银行流水号
	/// </summary>
	public int BankSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行账号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CertCode;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string CertCode
	{
		get { return StringExtend.GetString(_CertCode); }
		set { _CertCode = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyCode;

	/// <summary>
	/// 货币代码
	/// </summary>
	public string CurrencyCode
	{
		get { return StringExtend.GetString(_CurrencyCode); }
		set { _CurrencyCode = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 发生金额
	/// </summary>
	public double TxAmount;

	/// <summary>
	/// 有效标志
	/// </summary>
	public TThostFtdcTransferValidFlagType Flag;
}

/// <summary>
/// 响应信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspInfoField
{

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 交易所
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=61)]
	private byte[] _ExchangeName;

	/// <summary>
	/// 交易所名称
	/// </summary>
	public string ExchangeName
	{
		get { return StringExtend.GetString(_ExchangeName); }
		set { _ExchangeName = StringExtend.GetBytes(value, 61); }
	}

	/// <summary>
	/// 交易所属性
	/// </summary>
	public TThostFtdcExchangePropertyType ExchangeProperty;
}

/// <summary>
/// 产品
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcProductField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ProductName;

	/// <summary>
	/// 产品名称
	/// </summary>
	public string ProductName
	{
		get { return StringExtend.GetString(_ProductName); }
		set { _ProductName = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 产品类型
	/// </summary>
	public TThostFtdcProductClassType ProductClass;

	/// <summary>
	/// 合约数量乘数
	/// </summary>
	public int VolumeMultiple;

	/// <summary>
	/// 最小变动价位
	/// </summary>
	public double PriceTick;

	/// <summary>
	/// 市价单最大下单量
	/// </summary>
	public int MaxMarketOrderVolume;

	/// <summary>
	/// 市价单最小下单量
	/// </summary>
	public int MinMarketOrderVolume;

	/// <summary>
	/// 限价单最大下单量
	/// </summary>
	public int MaxLimitOrderVolume;

	/// <summary>
	/// 限价单最小下单量
	/// </summary>
	public int MinLimitOrderVolume;

	/// <summary>
	/// 持仓类型
	/// </summary>
	public TThostFtdcPositionTypeType PositionType;

	/// <summary>
	/// 持仓日期类型
	/// </summary>
	public TThostFtdcPositionDateTypeType PositionDateType;

	/// <summary>
	/// 平仓处理类型
	/// </summary>
	public TThostFtdcCloseDealTypeType CloseDealType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _TradeCurrencyID;

	/// <summary>
	/// 交易币种类型
	/// </summary>
	public string TradeCurrencyID
	{
		get { return StringExtend.GetString(_TradeCurrencyID); }
		set { _TradeCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 质押资金可用范围
	/// </summary>
	public TThostFtdcMortgageFundUseRangeType MortgageFundUseRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeProductID;

	/// <summary>
	/// 交易所产品代码
	/// </summary>
	public string ExchangeProductID
	{
		get { return StringExtend.GetString(_ExchangeProductID); }
		set { _ExchangeProductID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 合约基础商品乘数
	/// </summary>
	public double UnderlyingMultiple;
}

/// <summary>
/// 合约
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _InstrumentName;

	/// <summary>
	/// 合约名称
	/// </summary>
	public string InstrumentName
	{
		get { return StringExtend.GetString(_InstrumentName); }
		set { _InstrumentName = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 产品类型
	/// </summary>
	public TThostFtdcProductClassType ProductClass;

	/// <summary>
	/// 交割年份
	/// </summary>
	public int DeliveryYear;

	/// <summary>
	/// 交割月
	/// </summary>
	public int DeliveryMonth;

	/// <summary>
	/// 市价单最大下单量
	/// </summary>
	public int MaxMarketOrderVolume;

	/// <summary>
	/// 市价单最小下单量
	/// </summary>
	public int MinMarketOrderVolume;

	/// <summary>
	/// 限价单最大下单量
	/// </summary>
	public int MaxLimitOrderVolume;

	/// <summary>
	/// 限价单最小下单量
	/// </summary>
	public int MinLimitOrderVolume;

	/// <summary>
	/// 合约数量乘数
	/// </summary>
	public int VolumeMultiple;

	/// <summary>
	/// 最小变动价位
	/// </summary>
	public double PriceTick;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CreateDate;

	/// <summary>
	/// 创建日
	/// </summary>
	public string CreateDate
	{
		get { return StringExtend.GetString(_CreateDate); }
		set { _CreateDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 上市日
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExpireDate;

	/// <summary>
	/// 到期日
	/// </summary>
	public string ExpireDate
	{
		get { return StringExtend.GetString(_ExpireDate); }
		set { _ExpireDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _StartDelivDate;

	/// <summary>
	/// 开始交割日
	/// </summary>
	public string StartDelivDate
	{
		get { return StringExtend.GetString(_StartDelivDate); }
		set { _StartDelivDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _EndDelivDate;

	/// <summary>
	/// 结束交割日
	/// </summary>
	public string EndDelivDate
	{
		get { return StringExtend.GetString(_EndDelivDate); }
		set { _EndDelivDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 合约生命周期状态
	/// </summary>
	public TThostFtdcInstLifePhaseType InstLifePhase;

	/// <summary>
	/// 当前是否交易
	/// </summary>
	public int IsTrading;

	/// <summary>
	/// 持仓类型
	/// </summary>
	public TThostFtdcPositionTypeType PositionType;

	/// <summary>
	/// 持仓日期类型
	/// </summary>
	public TThostFtdcPositionDateTypeType PositionDateType;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatio;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatio;

	/// <summary>
	/// 是否使用大额单边保证金算法
	/// </summary>
	public TThostFtdcMaxMarginSideAlgorithmType MaxMarginSideAlgorithm;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _UnderlyingInstrID;

	/// <summary>
	/// 基础商品代码
	/// </summary>
	public string UnderlyingInstrID
	{
		get { return StringExtend.GetString(_UnderlyingInstrID); }
		set { _UnderlyingInstrID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 执行价
	/// </summary>
	public double StrikePrice;

	/// <summary>
	/// 期权类型
	/// </summary>
	public TThostFtdcOptionsTypeType OptionsType;

	/// <summary>
	/// 合约基础商品乘数
	/// </summary>
	public double UnderlyingMultiple;

	/// <summary>
	/// 组合类型
	/// </summary>
	public TThostFtdcCombinationTypeType CombinationType;
}

/// <summary>
/// 经纪公司
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BrokerAbbr;

	/// <summary>
	/// 经纪公司简称
	/// </summary>
	public string BrokerAbbr
	{
		get { return StringExtend.GetString(_BrokerAbbr); }
		set { _BrokerAbbr = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _BrokerName;

	/// <summary>
	/// 经纪公司名称
	/// </summary>
	public string BrokerName
	{
		get { return StringExtend.GetString(_BrokerName); }
		set { _BrokerName = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;
}

/// <summary>
/// 交易所交易员
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTraderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装数量
	/// </summary>
	public int InstallCount;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 投资者
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorGroupID;

	/// <summary>
	/// 投资者分组代码
	/// </summary>
	public string InvestorGroupID
	{
		get { return StringExtend.GetString(_InvestorGroupID); }
		set { _InvestorGroupID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _InvestorName;

	/// <summary>
	/// 投资者名称
	/// </summary>
	public string InvestorName
	{
		get { return StringExtend.GetString(_InvestorName); }
		set { _InvestorName = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdentifiedCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 联系电话
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 通讯地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 开户日期
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Mobile;

	/// <summary>
	/// 手机
	/// </summary>
	public string Mobile
	{
		get { return StringExtend.GetString(_Mobile); }
		set { _Mobile = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CommModelID;

	/// <summary>
	/// 手续费率模板代码
	/// </summary>
	public string CommModelID
	{
		get { return StringExtend.GetString(_CommModelID); }
		set { _CommModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MarginModelID;

	/// <summary>
	/// 保证金率模板代码
	/// </summary>
	public string MarginModelID
	{
		get { return StringExtend.GetString(_MarginModelID); }
		set { _MarginModelID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 交易编码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingCodeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	/// <summary>
	/// 交易编码类型
	/// </summary>
	public TThostFtdcClientIDTypeType ClientIDType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 业务类型
	/// </summary>
	public TThostFtdcBizTypeType BizType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 会员编码和经纪公司编码对照表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcPartBrokerField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;
}

/// <summary>
/// 管理用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSuperUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _UserName;

	/// <summary>
	/// 用户名称
	/// </summary>
	public string UserName
	{
		get { return StringExtend.GetString(_UserName); }
		set { _UserName = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;
}

/// <summary>
/// 管理用户功能权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSuperUserFunctionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 功能代码
	/// </summary>
	public TThostFtdcFunctionCodeType FunctionCode;
}

/// <summary>
/// 投资者组
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorGroupField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorGroupID;

	/// <summary>
	/// 投资者分组代码
	/// </summary>
	public string InvestorGroupID
	{
		get { return StringExtend.GetString(_InvestorGroupID); }
		set { _InvestorGroupID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _InvestorGroupName;

	/// <summary>
	/// 投资者分组名称
	/// </summary>
	public string InvestorGroupName
	{
		get { return StringExtend.GetString(_InvestorGroupName); }
		set { _InvestorGroupName = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 资金账户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 上次质押金额
	/// </summary>
	public double PreMortgage;

	/// <summary>
	/// 上次信用额度
	/// </summary>
	public double PreCredit;

	/// <summary>
	/// 上次存款额
	/// </summary>
	public double PreDeposit;

	/// <summary>
	/// 上次结算准备金
	/// </summary>
	public double PreBalance;

	/// <summary>
	/// 上次占用的保证金
	/// </summary>
	public double PreMargin;

	/// <summary>
	/// 利息基数
	/// </summary>
	public double InterestBase;

	/// <summary>
	/// 利息收入
	/// </summary>
	public double Interest;

	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;

	/// <summary>
	/// 出金金额
	/// </summary>
	public double Withdraw;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;

	/// <summary>
	/// 冻结的资金
	/// </summary>
	public double FrozenCash;

	/// <summary>
	/// 冻结的手续费
	/// </summary>
	public double FrozenCommission;

	/// <summary>
	/// 当前保证金总额
	/// </summary>
	public double CurrMargin;

	/// <summary>
	/// 资金差额
	/// </summary>
	public double CashIn;

	/// <summary>
	/// 手续费
	/// </summary>
	public double Commission;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;

	/// <summary>
	/// 期货结算准备金
	/// </summary>
	public double Balance;

	/// <summary>
	/// 可用资金
	/// </summary>
	public double Available;

	/// <summary>
	/// 可取资金
	/// </summary>
	public double WithdrawQuota;

	/// <summary>
	/// 基本准备金
	/// </summary>
	public double Reserve;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 信用额度
	/// </summary>
	public double Credit;

	/// <summary>
	/// 质押金额
	/// </summary>
	public double Mortgage;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchangeMargin;

	/// <summary>
	/// 投资者交割保证金
	/// </summary>
	public double DeliveryMargin;

	/// <summary>
	/// 交易所交割保证金
	/// </summary>
	public double ExchangeDeliveryMargin;

	/// <summary>
	/// 保底期货结算准备金
	/// </summary>
	public double ReserveBalance;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 上次货币质入金额
	/// </summary>
	public double PreFundMortgageIn;

	/// <summary>
	/// 上次货币质出金额
	/// </summary>
	public double PreFundMortgageOut;

	/// <summary>
	/// 货币质入金额
	/// </summary>
	public double FundMortgageIn;

	/// <summary>
	/// 货币质出金额
	/// </summary>
	public double FundMortgageOut;

	/// <summary>
	/// 货币质押余额
	/// </summary>
	public double FundMortgageAvailable;

	/// <summary>
	/// 可质押货币金额
	/// </summary>
	public double MortgageableFund;

	/// <summary>
	/// 特殊产品占用保证金
	/// </summary>
	public double SpecProductMargin;

	/// <summary>
	/// 特殊产品冻结保证金
	/// </summary>
	public double SpecProductFrozenMargin;

	/// <summary>
	/// 特殊产品手续费
	/// </summary>
	public double SpecProductCommission;

	/// <summary>
	/// 特殊产品冻结手续费
	/// </summary>
	public double SpecProductFrozenCommission;

	/// <summary>
	/// 特殊产品持仓盈亏
	/// </summary>
	public double SpecProductPositionProfit;

	/// <summary>
	/// 特殊产品平仓盈亏
	/// </summary>
	public double SpecProductCloseProfit;

	/// <summary>
	/// 根据持仓盈亏算法计算的特殊产品持仓盈亏
	/// </summary>
	public double SpecProductPositionProfitByAlg;

	/// <summary>
	/// 特殊产品交易所保证金
	/// </summary>
	public double SpecProductExchangeMargin;

	/// <summary>
	/// 业务类型
	/// </summary>
	public TThostFtdcBizTypeType BizType;

	/// <summary>
	/// 延时换汇冻结金额
	/// </summary>
	public double FrozenSwap;

	/// <summary>
	/// 剩余换汇额度
	/// </summary>
	public double RemainSwap;
}

/// <summary>
/// 投资者持仓
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorPositionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 持仓多空方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 持仓日期
	/// </summary>
	public TThostFtdcPositionDateType PositionDate;

	/// <summary>
	/// 上日持仓
	/// </summary>
	public int YdPosition;

	/// <summary>
	/// 今日持仓
	/// </summary>
	public int Position;

	/// <summary>
	/// 多头冻结
	/// </summary>
	public int LongFrozen;

	/// <summary>
	/// 空头冻结
	/// </summary>
	public int ShortFrozen;

	/// <summary>
	/// 开仓冻结金额
	/// </summary>
	public double LongFrozenAmount;

	/// <summary>
	/// 开仓冻结金额
	/// </summary>
	public double ShortFrozenAmount;

	/// <summary>
	/// 开仓量
	/// </summary>
	public int OpenVolume;

	/// <summary>
	/// 平仓量
	/// </summary>
	public int CloseVolume;

	/// <summary>
	/// 开仓金额
	/// </summary>
	public double OpenAmount;

	/// <summary>
	/// 平仓金额
	/// </summary>
	public double CloseAmount;

	/// <summary>
	/// 持仓成本
	/// </summary>
	public double PositionCost;

	/// <summary>
	/// 上次占用的保证金
	/// </summary>
	public double PreMargin;

	/// <summary>
	/// 占用的保证金
	/// </summary>
	public double UseMargin;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;

	/// <summary>
	/// 冻结的资金
	/// </summary>
	public double FrozenCash;

	/// <summary>
	/// 冻结的手续费
	/// </summary>
	public double FrozenCommission;

	/// <summary>
	/// 资金差额
	/// </summary>
	public double CashIn;

	/// <summary>
	/// 手续费
	/// </summary>
	public double Commission;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;

	/// <summary>
	/// 上次结算价
	/// </summary>
	public double PreSettlementPrice;

	/// <summary>
	/// 本次结算价
	/// </summary>
	public double SettlementPrice;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 开仓成本
	/// </summary>
	public double OpenCost;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchangeMargin;

	/// <summary>
	/// 组合成交形成的持仓
	/// </summary>
	public int CombPosition;

	/// <summary>
	/// 组合多头冻结
	/// </summary>
	public int CombLongFrozen;

	/// <summary>
	/// 组合空头冻结
	/// </summary>
	public int CombShortFrozen;

	/// <summary>
	/// 逐日盯市平仓盈亏
	/// </summary>
	public double CloseProfitByDate;

	/// <summary>
	/// 逐笔对冲平仓盈亏
	/// </summary>
	public double CloseProfitByTrade;

	/// <summary>
	/// 今日持仓
	/// </summary>
	public int TodayPosition;

	/// <summary>
	/// 保证金率
	/// </summary>
	public double MarginRateByMoney;

	/// <summary>
	/// 保证金率(按手数)
	/// </summary>
	public double MarginRateByVolume;

	/// <summary>
	/// 执行冻结
	/// </summary>
	public int StrikeFrozen;

	/// <summary>
	/// 执行冻结金额
	/// </summary>
	public double StrikeFrozenAmount;

	/// <summary>
	/// 放弃执行冻结
	/// </summary>
	public int AbandonFrozen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 执行冻结的昨仓
	/// </summary>
	public int YdStrikeFrozen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 大商所持仓成本差值，只有大商所使用
	/// </summary>
	public double PositionCostOffset;
}

/// <summary>
/// 合约保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentMarginRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;

	/// <summary>
	/// 是否相对交易所收取
	/// </summary>
	public int IsRelative;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 合约手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentCommissionRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 开仓手续费率
	/// </summary>
	public double OpenRatioByMoney;

	/// <summary>
	/// 开仓手续费
	/// </summary>
	public double OpenRatioByVolume;

	/// <summary>
	/// 平仓手续费率
	/// </summary>
	public double CloseRatioByMoney;

	/// <summary>
	/// 平仓手续费
	/// </summary>
	public double CloseRatioByVolume;

	/// <summary>
	/// 平今手续费率
	/// </summary>
	public double CloseTodayRatioByMoney;

	/// <summary>
	/// 平今手续费
	/// </summary>
	public double CloseTodayRatioByVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 业务类型
	/// </summary>
	public TThostFtdcBizTypeType BizType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 深度行情
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDepthMarketDataField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;

	/// <summary>
	/// 上次结算价
	/// </summary>
	public double PreSettlementPrice;

	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;

	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;

	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;

	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;

	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;

	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;

	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;

	/// <summary>
	/// 本次结算价
	/// </summary>
	public double SettlementPrice;

	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;

	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;

	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;

	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;

	/// <summary>
	/// 申买价一
	/// </summary>
	public double BidPrice1;

	/// <summary>
	/// 申买量一
	/// </summary>
	public int BidVolume1;

	/// <summary>
	/// 申卖价一
	/// </summary>
	public double AskPrice1;

	/// <summary>
	/// 申卖量一
	/// </summary>
	public int AskVolume1;

	/// <summary>
	/// 申买价二
	/// </summary>
	public double BidPrice2;

	/// <summary>
	/// 申买量二
	/// </summary>
	public int BidVolume2;

	/// <summary>
	/// 申卖价二
	/// </summary>
	public double AskPrice2;

	/// <summary>
	/// 申卖量二
	/// </summary>
	public int AskVolume2;

	/// <summary>
	/// 申买价三
	/// </summary>
	public double BidPrice3;

	/// <summary>
	/// 申买量三
	/// </summary>
	public int BidVolume3;

	/// <summary>
	/// 申卖价三
	/// </summary>
	public double AskPrice3;

	/// <summary>
	/// 申卖量三
	/// </summary>
	public int AskVolume3;

	/// <summary>
	/// 申买价四
	/// </summary>
	public double BidPrice4;

	/// <summary>
	/// 申买量四
	/// </summary>
	public int BidVolume4;

	/// <summary>
	/// 申卖价四
	/// </summary>
	public double AskPrice4;

	/// <summary>
	/// 申卖量四
	/// </summary>
	public int AskVolume4;

	/// <summary>
	/// 申买价五
	/// </summary>
	public double BidPrice5;

	/// <summary>
	/// 申买量五
	/// </summary>
	public int BidVolume5;

	/// <summary>
	/// 申卖价五
	/// </summary>
	public double AskPrice5;

	/// <summary>
	/// 申卖量五
	/// </summary>
	public int AskVolume5;

	/// <summary>
	/// 当日均价
	/// </summary>
	public double AveragePrice;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDay;

	/// <summary>
	/// 业务日期
	/// </summary>
	public string ActionDay
	{
		get { return StringExtend.GetString(_ActionDay); }
		set { _ActionDay = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 投资者合约交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentTradingRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 交易权限
	/// </summary>
	public TThostFtdcTradingRightType TradingRight;
}

/// <summary>
/// 经纪公司用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _UserName;

	/// <summary>
	/// 用户名称
	/// </summary>
	public string UserName
	{
		get { return StringExtend.GetString(_UserName); }
		set { _UserName = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 用户类型
	/// </summary>
	public TThostFtdcUserTypeType UserType;

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	/// <summary>
	/// 是否使用令牌
	/// </summary>
	public int IsUsingOTP;

	/// <summary>
	/// 是否强制终端认证
	/// </summary>
	public int IsAuthForce;
}

/// <summary>
/// 经纪公司用户口令
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserPasswordField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _LastUpdateTime;

	/// <summary>
	/// 上次修改时间
	/// </summary>
	public string LastUpdateTime
	{
		get { return StringExtend.GetString(_LastUpdateTime); }
		set { _LastUpdateTime = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _LastLoginTime;

	/// <summary>
	/// 上次登陆时间
	/// </summary>
	public string LastLoginTime
	{
		get { return StringExtend.GetString(_LastLoginTime); }
		set { _LastLoginTime = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExpireDate;

	/// <summary>
	/// 密码过期时间
	/// </summary>
	public string ExpireDate
	{
		get { return StringExtend.GetString(_ExpireDate); }
		set { _ExpireDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _WeakExpireDate;

	/// <summary>
	/// 弱密码过期时间
	/// </summary>
	public string WeakExpireDate
	{
		get { return StringExtend.GetString(_WeakExpireDate); }
		set { _WeakExpireDate = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 经纪公司用户功能权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserFunctionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司功能代码
	/// </summary>
	public TThostFtdcBrokerFunctionCodeType BrokerFunctionCode;
}

/// <summary>
/// 交易所交易员报盘机
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTraderOfferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 交易所交易员连接状态
	/// </summary>
	public TThostFtdcTraderConnectStatusType TraderConnectStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectRequestDate;

	/// <summary>
	/// 发出连接请求的日期
	/// </summary>
	public string ConnectRequestDate
	{
		get { return StringExtend.GetString(_ConnectRequestDate); }
		set { _ConnectRequestDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectRequestTime;

	/// <summary>
	/// 发出连接请求的时间
	/// </summary>
	public string ConnectRequestTime
	{
		get { return StringExtend.GetString(_ConnectRequestTime); }
		set { _ConnectRequestTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportDate;

	/// <summary>
	/// 上次报告日期
	/// </summary>
	public string LastReportDate
	{
		get { return StringExtend.GetString(_LastReportDate); }
		set { _LastReportDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportTime;

	/// <summary>
	/// 上次报告时间
	/// </summary>
	public string LastReportTime
	{
		get { return StringExtend.GetString(_LastReportTime); }
		set { _LastReportTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectDate;

	/// <summary>
	/// 完成连接日期
	/// </summary>
	public string ConnectDate
	{
		get { return StringExtend.GetString(_ConnectDate); }
		set { _ConnectDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectTime;

	/// <summary>
	/// 完成连接时间
	/// </summary>
	public string ConnectTime
	{
		get { return StringExtend.GetString(_ConnectTime); }
		set { _ConnectTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _StartDate;

	/// <summary>
	/// 启动日期
	/// </summary>
	public string StartDate
	{
		get { return StringExtend.GetString(_StartDate); }
		set { _StartDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _StartTime;

	/// <summary>
	/// 启动时间
	/// </summary>
	public string StartTime
	{
		get { return StringExtend.GetString(_StartTime); }
		set { _StartTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MaxTradeID;

	/// <summary>
	/// 本席位最大成交编号
	/// </summary>
	public string MaxTradeID
	{
		get { return StringExtend.GetString(_MaxTradeID); }
		set { _MaxTradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _MaxOrderMessageReference;

	/// <summary>
	/// 本席位最大报单备拷
	/// </summary>
	public string MaxOrderMessageReference
	{
		get { return StringExtend.GetString(_MaxOrderMessageReference); }
		set { _MaxOrderMessageReference = StringExtend.GetBytes(value, 7); }
	}
}

/// <summary>
/// 投资者结算结果
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSettlementInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=501)]
	private byte[] _Content;

	/// <summary>
	/// 消息正文
	/// </summary>
	public string Content
	{
		get { return StringExtend.GetString(_Content); }
		set { _Content = StringExtend.GetBytes(value, 501); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 合约保证金率调整
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentMarginRateAdjustField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;

	/// <summary>
	/// 是否相对交易所收取
	/// </summary>
	public int IsRelative;
}

/// <summary>
/// 交易所保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeMarginRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所保证金率调整
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeMarginRateAdjustField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 跟随交易所投资者多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 跟随交易所投资者多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 跟随交易所投资者空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 跟随交易所投资者空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;

	/// <summary>
	/// 交易所多头保证金率
	/// </summary>
	public double ExchLongMarginRatioByMoney;

	/// <summary>
	/// 交易所多头保证金费
	/// </summary>
	public double ExchLongMarginRatioByVolume;

	/// <summary>
	/// 交易所空头保证金率
	/// </summary>
	public double ExchShortMarginRatioByMoney;

	/// <summary>
	/// 交易所空头保证金费
	/// </summary>
	public double ExchShortMarginRatioByVolume;

	/// <summary>
	/// 不跟随交易所投资者多头保证金率
	/// </summary>
	public double NoLongMarginRatioByMoney;

	/// <summary>
	/// 不跟随交易所投资者多头保证金费
	/// </summary>
	public double NoLongMarginRatioByVolume;

	/// <summary>
	/// 不跟随交易所投资者空头保证金率
	/// </summary>
	public double NoShortMarginRatioByMoney;

	/// <summary>
	/// 不跟随交易所投资者空头保证金费
	/// </summary>
	public double NoShortMarginRatioByVolume;
}

/// <summary>
/// 汇率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _FromCurrencyID;

	/// <summary>
	/// 源币种
	/// </summary>
	public string FromCurrencyID
	{
		get { return StringExtend.GetString(_FromCurrencyID); }
		set { _FromCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 源币种单位数量
	/// </summary>
	public double FromCurrencyUnit;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _ToCurrencyID;

	/// <summary>
	/// 目标币种
	/// </summary>
	public string ToCurrencyID
	{
		get { return StringExtend.GetString(_ToCurrencyID); }
		set { _ToCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇率
	/// </summary>
	public double ExchangeRate;
}

/// <summary>
/// 结算引用
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSettlementRefField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;
}

/// <summary>
/// 当前时间
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCurrentTimeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CurrDate;

	/// <summary>
	/// 当前日期
	/// </summary>
	public string CurrDate
	{
		get { return StringExtend.GetString(_CurrDate); }
		set { _CurrDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CurrTime;

	/// <summary>
	/// 当前时间
	/// </summary>
	public string CurrTime
	{
		get { return StringExtend.GetString(_CurrTime); }
		set { _CurrTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 当前时间（毫秒）
	/// </summary>
	public int CurrMillisec;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDay;

	/// <summary>
	/// 业务日期
	/// </summary>
	public string ActionDay
	{
		get { return StringExtend.GetString(_ActionDay); }
		set { _ActionDay = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 通讯阶段
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCommPhaseField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 通讯时段编号
	/// </summary>
	public short CommPhaseNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _SystemID;

	/// <summary>
	/// 系统编号
	/// </summary>
	public string SystemID
	{
		get { return StringExtend.GetString(_SystemID); }
		set { _SystemID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 登录信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLoginInfoField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginDate;

	/// <summary>
	/// 登录日期
	/// </summary>
	public string LoginDate
	{
		get { return StringExtend.GetString(_LoginDate); }
		set { _LoginDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginTime;

	/// <summary>
	/// 登录时间
	/// </summary>
	public string LoginTime
	{
		get { return StringExtend.GetString(_LoginTime); }
		set { _LoginTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _SystemName;

	/// <summary>
	/// 系统名称
	/// </summary>
	public string SystemName
	{
		get { return StringExtend.GetString(_SystemName); }
		set { _SystemName = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _PasswordDeprecated;

	/// <summary>
	/// 密码,已弃用
	/// </summary>
	public string PasswordDeprecated
	{
		get { return StringExtend.GetString(_PasswordDeprecated); }
		set { _PasswordDeprecated = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MaxOrderRef;

	/// <summary>
	/// 最大报单引用
	/// </summary>
	public string MaxOrderRef
	{
		get { return StringExtend.GetString(_MaxOrderRef); }
		set { _MaxOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SHFETime;

	/// <summary>
	/// 上期所时间
	/// </summary>
	public string SHFETime
	{
		get { return StringExtend.GetString(_SHFETime); }
		set { _SHFETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _DCETime;

	/// <summary>
	/// 大商所时间
	/// </summary>
	public string DCETime
	{
		get { return StringExtend.GetString(_DCETime); }
		set { _DCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CZCETime;

	/// <summary>
	/// 郑商所时间
	/// </summary>
	public string CZCETime
	{
		get { return StringExtend.GetString(_CZCETime); }
		set { _CZCETime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _FFEXTime;

	/// <summary>
	/// 中金所时间
	/// </summary>
	public string FFEXTime
	{
		get { return StringExtend.GetString(_FFEXTime); }
		set { _FFEXTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OneTimePassword;

	/// <summary>
	/// 动态密码
	/// </summary>
	public string OneTimePassword
	{
		get { return StringExtend.GetString(_OneTimePassword); }
		set { _OneTimePassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _INETime;

	/// <summary>
	/// 能源中心时间
	/// </summary>
	public string INETime
	{
		get { return StringExtend.GetString(_INETime); }
		set { _INETime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 查询时是否需要流控
	/// </summary>
	public int IsQryControl;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 登录信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLogoutAllField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _SystemName;

	/// <summary>
	/// 系统名称
	/// </summary>
	public string SystemName
	{
		get { return StringExtend.GetString(_SystemName); }
		set { _SystemName = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 前置状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcFrontStatusField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportDate;

	/// <summary>
	/// 上次报告日期
	/// </summary>
	public string LastReportDate
	{
		get { return StringExtend.GetString(_LastReportDate); }
		set { _LastReportDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportTime;

	/// <summary>
	/// 上次报告时间
	/// </summary>
	public string LastReportTime
	{
		get { return StringExtend.GetString(_LastReportTime); }
		set { _LastReportTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;
}

/// <summary>
/// 用户口令变更
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserPasswordUpdateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OldPassword;

	/// <summary>
	/// 原来的口令
	/// </summary>
	public string OldPassword
	{
		get { return StringExtend.GetString(_OldPassword); }
		set { _OldPassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewPassword;

	/// <summary>
	/// 新的口令
	/// </summary>
	public string NewPassword
	{
		get { return StringExtend.GetString(_NewPassword); }
		set { _NewPassword = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 输入报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 用户强评标志
	/// </summary>
	public int UserForceClose;

	/// <summary>
	/// 互换单标志
	/// </summary>
	public int IsSwapOrder;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 报单提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单来源
	/// </summary>
	public TThostFtdcOrderSourceType OrderSource;

	/// <summary>
	/// 报单状态
	/// </summary>
	public TThostFtdcOrderStatusType OrderStatus;

	/// <summary>
	/// 报单类型
	/// </summary>
	public TThostFtdcOrderTypeType OrderType;

	/// <summary>
	/// 今成交数量
	/// </summary>
	public int VolumeTraded;

	/// <summary>
	/// 剩余数量
	/// </summary>
	public int VolumeTotal;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 委托时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActiveTime;

	/// <summary>
	/// 激活时间
	/// </summary>
	public string ActiveTime
	{
		get { return StringExtend.GetString(_ActiveTime); }
		set { _ActiveTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SuspendTime;

	/// <summary>
	/// 挂起时间
	/// </summary>
	public string SuspendTime
	{
		get { return StringExtend.GetString(_SuspendTime); }
		set { _SuspendTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ActiveTraderID;

	/// <summary>
	/// 最后修改交易所交易员代码
	/// </summary>
	public string ActiveTraderID
	{
		get { return StringExtend.GetString(_ActiveTraderID); }
		set { _ActiveTraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 用户强评标志
	/// </summary>
	public int UserForceClose;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司报单编号
	/// </summary>
	public int BrokerOrderSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _RelativeOrderSysID;

	/// <summary>
	/// 相关报单
	/// </summary>
	public string RelativeOrderSysID
	{
		get { return StringExtend.GetString(_RelativeOrderSysID); }
		set { _RelativeOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 郑商所成交数量
	/// </summary>
	public int ZCETotalTradedVolume;

	/// <summary>
	/// 互换单标志
	/// </summary>
	public int IsSwapOrder;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOrderField
{

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 报单提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单来源
	/// </summary>
	public TThostFtdcOrderSourceType OrderSource;

	/// <summary>
	/// 报单状态
	/// </summary>
	public TThostFtdcOrderStatusType OrderStatus;

	/// <summary>
	/// 报单类型
	/// </summary>
	public TThostFtdcOrderTypeType OrderType;

	/// <summary>
	/// 今成交数量
	/// </summary>
	public int VolumeTraded;

	/// <summary>
	/// 剩余数量
	/// </summary>
	public int VolumeTotal;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 委托时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActiveTime;

	/// <summary>
	/// 激活时间
	/// </summary>
	public string ActiveTime
	{
		get { return StringExtend.GetString(_ActiveTime); }
		set { _ActiveTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SuspendTime;

	/// <summary>
	/// 挂起时间
	/// </summary>
	public string SuspendTime
	{
		get { return StringExtend.GetString(_SuspendTime); }
		set { _SuspendTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ActiveTraderID;

	/// <summary>
	/// 最后修改交易所交易员代码
	/// </summary>
	public string ActiveTraderID
	{
		get { return StringExtend.GetString(_ActiveTraderID); }
		set { _ActiveTraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报单插入失败
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOrderInsertErrorField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 输入报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报单操作失败
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOrderActionErrorField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 交易所成交
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeTradeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TradeID;

	/// <summary>
	/// 成交编号
	/// </summary>
	public string TradeID
	{
		get { return StringExtend.GetString(_TradeID); }
		set { _TradeID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 交易角色
	/// </summary>
	public TThostFtdcTradingRoleType TradingRole;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double Price;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 成交时期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 成交时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交类型
	/// </summary>
	public TThostFtdcTradeTypeType TradeType;

	/// <summary>
	/// 成交价来源
	/// </summary>
	public TThostFtdcPriceSourceType PriceSource;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 成交来源
	/// </summary>
	public TThostFtdcTradeSourceType TradeSource;
}

/// <summary>
/// 成交
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TradeID;

	/// <summary>
	/// 成交编号
	/// </summary>
	public string TradeID
	{
		get { return StringExtend.GetString(_TradeID); }
		set { _TradeID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 交易角色
	/// </summary>
	public TThostFtdcTradingRoleType TradingRole;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double Price;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 成交时期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 成交时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交类型
	/// </summary>
	public TThostFtdcTradeTypeType TradeType;

	/// <summary>
	/// 成交价来源
	/// </summary>
	public TThostFtdcPriceSourceType PriceSource;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 经纪公司报单编号
	/// </summary>
	public int BrokerOrderSeq;

	/// <summary>
	/// 成交来源
	/// </summary>
	public TThostFtdcTradeSourceType TradeSource;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 用户会话
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserSessionField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginDate;

	/// <summary>
	/// 登录日期
	/// </summary>
	public string LoginDate
	{
		get { return StringExtend.GetString(_LoginDate); }
		set { _LoginDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LoginTime;

	/// <summary>
	/// 登录时间
	/// </summary>
	public string LoginTime
	{
		get { return StringExtend.GetString(_LoginTime); }
		set { _LoginTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}
}

/// <summary>
/// 查询最大报单数量
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQueryMaxOrderVolumeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 最大允许报单数量
	/// </summary>
	public int MaxVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 投资者结算结果确认信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSettlementInfoConfirmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConfirmDate;

	/// <summary>
	/// 确认日期
	/// </summary>
	public string ConfirmDate
	{
		get { return StringExtend.GetString(_ConfirmDate); }
		set { _ConfirmDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConfirmTime;

	/// <summary>
	/// 确认时间
	/// </summary>
	public string ConfirmTime
	{
		get { return StringExtend.GetString(_ConfirmTime); }
		set { _ConfirmTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 出入金同步
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncDepositField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _DepositSeqNo;

	/// <summary>
	/// 出入金流水号
	/// </summary>
	public string DepositSeqNo
	{
		get { return StringExtend.GetString(_DepositSeqNo); }
		set { _DepositSeqNo = StringExtend.GetBytes(value, 15); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;

	/// <summary>
	/// 是否强制进行
	/// </summary>
	public int IsForce;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 货币质押同步
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncFundMortgageField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _MortgageSeqNo;

	/// <summary>
	/// 货币质押流水号
	/// </summary>
	public string MortgageSeqNo
	{
		get { return StringExtend.GetString(_MortgageSeqNo); }
		set { _MortgageSeqNo = StringExtend.GetBytes(value, 15); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _FromCurrencyID;

	/// <summary>
	/// 源币种
	/// </summary>
	public string FromCurrencyID
	{
		get { return StringExtend.GetString(_FromCurrencyID); }
		set { _FromCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 质押金额
	/// </summary>
	public double MortgageAmount;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _ToCurrencyID;

	/// <summary>
	/// 目标币种
	/// </summary>
	public string ToCurrencyID
	{
		get { return StringExtend.GetString(_ToCurrencyID); }
		set { _ToCurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 经纪公司同步
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerSyncField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 正在同步中的投资者
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInvestorField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorGroupID;

	/// <summary>
	/// 投资者分组代码
	/// </summary>
	public string InvestorGroupID
	{
		get { return StringExtend.GetString(_InvestorGroupID); }
		set { _InvestorGroupID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _InvestorName;

	/// <summary>
	/// 投资者名称
	/// </summary>
	public string InvestorName
	{
		get { return StringExtend.GetString(_InvestorName); }
		set { _InvestorName = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdentifiedCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 联系电话
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 通讯地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 开户日期
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Mobile;

	/// <summary>
	/// 手机
	/// </summary>
	public string Mobile
	{
		get { return StringExtend.GetString(_Mobile); }
		set { _Mobile = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CommModelID;

	/// <summary>
	/// 手续费率模板代码
	/// </summary>
	public string CommModelID
	{
		get { return StringExtend.GetString(_CommModelID); }
		set { _CommModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MarginModelID;

	/// <summary>
	/// 保证金率模板代码
	/// </summary>
	public string MarginModelID
	{
		get { return StringExtend.GetString(_MarginModelID); }
		set { _MarginModelID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 正在同步中的交易代码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingTradingCodeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	/// <summary>
	/// 交易编码类型
	/// </summary>
	public TThostFtdcClientIDTypeType ClientIDType;
}

/// <summary>
/// 正在同步中的投资者分组
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInvestorGroupField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorGroupID;

	/// <summary>
	/// 投资者分组代码
	/// </summary>
	public string InvestorGroupID
	{
		get { return StringExtend.GetString(_InvestorGroupID); }
		set { _InvestorGroupID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _InvestorGroupName;

	/// <summary>
	/// 投资者分组名称
	/// </summary>
	public string InvestorGroupName
	{
		get { return StringExtend.GetString(_InvestorGroupName); }
		set { _InvestorGroupName = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 正在同步中的交易账号
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingTradingAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 上次质押金额
	/// </summary>
	public double PreMortgage;

	/// <summary>
	/// 上次信用额度
	/// </summary>
	public double PreCredit;

	/// <summary>
	/// 上次存款额
	/// </summary>
	public double PreDeposit;

	/// <summary>
	/// 上次结算准备金
	/// </summary>
	public double PreBalance;

	/// <summary>
	/// 上次占用的保证金
	/// </summary>
	public double PreMargin;

	/// <summary>
	/// 利息基数
	/// </summary>
	public double InterestBase;

	/// <summary>
	/// 利息收入
	/// </summary>
	public double Interest;

	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;

	/// <summary>
	/// 出金金额
	/// </summary>
	public double Withdraw;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;

	/// <summary>
	/// 冻结的资金
	/// </summary>
	public double FrozenCash;

	/// <summary>
	/// 冻结的手续费
	/// </summary>
	public double FrozenCommission;

	/// <summary>
	/// 当前保证金总额
	/// </summary>
	public double CurrMargin;

	/// <summary>
	/// 资金差额
	/// </summary>
	public double CashIn;

	/// <summary>
	/// 手续费
	/// </summary>
	public double Commission;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;

	/// <summary>
	/// 期货结算准备金
	/// </summary>
	public double Balance;

	/// <summary>
	/// 可用资金
	/// </summary>
	public double Available;

	/// <summary>
	/// 可取资金
	/// </summary>
	public double WithdrawQuota;

	/// <summary>
	/// 基本准备金
	/// </summary>
	public double Reserve;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 信用额度
	/// </summary>
	public double Credit;

	/// <summary>
	/// 质押金额
	/// </summary>
	public double Mortgage;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchangeMargin;

	/// <summary>
	/// 投资者交割保证金
	/// </summary>
	public double DeliveryMargin;

	/// <summary>
	/// 交易所交割保证金
	/// </summary>
	public double ExchangeDeliveryMargin;

	/// <summary>
	/// 保底期货结算准备金
	/// </summary>
	public double ReserveBalance;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 上次货币质入金额
	/// </summary>
	public double PreFundMortgageIn;

	/// <summary>
	/// 上次货币质出金额
	/// </summary>
	public double PreFundMortgageOut;

	/// <summary>
	/// 货币质入金额
	/// </summary>
	public double FundMortgageIn;

	/// <summary>
	/// 货币质出金额
	/// </summary>
	public double FundMortgageOut;

	/// <summary>
	/// 货币质押余额
	/// </summary>
	public double FundMortgageAvailable;

	/// <summary>
	/// 可质押货币金额
	/// </summary>
	public double MortgageableFund;

	/// <summary>
	/// 特殊产品占用保证金
	/// </summary>
	public double SpecProductMargin;

	/// <summary>
	/// 特殊产品冻结保证金
	/// </summary>
	public double SpecProductFrozenMargin;

	/// <summary>
	/// 特殊产品手续费
	/// </summary>
	public double SpecProductCommission;

	/// <summary>
	/// 特殊产品冻结手续费
	/// </summary>
	public double SpecProductFrozenCommission;

	/// <summary>
	/// 特殊产品持仓盈亏
	/// </summary>
	public double SpecProductPositionProfit;

	/// <summary>
	/// 特殊产品平仓盈亏
	/// </summary>
	public double SpecProductCloseProfit;

	/// <summary>
	/// 根据持仓盈亏算法计算的特殊产品持仓盈亏
	/// </summary>
	public double SpecProductPositionProfitByAlg;

	/// <summary>
	/// 特殊产品交易所保证金
	/// </summary>
	public double SpecProductExchangeMargin;

	/// <summary>
	/// 延时换汇冻结金额
	/// </summary>
	public double FrozenSwap;

	/// <summary>
	/// 剩余换汇额度
	/// </summary>
	public double RemainSwap;
}

/// <summary>
/// 正在同步中的投资者持仓
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInvestorPositionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 持仓多空方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 持仓日期
	/// </summary>
	public TThostFtdcPositionDateType PositionDate;

	/// <summary>
	/// 上日持仓
	/// </summary>
	public int YdPosition;

	/// <summary>
	/// 今日持仓
	/// </summary>
	public int Position;

	/// <summary>
	/// 多头冻结
	/// </summary>
	public int LongFrozen;

	/// <summary>
	/// 空头冻结
	/// </summary>
	public int ShortFrozen;

	/// <summary>
	/// 开仓冻结金额
	/// </summary>
	public double LongFrozenAmount;

	/// <summary>
	/// 开仓冻结金额
	/// </summary>
	public double ShortFrozenAmount;

	/// <summary>
	/// 开仓量
	/// </summary>
	public int OpenVolume;

	/// <summary>
	/// 平仓量
	/// </summary>
	public int CloseVolume;

	/// <summary>
	/// 开仓金额
	/// </summary>
	public double OpenAmount;

	/// <summary>
	/// 平仓金额
	/// </summary>
	public double CloseAmount;

	/// <summary>
	/// 持仓成本
	/// </summary>
	public double PositionCost;

	/// <summary>
	/// 上次占用的保证金
	/// </summary>
	public double PreMargin;

	/// <summary>
	/// 占用的保证金
	/// </summary>
	public double UseMargin;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;

	/// <summary>
	/// 冻结的资金
	/// </summary>
	public double FrozenCash;

	/// <summary>
	/// 冻结的手续费
	/// </summary>
	public double FrozenCommission;

	/// <summary>
	/// 资金差额
	/// </summary>
	public double CashIn;

	/// <summary>
	/// 手续费
	/// </summary>
	public double Commission;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;

	/// <summary>
	/// 上次结算价
	/// </summary>
	public double PreSettlementPrice;

	/// <summary>
	/// 本次结算价
	/// </summary>
	public double SettlementPrice;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 开仓成本
	/// </summary>
	public double OpenCost;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchangeMargin;

	/// <summary>
	/// 组合成交形成的持仓
	/// </summary>
	public int CombPosition;

	/// <summary>
	/// 组合多头冻结
	/// </summary>
	public int CombLongFrozen;

	/// <summary>
	/// 组合空头冻结
	/// </summary>
	public int CombShortFrozen;

	/// <summary>
	/// 逐日盯市平仓盈亏
	/// </summary>
	public double CloseProfitByDate;

	/// <summary>
	/// 逐笔对冲平仓盈亏
	/// </summary>
	public double CloseProfitByTrade;

	/// <summary>
	/// 今日持仓
	/// </summary>
	public int TodayPosition;

	/// <summary>
	/// 保证金率
	/// </summary>
	public double MarginRateByMoney;

	/// <summary>
	/// 保证金率(按手数)
	/// </summary>
	public double MarginRateByVolume;

	/// <summary>
	/// 执行冻结
	/// </summary>
	public int StrikeFrozen;

	/// <summary>
	/// 执行冻结金额
	/// </summary>
	public double StrikeFrozenAmount;

	/// <summary>
	/// 放弃执行冻结
	/// </summary>
	public int AbandonFrozen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 执行冻结的昨仓
	/// </summary>
	public int YdStrikeFrozen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 大商所持仓成本差值，只有大商所使用
	/// </summary>
	public double PositionCostOffset;
}

/// <summary>
/// 正在同步中的合约保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInstrumentMarginRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;

	/// <summary>
	/// 是否相对交易所收取
	/// </summary>
	public int IsRelative;
}

/// <summary>
/// 正在同步中的合约手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInstrumentCommissionRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 开仓手续费率
	/// </summary>
	public double OpenRatioByMoney;

	/// <summary>
	/// 开仓手续费
	/// </summary>
	public double OpenRatioByVolume;

	/// <summary>
	/// 平仓手续费率
	/// </summary>
	public double CloseRatioByMoney;

	/// <summary>
	/// 平仓手续费
	/// </summary>
	public double CloseRatioByVolume;

	/// <summary>
	/// 平今手续费率
	/// </summary>
	public double CloseTodayRatioByMoney;

	/// <summary>
	/// 平今手续费
	/// </summary>
	public double CloseTodayRatioByVolume;
}

/// <summary>
/// 正在同步中的合约交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncingInstrumentTradingRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 交易权限
	/// </summary>
	public TThostFtdcTradingRightType TradingRight;
}

/// <summary>
/// 查询报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询成交
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTradeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TradeID;

	/// <summary>
	/// 成交编号
	/// </summary>
	public string TradeID
	{
		get { return StringExtend.GetString(_TradeID); }
		set { _TradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string TradeTimeStart
	{
		get { return StringExtend.GetString(_TradeTimeStart); }
		set { _TradeTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string TradeTimeEnd
	{
		get { return StringExtend.GetString(_TradeTimeEnd); }
		set { _TradeTimeEnd = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询投资者持仓
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorPositionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询资金账户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTradingAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 业务类型
	/// </summary>
	public TThostFtdcBizTypeType BizType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询投资者
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询交易编码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTradingCodeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 交易编码类型
	/// </summary>
	public TThostFtdcClientIDTypeType ClientIDType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询投资者组
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorGroupField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 查询合约保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentMarginRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentCommissionRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询合约交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentTradingRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 查询经纪公司
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 查询交易员
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTraderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询管理用户功能权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySuperUserFunctionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询用户会话
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryUserSessionField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询经纪公司会员代码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryPartBrokerField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 查询前置状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryFrontStatusField
{

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;
}

/// <summary>
/// 查询交易所报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询交易所报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询管理用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySuperUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询交易所
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询产品
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryProductField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 产品类型
	/// </summary>
	public TThostFtdcProductClassType ProductClass;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询合约
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 查询行情
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryDepthMarketDataField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询经纪公司用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询经纪公司用户权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerUserFunctionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询交易员报盘机
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTraderOfferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询出入金流水
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySyncDepositField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _DepositSeqNo;

	/// <summary>
	/// 出入金流水号
	/// </summary>
	public string DepositSeqNo
	{
		get { return StringExtend.GetString(_DepositSeqNo); }
		set { _DepositSeqNo = StringExtend.GetBytes(value, 15); }
	}
}

/// <summary>
/// 查询投资者结算结果
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySettlementInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询交易所保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeMarginRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询交易所调整保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeMarginRateAdjustField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;
}

/// <summary>
/// 查询汇率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _FromCurrencyID;

	/// <summary>
	/// 源币种
	/// </summary>
	public string FromCurrencyID
	{
		get { return StringExtend.GetString(_FromCurrencyID); }
		set { _FromCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _ToCurrencyID;

	/// <summary>
	/// 目标币种
	/// </summary>
	public string ToCurrencyID
	{
		get { return StringExtend.GetString(_ToCurrencyID); }
		set { _ToCurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询货币质押流水
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySyncFundMortgageField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _MortgageSeqNo;

	/// <summary>
	/// 货币质押流水号
	/// </summary>
	public string MortgageSeqNo
	{
		get { return StringExtend.GetString(_MortgageSeqNo); }
		set { _MortgageSeqNo = StringExtend.GetBytes(value, 15); }
	}
}

/// <summary>
/// 查询报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryHisOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;
}

/// <summary>
/// 当前期权合约最小保证金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrMiniMarginField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 单位（手）期权合约最小保证金
	/// </summary>
	public double MinMargin;

	/// <summary>
	/// 取值方式
	/// </summary>
	public TThostFtdcValueMethodType ValueMethod;

	/// <summary>
	/// 是否跟随交易所收取
	/// </summary>
	public int IsRelative;
}

/// <summary>
/// 当前期权合约保证金调整系数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrMarginAdjustField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机空头保证金调整系数
	/// </summary>
	public double SShortMarginRatioByMoney;

	/// <summary>
	/// 投机空头保证金调整系数
	/// </summary>
	public double SShortMarginRatioByVolume;

	/// <summary>
	/// 保值空头保证金调整系数
	/// </summary>
	public double HShortMarginRatioByMoney;

	/// <summary>
	/// 保值空头保证金调整系数
	/// </summary>
	public double HShortMarginRatioByVolume;

	/// <summary>
	/// 套利空头保证金调整系数
	/// </summary>
	public double AShortMarginRatioByMoney;

	/// <summary>
	/// 套利空头保证金调整系数
	/// </summary>
	public double AShortMarginRatioByVolume;

	/// <summary>
	/// 是否跟随交易所收取
	/// </summary>
	public int IsRelative;

	/// <summary>
	/// 做市商空头保证金调整系数
	/// </summary>
	public double MShortMarginRatioByMoney;

	/// <summary>
	/// 做市商空头保证金调整系数
	/// </summary>
	public double MShortMarginRatioByVolume;
}

/// <summary>
/// 当前期权合约手续费的详细内容
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 开仓手续费率
	/// </summary>
	public double OpenRatioByMoney;

	/// <summary>
	/// 开仓手续费
	/// </summary>
	public double OpenRatioByVolume;

	/// <summary>
	/// 平仓手续费率
	/// </summary>
	public double CloseRatioByMoney;

	/// <summary>
	/// 平仓手续费
	/// </summary>
	public double CloseRatioByVolume;

	/// <summary>
	/// 平今手续费率
	/// </summary>
	public double CloseTodayRatioByMoney;

	/// <summary>
	/// 平今手续费
	/// </summary>
	public double CloseTodayRatioByVolume;

	/// <summary>
	/// 执行手续费率
	/// </summary>
	public double StrikeRatioByMoney;

	/// <summary>
	/// 执行手续费
	/// </summary>
	public double StrikeRatioByVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 期权交易成本
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrTradeCostField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 期权合约保证金不变部分
	/// </summary>
	public double FixedMargin;

	/// <summary>
	/// 期权合约最小保证金
	/// </summary>
	public double MiniMargin;

	/// <summary>
	/// 期权合约权利金
	/// </summary>
	public double Royalty;

	/// <summary>
	/// 交易所期权合约保证金不变部分
	/// </summary>
	public double ExchFixedMargin;

	/// <summary>
	/// 交易所期权合约最小保证金
	/// </summary>
	public double ExchMiniMargin;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 期权交易成本查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOptionInstrTradeCostField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 期权合约报价
	/// </summary>
	public double InputPrice;

	/// <summary>
	/// 标的价格,填0则用昨结算价
	/// </summary>
	public double UnderlyingPrice;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 期权手续费率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOptionInstrCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 股指现货指数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcIndexPriceField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 指数现货收盘价
	/// </summary>
	public double ClosePrice;
}

/// <summary>
/// 输入的执行宣告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	/// <summary>
	/// 保留头寸申请的持仓方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 期权行权后是否保留期货头寸的标记,该字段已废弃
	/// </summary>
	public TThostFtdcExecOrderPositionFlagType ReservePositionFlag;

	/// <summary>
	/// 期权行权后生成的头寸是否自动平仓
	/// </summary>
	public TThostFtdcExecOrderCloseFlagType CloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 输入执行宣告操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 执行宣告操作引用
	/// </summary>
	public int ExecOrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告操作编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 执行宣告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	/// <summary>
	/// 保留头寸申请的持仓方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 期权行权后是否保留期货头寸的标记,该字段已废弃
	/// </summary>
	public TThostFtdcExecOrderPositionFlagType ReservePositionFlag;

	/// <summary>
	/// 期权行权后生成的头寸是否自动平仓
	/// </summary>
	public TThostFtdcExecOrderCloseFlagType CloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderLocalID;

	/// <summary>
	/// 本地执行宣告编号
	/// </summary>
	public string ExecOrderLocalID
	{
		get { return StringExtend.GetString(_ExecOrderLocalID); }
		set { _ExecOrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 执行宣告提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 执行结果
	/// </summary>
	public TThostFtdcExecResultType ExecResult;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司报单编号
	/// </summary>
	public int BrokerExecOrderSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 执行宣告操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 执行宣告操作引用
	/// </summary>
	public int ExecOrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告操作编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderLocalID;

	/// <summary>
	/// 本地执行宣告编号
	/// </summary>
	public string ExecOrderLocalID
	{
		get { return StringExtend.GetString(_ExecOrderLocalID); }
		set { _ExecOrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 执行宣告查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所执行宣告信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeExecOrderField
{

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	/// <summary>
	/// 保留头寸申请的持仓方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 期权行权后是否保留期货头寸的标记,该字段已废弃
	/// </summary>
	public TThostFtdcExecOrderPositionFlagType ReservePositionFlag;

	/// <summary>
	/// 期权行权后生成的头寸是否自动平仓
	/// </summary>
	public TThostFtdcExecOrderCloseFlagType CloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderLocalID;

	/// <summary>
	/// 本地执行宣告编号
	/// </summary>
	public string ExecOrderLocalID
	{
		get { return StringExtend.GetString(_ExecOrderLocalID); }
		set { _ExecOrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 执行宣告提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 执行结果
	/// </summary>
	public TThostFtdcExecResultType ExecResult;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所执行宣告查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 执行宣告操作查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所执行宣告操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告操作编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderLocalID;

	/// <summary>
	/// 本地执行宣告编号
	/// </summary>
	public string ExecOrderLocalID
	{
		get { return StringExtend.GetString(_ExecOrderLocalID); }
		set { _ExecOrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
}

/// <summary>
/// 交易所执行宣告操作查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 错误执行宣告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcErrExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 执行类型
	/// </summary>
	public TThostFtdcActionTypeType ActionType;

	/// <summary>
	/// 保留头寸申请的持仓方向
	/// </summary>
	public TThostFtdcPosiDirectionType PosiDirection;

	/// <summary>
	/// 期权行权后是否保留期货头寸的标记,该字段已废弃
	/// </summary>
	public TThostFtdcExecOrderPositionFlagType ReservePositionFlag;

	/// <summary>
	/// 期权行权后生成的头寸是否自动平仓
	/// </summary>
	public TThostFtdcExecOrderCloseFlagType CloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 查询错误执行宣告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryErrExecOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 错误执行宣告操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcErrExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 执行宣告操作引用
	/// </summary>
	public int ExecOrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ExecOrderRef;

	/// <summary>
	/// 执行宣告引用
	/// </summary>
	public string ExecOrderRef
	{
		get { return StringExtend.GetString(_ExecOrderRef); }
		set { _ExecOrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ExecOrderSysID;

	/// <summary>
	/// 执行宣告操作编号
	/// </summary>
	public string ExecOrderSysID
	{
		get { return StringExtend.GetString(_ExecOrderSysID); }
		set { _ExecOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 查询错误执行宣告操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryErrExecOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 投资者期权合约交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrTradingRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 交易权限
	/// </summary>
	public TThostFtdcTradingRightType TradingRight;
}

/// <summary>
/// 查询期权合约交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOptionInstrTradingRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;
}

/// <summary>
/// 输入的询价
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputForQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ForQuoteRef;

	/// <summary>
	/// 询价引用
	/// </summary>
	public string ForQuoteRef
	{
		get { return StringExtend.GetString(_ForQuoteRef); }
		set { _ForQuoteRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 询价
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcForQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ForQuoteRef;

	/// <summary>
	/// 询价引用
	/// </summary>
	public string ForQuoteRef
	{
		get { return StringExtend.GetString(_ForQuoteRef); }
		set { _ForQuoteRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ForQuoteLocalID;

	/// <summary>
	/// 本地询价编号
	/// </summary>
	public string ForQuoteLocalID
	{
		get { return StringExtend.GetString(_ForQuoteLocalID); }
		set { _ForQuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 询价状态
	/// </summary>
	public TThostFtdcForQuoteStatusType ForQuoteStatus;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司询价编号
	/// </summary>
	public int BrokerForQutoSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 询价查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryForQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 交易所询价信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeForQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ForQuoteLocalID;

	/// <summary>
	/// 本地询价编号
	/// </summary>
	public string ForQuoteLocalID
	{
		get { return StringExtend.GetString(_ForQuoteLocalID); }
		set { _ForQuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 询价状态
	/// </summary>
	public TThostFtdcForQuoteStatusType ForQuoteStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所询价查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeForQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 输入的报价
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteRef;

	/// <summary>
	/// 报价引用
	/// </summary>
	public string QuoteRef
	{
		get { return StringExtend.GetString(_QuoteRef); }
		set { _QuoteRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 卖价格
	/// </summary>
	public double AskPrice;

	/// <summary>
	/// 买价格
	/// </summary>
	public double BidPrice;

	/// <summary>
	/// 卖数量
	/// </summary>
	public int AskVolume;

	/// <summary>
	/// 买数量
	/// </summary>
	public int BidVolume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 卖开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType AskOffsetFlag;

	/// <summary>
	/// 买开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType BidOffsetFlag;

	/// <summary>
	/// 卖投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType AskHedgeFlag;

	/// <summary>
	/// 买投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType BidHedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AskOrderRef;

	/// <summary>
	/// 衍生卖报单引用
	/// </summary>
	public string AskOrderRef
	{
		get { return StringExtend.GetString(_AskOrderRef); }
		set { _AskOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BidOrderRef;

	/// <summary>
	/// 衍生买报单引用
	/// </summary>
	public string BidOrderRef
	{
		get { return StringExtend.GetString(_BidOrderRef); }
		set { _BidOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ForQuoteSysID;

	/// <summary>
	/// 应价编号
	/// </summary>
	public string ForQuoteSysID
	{
		get { return StringExtend.GetString(_ForQuoteSysID); }
		set { _ForQuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 输入报价操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputQuoteActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报价操作引用
	/// </summary>
	public int QuoteActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteRef;

	/// <summary>
	/// 报价引用
	/// </summary>
	public string QuoteRef
	{
		get { return StringExtend.GetString(_QuoteRef); }
		set { _QuoteRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价操作编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报价
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteRef;

	/// <summary>
	/// 报价引用
	/// </summary>
	public string QuoteRef
	{
		get { return StringExtend.GetString(_QuoteRef); }
		set { _QuoteRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 卖价格
	/// </summary>
	public double AskPrice;

	/// <summary>
	/// 买价格
	/// </summary>
	public double BidPrice;

	/// <summary>
	/// 卖数量
	/// </summary>
	public int AskVolume;

	/// <summary>
	/// 买数量
	/// </summary>
	public int BidVolume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 卖开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType AskOffsetFlag;

	/// <summary>
	/// 买开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType BidOffsetFlag;

	/// <summary>
	/// 卖投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType AskHedgeFlag;

	/// <summary>
	/// 买投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType BidHedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteLocalID;

	/// <summary>
	/// 本地报价编号
	/// </summary>
	public string QuoteLocalID
	{
		get { return StringExtend.GetString(_QuoteLocalID); }
		set { _QuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 报价提示序号
	/// </summary>
	public int NotifySequence;

	/// <summary>
	/// 报价提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 报价状态
	/// </summary>
	public TThostFtdcOrderStatusType QuoteStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _AskOrderSysID;

	/// <summary>
	/// 卖方报单编号
	/// </summary>
	public string AskOrderSysID
	{
		get { return StringExtend.GetString(_AskOrderSysID); }
		set { _AskOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BidOrderSysID;

	/// <summary>
	/// 买方报单编号
	/// </summary>
	public string BidOrderSysID
	{
		get { return StringExtend.GetString(_BidOrderSysID); }
		set { _BidOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司报价编号
	/// </summary>
	public int BrokerQuoteSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AskOrderRef;

	/// <summary>
	/// 衍生卖报单引用
	/// </summary>
	public string AskOrderRef
	{
		get { return StringExtend.GetString(_AskOrderRef); }
		set { _AskOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BidOrderRef;

	/// <summary>
	/// 衍生买报单引用
	/// </summary>
	public string BidOrderRef
	{
		get { return StringExtend.GetString(_BidOrderRef); }
		set { _BidOrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ForQuoteSysID;

	/// <summary>
	/// 应价编号
	/// </summary>
	public string ForQuoteSysID
	{
		get { return StringExtend.GetString(_ForQuoteSysID); }
		set { _ForQuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报价操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQuoteActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报价操作引用
	/// </summary>
	public int QuoteActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteRef;

	/// <summary>
	/// 报价引用
	/// </summary>
	public string QuoteRef
	{
		get { return StringExtend.GetString(_QuoteRef); }
		set { _QuoteRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价操作编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteLocalID;

	/// <summary>
	/// 本地报价编号
	/// </summary>
	public string QuoteLocalID
	{
		get { return StringExtend.GetString(_QuoteLocalID); }
		set { _QuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报价查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 交易所报价信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeQuoteField
{

	/// <summary>
	/// 卖价格
	/// </summary>
	public double AskPrice;

	/// <summary>
	/// 买价格
	/// </summary>
	public double BidPrice;

	/// <summary>
	/// 卖数量
	/// </summary>
	public int AskVolume;

	/// <summary>
	/// 买数量
	/// </summary>
	public int BidVolume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 卖开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType AskOffsetFlag;

	/// <summary>
	/// 买开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType BidOffsetFlag;

	/// <summary>
	/// 卖投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType AskHedgeFlag;

	/// <summary>
	/// 买投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType BidHedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteLocalID;

	/// <summary>
	/// 本地报价编号
	/// </summary>
	public string QuoteLocalID
	{
		get { return StringExtend.GetString(_QuoteLocalID); }
		set { _QuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 报价提示序号
	/// </summary>
	public int NotifySequence;

	/// <summary>
	/// 报价提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 报价状态
	/// </summary>
	public TThostFtdcOrderStatusType QuoteStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _AskOrderSysID;

	/// <summary>
	/// 卖方报单编号
	/// </summary>
	public string AskOrderSysID
	{
		get { return StringExtend.GetString(_AskOrderSysID); }
		set { _AskOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BidOrderSysID;

	/// <summary>
	/// 买方报单编号
	/// </summary>
	public string BidOrderSysID
	{
		get { return StringExtend.GetString(_BidOrderSysID); }
		set { _BidOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ForQuoteSysID;

	/// <summary>
	/// 应价编号
	/// </summary>
	public string ForQuoteSysID
	{
		get { return StringExtend.GetString(_ForQuoteSysID); }
		set { _ForQuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报价查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeQuoteField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 报价操作查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryQuoteActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所报价操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeQuoteActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _QuoteSysID;

	/// <summary>
	/// 报价操作编号
	/// </summary>
	public string QuoteSysID
	{
		get { return StringExtend.GetString(_QuoteSysID); }
		set { _QuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _QuoteLocalID;

	/// <summary>
	/// 本地报价编号
	/// </summary>
	public string QuoteLocalID
	{
		get { return StringExtend.GetString(_QuoteLocalID); }
		set { _QuoteLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所报价操作查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeQuoteActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 期权合约delta值
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionInstrDeltaField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// Delta值
	/// </summary>
	public double Delta;
}

/// <summary>
/// 发给做市商的询价请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcForQuoteRspField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ForQuoteSysID;

	/// <summary>
	/// 询价编号
	/// </summary>
	public string ForQuoteSysID
	{
		get { return StringExtend.GetString(_ForQuoteSysID); }
		set { _ForQuoteSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ForQuoteTime;

	/// <summary>
	/// 询价时间
	/// </summary>
	public string ForQuoteTime
	{
		get { return StringExtend.GetString(_ForQuoteTime); }
		set { _ForQuoteTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDay;

	/// <summary>
	/// 业务日期
	/// </summary>
	public string ActionDay
	{
		get { return StringExtend.GetString(_ActionDay); }
		set { _ActionDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 当前期权合约执行偏移值的详细内容
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcStrikeOffsetField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 执行偏移值
	/// </summary>
	public double Offset;

	/// <summary>
	/// 执行偏移类型
	/// </summary>
	public TThostFtdcStrikeOffsetTypeType OffsetType;
}

/// <summary>
/// 期权执行偏移值查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryStrikeOffsetField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 输入批量报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputBatchOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 批量报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBatchOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 交易所批量报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeBatchOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询批量报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBatchOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 组合合约安全系数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCombInstrumentGuardField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 
	/// </summary>
	public double GuarantRatio;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 组合合约安全系数查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCombInstrumentGuardField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 输入的申请组合
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputCombActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CombActionRef;

	/// <summary>
	/// 组合引用
	/// </summary>
	public string CombActionRef
	{
		get { return StringExtend.GetString(_CombActionRef); }
		set { _CombActionRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 组合指令方向
	/// </summary>
	public TThostFtdcCombDirectionType CombDirection;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 申请组合
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCombActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CombActionRef;

	/// <summary>
	/// 组合引用
	/// </summary>
	public string CombActionRef
	{
		get { return StringExtend.GetString(_CombActionRef); }
		set { _CombActionRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 组合指令方向
	/// </summary>
	public TThostFtdcCombDirectionType CombDirection;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 本地申请组合编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 组合状态
	/// </summary>
	public TThostFtdcOrderActionStatusType ActionStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ComTradeID;

	/// <summary>
	/// 组合编号
	/// </summary>
	public string ComTradeID
	{
		get { return StringExtend.GetString(_ComTradeID); }
		set { _ComTradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 申请组合查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCombActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 交易所申请组合信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeCombActionField
{

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 组合指令方向
	/// </summary>
	public TThostFtdcCombDirectionType CombDirection;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 本地申请组合编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 组合状态
	/// </summary>
	public TThostFtdcOrderActionStatusType ActionStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ComTradeID;

	/// <summary>
	/// 组合编号
	/// </summary>
	public string ComTradeID
	{
		get { return StringExtend.GetString(_ComTradeID); }
		set { _ComTradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所申请组合查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeCombActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 产品报价汇率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcProductExchRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _QuoteCurrencyID;

	/// <summary>
	/// 报价币种类型
	/// </summary>
	public string QuoteCurrencyID
	{
		get { return StringExtend.GetString(_QuoteCurrencyID); }
		set { _QuoteCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇率
	/// </summary>
	public double ExchangeRate;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 产品报价汇率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryProductExchRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 查询询价价差参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryForQuoteParamField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 询价价差参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcForQuoteParamField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;

	/// <summary>
	/// 价差
	/// </summary>
	public double PriceInterval;
}

/// <summary>
/// 当前做市商期权合约手续费的详细内容
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMMOptionInstrCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 开仓手续费率
	/// </summary>
	public double OpenRatioByMoney;

	/// <summary>
	/// 开仓手续费
	/// </summary>
	public double OpenRatioByVolume;

	/// <summary>
	/// 平仓手续费率
	/// </summary>
	public double CloseRatioByMoney;

	/// <summary>
	/// 平仓手续费
	/// </summary>
	public double CloseRatioByVolume;

	/// <summary>
	/// 平今手续费率
	/// </summary>
	public double CloseTodayRatioByMoney;

	/// <summary>
	/// 平今手续费
	/// </summary>
	public double CloseTodayRatioByVolume;

	/// <summary>
	/// 执行手续费率
	/// </summary>
	public double StrikeRatioByMoney;

	/// <summary>
	/// 执行手续费
	/// </summary>
	public double StrikeRatioByVolume;
}

/// <summary>
/// 做市商期权手续费率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryMMOptionInstrCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 做市商合约手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMMInstrumentCommissionRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 开仓手续费率
	/// </summary>
	public double OpenRatioByMoney;

	/// <summary>
	/// 开仓手续费
	/// </summary>
	public double OpenRatioByVolume;

	/// <summary>
	/// 平仓手续费率
	/// </summary>
	public double CloseRatioByMoney;

	/// <summary>
	/// 平仓手续费
	/// </summary>
	public double CloseRatioByVolume;

	/// <summary>
	/// 平今手续费率
	/// </summary>
	public double CloseTodayRatioByMoney;

	/// <summary>
	/// 平今手续费
	/// </summary>
	public double CloseTodayRatioByVolume;
}

/// <summary>
/// 查询做市商合约手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryMMInstrumentCommissionRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 当前报单手续费的详细内容
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentOrderCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 报单手续费
	/// </summary>
	public double OrderCommByVolume;

	/// <summary>
	/// 撤单手续费
	/// </summary>
	public double OrderActionCommByVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 报单手续费率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentOrderCommRateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 交易参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradeParamField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 参数代码
	/// </summary>
	public TThostFtdcTradeParamIDType TradeParamID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=256)]
	private byte[] _TradeParamValue;

	/// <summary>
	/// 参数代码值
	/// </summary>
	public string TradeParamValue
	{
		get { return StringExtend.GetString(_TradeParamValue); }
		set { _TradeParamValue = StringExtend.GetBytes(value, 256); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _Memo;

	/// <summary>
	/// 备注
	/// </summary>
	public string Memo
	{
		get { return StringExtend.GetString(_Memo); }
		set { _Memo = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 合约保证金率调整
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentMarginRateULField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 多头保证金率
	/// </summary>
	public double LongMarginRatioByMoney;

	/// <summary>
	/// 多头保证金费
	/// </summary>
	public double LongMarginRatioByVolume;

	/// <summary>
	/// 空头保证金率
	/// </summary>
	public double ShortMarginRatioByMoney;

	/// <summary>
	/// 空头保证金费
	/// </summary>
	public double ShortMarginRatioByVolume;
}

/// <summary>
/// 期货持仓限制参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcFutureLimitPosiParamField
{

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 当日投机开仓数量限制
	/// </summary>
	public int SpecOpenVolume;

	/// <summary>
	/// 当日套利开仓数量限制
	/// </summary>
	public int ArbiOpenVolume;

	/// <summary>
	/// 当日投机+套利开仓数量限制
	/// </summary>
	public int OpenVolume;
}

/// <summary>
/// 禁止登录IP
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLoginForbiddenIPField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// IP列表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcIPListField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 是否白名单
	/// </summary>
	public int IsWhite;
}

/// <summary>
/// 输入的期权自对冲
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputOptionSelfCloseField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseRef;

	/// <summary>
	/// 期权自对冲引用
	/// </summary>
	public string OptionSelfCloseRef
	{
		get { return StringExtend.GetString(_OptionSelfCloseRef); }
		set { _OptionSelfCloseRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 期权行权的头寸是否自对冲
	/// </summary>
	public TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 输入期权自对冲操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInputOptionSelfCloseActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 期权自对冲操作引用
	/// </summary>
	public int OptionSelfCloseActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseRef;

	/// <summary>
	/// 期权自对冲引用
	/// </summary>
	public string OptionSelfCloseRef
	{
		get { return StringExtend.GetString(_OptionSelfCloseRef); }
		set { _OptionSelfCloseRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲操作编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 期权自对冲
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionSelfCloseField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseRef;

	/// <summary>
	/// 期权自对冲引用
	/// </summary>
	public string OptionSelfCloseRef
	{
		get { return StringExtend.GetString(_OptionSelfCloseRef); }
		set { _OptionSelfCloseRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 期权行权的头寸是否自对冲
	/// </summary>
	public TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseLocalID;

	/// <summary>
	/// 本地期权自对冲编号
	/// </summary>
	public string OptionSelfCloseLocalID
	{
		get { return StringExtend.GetString(_OptionSelfCloseLocalID); }
		set { _OptionSelfCloseLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期权自对冲提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 自对冲结果
	/// </summary>
	public TThostFtdcExecResultType ExecResult;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司报单编号
	/// </summary>
	public int BrokerOptionSelfCloseSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 期权自对冲操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOptionSelfCloseActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 期权自对冲操作引用
	/// </summary>
	public int OptionSelfCloseActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseRef;

	/// <summary>
	/// 期权自对冲引用
	/// </summary>
	public string OptionSelfCloseRef
	{
		get { return StringExtend.GetString(_OptionSelfCloseRef); }
		set { _OptionSelfCloseRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲操作编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseLocalID;

	/// <summary>
	/// 本地期权自对冲编号
	/// </summary>
	public string OptionSelfCloseLocalID
	{
		get { return StringExtend.GetString(_OptionSelfCloseLocalID); }
		set { _OptionSelfCloseLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 期权自对冲查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOptionSelfCloseField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeStart;

	/// <summary>
	/// 开始时间
	/// </summary>
	public string InsertTimeStart
	{
		get { return StringExtend.GetString(_InsertTimeStart); }
		set { _InsertTimeStart = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTimeEnd;

	/// <summary>
	/// 结束时间
	/// </summary>
	public string InsertTimeEnd
	{
		get { return StringExtend.GetString(_InsertTimeEnd); }
		set { _InsertTimeEnd = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所期权自对冲信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOptionSelfCloseField
{

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 期权行权的头寸是否自对冲
	/// </summary>
	public TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseLocalID;

	/// <summary>
	/// 本地期权自对冲编号
	/// </summary>
	public string OptionSelfCloseLocalID
	{
		get { return StringExtend.GetString(_OptionSelfCloseLocalID); }
		set { _OptionSelfCloseLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期权自对冲提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 插入时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 自对冲结果
	/// </summary>
	public TThostFtdcExecResultType ExecResult;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 期权自对冲操作查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryOptionSelfCloseActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所期权自对冲操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeOptionSelfCloseActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OptionSelfCloseSysID;

	/// <summary>
	/// 期权自对冲操作编号
	/// </summary>
	public string OptionSelfCloseSysID
	{
		get { return StringExtend.GetString(_OptionSelfCloseSysID); }
		set { _OptionSelfCloseSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OptionSelfCloseLocalID;

	/// <summary>
	/// 本地期权自对冲编号
	/// </summary>
	public string OptionSelfCloseLocalID
	{
		get { return StringExtend.GetString(_OptionSelfCloseLocalID); }
		set { _OptionSelfCloseLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 期权行权的头寸是否自对冲
	/// </summary>
	public TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;
}

/// <summary>
/// 延时换汇同步
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncDelaySwapField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _DelaySwapSeqNo;

	/// <summary>
	/// 换汇流水号
	/// </summary>
	public string DelaySwapSeqNo
	{
		get { return StringExtend.GetString(_DelaySwapSeqNo); }
		set { _DelaySwapSeqNo = StringExtend.GetBytes(value, 15); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _FromCurrencyID;

	/// <summary>
	/// 源币种
	/// </summary>
	public string FromCurrencyID
	{
		get { return StringExtend.GetString(_FromCurrencyID); }
		set { _FromCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 源金额
	/// </summary>
	public double FromAmount;

	/// <summary>
	/// 源换汇冻结金额(可用冻结)
	/// </summary>
	public double FromFrozenSwap;

	/// <summary>
	/// 源剩余换汇额度(可提冻结)
	/// </summary>
	public double FromRemainSwap;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _ToCurrencyID;

	/// <summary>
	/// 目标币种
	/// </summary>
	public string ToCurrencyID
	{
		get { return StringExtend.GetString(_ToCurrencyID); }
		set { _ToCurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 目标金额
	/// </summary>
	public double ToAmount;
}

/// <summary>
/// 查询延时换汇同步
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySyncDelaySwapField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _DelaySwapSeqNo;

	/// <summary>
	/// 延时换汇流水号
	/// </summary>
	public string DelaySwapSeqNo
	{
		get { return StringExtend.GetString(_DelaySwapSeqNo); }
		set { _DelaySwapSeqNo = StringExtend.GetBytes(value, 15); }
	}
}

/// <summary>
/// 投资单元
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestUnitField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _InvestorUnitName;

	/// <summary>
	/// 投资者单元名称
	/// </summary>
	public string InvestorUnitName
	{
		get { return StringExtend.GetString(_InvestorUnitName); }
		set { _InvestorUnitName = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorGroupID;

	/// <summary>
	/// 投资者分组代码
	/// </summary>
	public string InvestorGroupID
	{
		get { return StringExtend.GetString(_InvestorGroupID); }
		set { _InvestorGroupID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CommModelID;

	/// <summary>
	/// 手续费率模板代码
	/// </summary>
	public string CommModelID
	{
		get { return StringExtend.GetString(_CommModelID); }
		set { _CommModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MarginModelID;

	/// <summary>
	/// 保证金率模板代码
	/// </summary>
	public string MarginModelID
	{
		get { return StringExtend.GetString(_MarginModelID); }
		set { _MarginModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询投资单元
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestUnitField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 二级代理商资金校验模式
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSecAgentCheckModeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BrokerSecAgentID;

	/// <summary>
	/// 境外中介机构资金帐号
	/// </summary>
	public string BrokerSecAgentID
	{
		get { return StringExtend.GetString(_BrokerSecAgentID); }
		set { _BrokerSecAgentID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 是否需要校验自己的资金账户
	/// </summary>
	public int CheckSelfAccount;
}

/// <summary>
/// 二级代理商信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSecAgentTradeInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BrokerSecAgentID;

	/// <summary>
	/// 境外中介机构资金帐号
	/// </summary>
	public string BrokerSecAgentID
	{
		get { return StringExtend.GetString(_BrokerSecAgentID); }
		set { _BrokerSecAgentID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 二级代理商姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 市场行情
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;

	/// <summary>
	/// 上次结算价
	/// </summary>
	public double PreSettlementPrice;

	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;

	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;

	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;

	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;

	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;

	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;

	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;

	/// <summary>
	/// 本次结算价
	/// </summary>
	public double SettlementPrice;

	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;

	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;

	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;

	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDay;

	/// <summary>
	/// 业务日期
	/// </summary>
	public string ActionDay
	{
		get { return StringExtend.GetString(_ActionDay); }
		set { _ActionDay = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 行情基础属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataBaseField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 上次结算价
	/// </summary>
	public double PreSettlementPrice;

	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;

	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;

	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;
}

/// <summary>
/// 行情静态属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataStaticField
{

	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;

	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;

	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;

	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;

	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;

	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;

	/// <summary>
	/// 本次结算价
	/// </summary>
	public double SettlementPrice;

	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;
}

/// <summary>
/// 行情最新成交属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataLastMatchField
{

	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;

	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;
}

/// <summary>
/// 行情最优价属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataBestPriceField
{

	/// <summary>
	/// 申买价一
	/// </summary>
	public double BidPrice1;

	/// <summary>
	/// 申买量一
	/// </summary>
	public int BidVolume1;

	/// <summary>
	/// 申卖价一
	/// </summary>
	public double AskPrice1;

	/// <summary>
	/// 申卖量一
	/// </summary>
	public int AskVolume1;
}

/// <summary>
/// 行情申买二、三属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataBid23Field
{

	/// <summary>
	/// 申买价二
	/// </summary>
	public double BidPrice2;

	/// <summary>
	/// 申买量二
	/// </summary>
	public int BidVolume2;

	/// <summary>
	/// 申买价三
	/// </summary>
	public double BidPrice3;

	/// <summary>
	/// 申买量三
	/// </summary>
	public int BidVolume3;
}

/// <summary>
/// 行情申卖二、三属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataAsk23Field
{

	/// <summary>
	/// 申卖价二
	/// </summary>
	public double AskPrice2;

	/// <summary>
	/// 申卖量二
	/// </summary>
	public int AskVolume2;

	/// <summary>
	/// 申卖价三
	/// </summary>
	public double AskPrice3;

	/// <summary>
	/// 申卖量三
	/// </summary>
	public int AskVolume3;
}

/// <summary>
/// 行情申买四、五属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataBid45Field
{

	/// <summary>
	/// 申买价四
	/// </summary>
	public double BidPrice4;

	/// <summary>
	/// 申买量四
	/// </summary>
	public int BidVolume4;

	/// <summary>
	/// 申买价五
	/// </summary>
	public double BidPrice5;

	/// <summary>
	/// 申买量五
	/// </summary>
	public int BidVolume5;
}

/// <summary>
/// 行情申卖四、五属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataAsk45Field
{

	/// <summary>
	/// 申卖价四
	/// </summary>
	public double AskPrice4;

	/// <summary>
	/// 申卖量四
	/// </summary>
	public int AskVolume4;

	/// <summary>
	/// 申卖价五
	/// </summary>
	public double AskPrice5;

	/// <summary>
	/// 申卖量五
	/// </summary>
	public int AskVolume5;
}

/// <summary>
/// 行情更新时间属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataUpdateTimeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDay;

	/// <summary>
	/// 业务日期
	/// </summary>
	public string ActionDay
	{
		get { return StringExtend.GetString(_ActionDay); }
		set { _ActionDay = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 行情交易所代码属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataExchangeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 指定的合约
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSpecificInstrumentField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 合约状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInstrumentStatusField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SettlementGroupID;

	/// <summary>
	/// 结算组代码
	/// </summary>
	public string SettlementGroupID
	{
		get { return StringExtend.GetString(_SettlementGroupID); }
		set { _SettlementGroupID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 合约交易状态
	/// </summary>
	public TThostFtdcInstrumentStatusType InstrumentStatus;

	/// <summary>
	/// 交易阶段编号
	/// </summary>
	public int TradingSegmentSN;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _EnterTime;

	/// <summary>
	/// 进入本状态时间
	/// </summary>
	public string EnterTime
	{
		get { return StringExtend.GetString(_EnterTime); }
		set { _EnterTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 进入本状态原因
	/// </summary>
	public TThostFtdcInstStatusEnterReasonType EnterReason;
}

/// <summary>
/// 查询合约状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInstrumentStatusField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 投资者账户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 浮动盈亏算法
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcPositionProfitAlgorithmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 盈亏算法
	/// </summary>
	public TThostFtdcAlgorithmType Algorithm;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _Memo;

	/// <summary>
	/// 备注
	/// </summary>
	public string Memo
	{
		get { return StringExtend.GetString(_Memo); }
		set { _Memo = StringExtend.GetBytes(value, 161); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 会员资金折扣
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDiscountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 资金折扣比例
	/// </summary>
	public double Discount;
}

/// <summary>
/// 查询转帐银行
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTransferBankField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}
}

/// <summary>
/// 转帐银行
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferBankField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _BankName;

	/// <summary>
	/// 银行名称
	/// </summary>
	public string BankName
	{
		get { return StringExtend.GetString(_BankName); }
		set { _BankName = StringExtend.GetBytes(value, 101); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;
}

/// <summary>
/// 查询投资者持仓明细
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorPositionDetailField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 投资者持仓明细
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorPositionDetailField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 买卖
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 开仓日期
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TradeID;

	/// <summary>
	/// 成交编号
	/// </summary>
	public string TradeID
	{
		get { return StringExtend.GetString(_TradeID); }
		set { _TradeID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	/// <summary>
	/// 开仓价
	/// </summary>
	public double OpenPrice;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 成交类型
	/// </summary>
	public TThostFtdcTradeTypeType TradeType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CombInstrumentID;

	/// <summary>
	/// 组合合约代码
	/// </summary>
	public string CombInstrumentID
	{
		get { return StringExtend.GetString(_CombInstrumentID); }
		set { _CombInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 逐日盯市平仓盈亏
	/// </summary>
	public double CloseProfitByDate;

	/// <summary>
	/// 逐笔对冲平仓盈亏
	/// </summary>
	public double CloseProfitByTrade;

	/// <summary>
	/// 逐日盯市持仓盈亏
	/// </summary>
	public double PositionProfitByDate;

	/// <summary>
	/// 逐笔对冲持仓盈亏
	/// </summary>
	public double PositionProfitByTrade;

	/// <summary>
	/// 投资者保证金
	/// </summary>
	public double Margin;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchMargin;

	/// <summary>
	/// 保证金率
	/// </summary>
	public double MarginRateByMoney;

	/// <summary>
	/// 保证金率(按手数)
	/// </summary>
	public double MarginRateByVolume;

	/// <summary>
	/// 昨结算价
	/// </summary>
	public double LastSettlementPrice;

	/// <summary>
	/// 结算价
	/// </summary>
	public double SettlementPrice;

	/// <summary>
	/// 平仓量
	/// </summary>
	public int CloseVolume;

	/// <summary>
	/// 平仓金额
	/// </summary>
	public double CloseAmount;

	/// <summary>
	/// 按照时间顺序平仓的笔数,大商所专用
	/// </summary>
	public int TimeFirstVolume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 资金账户口令域
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingAccountPasswordField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 交易所行情报盘机
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMDTraderOfferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 交易所交易员连接状态
	/// </summary>
	public TThostFtdcTraderConnectStatusType TraderConnectStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectRequestDate;

	/// <summary>
	/// 发出连接请求的日期
	/// </summary>
	public string ConnectRequestDate
	{
		get { return StringExtend.GetString(_ConnectRequestDate); }
		set { _ConnectRequestDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectRequestTime;

	/// <summary>
	/// 发出连接请求的时间
	/// </summary>
	public string ConnectRequestTime
	{
		get { return StringExtend.GetString(_ConnectRequestTime); }
		set { _ConnectRequestTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportDate;

	/// <summary>
	/// 上次报告日期
	/// </summary>
	public string LastReportDate
	{
		get { return StringExtend.GetString(_LastReportDate); }
		set { _LastReportDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _LastReportTime;

	/// <summary>
	/// 上次报告时间
	/// </summary>
	public string LastReportTime
	{
		get { return StringExtend.GetString(_LastReportTime); }
		set { _LastReportTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectDate;

	/// <summary>
	/// 完成连接日期
	/// </summary>
	public string ConnectDate
	{
		get { return StringExtend.GetString(_ConnectDate); }
		set { _ConnectDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ConnectTime;

	/// <summary>
	/// 完成连接时间
	/// </summary>
	public string ConnectTime
	{
		get { return StringExtend.GetString(_ConnectTime); }
		set { _ConnectTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _StartDate;

	/// <summary>
	/// 启动日期
	/// </summary>
	public string StartDate
	{
		get { return StringExtend.GetString(_StartDate); }
		set { _StartDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _StartTime;

	/// <summary>
	/// 启动时间
	/// </summary>
	public string StartTime
	{
		get { return StringExtend.GetString(_StartTime); }
		set { _StartTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MaxTradeID;

	/// <summary>
	/// 本席位最大成交编号
	/// </summary>
	public string MaxTradeID
	{
		get { return StringExtend.GetString(_MaxTradeID); }
		set { _MaxTradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _MaxOrderMessageReference;

	/// <summary>
	/// 本席位最大报单备拷
	/// </summary>
	public string MaxOrderMessageReference
	{
		get { return StringExtend.GetString(_MaxOrderMessageReference); }
		set { _MaxOrderMessageReference = StringExtend.GetBytes(value, 7); }
	}
}

/// <summary>
/// 查询行情报盘机
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryMDTraderOfferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询客户通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryNoticeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 客户通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcNoticeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=501)]
	private byte[] _Content;

	/// <summary>
	/// 消息正文
	/// </summary>
	public string Content
	{
		get { return StringExtend.GetString(_Content); }
		set { _Content = StringExtend.GetBytes(value, 501); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=2)]
	private byte[] _SequenceLabel;

	/// <summary>
	/// 经纪公司通知内容序列号
	/// </summary>
	public string SequenceLabel
	{
		get { return StringExtend.GetString(_SequenceLabel); }
		set { _SequenceLabel = StringExtend.GetBytes(value, 2); }
	}
}

/// <summary>
/// 用户权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserRightField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 客户权限类型
	/// </summary>
	public TThostFtdcUserRightTypeType UserRightType;

	/// <summary>
	/// 是否禁止
	/// </summary>
	public int IsForbidden;
}

/// <summary>
/// 查询结算信息确认域
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySettlementInfoConfirmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 装载结算信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLoadSettlementInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 经纪公司可提资金算法表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerWithdrawAlgorithmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 可提资金算法
	/// </summary>
	public TThostFtdcAlgorithmType WithdrawAlgorithm;

	/// <summary>
	/// 资金使用率
	/// </summary>
	public double UsingRatio;

	/// <summary>
	/// 可提是否包含平仓盈利
	/// </summary>
	public TThostFtdcIncludeCloseProfitType IncludeCloseProfit;

	/// <summary>
	/// 本日无仓且无成交客户是否受可提比例限制
	/// </summary>
	public TThostFtdcAllWithoutTradeType AllWithoutTrade;

	/// <summary>
	/// 可用是否包含平仓盈利
	/// </summary>
	public TThostFtdcIncludeCloseProfitType AvailIncludeCloseProfit;

	/// <summary>
	/// 是否启用用户事件
	/// </summary>
	public int IsBrokerUserEvent;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 货币质押比率
	/// </summary>
	public double FundMortgageRatio;

	/// <summary>
	/// 权益算法
	/// </summary>
	public TThostFtdcBalanceAlgorithmType BalanceAlgorithm;
}

/// <summary>
/// 资金账户口令变更域
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingAccountPasswordUpdateV1Field
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OldPassword;

	/// <summary>
	/// 原来的口令
	/// </summary>
	public string OldPassword
	{
		get { return StringExtend.GetString(_OldPassword); }
		set { _OldPassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewPassword;

	/// <summary>
	/// 新的口令
	/// </summary>
	public string NewPassword
	{
		get { return StringExtend.GetString(_NewPassword); }
		set { _NewPassword = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 资金账户口令变更域
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingAccountPasswordUpdateField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OldPassword;

	/// <summary>
	/// 原来的口令
	/// </summary>
	public string OldPassword
	{
		get { return StringExtend.GetString(_OldPassword); }
		set { _OldPassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewPassword;

	/// <summary>
	/// 新的口令
	/// </summary>
	public string NewPassword
	{
		get { return StringExtend.GetString(_NewPassword); }
		set { _NewPassword = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询组合合约分腿
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCombinationLegField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CombInstrumentID;

	/// <summary>
	/// 组合合约代码
	/// </summary>
	public string CombInstrumentID
	{
		get { return StringExtend.GetString(_CombInstrumentID); }
		set { _CombInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 单腿编号
	/// </summary>
	public int LegID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _LegInstrumentID;

	/// <summary>
	/// 单腿合约代码
	/// </summary>
	public string LegInstrumentID
	{
		get { return StringExtend.GetString(_LegInstrumentID); }
		set { _LegInstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 查询组合合约分腿
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySyncStatusField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 组合交易合约的单腿
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCombinationLegField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CombInstrumentID;

	/// <summary>
	/// 组合合约代码
	/// </summary>
	public string CombInstrumentID
	{
		get { return StringExtend.GetString(_CombInstrumentID); }
		set { _CombInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 单腿编号
	/// </summary>
	public int LegID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _LegInstrumentID;

	/// <summary>
	/// 单腿合约代码
	/// </summary>
	public string LegInstrumentID
	{
		get { return StringExtend.GetString(_LegInstrumentID); }
		set { _LegInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 单腿乘数
	/// </summary>
	public int LegMultiple;

	/// <summary>
	/// 派生层数
	/// </summary>
	public int ImplyLevel;
}

/// <summary>
/// 数据同步状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSyncStatusField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 数据同步状态
	/// </summary>
	public TThostFtdcDataSyncStatusType DataSyncStatus;
}

/// <summary>
/// 查询联系人
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryLinkManField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 联系人
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLinkManField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 联系人类型
	/// </summary>
	public TThostFtdcPersonTypeType PersonType;

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdentifiedCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _PersonName;

	/// <summary>
	/// 名称
	/// </summary>
	public string PersonName
	{
		get { return StringExtend.GetString(_PersonName); }
		set { _PersonName = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 联系电话
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 通讯地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮政编码
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	/// <summary>
	/// 优先级
	/// </summary>
	public int Priority;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UOAZipCode;

	/// <summary>
	/// 开户邮政编码
	/// </summary>
	public string UOAZipCode
	{
		get { return StringExtend.GetString(_UOAZipCode); }
		set { _UOAZipCode = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _PersonFullName;

	/// <summary>
	/// 全称
	/// </summary>
	public string PersonFullName
	{
		get { return StringExtend.GetString(_PersonFullName); }
		set { _PersonFullName = StringExtend.GetBytes(value, 101); }
	}
}

/// <summary>
/// 查询经纪公司用户事件
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerUserEventField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 用户事件类型
	/// </summary>
	public TThostFtdcUserEventTypeType UserEventType;
}

/// <summary>
/// 查询经纪公司用户事件
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserEventField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 用户事件类型
	/// </summary>
	public TThostFtdcUserEventTypeType UserEventType;

	/// <summary>
	/// 用户事件序号
	/// </summary>
	public int EventSequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _EventDate;

	/// <summary>
	/// 事件发生日期
	/// </summary>
	public string EventDate
	{
		get { return StringExtend.GetString(_EventDate); }
		set { _EventDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _EventTime;

	/// <summary>
	/// 事件发生时间
	/// </summary>
	public string EventTime
	{
		get { return StringExtend.GetString(_EventTime); }
		set { _EventTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=1025)]
	private byte[] _UserEventInfo;

	/// <summary>
	/// 用户事件信息
	/// </summary>
	public string UserEventInfo
	{
		get { return StringExtend.GetString(_UserEventInfo); }
		set { _UserEventInfo = StringExtend.GetBytes(value, 1025); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 查询签约银行请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryContractBankField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}
}

/// <summary>
/// 查询签约银行响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcContractBankField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBrchID;

	/// <summary>
	/// 银行分中心代码
	/// </summary>
	public string BankBrchID
	{
		get { return StringExtend.GetString(_BankBrchID); }
		set { _BankBrchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _BankName;

	/// <summary>
	/// 银行名称
	/// </summary>
	public string BankName
	{
		get { return StringExtend.GetString(_BankName); }
		set { _BankName = StringExtend.GetBytes(value, 101); }
	}
}

/// <summary>
/// 投资者组合持仓明细
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorPositionCombineDetailField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 开仓日期
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ComTradeID;

	/// <summary>
	/// 组合编号
	/// </summary>
	public string ComTradeID
	{
		get { return StringExtend.GetString(_ComTradeID); }
		set { _ComTradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TradeID;

	/// <summary>
	/// 撮合编号
	/// </summary>
	public string TradeID
	{
		get { return StringExtend.GetString(_TradeID); }
		set { _TradeID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 买卖
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 持仓量
	/// </summary>
	public int TotalAmt;

	/// <summary>
	/// 投资者保证金
	/// </summary>
	public double Margin;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchMargin;

	/// <summary>
	/// 保证金率
	/// </summary>
	public double MarginRateByMoney;

	/// <summary>
	/// 保证金率(按手数)
	/// </summary>
	public double MarginRateByVolume;

	/// <summary>
	/// 单腿编号
	/// </summary>
	public int LegID;

	/// <summary>
	/// 单腿乘数
	/// </summary>
	public int LegMultiple;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CombInstrumentID;

	/// <summary>
	/// 组合持仓合约编码
	/// </summary>
	public string CombInstrumentID
	{
		get { return StringExtend.GetString(_CombInstrumentID); }
		set { _CombInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 成交组号
	/// </summary>
	public int TradeGroupID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 预埋单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcParkedOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 用户强评标志
	/// </summary>
	public int UserForceClose;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ParkedOrderID;

	/// <summary>
	/// 预埋报单编号
	/// </summary>
	public string ParkedOrderID
	{
		get { return StringExtend.GetString(_ParkedOrderID); }
		set { _ParkedOrderID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 用户类型
	/// </summary>
	public TThostFtdcUserTypeType UserType;

	/// <summary>
	/// 预埋单状态
	/// </summary>
	public TThostFtdcParkedOrderStatusType Status;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 互换单标志
	/// </summary>
	public int IsSwapOrder;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 输入预埋单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcParkedOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ParkedOrderActionID;

	/// <summary>
	/// 预埋撤单单编号
	/// </summary>
	public string ParkedOrderActionID
	{
		get { return StringExtend.GetString(_ParkedOrderActionID); }
		set { _ParkedOrderActionID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 用户类型
	/// </summary>
	public TThostFtdcUserTypeType UserType;

	/// <summary>
	/// 预埋撤单状态
	/// </summary>
	public TThostFtdcParkedOrderStatusType Status;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询预埋单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryParkedOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询预埋撤单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryParkedOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 删除预埋单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRemoveParkedOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ParkedOrderID;

	/// <summary>
	/// 预埋报单编号
	/// </summary>
	public string ParkedOrderID
	{
		get { return StringExtend.GetString(_ParkedOrderID); }
		set { _ParkedOrderID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 删除预埋撤单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRemoveParkedOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ParkedOrderActionID;

	/// <summary>
	/// 预埋撤单编号
	/// </summary>
	public string ParkedOrderActionID
	{
		get { return StringExtend.GetString(_ParkedOrderActionID); }
		set { _ParkedOrderActionID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 经纪公司可提资金算法表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorWithdrawAlgorithmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 可提资金比例
	/// </summary>
	public double UsingRatio;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 货币质押比率
	/// </summary>
	public double FundMortgageRatio;
}

/// <summary>
/// 查询组合持仓明细
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorPositionCombineDetailField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CombInstrumentID;

	/// <summary>
	/// 组合持仓合约编码
	/// </summary>
	public string CombInstrumentID
	{
		get { return StringExtend.GetString(_CombInstrumentID); }
		set { _CombInstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 成交均价
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarketDataAveragePriceField
{

	/// <summary>
	/// 当日均价
	/// </summary>
	public double AveragePrice;
}

/// <summary>
/// 校验投资者密码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcVerifyInvestorPasswordField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 用户IP
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserIPField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPMask;

	/// <summary>
	/// IP地址掩码
	/// </summary>
	public string IPMask
	{
		get { return StringExtend.GetString(_IPMask); }
		set { _IPMask = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 用户事件通知信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingNoticeInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SendTime;

	/// <summary>
	/// 发送时间
	/// </summary>
	public string SendTime
	{
		get { return StringExtend.GetString(_SendTime); }
		set { _SendTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=501)]
	private byte[] _FieldContent;

	/// <summary>
	/// 消息正文
	/// </summary>
	public string FieldContent
	{
		get { return StringExtend.GetString(_FieldContent); }
		set { _FieldContent = StringExtend.GetBytes(value, 501); }
	}

	/// <summary>
	/// 序列系列号
	/// </summary>
	public short SequenceSeries;

	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 用户事件通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingNoticeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcInvestorRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 序列系列号
	/// </summary>
	public short SequenceSeries;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SendTime;

	/// <summary>
	/// 发送时间
	/// </summary>
	public string SendTime
	{
		get { return StringExtend.GetString(_SendTime); }
		set { _SendTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=501)]
	private byte[] _FieldContent;

	/// <summary>
	/// 消息正文
	/// </summary>
	public string FieldContent
	{
		get { return StringExtend.GetString(_FieldContent); }
		set { _FieldContent = StringExtend.GetBytes(value, 501); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询交易事件通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTradingNoticeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询错误报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryErrOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 错误报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcErrOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 用户强评标志
	/// </summary>
	public int UserForceClose;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 互换单标志
	/// </summary>
	public int IsSwapOrder;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 交易编码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询错误报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcErrorConditionalOrderField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 报单价格条件
	/// </summary>
	public TThostFtdcOrderPriceTypeType OrderPriceType;

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombOffsetFlag;

	/// <summary>
	/// 组合开平标志
	/// </summary>
	public string CombOffsetFlag
	{
		get { return StringExtend.GetString(_CombOffsetFlag); }
		set { _CombOffsetFlag = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _CombHedgeFlag;

	/// <summary>
	/// 组合投机套保标志
	/// </summary>
	public string CombHedgeFlag
	{
		get { return StringExtend.GetString(_CombHedgeFlag); }
		set { _CombHedgeFlag = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量
	/// </summary>
	public int VolumeTotalOriginal;

	/// <summary>
	/// 有效期类型
	/// </summary>
	public TThostFtdcTimeConditionType TimeCondition;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _GTDDate;

	/// <summary>
	/// GTD日期
	/// </summary>
	public string GTDDate
	{
		get { return StringExtend.GetString(_GTDDate); }
		set { _GTDDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 成交量类型
	/// </summary>
	public TThostFtdcVolumeConditionType VolumeCondition;

	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;

	/// <summary>
	/// 触发条件
	/// </summary>
	public TThostFtdcContingentConditionType ContingentCondition;

	/// <summary>
	/// 止损价
	/// </summary>
	public double StopPrice;

	/// <summary>
	/// 强平原因
	/// </summary>
	public TThostFtdcForceCloseReasonType ForceCloseReason;

	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ExchangeInstID;

	/// <summary>
	/// 合约在交易所的代码
	/// </summary>
	public string ExchangeInstID
	{
		get { return StringExtend.GetString(_ExchangeInstID); }
		set { _ExchangeInstID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 报单提交状态
	/// </summary>
	public TThostFtdcOrderSubmitStatusType OrderSubmitStatus;

	/// <summary>
	/// 报单提示序号
	/// </summary>
	public int NotifySequence;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单来源
	/// </summary>
	public TThostFtdcOrderSourceType OrderSource;

	/// <summary>
	/// 报单状态
	/// </summary>
	public TThostFtdcOrderStatusType OrderStatus;

	/// <summary>
	/// 报单类型
	/// </summary>
	public TThostFtdcOrderTypeType OrderType;

	/// <summary>
	/// 今成交数量
	/// </summary>
	public int VolumeTraded;

	/// <summary>
	/// 剩余数量
	/// </summary>
	public int VolumeTotal;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertDate;

	/// <summary>
	/// 报单日期
	/// </summary>
	public string InsertDate
	{
		get { return StringExtend.GetString(_InsertDate); }
		set { _InsertDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _InsertTime;

	/// <summary>
	/// 委托时间
	/// </summary>
	public string InsertTime
	{
		get { return StringExtend.GetString(_InsertTime); }
		set { _InsertTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActiveTime;

	/// <summary>
	/// 激活时间
	/// </summary>
	public string ActiveTime
	{
		get { return StringExtend.GetString(_ActiveTime); }
		set { _ActiveTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SuspendTime;

	/// <summary>
	/// 挂起时间
	/// </summary>
	public string SuspendTime
	{
		get { return StringExtend.GetString(_SuspendTime); }
		set { _SuspendTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _UpdateTime;

	/// <summary>
	/// 最后修改时间
	/// </summary>
	public string UpdateTime
	{
		get { return StringExtend.GetString(_UpdateTime); }
		set { _UpdateTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelTime;

	/// <summary>
	/// 撤销时间
	/// </summary>
	public string CancelTime
	{
		get { return StringExtend.GetString(_CancelTime); }
		set { _CancelTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ActiveTraderID;

	/// <summary>
	/// 最后修改交易所交易员代码
	/// </summary>
	public string ActiveTraderID
	{
		get { return StringExtend.GetString(_ActiveTraderID); }
		set { _ActiveTraderID = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClearingPartID;

	/// <summary>
	/// 结算会员编号
	/// </summary>
	public string ClearingPartID
	{
		get { return StringExtend.GetString(_ClearingPartID); }
		set { _ClearingPartID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 用户强评标志
	/// </summary>
	public int UserForceClose;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ActiveUserID;

	/// <summary>
	/// 操作用户代码
	/// </summary>
	public string ActiveUserID
	{
		get { return StringExtend.GetString(_ActiveUserID); }
		set { _ActiveUserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 经纪公司报单编号
	/// </summary>
	public int BrokerOrderSeq;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _RelativeOrderSysID;

	/// <summary>
	/// 相关报单
	/// </summary>
	public string RelativeOrderSysID
	{
		get { return StringExtend.GetString(_RelativeOrderSysID); }
		set { _RelativeOrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 郑商所成交数量
	/// </summary>
	public int ZCETotalTradedVolume;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 互换单标志
	/// </summary>
	public int IsSwapOrder;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询错误报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryErrOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 错误报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcErrOrderActionField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 报单操作引用
	/// </summary>
	public int OrderActionRef;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderRef;

	/// <summary>
	/// 报单引用
	/// </summary>
	public string OrderRef
	{
		get { return StringExtend.GetString(_OrderRef); }
		set { _OrderRef = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 前置编号
	/// </summary>
	public int FrontID;

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _OrderSysID;

	/// <summary>
	/// 报单编号
	/// </summary>
	public string OrderSysID
	{
		get { return StringExtend.GetString(_OrderSysID); }
		set { _OrderSysID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 操作标志
	/// </summary>
	public TThostFtdcActionFlagType ActionFlag;

	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;

	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionDate;

	/// <summary>
	/// 操作日期
	/// </summary>
	public string ActionDate
	{
		get { return StringExtend.GetString(_ActionDate); }
		set { _ActionDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ActionTime;

	/// <summary>
	/// 操作时间
	/// </summary>
	public string ActionTime
	{
		get { return StringExtend.GetString(_ActionTime); }
		set { _ActionTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _TraderID;

	/// <summary>
	/// 交易所交易员代码
	/// </summary>
	public string TraderID
	{
		get { return StringExtend.GetString(_TraderID); }
		set { _TraderID = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _OrderLocalID;

	/// <summary>
	/// 本地报单编号
	/// </summary>
	public string OrderLocalID
	{
		get { return StringExtend.GetString(_OrderLocalID); }
		set { _OrderLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _ActionLocalID;

	/// <summary>
	/// 操作本地编号
	/// </summary>
	public string ActionLocalID
	{
		get { return StringExtend.GetString(_ActionLocalID); }
		set { _ActionLocalID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ClientID;

	/// <summary>
	/// 客户代码
	/// </summary>
	public string ClientID
	{
		get { return StringExtend.GetString(_ClientID); }
		set { _ClientID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _BusinessUnit;

	/// <summary>
	/// 业务单元
	/// </summary>
	public string BusinessUnit
	{
		get { return StringExtend.GetString(_BusinessUnit); }
		set { _BusinessUnit = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 报单操作状态
	/// </summary>
	public TThostFtdcOrderActionStatusType OrderActionStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _StatusMsg;

	/// <summary>
	/// 状态信息
	/// </summary>
	public string StatusMsg
	{
		get { return StringExtend.GetString(_StatusMsg); }
		set { _StatusMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BranchID;

	/// <summary>
	/// 营业部编号
	/// </summary>
	public string BranchID
	{
		get { return StringExtend.GetString(_BranchID); }
		set { _BranchID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 查询交易所状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryExchangeSequenceField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 交易所状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcExchangeSequenceField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 序号
	/// </summary>
	public int SequenceNo;

	/// <summary>
	/// 合约交易状态
	/// </summary>
	public TThostFtdcInstrumentStatusType MarketStatus;
}

/// <summary>
/// 根据价格查询最大报单数量
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQueryMaxOrderVolumeWithPriceField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 开平标志
	/// </summary>
	public TThostFtdcOffsetFlagType OffsetFlag;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 最大允许报单数量
	/// </summary>
	public int MaxVolume;

	/// <summary>
	/// 报单价格
	/// </summary>
	public double Price;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询经纪公司交易参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerTradingParamsField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 经纪公司交易参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerTradingParamsField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 保证金价格类型
	/// </summary>
	public TThostFtdcMarginPriceTypeType MarginPriceType;

	/// <summary>
	/// 盈亏算法
	/// </summary>
	public TThostFtdcAlgorithmType Algorithm;

	/// <summary>
	/// 可用是否包含平仓盈利
	/// </summary>
	public TThostFtdcIncludeCloseProfitType AvailIncludeCloseProfit;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 期权权利金价格类型
	/// </summary>
	public TThostFtdcOptionRoyaltyPriceTypeType OptionRoyaltyPriceType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询经纪公司交易算法
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBrokerTradingAlgosField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 经纪公司交易算法
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerTradingAlgosField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 持仓处理算法编号
	/// </summary>
	public TThostFtdcHandlePositionAlgoIDType HandlePositionAlgoID;

	/// <summary>
	/// 寻找保证金率算法编号
	/// </summary>
	public TThostFtdcFindMarginRateAlgoIDType FindMarginRateAlgoID;

	/// <summary>
	/// 资金处理算法编号
	/// </summary>
	public TThostFtdcHandleTradingAccountAlgoIDType HandleTradingAccountAlgoID;
}

/// <summary>
/// 查询经纪公司资金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQueryBrokerDepositField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 经纪公司资金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerDepositField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 会员代码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 上次结算准备金
	/// </summary>
	public double PreBalance;

	/// <summary>
	/// 当前保证金总额
	/// </summary>
	public double CurrMargin;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 期货结算准备金
	/// </summary>
	public double Balance;

	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;

	/// <summary>
	/// 出金金额
	/// </summary>
	public double Withdraw;

	/// <summary>
	/// 可提资金
	/// </summary>
	public double Available;

	/// <summary>
	/// 基本准备金
	/// </summary>
	public double Reserve;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;
}

/// <summary>
/// 查询保证金监管系统经纪公司密钥
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCFMMCBrokerKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// 保证金监管系统经纪公司密钥
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCFMMCBrokerKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 经纪公司统一编码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CreateDate;

	/// <summary>
	/// 密钥生成日期
	/// </summary>
	public string CreateDate
	{
		get { return StringExtend.GetString(_CreateDate); }
		set { _CreateDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CreateTime;

	/// <summary>
	/// 密钥生成时间
	/// </summary>
	public string CreateTime
	{
		get { return StringExtend.GetString(_CreateTime); }
		set { _CreateTime = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 密钥编号
	/// </summary>
	public int KeyID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CurrentKey;

	/// <summary>
	/// 动态密钥
	/// </summary>
	public string CurrentKey
	{
		get { return StringExtend.GetString(_CurrentKey); }
		set { _CurrentKey = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 动态密钥类型
	/// </summary>
	public TThostFtdcCFMMCKeyKindType KeyKind;
}

/// <summary>
/// 保证金监管系统经纪公司资金账户密钥
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCFMMCTradingAccountKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 经纪公司统一编码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 密钥编号
	/// </summary>
	public int KeyID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CurrentKey;

	/// <summary>
	/// 动态密钥
	/// </summary>
	public string CurrentKey
	{
		get { return StringExtend.GetString(_CurrentKey); }
		set { _CurrentKey = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 请求查询保证金监管系统经纪公司资金账户密钥
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCFMMCTradingAccountKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 用户动态令牌参数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserOTPParamField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=2)]
	private byte[] _OTPVendorsID;

	/// <summary>
	/// 动态令牌提供商
	/// </summary>
	public string OTPVendorsID
	{
		get { return StringExtend.GetString(_OTPVendorsID); }
		set { _OTPVendorsID = StringExtend.GetBytes(value, 2); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _SerialNumber;

	/// <summary>
	/// 动态令牌序列号
	/// </summary>
	public string SerialNumber
	{
		get { return StringExtend.GetString(_SerialNumber); }
		set { _SerialNumber = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _AuthKey;

	/// <summary>
	/// 令牌密钥
	/// </summary>
	public string AuthKey
	{
		get { return StringExtend.GetString(_AuthKey); }
		set { _AuthKey = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 漂移值
	/// </summary>
	public int LastDrift;

	/// <summary>
	/// 成功值
	/// </summary>
	public int LastSuccess;

	/// <summary>
	/// 动态令牌类型
	/// </summary>
	public TThostFtdcOTPTypeType OTPType;
}

/// <summary>
/// 手工同步用户动态令牌
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcManualSyncBrokerUserOTPField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 动态令牌类型
	/// </summary>
	public TThostFtdcOTPTypeType OTPType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _FirstOTP;

	/// <summary>
	/// 第一个动态密码
	/// </summary>
	public string FirstOTP
	{
		get { return StringExtend.GetString(_FirstOTP); }
		set { _FirstOTP = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _SecondOTP;

	/// <summary>
	/// 第二个动态密码
	/// </summary>
	public string SecondOTP
	{
		get { return StringExtend.GetString(_SecondOTP); }
		set { _SecondOTP = StringExtend.GetBytes(value, 41); }
	}
}

/// <summary>
/// 投资者手续费率模板
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCommRateModelField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CommModelID;

	/// <summary>
	/// 手续费率模板代码
	/// </summary>
	public string CommModelID
	{
		get { return StringExtend.GetString(_CommModelID); }
		set { _CommModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _CommModelName;

	/// <summary>
	/// 模板名称
	/// </summary>
	public string CommModelName
	{
		get { return StringExtend.GetString(_CommModelName); }
		set { _CommModelName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 请求查询投资者手续费率模板
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCommRateModelField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _CommModelID;

	/// <summary>
	/// 手续费率模板代码
	/// </summary>
	public string CommModelID
	{
		get { return StringExtend.GetString(_CommModelID); }
		set { _CommModelID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 投资者保证金率模板
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMarginModelField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MarginModelID;

	/// <summary>
	/// 保证金率模板代码
	/// </summary>
	public string MarginModelID
	{
		get { return StringExtend.GetString(_MarginModelID); }
		set { _MarginModelID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _MarginModelName;

	/// <summary>
	/// 模板名称
	/// </summary>
	public string MarginModelName
	{
		get { return StringExtend.GetString(_MarginModelName); }
		set { _MarginModelName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 请求查询投资者保证金率模板
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryMarginModelField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _MarginModelID;

	/// <summary>
	/// 保证金率模板代码
	/// </summary>
	public string MarginModelID
	{
		get { return StringExtend.GetString(_MarginModelID); }
		set { _MarginModelID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 仓单折抵信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcEWarrantOffsetField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 买卖方向
	/// </summary>
	public TThostFtdcDirectionType Direction;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询仓单折抵信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryEWarrantOffsetField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _InstrumentID;

	/// <summary>
	/// 合约代码
	/// </summary>
	public string InstrumentID
	{
		get { return StringExtend.GetString(_InstrumentID); }
		set { _InstrumentID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询投资者品种/跨品种保证金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryInvestorProductGroupMarginField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductGroupID;

	/// <summary>
	/// 品种/跨品种标示
	/// </summary>
	public string ProductGroupID
	{
		get { return StringExtend.GetString(_ProductGroupID); }
		set { _ProductGroupID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 投资者品种/跨品种保证金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcInvestorProductGroupMarginField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductGroupID;

	/// <summary>
	/// 品种/跨品种标示
	/// </summary>
	public string ProductGroupID
	{
		get { return StringExtend.GetString(_ProductGroupID); }
		set { _ProductGroupID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;

	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;

	/// <summary>
	/// 多头冻结的保证金
	/// </summary>
	public double LongFrozenMargin;

	/// <summary>
	/// 空头冻结的保证金
	/// </summary>
	public double ShortFrozenMargin;

	/// <summary>
	/// 占用的保证金
	/// </summary>
	public double UseMargin;

	/// <summary>
	/// 多头保证金
	/// </summary>
	public double LongUseMargin;

	/// <summary>
	/// 空头保证金
	/// </summary>
	public double ShortUseMargin;

	/// <summary>
	/// 交易所保证金
	/// </summary>
	public double ExchMargin;

	/// <summary>
	/// 交易所多头保证金
	/// </summary>
	public double LongExchMargin;

	/// <summary>
	/// 交易所空头保证金
	/// </summary>
	public double ShortExchMargin;

	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;

	/// <summary>
	/// 冻结的手续费
	/// </summary>
	public double FrozenCommission;

	/// <summary>
	/// 手续费
	/// </summary>
	public double Commission;

	/// <summary>
	/// 冻结的资金
	/// </summary>
	public double FrozenCash;

	/// <summary>
	/// 资金差额
	/// </summary>
	public double CashIn;

	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;

	/// <summary>
	/// 折抵总金额
	/// </summary>
	public double OffsetAmount;

	/// <summary>
	/// 多头折抵总金额
	/// </summary>
	public double LongOffsetAmount;

	/// <summary>
	/// 空头折抵总金额
	/// </summary>
	public double ShortOffsetAmount;

	/// <summary>
	/// 交易所折抵总金额
	/// </summary>
	public double ExchOffsetAmount;

	/// <summary>
	/// 交易所多头折抵总金额
	/// </summary>
	public double LongExchOffsetAmount;

	/// <summary>
	/// 交易所空头折抵总金额
	/// </summary>
	public double ShortExchOffsetAmount;

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TThostFtdcHedgeFlagType HedgeFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 查询监控中心用户令牌
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQueryCFMMCTradingAccountTokenField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _InvestUnitID;

	/// <summary>
	/// 投资单元代码
	/// </summary>
	public string InvestUnitID
	{
		get { return StringExtend.GetString(_InvestUnitID); }
		set { _InvestUnitID = StringExtend.GetBytes(value, 17); }
	}
}

/// <summary>
/// 监控中心用户令牌
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCFMMCTradingAccountTokenField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ParticipantID;

	/// <summary>
	/// 经纪公司统一编码
	/// </summary>
	public string ParticipantID
	{
		get { return StringExtend.GetString(_ParticipantID); }
		set { _ParticipantID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 密钥编号
	/// </summary>
	public int KeyID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _Token;

	/// <summary>
	/// 动态令牌
	/// </summary>
	public string Token
	{
		get { return StringExtend.GetString(_Token); }
		set { _Token = StringExtend.GetBytes(value, 21); }
	}
}

/// <summary>
/// 查询产品组
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryProductGroupField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}
}

/// <summary>
/// 投资者品种/跨品种保证金产品组
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcProductGroupField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductID;

	/// <summary>
	/// 产品代码
	/// </summary>
	public string ProductID
	{
		get { return StringExtend.GetString(_ProductID); }
		set { _ProductID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _ProductGroupID;

	/// <summary>
	/// 产品组代码
	/// </summary>
	public string ProductGroupID
	{
		get { return StringExtend.GetString(_ProductGroupID); }
		set { _ProductGroupID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 交易所公告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBulletinField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 公告编号
	/// </summary>
	public int BulletinID;

	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _NewsType;

	/// <summary>
	/// 公告类型
	/// </summary>
	public string NewsType
	{
		get { return StringExtend.GetString(_NewsType); }
		set { _NewsType = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 紧急程度
	/// </summary>
	public TThostFtdcNewsUrgencyType NewsUrgency;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _SendTime;

	/// <summary>
	/// 发送时间
	/// </summary>
	public string SendTime
	{
		get { return StringExtend.GetString(_SendTime); }
		set { _SendTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _Abstract;

	/// <summary>
	/// 消息摘要
	/// </summary>
	public string Abstract
	{
		get { return StringExtend.GetString(_Abstract); }
		set { _Abstract = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _ComeFrom;

	/// <summary>
	/// 消息来源
	/// </summary>
	public string ComeFrom
	{
		get { return StringExtend.GetString(_ComeFrom); }
		set { _ComeFrom = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=501)]
	private byte[] _Content;

	/// <summary>
	/// 消息正文
	/// </summary>
	public string Content
	{
		get { return StringExtend.GetString(_Content); }
		set { _Content = StringExtend.GetBytes(value, 501); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=201)]
	private byte[] _URLLink;

	/// <summary>
	/// WEB地址
	/// </summary>
	public string URLLink
	{
		get { return StringExtend.GetString(_URLLink); }
		set { _URLLink = StringExtend.GetBytes(value, 201); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _MarketID;

	/// <summary>
	/// 市场代码
	/// </summary>
	public string MarketID
	{
		get { return StringExtend.GetString(_MarketID); }
		set { _MarketID = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// 查询交易所公告
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryBulletinField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ExchangeID;

	/// <summary>
	/// 交易所代码
	/// </summary>
	public string ExchangeID
	{
		get { return StringExtend.GetString(_ExchangeID); }
		set { _ExchangeID = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 公告编号
	/// </summary>
	public int BulletinID;

	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _NewsType;

	/// <summary>
	/// 公告类型
	/// </summary>
	public string NewsType
	{
		get { return StringExtend.GetString(_NewsType); }
		set { _NewsType = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 紧急程度
	/// </summary>
	public TThostFtdcNewsUrgencyType NewsUrgency;
}

/// <summary>
/// 转帐开户请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqOpenAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇钞标志
	/// </summary>
	public TThostFtdcCashExchangeCodeType CashExchangeCode;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 转帐销户请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqCancelAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇钞标志
	/// </summary>
	public TThostFtdcCashExchangeCodeType CashExchangeCode;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 变更银行账户请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqChangeAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewBankAccount;

	/// <summary>
	/// 新银行帐号
	/// </summary>
	public string NewBankAccount
	{
		get { return StringExtend.GetString(_NewBankAccount); }
		set { _NewBankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewBankPassWord;

	/// <summary>
	/// 新银行密码
	/// </summary>
	public string NewBankPassWord
	{
		get { return StringExtend.GetString(_NewBankPassWord); }
		set { _NewBankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 转账请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqTransferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	/// <summary>
	/// 期货可取金额
	/// </summary>
	public double FutureFetchAmount;

	/// <summary>
	/// 费用支付标志
	/// </summary>
	public TThostFtdcFeePayFlagType FeePayFlag;

	/// <summary>
	/// 应收客户费用
	/// </summary>
	public double CustFee;

	/// <summary>
	/// 应收期货公司费用
	/// </summary>
	public double BrokerFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 发送方给接收方的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 转账交易状态
	/// </summary>
	public TThostFtdcTransferStatusType TransferStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 银行发起银行资金转期货响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspTransferField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	/// <summary>
	/// 期货可取金额
	/// </summary>
	public double FutureFetchAmount;

	/// <summary>
	/// 费用支付标志
	/// </summary>
	public TThostFtdcFeePayFlagType FeePayFlag;

	/// <summary>
	/// 应收客户费用
	/// </summary>
	public double CustFee;

	/// <summary>
	/// 应收期货公司费用
	/// </summary>
	public double BrokerFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 发送方给接收方的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 转账交易状态
	/// </summary>
	public TThostFtdcTransferStatusType TransferStatus;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 冲正请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqRepealField
{

	/// <summary>
	/// 冲正时间间隔
	/// </summary>
	public int RepealTimeInterval;

	/// <summary>
	/// 已经冲正次数
	/// </summary>
	public int RepealedTimes;

	/// <summary>
	/// 银行冲正标志
	/// </summary>
	public TThostFtdcBankRepealFlagType BankRepealFlag;

	/// <summary>
	/// 期商冲正标志
	/// </summary>
	public TThostFtdcBrokerRepealFlagType BrokerRepealFlag;

	/// <summary>
	/// 被冲正平台流水号
	/// </summary>
	public int PlateRepealSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankRepealSerial;

	/// <summary>
	/// 被冲正银行流水号
	/// </summary>
	public string BankRepealSerial
	{
		get { return StringExtend.GetString(_BankRepealSerial); }
		set { _BankRepealSerial = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 被冲正期货流水号
	/// </summary>
	public int FutureRepealSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	/// <summary>
	/// 期货可取金额
	/// </summary>
	public double FutureFetchAmount;

	/// <summary>
	/// 费用支付标志
	/// </summary>
	public TThostFtdcFeePayFlagType FeePayFlag;

	/// <summary>
	/// 应收客户费用
	/// </summary>
	public double CustFee;

	/// <summary>
	/// 应收期货公司费用
	/// </summary>
	public double BrokerFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 发送方给接收方的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 转账交易状态
	/// </summary>
	public TThostFtdcTransferStatusType TransferStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 冲正响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspRepealField
{

	/// <summary>
	/// 冲正时间间隔
	/// </summary>
	public int RepealTimeInterval;

	/// <summary>
	/// 已经冲正次数
	/// </summary>
	public int RepealedTimes;

	/// <summary>
	/// 银行冲正标志
	/// </summary>
	public TThostFtdcBankRepealFlagType BankRepealFlag;

	/// <summary>
	/// 期商冲正标志
	/// </summary>
	public TThostFtdcBrokerRepealFlagType BrokerRepealFlag;

	/// <summary>
	/// 被冲正平台流水号
	/// </summary>
	public int PlateRepealSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankRepealSerial;

	/// <summary>
	/// 被冲正银行流水号
	/// </summary>
	public string BankRepealSerial
	{
		get { return StringExtend.GetString(_BankRepealSerial); }
		set { _BankRepealSerial = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 被冲正期货流水号
	/// </summary>
	public int FutureRepealSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	/// <summary>
	/// 期货可取金额
	/// </summary>
	public double FutureFetchAmount;

	/// <summary>
	/// 费用支付标志
	/// </summary>
	public TThostFtdcFeePayFlagType FeePayFlag;

	/// <summary>
	/// 应收客户费用
	/// </summary>
	public double CustFee;

	/// <summary>
	/// 应收期货公司费用
	/// </summary>
	public double BrokerFee;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 发送方给接收方的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 转账交易状态
	/// </summary>
	public TThostFtdcTransferStatusType TransferStatus;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 查询账户信息请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqQueryAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 查询账户信息响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspQueryAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 银行可用金额
	/// </summary>
	public double BankUseAmount;

	/// <summary>
	/// 银行可取金额
	/// </summary>
	public double BankFetchAmount;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 期商签到签退
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcFutureSignIOField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;
}

/// <summary>
/// 期商签到响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspFutureSignInField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _PinKey;

	/// <summary>
	/// PIN密钥
	/// </summary>
	public string PinKey
	{
		get { return StringExtend.GetString(_PinKey); }
		set { _PinKey = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _MacKey;

	/// <summary>
	/// MAC密钥
	/// </summary>
	public string MacKey
	{
		get { return StringExtend.GetString(_MacKey); }
		set { _MacKey = StringExtend.GetBytes(value, 129); }
	}
}

/// <summary>
/// 期商签退请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqFutureSignOutField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;
}

/// <summary>
/// 期商签退响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspFutureSignOutField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 查询指定流水号的交易结果请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqQueryTradeResultBySerialField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 流水号
	/// </summary>
	public int Reference;

	/// <summary>
	/// 本流水号发布者的机构类型
	/// </summary>
	public TThostFtdcInstitutionTypeType RefrenceIssureType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _RefrenceIssure;

	/// <summary>
	/// 本流水号发布者机构编码
	/// </summary>
	public string RefrenceIssure
	{
		get { return StringExtend.GetString(_RefrenceIssure); }
		set { _RefrenceIssure = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 查询指定流水号的交易结果响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspQueryTradeResultBySerialField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	/// <summary>
	/// 流水号
	/// </summary>
	public int Reference;

	/// <summary>
	/// 本流水号发布者的机构类型
	/// </summary>
	public TThostFtdcInstitutionTypeType RefrenceIssureType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _RefrenceIssure;

	/// <summary>
	/// 本流水号发布者机构编码
	/// </summary>
	public string RefrenceIssure
	{
		get { return StringExtend.GetString(_RefrenceIssure); }
		set { _RefrenceIssure = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _OriginReturnCode;

	/// <summary>
	/// 原始返回代码
	/// </summary>
	public string OriginReturnCode
	{
		get { return StringExtend.GetString(_OriginReturnCode); }
		set { _OriginReturnCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _OriginDescrInfoForReturnCode;

	/// <summary>
	/// 原始返回码描述
	/// </summary>
	public string OriginDescrInfoForReturnCode
	{
		get { return StringExtend.GetString(_OriginDescrInfoForReturnCode); }
		set { _OriginDescrInfoForReturnCode = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 转帐金额
	/// </summary>
	public double TradeAmount;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}
}

/// <summary>
/// 日终文件就绪请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqDayEndFileReadyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 文件业务功能
	/// </summary>
	public TThostFtdcFileBusinessCodeType FileBusinessCode;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}
}

/// <summary>
/// 返回结果
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReturnResultField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ReturnCode;

	/// <summary>
	/// 返回代码
	/// </summary>
	public string ReturnCode
	{
		get { return StringExtend.GetString(_ReturnCode); }
		set { _ReturnCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _DescrInfoForReturnCode;

	/// <summary>
	/// 返回码描述
	/// </summary>
	public string DescrInfoForReturnCode
	{
		get { return StringExtend.GetString(_DescrInfoForReturnCode); }
		set { _DescrInfoForReturnCode = StringExtend.GetBytes(value, 129); }
	}
}

/// <summary>
/// 验证期货资金密码
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcVerifyFuturePasswordField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 验证客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcVerifyCustInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 验证期货资金密码和客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcVerifyFuturePasswordAndCustInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 验证期货资金密码和客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDepositResultInformField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=15)]
	private byte[] _DepositSeqNo;

	/// <summary>
	/// 出入金流水号，该流水号为银期报盘返回的流水号
	/// </summary>
	public string DepositSeqNo
	{
		get { return StringExtend.GetString(_DepositSeqNo); }
		set { _DepositSeqNo = StringExtend.GetBytes(value, 15); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ReturnCode;

	/// <summary>
	/// 返回代码
	/// </summary>
	public string ReturnCode
	{
		get { return StringExtend.GetString(_ReturnCode); }
		set { _ReturnCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _DescrInfoForReturnCode;

	/// <summary>
	/// 返回码描述
	/// </summary>
	public string DescrInfoForReturnCode
	{
		get { return StringExtend.GetString(_DescrInfoForReturnCode); }
		set { _DescrInfoForReturnCode = StringExtend.GetBytes(value, 129); }
	}
}

/// <summary>
/// 交易核心向银期报盘发出密钥同步请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqSyncKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 交易核心给银期报盘的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;
}

/// <summary>
/// 交易核心向银期报盘发出密钥同步响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspSyncKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 交易核心给银期报盘的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 查询账户信息通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcNotifyQueryAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 银行可用金额
	/// </summary>
	public double BankUseAmount;

	/// <summary>
	/// 银行可取金额
	/// </summary>
	public double BankFetchAmount;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 银期转账交易流水表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTransferSerialField
{

	/// <summary>
	/// 平台流水号
	/// </summary>
	public int PlateSerial;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易发起方日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 交易代码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	/// <summary>
	/// 会话编号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行编码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构编码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期货公司编码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	/// <summary>
	/// 期货公司帐号类型
	/// </summary>
	public TThostFtdcFutureAccTypeType FutureAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 期货公司流水号
	/// </summary>
	public int FutureSerial;

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 交易金额
	/// </summary>
	public double TradeAmount;

	/// <summary>
	/// 应收客户费用
	/// </summary>
	public double CustFee;

	/// <summary>
	/// 应收期货公司费用
	/// </summary>
	public double BrokerFee;

	/// <summary>
	/// 有效标志
	/// </summary>
	public TThostFtdcAvailabilityFlagType AvailabilityFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperatorCode;

	/// <summary>
	/// 操作员
	/// </summary>
	public string OperatorCode
	{
		get { return StringExtend.GetString(_OperatorCode); }
		set { _OperatorCode = StringExtend.GetBytes(value, 17); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankNewAccount;

	/// <summary>
	/// 新银行帐号
	/// </summary>
	public string BankNewAccount
	{
		get { return StringExtend.GetString(_BankNewAccount); }
		set { _BankNewAccount = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 请求查询转帐流水
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryTransferSerialField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行编码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 期商签到通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcNotifyFutureSignInField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _PinKey;

	/// <summary>
	/// PIN密钥
	/// </summary>
	public string PinKey
	{
		get { return StringExtend.GetString(_PinKey); }
		set { _PinKey = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _MacKey;

	/// <summary>
	/// MAC密钥
	/// </summary>
	public string MacKey
	{
		get { return StringExtend.GetString(_MacKey); }
		set { _MacKey = StringExtend.GetBytes(value, 129); }
	}
}

/// <summary>
/// 期商签退通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcNotifyFutureSignOutField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 交易核心向银期报盘发出密钥同步处理结果的通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcNotifySyncKeyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=129)]
	private byte[] _Message;

	/// <summary>
	/// 交易核心给银期报盘的消息
	/// </summary>
	public string Message
	{
		get { return StringExtend.GetString(_Message); }
		set { _Message = StringExtend.GetBytes(value, 129); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 请求编号
	/// </summary>
	public int RequestID;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 请求查询银期签约关系
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryAccountregisterField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行编码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构编码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 客户开销户信息表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcAccountregisterField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDay;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDay
	{
		get { return StringExtend.GetString(_TradeDay); }
		set { _TradeDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行编码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构编码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期货公司编码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期货公司分支机构编码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 开销户类别
	/// </summary>
	public TThostFtdcOpenOrDestroyType OpenOrDestroy;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _RegDate;

	/// <summary>
	/// 签约日期
	/// </summary>
	public string RegDate
	{
		get { return StringExtend.GetString(_RegDate); }
		set { _RegDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OutDate;

	/// <summary>
	/// 解约日期
	/// </summary>
	public string OutDate
	{
		get { return StringExtend.GetString(_OutDate); }
		set { _OutDate = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 银期开户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcOpenAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇钞标志
	/// </summary>
	public TThostFtdcCashExchangeCodeType CashExchangeCode;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 银期销户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCancelAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	/// <summary>
	/// 汇钞标志
	/// </summary>
	public TThostFtdcCashExchangeCodeType CashExchangeCode;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=3)]
	private byte[] _DeviceID;

	/// <summary>
	/// 渠道标志
	/// </summary>
	public string DeviceID
	{
		get { return StringExtend.GetString(_DeviceID); }
		set { _DeviceID = StringExtend.GetBytes(value, 3); }
	}

	/// <summary>
	/// 期货单位帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankSecuAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankSecuAcc;

	/// <summary>
	/// 期货单位帐号
	/// </summary>
	public string BankSecuAcc
	{
		get { return StringExtend.GetString(_BankSecuAcc); }
		set { _BankSecuAcc = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=17)]
	private byte[] _OperNo;

	/// <summary>
	/// 交易柜员
	/// </summary>
	public string OperNo
	{
		get { return StringExtend.GetString(_OperNo); }
		set { _OperNo = StringExtend.GetBytes(value, 17); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户标识
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 银期变更银行账号信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcChangeAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewBankAccount;

	/// <summary>
	/// 新银行帐号
	/// </summary>
	public string NewBankAccount
	{
		get { return StringExtend.GetString(_NewBankAccount); }
		set { _NewBankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _NewBankPassWord;

	/// <summary>
	/// 新银行密码
	/// </summary>
	public string NewBankPassWord
	{
		get { return StringExtend.GetString(_NewBankPassWord); }
		set { _NewBankPassWord = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// 银行密码标志
	/// </summary>
	public TThostFtdcPwdFlagType BankPwdFlag;

	/// <summary>
	/// 期货资金密码核对标志
	/// </summary>
	public TThostFtdcPwdFlagType SecuPwdFlag;

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _LongCustomerName;

	/// <summary>
	/// 长客户姓名
	/// </summary>
	public string LongCustomerName
	{
		get { return StringExtend.GetString(_LongCustomerName); }
		set { _LongCustomerName = StringExtend.GetBytes(value, 161); }
	}
}

/// <summary>
/// 二级代理操作员银期权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcSecAgentACIDMapField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账户
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BrokerSecAgentID;

	/// <summary>
	/// 境外中介机构资金帐号
	/// </summary>
	public string BrokerSecAgentID
	{
		get { return StringExtend.GetString(_BrokerSecAgentID); }
		set { _BrokerSecAgentID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 二级代理操作员银期权限查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySecAgentACIDMapField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 资金账户
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 灾备中心交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserRightsAssignField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 应用单元代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 交易中心代码
	/// </summary>
	public int DRIdentityID;
}

/// <summary>
/// 经济公司是否有在本标示的交易权限
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcBrokerUserRightAssignField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 应用单元代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	/// <summary>
	/// 交易中心代码
	/// </summary>
	public int DRIdentityID;

	/// <summary>
	/// 能否交易
	/// </summary>
	public int Tradeable;
}

/// <summary>
/// 灾备交易转换报文
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDRTransferField
{

	/// <summary>
	/// 原交易中心代码
	/// </summary>
	public int OrigDRIdentityID;

	/// <summary>
	/// 目标交易中心代码
	/// </summary>
	public int DestDRIdentityID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _OrigBrokerID;

	/// <summary>
	/// 原应用单元代码
	/// </summary>
	public string OrigBrokerID
	{
		get { return StringExtend.GetString(_OrigBrokerID); }
		set { _OrigBrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _DestBrokerID;

	/// <summary>
	/// 目标易用单元代码
	/// </summary>
	public string DestBrokerID
	{
		get { return StringExtend.GetString(_DestBrokerID); }
		set { _DestBrokerID = StringExtend.GetBytes(value, 11); }
	}
}

/// <summary>
/// Fens用户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcFensUserInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 登录模式
	/// </summary>
	public TThostFtdcLoginModeType LoginMode;
}

/// <summary>
/// 当前银期所属交易中心
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCurrTransferIdentityField
{

	/// <summary>
	/// 交易中心代码
	/// </summary>
	public int IdentityID;
}

/// <summary>
/// 禁止登录用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcLoginForbiddenUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询禁止登录用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryLoginForbiddenUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// UDP组播组信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcMulticastGroupInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _GroupIP;

	/// <summary>
	/// 组播组IP地址
	/// </summary>
	public string GroupIP
	{
		get { return StringExtend.GetString(_GroupIP); }
		set { _GroupIP = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 组播组IP端口
	/// </summary>
	public int GroupPort;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _SourceIP;

	/// <summary>
	/// 源地址
	/// </summary>
	public string SourceIP
	{
		get { return StringExtend.GetString(_SourceIP); }
		set { _SourceIP = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 资金账户基本准备金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcTradingAccountReserveField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	/// <summary>
	/// 基本准备金
	/// </summary>
	public double Reserve;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询禁止登录IP
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryLoginForbiddenIPField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询IP列表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryIPListField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _IPAddress;

	/// <summary>
	/// IP地址
	/// </summary>
	public string IPAddress
	{
		get { return StringExtend.GetString(_IPAddress); }
		set { _IPAddress = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 查询用户下单权限分配表
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryUserRightsAssignField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 应用单元代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 银期预约开户确认请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReserveOpenAccountConfirmField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 161); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 期货密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankReserveOpenSeq;

	/// <summary>
	/// 预约开户银行流水号
	/// </summary>
	public string BankReserveOpenSeq
	{
		get { return StringExtend.GetString(_BankReserveOpenSeq); }
		set { _BankReserveOpenSeq = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _BookDate;

	/// <summary>
	/// 预约开户日期
	/// </summary>
	public string BookDate
	{
		get { return StringExtend.GetString(_BookDate); }
		set { _BookDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BookPsw;

	/// <summary>
	/// 预约开户验证密码
	/// </summary>
	public string BookPsw
	{
		get { return StringExtend.GetString(_BookPsw); }
		set { _BookPsw = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 银期预约开户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReserveOpenAccountField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _TradeCode;

	/// <summary>
	/// 业务功能码
	/// </summary>
	public string TradeCode
	{
		get { return StringExtend.GetString(_TradeCode); }
		set { _TradeCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行代码
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=5)]
	private byte[] _BankBranchID;

	/// <summary>
	/// 银行分支机构代码
	/// </summary>
	public string BankBranchID
	{
		get { return StringExtend.GetString(_BankBranchID); }
		set { _BankBranchID = StringExtend.GetBytes(value, 5); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 期商代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _BrokerBranchID;

	/// <summary>
	/// 期商分支机构代码
	/// </summary>
	public string BrokerBranchID
	{
		get { return StringExtend.GetString(_BrokerBranchID); }
		set { _BrokerBranchID = StringExtend.GetBytes(value, 31); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeDate;

	/// <summary>
	/// 交易日期
	/// </summary>
	public string TradeDate
	{
		get { return StringExtend.GetString(_TradeDate); }
		set { _TradeDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradeTime;

	/// <summary>
	/// 交易时间
	/// </summary>
	public string TradeTime
	{
		get { return StringExtend.GetString(_TradeTime); }
		set { _TradeTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BankSerial;

	/// <summary>
	/// 银行流水号
	/// </summary>
	public string BankSerial
	{
		get { return StringExtend.GetString(_BankSerial); }
		set { _BankSerial = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易系统日期 
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	/// <summary>
	/// 银期平台消息流水号
	/// </summary>
	public int PlateSerial;

	/// <summary>
	/// 最后分片标志
	/// </summary>
	public TThostFtdcLastFragmentType LastFragment;

	/// <summary>
	/// 会话号
	/// </summary>
	public int SessionID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=161)]
	private byte[] _CustomerName;

	/// <summary>
	/// 客户姓名
	/// </summary>
	public string CustomerName
	{
		get { return StringExtend.GetString(_CustomerName); }
		set { _CustomerName = StringExtend.GetBytes(value, 161); }
	}

	/// <summary>
	/// 证件类型
	/// </summary>
	public TThostFtdcIdCardTypeType IdCardType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=51)]
	private byte[] _IdentifiedCardNo;

	/// <summary>
	/// 证件号码
	/// </summary>
	public string IdentifiedCardNo
	{
		get { return StringExtend.GetString(_IdentifiedCardNo); }
		set { _IdentifiedCardNo = StringExtend.GetBytes(value, 51); }
	}

	/// <summary>
	/// 性别
	/// </summary>
	public TThostFtdcGenderType Gender;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _CountryCode;

	/// <summary>
	/// 国家代码
	/// </summary>
	public string CountryCode
	{
		get { return StringExtend.GetString(_CountryCode); }
		set { _CountryCode = StringExtend.GetBytes(value, 21); }
	}

	/// <summary>
	/// 客户类型
	/// </summary>
	public TThostFtdcCustTypeType CustType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _Address;

	/// <summary>
	/// 地址
	/// </summary>
	public string Address
	{
		get { return StringExtend.GetString(_Address); }
		set { _Address = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=7)]
	private byte[] _ZipCode;

	/// <summary>
	/// 邮编
	/// </summary>
	public string ZipCode
	{
		get { return StringExtend.GetString(_ZipCode); }
		set { _ZipCode = StringExtend.GetBytes(value, 7); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Telephone;

	/// <summary>
	/// 电话号码
	/// </summary>
	public string Telephone
	{
		get { return StringExtend.GetString(_Telephone); }
		set { _Telephone = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MobilePhone;

	/// <summary>
	/// 手机
	/// </summary>
	public string MobilePhone
	{
		get { return StringExtend.GetString(_MobilePhone); }
		set { _MobilePhone = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Fax;

	/// <summary>
	/// 传真
	/// </summary>
	public string Fax
	{
		get { return StringExtend.GetString(_Fax); }
		set { _Fax = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _EMail;

	/// <summary>
	/// 电子邮件
	/// </summary>
	public string EMail
	{
		get { return StringExtend.GetString(_EMail); }
		set { _EMail = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 资金账户状态
	/// </summary>
	public TThostFtdcMoneyAccountStatusType MoneyAccountStatus;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行帐号
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankPassWord;

	/// <summary>
	/// 银行密码
	/// </summary>
	public string BankPassWord
	{
		get { return StringExtend.GetString(_BankPassWord); }
		set { _BankPassWord = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 安装编号
	/// </summary>
	public int InstallID;

	/// <summary>
	/// 验证客户证件号码标志
	/// </summary>
	public TThostFtdcYesNoIndicatorType VerifyCertNoFlag;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _Digest;

	/// <summary>
	/// 摘要
	/// </summary>
	public string Digest
	{
		get { return StringExtend.GetString(_Digest); }
		set { _Digest = StringExtend.GetBytes(value, 36); }
	}

	/// <summary>
	/// 银行帐号类型
	/// </summary>
	public TThostFtdcBankAccTypeType BankAccType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _BrokerIDByBank;

	/// <summary>
	/// 期货公司银行编码
	/// </summary>
	public string BrokerIDByBank
	{
		get { return StringExtend.GetString(_BrokerIDByBank); }
		set { _BrokerIDByBank = StringExtend.GetBytes(value, 33); }
	}

	/// <summary>
	/// 交易ID
	/// </summary>
	public int TID;

	/// <summary>
	/// 预约开户状态
	/// </summary>
	public TThostFtdcReserveOpenAccStasType ReserveOpenAccStas;

	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=81)]
	private byte[] _ErrorMsg;

	/// <summary>
	/// 错误信息
	/// </summary>
	public string ErrorMsg
	{
		get { return StringExtend.GetString(_ErrorMsg); }
		set { _ErrorMsg = StringExtend.GetBytes(value, 81); }
	}
}

/// <summary>
/// 银行账户属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcAccountPropertyField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _AccountID;

	/// <summary>
	/// 投资者帐号
	/// </summary>
	public string AccountID
	{
		get { return StringExtend.GetString(_AccountID); }
		set { _AccountID = StringExtend.GetBytes(value, 13); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _BankID;

	/// <summary>
	/// 银行统一标识类型
	/// </summary>
	public string BankID
	{
		get { return StringExtend.GetString(_BankID); }
		set { _BankID = StringExtend.GetBytes(value, 4); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _BankAccount;

	/// <summary>
	/// 银行账户
	/// </summary>
	public string BankAccount
	{
		get { return StringExtend.GetString(_BankAccount); }
		set { _BankAccount = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _OpenName;

	/// <summary>
	/// 银行账户的开户人名称
	/// </summary>
	public string OpenName
	{
		get { return StringExtend.GetString(_OpenName); }
		set { _OpenName = StringExtend.GetBytes(value, 101); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=101)]
	private byte[] _OpenBank;

	/// <summary>
	/// 银行账户的开户行
	/// </summary>
	public string OpenBank
	{
		get { return StringExtend.GetString(_OpenBank); }
		set { _OpenBank = StringExtend.GetBytes(value, 101); }
	}

	/// <summary>
	/// 是否活跃
	/// </summary>
	public int IsActive;

	/// <summary>
	/// 账户来源
	/// </summary>
	public TThostFtdcAccountSourceTypeType AccountSourceType;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OpenDate;

	/// <summary>
	/// 开户日期
	/// </summary>
	public string OpenDate
	{
		get { return StringExtend.GetString(_OpenDate); }
		set { _OpenDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _CancelDate;

	/// <summary>
	/// 注销日期
	/// </summary>
	public string CancelDate
	{
		get { return StringExtend.GetString(_CancelDate); }
		set { _CancelDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=65)]
	private byte[] _OperatorID;

	/// <summary>
	/// 录入员代码
	/// </summary>
	public string OperatorID
	{
		get { return StringExtend.GetString(_OperatorID); }
		set { _OperatorID = StringExtend.GetBytes(value, 65); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OperateDate;

	/// <summary>
	/// 录入日期
	/// </summary>
	public string OperateDate
	{
		get { return StringExtend.GetString(_OperateDate); }
		set { _OperateDate = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _OperateTime;

	/// <summary>
	/// 录入时间
	/// </summary>
	public string OperateTime
	{
		get { return StringExtend.GetString(_OperateTime); }
		set { _OperateTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=4)]
	private byte[] _CurrencyID;

	/// <summary>
	/// 币种代码
	/// </summary>
	public string CurrencyID
	{
		get { return StringExtend.GetString(_CurrencyID); }
		set { _CurrencyID = StringExtend.GetBytes(value, 4); }
	}
}

/// <summary>
/// 查询当前交易中心
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQryCurrDRIdentityField
{

	/// <summary>
	/// 交易中心代码
	/// </summary>
	public int DRIdentityID;
}

/// <summary>
/// 当前交易中心
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcCurrDRIdentityField
{

	/// <summary>
	/// 交易中心代码
	/// </summary>
	public int DRIdentityID;
}

/// <summary>
/// 查询二级代理商资金校验模式
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySecAgentCheckModeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询二级代理商信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQrySecAgentTradeInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _BrokerSecAgentID;

	/// <summary>
	/// 境外中介机构资金帐号
	/// </summary>
	public string BrokerSecAgentID
	{
		get { return StringExtend.GetString(_BrokerSecAgentID); }
		set { _BrokerSecAgentID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 用户系统信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcUserSystemInfoField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 用户端系统内部信息长度
	/// </summary>
	public int ClientSystemInfoLen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=273)]
	private byte[] _ClientSystemInfo;

	/// <summary>
	/// 用户端系统内部信息
	/// </summary>
	public string ClientSystemInfo
	{
		get { return StringExtend.GetString(_ClientSystemInfo); }
		set { _ClientSystemInfo = StringExtend.GetBytes(value, 273); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ClientPublicIP;

	/// <summary>
	/// 用户公网IP
	/// </summary>
	public string ClientPublicIP
	{
		get { return StringExtend.GetString(_ClientPublicIP); }
		set { _ClientPublicIP = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 终端IP端口
	/// </summary>
	public int ClientIPPort;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _ClientLoginTime;

	/// <summary>
	/// 登录成功时间
	/// </summary>
	public string ClientLoginTime
	{
		get { return StringExtend.GetString(_ClientLoginTime); }
		set { _ClientLoginTime = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=33)]
	private byte[] _ClientAppID;

	/// <summary>
	/// App代码
	/// </summary>
	public string ClientAppID
	{
		get { return StringExtend.GetString(_ClientAppID); }
		set { _ClientAppID = StringExtend.GetBytes(value, 33); }
	}
}

/// <summary>
/// 用户发出获取安全安全登陆方法请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqUserAuthMethodField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 用户发出获取安全安全登陆方法回复
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspUserAuthMethodField
{

	/// <summary>
	/// 当前可以用的认证模式
	/// </summary>
	public int UsableAuthMethod;
}

/// <summary>
/// 用户发出获取安全安全登陆方法请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqGenUserCaptchaField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 生成的图片验证码信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspGenUserCaptchaField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 图片信息长度
	/// </summary>
	public int CaptchaInfoLen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=2561)]
	private byte[] _CaptchaInfo;

	/// <summary>
	/// 图片信息
	/// </summary>
	public string CaptchaInfo
	{
		get { return StringExtend.GetString(_CaptchaInfo); }
		set { _CaptchaInfo = StringExtend.GetBytes(value, 2561); }
	}
}

/// <summary>
/// 用户发出获取安全安全登陆方法请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqGenUserTextField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}
}

/// <summary>
/// 短信验证码生成的回复
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspGenUserTextField
{

	/// <summary>
	/// 短信验证码序号
	/// </summary>
	public int UserTextSeq;
}

/// <summary>
/// 用户发出带图形验证码的登录请求请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqUserLoginWithCaptchaField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ClientIPAddress;

	/// <summary>
	/// 终端IP地址
	/// </summary>
	public string ClientIPAddress
	{
		get { return StringExtend.GetString(_ClientIPAddress); }
		set { _ClientIPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Captcha;

	/// <summary>
	/// 图形验证码的文字内容
	/// </summary>
	public string Captcha
	{
		get { return StringExtend.GetString(_Captcha); }
		set { _Captcha = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 终端IP端口
	/// </summary>
	public int ClientIPPort;
}

/// <summary>
/// 用户发出带短信验证码的登录请求请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqUserLoginWithTextField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ClientIPAddress;

	/// <summary>
	/// 终端IP地址
	/// </summary>
	public string ClientIPAddress
	{
		get { return StringExtend.GetString(_ClientIPAddress); }
		set { _ClientIPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Text;

	/// <summary>
	/// 短信验证码文字内容
	/// </summary>
	public string Text
	{
		get { return StringExtend.GetString(_Text); }
		set { _Text = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 终端IP端口
	/// </summary>
	public int ClientIPPort;
}

/// <summary>
/// 用户发出带动态验证码的登录请求请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqUserLoginWithOTPField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=9)]
	private byte[] _TradingDay;

	/// <summary>
	/// 交易日
	/// </summary>
	public string TradingDay
	{
		get { return StringExtend.GetString(_TradingDay); }
		set { _TradingDay = StringExtend.GetBytes(value, 9); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _Password;

	/// <summary>
	/// 密码
	/// </summary>
	public string Password
	{
		get { return StringExtend.GetString(_Password); }
		set { _Password = StringExtend.GetBytes(value, 41); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _UserProductInfo;

	/// <summary>
	/// 用户端产品信息
	/// </summary>
	public string UserProductInfo
	{
		get { return StringExtend.GetString(_UserProductInfo); }
		set { _UserProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _InterfaceProductInfo;

	/// <summary>
	/// 接口端产品信息
	/// </summary>
	public string InterfaceProductInfo
	{
		get { return StringExtend.GetString(_InterfaceProductInfo); }
		set { _InterfaceProductInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _ProtocolInfo;

	/// <summary>
	/// 协议信息
	/// </summary>
	public string ProtocolInfo
	{
		get { return StringExtend.GetString(_ProtocolInfo); }
		set { _ProtocolInfo = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=21)]
	private byte[] _MacAddress;

	/// <summary>
	/// Mac地址
	/// </summary>
	public string MacAddress
	{
		get { return StringExtend.GetString(_MacAddress); }
		set { _MacAddress = StringExtend.GetBytes(value, 21); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _ClientIPAddress;

	/// <summary>
	/// 终端IP地址
	/// </summary>
	public string ClientIPAddress
	{
		get { return StringExtend.GetString(_ClientIPAddress); }
		set { _ClientIPAddress = StringExtend.GetBytes(value, 16); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=36)]
	private byte[] _LoginRemark;

	/// <summary>
	/// 登录备注
	/// </summary>
	public string LoginRemark
	{
		get { return StringExtend.GetString(_LoginRemark); }
		set { _LoginRemark = StringExtend.GetBytes(value, 36); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=41)]
	private byte[] _OTPPassword;

	/// <summary>
	/// OTP密码
	/// </summary>
	public string OTPPassword
	{
		get { return StringExtend.GetString(_OTPPassword); }
		set { _OTPPassword = StringExtend.GetBytes(value, 41); }
	}

	/// <summary>
	/// 终端IP端口
	/// </summary>
	public int ClientIPPort;
}

/// <summary>
/// api握手请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqApiHandshakeField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=31)]
	private byte[] _CryptoKeyVersion;

	/// <summary>
	/// api与front通信密钥版本号
	/// </summary>
	public string CryptoKeyVersion
	{
		get { return StringExtend.GetString(_CryptoKeyVersion); }
		set { _CryptoKeyVersion = StringExtend.GetBytes(value, 31); }
	}
}

/// <summary>
/// front发给api的握手回复
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcRspApiHandshakeField
{

	/// <summary>
	/// 握手回复数据长度
	/// </summary>
	public int FrontHandshakeDataLen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=301)]
	private byte[] _FrontHandshakeData;

	/// <summary>
	/// 握手回复数据
	/// </summary>
	public string FrontHandshakeData
	{
		get { return StringExtend.GetString(_FrontHandshakeData); }
		set { _FrontHandshakeData = StringExtend.GetBytes(value, 301); }
	}

	/// <summary>
	/// API认证是否开启
	/// </summary>
	public int IsApiAuthEnabled;
}

/// <summary>
/// api给front的验证key的请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcReqVerifyApiKeyField
{

	/// <summary>
	/// 握手回复数据长度
	/// </summary>
	public int ApiHandshakeDataLen;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=301)]
	private byte[] _ApiHandshakeData;

	/// <summary>
	/// 握手回复数据
	/// </summary>
	public string ApiHandshakeData
	{
		get { return StringExtend.GetString(_ApiHandshakeData); }
		set { _ApiHandshakeData = StringExtend.GetBytes(value, 301); }
	}
}

/// <summary>
/// 操作员组织架构关系
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcDepartmentUserField
{

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=11)]
	private byte[] _BrokerID;

	/// <summary>
	/// 经纪公司代码
	/// </summary>
	public string BrokerID
	{
		get { return StringExtend.GetString(_BrokerID); }
		set { _BrokerID = StringExtend.GetBytes(value, 11); }
	}

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=16)]
	private byte[] _UserID;

	/// <summary>
	/// 用户代码
	/// </summary>
	public string UserID
	{
		get { return StringExtend.GetString(_UserID); }
		set { _UserID = StringExtend.GetBytes(value, 16); }
	}

	/// <summary>
	/// 投资者范围
	/// </summary>
	public TThostFtdcDepartmentRangeType InvestorRange;

	[MarshalAs(UnmanagedType.ByValArray, SizeConst=13)]
	private byte[] _InvestorID;

	/// <summary>
	/// 投资者代码
	/// </summary>
	public string InvestorID
	{
		get { return StringExtend.GetString(_InvestorID); }
		set { _InvestorID = StringExtend.GetBytes(value, 13); }
	}
}

/// <summary>
/// 查询频率，每秒查询比数
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CThostFtdcQueryFreqField
{

	/// <summary>
	/// 查询频率
	/// </summary>
	public int QueryFreq;
}

