using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;

namespace HaiFeng
{
	public class ctp_quote
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
		
		public ctp_quote()
		{
			string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(this.GetType().Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            dll_path = Path.Combine(dll_path, "lib" + (Environment.Is64BitProcess ? "64" : "32"));
            if (!Directory.Exists(dll_path))
            {
                File.WriteAllBytes("lib.zip", Properties.Resources.lib);
                ZipFile.ExtractToDirectory("lib.zip", ".");
                File.Delete("lib.zip");
            }
			Environment.CurrentDirectory = dll_path;
			_handle = LoadLibrary(Path.Combine(dll_path, "ctp_quote.dll"));
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
		public delegate IntPtr DeleSubscribeMarketData(IntPtr api, IntPtr ppInstrumentID, int nCount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleUnSubscribeMarketData(IntPtr api, IntPtr ppInstrumentID, int nCount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribeForQuoteRsp(IntPtr api, IntPtr ppInstrumentID, int nCount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleUnSubscribeForQuoteRsp(IntPtr api, IntPtr ppInstrumentID, int nCount);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogin(IntPtr api, ref CThostFtdcReqUserLoginField pReqUserLoginField, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogout(IntPtr api, ref CThostFtdcUserLogoutField pUserLogout, int nRequestID);
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
                    

        public IntPtr SubscribeMarketData(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "SubscribeMarketData", typeof(DeleSubscribeMarketData)) as DeleSubscribeMarketData)(_api, ppInstrumentID, nCount);
        }
                    

        public IntPtr UnSubscribeMarketData(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "UnSubscribeMarketData", typeof(DeleUnSubscribeMarketData)) as DeleUnSubscribeMarketData)(_api, ppInstrumentID, nCount);
        }
                    

        public IntPtr SubscribeForQuoteRsp(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "SubscribeForQuoteRsp", typeof(DeleSubscribeForQuoteRsp)) as DeleSubscribeForQuoteRsp)(_api, ppInstrumentID, nCount);
        }
                    

        public IntPtr UnSubscribeForQuoteRsp(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "UnSubscribeForQuoteRsp", typeof(DeleUnSubscribeForQuoteRsp)) as DeleUnSubscribeForQuoteRsp)(_api, ppInstrumentID, nCount);
        }
                    

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
                    

        public IntPtr ReqUserLogout(string BrokerID = "",string UserID = "")
        {
			CThostFtdcUserLogoutField pUserLogout = new CThostFtdcUserLogoutField
			{
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqUserLogout", typeof(DeleReqUserLogout)) as DeleReqUserLogout)(_api, ref pUserLogout, this.nRequestID++);
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
		public delegate void DeleOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogout(ref CThostFtdcUserLogoutField pUserLogout,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspError(ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSubMarketData(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUnSubMarketData(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSubForQuoteRsp(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUnSubForQuoteRsp(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnDepthMarketData(ref CThostFtdcDepthMarketDataField pDepthMarketData);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnForQuoteRsp(ref CThostFtdcForQuoteRspField pForQuoteRsp);
		public void SetOnFrontConnected(DeleOnFrontConnected func) {(Invoke(_handle, "SetOnFrontConnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnFrontDisconnected(DeleOnFrontDisconnected func) {(Invoke(_handle, "SetOnFrontDisconnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnHeartBeatWarning(DeleOnHeartBeatWarning func) {(Invoke(_handle, "SetOnHeartBeatWarning", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogin(DeleOnRspUserLogin func) {(Invoke(_handle, "SetOnRspUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogout(DeleOnRspUserLogout func) {(Invoke(_handle, "SetOnRspUserLogout", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspError(DeleOnRspError func) {(Invoke(_handle, "SetOnRspError", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspSubMarketData(DeleOnRspSubMarketData func) {(Invoke(_handle, "SetOnRspSubMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUnSubMarketData(DeleOnRspUnSubMarketData func) {(Invoke(_handle, "SetOnRspUnSubMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspSubForQuoteRsp(DeleOnRspSubForQuoteRsp func) {(Invoke(_handle, "SetOnRspSubForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUnSubForQuoteRsp(DeleOnRspUnSubForQuoteRsp func) {(Invoke(_handle, "SetOnRspUnSubForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnDepthMarketData(DeleOnRtnDepthMarketData func) {(Invoke(_handle, "SetOnRtnDepthMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnForQuoteRsp(DeleOnRtnForQuoteRsp func) {(Invoke(_handle, "SetOnRtnForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
	}
}