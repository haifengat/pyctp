using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;

namespace HaiFeng
{
	public class ctp_trade
	{
		#region Dll Load /UnLoad
		/// <summary>
		/// 原型是 :HMODULE LoadLibrary(LPCTSTR lpFileName);
		/// </summary>
		/// <param name="lpFileName"> DLL 文件名 </param>
		/// <returns> 函数库模块的句柄 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr LoadLibrary(string lpFileName);

		/// <summary>
		/// 原型是 : FARPROC GetProcAddress(HMODULE hModule, LPCWSTR lpProcName);
		/// </summary>
		/// <param name="hModule"> 包含需调用函数的函数库模块的句柄 </param>
		/// <param name="lpProcName"> 调用函数的名称 </param>
		/// <returns> 函数指针 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);

		/// <summary>
		/// 原型是 : BOOL FreeLibrary(HMODULE hModule);
		/// </summary>
		/// <param name="hModule"> 需释放的函数库模块的句柄 </param>
		/// <returns> 是否已释放指定的 Dll </returns>
		[DllImport("kernel32", EntryPoint = "FreeLibrary", SetLastError = true)]
		private static extern bool FreeLibrary(IntPtr hModule);

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
			// 若函数库模块的句柄为空，则抛出异常
			if (pHModule == IntPtr.Zero)
			{
				throw (new Exception(" 函数库模块的句柄为空 , 请确保已进行 LoadDll 操作 !"));
			}
			// 取得函数指针
			IntPtr farProc = GetProcAddress(pHModule, lpProcName);
			// 若函数指针，则抛出异常
			if (farProc == IntPtr.Zero)
			{
				throw (new Exception(" 没有找到 :" + lpProcName + " 这个函数的入口点 "));
			}
			return Marshal.GetDelegateForFunctionPointer(farProc, t);
		}
		#endregion

		IntPtr _handle = IntPtr.Zero, _api = IntPtr.Zero, _spi = IntPtr.Zero;
		private int nRequestID = 0;
		delegate IntPtr Create();
		
		public ctp_trade()
		{
			string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(this.GetType().Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            dll_path = Path.Combine(dll_path, "lib64");
            if (!Directory.Exists(dll_path))
            {
                File.WriteAllBytes("lib.zip", Properties.Resources.lib64);
                ZipFile.ExtractToDirectory("lib.zip", ".");
                File.Delete("lib.zip");
            }
			Environment.CurrentDirectory = dll_path;
			_handle = LoadLibrary(Path.Combine(dll_path, "ctp_trade.dll"));
			if (_handle == IntPtr.Zero)
			{
				throw (new Exception(String.Format("没有找到:", dll_path)));
			}
			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");

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
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRelease(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleInit(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleJoin(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterFront(IntPtr api, string pszFrontAddress);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterNameServer(IntPtr api, string pszNsAddress);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterFensUserInfo(IntPtr api, ref CThostFtdcFensUserInfoField pFensUserInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterSpi(IntPtr api, IntPtr pSpi);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePrivateTopic(IntPtr api, THOST_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePublicTopic(IntPtr api, THOST_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqAuthenticate(IntPtr api, ref CThostFtdcReqAuthenticateField pReqAuthenticateField, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterUserSystemInfo(IntPtr api, ref CThostFtdcUserSystemInfoField pUserSystemInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubmitUserSystemInfo(IntPtr api, ref CThostFtdcUserSystemInfoField pUserSystemInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogin(IntPtr api, ref CThostFtdcReqUserLoginField pReqUserLoginField, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogout(IntPtr api, ref CThostFtdcUserLogoutField pUserLogout, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserPasswordUpdate(IntPtr api, ref CThostFtdcUserPasswordUpdateField pUserPasswordUpdate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqTradingAccountPasswordUpdate(IntPtr api, ref CThostFtdcTradingAccountPasswordUpdateField pTradingAccountPasswordUpdate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserAuthMethod(IntPtr api, ref CThostFtdcReqUserAuthMethodField pReqUserAuthMethod, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqGenUserCaptcha(IntPtr api, ref CThostFtdcReqGenUserCaptchaField pReqGenUserCaptcha, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqGenUserText(IntPtr api, ref CThostFtdcReqGenUserTextField pReqGenUserText, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithCaptcha(IntPtr api, ref CThostFtdcReqUserLoginWithCaptchaField pReqUserLoginWithCaptcha, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithText(IntPtr api, ref CThostFtdcReqUserLoginWithTextField pReqUserLoginWithText, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLoginWithOTP(IntPtr api, ref CThostFtdcReqUserLoginWithOTPField pReqUserLoginWithOTP, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderInsert(IntPtr api, ref CThostFtdcInputOrderField pInputOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqParkedOrderInsert(IntPtr api, ref CThostFtdcParkedOrderField pParkedOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqParkedOrderAction(IntPtr api, ref CThostFtdcParkedOrderActionField pParkedOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderAction(IntPtr api, ref CThostFtdcInputOrderActionField pInputOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMaxOrderVolume(IntPtr api, ref CThostFtdcQryMaxOrderVolumeField pQryMaxOrderVolume, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqSettlementInfoConfirm(IntPtr api, ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqRemoveParkedOrder(IntPtr api, ref CThostFtdcRemoveParkedOrderField pRemoveParkedOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqRemoveParkedOrderAction(IntPtr api, ref CThostFtdcRemoveParkedOrderActionField pRemoveParkedOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderInsert(IntPtr api, ref CThostFtdcInputExecOrderField pInputExecOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderAction(IntPtr api, ref CThostFtdcInputExecOrderActionField pInputExecOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqForQuoteInsert(IntPtr api, ref CThostFtdcInputForQuoteField pInputForQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteInsert(IntPtr api, ref CThostFtdcInputQuoteField pInputQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteAction(IntPtr api, ref CThostFtdcInputQuoteActionField pInputQuoteAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqBatchOrderAction(IntPtr api, ref CThostFtdcInputBatchOrderActionField pInputBatchOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOptionSelfCloseInsert(IntPtr api, ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOptionSelfCloseAction(IntPtr api, ref CThostFtdcInputOptionSelfCloseActionField pInputOptionSelfCloseAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqCombActionInsert(IntPtr api, ref CThostFtdcInputCombActionField pInputCombAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOrder(IntPtr api, ref CThostFtdcQryOrderField pQryOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTrade(IntPtr api, ref CThostFtdcQryTradeField pQryTrade, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPosition(IntPtr api, ref CThostFtdcQryInvestorPositionField pQryInvestorPosition, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingAccount(IntPtr api, ref CThostFtdcQryTradingAccountField pQryTradingAccount, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestor(IntPtr api, ref CThostFtdcQryInvestorField pQryInvestor, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingCode(IntPtr api, ref CThostFtdcQryTradingCodeField pQryTradingCode, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentMarginRate(IntPtr api, ref CThostFtdcQryInstrumentMarginRateField pQryInstrumentMarginRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentCommissionRate(IntPtr api, ref CThostFtdcQryInstrumentCommissionRateField pQryInstrumentCommissionRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchange(IntPtr api, ref CThostFtdcQryExchangeField pQryExchange, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProduct(IntPtr api, ref CThostFtdcQryProductField pQryProduct, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrument(IntPtr api, ref CThostFtdcQryInstrumentField pQryInstrument, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryDepthMarketData(IntPtr api, ref CThostFtdcQryDepthMarketDataField pQryDepthMarketData, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySettlementInfo(IntPtr api, ref CThostFtdcQrySettlementInfoField pQrySettlementInfo, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTransferBank(IntPtr api, ref CThostFtdcQryTransferBankField pQryTransferBank, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPositionDetail(IntPtr api, ref CThostFtdcQryInvestorPositionDetailField pQryInvestorPositionDetail, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryNotice(IntPtr api, ref CThostFtdcQryNoticeField pQryNotice, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySettlementInfoConfirm(IntPtr api, ref CThostFtdcQrySettlementInfoConfirmField pQrySettlementInfoConfirm, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPositionCombineDetail(IntPtr api, ref CThostFtdcQryInvestorPositionCombineDetailField pQryInvestorPositionCombineDetail, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCFMMCTradingAccountKey(IntPtr api, ref CThostFtdcQryCFMMCTradingAccountKeyField pQryCFMMCTradingAccountKey, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryEWarrantOffset(IntPtr api, ref CThostFtdcQryEWarrantOffsetField pQryEWarrantOffset, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorProductGroupMargin(IntPtr api, ref CThostFtdcQryInvestorProductGroupMarginField pQryInvestorProductGroupMargin, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeMarginRate(IntPtr api, ref CThostFtdcQryExchangeMarginRateField pQryExchangeMarginRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeMarginRateAdjust(IntPtr api, ref CThostFtdcQryExchangeMarginRateAdjustField pQryExchangeMarginRateAdjust, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchangeRate(IntPtr api, ref CThostFtdcQryExchangeRateField pQryExchangeRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentACIDMap(IntPtr api, ref CThostFtdcQrySecAgentACIDMapField pQrySecAgentACIDMap, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProductExchRate(IntPtr api, ref CThostFtdcQryProductExchRateField pQryProductExchRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryProductGroup(IntPtr api, ref CThostFtdcQryProductGroupField pQryProductGroup, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMMInstrumentCommissionRate(IntPtr api, ref CThostFtdcQryMMInstrumentCommissionRateField pQryMMInstrumentCommissionRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMMOptionInstrCommRate(IntPtr api, ref CThostFtdcQryMMOptionInstrCommRateField pQryMMOptionInstrCommRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentOrderCommRate(IntPtr api, ref CThostFtdcQryInstrumentOrderCommRateField pQryInstrumentOrderCommRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentTradingAccount(IntPtr api, ref CThostFtdcQryTradingAccountField pQryTradingAccount, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentCheckMode(IntPtr api, ref CThostFtdcQrySecAgentCheckModeField pQrySecAgentCheckMode, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySecAgentTradeInfo(IntPtr api, ref CThostFtdcQrySecAgentTradeInfoField pQrySecAgentTradeInfo, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionInstrTradeCost(IntPtr api, ref CThostFtdcQryOptionInstrTradeCostField pQryOptionInstrTradeCost, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionInstrCommRate(IntPtr api, ref CThostFtdcQryOptionInstrCommRateField pQryOptionInstrCommRate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExecOrder(IntPtr api, ref CThostFtdcQryExecOrderField pQryExecOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryForQuote(IntPtr api, ref CThostFtdcQryForQuoteField pQryForQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryQuote(IntPtr api, ref CThostFtdcQryQuoteField pQryQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOptionSelfClose(IntPtr api, ref CThostFtdcQryOptionSelfCloseField pQryOptionSelfClose, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestUnit(IntPtr api, ref CThostFtdcQryInvestUnitField pQryInvestUnit, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCombInstrumentGuard(IntPtr api, ref CThostFtdcQryCombInstrumentGuardField pQryCombInstrumentGuard, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCombAction(IntPtr api, ref CThostFtdcQryCombActionField pQryCombAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTransferSerial(IntPtr api, ref CThostFtdcQryTransferSerialField pQryTransferSerial, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryAccountregister(IntPtr api, ref CThostFtdcQryAccountregisterField pQryAccountregister, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryContractBank(IntPtr api, ref CThostFtdcQryContractBankField pQryContractBank, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryParkedOrder(IntPtr api, ref CThostFtdcQryParkedOrderField pQryParkedOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryParkedOrderAction(IntPtr api, ref CThostFtdcQryParkedOrderActionField pQryParkedOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingNotice(IntPtr api, ref CThostFtdcQryTradingNoticeField pQryTradingNotice, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryBrokerTradingParams(IntPtr api, ref CThostFtdcQryBrokerTradingParamsField pQryBrokerTradingParams, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryBrokerTradingAlgos(IntPtr api, ref CThostFtdcQryBrokerTradingAlgosField pQryBrokerTradingAlgos, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQueryCFMMCTradingAccountToken(IntPtr api, ref CThostFtdcQueryCFMMCTradingAccountTokenField pQueryCFMMCTradingAccountToken, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqFromBankToFutureByFuture(IntPtr api, ref CThostFtdcReqTransferField pReqTransfer, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqFromFutureToBankByFuture(IntPtr api, ref CThostFtdcReqTransferField pReqTransfer, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQueryBankAccountMoneyByFuture(IntPtr api, ref CThostFtdcReqQueryAccountField pReqQueryAccount, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryClassifiedInstrument(IntPtr api, ref CThostFtdcQryClassifiedInstrumentField pQryClassifiedInstrument, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryCombPromotionParam(IntPtr api, ref CThostFtdcQryCombPromotionParamField pQryCombPromotionParam, int nRequestID);
        public IntPtr Release()
        {
            return (Invoke(_handle, "Release", typeof(DeleRelease)) as DeleRelease)(_api);
        }
                    

        public IntPtr Init()
        {
            return (Invoke(_handle, "Init", typeof(DeleInit)) as DeleInit)(_api);
        }
                    

        public IntPtr Join()
        {
            return (Invoke(_handle, "Join", typeof(DeleJoin)) as DeleJoin)(_api);
        }
                    

        public IntPtr RegisterFront(string pszFrontAddress)
        {
            return (Invoke(_handle, "RegisterFront", typeof(DeleRegisterFront)) as DeleRegisterFront)(_api, pszFrontAddress);
        }
                    

        public IntPtr RegisterNameServer(string pszNsAddress)
        {
            return (Invoke(_handle, "RegisterNameServer", typeof(DeleRegisterNameServer)) as DeleRegisterNameServer)(_api, pszNsAddress);
        }
                    

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
                    

        public IntPtr RegisterSpi(IntPtr pSpi)
        {
            return (Invoke(_handle, "RegisterSpi", typeof(DeleRegisterSpi)) as DeleRegisterSpi)(_api, pSpi);
        }
                    

        public IntPtr SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePrivateTopic", typeof(DeleSubscribePrivateTopic)) as DeleSubscribePrivateTopic)(_api, nResumeType);
        }
                    

        public IntPtr SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePublicTopic", typeof(DeleSubscribePublicTopic)) as DeleSubscribePublicTopic)(_api, nResumeType);
        }
                    

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
                    

        public IntPtr RegisterUserSystemInfo(string BrokerID = "",string UserID = "",int ClientSystemInfoLen = 0,string ClientSystemInfo = "",string reserve1 = "",int ClientIPPort = 0,string ClientLoginTime = "",string ClientAppID = "",string ClientPublicIP = "")
        {
			CThostFtdcUserSystemInfoField pUserSystemInfo = new CThostFtdcUserSystemInfoField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ClientSystemInfoLen = ClientSystemInfoLen,
				ClientSystemInfo = ClientSystemInfo,
				reserve1 = reserve1,
				ClientIPPort = ClientIPPort,
				ClientLoginTime = ClientLoginTime,
				ClientAppID = ClientAppID,
				ClientPublicIP = ClientPublicIP,
			};
            return (Invoke(_handle, "RegisterUserSystemInfo", typeof(DeleRegisterUserSystemInfo)) as DeleRegisterUserSystemInfo)(_api, ref pUserSystemInfo);
        }
                    

        public IntPtr SubmitUserSystemInfo(string BrokerID = "",string UserID = "",int ClientSystemInfoLen = 0,string ClientSystemInfo = "",string reserve1 = "",int ClientIPPort = 0,string ClientLoginTime = "",string ClientAppID = "",string ClientPublicIP = "")
        {
			CThostFtdcUserSystemInfoField pUserSystemInfo = new CThostFtdcUserSystemInfoField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ClientSystemInfoLen = ClientSystemInfoLen,
				ClientSystemInfo = ClientSystemInfo,
				reserve1 = reserve1,
				ClientIPPort = ClientIPPort,
				ClientLoginTime = ClientLoginTime,
				ClientAppID = ClientAppID,
				ClientPublicIP = ClientPublicIP,
			};
            return (Invoke(_handle, "SubmitUserSystemInfo", typeof(DeleSubmitUserSystemInfo)) as DeleSubmitUserSystemInfo)(_api, ref pUserSystemInfo);
        }
                    

        public IntPtr ReqUserLogin(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string OneTimePassword = "",string reserve1 = "",string LoginRemark = "",int ClientIPPort = 0,string ClientIPAddress = "")
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
				reserve1 = reserve1,
				LoginRemark = LoginRemark,
				ClientIPPort = ClientIPPort,
				ClientIPAddress = ClientIPAddress,
			};
            return (Invoke(_handle, "ReqUserLogin", typeof(DeleReqUserLogin)) as DeleReqUserLogin)(_api, ref pReqUserLoginField, this.nRequestID++);
        }
                    

        public IntPtr ReqUserLogout(string BrokerID = "",string UserID = "")
        {
			CThostFtdcUserLogoutField pUserLogout = new CThostFtdcUserLogoutField
			{
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqUserLogout", typeof(DeleReqUserLogout)) as DeleReqUserLogout)(_api, ref pUserLogout, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqUserLoginWithCaptcha(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string reserve1 = "",string LoginRemark = "",string Captcha = "",int ClientIPPort = 0,string ClientIPAddress = "")
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
				reserve1 = reserve1,
				LoginRemark = LoginRemark,
				Captcha = Captcha,
				ClientIPPort = ClientIPPort,
				ClientIPAddress = ClientIPAddress,
			};
            return (Invoke(_handle, "ReqUserLoginWithCaptcha", typeof(DeleReqUserLoginWithCaptcha)) as DeleReqUserLoginWithCaptcha)(_api, ref pReqUserLoginWithCaptcha, this.nRequestID++);
        }
                    

        public IntPtr ReqUserLoginWithText(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string reserve1 = "",string LoginRemark = "",string Text = "",int ClientIPPort = 0,string ClientIPAddress = "")
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
				reserve1 = reserve1,
				LoginRemark = LoginRemark,
				Text = Text,
				ClientIPPort = ClientIPPort,
				ClientIPAddress = ClientIPAddress,
			};
            return (Invoke(_handle, "ReqUserLoginWithText", typeof(DeleReqUserLoginWithText)) as DeleReqUserLoginWithText)(_api, ref pReqUserLoginWithText, this.nRequestID++);
        }
                    

        public IntPtr ReqUserLoginWithOTP(string TradingDay = "",string BrokerID = "",string UserID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string MacAddress = "",string reserve1 = "",string LoginRemark = "",string OTPPassword = "",int ClientIPPort = 0,string ClientIPAddress = "")
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
				reserve1 = reserve1,
				LoginRemark = LoginRemark,
				OTPPassword = OTPPassword,
				ClientIPPort = ClientIPPort,
				ClientIPAddress = ClientIPAddress,
			};
            return (Invoke(_handle, "ReqUserLoginWithOTP", typeof(DeleReqUserLoginWithOTP)) as DeleReqUserLoginWithOTP)(_api, ref pReqUserLoginWithOTP, this.nRequestID++);
        }
                    

        public IntPtr ReqOrderInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string OrderRef = "",string UserID = "",TThostFtdcOrderPriceTypeType OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice,TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,string CombOffsetFlag = "",string CombHedgeFlag = "",double LimitPrice = 0.0,int VolumeTotalOriginal = 0,TThostFtdcTimeConditionType TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC,string GTDDate = "",TThostFtdcVolumeConditionType VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV,int MinVolume = 0,TThostFtdcContingentConditionType ContingentCondition = TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,double StopPrice = 0.0,TThostFtdcForceCloseReasonType ForceCloseReason = TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,int IsAutoSuspend = 0,string BusinessUnit = "",int RequestID = 0,int UserForceClose = 0,int IsSwapOrder = 0,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputOrderField pInputOrder = new CThostFtdcInputOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
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
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqOrderInsert", typeof(DeleReqOrderInsert)) as DeleReqOrderInsert)(_api, ref pInputOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqParkedOrderInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string OrderRef = "",string UserID = "",TThostFtdcOrderPriceTypeType OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice,TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,string CombOffsetFlag = "",string CombHedgeFlag = "",double LimitPrice = 0.0,int VolumeTotalOriginal = 0,TThostFtdcTimeConditionType TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC,string GTDDate = "",TThostFtdcVolumeConditionType VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV,int MinVolume = 0,TThostFtdcContingentConditionType ContingentCondition = TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,double StopPrice = 0.0,TThostFtdcForceCloseReasonType ForceCloseReason = TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,int IsAutoSuspend = 0,string BusinessUnit = "",int RequestID = 0,int UserForceClose = 0,string ExchangeID = "",string ParkedOrderID = "",TThostFtdcUserTypeType UserType = TThostFtdcUserTypeType.THOST_FTDC_UT_Investor,TThostFtdcParkedOrderStatusType Status = TThostFtdcParkedOrderStatusType.THOST_FTDC_PAOS_NotSend,int ErrorID = 0,string ErrorMsg = "",int IsSwapOrder = 0,string AccountID = "",string CurrencyID = "",string ClientID = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcParkedOrderField pParkedOrder = new CThostFtdcParkedOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
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
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqParkedOrderInsert", typeof(DeleReqParkedOrderInsert)) as DeleReqParkedOrderInsert)(_api, ref pParkedOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqParkedOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 0,string OrderRef = "",int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string OrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,double LimitPrice = 0.0,int VolumeChange = 0,string UserID = "",string reserve1 = "",string ParkedOrderActionID = "",TThostFtdcUserTypeType UserType = TThostFtdcUserTypeType.THOST_FTDC_UT_Investor,TThostFtdcParkedOrderStatusType Status = TThostFtdcParkedOrderStatusType.THOST_FTDC_PAOS_NotSend,int ErrorID = 0,string ErrorMsg = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
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
				reserve1 = reserve1,
				ParkedOrderActionID = ParkedOrderActionID,
				UserType = UserType,
				Status = Status,
				ErrorID = ErrorID,
				ErrorMsg = ErrorMsg,
				InvestUnitID = InvestUnitID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqParkedOrderAction", typeof(DeleReqParkedOrderAction)) as DeleReqParkedOrderAction)(_api, ref pParkedOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 0,string OrderRef = "",int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string OrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,double LimitPrice = 0.0,int VolumeChange = 0,string UserID = "",string reserve1 = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
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
				reserve1 = reserve1,
				InvestUnitID = InvestUnitID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqOrderAction", typeof(DeleReqOrderAction)) as DeleReqOrderAction)(_api, ref pInputOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqQryMaxOrderVolume(string BrokerID = "",string InvestorID = "",string reserve1 = "",TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,TThostFtdcOffsetFlagType OffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,int MaxVolume = 0,string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryMaxOrderVolumeField pQryMaxOrderVolume = new CThostFtdcQryMaxOrderVolumeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				Direction = Direction,
				OffsetFlag = OffsetFlag,
				HedgeFlag = HedgeFlag,
				MaxVolume = MaxVolume,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryMaxOrderVolume", typeof(DeleReqQryMaxOrderVolume)) as DeleReqQryMaxOrderVolume)(_api, ref pQryMaxOrderVolume, this.nRequestID++);
        }
                    

        public IntPtr ReqSettlementInfoConfirm(string BrokerID = "",string InvestorID = "",string ConfirmDate = "",string ConfirmTime = "",int SettlementID = 0,string AccountID = "",string CurrencyID = "")
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
                    

        public IntPtr ReqExecOrderInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExecOrderRef = "",string UserID = "",int Volume = 0,int RequestID = 0,string BusinessUnit = "",TThostFtdcOffsetFlagType OffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcActionTypeType ActionType = TThostFtdcActionTypeType.THOST_FTDC_ACTP_Exec,TThostFtdcPosiDirectionType PosiDirection = TThostFtdcPosiDirectionType.THOST_FTDC_PD_Net,TThostFtdcExecOrderPositionFlagType ReservePositionFlag = TThostFtdcExecOrderPositionFlagType.THOST_FTDC_EOPF_Reserve,TThostFtdcExecOrderCloseFlagType CloseFlag = TThostFtdcExecOrderCloseFlagType.THOST_FTDC_EOCF_AutoClose,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputExecOrderField pInputExecOrder = new CThostFtdcInputExecOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
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
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqExecOrderInsert", typeof(DeleReqExecOrderInsert)) as DeleReqExecOrderInsert)(_api, ref pInputExecOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqExecOrderAction(string BrokerID = "",string InvestorID = "",int ExecOrderActionRef = 0,string ExecOrderRef = "",int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string ExecOrderSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string reserve1 = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
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
				reserve1 = reserve1,
				InvestUnitID = InvestUnitID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqExecOrderAction", typeof(DeleReqExecOrderAction)) as DeleReqExecOrderAction)(_api, ref pInputExecOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqForQuoteInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ForQuoteRef = "",string UserID = "",string ExchangeID = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputForQuoteField pInputForQuote = new CThostFtdcInputForQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ForQuoteRef = ForQuoteRef,
				UserID = UserID,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqForQuoteInsert", typeof(DeleReqForQuoteInsert)) as DeleReqForQuoteInsert)(_api, ref pInputForQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqQuoteInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string QuoteRef = "",string UserID = "",double AskPrice = 0.0,double BidPrice = 0.0,int AskVolume = 0,int BidVolume = 0,int RequestID = 0,string BusinessUnit = "",TThostFtdcOffsetFlagType AskOffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcOffsetFlagType BidOffsetFlag = TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open,TThostFtdcHedgeFlagType AskHedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcHedgeFlagType BidHedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string AskOrderRef = "",string BidOrderRef = "",string ForQuoteSysID = "",string ExchangeID = "",string InvestUnitID = "",string ClientID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputQuoteField pInputQuote = new CThostFtdcInputQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
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
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqQuoteInsert", typeof(DeleReqQuoteInsert)) as DeleReqQuoteInsert)(_api, ref pInputQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqQuoteAction(string BrokerID = "",string InvestorID = "",int QuoteActionRef = 0,string QuoteRef = "",int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string QuoteSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string reserve1 = "",string InvestUnitID = "",string ClientID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
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
				reserve1 = reserve1,
				InvestUnitID = InvestUnitID,
				ClientID = ClientID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqQuoteAction", typeof(DeleReqQuoteAction)) as DeleReqQuoteAction)(_api, ref pInputQuoteAction, this.nRequestID++);
        }
                    

        public IntPtr ReqBatchOrderAction(string BrokerID = "",string InvestorID = "",int OrderActionRef = 0,int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string UserID = "",string InvestUnitID = "",string reserve1 = "",string MacAddress = "",string IPAddress = "")
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
				reserve1 = reserve1,
				MacAddress = MacAddress,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqBatchOrderAction", typeof(DeleReqBatchOrderAction)) as DeleReqBatchOrderAction)(_api, ref pInputBatchOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqOptionSelfCloseInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string OptionSelfCloseRef = "",string UserID = "",int Volume = 0,int RequestID = 0,string BusinessUnit = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag = TThostFtdcOptSelfCloseFlagType.THOST_FTDC_OSCF_CloseSelfOptionPosition,string ExchangeID = "",string InvestUnitID = "",string AccountID = "",string CurrencyID = "",string ClientID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose = new CThostFtdcInputOptionSelfCloseField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
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
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqOptionSelfCloseInsert", typeof(DeleReqOptionSelfCloseInsert)) as DeleReqOptionSelfCloseInsert)(_api, ref pInputOptionSelfClose, this.nRequestID++);
        }
                    

        public IntPtr ReqOptionSelfCloseAction(string BrokerID = "",string InvestorID = "",int OptionSelfCloseActionRef = 0,string OptionSelfCloseRef = "",int RequestID = 0,int FrontID = 0,int SessionID = 0,string ExchangeID = "",string OptionSelfCloseSysID = "",TThostFtdcActionFlagType ActionFlag = TThostFtdcActionFlagType.THOST_FTDC_AF_Delete,string UserID = "",string reserve1 = "",string InvestUnitID = "",string reserve2 = "",string MacAddress = "",string InstrumentID = "",string IPAddress = "")
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
				reserve1 = reserve1,
				InvestUnitID = InvestUnitID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqOptionSelfCloseAction", typeof(DeleReqOptionSelfCloseAction)) as DeleReqOptionSelfCloseAction)(_api, ref pInputOptionSelfCloseAction, this.nRequestID++);
        }
                    

        public IntPtr ReqCombActionInsert(string BrokerID = "",string InvestorID = "",string reserve1 = "",string CombActionRef = "",string UserID = "",TThostFtdcDirectionType Direction = TThostFtdcDirectionType.THOST_FTDC_D_Buy,int Volume = 0,TThostFtdcCombDirectionType CombDirection = TThostFtdcCombDirectionType.THOST_FTDC_CMDR_Comb,TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string reserve2 = "",string MacAddress = "",string InvestUnitID = "",int FrontID = 0,int SessionID = 0,string InstrumentID = "",string IPAddress = "")
        {
			CThostFtdcInputCombActionField pInputCombAction = new CThostFtdcInputCombActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				CombActionRef = CombActionRef,
				UserID = UserID,
				Direction = Direction,
				Volume = Volume,
				CombDirection = CombDirection,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				reserve2 = reserve2,
				MacAddress = MacAddress,
				InvestUnitID = InvestUnitID,
				FrontID = FrontID,
				SessionID = SessionID,
				InstrumentID = InstrumentID,
				IPAddress = IPAddress,
			};
            return (Invoke(_handle, "ReqCombActionInsert", typeof(DeleReqCombActionInsert)) as DeleReqCombActionInsert)(_api, ref pInputCombAction, this.nRequestID++);
        }
                    

        public IntPtr ReqQryOrder(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string OrderSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryOrderField pQryOrder = new CThostFtdcQryOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryOrder", typeof(DeleReqQryOrder)) as DeleReqQryOrder)(_api, ref pQryOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqQryTrade(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string TradeID = "",string TradeTimeStart = "",string TradeTimeEnd = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryTradeField pQryTrade = new CThostFtdcQryTradeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				TradeID = TradeID,
				TradeTimeStart = TradeTimeStart,
				TradeTimeEnd = TradeTimeEnd,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryTrade", typeof(DeleReqQryTrade)) as DeleReqQryTrade)(_api, ref pQryTrade, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorPosition(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryInvestorPositionField pQryInvestorPosition = new CThostFtdcQryInvestorPositionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInvestorPosition", typeof(DeleReqQryInvestorPosition)) as DeleReqQryInvestorPosition)(_api, ref pQryInvestorPosition, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryInvestor(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQryInvestorField pQryInvestor = new CThostFtdcQryInvestorField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQryInvestor", typeof(DeleReqQryInvestor)) as DeleReqQryInvestor)(_api, ref pQryInvestor, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryInstrumentMarginRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryInstrumentMarginRateField pQryInstrumentMarginRate = new CThostFtdcQryInstrumentMarginRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrumentMarginRate", typeof(DeleReqQryInstrumentMarginRate)) as DeleReqQryInstrumentMarginRate)(_api, ref pQryInstrumentMarginRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInstrumentCommissionRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryInstrumentCommissionRateField pQryInstrumentCommissionRate = new CThostFtdcQryInstrumentCommissionRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrumentCommissionRate", typeof(DeleReqQryInstrumentCommissionRate)) as DeleReqQryInstrumentCommissionRate)(_api, ref pQryInstrumentCommissionRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryExchange(string ExchangeID = "")
        {
			CThostFtdcQryExchangeField pQryExchange = new CThostFtdcQryExchangeField
			{
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryExchange", typeof(DeleReqQryExchange)) as DeleReqQryExchange)(_api, ref pQryExchange, this.nRequestID++);
        }
                    

        public IntPtr ReqQryProduct(string reserve1 = "",TThostFtdcProductClassType ProductClass = TThostFtdcProductClassType.THOST_FTDC_PC_Futures,string ExchangeID = "",string ProductID = "")
        {
			CThostFtdcQryProductField pQryProduct = new CThostFtdcQryProductField
			{
				reserve1 = reserve1,
				ProductClass = ProductClass,
				ExchangeID = ExchangeID,
				ProductID = ProductID,
			};
            return (Invoke(_handle, "ReqQryProduct", typeof(DeleReqQryProduct)) as DeleReqQryProduct)(_api, ref pQryProduct, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInstrument(string reserve1 = "",string ExchangeID = "",string reserve2 = "",string reserve3 = "",string InstrumentID = "",string ExchangeInstID = "",string ProductID = "")
        {
			CThostFtdcQryInstrumentField pQryInstrument = new CThostFtdcQryInstrumentField
			{
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				reserve2 = reserve2,
				reserve3 = reserve3,
				InstrumentID = InstrumentID,
				ExchangeInstID = ExchangeInstID,
				ProductID = ProductID,
			};
            return (Invoke(_handle, "ReqQryInstrument", typeof(DeleReqQryInstrument)) as DeleReqQryInstrument)(_api, ref pQryInstrument, this.nRequestID++);
        }
                    

        public IntPtr ReqQryDepthMarketData(string reserve1 = "",string ExchangeID = "",string InstrumentID = "")
        {
			CThostFtdcQryDepthMarketDataField pQryDepthMarketData = new CThostFtdcQryDepthMarketDataField
			{
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryDepthMarketData", typeof(DeleReqQryDepthMarketData)) as DeleReqQryDepthMarketData)(_api, ref pQryDepthMarketData, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryTransferBank(string BankID = "",string BankBrchID = "")
        {
			CThostFtdcQryTransferBankField pQryTransferBank = new CThostFtdcQryTransferBankField
			{
				BankID = BankID,
				BankBrchID = BankBrchID,
			};
            return (Invoke(_handle, "ReqQryTransferBank", typeof(DeleReqQryTransferBank)) as DeleReqQryTransferBank)(_api, ref pQryTransferBank, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorPositionDetail(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryInvestorPositionDetailField pQryInvestorPositionDetail = new CThostFtdcQryInvestorPositionDetailField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInvestorPositionDetail", typeof(DeleReqQryInvestorPositionDetail)) as DeleReqQryInvestorPositionDetail)(_api, ref pQryInvestorPositionDetail, this.nRequestID++);
        }
                    

        public IntPtr ReqQryNotice(string BrokerID = "")
        {
			CThostFtdcQryNoticeField pQryNotice = new CThostFtdcQryNoticeField
			{
				BrokerID = BrokerID,
			};
            return (Invoke(_handle, "ReqQryNotice", typeof(DeleReqQryNotice)) as DeleReqQryNotice)(_api, ref pQryNotice, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryInvestorPositionCombineDetail(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string CombInstrumentID = "")
        {
			CThostFtdcQryInvestorPositionCombineDetailField pQryInvestorPositionCombineDetail = new CThostFtdcQryInvestorPositionCombineDetailField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				CombInstrumentID = CombInstrumentID,
			};
            return (Invoke(_handle, "ReqQryInvestorPositionCombineDetail", typeof(DeleReqQryInvestorPositionCombineDetail)) as DeleReqQryInvestorPositionCombineDetail)(_api, ref pQryInvestorPositionCombineDetail, this.nRequestID++);
        }
                    

        public IntPtr ReqQryCFMMCTradingAccountKey(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQryCFMMCTradingAccountKeyField pQryCFMMCTradingAccountKey = new CThostFtdcQryCFMMCTradingAccountKeyField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQryCFMMCTradingAccountKey", typeof(DeleReqQryCFMMCTradingAccountKey)) as DeleReqQryCFMMCTradingAccountKey)(_api, ref pQryCFMMCTradingAccountKey, this.nRequestID++);
        }
                    

        public IntPtr ReqQryEWarrantOffset(string BrokerID = "",string InvestorID = "",string ExchangeID = "",string reserve1 = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryEWarrantOffsetField pQryEWarrantOffset = new CThostFtdcQryEWarrantOffsetField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				reserve1 = reserve1,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryEWarrantOffset", typeof(DeleReqQryEWarrantOffset)) as DeleReqQryEWarrantOffset)(_api, ref pQryEWarrantOffset, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorProductGroupMargin(string BrokerID = "",string InvestorID = "",string reserve1 = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string InvestUnitID = "",string ProductGroupID = "")
        {
			CThostFtdcQryInvestorProductGroupMarginField pQryInvestorProductGroupMargin = new CThostFtdcQryInvestorProductGroupMarginField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				ProductGroupID = ProductGroupID,
			};
            return (Invoke(_handle, "ReqQryInvestorProductGroupMargin", typeof(DeleReqQryInvestorProductGroupMargin)) as DeleReqQryInvestorProductGroupMargin)(_api, ref pQryInvestorProductGroupMargin, this.nRequestID++);
        }
                    

        public IntPtr ReqQryExchangeMarginRate(string BrokerID = "",string reserve1 = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string ExchangeID = "",string InstrumentID = "")
        {
			CThostFtdcQryExchangeMarginRateField pQryExchangeMarginRate = new CThostFtdcQryExchangeMarginRateField
			{
				BrokerID = BrokerID,
				reserve1 = reserve1,
				HedgeFlag = HedgeFlag,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryExchangeMarginRate", typeof(DeleReqQryExchangeMarginRate)) as DeleReqQryExchangeMarginRate)(_api, ref pQryExchangeMarginRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryExchangeMarginRateAdjust(string BrokerID = "",string reserve1 = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,string InstrumentID = "")
        {
			CThostFtdcQryExchangeMarginRateAdjustField pQryExchangeMarginRateAdjust = new CThostFtdcQryExchangeMarginRateAdjustField
			{
				BrokerID = BrokerID,
				reserve1 = reserve1,
				HedgeFlag = HedgeFlag,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryExchangeMarginRateAdjust", typeof(DeleReqQryExchangeMarginRateAdjust)) as DeleReqQryExchangeMarginRateAdjust)(_api, ref pQryExchangeMarginRateAdjust, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryProductExchRate(string reserve1 = "",string ExchangeID = "",string ProductID = "")
        {
			CThostFtdcQryProductExchRateField pQryProductExchRate = new CThostFtdcQryProductExchRateField
			{
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				ProductID = ProductID,
			};
            return (Invoke(_handle, "ReqQryProductExchRate", typeof(DeleReqQryProductExchRate)) as DeleReqQryProductExchRate)(_api, ref pQryProductExchRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryProductGroup(string reserve1 = "",string ExchangeID = "",string ProductID = "")
        {
			CThostFtdcQryProductGroupField pQryProductGroup = new CThostFtdcQryProductGroupField
			{
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				ProductID = ProductID,
			};
            return (Invoke(_handle, "ReqQryProductGroup", typeof(DeleReqQryProductGroup)) as DeleReqQryProductGroup)(_api, ref pQryProductGroup, this.nRequestID++);
        }
                    

        public IntPtr ReqQryMMInstrumentCommissionRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",string InstrumentID = "")
        {
			CThostFtdcQryMMInstrumentCommissionRateField pQryMMInstrumentCommissionRate = new CThostFtdcQryMMInstrumentCommissionRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryMMInstrumentCommissionRate", typeof(DeleReqQryMMInstrumentCommissionRate)) as DeleReqQryMMInstrumentCommissionRate)(_api, ref pQryMMInstrumentCommissionRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryMMOptionInstrCommRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",string InstrumentID = "")
        {
			CThostFtdcQryMMOptionInstrCommRateField pQryMMOptionInstrCommRate = new CThostFtdcQryMMOptionInstrCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryMMOptionInstrCommRate", typeof(DeleReqQryMMOptionInstrCommRate)) as DeleReqQryMMOptionInstrCommRate)(_api, ref pQryMMOptionInstrCommRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInstrumentOrderCommRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",string InstrumentID = "")
        {
			CThostFtdcQryInstrumentOrderCommRateField pQryInstrumentOrderCommRate = new CThostFtdcQryInstrumentOrderCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrumentOrderCommRate", typeof(DeleReqQryInstrumentOrderCommRate)) as DeleReqQryInstrumentOrderCommRate)(_api, ref pQryInstrumentOrderCommRate, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQrySecAgentCheckMode(string BrokerID = "",string InvestorID = "")
        {
			CThostFtdcQrySecAgentCheckModeField pQrySecAgentCheckMode = new CThostFtdcQrySecAgentCheckModeField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQrySecAgentCheckMode", typeof(DeleReqQrySecAgentCheckMode)) as DeleReqQrySecAgentCheckMode)(_api, ref pQrySecAgentCheckMode, this.nRequestID++);
        }
                    

        public IntPtr ReqQrySecAgentTradeInfo(string BrokerID = "",string BrokerSecAgentID = "")
        {
			CThostFtdcQrySecAgentTradeInfoField pQrySecAgentTradeInfo = new CThostFtdcQrySecAgentTradeInfoField
			{
				BrokerID = BrokerID,
				BrokerSecAgentID = BrokerSecAgentID,
			};
            return (Invoke(_handle, "ReqQrySecAgentTradeInfo", typeof(DeleReqQrySecAgentTradeInfo)) as DeleReqQrySecAgentTradeInfo)(_api, ref pQrySecAgentTradeInfo, this.nRequestID++);
        }
                    

        public IntPtr ReqQryOptionInstrTradeCost(string BrokerID = "",string InvestorID = "",string reserve1 = "",TThostFtdcHedgeFlagType HedgeFlag = TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation,double InputPrice = 0.0,double UnderlyingPrice = 0.0,string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryOptionInstrTradeCostField pQryOptionInstrTradeCost = new CThostFtdcQryOptionInstrTradeCostField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				HedgeFlag = HedgeFlag,
				InputPrice = InputPrice,
				UnderlyingPrice = UnderlyingPrice,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryOptionInstrTradeCost", typeof(DeleReqQryOptionInstrTradeCost)) as DeleReqQryOptionInstrTradeCost)(_api, ref pQryOptionInstrTradeCost, this.nRequestID++);
        }
                    

        public IntPtr ReqQryOptionInstrCommRate(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryOptionInstrCommRateField pQryOptionInstrCommRate = new CThostFtdcQryOptionInstrCommRateField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryOptionInstrCommRate", typeof(DeleReqQryOptionInstrCommRate)) as DeleReqQryOptionInstrCommRate)(_api, ref pQryOptionInstrCommRate, this.nRequestID++);
        }
                    

        public IntPtr ReqQryExecOrder(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string ExecOrderSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InstrumentID = "")
        {
			CThostFtdcQryExecOrderField pQryExecOrder = new CThostFtdcQryExecOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				ExecOrderSysID = ExecOrderSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryExecOrder", typeof(DeleReqQryExecOrder)) as DeleReqQryExecOrder)(_api, ref pQryExecOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqQryForQuote(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryForQuoteField pQryForQuote = new CThostFtdcQryForQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryForQuote", typeof(DeleReqQryForQuote)) as DeleReqQryForQuote)(_api, ref pQryForQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqQryQuote(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string QuoteSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryQuoteField pQryQuote = new CThostFtdcQryQuoteField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				QuoteSysID = QuoteSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryQuote", typeof(DeleReqQryQuote)) as DeleReqQryQuote)(_api, ref pQryQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqQryOptionSelfClose(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string OptionSelfCloseSysID = "",string InsertTimeStart = "",string InsertTimeEnd = "",string InstrumentID = "")
        {
			CThostFtdcQryOptionSelfCloseField pQryOptionSelfClose = new CThostFtdcQryOptionSelfCloseField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				OptionSelfCloseSysID = OptionSelfCloseSysID,
				InsertTimeStart = InsertTimeStart,
				InsertTimeEnd = InsertTimeEnd,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryOptionSelfClose", typeof(DeleReqQryOptionSelfClose)) as DeleReqQryOptionSelfClose)(_api, ref pQryOptionSelfClose, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryCombInstrumentGuard(string BrokerID = "",string reserve1 = "",string ExchangeID = "",string InstrumentID = "")
        {
			CThostFtdcQryCombInstrumentGuardField pQryCombInstrumentGuard = new CThostFtdcQryCombInstrumentGuardField
			{
				BrokerID = BrokerID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryCombInstrumentGuard", typeof(DeleReqQryCombInstrumentGuard)) as DeleReqQryCombInstrumentGuard)(_api, ref pQryCombInstrumentGuard, this.nRequestID++);
        }
                    

        public IntPtr ReqQryCombAction(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryCombActionField pQryCombAction = new CThostFtdcQryCombActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryCombAction", typeof(DeleReqQryCombAction)) as DeleReqQryCombAction)(_api, ref pQryCombAction, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryParkedOrder(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryParkedOrderField pQryParkedOrder = new CThostFtdcQryParkedOrderField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryParkedOrder", typeof(DeleReqQryParkedOrder)) as DeleReqQryParkedOrder)(_api, ref pQryParkedOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqQryParkedOrderAction(string BrokerID = "",string InvestorID = "",string reserve1 = "",string ExchangeID = "",string InvestUnitID = "",string InstrumentID = "")
        {
			CThostFtdcQryParkedOrderActionField pQryParkedOrderAction = new CThostFtdcQryParkedOrderActionField
			{
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				reserve1 = reserve1,
				ExchangeID = ExchangeID,
				InvestUnitID = InvestUnitID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryParkedOrderAction", typeof(DeleReqQryParkedOrderAction)) as DeleReqQryParkedOrderAction)(_api, ref pQryParkedOrderAction, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqQryBrokerTradingAlgos(string BrokerID = "",string ExchangeID = "",string reserve1 = "",string InstrumentID = "")
        {
			CThostFtdcQryBrokerTradingAlgosField pQryBrokerTradingAlgos = new CThostFtdcQryBrokerTradingAlgosField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				reserve1 = reserve1,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryBrokerTradingAlgos", typeof(DeleReqQryBrokerTradingAlgos)) as DeleReqQryBrokerTradingAlgos)(_api, ref pQryBrokerTradingAlgos, this.nRequestID++);
        }
                    

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
                    

        public IntPtr ReqFromBankToFutureByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 0,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 0,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int InstallID = 0,int FutureSerial = 0,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",double TradeAmount = 0.0,double FutureFetchAmount = 0.0,TThostFtdcFeePayFlagType FeePayFlag = TThostFtdcFeePayFlagType.THOST_FTDC_FPF_BEN,double CustFee = 0.0,double BrokerFee = 0.0,string Message = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 0,int TID = 0,TThostFtdcTransferStatusType TransferStatus = TThostFtdcTransferStatusType.THOST_FTDC_TRFS_Normal,string LongCustomerName = "")
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
                    

        public IntPtr ReqFromFutureToBankByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 0,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 0,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int InstallID = 0,int FutureSerial = 0,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",double TradeAmount = 0.0,double FutureFetchAmount = 0.0,TThostFtdcFeePayFlagType FeePayFlag = TThostFtdcFeePayFlagType.THOST_FTDC_FPF_BEN,double CustFee = 0.0,double BrokerFee = 0.0,string Message = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 0,int TID = 0,TThostFtdcTransferStatusType TransferStatus = TThostFtdcTransferStatusType.THOST_FTDC_TRFS_Normal,string LongCustomerName = "")
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
                    

        public IntPtr ReqQueryBankAccountMoneyByFuture(string TradeCode = "",string BankID = "",string BankBranchID = "",string BrokerID = "",string BrokerBranchID = "",string TradeDate = "",string TradeTime = "",string BankSerial = "",string TradingDay = "",int PlateSerial = 0,TThostFtdcLastFragmentType LastFragment = TThostFtdcLastFragmentType.THOST_FTDC_LF_Yes,int SessionID = 0,string CustomerName = "",TThostFtdcIdCardTypeType IdCardType = TThostFtdcIdCardTypeType.THOST_FTDC_ICT_EID,string IdentifiedCardNo = "",TThostFtdcCustTypeType CustType = TThostFtdcCustTypeType.THOST_FTDC_CUSTT_Person,string BankAccount = "",string BankPassWord = "",string AccountID = "",string Password = "",int FutureSerial = 0,int InstallID = 0,string UserID = "",TThostFtdcYesNoIndicatorType VerifyCertNoFlag = TThostFtdcYesNoIndicatorType.THOST_FTDC_YNI_Yes,string CurrencyID = "",string Digest = "",TThostFtdcBankAccTypeType BankAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string DeviceID = "",TThostFtdcBankAccTypeType BankSecuAccType = TThostFtdcBankAccTypeType.THOST_FTDC_BAT_BankBook,string BrokerIDByBank = "",string BankSecuAcc = "",TThostFtdcPwdFlagType BankPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,TThostFtdcPwdFlagType SecuPwdFlag = TThostFtdcPwdFlagType.THOST_FTDC_BPWDF_NoCheck,string OperNo = "",int RequestID = 0,int TID = 0,string LongCustomerName = "")
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
                    

        public IntPtr ReqQryClassifiedInstrument(string InstrumentID = "",string ExchangeID = "",string ExchangeInstID = "",string ProductID = "",TThostFtdcTradingTypeType TradingType = TThostFtdcTradingTypeType.THOST_FTDC_TD_ALL,TThostFtdcClassTypeType ClassType = TThostFtdcClassTypeType.THOST_FTDC_INS_ALL)
        {
			CThostFtdcQryClassifiedInstrumentField pQryClassifiedInstrument = new CThostFtdcQryClassifiedInstrumentField
			{
				InstrumentID = InstrumentID,
				ExchangeID = ExchangeID,
				ExchangeInstID = ExchangeInstID,
				ProductID = ProductID,
				TradingType = TradingType,
				ClassType = ClassType,
			};
            return (Invoke(_handle, "ReqQryClassifiedInstrument", typeof(DeleReqQryClassifiedInstrument)) as DeleReqQryClassifiedInstrument)(_api, ref pQryClassifiedInstrument, this.nRequestID++);
        }
                    

        public IntPtr ReqQryCombPromotionParam(string ExchangeID = "",string InstrumentID = "")
        {
			CThostFtdcQryCombPromotionParamField pQryCombPromotionParam = new CThostFtdcQryCombPromotionParamField
			{
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryCombPromotionParam", typeof(DeleReqQryCombPromotionParam)) as DeleReqQryCombPromotionParam)(_api, ref pQryCombPromotionParam, this.nRequestID++);
        }
                    
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		delegate void DeleSet(IntPtr spi, Delegate func);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontConnected();
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontDisconnected(int nReason);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnHeartBeatWarning(int nTimeLapse);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspAuthenticate(ref CThostFtdcRspAuthenticateField pRspAuthenticateField,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogout(ref CThostFtdcUserLogoutField pUserLogout,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserPasswordUpdate(ref CThostFtdcUserPasswordUpdateField pUserPasswordUpdate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspTradingAccountPasswordUpdate(ref CThostFtdcTradingAccountPasswordUpdateField pTradingAccountPasswordUpdate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserAuthMethod(ref CThostFtdcRspUserAuthMethodField pRspUserAuthMethod,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspGenUserCaptcha(ref CThostFtdcRspGenUserCaptchaField pRspGenUserCaptcha,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspGenUserText(ref CThostFtdcRspGenUserTextField pRspGenUserText,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderInsert(ref CThostFtdcInputOrderField pInputOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspParkedOrderInsert(ref CThostFtdcParkedOrderField pParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspParkedOrderAction(ref CThostFtdcParkedOrderActionField pParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderAction(ref CThostFtdcInputOrderActionField pInputOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMaxOrderVolume(ref CThostFtdcQryMaxOrderVolumeField pQryMaxOrderVolume,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSettlementInfoConfirm(ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspRemoveParkedOrder(ref CThostFtdcRemoveParkedOrderField pRemoveParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspRemoveParkedOrderAction(ref CThostFtdcRemoveParkedOrderActionField pRemoveParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderInsert(ref CThostFtdcInputExecOrderField pInputExecOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderAction(ref CThostFtdcInputExecOrderActionField pInputExecOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspForQuoteInsert(ref CThostFtdcInputForQuoteField pInputForQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteInsert(ref CThostFtdcInputQuoteField pInputQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteAction(ref CThostFtdcInputQuoteActionField pInputQuoteAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspBatchOrderAction(ref CThostFtdcInputBatchOrderActionField pInputBatchOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOptionSelfCloseInsert(ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOptionSelfCloseAction(ref CThostFtdcInputOptionSelfCloseActionField pInputOptionSelfCloseAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspCombActionInsert(ref CThostFtdcInputCombActionField pInputCombAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOrder(ref CThostFtdcOrderField pOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTrade(ref CThostFtdcTradeField pTrade,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPosition(ref CThostFtdcInvestorPositionField pInvestorPosition,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingAccount(ref CThostFtdcTradingAccountField pTradingAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestor(ref CThostFtdcInvestorField pInvestor,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingCode(ref CThostFtdcTradingCodeField pTradingCode,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentMarginRate(ref CThostFtdcInstrumentMarginRateField pInstrumentMarginRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentCommissionRate(ref CThostFtdcInstrumentCommissionRateField pInstrumentCommissionRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchange(ref CThostFtdcExchangeField pExchange,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProduct(ref CThostFtdcProductField pProduct,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrument(ref CThostFtdcInstrumentField pInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryDepthMarketData(ref CThostFtdcDepthMarketDataField pDepthMarketData,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySettlementInfo(ref CThostFtdcSettlementInfoField pSettlementInfo,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTransferBank(ref CThostFtdcTransferBankField pTransferBank,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPositionDetail(ref CThostFtdcInvestorPositionDetailField pInvestorPositionDetail,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryNotice(ref CThostFtdcNoticeField pNotice,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySettlementInfoConfirm(ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPositionCombineDetail(ref CThostFtdcInvestorPositionCombineDetailField pInvestorPositionCombineDetail,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCFMMCTradingAccountKey(ref CThostFtdcCFMMCTradingAccountKeyField pCFMMCTradingAccountKey,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryEWarrantOffset(ref CThostFtdcEWarrantOffsetField pEWarrantOffset,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorProductGroupMargin(ref CThostFtdcInvestorProductGroupMarginField pInvestorProductGroupMargin,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeMarginRate(ref CThostFtdcExchangeMarginRateField pExchangeMarginRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeMarginRateAdjust(ref CThostFtdcExchangeMarginRateAdjustField pExchangeMarginRateAdjust,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchangeRate(ref CThostFtdcExchangeRateField pExchangeRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentACIDMap(ref CThostFtdcSecAgentACIDMapField pSecAgentACIDMap,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProductExchRate(ref CThostFtdcProductExchRateField pProductExchRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryProductGroup(ref CThostFtdcProductGroupField pProductGroup,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMMInstrumentCommissionRate(ref CThostFtdcMMInstrumentCommissionRateField pMMInstrumentCommissionRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMMOptionInstrCommRate(ref CThostFtdcMMOptionInstrCommRateField pMMOptionInstrCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentOrderCommRate(ref CThostFtdcInstrumentOrderCommRateField pInstrumentOrderCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentTradingAccount(ref CThostFtdcTradingAccountField pTradingAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentCheckMode(ref CThostFtdcSecAgentCheckModeField pSecAgentCheckMode,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySecAgentTradeInfo(ref CThostFtdcSecAgentTradeInfoField pSecAgentTradeInfo,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionInstrTradeCost(ref CThostFtdcOptionInstrTradeCostField pOptionInstrTradeCost,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionInstrCommRate(ref CThostFtdcOptionInstrCommRateField pOptionInstrCommRate,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExecOrder(ref CThostFtdcExecOrderField pExecOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryForQuote(ref CThostFtdcForQuoteField pForQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryQuote(ref CThostFtdcQuoteField pQuote,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOptionSelfClose(ref CThostFtdcOptionSelfCloseField pOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestUnit(ref CThostFtdcInvestUnitField pInvestUnit,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCombInstrumentGuard(ref CThostFtdcCombInstrumentGuardField pCombInstrumentGuard,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCombAction(ref CThostFtdcCombActionField pCombAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTransferSerial(ref CThostFtdcTransferSerialField pTransferSerial,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryAccountregister(ref CThostFtdcAccountregisterField pAccountregister,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspError(ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOrder(ref CThostFtdcOrderField pOrder);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTrade(ref CThostFtdcTradeField pTrade);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderInsert(ref CThostFtdcInputOrderField pInputOrder,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderAction(ref CThostFtdcOrderActionField pOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnInstrumentStatus(ref CThostFtdcInstrumentStatusField pInstrumentStatus);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnBulletin(ref CThostFtdcBulletinField pBulletin);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTradingNotice(ref CThostFtdcTradingNoticeInfoField pTradingNoticeInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnErrorConditionalOrder(ref CThostFtdcErrorConditionalOrderField pErrorConditionalOrder);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnExecOrder(ref CThostFtdcExecOrderField pExecOrder);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderInsert(ref CThostFtdcInputExecOrderField pInputExecOrder,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderAction(ref CThostFtdcExecOrderActionField pExecOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnForQuoteInsert(ref CThostFtdcInputForQuoteField pInputForQuote,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnQuote(ref CThostFtdcQuoteField pQuote);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteInsert(ref CThostFtdcInputQuoteField pInputQuote,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteAction(ref CThostFtdcQuoteActionField pQuoteAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnForQuoteRsp(ref CThostFtdcForQuoteRspField pForQuoteRsp);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCFMMCTradingAccountToken(ref CThostFtdcCFMMCTradingAccountTokenField pCFMMCTradingAccountToken);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnBatchOrderAction(ref CThostFtdcBatchOrderActionField pBatchOrderAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOptionSelfClose(ref CThostFtdcOptionSelfCloseField pOptionSelfClose);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOptionSelfCloseInsert(ref CThostFtdcInputOptionSelfCloseField pInputOptionSelfClose,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOptionSelfCloseAction(ref CThostFtdcOptionSelfCloseActionField pOptionSelfCloseAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCombAction(ref CThostFtdcCombActionField pCombAction);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnCombActionInsert(ref CThostFtdcInputCombActionField pInputCombAction,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryContractBank(ref CThostFtdcContractBankField pContractBank,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryParkedOrder(ref CThostFtdcParkedOrderField pParkedOrder,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryParkedOrderAction(ref CThostFtdcParkedOrderActionField pParkedOrderAction,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingNotice(ref CThostFtdcTradingNoticeField pTradingNotice,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryBrokerTradingParams(ref CThostFtdcBrokerTradingParamsField pBrokerTradingParams,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryBrokerTradingAlgos(ref CThostFtdcBrokerTradingAlgosField pBrokerTradingAlgos,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryCFMMCTradingAccountToken(ref CThostFtdcQueryCFMMCTradingAccountTokenField pQueryCFMMCTradingAccountToken,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromBankToFutureByBank(ref CThostFtdcRspTransferField pRspTransfer);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromFutureToBankByBank(ref CThostFtdcRspTransferField pRspTransfer);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByBank(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByBank(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromBankToFutureByFuture(ref CThostFtdcRspTransferField pRspTransfer);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFromFutureToBankByFuture(ref CThostFtdcRspTransferField pRspTransfer);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByFutureManual(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByFutureManual(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnQueryBankBalanceByFuture(ref CThostFtdcNotifyQueryAccountField pNotifyQueryAccount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnBankToFutureByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnFutureToBankByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnRepealBankToFutureByFutureManual(ref CThostFtdcReqRepealField pReqRepeal,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnRepealFutureToBankByFutureManual(ref CThostFtdcReqRepealField pReqRepeal,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQueryBankBalanceByFuture(ref CThostFtdcReqQueryAccountField pReqQueryAccount,ref CThostFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromBankToFutureByFuture(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnRepealFromFutureToBankByFuture(ref CThostFtdcRspRepealField pRspRepeal);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspFromBankToFutureByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspFromFutureToBankByFuture(ref CThostFtdcReqTransferField pReqTransfer,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryBankAccountMoneyByFuture(ref CThostFtdcReqQueryAccountField pReqQueryAccount,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOpenAccountByBank(ref CThostFtdcOpenAccountField pOpenAccount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnCancelAccountByBank(ref CThostFtdcCancelAccountField pCancelAccount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnChangeAccountByBank(ref CThostFtdcChangeAccountField pChangeAccount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryClassifiedInstrument(ref CThostFtdcInstrumentField pInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryCombPromotionParam(ref CThostFtdcCombPromotionParamField pCombPromotionParam,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		public void SetOnFrontConnected(DeleOnFrontConnected func) {(Invoke(_handle, "SetOnFrontConnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnFrontDisconnected(DeleOnFrontDisconnected func) {(Invoke(_handle, "SetOnFrontDisconnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnHeartBeatWarning(DeleOnHeartBeatWarning func) {(Invoke(_handle, "SetOnHeartBeatWarning", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspAuthenticate(DeleOnRspAuthenticate func) {(Invoke(_handle, "SetOnRspAuthenticate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogin(DeleOnRspUserLogin func) {(Invoke(_handle, "SetOnRspUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogout(DeleOnRspUserLogout func) {(Invoke(_handle, "SetOnRspUserLogout", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserPasswordUpdate(DeleOnRspUserPasswordUpdate func) {(Invoke(_handle, "SetOnRspUserPasswordUpdate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspTradingAccountPasswordUpdate(DeleOnRspTradingAccountPasswordUpdate func) {(Invoke(_handle, "SetOnRspTradingAccountPasswordUpdate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserAuthMethod(DeleOnRspUserAuthMethod func) {(Invoke(_handle, "SetOnRspUserAuthMethod", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspGenUserCaptcha(DeleOnRspGenUserCaptcha func) {(Invoke(_handle, "SetOnRspGenUserCaptcha", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspGenUserText(DeleOnRspGenUserText func) {(Invoke(_handle, "SetOnRspGenUserText", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOrderInsert(DeleOnRspOrderInsert func) {(Invoke(_handle, "SetOnRspOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspParkedOrderInsert(DeleOnRspParkedOrderInsert func) {(Invoke(_handle, "SetOnRspParkedOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspParkedOrderAction(DeleOnRspParkedOrderAction func) {(Invoke(_handle, "SetOnRspParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOrderAction(DeleOnRspOrderAction func) {(Invoke(_handle, "SetOnRspOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryMaxOrderVolume(DeleOnRspQryMaxOrderVolume func) {(Invoke(_handle, "SetOnRspQryMaxOrderVolume", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspSettlementInfoConfirm(DeleOnRspSettlementInfoConfirm func) {(Invoke(_handle, "SetOnRspSettlementInfoConfirm", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspRemoveParkedOrder(DeleOnRspRemoveParkedOrder func) {(Invoke(_handle, "SetOnRspRemoveParkedOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspRemoveParkedOrderAction(DeleOnRspRemoveParkedOrderAction func) {(Invoke(_handle, "SetOnRspRemoveParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspExecOrderInsert(DeleOnRspExecOrderInsert func) {(Invoke(_handle, "SetOnRspExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspExecOrderAction(DeleOnRspExecOrderAction func) {(Invoke(_handle, "SetOnRspExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspForQuoteInsert(DeleOnRspForQuoteInsert func) {(Invoke(_handle, "SetOnRspForQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQuoteInsert(DeleOnRspQuoteInsert func) {(Invoke(_handle, "SetOnRspQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQuoteAction(DeleOnRspQuoteAction func) {(Invoke(_handle, "SetOnRspQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspBatchOrderAction(DeleOnRspBatchOrderAction func) {(Invoke(_handle, "SetOnRspBatchOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOptionSelfCloseInsert(DeleOnRspOptionSelfCloseInsert func) {(Invoke(_handle, "SetOnRspOptionSelfCloseInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOptionSelfCloseAction(DeleOnRspOptionSelfCloseAction func) {(Invoke(_handle, "SetOnRspOptionSelfCloseAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspCombActionInsert(DeleOnRspCombActionInsert func) {(Invoke(_handle, "SetOnRspCombActionInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryOrder(DeleOnRspQryOrder func) {(Invoke(_handle, "SetOnRspQryOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTrade(DeleOnRspQryTrade func) {(Invoke(_handle, "SetOnRspQryTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorPosition(DeleOnRspQryInvestorPosition func) {(Invoke(_handle, "SetOnRspQryInvestorPosition", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTradingAccount(DeleOnRspQryTradingAccount func) {(Invoke(_handle, "SetOnRspQryTradingAccount", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestor(DeleOnRspQryInvestor func) {(Invoke(_handle, "SetOnRspQryInvestor", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTradingCode(DeleOnRspQryTradingCode func) {(Invoke(_handle, "SetOnRspQryTradingCode", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrumentMarginRate(DeleOnRspQryInstrumentMarginRate func) {(Invoke(_handle, "SetOnRspQryInstrumentMarginRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrumentCommissionRate(DeleOnRspQryInstrumentCommissionRate func) {(Invoke(_handle, "SetOnRspQryInstrumentCommissionRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExchange(DeleOnRspQryExchange func) {(Invoke(_handle, "SetOnRspQryExchange", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryProduct(DeleOnRspQryProduct func) {(Invoke(_handle, "SetOnRspQryProduct", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrument(DeleOnRspQryInstrument func) {(Invoke(_handle, "SetOnRspQryInstrument", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryDepthMarketData(DeleOnRspQryDepthMarketData func) {(Invoke(_handle, "SetOnRspQryDepthMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySettlementInfo(DeleOnRspQrySettlementInfo func) {(Invoke(_handle, "SetOnRspQrySettlementInfo", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTransferBank(DeleOnRspQryTransferBank func) {(Invoke(_handle, "SetOnRspQryTransferBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorPositionDetail(DeleOnRspQryInvestorPositionDetail func) {(Invoke(_handle, "SetOnRspQryInvestorPositionDetail", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryNotice(DeleOnRspQryNotice func) {(Invoke(_handle, "SetOnRspQryNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySettlementInfoConfirm(DeleOnRspQrySettlementInfoConfirm func) {(Invoke(_handle, "SetOnRspQrySettlementInfoConfirm", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorPositionCombineDetail(DeleOnRspQryInvestorPositionCombineDetail func) {(Invoke(_handle, "SetOnRspQryInvestorPositionCombineDetail", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryCFMMCTradingAccountKey(DeleOnRspQryCFMMCTradingAccountKey func) {(Invoke(_handle, "SetOnRspQryCFMMCTradingAccountKey", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryEWarrantOffset(DeleOnRspQryEWarrantOffset func) {(Invoke(_handle, "SetOnRspQryEWarrantOffset", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorProductGroupMargin(DeleOnRspQryInvestorProductGroupMargin func) {(Invoke(_handle, "SetOnRspQryInvestorProductGroupMargin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExchangeMarginRate(DeleOnRspQryExchangeMarginRate func) {(Invoke(_handle, "SetOnRspQryExchangeMarginRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExchangeMarginRateAdjust(DeleOnRspQryExchangeMarginRateAdjust func) {(Invoke(_handle, "SetOnRspQryExchangeMarginRateAdjust", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExchangeRate(DeleOnRspQryExchangeRate func) {(Invoke(_handle, "SetOnRspQryExchangeRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySecAgentACIDMap(DeleOnRspQrySecAgentACIDMap func) {(Invoke(_handle, "SetOnRspQrySecAgentACIDMap", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryProductExchRate(DeleOnRspQryProductExchRate func) {(Invoke(_handle, "SetOnRspQryProductExchRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryProductGroup(DeleOnRspQryProductGroup func) {(Invoke(_handle, "SetOnRspQryProductGroup", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryMMInstrumentCommissionRate(DeleOnRspQryMMInstrumentCommissionRate func) {(Invoke(_handle, "SetOnRspQryMMInstrumentCommissionRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryMMOptionInstrCommRate(DeleOnRspQryMMOptionInstrCommRate func) {(Invoke(_handle, "SetOnRspQryMMOptionInstrCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrumentOrderCommRate(DeleOnRspQryInstrumentOrderCommRate func) {(Invoke(_handle, "SetOnRspQryInstrumentOrderCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySecAgentTradingAccount(DeleOnRspQrySecAgentTradingAccount func) {(Invoke(_handle, "SetOnRspQrySecAgentTradingAccount", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySecAgentCheckMode(DeleOnRspQrySecAgentCheckMode func) {(Invoke(_handle, "SetOnRspQrySecAgentCheckMode", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySecAgentTradeInfo(DeleOnRspQrySecAgentTradeInfo func) {(Invoke(_handle, "SetOnRspQrySecAgentTradeInfo", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryOptionInstrTradeCost(DeleOnRspQryOptionInstrTradeCost func) {(Invoke(_handle, "SetOnRspQryOptionInstrTradeCost", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryOptionInstrCommRate(DeleOnRspQryOptionInstrCommRate func) {(Invoke(_handle, "SetOnRspQryOptionInstrCommRate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExecOrder(DeleOnRspQryExecOrder func) {(Invoke(_handle, "SetOnRspQryExecOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryForQuote(DeleOnRspQryForQuote func) {(Invoke(_handle, "SetOnRspQryForQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryQuote(DeleOnRspQryQuote func) {(Invoke(_handle, "SetOnRspQryQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryOptionSelfClose(DeleOnRspQryOptionSelfClose func) {(Invoke(_handle, "SetOnRspQryOptionSelfClose", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestUnit(DeleOnRspQryInvestUnit func) {(Invoke(_handle, "SetOnRspQryInvestUnit", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryCombInstrumentGuard(DeleOnRspQryCombInstrumentGuard func) {(Invoke(_handle, "SetOnRspQryCombInstrumentGuard", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryCombAction(DeleOnRspQryCombAction func) {(Invoke(_handle, "SetOnRspQryCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTransferSerial(DeleOnRspQryTransferSerial func) {(Invoke(_handle, "SetOnRspQryTransferSerial", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryAccountregister(DeleOnRspQryAccountregister func) {(Invoke(_handle, "SetOnRspQryAccountregister", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspError(DeleOnRspError func) {(Invoke(_handle, "SetOnRspError", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnOrder(DeleOnRtnOrder func) {(Invoke(_handle, "SetOnRtnOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnTrade(DeleOnRtnTrade func) {(Invoke(_handle, "SetOnRtnTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOrderInsert(DeleOnErrRtnOrderInsert func) {(Invoke(_handle, "SetOnErrRtnOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOrderAction(DeleOnErrRtnOrderAction func) {(Invoke(_handle, "SetOnErrRtnOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnInstrumentStatus(DeleOnRtnInstrumentStatus func) {(Invoke(_handle, "SetOnRtnInstrumentStatus", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnBulletin(DeleOnRtnBulletin func) {(Invoke(_handle, "SetOnRtnBulletin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnTradingNotice(DeleOnRtnTradingNotice func) {(Invoke(_handle, "SetOnRtnTradingNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnErrorConditionalOrder(DeleOnRtnErrorConditionalOrder func) {(Invoke(_handle, "SetOnRtnErrorConditionalOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnExecOrder(DeleOnRtnExecOrder func) {(Invoke(_handle, "SetOnRtnExecOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnExecOrderInsert(DeleOnErrRtnExecOrderInsert func) {(Invoke(_handle, "SetOnErrRtnExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnExecOrderAction(DeleOnErrRtnExecOrderAction func) {(Invoke(_handle, "SetOnErrRtnExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnForQuoteInsert(DeleOnErrRtnForQuoteInsert func) {(Invoke(_handle, "SetOnErrRtnForQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnQuote(DeleOnRtnQuote func) {(Invoke(_handle, "SetOnRtnQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnQuoteInsert(DeleOnErrRtnQuoteInsert func) {(Invoke(_handle, "SetOnErrRtnQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnQuoteAction(DeleOnErrRtnQuoteAction func) {(Invoke(_handle, "SetOnErrRtnQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnForQuoteRsp(DeleOnRtnForQuoteRsp func) {(Invoke(_handle, "SetOnRtnForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnCFMMCTradingAccountToken(DeleOnRtnCFMMCTradingAccountToken func) {(Invoke(_handle, "SetOnRtnCFMMCTradingAccountToken", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnBatchOrderAction(DeleOnErrRtnBatchOrderAction func) {(Invoke(_handle, "SetOnErrRtnBatchOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnOptionSelfClose(DeleOnRtnOptionSelfClose func) {(Invoke(_handle, "SetOnRtnOptionSelfClose", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOptionSelfCloseInsert(DeleOnErrRtnOptionSelfCloseInsert func) {(Invoke(_handle, "SetOnErrRtnOptionSelfCloseInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOptionSelfCloseAction(DeleOnErrRtnOptionSelfCloseAction func) {(Invoke(_handle, "SetOnErrRtnOptionSelfCloseAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnCombAction(DeleOnRtnCombAction func) {(Invoke(_handle, "SetOnRtnCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnCombActionInsert(DeleOnErrRtnCombActionInsert func) {(Invoke(_handle, "SetOnErrRtnCombActionInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryContractBank(DeleOnRspQryContractBank func) {(Invoke(_handle, "SetOnRspQryContractBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryParkedOrder(DeleOnRspQryParkedOrder func) {(Invoke(_handle, "SetOnRspQryParkedOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryParkedOrderAction(DeleOnRspQryParkedOrderAction func) {(Invoke(_handle, "SetOnRspQryParkedOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTradingNotice(DeleOnRspQryTradingNotice func) {(Invoke(_handle, "SetOnRspQryTradingNotice", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryBrokerTradingParams(DeleOnRspQryBrokerTradingParams func) {(Invoke(_handle, "SetOnRspQryBrokerTradingParams", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryBrokerTradingAlgos(DeleOnRspQryBrokerTradingAlgos func) {(Invoke(_handle, "SetOnRspQryBrokerTradingAlgos", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQueryCFMMCTradingAccountToken(DeleOnRspQueryCFMMCTradingAccountToken func) {(Invoke(_handle, "SetOnRspQueryCFMMCTradingAccountToken", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnFromBankToFutureByBank(DeleOnRtnFromBankToFutureByBank func) {(Invoke(_handle, "SetOnRtnFromBankToFutureByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnFromFutureToBankByBank(DeleOnRtnFromFutureToBankByBank func) {(Invoke(_handle, "SetOnRtnFromFutureToBankByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromBankToFutureByBank(DeleOnRtnRepealFromBankToFutureByBank func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromFutureToBankByBank(DeleOnRtnRepealFromFutureToBankByBank func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnFromBankToFutureByFuture(DeleOnRtnFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRtnFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnFromFutureToBankByFuture(DeleOnRtnFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRtnFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromBankToFutureByFutureManual(DeleOnRtnRepealFromBankToFutureByFutureManual func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromFutureToBankByFutureManual(DeleOnRtnRepealFromFutureToBankByFutureManual func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnQueryBankBalanceByFuture(DeleOnRtnQueryBankBalanceByFuture func) {(Invoke(_handle, "SetOnRtnQueryBankBalanceByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnBankToFutureByFuture(DeleOnErrRtnBankToFutureByFuture func) {(Invoke(_handle, "SetOnErrRtnBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnFutureToBankByFuture(DeleOnErrRtnFutureToBankByFuture func) {(Invoke(_handle, "SetOnErrRtnFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnRepealBankToFutureByFutureManual(DeleOnErrRtnRepealBankToFutureByFutureManual func) {(Invoke(_handle, "SetOnErrRtnRepealBankToFutureByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnRepealFutureToBankByFutureManual(DeleOnErrRtnRepealFutureToBankByFutureManual func) {(Invoke(_handle, "SetOnErrRtnRepealFutureToBankByFutureManual", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnQueryBankBalanceByFuture(DeleOnErrRtnQueryBankBalanceByFuture func) {(Invoke(_handle, "SetOnErrRtnQueryBankBalanceByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromBankToFutureByFuture(DeleOnRtnRepealFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRtnRepealFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnRepealFromFutureToBankByFuture(DeleOnRtnRepealFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRtnRepealFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspFromBankToFutureByFuture(DeleOnRspFromBankToFutureByFuture func) {(Invoke(_handle, "SetOnRspFromBankToFutureByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspFromFutureToBankByFuture(DeleOnRspFromFutureToBankByFuture func) {(Invoke(_handle, "SetOnRspFromFutureToBankByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQueryBankAccountMoneyByFuture(DeleOnRspQueryBankAccountMoneyByFuture func) {(Invoke(_handle, "SetOnRspQueryBankAccountMoneyByFuture", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnOpenAccountByBank(DeleOnRtnOpenAccountByBank func) {(Invoke(_handle, "SetOnRtnOpenAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnCancelAccountByBank(DeleOnRtnCancelAccountByBank func) {(Invoke(_handle, "SetOnRtnCancelAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnChangeAccountByBank(DeleOnRtnChangeAccountByBank func) {(Invoke(_handle, "SetOnRtnChangeAccountByBank", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryClassifiedInstrument(DeleOnRspQryClassifiedInstrument func) {(Invoke(_handle, "SetOnRspQryClassifiedInstrument", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryCombPromotionParam(DeleOnRspQryCombPromotionParam func) {(Invoke(_handle, "SetOnRspQryCombPromotionParam", typeof(DeleSet)) as DeleSet)(_spi, func);}
	}
}