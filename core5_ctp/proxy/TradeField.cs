using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 成交
	/// </summary>
	public class TradeField : BindableBase
	{
		/// <summary>
		/// 成交编号
		/// </summary>
		[DisplayName("成交编号")]
		public string TradeID { get { return _TradeID; } set { if (value != null) SetProperty(ref _TradeID, value); } }
		private string _TradeID = string.Empty;

		/// <summary>
		/// 合约代码
		/// </summary>
		[DisplayName("合约")]
		public string InstrumentID { get { return _InstrumentID; } set { if (value != null) SetProperty(ref _InstrumentID, value); } }
		private string _InstrumentID = string.Empty;

		/// <summary>
		/// 交易所代码
		/// </summary>
		[DisplayName("交易所")]
		public Exchange ExchangeID { get { return _ExchangeID; } set { SetProperty(ref _ExchangeID, value); } }
		private Exchange _ExchangeID = Exchange.SHFE;

		/// <summary>
		/// 买卖方向
		/// </summary>
		[DisplayName("买卖")]
		public DirectionType Direction { get { return _Direction; } set { SetProperty(ref _Direction, value); } }
		private DirectionType _Direction;

		/// <summary>
		/// 开平标志
		/// </summary>
		[DisplayName("开平")]
		public OffsetType Offset { get { return _Offset; } set { SetProperty(ref _Offset, value); } }
		private OffsetType _Offset;

		/// <summary>
		/// 投机套保标志
		/// </summary>
		[DisplayName("投保")]
		public HedgeType Hedge { get { return _Hedge; } set { SetProperty(ref _Hedge, value); } }
		private HedgeType _Hedge;

		/// <summary>
		/// 成交价格
		/// </summary>
		[DisplayName("成交价格")]
		public double Price { get { return _Price; } set { SetProperty(ref _Price, value); } }
		private double _Price;

		/// <summary>
		/// 成交数量
		/// </summary>
		[DisplayName("成交数量")]
		public int Volume { get { return _Volume; } set { SetProperty(ref _Volume, value); } }
		private int _Volume;

		/// <summary>
		/// 成交时间
		/// </summary>
		[DisplayName("成交时间")]
		public string TradeTime { get { return _TradeTime; } set { if (value != null) SetProperty(ref _TradeTime, value); } }
		private string _TradeTime;

		/// <summary>
		/// 交易日
		/// </summary>
		[DisplayName("交易日")]
		public string TradingDay { get { return _TradingDay; } set { if (value != null) SetProperty(ref _TradingDay, value); } }
		private string _TradingDay = string.Empty;

		/// <summary>
		/// 对应的委托标识
		/// </summary>
		[DisplayName("报单编号")]
		public string OrderID { get { return _OrderID; } set { if (value != null) SetProperty(ref _OrderID, value); } }
		private string _OrderID = string.Empty;

		/// <summary>
		/// 交易所生成的编号
		/// </summary>
		[DisplayName("交易所编号")]
		public string SysID { get { return _SysID; } set { if (value != null) SetProperty(ref _SysID, value); } }
		private string _SysID = string.Empty;

		/// <summary>
		/// 返回:标识,合约,买卖,开平,成交价,手数,成交时间,报单单编号,交易所编号
		/// </summary>
		/// <returns></returns>
		public override string ToString()
		{
			return $"{_TradeID}, {_InstrumentID},{_Direction},{_Offset},{_Price},{_Volume},{_TradeTime},{_OrderID},{_SysID}";
		}
	}
}
