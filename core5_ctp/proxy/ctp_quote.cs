using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;
using PureCode.CtpCSharp;

namespace HaiFeng
{
	public class ctp_quote
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

		static ctp_quote()
        {
            string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(typeof(ctp_quote).Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            string dllFileName = Path.Combine(dll_path, "ctp_quote.dll");
			
            loader = new AssembyLoader(dllFileName);
            var _handle = loader.GetDllHandle();

			if (_handle == IntPtr.Zero)
			{
				throw (new Exception(String.Format("没有找到:", dll_path)));
			}

			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");
        }
        
		public ctp_quote()
		{
            _handle = loader.GetDllHandle();

			_api = (Invoke(_handle, "CreateApi", typeof(Create)) as Create)();
			_spi = (Invoke(_handle, "CreateSpi", typeof(Create)) as Create)();
			this.RegisterSpi(_spi);
		}

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
		///订阅行情。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribeMarketData(IntPtr api, IntPtr ppInstrumentID, int nCount);

		/// <summary>
		///退订行情。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleUnSubscribeMarketData(IntPtr api, IntPtr ppInstrumentID, int nCount);

		/// <summary>
		///订阅询价。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribeForQuoteRsp(IntPtr api, IntPtr ppInstrumentID, int nCount);

		/// <summary>
		///退订询价。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleUnSubscribeForQuoteRsp(IntPtr api, IntPtr ppInstrumentID, int nCount);

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
		///订阅行情。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
        public IntPtr SubscribeMarketData(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "SubscribeMarketData", typeof(DeleSubscribeMarketData)) as DeleSubscribeMarketData)(_api, ppInstrumentID, nCount);
        }
                    

		/// <summary>
		///退订行情。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
        public IntPtr UnSubscribeMarketData(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "UnSubscribeMarketData", typeof(DeleUnSubscribeMarketData)) as DeleUnSubscribeMarketData)(_api, ppInstrumentID, nCount);
        }
                    

		/// <summary>
		///订阅询价。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
        public IntPtr SubscribeForQuoteRsp(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "SubscribeForQuoteRsp", typeof(DeleSubscribeForQuoteRsp)) as DeleSubscribeForQuoteRsp)(_api, ppInstrumentID, nCount);
        }
                    

		/// <summary>
		///退订询价。
		///@param ppInstrumentID 合约ID  
		///@param nCount 要订阅/退订行情的合约个数
		///@remark 
		/// </summary>
        public IntPtr UnSubscribeForQuoteRsp(IntPtr ppInstrumentID,int nCount = 1)
        {
			
            return (Invoke(_handle, "UnSubscribeForQuoteRsp", typeof(DeleUnSubscribeForQuoteRsp)) as DeleUnSubscribeForQuoteRsp)(_api, ppInstrumentID, nCount);
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
		///错误应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspError(ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///订阅行情应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSubMarketData(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///取消订阅行情应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUnSubMarketData(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///订阅询价应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspSubForQuoteRsp(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///取消订阅询价应答
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUnSubForQuoteRsp(ref CThostFtdcSpecificInstrumentField pSpecificInstrument,ref CThostFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		
		/// <summary>
		///深度行情通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnDepthMarketData(ref CThostFtdcDepthMarketDataField pDepthMarketData);
		
		/// <summary>
		///询价通知
		/// </summary>
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnForQuoteRsp(ref CThostFtdcForQuoteRspField pForQuoteRsp);
		
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
		///登录请求响应
		/// </summary>
		public void SetOnRspUserLogin(DeleOnRspUserLogin func) {(Invoke(_handle, "SetOnRspUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///登出请求响应
		/// </summary>
		public void SetOnRspUserLogout(DeleOnRspUserLogout func) {(Invoke(_handle, "SetOnRspUserLogout", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///错误应答
		/// </summary>
		public void SetOnRspError(DeleOnRspError func) {(Invoke(_handle, "SetOnRspError", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///订阅行情应答
		/// </summary>
		public void SetOnRspSubMarketData(DeleOnRspSubMarketData func) {(Invoke(_handle, "SetOnRspSubMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///取消订阅行情应答
		/// </summary>
		public void SetOnRspUnSubMarketData(DeleOnRspUnSubMarketData func) {(Invoke(_handle, "SetOnRspUnSubMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///订阅询价应答
		/// </summary>
		public void SetOnRspSubForQuoteRsp(DeleOnRspSubForQuoteRsp func) {(Invoke(_handle, "SetOnRspSubForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///取消订阅询价应答
		/// </summary>
		public void SetOnRspUnSubForQuoteRsp(DeleOnRspUnSubForQuoteRsp func) {(Invoke(_handle, "SetOnRspUnSubForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///深度行情通知
		/// </summary>
		public void SetOnRtnDepthMarketData(DeleOnRtnDepthMarketData func) {(Invoke(_handle, "SetOnRtnDepthMarketData", typeof(DeleSet)) as DeleSet)(_spi, func);}
		
		/// <summary>
		///询价通知
		/// </summary>
		public void SetOnRtnForQuoteRsp(DeleOnRtnForQuoteRsp func) {(Invoke(_handle, "SetOnRtnForQuoteRsp", typeof(DeleSet)) as DeleSet)(_spi, func);}
	}
}