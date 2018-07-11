using System;
using System.Collections;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;

namespace HaiFeng
{
	public abstract class Trade
	{
		/// <summary>
		/// 交易所/品种/合约交易状态
		/// </summary>
		public ConcurrentDictionary<string, ExchangeStatusType> DicExcStatus = new ConcurrentDictionary<string, ExchangeStatusType>();

		/// <summary>
		/// 合约信息
		/// </summary>
		public ConcurrentDictionary<string, InstrumentField> DicInstrumentField = new ConcurrentDictionary<string, InstrumentField>();

		/// <summary>
		/// 报单. CTP:session|front|orderef
		/// </summary>
		public ConcurrentDictionary<string, OrderField> DicOrderField = new ConcurrentDictionary<string, OrderField>();

		/// <summary>
		/// 成交. CTP:TradeID+Direct(区分自成交)
		/// </summary>
		public ConcurrentDictionary<string, TradeField> DicTradeField = new ConcurrentDictionary<string, TradeField>();

		/// <summary>
		/// 持仓
		/// </summary>
		public ConcurrentDictionary<string, PositionField> DicPositionField = new ConcurrentDictionary<string, PositionField>();

		/// <summary>
		/// 资金权益
		/// </summary>
		public TradingAccount TradingAccount = new TradingAccount();


		/// <summary>
		/// 连接
		/// </summary>
		/// <param name="pFront"></param>
		/// <returns></returns>
		public abstract int ReqConnect(string pFront);

		/// <summary>
		/// 登录
		/// </summary>
		/// <param name="pInvestor">用户名</param>
		/// <param name="pPassword">密码</param>
		/// <param name="pBroker">经纪商代码</param>
		/// <returns></returns>
		public abstract int ReqUserLogin(string pInvestor, string pPassword, string pBroker);

		/// <summary>
		/// 交易日
		/// </summary>
		public abstract string TradingDay { get; protected set; }

		/// <summary>
		/// 是否登录成功
		/// </summary>
		public abstract bool IsLogin { get; protected set; }

		/// <summary>
		/// 退出
		/// </summary>
		/// <returns></returns>
		public abstract void ReqUserLogout();

		public abstract int ReqAuth(string pProductInfo, string pAuthCode);


		/// <summary>
		/// 委托
		/// </summary>
		/// <param name="pInstrument">合约</param>
		/// <param name="pDirection">买卖</param>
		/// <param name="pOffset">开平</param>
		/// <param name="pPrice">价格</param>
		/// <param name="pVolume">数量</param>
		/// <param name="pType">委托类型</param>
		/// <param name="pCustom">自定义字段(6位数字)</param>
		/// <param name="pHedge">投保</param>
		/// <returns></returns>
		public abstract int ReqOrderInsert(string pInstrument, DirectionType pDirection, OffsetType pOffset, double pPrice, int pVolume, int pCustom, OrderType pType = OrderType.Limit, HedgeType pHedge = HedgeType.Speculation);

		/// <summary>
		/// 
		/// </summary>
		/// <param name="pOrderId"></param>
		/// <returns></returns>
		public abstract int ReqOrderAction(string pOrderId);

		/// <summary>
		/// 
		/// </summary>
		/// <param name="pOldPassword"></param>
		/// <param name="pNewPassword"></param>
		/// <returns></returns>
		public abstract int ReqUserPasswordUpdate(string pOldPassword, string pNewPassword);

		/// <summary>
		/// 取交易所时间
		/// </summary>
		/// <returns></returns>
		public abstract TimeSpan GetExchangeTime();

		/// <summary>
		/// 取交易所状态(参数错误时返回Closed)
		/// </summary>
		/// <returns></returns>
		public abstract ExchangeStatusType GetInstrumentStatus(string pExc);


		#region 注册响应
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

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnNotice(object sender, StringEventArgs e);

		internal RtnNotice _OnRtnNotice;

		/// <summary>
		/// 
		/// </summary>
		public event RtnNotice OnRtnNotice
		{
			add
			{
				_OnRtnNotice += value;
			}
			remove
			{
				_OnRtnNotice -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnExchangeStatus(object sender, StatusEventArgs e);

		internal RtnExchangeStatus _OnRtnExchangeStatus;

		/// <summary>
		/// 
		/// </summary>
		public event RtnExchangeStatus OnRtnExchangeStatus
		{
			add
			{
				_OnRtnExchangeStatus += value;
			}
			remove
			{
				_OnRtnExchangeStatus -= value;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnOrder(object sender, OrderArgs e);

		internal RtnOrder _OnRtnOrder;

		/// <summary>
		/// 
		/// </summary>
		public event RtnOrder OnRtnOrder
		{
			add
			{
				_OnRtnOrder += value;
			}
			remove
			{
				_OnRtnOrder -= value;
			}
		}


		public delegate void RtnErrOrder(object sender, ErrOrderArgs e);
		internal RtnErrOrder _OnRtnErrOrder;

		/// <summary>
		/// 
		/// </summary>
		public event RtnErrOrder OnRtnErrOrder
		{
			add
			{
				_OnRtnErrOrder += value;
			}
			remove
			{
				_OnRtnErrOrder -= value;
			}
		}

		internal RtnErrOrder _OnRtnErrCancel;

		/// <summary>
		/// 
		/// </summary>
		public event RtnErrOrder OnRtnErrCancel
		{
			add
			{
				_OnRtnErrCancel += value;
			}
			remove
			{
				_OnRtnErrCancel -= value;
			}
		}

		internal RtnOrder _OnRtnCancel;

		/// <summary>
		/// 撤单响应
		/// </summary>
		public event RtnOrder OnRtnCancel
		{
			add
			{
				_OnRtnCancel += value;
			}
			remove
			{
				_OnRtnCancel -= value;
			}
		}
		

		/// <summary>
		/// 成交响应
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		public delegate void RtnTrade(object sender, TradeArgs e);

		internal RtnTrade _OnRtnTrade;

		/// <summary>
		/// 
		/// </summary>
		public event RtnTrade OnRtnTrade
		{
			add
			{
				_OnRtnTrade += value;
			}
			remove
			{
				_OnRtnTrade -= value;
			}
		}

		internal RtnError _OnRtnPasswordUpdate;

		/// <summary>
		/// 
		/// </summary>
		public event RtnError OnRtnPasswordUpdate
		{
			add
			{
				_OnRtnPasswordUpdate += value;
			}
			remove
			{
				_OnRtnPasswordUpdate -= value;
			}
		}
		#endregion
	}
}

