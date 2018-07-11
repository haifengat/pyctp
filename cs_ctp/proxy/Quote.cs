using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	public abstract class Quote
	{
		private ConcurrentDictionary<string, MarketData> _ticks = new ConcurrentDictionary<string, MarketData>();

		/// <summary>
		/// Tick数据
		/// </summary>
		public ConcurrentDictionary<string, MarketData> DicTick { get { return _ticks; } }

		#region 响应
		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnTick(object sender, TickEventArgs e);

		/// <summary>
		/// 行情响应用
		/// </summary>
		internal RtnTick _OnRtnTick;

		/// <summary>
		/// 
		/// </summary>
		public event RtnTick OnRtnTick
		{
			add
			{
				_OnRtnTick += value;
			}
			remove
			{
				_OnRtnTick -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void FrontConnected(object sender, EventArgs e);

		internal FrontConnected _OnFrontConnected;

		/// <summary>
		/// 
		/// </summary>
		public event FrontConnected OnFrontConnected
		{
			add
			{
				_OnFrontConnected += value;
			}
			remove
			{
				_OnFrontConnected -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RspUserLogin(object sender, IntEventArgs e);

		internal RspUserLogin _OnRspUserLogin;

		/// <summary>
		/// 
		/// </summary>
		public event RspUserLogin OnRspUserLogin
		{
			add
			{
				_OnRspUserLogin += value;
			}
			remove
			{
				_OnRspUserLogin -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RspUserLogout(object sender, IntEventArgs e);

		internal RspUserLogout _OnRspUserLogout;

		/// <summary>
		/// 
		/// </summary>
		public event RspUserLogout OnRspUserLogout
		{
			add
			{
				_OnRspUserLogout += value;
			}
			remove
			{
				_OnRspUserLogout -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnError(object sender, ErrorEventArgs e);

		internal RtnError _OnRtnError;

		/// <summary>
		/// 
		/// </summary>
		public event RtnError OnRtnError
		{
			add
			{
				_OnRtnError += value;
			}
			remove
			{
				_OnRtnError -= value;
			}
		}
		#endregion
		

		/// <summary>
		/// 连接
		/// </summary>
		/// <returns></returns>
		public abstract int ReqConnect(string pFront);

		/// <summary>
		/// 登录[重连时自动订阅DicTick.Keys中的合约]
		/// </summary>
		/// <returns></returns>
		public abstract int ReqUserLogin(string pInvestor, string pPassword, string pBroker);

		/// <summary>
		/// 是否登录成功
		/// </summary>
		public abstract bool IsLogin { get; protected set; }

		/// <summary>
		/// 退订[接口会Release]
		/// </summary>
		public abstract void ReqUserLogout();

		/// <summary>
		/// 订阅合约
		/// </summary>
		/// <param name="pInstrument"></param>
		/// <returns></returns>
		public abstract int ReqSubscribeMarketData(params string[] pInstrument);

		/// <summary>
		/// 退订
		/// </summary>
		/// <param name="pInstrument"></param>
		/// <returns></returns>
		public abstract int ReqUnSubscribeMarketData(params string[] pInstrument);
	}
}
