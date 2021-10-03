using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 
	/// </summary>
	public class IntEventArgs : EventArgs
	{
		/// <summary>
		/// 错误代码
		/// </summary>
		public int Value = 0;
	}

	/// <summary>
	/// 数据事件
	/// </summary>
	public class TickEventArgs : EventArgs
	{
		/// <summary>
		/// 行情数据
		/// </summary>
		public MarketData Tick;
	}


	/// <summary>
	/// 
	/// </summary>
	public class StringEventArgs : EventArgs
	{
		/// <summary>
		/// 错误代码
		/// </summary>
		public string Value = string.Empty;
	}

	/// <summary>
	/// 
	/// </summary>
	public class ErrorEventArgs : EventArgs
	{
		/// <summary>
		/// 错误代码
		/// </summary>
		public int ErrorID = 0;
		/// <summary>
		/// 错误说明
		/// </summary>
		public string ErrorMsg = string.Empty;
	}

	/// <summary>
	/// 
	/// </summary>
	public class StatusEventArgs : EventArgs
	{
		/// <summary>
		/// 交易所/品种/合约
		/// </summary>
		public string Exchange = string.Empty;
		/// <summary>
		/// 交易状态
		/// </summary>
		public ExchangeStatusType Status = ExchangeStatusType.Trading;
	}

	/// <summary>
	/// 报单状态改变响应
	/// </summary>
	public class OrderArgs : EventArgs
	{
		/// <summary>
		/// 报单
		/// </summary>
		public OrderField Value;
	}
	public class ErrOrderArgs : EventArgs
	{
		/// <summary>
		/// 报单
		/// </summary>
		public OrderField Value;

		public int ErrorID;

		public string ErrorMsg;
	}

	/// <summary>
	/// 报单成交响应
	/// </summary>
	public class TradeArgs : EventArgs
	{
		/// <summary>
		/// 报单
		/// </summary>
		public TradeField Value;
	}
}
