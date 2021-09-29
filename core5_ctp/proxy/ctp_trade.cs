using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;
using PureCode.CtpCSharp;

namespace HaiFeng
{
	public class ctp_trade
	{
		#region Dll Load /UnLoad

		/// <summary>
		///
		/// </summary>
		/// <param name="pHModule"></param>
		/// <param name="lpProcName"></param>
		/// <param name="t"></param>
		/// <returns></returns>
		/// <exception cref="Exception"></exception>
		private static Delegate Invoke(IntPtr pHModule, string lpProcName, Type t)
		{
            return loader.Invoke(pHModule, lpProcName, t);
		}
		#endregion

        private static readonly AssembyLoader loader;
		IntPtr _handle = IntPtr.Zero, _api = IntPtr.Zero, _spi = IntPtr.Zero;
		private int nRequestID = 0;
		delegate IntPtr Create();

		static ctp_trade()
        {
            string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(typeof(ctp_trade).Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            string dllFileName = Path.Combine(dll_path, "ctp_trade.dll");
			
            loader = new AssembyLoader(dllFileName);
            var _handle = loader.GetDllHandle();

			if (_handle == IntPtr.Zero)
			{
				throw (new Exception(String.Format("没有找到:", dll_path)));
			}

			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");
        }
        
		public ctp_trade()
		{
            _handle = loader.GetDllHandle();

			_api = (Invoke(_handle, "CreateApi", typeof(Create)) as Create)();
			_spi = (Invoke(_handle, "CreateSpi", typeof(Create)) as Create)();
			this.RegisterSpi(_spi);
		}

        #region SE版本增加
        [UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
        public delegate IntPtr DeleGetVersion();
        public string GetVersion()
        {
            return Marshal.PtrToStringAnsi((Invoke(_handle, "GetVersion", typeof(DeleGetVersion)) as DeleGetVersion)());
        }
        #endregion

		/// <summary>
		///删除接口对象本身
		///@remark 不再使用本接口对象时,调用该函数删除接口对象
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRelease(IntPtr api);

		/// <summary>
		///初始化
		///@remark 初始化运行环境,只有调用后,接口才开始工作
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleInit(IntPtr api);

		/// <summary>
		///等待接口线程结束运行
		///@return 线程退出代码
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleJoin(IntPtr api);

		/// <summary>
		///注册前置机网络地址
		///@param pszFrontAddress：前置机网络地址。
		///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。 
		///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterFront(IntPtr api, string pszFrontAddress);

		/// <summary>
		///注册名字服务器网络地址
		///@param pszNsAddress：名字服务器网络地址。
		///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。 
		///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
		///@remark RegisterNameServer优先于RegisterFront
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterNameServer(IntPtr api, string pszNsAddress);

		/// <summary>
		///注册名字服务器用户信息
		///@param pFensUserInfo：用户信息。
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterFensUserInfo(IntPtr api, ref CThostFtdcFensUserInfoField pFensUserInfo);

		/// <summary>
		///注册回调接口
		///@param pSpi 派生自回调接口类的实例
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterSpi(IntPtr api, IntPtr pSpi);

		/// <summary>
		///订阅私有流。
		///@param nResumeType 私有流重传方式  
		///        THOST_TERT_RESTART:从本交易日开始重传
		///        THOST_TERT_RESUME:从上次收到的续传
		///        THOST_TERT_QUICK:只传送登录后私有流的内容
		///@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePrivateTopic(IntPtr api, THOST_TE_RESUME_TYPE nResumeType);

		/// <summary>
		///订阅公共流。
		///@param nResumeType 公共流重传方式  
		///        THOST_TERT_RESTART:从本交易日开始重传
		///        THOST_TERT_RESUME:从上次收到的续传
		///        THOST_TERT_QUICK:只传送登录后公共流的内容
		///@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePublicTopic(IntPtr api, THOST_TE_RESUME_TYPE nResumeType);

		/// <summary>
		///客户端认证请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqAuthenticate(IntPtr api, ref CThostFtdcReqAuthenticateField pReqAuthenticateField, int nRequestID);

		/// <summary>
		///注册用户终端信息，用于中继服务器多连接模式
		///需要在终端认证成功后，用户登录前调用该接口
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterUserSystemInfo(IntPtr api, ref CThostFtdcUserSystemInfoField pUserSystemInfo);

		/// <summary>
		///上报用户终端信息，用于中继服务器操作员登录模式
		///操作员登录后，可以多次调用该接口上报客户信息
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubmitUserSystemInfo(IntPtr api, ref CThostFtdcUserSystemInfoField pUserSystemInfo);

		/// <summary>
		///用户登录请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogin(IntPtr api, ref CThostFtdcReqUserLoginField pReqUserLoginField, int nRequestID);

		/// <summary>
		///登出请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogout(IntPtr api, ref CThostFtdcUserLogoutField pUserLogout, int nRequestID);

		/// <summary>
		///用户口令更新请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserPasswordUpdate(IntPtr api, ref CThostFtdcUserPasswordUpdateField pUserPasswordUpdate, int nRequestID);

		/// <summary>
		///资金账户口令更新请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqTradingAccountPasswordUpdate(IntPtr api, ref CThostFtdcTradingAccountPasswordUpdateField pTradingAccountPasswordUpdate, int nRequestID);

		/// <summary>
		///查询用户当前支持的认证模式
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserAuthMethod(IntPtr api, ref CThostFtdcReqUserAuthMethodField pReqUserAuthMethod, int nRequestID);

		/// <summary>
		///用户发出获取图形验证码请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqGenUserCaptcha(IntPtr api, ref CThostFtdcReqGenUserCaptchaField pReqGenUserCaptcha, int nRequestID);

		/// <summary>
		///用户发出获取短信验证码请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqGenUserText(IntPtr api, ref CThostFtdcReqGenUserTextField pReqGenUserText, int nRequestID);

		/// <summary>
		///用户发出带有图片验证码的登陆请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithCaptcha(IntPtr api, ref CThostFtdcReqUserLoginWithCaptchaField pReqUserLoginWithCaptcha, int nRequestID);

		/// <summary>
		///用户发出带有短信验证码的登陆请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithText(IntPtr api, ref CThostFtdcReqUserLoginWithTextField pReqUserLoginWithText, int nRequestID);

		/// <summary>
		///用户发出带有动态口令的登陆请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithOTP(IntPtr api, ref CThostFtdcReqUserLoginWithOTPField pReqUserLoginWithOTP, int nRequestID);

		/// <summary>
		///报单录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderInsert(IntPtr api, ref CThostFtdcInputOrderField pInputOrder, int nRequestID);

		/// <summary>
		///预埋单录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqParkedOrderInsert(IntPtr api, ref CThostFtdcParkedOrderField pParkedOrder, int nRequestID);

		/// <summary>
		///预埋撤单录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqParkedOrderAction(IntPtr api, ref CThostFtdcParkedOrderActionField pParkedOrderAction, int nRequestID);

		/// <summary>
		///报单操作请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderAction(IntPtr api, ref CThostFtdcInputOrderActionField pInputOrderAction, int nRequestID);

		/// <summary>
		///查询最大报单数量请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQueryMaxOrderVolume(IntPtr api, ref CThostFtdcQueryMaxOrderVolumeField pQueryMaxOrderVolume, int nRequestID);

		/// <summary>
		///投资者结算结果确认
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqSettlementInfoConfirm(IntPtr api, ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm, int nRequestID);

		/// <summary>
		///请求删除预埋单
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqRemoveParkedOrder(IntPtr api, ref CThostFtdcRemoveParkedOrderField pRemoveParkedOrder, int nRequestID);

		/// <summary>
		///请求删除预埋撤单
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqRemoveParkedOrderAction(IntPtr api, ref CThostFtdcRemoveParkedOrderActionField pRemoveParkedOrderAction, int nRequestID);

		/// <summary>
		///执行宣告录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderInsert(IntPtr api, ref CThostFtdcInputExecOrderField pInputExecOrder, int nRequestID);

		/// <summary>
		///执行宣告操作请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderAction(IntPtr api, ref CThostFtdcInputExecOrderActionField pInputExecOrderAction, int nRequestID);

		/// <summary>
		///询价录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqForQuoteInsert(IntPtr api, ref CThostFtdcInputForQuoteField pInputForQuote, int nRequestID);

		/// <summary>
		///报价录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteInsert(IntPtr api, ref CThostFtdcInputQuoteField pInputQuote, int nRequestID);

		/// <summary>
		///报价操作请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteAction(IntPtr api, ref CThostFtdcInputQuoteActionField pInputQuoteAction, int nRequestID);

		/// <summary>
		///批量报单操作请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqBatchOrderAction(IntPtr api, ref CThostFtdcInputBatchOrderActionField pInputBatchOrderAction, int nRequestID);

		/// <summary>
		///期权自对冲录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOptionSelfCloseInsert(IntPtr api, ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose, int nRequestID);

		/// <summary>
		///期权自对冲操作请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOptionSelfCloseAction(IntPtr api, ref CThostFtdcInputOptionSelfCloseActionField pInputOptionSelfCloseAction, int nRequestID);

		/// <summary>
		///申请组合录入请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqCombActionInsert(IntPtr api, ref CThostFtdcInputCombActionField pInputCombAction, int nRequestID);

		/// <summary>
		///请求查询报单
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOrder(IntPtr api, ref CThostFtdcQryOrderField pQryOrder, int nRequestID);

		/// <summary>
		///请求查询成交
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTrade(IntPtr api, ref CThostFtdcQryTradeField pQryTrade, int nRequestID);

		/// <summary>
		///请求查询投资者持仓
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPosition(IntPtr api, ref CThostFtdcQryInvestorPositionField pQryInvestorPosition, int nRequestID);

		/// <summary>
		///请求查询资金账户
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingAccount(IntPtr api, ref CThostFtdcQryTradingAccountField pQryTradingAccount, int nRequestID);

		/// <summary>
		///请求查询投资者
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestor(IntPtr api, ref CThostFtdcQryInvestorField pQryInvestor, int nRequestID);

		/// <summary>
		///请求查询交易编码
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingCode(IntPtr api, ref CThostFtdcQryTradingCodeField pQryTradingCode, int nRequestID);

		/// <summary>
		///请求查询合约保证金率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentMarginRate(IntPtr api, ref CThostFtdcQryInstrumentMarginRateField pQryInstrumentMarginRate, int nRequestID);

		/// <summary>
		///请求查询合约手续费率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentCommissionRate(IntPtr api, ref CThostFtdcQryInstrumentCommissionRateField pQryInstrumentCommissionRate, int nRequestID);

		/// <summary>
		///请求查询交易所
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchange(IntPtr api, ref CThostFtdcQryExchangeField pQryExchange, int nRequestID);

		/// <summary>
		///请求查询产品
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProduct(IntPtr api, ref CThostFtdcQryProductField pQryProduct, int nRequestID);

		/// <summary>
		///请求查询合约
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrument(IntPtr api, ref CThostFtdcQryInstrumentField pQryInstrument, int nRequestID);

		/// <summary>
		///请求查询行情
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryDepthMarketData(IntPtr api, ref CThostFtdcQryDepthMarketDataField pQryDepthMarketData, int nRequestID);

		/// <summary>
		///请求查询投资者结算结果
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySettlementInfo(IntPtr api, ref CThostFtdcQrySettlementInfoField pQrySettlementInfo, int nRequestID);

		/// <summary>
		///请求查询转帐银行
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTransferBank(IntPtr api, ref CThostFtdcQryTransferBankField pQryTransferBank, int nRequestID);

		/// <summary>
		///请求查询投资者持仓明细
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPositionDetail(IntPtr api, ref CThostFtdcQryInvestorPositionDetailField pQryInvestorPositionDetail, int nRequestID);

		/// <summary>
		///请求查询客户通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryNotice(IntPtr api, ref CThostFtdcQryNoticeField pQryNotice, int nRequestID);

		/// <summary>
		///请求查询结算信息确认
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySettlementInfoConfirm(IntPtr api, ref CThostFtdcQrySettlementInfoConfirmField pQrySettlementInfoConfirm, int nRequestID);

		/// <summary>
		///请求查询投资者持仓明细
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPositionCombineDetail(IntPtr api, ref CThostFtdcQryInvestorPositionCombineDetailField pQryInvestorPositionCombineDetail, int nRequestID);

		/// <summary>
		///请求查询保证金监管系统经纪公司资金账户密钥
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCFMMCTradingAccountKey(IntPtr api, ref CThostFtdcQryCFMMCTradingAccountKeyField pQryCFMMCTradingAccountKey, int nRequestID);

		/// <summary>
		///请求查询仓单折抵信息
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryEWarrantOffset(IntPtr api, ref CThostFtdcQryEWarrantOffsetField pQryEWarrantOffset, int nRequestID);

		/// <summary>
		///请求查询投资者品种/跨品种保证金
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorProductGroupMargin(IntPtr api, ref CThostFtdcQryInvestorProductGroupMarginField pQryInvestorProductGroupMargin, int nRequestID);

		/// <summary>
		///请求查询交易所保证金率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeMarginRate(IntPtr api, ref CThostFtdcQryExchangeMarginRateField pQryExchangeMarginRate, int nRequestID);

		/// <summary>
		///请求查询交易所调整保证金率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeMarginRateAdjust(IntPtr api, ref CThostFtdcQryExchangeMarginRateAdjustField pQryExchangeMarginRateAdjust, int nRequestID);

		/// <summary>
		///请求查询汇率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeRate(IntPtr api, ref CThostFtdcQryExchangeRateField pQryExchangeRate, int nRequestID);

		/// <summary>
		///请求查询二级代理操作员银期权限
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentACIDMap(IntPtr api, ref CThostFtdcQrySecAgentACIDMapField pQrySecAgentACIDMap, int nRequestID);

		/// <summary>
		///请求查询产品报价汇率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProductExchRate(IntPtr api, ref CThostFtdcQryProductExchRateField pQryProductExchRate, int nRequestID);

		/// <summary>
		///请求查询产品组
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProductGroup(IntPtr api, ref CThostFtdcQryProductGroupField pQryProductGroup, int nRequestID);

		/// <summary>
		///请求查询做市商合约手续费率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMMInstrumentCommissionRate(IntPtr api, ref CThostFtdcQryMMInstrumentCommissionRateField pQryMMInstrumentCommissionRate, int nRequestID);

		/// <summary>
		///请求查询做市商期权合约手续费
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMMOptionInstrCommRate(IntPtr api, ref CThostFtdcQryMMOptionInstrCommRateField pQryMMOptionInstrCommRate, int nRequestID);

		/// <summary>
		///请求查询报单手续费
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentOrderCommRate(IntPtr api, ref CThostFtdcQryInstrumentOrderCommRateField pQryInstrumentOrderCommRate, int nRequestID);

		/// <summary>
		///请求查询资金账户
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentTradingAccount(IntPtr api, ref CThostFtdcQryTradingAccountField pQryTradingAccount, int nRequestID);

		/// <summary>
		///请求查询二级代理商资金校验模式
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentCheckMode(IntPtr api, ref CThostFtdcQrySecAgentCheckModeField pQrySecAgentCheckMode, int nRequestID);

		/// <summary>
		///请求查询二级代理商信息
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentTradeInfo(IntPtr api, ref CThostFtdcQrySecAgentTradeInfoField pQrySecAgentTradeInfo, int nRequestID);

		/// <summary>
		///请求查询期权交易成本
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionInstrTradeCost(IntPtr api, ref CThostFtdcQryOptionInstrTradeCostField pQryOptionInstrTradeCost, int nRequestID);

		/// <summary>
		///请求查询期权合约手续费
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionInstrCommRate(IntPtr api, ref CThostFtdcQryOptionInstrCommRateField pQryOptionInstrCommRate, int nRequestID);

		/// <summary>
		///请求查询执行宣告
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExecOrder(IntPtr api, ref CThostFtdcQryExecOrderField pQryExecOrder, int nRequestID);

		/// <summary>
		///请求查询询价
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryForQuote(IntPtr api, ref CThostFtdcQryForQuoteField pQryForQuote, int nRequestID);

		/// <summary>
		///请求查询报价
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryQuote(IntPtr api, ref CThostFtdcQryQuoteField pQryQuote, int nRequestID);

		/// <summary>
		///请求查询期权自对冲
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionSelfClose(IntPtr api, ref CThostFtdcQryOptionSelfCloseField pQryOptionSelfClose, int nRequestID);

		/// <summary>
		///请求查询投资单元
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestUnit(IntPtr api, ref CThostFtdcQryInvestUnitField pQryInvestUnit, int nRequestID);

		/// <summary>
		///请求查询组合合约安全系数
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCombInstrumentGuard(IntPtr api, ref CThostFtdcQryCombInstrumentGuardField pQryCombInstrumentGuard, int nRequestID);

		/// <summary>
		///请求查询申请组合
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCombAction(IntPtr api, ref CThostFtdcQryCombActionField pQryCombAction, int nRequestID);

		/// <summary>
		///请求查询转帐流水
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTransferSerial(IntPtr api, ref CThostFtdcQryTransferSerialField pQryTransferSerial, int nRequestID);

		/// <summary>
		///请求查询银期签约关系
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryAccountregister(IntPtr api, ref CThostFtdcQryAccountregisterField pQryAccountregister, int nRequestID);

		/// <summary>
		///请求查询签约银行
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryContractBank(IntPtr api, ref CThostFtdcQryContractBankField pQryContractBank, int nRequestID);

		/// <summary>
		///请求查询预埋单
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryParkedOrder(IntPtr api, ref CThostFtdcQryParkedOrderField pQryParkedOrder, int nRequestID);

		/// <summary>
		///请求查询预埋撤单
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryParkedOrderAction(IntPtr api, ref CThostFtdcQryParkedOrderActionField pQryParkedOrderAction, int nRequestID);

		/// <summary>
		///请求查询交易通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingNotice(IntPtr api, ref CThostFtdcQryTradingNoticeField pQryTradingNotice, int nRequestID);

		/// <summary>
		///请求查询经纪公司交易参数
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryBrokerTradingParams(IntPtr api, ref CThostFtdcQryBrokerTradingParamsField pQryBrokerTradingParams, int nRequestID);

		/// <summary>
		///请求查询经纪公司交易算法
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryBrokerTradingAlgos(IntPtr api, ref CThostFtdcQryBrokerTradingAlgosField pQryBrokerTradingAlgos, int nRequestID);

		/// <summary>
		///请求查询监控中心用户令牌
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQueryCFMMCTradingAccountToken(IntPtr api, ref CThostFtdcQueryCFMMCTradingAccountTokenField pQueryCFMMCTradingAccountToken, int nRequestID);

		/// <summary>
		///期货发起银行资金转期货请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqFromBankToFutureByFuture(IntPtr api, ref CThostFtdcReqTransferField pReqTransfer, int nRequestID);

		/// <summary>
		///期货发起期货资金转银行请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqFromFutureToBankByFuture(IntPtr api, ref CThostFtdcReqTransferField pReqTransfer, int nRequestID);

		/// <summary>
		///期货发起查询银行余额请求
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQueryBankAccountMoneyByFuture(IntPtr api, ref CThostFtdcReqQueryAccountField pReqQueryAccount, int nRequestID);
		/// <summary>
		///删除接口对象本身
		///@remark 不再使用本接口对象时,调用该函数删除接口对象
		/// </summary>
        public IntPtr Release()
        {
            return (Invoke(_handle, "Release", typeof(DeleRelease)) as DeleRelease)(_api);
        }
                    

		/// <summary>
		///初始化
		///@remark 初始化运行环境,只有调用后,接口才开始工作
		/// </summary>
        public IntPtr Init()
        {
            return (Invoke(_handle, "Init", typeof(DeleInit)) as DeleInit)(_api);
        }
                    

		/// <summary>
		///等待接口线程结束运行
		///@return 线程退出代码
		/// </summary>
        public IntPtr Join()
        {
            return (Invoke(_handle, "Join", typeof(DeleJoin)) as DeleJoin)(_api);
        }
                    

		/// <summary>
		///注册前置机网络地址
		///@param pszFrontAddress：前置机网络地址。
		///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。 
		///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
		/// </summary>
        public IntPtr RegisterFront(string pszFrontAddress)
        {
            return (Invoke(_handle, "RegisterFront", typeof(DeleRegisterFront)) as DeleRegisterFront)(_api, pszFrontAddress);
        }
                    

		/// <summary>
		///注册名字服务器网络地址
		///@param pszNsAddress：名字服务器网络地址。
		///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。 
		///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
		///@remark RegisterNameServer优先于RegisterFront
		/// </summary>
        public IntPtr RegisterNameServer(string pszNsAddress)
        {
            return (Invoke(_handle, "RegisterNameServer", typeof(DeleRegisterNameServer)) as DeleRegisterNameServer)(_api, pszNsAddress);
        }
                    

		/// <summary>
		///注册名字服务器用户信息
		///@param pFensUserInfo：用户信息。
		/// </summary>
        public IntPtr RegisterFensUserInfo(string BrokerID = "",string UserID = "",TThostFtdcLoginModeType LoginMode = TThostFtdcLoginModeType.THOST_FTDC_LM_Trade)
        {
			CThostFtdcFensUserInfoField pFensUserInfo = new CThostFtdcFensUserInfoField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				LoginMode = LoginMode,
			};
            return (Invoke(_handle, "RegisterFensUserInfo", typeof(DeleRegisterFensUserInfo)) as DeleRegisterFensUserInfo)(_api, ref pFensUserInfo);
        }
                    

		/// <summary>
		///注册回调接口
		///@param pSpi 派生自回调接口类的实例
		/// </summary>
        public IntPtr RegisterSpi(IntPtr pSpi)
        {
            return (Invoke(_handle, "RegisterSpi", typeof(DeleRegisterSpi)) as DeleRegisterSpi)(_api, pSpi);
        }
                    

		/// <summary>
		///订阅私有流。
		///@param nResumeType 私有流重传方式  
		///        THOST_TERT_RESTART:从本交易日开始重传
		///        THOST_TERT_RESUME:从上次收到的续传
		///        THOST_TERT_QUICK:只传送登录后私有流的内容
		///@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
		/// </summary>
        public IntPtr SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePrivateTopic", typeof(DeleSubscribePrivateTopic)) as DeleSubscribePrivateTopic)(_api, nResumeType);
        }
                    

		/// <summary>
		///订阅公共流。
		///@param nResumeType 公共流重传方式  
		///        THOST_TERT_RESTART:从本交易日开始重传
		///        THOST_TERT_RESUME:从上次收到的续传
		///        THOST_TERT_QUICK:只传送登录后公共流的内容
		///@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
		/// </summary>
        public IntPtr SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePublicTopic", typeof(DeleSubscribePublicTopic)) as DeleSubscribePublicTopic)(_api, nResumeType);
        }
                    

		/// <summary>
		///客户端认证请求
		/// </summary>
        public IntPtr ReqAuthenticate(string BrokerID = "",string UserID = "",string UserProductInfo = "",string AuthCode = "",string AppID = "")
        {
			CThostFtdcReqAuthenticateField pReqAuthenticateField = new CThostFtdcReqAuthenticateField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				UserProductInfo = UserProductInfo,
				AuthCode = AuthCode,
				AppID = AppID,
			};
            return (Invoke(_handle, "ReqAuthenticate", typeof(DeleReqAuthenticate)) as DeleReqAuthenticate)(_api, ref pReqAuthenticateField, this.nRequestID++);
        }
                    

		/// <summary>
		///注册用户终端信息，用于中继服务器多连接模式
		///需要在终端认证成功后，用户登录前调用该接口
		/// </summary>
        public IntPtr RegisterUserSystemInfo(string BrokerID = "",string UserID = "",int ClientSystemInfoLen = 1,string ClientSystemInfo = "",string ClientPublicIP = "",int ClientIPPort = 1,string ClientLoginTime = "",string ClientAppID = "")
        {
			CThostFtdcUserSystemInfoField pUserSystemInfo = new CThostFtdcUserSystemInfoField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ClientSystemInfoLen = ClientSystemInfoLen,
				ClientSystemInfo = ClientSystemInfo,
				ClientPublicIP = ClientPublicIP,
				ClientIPPort = ClientIPPort,
				ClientLoginTime = ClientLoginTime,
				ClientAppID = ClientAppID,
			};
            return (Invoke(_handle, "RegisterUserSystemInfo", typeof(DeleRegisterUserSystemInfo)) as DeleRegisterUserSystemInfo)(_api, ref pUserSystemInfo);
        }
                    

		/// <summary>
		///上报用户终端信息，用于中继服务器操作员登录模式
		///操作员登录后，可以多次调用该接口上报客户信息
		/// </summary>
        public IntPtr SubmitUserSystemInfo(string BrokerID = "",string UserID = "",int ClientSystemInfoLen = 1,string ClientSystemInfo = "",string ClientPublicIP = "",int ClientIPPort = 1,string ClientLoginTime = "",string ClientAppID = "")
        {
			CThostFtdcUserSystemInfoField pUserSystemInfo = new CThostFtdcUserSystemInfoField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ClientSystemInfoLen = ClientSystemInfoLen,
				ClientSystemInfo = ClientSystemInfo,
				ClientPublicIP = ClientPublicIP,
				ClientIPPort = ClientIPPort,
				ClientLoginTime = ClientLoginTime,
				ClientAppID = ClientAppID,
			};
            return (Invoke(_handle, "SubmitUserSystemInfo", typeof(DeleSubmitUserSystemInfo)) as DeleSubmitUserSystemInfo)(_api, ref pUserSystemInfo);
        }
                    

		/// <summary>
		///用户登录请求
		/// </summary>
        public IntPtr ReqUserLogin(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string OneTimePassword = "",string ClientIPAddress = "",string LoginRemark = "",int ClientIPPort = 1)
        {
			CThostFtdcReqUserLoginField pReqUserLoginField = new CThostFtdcReqUserLoginField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
				Password = Password,
				UserProductInfo = UserProductInfo,
				InterfaceProductInfo = InterfaceProductInfo,
				ProtocolInfo = ProtocolInfo,
				MacAddress = MacAddress,
				OneTimePassword = OneTimePassword,
				ClientIPAddress = ClientIPAddress,
				LoginRemark = LoginRemark,
				ClientIPPort = ClientIPPort,
			};
            return (Invoke(_handle, "ReqUserLogin", typeof(DeleReqUserLogin)) as DeleReqUserLogin)(_api, ref pReqUserLoginField, this.nRequestID++);
        }
                    

		/// <summary>
		///登出请求
		/// </summary>
        public IntPtr ReqUserLogout(string BrokerID = "",string UserID = "")
        {
			CThostFtdcUserLogoutField pUserLogout = new CThostFtdcUserLogoutField
			{
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqUserLogout", typeof(DeleReqUserLogout)) as DeleReqUserLogout)(_api, ref pUserLogout, this.nRequestID++);
        }
                    

		/// <summary>
		///用户口令更新请求
		/// </summary>
        public IntPtr ReqUserPasswordUpdate(string BrokerID = "",string UserID = "",string OldPassword = "",string NewPassword = "")
        {
			CThostFtdcUserPasswordUpdateField pUserPasswordUpdate = new CThostFtdcUserPasswordUpdateField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				OldPassword = OldPassword,
				NewPassword = NewPassword,
			};
            return (Invoke(_handle, "ReqUserPasswordUpdate", typeof(DeleReqUserPasswordUpdate)) as DeleReqUserPasswordUpdate)(_api, ref pUserPasswordUpdate, this.nRequestID++);
        }
                    

		/// <summary>
		///资金账户口令更新请求
		/// </summary>
        public IntPtr ReqTradingAccountPasswordUpdate(string BrokerID = "",string AccountID = "",string OldPassword = "",string NewPassword = "",string CurrencyID = "")
        {
			CThostFtdcTradingAccountPasswordUpdateField pTradingAccountPasswordUpdate = new CThostFtdcTradingAccountPasswordUpdateField
			{
				BrokerID = BrokerID,
				AccountID = AccountID,
				OldPassword = OldPassword,
				NewPassword = NewPassword,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqTradingAccountPasswordUpdate", typeof(DeleReqTradingAccountPasswordUpdate)) as DeleReqTradingAccountPasswordUpdate)(_api, ref pTradingAccountPasswordUpdate, this.nRequestID++);
        }
                    

		/// <summary>
		///查询用户当前支持的认证模式
		/// </summary>
        public IntPtr ReqUserAuthMethod(string TradingDay = "",string BrokerID = "",string UserID = "")
        {
			CThostFtdcReqUserAuthMethodField pReqUserAuthMethod = new CThostFtdcReqUserAuthMethodField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqUserAuthMethod", typeof(DeleReqUserAuthMethod)) as DeleReqUserAuthMethod)(_api, ref pReqUserAuthMethod, this.nRequestID++);
        }
                    

		/// <summary>
		///用户发出获取图形验证码请求
		/// </summary>
        public IntPtr ReqGenUserCaptcha(string TradingDay = "",string BrokerID = "",string UserID = "")
        {
			CThostFtdcReqGenUserCaptchaField pReqGenUserCaptcha = new CThostFtdcReqGenUserCaptchaField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqGenUserCaptcha", typeof(DeleReqGenUserCaptcha)) as DeleReqGenUserCaptcha)(_api, ref pReqGenUserCaptcha, this.nRequestID++);
        }
                    

		/// <summary>
		///用户发出获取短信验证码请求
		/// </summary>
        public IntPtr ReqGenUserText(string TradingDay = "",string BrokerID = "",string UserID = "")
        {
			CThostFtdcReqGenUserTextField pReqGenUserText = new CThostFtdcReqGenUserTextField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqGenUserText", typeof(DeleReqGenUserText)) as DeleReqGenUserText)(_api, ref pReqGenUserText, this.nRequestID++);
        }
                    

		/// <summary>
		///用户发出带有图片验证码的登陆请求
		/// </summary>
        public IntPtr ReqUserLoginWithCaptcha(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string ClientIPAddress = "",string LoginRemark = "",string Captcha = "",int ClientIPPort = 1)
        {
			CThostFtdcReqUserLoginWithCaptchaField pReqUserLoginWithCaptcha = new CThostFtdcReqUserLoginWithCaptchaField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
				Password = Password,
				UserProductInfo = UserProductInfo,
				InterfaceProductInfo = InterfaceProductInfo,
				ProtocolInfo = ProtocolInfo,
				MacAddress = MacAddress,
				ClientIPAddress = ClientIPAddress,
				LoginRemark = LoginRemark,
				Captcha = Captcha,
				ClientIPPort = ClientIPPort,
			};
            return (Invoke(_handle, "ReqUserLoginWithCaptcha", typeof(DeleReqUserLoginWithCaptcha)) as DeleReqUserLoginWithCaptcha)(_api, ref pReqUserLoginWithCaptcha, this.nRequestID++);
        }
                    

		/// <summary>
		///用户发出带有短信验证码的登陆请求
		/// </summary>
        public IntPtr ReqUserLoginWithText(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string ClientIPAddress = "",string LoginRemark = "",string Text = "",int ClientIPPort = 1)
        {
			CThostFtdcReqUserLoginWithTextField pReqUserLoginWithText = new CThostFtdcReqUserLoginWithTextField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
				Password = Password,
				UserProductInfo = UserProductInfo,
				InterfaceProductInfo = InterfaceProductInfo,
				ProtocolInfo = ProtocolInfo,
				MacAddress = MacAddress,
				ClientIPAddress = ClientIPAddress,
				LoginRemark = LoginRemark,
				Text = Text,
				ClientIPPort = ClientIPPort,
			};
            return (Invoke(_handle, "ReqUserLoginWithText", typeof(DeleReqUserLoginWithText)) as DeleReqUserLoginWithText)(_api, ref pReqUserLoginWithText, this.nRequestID++);
        }
                    

		/// <summary>
		///用户发出带有动态口令的登陆请求
		/// </summary>
        public IntPtr ReqUserLoginWithOTP(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string ClientIPAddress = "",string LoginRemark = "",string OTPPassword = "",int ClientIPPort = 1)
        {
			CThostFtdcReqUserLoginWithOTPField pReqUserLoginWithOTP = new CThostFtdcReqUserLoginWithOTPField
			{
				TradingDay = TradingDay,
				BrokerID = BrokerID,
				UserID = UserID,
				Password = Password,
				UserProductInfo = UserProductInfo,
				InterfaceProductInfo = InterfaceProductInfo,
				ProtocolInfo = ProtocolInfo,
				MacAddress = MacAddress,
				ClientIPAddress = ClientIPAddress,
				LoginRemark = LoginRemark,
				OTPPassword = OTPPassword,
				ClientIPPort = ClientIPPort,
			};
            return (Invoke(_handle, "ReqUserLoginWithOTP", typeof(DeleReqUserLoginWithOTP)) as DeleReqUserLoginWithOTP)(_api, ref pReqUserLoginWithOTP, this.nRequestID++);
        }
                    

		/// <summary>
		///报单录入请求
		/// </summary>
        public IntPtr ReqOrderInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string OrderRef = "",string UserID = "",TThostFtdcOrderPriceTypeType OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice,TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,string CombOffsetFlag = "",string CombHedgeFlag = "",double LimitPrice = 0.0,int VolumeTotalOriginal = 1,TThostFtdcTimeConditionType TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC,string GTDDate = "",TThostFtdcVolumeConditionType VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV,int MinVolume = 1,TThostFtdcContingentConditionType ContingentCondition = TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,double StopPrice = 0.0,TThostFtdcForceCloseReasonType ForceCloseReason = TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,int IsAutoSuspend = 1,string BusinessUnit = "",int RequestID = 1,int UserForceClose = 1,int IsSwapOrder = 1,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputOrderField pInputOrder = new CThostFtdcInputOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				OrderRef = OrderRef,
				UserID = UserID,
				OrderPriceType = OrderPriceType,
				Direction = Direction,
				CombOffsetFlag = CombOffsetFlag,
				CombHedgeFlag = CombHedgeFlag,
				LimitPrice = LimitPrice,
				VolumeTotalOriginal = VolumeTotalOriginal,
				TimeCondition = TimeCondition,
				GTDDate = GTDDate,
				VolumeCondition = VolumeCondition,
				MinVolume = MinVolume,
				ContingentCondition = ContingentCondition,
				StopPrice = StopPrice,
				ForceCloseReason = ForceCloseReason,
				IsAutoSuspend = IsAutoSuspend,
				BusinessUnit = BusinessUnit,
				RequestID = RequestID,
				UserForceClose = UserForceClose,
				IsSwapOrder = IsSwapOrder,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
				ClientID = ClientID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqOrderInsert", typeof(DeleReqOrderInsert)) as DeleReqOrderInsert)(_api, ref pInputOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///预埋单录入请求
		/// </summary>
        public IntPtr ReqParkedOrderInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string OrderRef = "",string UserID = "",TThostFtdcOrderPriceTypeType OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice,TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,string CombOffsetFlag = "",string CombHedgeFlag = "",double LimitPrice = 0.0,int VolumeTotalOriginal = 1,TThostFtdcTimeConditionType TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC,string GTDDate = "",TThostFtdcVolumeConditionType VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV,int MinVolume = 1,TThostFtdcContingentConditionType ContingentCondition = TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,double StopPrice = 0.0,TThostFtdcForceCloseReasonType ForceCloseReason = TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,int IsAutoSuspend = 1,string BusinessUnit = "",int RequestID = 1,int UserForceClose = 1,string ExchangeID = "",string ParkedOrderID = "",TThostFtdcUserTypeType UserType = TThostFtdcUserTypeType.THOST_FTDC_UT_Investor,TThostFtdcParkedOrderStatusType Status = TThostFtdcParkedOrderStatusType.THOST_FTDC_PAOS_NotSend,int ErrorID = 1,string ErrorMsg = "",int IsSwapOrder = 1,string AccountID = "",string CurrencyID = "",string ClientID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcParkedOrderField pParkedOrder = new CThostFtdcParkedOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				OrderRef = OrderRef,
				UserID = UserID,
				OrderPriceType = OrderPriceType,
				Direction = Direction,
				CombOffsetFlag = CombOffsetFlag,
				CombHedgeFlag = CombHedgeFlag,
				LimitPrice = LimitPrice,
				VolumeTotalOriginal = VolumeTotalOriginal,
				TimeCondition = TimeCondition,
				GTDDate = GTDDate,
				VolumeCondition = VolumeCondition,
				MinVolume = MinVolume,
				ContingentCondition = ContingentCondition,
				StopPrice = StopPrice,
				ForceCloseReason = ForceCloseReason,
				IsAutoSuspend = IsAutoSuspend,
				BusinessUnit = BusinessUnit,
				RequestID = RequestID,
				UserForceClose = UserForceClose,
				ExchangeID = ExchangeID,
				ParkedOrderID = ParkedOrderID,
				UserType = UserType,
				Status = Status,
				ErrorID = ErrorID,
				ErrorMsg = ErrorMsg,
				IsSwapOrder = IsSwapOrder,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
				ClientID = ClientID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqParkedOrderInsert", typeof(DeleReqParkedOrderInsert)) as DeleReqParkedOrderInsert)(_api, ref pParkedOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///预埋撤单录入请求
		/// </summary>
        public IntPtr ReqParkedOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 1,string OrderRef = "",int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string OrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,double LimitPrice = 0.0,int VolumeChange = 1,string UserID = "",string InstrumentID = "",string ParkedOrderActionID = "",TThostFtdcUserTypeType UserType = TThostFtdcUserTypeType.THOST_FTDC_UT_Investor,TThostFtdcParkedOrderStatusType Status = TThostFtdcParkedOrderStatusType.THOST_FTDC_PAOS_NotSend,int ErrorID = 1,string ErrorMsg = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcParkedOrderActionField pParkedOrderAction = new CThostFtdcParkedOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				OrderActionRef = OrderActionRef,
				OrderRef = OrderRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				ActionFlag = ActionFlag,
				LimitPrice = LimitPrice,
				VolumeChange = VolumeChange,
				UserID = UserID,
				InstrumentID = InstrumentID,
				ParkedOrderActionID = ParkedOrderActionID,
				UserType = UserType,
				Status = Status,
				ErrorID = ErrorID,
				ErrorMsg = ErrorMsg,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqParkedOrderAction", typeof(DeleReqParkedOrderAction)) as DeleReqParkedOrderAction)(_api, ref pParkedOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///报单操作请求
		/// </summary>
        public IntPtr ReqOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 1,string OrderRef = "",int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string OrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,double LimitPrice = 0.0,int VolumeChange = 1,string UserID = "",string InstrumentID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputOrderActionField pInputOrderAction = new CThostFtdcInputOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				OrderActionRef = OrderActionRef,
				OrderRef = OrderRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				ActionFlag = ActionFlag,
				LimitPrice = LimitPrice,
				VolumeChange = VolumeChange,
				UserID = UserID,
				InstrumentID = InstrumentID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqOrderAction", typeof(DeleReqOrderAction)) as DeleReqOrderAction)(_api, ref pInputOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///查询最大报单数量请求
		/// </summary>
        public IntPtr ReqQueryMaxOrderVolume(string BrokerID = "",string InvestorID = "",string InstrumentID = "",TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,TThostFtdcOffsetFlagType OffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,int MaxVolume = 1,string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQueryMaxOrderVolumeField pQueryMaxOrderVolume = new CThostFtdcQueryMaxOrderVolumeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				Direction = Direction,
				OffsetFlag = OffsetFlag,
				HedgeFlag = HedgeFlag,
				MaxVolume = MaxVolume,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQueryMaxOrderVolume", typeof(DeleReqQueryMaxOrderVolume)) as DeleReqQueryMaxOrderVolume)(_api, ref pQueryMaxOrderVolume, this.nRequestID++);
        }
                    

		/// <summary>
		///投资者结算结果确认
		/// </summary>
        public IntPtr ReqSettlementInfoConfirm(string BrokerID = "",string InvestorID = "",string ConfirmDate = "",string ConfirmTime = "",int SettlementID = 1,string AccountID = "",string CurrencyID = "")
        {
			CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm = new CThostFtdcSettlementInfoConfirmField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ConfirmDate = ConfirmDate,
				ConfirmTime = ConfirmTime,
				SettlementID = SettlementID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqSettlementInfoConfirm", typeof(DeleReqSettlementInfoConfirm)) as DeleReqSettlementInfoConfirm)(_api, ref pSettlementInfoConfirm, this.nRequestID++);
        }
                    

		/// <summary>
		///请求删除预埋单
		/// </summary>
        public IntPtr ReqRemoveParkedOrder(string BrokerID = "",string InvestorID = "",string ParkedOrderID = "",string InvestUnitID = "")
        {
			CThostFtdcRemoveParkedOrderField pRemoveParkedOrder = new CThostFtdcRemoveParkedOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ParkedOrderID = ParkedOrderID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqRemoveParkedOrder", typeof(DeleReqRemoveParkedOrder)) as DeleReqRemoveParkedOrder)(_api, ref pRemoveParkedOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///请求删除预埋撤单
		/// </summary>
        public IntPtr ReqRemoveParkedOrderAction(string BrokerID = "",string InvestorID = "",string ParkedOrderActionID = "",string InvestUnitID = "")
        {
			CThostFtdcRemoveParkedOrderActionField pRemoveParkedOrderAction = new CThostFtdcRemoveParkedOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ParkedOrderActionID = ParkedOrderActionID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqRemoveParkedOrderAction", typeof(DeleReqRemoveParkedOrderAction)) as DeleReqRemoveParkedOrderAction)(_api, ref pRemoveParkedOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///执行宣告录入请求
		/// </summary>
        public IntPtr ReqExecOrderInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExecOrderRef = "",string UserID = "",int Volume = 1,int RequestID = 1,string BusinessUnit = "",TThostFtdcOffsetFlagType OffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcActionTypeType ActionType = TThostFtdcActionTypeType.THOST_FTDC_ACTP_Exec,TThostFtdcPosiDirectionType PosiDirection = TThostFtdcPosiDirectionType.THOST_FTDC_PD_Net,TThostFtdcExecOrderPositionFlagType ReservePositionFlag = TThostFtdcExecOrderPositionFlagType.THOST_FTDC_EOPF_Reserve,TThostFtdcExecOrderCloseFlagType CloseFlag = TThostFtdcExecOrderCloseFlagType.THOST_FTDC_EOCF_AutoClose,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputExecOrderField pInputExecOrder = new CThostFtdcInputExecOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExecOrderRef = ExecOrderRef,
				UserID = UserID,
				Volume = Volume,
				RequestID = RequestID,
				BusinessUnit = BusinessUnit,
				OffsetFlag = OffsetFlag,
				HedgeFlag = HedgeFlag,
				ActionType = ActionType,
				PosiDirection = PosiDirection,
				ReservePositionFlag = ReservePositionFlag,
				CloseFlag = CloseFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
				ClientID = ClientID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqExecOrderInsert", typeof(DeleReqExecOrderInsert)) as DeleReqExecOrderInsert)(_api, ref pInputExecOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///执行宣告操作请求
		/// </summary>
        public IntPtr ReqExecOrderAction(string BrokerID = "",string InvestorID = "",int ExecOrderActionRef = 1,string ExecOrderRef = "",int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string ExecOrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string InstrumentID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputExecOrderActionField pInputExecOrderAction = new CThostFtdcInputExecOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ExecOrderActionRef = ExecOrderActionRef,
				ExecOrderRef = ExecOrderRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				ExecOrderSysID = ExecOrderSysID,
				ActionFlag = ActionFlag,
				UserID = UserID,
				InstrumentID = InstrumentID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqExecOrderAction", typeof(DeleReqExecOrderAction)) as DeleReqExecOrderAction)(_api, ref pInputExecOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///询价录入请求
		/// </summary>
        public IntPtr ReqForQuoteInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ForQuoteRef = "",string UserID = "",string ExchangeID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputForQuoteField pInputForQuote = new CThostFtdcInputForQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ForQuoteRef = ForQuoteRef,
				UserID = UserID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqForQuoteInsert", typeof(DeleReqForQuoteInsert)) as DeleReqForQuoteInsert)(_api, ref pInputForQuote, this.nRequestID++);
        }
                    

		/// <summary>
		///报价录入请求
		/// </summary>
        public IntPtr ReqQuoteInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string QuoteRef = "",string UserID = "",double AskPrice = 0.0,double BidPrice = 0.0,int AskVolume = 1,int BidVolume = 1,int RequestID = 1,string BusinessUnit = "",TThostFtdcOffsetFlagType AskOffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcOffsetFlagType BidOffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType AskHedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcHedgeFlagType BidHedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string AskOrderRef = "",string BidOrderRef = "",string ForQuoteSysID = "",string ExchangeID = "",string InvestUnitID = "",string ClientID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputQuoteField pInputQuote = new CThostFtdcInputQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				QuoteRef = QuoteRef,
				UserID = UserID,
				AskPrice = AskPrice,
				BidPrice = BidPrice,
				AskVolume = AskVolume,
				BidVolume = BidVolume,
				RequestID = RequestID,
				BusinessUnit = BusinessUnit,
				AskOffsetFlag = AskOffsetFlag,
				BidOffsetFlag = BidOffsetFlag,
				AskHedgeFlag = AskHedgeFlag,
				BidHedgeFlag = BidHedgeFlag,
				AskOrderRef = AskOrderRef,
				BidOrderRef = BidOrderRef,
				ForQuoteSysID = ForQuoteSysID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				ClientID = ClientID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqQuoteInsert", typeof(DeleReqQuoteInsert)) as DeleReqQuoteInsert)(_api, ref pInputQuote, this.nRequestID++);
        }
                    

		/// <summary>
		///报价操作请求
		/// </summary>
        public IntPtr ReqQuoteAction(string BrokerID = "",string InvestorID = "",int QuoteActionRef = 1,string QuoteRef = "",int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string QuoteSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string InstrumentID = "",string InvestUnitID = "",string ClientID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputQuoteActionField pInputQuoteAction = new CThostFtdcInputQuoteActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				QuoteActionRef = QuoteActionRef,
				QuoteRef = QuoteRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				QuoteSysID = QuoteSysID,
				ActionFlag = ActionFlag,
				UserID = UserID,
				InstrumentID = InstrumentID,
				InvestUnitID = InvestUnitID,
				ClientID = ClientID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqQuoteAction", typeof(DeleReqQuoteAction)) as DeleReqQuoteAction)(_api, ref pInputQuoteAction, this.nRequestID++);
        }
                    

		/// <summary>
		///批量报单操作请求
		/// </summary>
        public IntPtr ReqBatchOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 1,int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string UserID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputBatchOrderActionField pInputBatchOrderAction = new CThostFtdcInputBatchOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				OrderActionRef = OrderActionRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				UserID = UserID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqBatchOrderAction", typeof(DeleReqBatchOrderAction)) as DeleReqBatchOrderAction)(_api, ref pInputBatchOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///期权自对冲录入请求
		/// </summary>
        public IntPtr ReqOptionSelfCloseInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string OptionSelfCloseRef = "",string UserID = "",int Volume = 1,int RequestID = 1,string BusinessUnit = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag = TThostFtdcOptSelfCloseFlagType.THOST_FTDC_OSCF_CloseSelfOptionPosition,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose = new CThostFtdcInputOptionSelfCloseField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				OptionSelfCloseRef = OptionSelfCloseRef,
				UserID = UserID,
				Volume = Volume,
				RequestID = RequestID,
				BusinessUnit = BusinessUnit,
				HedgeFlag = HedgeFlag,
				OptSelfCloseFlag = OptSelfCloseFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
				ClientID = ClientID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqOptionSelfCloseInsert", typeof(DeleReqOptionSelfCloseInsert)) as DeleReqOptionSelfCloseInsert)(_api, ref pInputOptionSelfClose, this.nRequestID++);
        }
                    

		/// <summary>
		///期权自对冲操作请求
		/// </summary>
        public IntPtr ReqOptionSelfCloseAction(string BrokerID = "",string InvestorID = "",int OptionSelfCloseActionRef = 1,string OptionSelfCloseRef = "",int RequestID = 1,int FrontID = 1,int SessionID = 1,string ExchangeID = "",string OptionSelfCloseSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string InstrumentID = "",string InvestUnitID = "",string IPAddress = "",string MacAddress = "")
        {
			CThostFtdcInputOptionSelfCloseActionField pInputOptionSelfCloseAction = new CThostFtdcInputOptionSelfCloseActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				OptionSelfCloseActionRef = OptionSelfCloseActionRef,
				OptionSelfCloseRef = OptionSelfCloseRef,
				RequestID = RequestID,
				FrontID = FrontID,
				SessionID = SessionID,
				ExchangeID = ExchangeID,
				OptionSelfCloseSysID = OptionSelfCloseSysID,
				ActionFlag = ActionFlag,
				UserID = UserID,
				InstrumentID = InstrumentID,
				InvestUnitID = InvestUnitID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
			};
            return (Invoke(_handle, "ReqOptionSelfCloseAction", typeof(DeleReqOptionSelfCloseAction)) as DeleReqOptionSelfCloseAction)(_api, ref pInputOptionSelfCloseAction, this.nRequestID++);
        }
                    

		/// <summary>
		///申请组合录入请求
		/// </summary>
        public IntPtr ReqCombActionInsert(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string CombActionRef = "",string UserID = "",TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,int Volume = 1,TThostFtdcCombDirectionType CombDirection = TThostFtdcCombDirectionType.THOST_FTDC_CMDR_Comb,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string IPAddress = "",string MacAddress = "",string InvestUnitID = "")
        {
			CThostFtdcInputCombActionField pInputCombAction = new CThostFtdcInputCombActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				CombActionRef = CombActionRef,
				UserID = UserID,
				Direction = Direction,
				Volume = Volume,
				CombDirection = CombDirection,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqCombActionInsert", typeof(DeleReqCombActionInsert)) as DeleReqCombActionInsert)(_api, ref pInputCombAction, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询报单
		/// </summary>
        public IntPtr ReqQryOrder(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string OrderSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "")
        {
			CThostFtdcQryOrderField pQryOrder = new CThostFtdcQryOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryOrder", typeof(DeleReqQryOrder)) as DeleReqQryOrder)(_api, ref pQryOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询成交
		/// </summary>
        public IntPtr ReqQryTrade(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string TradeID = "",string TradeTimeStart = "",string TradeTimeEnd = "",string InvestUnitID = "")
        {
			CThostFtdcQryTradeField pQryTrade = new CThostFtdcQryTradeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				TradeID = TradeID,
				TradeTimeStart = TradeTimeStart,
				TradeTimeEnd = TradeTimeEnd,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryTrade", typeof(DeleReqQryTrade)) as DeleReqQryTrade)(_api, ref pQryTrade, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者持仓
		/// </summary>
        public IntPtr ReqQryInvestorPosition(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInvestorPositionField pQryInvestorPosition = new CThostFtdcQryInvestorPositionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInvestorPosition", typeof(DeleReqQryInvestorPosition)) as DeleReqQryInvestorPosition)(_api, ref pQryInvestorPosition, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询资金账户
		/// </summary>
        public IntPtr ReqQryTradingAccount(string BrokerID = "",string InvestorID = "",string CurrencyID = "",TThostFtdcBizTypeType BizType = TThostFtdcBizTypeType.THOST_FTDC_BZTP_Future,string AccountID = "")
        {
			CThostFtdcQryTradingAccountField pQryTradingAccount = new CThostFtdcQryTradingAccountField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				CurrencyID = CurrencyID,
				BizType = BizType,
				AccountID = AccountID,
			};
            return (Invoke(_handle, "ReqQryTradingAccount", typeof(DeleReqQryTradingAccount)) as DeleReqQryTradingAccount)(_api, ref pQryTradingAccount, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者
		/// </summary>
        public IntPtr ReqQryInvestor(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQryInvestorField pQryInvestor = new CThostFtdcQryInvestorField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQryInvestor", typeof(DeleReqQryInvestor)) as DeleReqQryInvestor)(_api, ref pQryInvestor, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询交易编码
		/// </summary>
        public IntPtr ReqQryTradingCode(string BrokerID = "",string InvestorID = "",string ExchangeID = "",string ClientID = "",TThostFtdcClientIDTypeType ClientIDType = TThostFtdcClientIDTypeType.THOST_FTDC_CIDT_Speculation,string InvestUnitID = "")
        {
			CThostFtdcQryTradingCodeField pQryTradingCode = new CThostFtdcQryTradingCodeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				ClientID = ClientID,
				ClientIDType = ClientIDType,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryTradingCode", typeof(DeleReqQryTradingCode)) as DeleReqQryTradingCode)(_api, ref pQryTradingCode, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询合约保证金率
		/// </summary>
        public IntPtr ReqQryInstrumentMarginRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInstrumentMarginRateField pQryInstrumentMarginRate = new CThostFtdcQryInstrumentMarginRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInstrumentMarginRate", typeof(DeleReqQryInstrumentMarginRate)) as DeleReqQryInstrumentMarginRate)(_api, ref pQryInstrumentMarginRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询合约手续费率
		/// </summary>
        public IntPtr ReqQryInstrumentCommissionRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInstrumentCommissionRateField pQryInstrumentCommissionRate = new CThostFtdcQryInstrumentCommissionRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInstrumentCommissionRate", typeof(DeleReqQryInstrumentCommissionRate)) as DeleReqQryInstrumentCommissionRate)(_api, ref pQryInstrumentCommissionRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询交易所
		/// </summary>
        public IntPtr ReqQryExchange(string ExchangeID = "")
        {
			CThostFtdcQryExchangeField pQryExchange = new CThostFtdcQryExchangeField
			{
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryExchange", typeof(DeleReqQryExchange)) as DeleReqQryExchange)(_api, ref pQryExchange, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询产品
		/// </summary>
        public IntPtr ReqQryProduct(string ProductID = "",TThostFtdcProductClassType ProductClass = TThostFtdcProductClassType.THOST_FTDC_PC_Futures,string ExchangeID = "")
        {
			CThostFtdcQryProductField pQryProduct = new CThostFtdcQryProductField
			{
				ProductID = ProductID,
				ProductClass = ProductClass,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryProduct", typeof(DeleReqQryProduct)) as DeleReqQryProduct)(_api, ref pQryProduct, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询合约
		/// </summary>
        public IntPtr ReqQryInstrument(string InstrumentID = "",string ExchangeID = "",string ExchangeInstID = "",string ProductID = "")
        {
			CThostFtdcQryInstrumentField pQryInstrument = new CThostFtdcQryInstrumentField
			{
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				ExchangeInstID = ExchangeInstID,
				ProductID = ProductID,
			};
            return (Invoke(_handle, "ReqQryInstrument", typeof(DeleReqQryInstrument)) as DeleReqQryInstrument)(_api, ref pQryInstrument, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询行情
		/// </summary>
        public IntPtr ReqQryDepthMarketData(string InstrumentID = "",string ExchangeID = "")
        {
			CThostFtdcQryDepthMarketDataField pQryDepthMarketData = new CThostFtdcQryDepthMarketDataField
			{
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryDepthMarketData", typeof(DeleReqQryDepthMarketData)) as DeleReqQryDepthMarketData)(_api, ref pQryDepthMarketData, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者结算结果
		/// </summary>
        public IntPtr ReqQrySettlementInfo(string BrokerID = "",string InvestorID = "",string TradingDay = "",string AccountID = "",string CurrencyID = "")
        {
			CThostFtdcQrySettlementInfoField pQrySettlementInfo = new CThostFtdcQrySettlementInfoField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				TradingDay = TradingDay,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqQrySettlementInfo", typeof(DeleReqQrySettlementInfo)) as DeleReqQrySettlementInfo)(_api, ref pQrySettlementInfo, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询转帐银行
		/// </summary>
        public IntPtr ReqQryTransferBank(string BankID = "",string BankBrchID = "")
        {
			CThostFtdcQryTransferBankField pQryTransferBank = new CThostFtdcQryTransferBankField
			{
				BankID = BankID,
				BankBrchID = BankBrchID,
			};
            return (Invoke(_handle, "ReqQryTransferBank", typeof(DeleReqQryTransferBank)) as DeleReqQryTransferBank)(_api, ref pQryTransferBank, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者持仓明细
		/// </summary>
        public IntPtr ReqQryInvestorPositionDetail(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInvestorPositionDetailField pQryInvestorPositionDetail = new CThostFtdcQryInvestorPositionDetailField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInvestorPositionDetail", typeof(DeleReqQryInvestorPositionDetail)) as DeleReqQryInvestorPositionDetail)(_api, ref pQryInvestorPositionDetail, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询客户通知
		/// </summary>
        public IntPtr ReqQryNotice(string BrokerID = "")
        {
			CThostFtdcQryNoticeField pQryNotice = new CThostFtdcQryNoticeField
			{
				BrokerID = BrokerID,
			};
            return (Invoke(_handle, "ReqQryNotice", typeof(DeleReqQryNotice)) as DeleReqQryNotice)(_api, ref pQryNotice, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询结算信息确认
		/// </summary>
        public IntPtr ReqQrySettlementInfoConfirm(string BrokerID = "",string InvestorID = "",string AccountID = "",string CurrencyID = "")
        {
			CThostFtdcQrySettlementInfoConfirmField pQrySettlementInfoConfirm = new CThostFtdcQrySettlementInfoConfirmField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqQrySettlementInfoConfirm", typeof(DeleReqQrySettlementInfoConfirm)) as DeleReqQrySettlementInfoConfirm)(_api, ref pQrySettlementInfoConfirm, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者持仓明细
		/// </summary>
        public IntPtr ReqQryInvestorPositionCombineDetail(string BrokerID = "",string InvestorID = "",string CombInstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInvestorPositionCombineDetailField pQryInvestorPositionCombineDetail = new CThostFtdcQryInvestorPositionCombineDetailField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				CombInstrumentID = CombInstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInvestorPositionCombineDetail", typeof(DeleReqQryInvestorPositionCombineDetail)) as DeleReqQryInvestorPositionCombineDetail)(_api, ref pQryInvestorPositionCombineDetail, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询保证金监管系统经纪公司资金账户密钥
		/// </summary>
        public IntPtr ReqQryCFMMCTradingAccountKey(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQryCFMMCTradingAccountKeyField pQryCFMMCTradingAccountKey = new CThostFtdcQryCFMMCTradingAccountKeyField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQryCFMMCTradingAccountKey", typeof(DeleReqQryCFMMCTradingAccountKey)) as DeleReqQryCFMMCTradingAccountKey)(_api, ref pQryCFMMCTradingAccountKey, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询仓单折抵信息
		/// </summary>
        public IntPtr ReqQryEWarrantOffset(string BrokerID = "",string InvestorID = "",string ExchangeID = "",string InstrumentID = "",string InvestUnitID = "")
        {
			CThostFtdcQryEWarrantOffsetField pQryEWarrantOffset = new CThostFtdcQryEWarrantOffsetField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryEWarrantOffset", typeof(DeleReqQryEWarrantOffset)) as DeleReqQryEWarrantOffset)(_api, ref pQryEWarrantOffset, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资者品种/跨品种保证金
		/// </summary>
        public IntPtr ReqQryInvestorProductGroupMargin(string BrokerID = "",string InvestorID = "",string ProductGroupID = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInvestorProductGroupMarginField pQryInvestorProductGroupMargin = new CThostFtdcQryInvestorProductGroupMarginField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ProductGroupID = ProductGroupID,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInvestorProductGroupMargin", typeof(DeleReqQryInvestorProductGroupMargin)) as DeleReqQryInvestorProductGroupMargin)(_api, ref pQryInvestorProductGroupMargin, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询交易所保证金率
		/// </summary>
        public IntPtr ReqQryExchangeMarginRate(string BrokerID = "",string InstrumentID = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "")
        {
			CThostFtdcQryExchangeMarginRateField pQryExchangeMarginRate = new CThostFtdcQryExchangeMarginRateField
			{
				BrokerID = BrokerID,
				InstrumentID = InstrumentID,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryExchangeMarginRate", typeof(DeleReqQryExchangeMarginRate)) as DeleReqQryExchangeMarginRate)(_api, ref pQryExchangeMarginRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询交易所调整保证金率
		/// </summary>
        public IntPtr ReqQryExchangeMarginRateAdjust(string BrokerID = "",string InstrumentID = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation)
        {
			CThostFtdcQryExchangeMarginRateAdjustField pQryExchangeMarginRateAdjust = new CThostFtdcQryExchangeMarginRateAdjustField
			{
				BrokerID = BrokerID,
				InstrumentID = InstrumentID,
				HedgeFlag = HedgeFlag,
			};
            return (Invoke(_handle, "ReqQryExchangeMarginRateAdjust", typeof(DeleReqQryExchangeMarginRateAdjust)) as DeleReqQryExchangeMarginRateAdjust)(_api, ref pQryExchangeMarginRateAdjust, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询汇率
		/// </summary>
        public IntPtr ReqQryExchangeRate(string BrokerID = "",string FromCurrencyID = "",string ToCurrencyID = "")
        {
			CThostFtdcQryExchangeRateField pQryExchangeRate = new CThostFtdcQryExchangeRateField
			{
				BrokerID = BrokerID,
				FromCurrencyID = FromCurrencyID,
				ToCurrencyID = ToCurrencyID,
			};
            return (Invoke(_handle, "ReqQryExchangeRate", typeof(DeleReqQryExchangeRate)) as DeleReqQryExchangeRate)(_api, ref pQryExchangeRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询二级代理操作员银期权限
		/// </summary>
        public IntPtr ReqQrySecAgentACIDMap(string BrokerID = "",string UserID = "",string AccountID = "",string CurrencyID = "")
        {
			CThostFtdcQrySecAgentACIDMapField pQrySecAgentACIDMap = new CThostFtdcQrySecAgentACIDMapField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				AccountID = AccountID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqQrySecAgentACIDMap", typeof(DeleReqQrySecAgentACIDMap)) as DeleReqQrySecAgentACIDMap)(_api, ref pQrySecAgentACIDMap, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询产品报价汇率
		/// </summary>
        public IntPtr ReqQryProductExchRate(string ProductID = "",string ExchangeID = "")
        {
			CThostFtdcQryProductExchRateField pQryProductExchRate = new CThostFtdcQryProductExchRateField
			{
				ProductID = ProductID,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryProductExchRate", typeof(DeleReqQryProductExchRate)) as DeleReqQryProductExchRate)(_api, ref pQryProductExchRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询产品组
		/// </summary>
        public IntPtr ReqQryProductGroup(string ProductID = "",string ExchangeID = "")
        {
			CThostFtdcQryProductGroupField pQryProductGroup = new CThostFtdcQryProductGroupField
			{
				ProductID = ProductID,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryProductGroup", typeof(DeleReqQryProductGroup)) as DeleReqQryProductGroup)(_api, ref pQryProductGroup, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询做市商合约手续费率
		/// </summary>
        public IntPtr ReqQryMMInstrumentCommissionRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "")
        {
			CThostFtdcQryMMInstrumentCommissionRateField pQryMMInstrumentCommissionRate = new CThostFtdcQryMMInstrumentCommissionRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryMMInstrumentCommissionRate", typeof(DeleReqQryMMInstrumentCommissionRate)) as DeleReqQryMMInstrumentCommissionRate)(_api, ref pQryMMInstrumentCommissionRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询做市商期权合约手续费
		/// </summary>
        public IntPtr ReqQryMMOptionInstrCommRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "")
        {
			CThostFtdcQryMMOptionInstrCommRateField pQryMMOptionInstrCommRate = new CThostFtdcQryMMOptionInstrCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryMMOptionInstrCommRate", typeof(DeleReqQryMMOptionInstrCommRate)) as DeleReqQryMMOptionInstrCommRate)(_api, ref pQryMMOptionInstrCommRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询报单手续费
		/// </summary>
        public IntPtr ReqQryInstrumentOrderCommRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "")
        {
			CThostFtdcQryInstrumentOrderCommRateField pQryInstrumentOrderCommRate = new CThostFtdcQryInstrumentOrderCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrumentOrderCommRate", typeof(DeleReqQryInstrumentOrderCommRate)) as DeleReqQryInstrumentOrderCommRate)(_api, ref pQryInstrumentOrderCommRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询资金账户
		/// </summary>
        public IntPtr ReqQrySecAgentTradingAccount(string BrokerID = "",string InvestorID = "",string CurrencyID = "",TThostFtdcBizTypeType BizType = TThostFtdcBizTypeType.THOST_FTDC_BZTP_Future,string AccountID = "")
        {
			CThostFtdcQryTradingAccountField pQryTradingAccount = new CThostFtdcQryTradingAccountField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				CurrencyID = CurrencyID,
				BizType = BizType,
				AccountID = AccountID,
			};
            return (Invoke(_handle, "ReqQrySecAgentTradingAccount", typeof(DeleReqQrySecAgentTradingAccount)) as DeleReqQrySecAgentTradingAccount)(_api, ref pQryTradingAccount, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询二级代理商资金校验模式
		/// </summary>
        public IntPtr ReqQrySecAgentCheckMode(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQrySecAgentCheckModeField pQrySecAgentCheckMode = new CThostFtdcQrySecAgentCheckModeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQrySecAgentCheckMode", typeof(DeleReqQrySecAgentCheckMode)) as DeleReqQrySecAgentCheckMode)(_api, ref pQrySecAgentCheckMode, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询二级代理商信息
		/// </summary>
        public IntPtr ReqQrySecAgentTradeInfo(string BrokerID = "",string BrokerSecAgentID = "")
        {
			CThostFtdcQrySecAgentTradeInfoField pQrySecAgentTradeInfo = new CThostFtdcQrySecAgentTradeInfoField
			{
				BrokerID = BrokerID,
				BrokerSecAgentID = BrokerSecAgentID,
			};
            return (Invoke(_handle, "ReqQrySecAgentTradeInfo", typeof(DeleReqQrySecAgentTradeInfo)) as DeleReqQrySecAgentTradeInfo)(_api, ref pQrySecAgentTradeInfo, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询期权交易成本
		/// </summary>
        public IntPtr ReqQryOptionInstrTradeCost(string BrokerID = "",string InvestorID = "",string InstrumentID = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,double InputPrice = 0.0,double UnderlyingPrice = 0.0,string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryOptionInstrTradeCostField pQryOptionInstrTradeCost = new CThostFtdcQryOptionInstrTradeCostField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				HedgeFlag = HedgeFlag,
				InputPrice = InputPrice,
				UnderlyingPrice = UnderlyingPrice,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryOptionInstrTradeCost", typeof(DeleReqQryOptionInstrTradeCost)) as DeleReqQryOptionInstrTradeCost)(_api, ref pQryOptionInstrTradeCost, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询期权合约手续费
		/// </summary>
        public IntPtr ReqQryOptionInstrCommRate(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryOptionInstrCommRateField pQryOptionInstrCommRate = new CThostFtdcQryOptionInstrCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryOptionInstrCommRate", typeof(DeleReqQryOptionInstrCommRate)) as DeleReqQryOptionInstrCommRate)(_api, ref pQryOptionInstrCommRate, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询执行宣告
		/// </summary>
        public IntPtr ReqQryExecOrder(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string ExecOrderSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "")
        {
			CThostFtdcQryExecOrderField pQryExecOrder = new CThostFtdcQryExecOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				ExecOrderSysID = ExecOrderSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
			};
            return (Invoke(_handle, "ReqQryExecOrder", typeof(DeleReqQryExecOrder)) as DeleReqQryExecOrder)(_api, ref pQryExecOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询询价
		/// </summary>
        public IntPtr ReqQryForQuote(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "")
        {
			CThostFtdcQryForQuoteField pQryForQuote = new CThostFtdcQryForQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryForQuote", typeof(DeleReqQryForQuote)) as DeleReqQryForQuote)(_api, ref pQryForQuote, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询报价
		/// </summary>
        public IntPtr ReqQryQuote(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string QuoteSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "")
        {
			CThostFtdcQryQuoteField pQryQuote = new CThostFtdcQryQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				QuoteSysID = QuoteSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryQuote", typeof(DeleReqQryQuote)) as DeleReqQryQuote)(_api, ref pQryQuote, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询期权自对冲
		/// </summary>
        public IntPtr ReqQryOptionSelfClose(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string OptionSelfCloseSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "")
        {
			CThostFtdcQryOptionSelfCloseField pQryOptionSelfClose = new CThostFtdcQryOptionSelfCloseField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				OptionSelfCloseSysID = OptionSelfCloseSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
			};
            return (Invoke(_handle, "ReqQryOptionSelfClose", typeof(DeleReqQryOptionSelfClose)) as DeleReqQryOptionSelfClose)(_api, ref pQryOptionSelfClose, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询投资单元
		/// </summary>
        public IntPtr ReqQryInvestUnit(string BrokerID = "",string InvestorID = "",string InvestUnitID = "")
        {
			CThostFtdcQryInvestUnitField pQryInvestUnit = new CThostFtdcQryInvestUnitField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryInvestUnit", typeof(DeleReqQryInvestUnit)) as DeleReqQryInvestUnit)(_api, ref pQryInvestUnit, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询组合合约安全系数
		/// </summary>
        public IntPtr ReqQryCombInstrumentGuard(string BrokerID = "",string InstrumentID = "",string ExchangeID = "")
        {
			CThostFtdcQryCombInstrumentGuardField pQryCombInstrumentGuard = new CThostFtdcQryCombInstrumentGuardField
			{
				BrokerID = BrokerID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryCombInstrumentGuard", typeof(DeleReqQryCombInstrumentGuard)) as DeleReqQryCombInstrumentGuard)(_api, ref pQryCombInstrumentGuard, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询申请组合
		/// </summary>
        public IntPtr ReqQryCombAction(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryCombActionField pQryCombAction = new CThostFtdcQryCombActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryCombAction", typeof(DeleReqQryCombAction)) as DeleReqQryCombAction)(_api, ref pQryCombAction, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询转帐流水
		/// </summary>
        public IntPtr ReqQryTransferSerial(string BrokerID = "",string AccountID = "",string BankID = "",string CurrencyID = "")
        {
			CThostFtdcQryTransferSerialField pQryTransferSerial = new CThostFtdcQryTransferSerialField
			{
				BrokerID = BrokerID,
				AccountID = AccountID,
				BankID = BankID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqQryTransferSerial", typeof(DeleReqQryTransferSerial)) as DeleReqQryTransferSerial)(_api, ref pQryTransferSerial, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询银期签约关系
		/// </summary>
        public IntPtr ReqQryAccountregister(string BrokerID = "",string AccountID = "",string BankID = "",string BankBranchID = "",string CurrencyID = "")
        {
			CThostFtdcQryAccountregisterField pQryAccountregister = new CThostFtdcQryAccountregisterField
			{
				BrokerID = BrokerID,
				AccountID = AccountID,
				BankID = BankID,
				BankBranchID = BankBranchID,
				CurrencyID = CurrencyID,
			};
            return (Invoke(_handle, "ReqQryAccountregister", typeof(DeleReqQryAccountregister)) as DeleReqQryAccountregister)(_api, ref pQryAccountregister, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询签约银行
		/// </summary>
        public IntPtr ReqQryContractBank(string BrokerID = "",string BankID = "",string BankBrchID = "")
        {
			CThostFtdcQryContractBankField pQryContractBank = new CThostFtdcQryContractBankField
			{
				BrokerID = BrokerID,
				BankID = BankID,
				BankBrchID = BankBrchID,
			};
            return (Invoke(_handle, "ReqQryContractBank", typeof(DeleReqQryContractBank)) as DeleReqQryContractBank)(_api, ref pQryContractBank, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询预埋单
		/// </summary>
        public IntPtr ReqQryParkedOrder(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryParkedOrderField pQryParkedOrder = new CThostFtdcQryParkedOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryParkedOrder", typeof(DeleReqQryParkedOrder)) as DeleReqQryParkedOrder)(_api, ref pQryParkedOrder, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询预埋撤单
		/// </summary>
        public IntPtr ReqQryParkedOrderAction(string BrokerID = "",string InvestorID = "",string InstrumentID = "",string ExchangeID = "",string InvestUnitID = "")
        {
			CThostFtdcQryParkedOrderActionField pQryParkedOrderAction = new CThostFtdcQryParkedOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryParkedOrderAction", typeof(DeleReqQryParkedOrderAction)) as DeleReqQryParkedOrderAction)(_api, ref pQryParkedOrderAction, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询交易通知
		/// </summary>
        public IntPtr ReqQryTradingNotice(string BrokerID = "",string InvestorID = "",string InvestUnitID = "")
        {
			CThostFtdcQryTradingNoticeField pQryTradingNotice = new CThostFtdcQryTradingNoticeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQryTradingNotice", typeof(DeleReqQryTradingNotice)) as DeleReqQryTradingNotice)(_api, ref pQryTradingNotice, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询经纪公司交易参数
		/// </summary>
        public IntPtr ReqQryBrokerTradingParams(string BrokerID = "",string InvestorID = "",string CurrencyID = "",string AccountID = "")
        {
			CThostFtdcQryBrokerTradingParamsField pQryBrokerTradingParams = new CThostFtdcQryBrokerTradingParamsField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				CurrencyID = CurrencyID,
				AccountID = AccountID,
			};
            return (Invoke(_handle, "ReqQryBrokerTradingParams", typeof(DeleReqQryBrokerTradingParams)) as DeleReqQryBrokerTradingParams)(_api, ref pQryBrokerTradingParams, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询经纪公司交易算法
		/// </summary>
        public IntPtr ReqQryBrokerTradingAlgos(string BrokerID = "",string ExchangeID = "",string InstrumentID = "")
        {
			CThostFtdcQryBrokerTradingAlgosField pQryBrokerTradingAlgos = new CThostFtdcQryBrokerTradingAlgosField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryBrokerTradingAlgos", typeof(DeleReqQryBrokerTradingAlgos)) as DeleReqQryBrokerTradingAlgos)(_api, ref pQryBrokerTradingAlgos, this.nRequestID++);
        }
                    

		/// <summary>
		///请求查询监控中心用户令牌
		/// </summary>
        public IntPtr ReqQueryCFMMCTradingAccountToken(string BrokerID = "",string InvestorID = "",string InvestUnitID = "")
        {
			CThostFtdcQueryCFMMCTradingAccountTokenField pQueryCFMMCTradingAccountToken = new CThostFtdcQueryCFMMCTradingAccountTokenField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				InvestUnitID = InvestUnitID,
			};
            return (Invoke(_handle, "ReqQueryCFMMCTradingAccountToken", typeof(DeleReqQueryCFMMCTradingAccountToken)) as DeleReqQueryCFMMCTradingAccountToken)(_api, ref pQueryCFMMCTradingAccountToken, this.nRequestID++);
        }
                    

		/// <summary>
		///期货发起银行资金转期货请求
		/// </summary>
        public IntPtr ReqFromBankToFutureByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 1,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 1,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int InstallID = 1,int FutureSerial = 1,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",double TradeAmount = 0.0,double FutureFetchAmount = 0.0,TThostFtdcFeePayFlagType FeePayFlag = TThostFtdcFeePayFlagType.THOST_FTDC_FPF_BEN,double CustFee = 0.0,double BrokerFee = 0.0,string Message = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 1,int TID = 1,TThostFtdcTransferStatusType TransferStatus = TThostFtdcTransferStatusType.THOST_FTDC_TRFS_Normal,string LongCustomerName = "")
        {
			CThostFtdcReqTransferField pReqTransfer = new CThostFtdcReqTransferField
			{
				TradeCode = TradeCode,
				BankID = BankID,
				BankBranchID = BankBranchID,
				BrokerID = BrokerID,
				BrokerBranchID = BrokerBranchID,
				TradeDate = TradeDate,
				TradeTime = TradeTime,
				BankSerial = BankSerial,
				TradingDay = TradingDay,
				PlateSerial = PlateSerial,
				LastFragment = LastFragment,
				SessionID = SessionID,
				CustomerName = CustomerName,
				IdCardType = IdCardType,
				IdentifiedCardNo = IdentifiedCardNo,
				CustType = CustType,
				BankAccount = BankAccount,
				BankPassWord = BankPassWord,
				AccountID = AccountID,
				Password = Password,
				InstallID = InstallID,
				FutureSerial = FutureSerial,
				UserID = UserID,
				VerifyCertNoFlag = VerifyCertNoFlag,
				CurrencyID = CurrencyID,
				TradeAmount = TradeAmount,
				FutureFetchAmount = FutureFetchAmount,
				FeePayFlag = FeePayFlag,
				CustFee = CustFee,
				BrokerFee = BrokerFee,
				Message = Message,
				Digest = Digest,
				BankAccType = BankAccType,
				DeviceID = DeviceID,
				BankSecuAccType = BankSecuAccType,
				BrokerIDByBank = BrokerIDByBank,
				BankSecuAcc = BankSecuAcc,
				BankPwdFlag = BankPwdFlag,
				SecuPwdFlag = SecuPwdFlag,
				OperNo = OperNo,
				RequestID = RequestID,
				TID = TID,
				TransferStatus = TransferStatus,
				LongCustomerName = LongCustomerName,
			};
            return (Invoke(_handle, "ReqFromBankToFutureByFuture", typeof(DeleReqFromBankToFutureByFuture)) as DeleReqFromBankToFutureByFuture)(_api, ref pReqTransfer, this.nRequestID++);
        }
                    

		/// <summary>
		///期货发起期货资金转银行请求
		/// </summary>
        public IntPtr ReqFromFutureToBankByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 1,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 1,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int InstallID = 1,int FutureSerial = 1,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",double TradeAmount = 0.0,double FutureFetchAmount = 0.0,TThostFtdcFeePayFlagType FeePayFlag = TThostFtdcFeePayFlagType.THOST_FTDC_FPF_BEN,double CustFee = 0.0,double BrokerFee = 0.0,string Message = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 1,int TID = 1,TThostFtdcTransferStatusType TransferStatus = TThostFtdcTransferStatusType.THOST_FTDC_TRFS_Normal,string LongCustomerName = "")
        {
			CThostFtdcReqTransferField pReqTransfer = new CThostFtdcReqTransferField
			{
				TradeCode = TradeCode,
				BankID = BankID,
				BankBranchID = BankBranchID,
				BrokerID = BrokerID,
				BrokerBranchID = BrokerBranchID,
				TradeDate = TradeDate,
				TradeTime = TradeTime,
				BankSerial = BankSerial,
				TradingDay = TradingDay,
				PlateSerial = PlateSerial,
				LastFragment = LastFragment,
				SessionID = SessionID,
				CustomerName = CustomerName,
				IdCardType = IdCardType,
				IdentifiedCardNo = IdentifiedCardNo,
				CustType = CustType,
				BankAccount = BankAccount,
				BankPassWord = BankPassWord,
				AccountID = AccountID,
				Password = Password,
				InstallID = InstallID,
				FutureSerial = FutureSerial,
				UserID = UserID,
				VerifyCertNoFlag = VerifyCertNoFlag,
				CurrencyID = CurrencyID,
				TradeAmount = TradeAmount,
				FutureFetchAmount = FutureFetchAmount,
				FeePayFlag = FeePayFlag,
				CustFee = CustFee,
				BrokerFee = BrokerFee,
				Message = Message,
				Digest = Digest,
				BankAccType = BankAccType,
				DeviceID = DeviceID,
				BankSecuAccType = BankSecuAccType,
				BrokerIDByBank = BrokerIDByBank,
				BankSecuAcc = BankSecuAcc,
				BankPwdFlag = BankPwdFlag,
				SecuPwdFlag = SecuPwdFlag,
				OperNo = OperNo,
				RequestID = RequestID,
				TID = TID,
				TransferStatus = TransferStatus,
				LongCustomerName = LongCustomerName,
			};
            return (Invoke(_handle, "ReqFromFutureToBankByFuture", typeof(DeleReqFromFutureToBankByFuture)) as DeleReqFromFutureToBankByFuture)(_api, ref pReqTransfer, this.nRequestID++);
        }
                    

		/// <summary>
		///期货发起查询银行余额请求
		/// </summary>
        public IntPtr ReqQueryBankAccountMoneyByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 1,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 1,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int FutureSerial = 1,int InstallID = 1,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 1,int TID = 1,string LongCustomerName = "")
        {
			CThostFtdcReqQueryAccountField pReqQueryAccount = new CThostFtdcReqQueryAccountField
			{
				TradeCode = TradeCode,
				BankID = BankID,
				BankBranchID = BankBranchID,
				BrokerID = BrokerID,
				BrokerBranchID = BrokerBranchID,
				TradeDate = TradeDate,
				TradeTime = TradeTime,
				BankSerial = BankSerial,
				TradingDay = TradingDay,
				PlateSerial = PlateSerial,
				LastFragment = LastFragment,
				SessionID = SessionID,
				CustomerName = CustomerName,
				IdCardType = IdCardType,
				IdentifiedCardNo = IdentifiedCardNo,
				CustType = CustType,
				BankAccount = BankAccount,
				BankPassWord = BankPassWord,
				AccountID = AccountID,
				Password = Password,
				FutureSerial = FutureSerial,
				InstallID = InstallID,
				UserID = UserID,
				VerifyCertNoFlag = VerifyCertNoFlag,
				CurrencyID = CurrencyID,
				Digest = Digest,
				BankAccType = BankAccType,
				DeviceID = DeviceID,
				BankSecuAccType = BankSecuAccType,
				BrokerIDByBank = BrokerIDByBank,
				BankSecuAcc = BankSecuAcc,
				BankPwdFlag = BankPwdFlag,
				SecuPwdFlag = SecuPwdFlag,
				OperNo = OperNo,
				RequestID = RequestID,
				TID = TID,
				LongCustomerName = LongCustomerName,
			};
            return (Invoke(_handle, "ReqQueryBankAccountMoneyByFuture", typeof(DeleReqQueryBankAccountMoneyByFuture)) as DeleReqQueryBankAccountMoneyByFuture)(_api, ref pReqQueryAccount, this.nRequestID++);
        }
                    
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		delegate void DeleSet(IntPtr spi, Delegate func);
		
		/// <summary>
		///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontConnected();
		
		/// <summary>
		///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
		///@param nReason 错误原因
		///        0x1001 网络读失败
		///        0x1002 网络写失败
		///        0x2001 接收心跳超时
		///        0x2002 发送心跳失败
		///        0x2003 收到错误报文
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontDisconnected(int nReason);
		
		/// <summary>
		///心跳超时警告。当长时间未收到报文时，该方法被调用。
		///@param nTimeLapse 距离上次接收报文的时间
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnHeartBeatWarning(int nTimeLapse);
		
		/// <summary>
		///客户端认证响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspAuthenticate(ref CThostFtdcRspAuthenticateField pRspAuthenticateField,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///登录请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///登出请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogout(ref CThostFtdcUserLogoutField pUserLogout,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///用户口令更新请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserPasswordUpdate(ref CThostFtdcUserPasswordUpdateField pUserPasswordUpdate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///资金账户口令更新请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspTradingAccountPasswordUpdate(ref CThostFtdcTradingAccountPasswordUpdateField pTradingAccountPasswordUpdate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///查询用户当前支持的认证模式的回复
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserAuthMethod(ref CThostFtdcRspUserAuthMethodField pRspUserAuthMethod,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///获取图形验证码请求的回复
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspGenUserCaptcha(ref CThostFtdcRspGenUserCaptchaField pRspGenUserCaptcha,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///获取短信验证码请求的回复
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspGenUserText(ref CThostFtdcRspGenUserTextField pRspGenUserText,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///报单录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderInsert(ref CThostFtdcInputOrderField pInputOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///预埋单录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspParkedOrderInsert(ref CThostFtdcParkedOrderField pParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///预埋撤单录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspParkedOrderAction(ref CThostFtdcParkedOrderActionField pParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///报单操作请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderAction(ref CThostFtdcInputOrderActionField pInputOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///查询最大报单数量响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryMaxOrderVolume(ref CThostFtdcQueryMaxOrderVolumeField pQueryMaxOrderVolume,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///投资者结算结果确认响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSettlementInfoConfirm(ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///删除预埋单响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspRemoveParkedOrder(ref CThostFtdcRemoveParkedOrderField pRemoveParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///删除预埋撤单响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspRemoveParkedOrderAction(ref CThostFtdcRemoveParkedOrderActionField pRemoveParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///执行宣告录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderInsert(ref CThostFtdcInputExecOrderField pInputExecOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///执行宣告操作请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderAction(ref CThostFtdcInputExecOrderActionField pInputExecOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///询价录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspForQuoteInsert(ref CThostFtdcInputForQuoteField pInputForQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///报价录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteInsert(ref CThostFtdcInputQuoteField pInputQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///报价操作请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteAction(ref CThostFtdcInputQuoteActionField pInputQuoteAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///批量报单操作请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspBatchOrderAction(ref CThostFtdcInputBatchOrderActionField pInputBatchOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///期权自对冲录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOptionSelfCloseInsert(ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///期权自对冲操作请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOptionSelfCloseAction(ref CThostFtdcInputOptionSelfCloseActionField pInputOptionSelfCloseAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///申请组合录入请求响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspCombActionInsert(ref CThostFtdcInputCombActionField pInputCombAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询报单响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOrder(ref CThostFtdcOrderField pOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询成交响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTrade(ref CThostFtdcTradeField pTrade,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者持仓响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPosition(ref CThostFtdcInvestorPositionField pInvestorPosition,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询资金账户响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingAccount(ref CThostFtdcTradingAccountField pTradingAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestor(ref CThostFtdcInvestorField pInvestor,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询交易编码响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingCode(ref CThostFtdcTradingCodeField pTradingCode,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询合约保证金率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentMarginRate(ref CThostFtdcInstrumentMarginRateField pInstrumentMarginRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询合约手续费率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentCommissionRate(ref CThostFtdcInstrumentCommissionRateField pInstrumentCommissionRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询交易所响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchange(ref CThostFtdcExchangeField pExchange,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询产品响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProduct(ref CThostFtdcProductField pProduct,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询合约响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrument(ref CThostFtdcInstrumentField pInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询行情响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryDepthMarketData(ref CThostFtdcDepthMarketDataField pDepthMarketData,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者结算结果响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySettlementInfo(ref CThostFtdcSettlementInfoField pSettlementInfo,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询转帐银行响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTransferBank(ref CThostFtdcTransferBankField pTransferBank,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者持仓明细响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPositionDetail(ref CThostFtdcInvestorPositionDetailField pInvestorPositionDetail,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询客户通知响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryNotice(ref CThostFtdcNoticeField pNotice,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询结算信息确认响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySettlementInfoConfirm(ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者持仓明细响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPositionCombineDetail(ref CThostFtdcInvestorPositionCombineDetailField pInvestorPositionCombineDetail,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///查询保证金监管系统经纪公司资金账户密钥响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCFMMCTradingAccountKey(ref CThostFtdcCFMMCTradingAccountKeyField pCFMMCTradingAccountKey,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询仓单折抵信息响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryEWarrantOffset(ref CThostFtdcEWarrantOffsetField pEWarrantOffset,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资者品种/跨品种保证金响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorProductGroupMargin(ref CThostFtdcInvestorProductGroupMarginField pInvestorProductGroupMargin,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询交易所保证金率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeMarginRate(ref CThostFtdcExchangeMarginRateField pExchangeMarginRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询交易所调整保证金率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeMarginRateAdjust(ref CThostFtdcExchangeMarginRateAdjustField pExchangeMarginRateAdjust,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询汇率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeRate(ref CThostFtdcExchangeRateField pExchangeRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询二级代理操作员银期权限响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentACIDMap(ref CThostFtdcSecAgentACIDMapField pSecAgentACIDMap,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询产品报价汇率
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProductExchRate(ref CThostFtdcProductExchRateField pProductExchRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询产品组
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProductGroup(ref CThostFtdcProductGroupField pProductGroup,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询做市商合约手续费率响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMMInstrumentCommissionRate(ref CThostFtdcMMInstrumentCommissionRateField pMMInstrumentCommissionRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询做市商期权合约手续费响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMMOptionInstrCommRate(ref CThostFtdcMMOptionInstrCommRateField pMMOptionInstrCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询报单手续费响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentOrderCommRate(ref CThostFtdcInstrumentOrderCommRateField pInstrumentOrderCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询资金账户响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentTradingAccount(ref CThostFtdcTradingAccountField pTradingAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询二级代理商资金校验模式响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentCheckMode(ref CThostFtdcSecAgentCheckModeField pSecAgentCheckMode,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询二级代理商信息响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentTradeInfo(ref CThostFtdcSecAgentTradeInfoField pSecAgentTradeInfo,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询期权交易成本响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionInstrTradeCost(ref CThostFtdcOptionInstrTradeCostField pOptionInstrTradeCost,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询期权合约手续费响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionInstrCommRate(ref CThostFtdcOptionInstrCommRateField pOptionInstrCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询执行宣告响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExecOrder(ref CThostFtdcExecOrderField pExecOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询询价响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryForQuote(ref CThostFtdcForQuoteField pForQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询报价响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryQuote(ref CThostFtdcQuoteField pQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询期权自对冲响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionSelfClose(ref CThostFtdcOptionSelfCloseField pOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询投资单元响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestUnit(ref CThostFtdcInvestUnitField pInvestUnit,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询组合合约安全系数响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCombInstrumentGuard(ref CThostFtdcCombInstrumentGuardField pCombInstrumentGuard,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询申请组合响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCombAction(ref CThostFtdcCombActionField pCombAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询转帐流水响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTransferSerial(ref CThostFtdcTransferSerialField pTransferSerial,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询银期签约关系响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryAccountregister(ref CThostFtdcAccountregisterField pAccountregister,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///错误应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspError(ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///报单通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOrder(ref CThostFtdcOrderField pOrder);
		
		/// <summary>
		///成交通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTrade(ref CThostFtdcTradeField pTrade);
		
		/// <summary>
		///报单录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderInsert(ref CThostFtdcInputOrderField pInputOrder,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///报单操作错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderAction(ref CThostFtdcOrderActionField pOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///合约交易状态通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnInstrumentStatus(ref CThostFtdcInstrumentStatusField pInstrumentStatus);
		
		/// <summary>
		///交易所公告通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnBulletin(ref CThostFtdcBulletinField pBulletin);
		
		/// <summary>
		///交易通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTradingNotice(ref CThostFtdcTradingNoticeInfoField pTradingNoticeInfo);
		
		/// <summary>
		///提示条件单校验错误
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnErrorConditionalOrder(ref CThostFtdcErrorConditionalOrderField pErrorConditionalOrder);
		
		/// <summary>
		///执行宣告通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnExecOrder(ref CThostFtdcExecOrderField pExecOrder);
		
		/// <summary>
		///执行宣告录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderInsert(ref CThostFtdcInputExecOrderField pInputExecOrder,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///执行宣告操作错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderAction(ref CThostFtdcExecOrderActionField pExecOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///询价录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnForQuoteInsert(ref CThostFtdcInputForQuoteField pInputForQuote,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///报价通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnQuote(ref CThostFtdcQuoteField pQuote);
		
		/// <summary>
		///报价录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteInsert(ref CThostFtdcInputQuoteField pInputQuote,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///报价操作错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteAction(ref CThostFtdcQuoteActionField pQuoteAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///询价通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnForQuoteRsp(ref CThostFtdcForQuoteRspField pForQuoteRsp);
		
		/// <summary>
		///保证金监控中心用户令牌
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCFMMCTradingAccountToken(ref CThostFtdcCFMMCTradingAccountTokenField pCFMMCTradingAccountToken);
		
		/// <summary>
		///批量报单操作错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnBatchOrderAction(ref CThostFtdcBatchOrderActionField pBatchOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///期权自对冲通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOptionSelfClose(ref CThostFtdcOptionSelfCloseField pOptionSelfClose);
		
		/// <summary>
		///期权自对冲录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOptionSelfCloseInsert(ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///期权自对冲操作错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOptionSelfCloseAction(ref CThostFtdcOptionSelfCloseActionField pOptionSelfCloseAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///申请组合通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCombAction(ref CThostFtdcCombActionField pCombAction);
		
		/// <summary>
		///申请组合录入错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnCombActionInsert(ref CThostFtdcInputCombActionField pInputCombAction,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///请求查询签约银行响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryContractBank(ref CThostFtdcContractBankField pContractBank,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询预埋单响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryParkedOrder(ref CThostFtdcParkedOrderField pParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询预埋撤单响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryParkedOrderAction(ref CThostFtdcParkedOrderActionField pParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询交易通知响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingNotice(ref CThostFtdcTradingNoticeField pTradingNotice,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询经纪公司交易参数响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryBrokerTradingParams(ref CThostFtdcBrokerTradingParamsField pBrokerTradingParams,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询经纪公司交易算法响应
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryBrokerTradingAlgos(ref CThostFtdcBrokerTradingAlgosField pBrokerTradingAlgos,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///请求查询监控中心用户令牌
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryCFMMCTradingAccountToken(ref CThostFtdcQueryCFMMCTradingAccountTokenField pQueryCFMMCTradingAccountToken,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///银行发起银行资金转期货通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromBankToFutureByBank(ref CThostFtdcRspTransferField pRspTransfer);
		
		/// <summary>
		///银行发起期货资金转银行通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromFutureToBankByBank(ref CThostFtdcRspTransferField pRspTransfer);
		
		/// <summary>
		///银行发起冲正银行转期货通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByBank(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///银行发起冲正期货转银行通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByBank(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///期货发起银行资金转期货通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromBankToFutureByFuture(ref CThostFtdcRspTransferField pRspTransfer);
		
		/// <summary>
		///期货发起期货资金转银行通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromFutureToBankByFuture(ref CThostFtdcRspTransferField pRspTransfer);
		
		/// <summary>
		///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByFutureManual(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByFutureManual(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///期货发起查询银行余额通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnQueryBankBalanceByFuture(ref CThostFtdcNotifyQueryAccountField pNotifyQueryAccount);
		
		/// <summary>
		///期货发起银行资金转期货错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnBankToFutureByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///期货发起期货资金转银行错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnFutureToBankByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///系统运行时期货端手工发起冲正银行转期货错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnRepealBankToFutureByFutureManual(ref CThostFtdcReqRepealField pReqRepeal,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///系统运行时期货端手工发起冲正期货转银行错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnRepealFutureToBankByFutureManual(ref CThostFtdcReqRepealField pReqRepeal,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///期货发起查询银行余额错误回报
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQueryBankBalanceByFuture(ref CThostFtdcReqQueryAccountField pReqQueryAccount,ref CThostFtdcRspInfoField pRspInfo);
		
		/// <summary>
		///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByFuture(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByFuture(ref CThostFtdcRspRepealField pRspRepeal);
		
		/// <summary>
		///期货发起银行资金转期货应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspFromBankToFutureByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///期货发起期货资金转银行应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspFromFutureToBankByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///期货发起查询银行余额应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryBankAccountMoneyByFuture(ref CThostFtdcReqQueryAccountField pReqQueryAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///银行发起银期开户通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOpenAccountByBank(ref CThostFtdcOpenAccountField pOpenAccount);
		
		/// <summary>
		///银行发起银期销户通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCancelAccountByBank(ref CThostFtdcCancelAccountField pCancelAccount);
		
		/// <summary>
		///银行发起变更银行账号通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnChangeAccountByBank(ref CThostFtdcChangeAccountField pChangeAccount);
		
		/// <summary>
		///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
		/// </summary>
		public void SetOnFrontConnected(DeleOnFrontConnected func) {(Invoke(_handle, "SetOnFrontConnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
		///@param nReason 错误原因
		///        0x1001 网络读失败
		///        0x1002 网络写失败
		///        0x2001 接收心跳超时
		///        0x2002 发送心跳失败
		///        0x2003 收到错误报文
		/// </summary>
		public void SetOnFrontDisconnected(DeleOnFrontDisconnected func) {(Invoke(_handle, "SetOnFrontDisconnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///心跳超时警告。当长时间未收到报文时，该方法被调用。
		///@param nTimeLapse 距离上次接收报文的时间
		/// </summary>
		public void SetOnHeartBeatWarning(DeleOnHeartBeatWarning func) {(Invoke(_handle, "SetOnHeartBeatWarning", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///客户端认证响应
		/// </summary>
		public void SetOnRspAuthenticate(DeleOnRspAuthenticate func) {(Invoke(_handle, "SetOnRspAuthenticate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///登录请求响应
		/// </summary>
		public void SetOnRspUserLogin(DeleOnRspUserLogin func) {(Invoke(_handle, "SetOnRspUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///登出请求响应
		/// </summary>
		public void SetOnRspUserLogout(DeleOnRspUserLogout func) {(Invoke(_handle, "SetOnRspUserLogout", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///用户口令更新请求响应
		/// </summary>
		public void SetOnRspUserPasswordUpdate(DeleOnRspUserPasswordUpdate func) {(Invoke(_handle, "SetOnRspUserPasswordUpdate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///资金账户口令更新请求响应
		/// </summary>
		public void SetOnRspTradingAccountPasswordUpdate(DeleOnRspTradingAccountPasswordUpdate func) {(Invoke(_handle, "SetOnRspTradingAccountPasswordUpdate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///查询用户当前支持的认证模式的回复
		/// </summary>
		public void SetOnRspUserAuthMethod(DeleOnRspUserAuthMethod func) {(Invoke(_handle, "SetOnRspUserAuthMethod", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///获取图形验证码请求的回复
		/// </summary>
		public void SetOnRspGenUserCaptcha(DeleOnRspGenUserCaptcha func) {(Invoke(_handle, "SetOnRspGenUserCaptcha", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///获取短信验证码请求的回复
		/// </summary>
		public void SetOnRspGenUserText(DeleOnRspGenUserText func) {(Invoke(_handle, "SetOnRspGenUserText", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报单录入请求响应
		/// </summary>
		public void SetOnRspOrderInsert(DeleOnRspOrderInsert func) {(Invoke(_handle, "SetOnRspOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///预埋单录入请求响应
		/// </summary>
		public void SetOnRspParkedOrderInsert(DeleOnRspParkedOrderInsert func) {(Invoke(_handle, "SetOnRspParkedOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///预埋撤单录入请求响应
		/// </summary>
		public void SetOnRspParkedOrderAction(DeleOnRspParkedOrderAction func) {(Invoke(_handle, "SetOnRspParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报单操作请求响应
		/// </summary>
		public void SetOnRspOrderAction(DeleOnRspOrderAction func) {(Invoke(_handle, "SetOnRspOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///查询最大报单数量响应
		/// </summary>
		public void SetOnRspQueryMaxOrderVolume(DeleOnRspQueryMaxOrderVolume func) {(Invoke(_handle, "SetOnRspQueryMaxOrderVolume", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///投资者结算结果确认响应
		/// </summary>
		public void SetOnRspSettlementInfoConfirm(DeleOnRspSettlementInfoConfirm func) {(Invoke(_handle, "SetOnRspSettlementInfoConfirm", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///删除预埋单响应
		/// </summary>
		public void SetOnRspRemoveParkedOrder(DeleOnRspRemoveParkedOrder func) {(Invoke(_handle, "SetOnRspRemoveParkedOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///删除预埋撤单响应
		/// </summary>
		public void SetOnRspRemoveParkedOrderAction(DeleOnRspRemoveParkedOrderAction func) {(Invoke(_handle, "SetOnRspRemoveParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///执行宣告录入请求响应
		/// </summary>
		public void SetOnRspExecOrderInsert(DeleOnRspExecOrderInsert func) {(Invoke(_handle, "SetOnRspExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///执行宣告操作请求响应
		/// </summary>
		public void SetOnRspExecOrderAction(DeleOnRspExecOrderAction func) {(Invoke(_handle, "SetOnRspExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///询价录入请求响应
		/// </summary>
		public void SetOnRspForQuoteInsert(DeleOnRspForQuoteInsert func) {(Invoke(_handle, "SetOnRspForQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报价录入请求响应
		/// </summary>
		public void SetOnRspQuoteInsert(DeleOnRspQuoteInsert func) {(Invoke(_handle, "SetOnRspQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报价操作请求响应
		/// </summary>
		public void SetOnRspQuoteAction(DeleOnRspQuoteAction func) {(Invoke(_handle, "SetOnRspQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///批量报单操作请求响应
		/// </summary>
		public void SetOnRspBatchOrderAction(DeleOnRspBatchOrderAction func) {(Invoke(_handle, "SetOnRspBatchOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期权自对冲录入请求响应
		/// </summary>
		public void SetOnRspOptionSelfCloseInsert(DeleOnRspOptionSelfCloseInsert func) {(Invoke(_handle, "SetOnRspOptionSelfCloseInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期权自对冲操作请求响应
		/// </summary>
		public void SetOnRspOptionSelfCloseAction(DeleOnRspOptionSelfCloseAction func) {(Invoke(_handle, "SetOnRspOptionSelfCloseAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///申请组合录入请求响应
		/// </summary>
		public void SetOnRspCombActionInsert(DeleOnRspCombActionInsert func) {(Invoke(_handle, "SetOnRspCombActionInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询报单响应
		/// </summary>
		public void SetOnRspQryOrder(DeleOnRspQryOrder func) {(Invoke(_handle, "SetOnRspQryOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询成交响应
		/// </summary>
		public void SetOnRspQryTrade(DeleOnRspQryTrade func) {(Invoke(_handle, "SetOnRspQryTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者持仓响应
		/// </summary>
		public void SetOnRspQryInvestorPosition(DeleOnRspQryInvestorPosition func) {(Invoke(_handle, "SetOnRspQryInvestorPosition", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询资金账户响应
		/// </summary>
		public void SetOnRspQryTradingAccount(DeleOnRspQryTradingAccount func) {(Invoke(_handle, "SetOnRspQryTradingAccount", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者响应
		/// </summary>
		public void SetOnRspQryInvestor(DeleOnRspQryInvestor func) {(Invoke(_handle, "SetOnRspQryInvestor", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询交易编码响应
		/// </summary>
		public void SetOnRspQryTradingCode(DeleOnRspQryTradingCode func) {(Invoke(_handle, "SetOnRspQryTradingCode", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询合约保证金率响应
		/// </summary>
		public void SetOnRspQryInstrumentMarginRate(DeleOnRspQryInstrumentMarginRate func) {(Invoke(_handle, "SetOnRspQryInstrumentMarginRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询合约手续费率响应
		/// </summary>
		public void SetOnRspQryInstrumentCommissionRate(DeleOnRspQryInstrumentCommissionRate func) {(Invoke(_handle, "SetOnRspQryInstrumentCommissionRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询交易所响应
		/// </summary>
		public void SetOnRspQryExchange(DeleOnRspQryExchange func) {(Invoke(_handle, "SetOnRspQryExchange", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询产品响应
		/// </summary>
		public void SetOnRspQryProduct(DeleOnRspQryProduct func) {(Invoke(_handle, "SetOnRspQryProduct", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询合约响应
		/// </summary>
		public void SetOnRspQryInstrument(DeleOnRspQryInstrument func) {(Invoke(_handle, "SetOnRspQryInstrument", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询行情响应
		/// </summary>
		public void SetOnRspQryDepthMarketData(DeleOnRspQryDepthMarketData func) {(Invoke(_handle, "SetOnRspQryDepthMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者结算结果响应
		/// </summary>
		public void SetOnRspQrySettlementInfo(DeleOnRspQrySettlementInfo func) {(Invoke(_handle, "SetOnRspQrySettlementInfo", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询转帐银行响应
		/// </summary>
		public void SetOnRspQryTransferBank(DeleOnRspQryTransferBank func) {(Invoke(_handle, "SetOnRspQryTransferBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者持仓明细响应
		/// </summary>
		public void SetOnRspQryInvestorPositionDetail(DeleOnRspQryInvestorPositionDetail func) {(Invoke(_handle, "SetOnRspQryInvestorPositionDetail", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询客户通知响应
		/// </summary>
		public void SetOnRspQryNotice(DeleOnRspQryNotice func) {(Invoke(_handle, "SetOnRspQryNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询结算信息确认响应
		/// </summary>
		public void SetOnRspQrySettlementInfoConfirm(DeleOnRspQrySettlementInfoConfirm func) {(Invoke(_handle, "SetOnRspQrySettlementInfoConfirm", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者持仓明细响应
		/// </summary>
		public void SetOnRspQryInvestorPositionCombineDetail(DeleOnRspQryInvestorPositionCombineDetail func) {(Invoke(_handle, "SetOnRspQryInvestorPositionCombineDetail", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///查询保证金监管系统经纪公司资金账户密钥响应
		/// </summary>
		public void SetOnRspQryCFMMCTradingAccountKey(DeleOnRspQryCFMMCTradingAccountKey func) {(Invoke(_handle, "SetOnRspQryCFMMCTradingAccountKey", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询仓单折抵信息响应
		/// </summary>
		public void SetOnRspQryEWarrantOffset(DeleOnRspQryEWarrantOffset func) {(Invoke(_handle, "SetOnRspQryEWarrantOffset", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资者品种/跨品种保证金响应
		/// </summary>
		public void SetOnRspQryInvestorProductGroupMargin(DeleOnRspQryInvestorProductGroupMargin func) {(Invoke(_handle, "SetOnRspQryInvestorProductGroupMargin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询交易所保证金率响应
		/// </summary>
		public void SetOnRspQryExchangeMarginRate(DeleOnRspQryExchangeMarginRate func) {(Invoke(_handle, "SetOnRspQryExchangeMarginRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询交易所调整保证金率响应
		/// </summary>
		public void SetOnRspQryExchangeMarginRateAdjust(DeleOnRspQryExchangeMarginRateAdjust func) {(Invoke(_handle, "SetOnRspQryExchangeMarginRateAdjust", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询汇率响应
		/// </summary>
		public void SetOnRspQryExchangeRate(DeleOnRspQryExchangeRate func) {(Invoke(_handle, "SetOnRspQryExchangeRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询二级代理操作员银期权限响应
		/// </summary>
		public void SetOnRspQrySecAgentACIDMap(DeleOnRspQrySecAgentACIDMap func) {(Invoke(_handle, "SetOnRspQrySecAgentACIDMap", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询产品报价汇率
		/// </summary>
		public void SetOnRspQryProductExchRate(DeleOnRspQryProductExchRate func) {(Invoke(_handle, "SetOnRspQryProductExchRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询产品组
		/// </summary>
		public void SetOnRspQryProductGroup(DeleOnRspQryProductGroup func) {(Invoke(_handle, "SetOnRspQryProductGroup", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询做市商合约手续费率响应
		/// </summary>
		public void SetOnRspQryMMInstrumentCommissionRate(DeleOnRspQryMMInstrumentCommissionRate func) {(Invoke(_handle, "SetOnRspQryMMInstrumentCommissionRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询做市商期权合约手续费响应
		/// </summary>
		public void SetOnRspQryMMOptionInstrCommRate(DeleOnRspQryMMOptionInstrCommRate func) {(Invoke(_handle, "SetOnRspQryMMOptionInstrCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询报单手续费响应
		/// </summary>
		public void SetOnRspQryInstrumentOrderCommRate(DeleOnRspQryInstrumentOrderCommRate func) {(Invoke(_handle, "SetOnRspQryInstrumentOrderCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询资金账户响应
		/// </summary>
		public void SetOnRspQrySecAgentTradingAccount(DeleOnRspQrySecAgentTradingAccount func) {(Invoke(_handle, "SetOnRspQrySecAgentTradingAccount", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询二级代理商资金校验模式响应
		/// </summary>
		public void SetOnRspQrySecAgentCheckMode(DeleOnRspQrySecAgentCheckMode func) {(Invoke(_handle, "SetOnRspQrySecAgentCheckMode", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询二级代理商信息响应
		/// </summary>
		public void SetOnRspQrySecAgentTradeInfo(DeleOnRspQrySecAgentTradeInfo func) {(Invoke(_handle, "SetOnRspQrySecAgentTradeInfo", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询期权交易成本响应
		/// </summary>
		public void SetOnRspQryOptionInstrTradeCost(DeleOnRspQryOptionInstrTradeCost func) {(Invoke(_handle, "SetOnRspQryOptionInstrTradeCost", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询期权合约手续费响应
		/// </summary>
		public void SetOnRspQryOptionInstrCommRate(DeleOnRspQryOptionInstrCommRate func) {(Invoke(_handle, "SetOnRspQryOptionInstrCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询执行宣告响应
		/// </summary>
		public void SetOnRspQryExecOrder(DeleOnRspQryExecOrder func) {(Invoke(_handle, "SetOnRspQryExecOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询询价响应
		/// </summary>
		public void SetOnRspQryForQuote(DeleOnRspQryForQuote func) {(Invoke(_handle, "SetOnRspQryForQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询报价响应
		/// </summary>
		public void SetOnRspQryQuote(DeleOnRspQryQuote func) {(Invoke(_handle, "SetOnRspQryQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询期权自对冲响应
		/// </summary>
		public void SetOnRspQryOptionSelfClose(DeleOnRspQryOptionSelfClose func) {(Invoke(_handle, "SetOnRspQryOptionSelfClose", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询投资单元响应
		/// </summary>
		public void SetOnRspQryInvestUnit(DeleOnRspQryInvestUnit func) {(Invoke(_handle, "SetOnRspQryInvestUnit", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询组合合约安全系数响应
		/// </summary>
		public void SetOnRspQryCombInstrumentGuard(DeleOnRspQryCombInstrumentGuard func) {(Invoke(_handle, "SetOnRspQryCombInstrumentGuard", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询申请组合响应
		/// </summary>
		public void SetOnRspQryCombAction(DeleOnRspQryCombAction func) {(Invoke(_handle, "SetOnRspQryCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询转帐流水响应
		/// </summary>
		public void SetOnRspQryTransferSerial(DeleOnRspQryTransferSerial func) {(Invoke(_handle, "SetOnRspQryTransferSerial", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询银期签约关系响应
		/// </summary>
		public void SetOnRspQryAccountregister(DeleOnRspQryAccountregister func) {(Invoke(_handle, "SetOnRspQryAccountregister", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///错误应答
		/// </summary>
		public void SetOnRspError(DeleOnRspError func) {(Invoke(_handle, "SetOnRspError", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报单通知
		/// </summary>
		public void SetOnRtnOrder(DeleOnRtnOrder func) {(Invoke(_handle, "SetOnRtnOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///成交通知
		/// </summary>
		public void SetOnRtnTrade(DeleOnRtnTrade func) {(Invoke(_handle, "SetOnRtnTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报单录入错误回报
		/// </summary>
		public void SetOnErrRtnOrderInsert(DeleOnErrRtnOrderInsert func) {(Invoke(_handle, "SetOnErrRtnOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报单操作错误回报
		/// </summary>
		public void SetOnErrRtnOrderAction(DeleOnErrRtnOrderAction func) {(Invoke(_handle, "SetOnErrRtnOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///合约交易状态通知
		/// </summary>
		public void SetOnRtnInstrumentStatus(DeleOnRtnInstrumentStatus func) {(Invoke(_handle, "SetOnRtnInstrumentStatus", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///交易所公告通知
		/// </summary>
		public void SetOnRtnBulletin(DeleOnRtnBulletin func) {(Invoke(_handle, "SetOnRtnBulletin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///交易通知
		/// </summary>
		public void SetOnRtnTradingNotice(DeleOnRtnTradingNotice func) {(Invoke(_handle, "SetOnRtnTradingNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///提示条件单校验错误
		/// </summary>
		public void SetOnRtnErrorConditionalOrder(DeleOnRtnErrorConditionalOrder func) {(Invoke(_handle, "SetOnRtnErrorConditionalOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///执行宣告通知
		/// </summary>
		public void SetOnRtnExecOrder(DeleOnRtnExecOrder func) {(Invoke(_handle, "SetOnRtnExecOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///执行宣告录入错误回报
		/// </summary>
		public void SetOnErrRtnExecOrderInsert(DeleOnErrRtnExecOrderInsert func) {(Invoke(_handle, "SetOnErrRtnExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///执行宣告操作错误回报
		/// </summary>
		public void SetOnErrRtnExecOrderAction(DeleOnErrRtnExecOrderAction func) {(Invoke(_handle, "SetOnErrRtnExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///询价录入错误回报
		/// </summary>
		public void SetOnErrRtnForQuoteInsert(DeleOnErrRtnForQuoteInsert func) {(Invoke(_handle, "SetOnErrRtnForQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报价通知
		/// </summary>
		public void SetOnRtnQuote(DeleOnRtnQuote func) {(Invoke(_handle, "SetOnRtnQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报价录入错误回报
		/// </summary>
		public void SetOnErrRtnQuoteInsert(DeleOnErrRtnQuoteInsert func) {(Invoke(_handle, "SetOnErrRtnQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///报价操作错误回报
		/// </summary>
		public void SetOnErrRtnQuoteAction(DeleOnErrRtnQuoteAction func) {(Invoke(_handle, "SetOnErrRtnQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///询价通知
		/// </summary>
		public void SetOnRtnForQuoteRsp(DeleOnRtnForQuoteRsp func) {(Invoke(_handle, "SetOnRtnForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///保证金监控中心用户令牌
		/// </summary>
		public void SetOnRtnCFMMCTradingAccountToken(DeleOnRtnCFMMCTradingAccountToken func) {(Invoke(_handle, "SetOnRtnCFMMCTradingAccountToken", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///批量报单操作错误回报
		/// </summary>
		public void SetOnErrRtnBatchOrderAction(DeleOnErrRtnBatchOrderAction func) {(Invoke(_handle, "SetOnErrRtnBatchOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期权自对冲通知
		/// </summary>
		public void SetOnRtnOptionSelfClose(DeleOnRtnOptionSelfClose func) {(Invoke(_handle, "SetOnRtnOptionSelfClose", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期权自对冲录入错误回报
		/// </summary>
		public void SetOnErrRtnOptionSelfCloseInsert(DeleOnErrRtnOptionSelfCloseInsert func) {(Invoke(_handle, "SetOnErrRtnOptionSelfCloseInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期权自对冲操作错误回报
		/// </summary>
		public void SetOnErrRtnOptionSelfCloseAction(DeleOnErrRtnOptionSelfCloseAction func) {(Invoke(_handle, "SetOnErrRtnOptionSelfCloseAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///申请组合通知
		/// </summary>
		public void SetOnRtnCombAction(DeleOnRtnCombAction func) {(Invoke(_handle, "SetOnRtnCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///申请组合录入错误回报
		/// </summary>
		public void SetOnErrRtnCombActionInsert(DeleOnErrRtnCombActionInsert func) {(Invoke(_handle, "SetOnErrRtnCombActionInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询签约银行响应
		/// </summary>
		public void SetOnRspQryContractBank(DeleOnRspQryContractBank func) {(Invoke(_handle, "SetOnRspQryContractBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询预埋单响应
		/// </summary>
		public void SetOnRspQryParkedOrder(DeleOnRspQryParkedOrder func) {(Invoke(_handle, "SetOnRspQryParkedOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询预埋撤单响应
		/// </summary>
		public void SetOnRspQryParkedOrderAction(DeleOnRspQryParkedOrderAction func) {(Invoke(_handle, "SetOnRspQryParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询交易通知响应
		/// </summary>
		public void SetOnRspQryTradingNotice(DeleOnRspQryTradingNotice func) {(Invoke(_handle, "SetOnRspQryTradingNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询经纪公司交易参数响应
		/// </summary>
		public void SetOnRspQryBrokerTradingParams(DeleOnRspQryBrokerTradingParams func) {(Invoke(_handle, "SetOnRspQryBrokerTradingParams", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询经纪公司交易算法响应
		/// </summary>
		public void SetOnRspQryBrokerTradingAlgos(DeleOnRspQryBrokerTradingAlgos func) {(Invoke(_handle, "SetOnRspQryBrokerTradingAlgos", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///请求查询监控中心用户令牌
		/// </summary>
		public void SetOnRspQueryCFMMCTradingAccountToken(DeleOnRspQueryCFMMCTradingAccountToken func) {(Invoke(_handle, "SetOnRspQueryCFMMCTradingAccountToken", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起银行资金转期货通知
		/// </summary>
		public void SetOnRtnFromBankToFutureByBank(DeleOnRtnFromBankToFutureByBank func) {(Invoke(_handle, "SetOnRtnFromBankToFutureByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起期货资金转银行通知
		/// </summary>
		public void SetOnRtnFromFutureToBankByBank(DeleOnRtnFromFutureToBankByBank func) {(Invoke(_handle, "SetOnRtnFromFutureToBankByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起冲正银行转期货通知
		/// </summary>
		public void SetOnRtnRepealFromBankToFutureByBank(DeleOnRtnRepealFromBankToFutureByBank func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起冲正期货转银行通知
		/// </summary>
		public void SetOnRtnRepealFromFutureToBankByBank(DeleOnRtnRepealFromFutureToBankByBank func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起银行资金转期货通知
		/// </summary>
		public void SetOnRtnFromBankToFutureByFuture(DeleOnRtnFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRtnFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起期货资金转银行通知
		/// </summary>
		public void SetOnRtnFromFutureToBankByFuture(DeleOnRtnFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRtnFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
		/// </summary>
		public void SetOnRtnRepealFromBankToFutureByFutureManual(DeleOnRtnRepealFromBankToFutureByFutureManual func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
		/// </summary>
		public void SetOnRtnRepealFromFutureToBankByFutureManual(DeleOnRtnRepealFromFutureToBankByFutureManual func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起查询银行余额通知
		/// </summary>
		public void SetOnRtnQueryBankBalanceByFuture(DeleOnRtnQueryBankBalanceByFuture func) {(Invoke(_handle, "SetOnRtnQueryBankBalanceByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起银行资金转期货错误回报
		/// </summary>
		public void SetOnErrRtnBankToFutureByFuture(DeleOnErrRtnBankToFutureByFuture func) {(Invoke(_handle, "SetOnErrRtnBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起期货资金转银行错误回报
		/// </summary>
		public void SetOnErrRtnFutureToBankByFuture(DeleOnErrRtnFutureToBankByFuture func) {(Invoke(_handle, "SetOnErrRtnFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///系统运行时期货端手工发起冲正银行转期货错误回报
		/// </summary>
		public void SetOnErrRtnRepealBankToFutureByFutureManual(DeleOnErrRtnRepealBankToFutureByFutureManual func) {(Invoke(_handle, "SetOnErrRtnRepealBankToFutureByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///系统运行时期货端手工发起冲正期货转银行错误回报
		/// </summary>
		public void SetOnErrRtnRepealFutureToBankByFutureManual(DeleOnErrRtnRepealFutureToBankByFutureManual func) {(Invoke(_handle, "SetOnErrRtnRepealFutureToBankByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起查询银行余额错误回报
		/// </summary>
		public void SetOnErrRtnQueryBankBalanceByFuture(DeleOnErrRtnQueryBankBalanceByFuture func) {(Invoke(_handle, "SetOnErrRtnQueryBankBalanceByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
		/// </summary>
		public void SetOnRtnRepealFromBankToFutureByFuture(DeleOnRtnRepealFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
		/// </summary>
		public void SetOnRtnRepealFromFutureToBankByFuture(DeleOnRtnRepealFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起银行资金转期货应答
		/// </summary>
		public void SetOnRspFromBankToFutureByFuture(DeleOnRspFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRspFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起期货资金转银行应答
		/// </summary>
		public void SetOnRspFromFutureToBankByFuture(DeleOnRspFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRspFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///期货发起查询银行余额应答
		/// </summary>
		public void SetOnRspQueryBankAccountMoneyByFuture(DeleOnRspQueryBankAccountMoneyByFuture func) {(Invoke(_handle, "SetOnRspQueryBankAccountMoneyByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起银期开户通知
		/// </summary>
		public void SetOnRtnOpenAccountByBank(DeleOnRtnOpenAccountByBank func) {(Invoke(_handle, "SetOnRtnOpenAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起银期销户通知
		/// </summary>
		public void SetOnRtnCancelAccountByBank(DeleOnRtnCancelAccountByBank func) {(Invoke(_handle, "SetOnRtnCancelAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///银行发起变更银行账号通知
		/// </summary>
		public void SetOnRtnChangeAccountByBank(DeleOnRtnChangeAccountByBank func) {(Invoke(_handle, "SetOnRtnChangeAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
	}
}