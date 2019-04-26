using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using HaiFeng.Properties;
using static HaiFeng.ctp_quote;

namespace HaiFeng
{
	public abstract class CTPQuote : Quote
	{
		ctp_quote _q = null;
		private readonly List<Delegate> _listDele = new List<Delegate>();

        /// <summary>
        /// 
        /// </summary>
		public CTPQuote()
		{
			_q = new ctp_quote();
			SetCallBack();
		}

        /// <summary>
        /// 前置地址端口
        /// </summary>
        public override string FrontAddr { get; set; }

        /// <summary>
        /// 帐号
        /// </summary>
        public override string Investor { get; set; }

        /// <summary>
        /// 密码
        /// </summary>
        public override string Password { get; set; }

        /// <summary>
        /// 经纪商代码
        /// </summary>
        public override string Broker { get; set; }

        Delegate AddDele(Delegate d) { _listDele.Add(d); return d; }

		void SetCallBack()
		{
			_q.SetOnFrontConnected((DeleOnFrontConnected)AddDele(new DeleOnFrontConnected(CTPOnFrontConnected)));
			_q.SetOnRspUserLogin((DeleOnRspUserLogin)AddDele(new DeleOnRspUserLogin(CTPOnRspUserLogin)));
			_q.SetOnFrontDisconnected((DeleOnFrontDisconnected)AddDele(new DeleOnFrontDisconnected(CTPOnFrontDisconnected)));
			_q.SetOnRspSubMarketData((DeleOnRspSubMarketData)AddDele(new DeleOnRspSubMarketData(CTPOnRspSubMarketData)));
			_q.SetOnRtnDepthMarketData((DeleOnRtnDepthMarketData)AddDele(new DeleOnRtnDepthMarketData(CTPOnRtnDepthMarketData)));
			_q.SetOnRspError((DeleOnRspError)AddDele(new DeleOnRspError(CTPOnRspError)));
		}

		private void CTPOnRtnDepthMarketData(ref CThostFtdcDepthMarketDataField pDepthMarketData)
		{
			CThostFtdcDepthMarketDataField f = pDepthMarketData;

			if (string.IsNullOrEmpty(f.InstrumentID) || string.IsNullOrEmpty(f.UpdateTime) || double.IsInfinity(f.UpperLimitPrice))//过滤无穷大/小
			{
				return;
			}
			//修正last=double.max
			if (Math.Abs(f.LastPrice - double.MaxValue) < double.Epsilon)
			{
				if (Math.Abs(f.AskPrice1 - double.MaxValue) > double.Epsilon)
				{
					f.LastPrice = f.AskPrice1;
				}
				else if (Math.Abs(f.BidPrice1 - double.MaxValue) > double.Epsilon)
				{
					f.LastPrice = f.BidPrice1;
				}
				else
					return;
			}

			//去掉tradingday字段
			//if (string.IsNullOrEmpty(f.TradingDay))
			//{
			//	f.TradingDay = this.TradingDay; //日期:实盘中某些交易所,此字段为空
			//}
			//if (string.IsNullOrEmpty(f.ActionDay)) //此字段可能为空
			//{
			//	f.ActionDay = this.TradingDay;
			//}
			//f.ExchangeID = instrument.ExchangeID;
			//处理,单边有挂边的情况
			if (f.AskPrice1 > f.UpperLimitPrice) //未赋值的数据
			{
				f.AskPrice1 = f.LastPrice;
			}
			if (f.BidPrice1 > f.UpperLimitPrice)
			{
				f.BidPrice1 = f.LastPrice;
			}
			//修最高/最低
			if (Math.Abs(f.HighestPrice - double.MaxValue) < double.Epsilon)
			{
				f.HighestPrice = f.AskPrice1;
			}
			if (Math.Abs(f.LowestPrice - double.MaxValue) < double.Epsilon)
			{
				f.LowestPrice = f.BidPrice1;
			}

			HaiFeng.MarketData tick = DicTick.GetOrAdd(f.InstrumentID, new HaiFeng.MarketData
			{
				InstrumentID = f.InstrumentID,
			});


			if (f.UpdateMillisec == 0 && f.UpdateTime == tick.UpdateTime && tick.UpdateMillisec < 990)  //某些交易所(如郑商所)相同秒数的ms均为0
			{
				f.UpdateMillisec = tick.UpdateMillisec + 10;
			}

			tick.AskPrice = f.AskPrice1;
			tick.AskVolume = f.AskVolume1;
			tick.AveragePrice = f.AveragePrice;
			tick.BidPrice = f.BidPrice1;
			tick.BidVolume = f.BidVolume1;
			tick.LastPrice = f.LastPrice;
			tick.OpenInterest = f.OpenInterest;
			tick.UpdateMillisec = f.UpdateMillisec;
			tick.UpdateTime = f.UpdateTime;
			tick.Volume = f.Volume;
			tick.UpperLimitPrice = f.UpperLimitPrice;
			tick.LowerLimitPrice = f.LowerLimitPrice;

			this.DicTick[tick.InstrumentID] = tick;

			if (_OnRtnTick == null) return;
			_OnRtnTick(this, new TickEventArgs
			{
				Tick = tick
			});
		}

		private void CTPOnRspSubMarketData(ref CThostFtdcSpecificInstrumentField pSpecificInstrument, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
		{
		}

		private void CTPOnFrontDisconnected(int nReason)
		{
			this.IsLogin = false;
			_OnRspUserLogout?.Invoke(this, new IntEventArgs { Value = nReason });
			SetCallBack();
		}

		private void CTPOnRspError(ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
		{
			_OnRtnError?.Invoke(this, new ErrorEventArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg });
		}

		private void CTPOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
		{
			//避免登录错误后不断重连
			if (pRspInfo.ErrorID != 0)
				_q.SetOnFrontConnected(null);
			else //正常登录时注册连接事件(后续自动重连时可自行登录)
			{
				this.IsLogin = true;
				_q.SetOnFrontConnected(CTPOnFrontConnected);
			}
			_OnRspUserLogin?.Invoke(this, new IntEventArgs { Value = pRspInfo.ErrorID });
		}

		private void CTPOnFrontConnected()
		{
			_OnFrontConnected?.Invoke(this, new EventArgs());
		}

		public override bool IsLogin { get; protected set; }

		public override int ReqConnect()
		{
			_q.RegisterFront(this.FrontAddr);
			//_q.Init();
			return (int)_q.Init();
			//return (int)_q.Join(); //会造成阻塞
		}

		public override int ReqSubscribeMarketData(params string[] pInstrument)
		{
			int size = Marshal.SizeOf(typeof(IntPtr));
			IntPtr insts = Marshal.AllocHGlobal(size * pInstrument.Length);
			var tmp = insts;
			for (int i = 0; i < pInstrument.Length; i++, tmp += size)
			{
				Marshal.StructureToPtr(Marshal.StringToHGlobalAnsi(pInstrument[i]), tmp, false);
			}
			return (int)_q.SubscribeMarketData(insts, pInstrument.Length);
		}

		public override int ReqUnSubscribeMarketData(params string[] pInstrument)
		{
			int size = Marshal.SizeOf(typeof(IntPtr));
			IntPtr insts = Marshal.AllocHGlobal(size * pInstrument.Length);
			var tmp = insts;
			for (int i = 0; i < pInstrument.Length; i++, tmp += size)
			{
				Marshal.StructureToPtr(Marshal.StringToHGlobalAnsi(pInstrument[i]), tmp, false);
			}
			return (int)_q.UnSubscribeMarketData(insts, pInstrument.Length);
		}

		public override int ReqUserLogin()
		{
			return (int)_q.ReqUserLogin(BrokerID: this.Broker, UserID: this.Investor, Password: this.Password);
		}

		public override void ReqUserLogout()
		{
			this.IsLogin = false;
			//上面的disconnect注销掉,需要主动调用此回调函数
			_OnRspUserLogout?.Invoke(this, new IntEventArgs { Value = 0 });
			//取消连接响应,避免重连后的再登录.（release中已处理）
			//_q.SetOnFrontDisconnected(null);
			//_q.SetOnFrontConnected(null);
			_q.Release();
		}
	}
}
