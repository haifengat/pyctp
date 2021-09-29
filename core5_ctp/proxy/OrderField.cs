using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 报单
	/// </summary>
	public class OrderField : BindableBase
	{
		/// <summary>
		/// 报单标识
		/// </summary>
		[DisplayName("报单编号")]
		public string OrderID { get { return _OrderID; } set { if (value != null) SetProperty(ref _OrderID, value); } }
		private string _OrderID = string.Empty;

		/// <summary>
		/// 合约
		/// </summary>
		[DisplayName("合约")]
		public string InstrumentID { get { return _InstrumentID; } set { if (value != null) SetProperty(ref _InstrumentID, value); } }
		private string _InstrumentID = string.Empty;

		/// <summary>
		/// 买卖
		/// </summary>
		[DisplayName("买卖")]
		public DirectionType Direction { get { return _Direction; } set { SetProperty(ref _Direction, value); } }
		private DirectionType _Direction;

		/// <summary>
		/// 开平
		/// </summary>
		[DisplayName("开平")]
		public OffsetType Offset { get { return _Offset; } set { SetProperty(ref _Offset, value); } }
		private OffsetType _Offset;

		/// <summary>
		/// 报价
		/// </summary>
		[DisplayName("报单价格")]
		public double LimitPrice { get { return _LimitPrice; } set { SetProperty(ref _LimitPrice, value); } }
		private double _LimitPrice;

		/// <summary>
		/// 成交均价
		/// </summary>
		[DisplayName("成交均价")]
		public double AvgPrice { get { return _AvgPrice; } set { SetProperty(ref _AvgPrice, value); } }
		private double _AvgPrice;

		/// <summary>
		/// 报单时间(交易所)
		/// </summary>
		[DisplayName("报单时间")]
		public string InsertTime { get { return _InsertTime; } set { if (value != null) SetProperty(ref _InsertTime, value); } }
		private string _InsertTime = string.Empty;

		/// <summary>
		/// 最后成交时间(撤单状态时为撤单时间-IsLocal有效)
		/// </summary>
		[DisplayName("成撤时间")]
		public string TradeTime { get { return _TradeTime; } set { if (value != null) SetProperty(ref _TradeTime, value); } }
		private string _TradeTime = string.Empty;

		/// <summary>
		/// 末次成交量,trade更新
		/// </summary>
		[DisplayName("末次成交量")]
		public int TradeVolume { get { return _TradeVolume; } set { SetProperty(ref _TradeVolume, value); } }
		private int _TradeVolume;

		/// <summary>
		/// 报单数量
		/// </summary>
		[DisplayName("报单数量")]
		public int Volume { get { return _Volume; } set { SetProperty(ref _Volume, value); } }
		private int _Volume;

		/// <summary>
		/// 未成交,trade更新
		/// </summary>
		[DisplayName("未成交手数")]
		public int VolumeLeft { get { return _VolumeLeft; } set { SetProperty(ref _VolumeLeft, value); } }
		private int _VolumeLeft;

		/// <summary>
		/// 投保
		/// </summary>
		[DisplayName("投保")]
		public HedgeType Hedge { get { return _Hedge; } set { SetProperty(ref _Hedge, value); } }
		private HedgeType _Hedge;

		/// <summary>
		/// 状态
		/// </summary>
		[DisplayName("状态")]
		public OrderStatus Status { get { return _Status; } set { SetProperty(ref _Status, value); } }
		private OrderStatus _Status;

		/// <summary>
		/// 状态描述
		/// </summary>
		[DisplayName("详细状态")]
		public string StatusMsg { get { return _StatusMsg; } set { if (value != null) SetProperty(ref _StatusMsg, value); } }
		private string _StatusMsg = string.Empty;

		/// <summary>
		/// 是否自身委托
		/// </summary>
		[DisplayName("本地报单")]
		public bool IsLocal { get { return _IsLocal; } set { SetProperty(ref _IsLocal, value); } }
		private bool _IsLocal;

		/// <summary>
		/// 客户自定义字段(xSpeed仅支持数字)
		/// </summary>
		[DisplayName("自定义")]
		public int Custom { get { return _Custom; } set { SetProperty(ref _Custom, value); } }
		private int _Custom;

		/// <summary>
		/// 交易所生成的ID
		/// </summary>
		[DisplayName("交易所编号")]
		public string SysID { get { return _SysID; } set { if (value != null) SetProperty(ref _SysID, value); } }
		private string _SysID = string.Empty;

		/// <summary>
		/// 返回:标识,合约,买卖,开平,报价,手数,报单时间,成交均价,剩余手数,成交时间,状态,状态信息,本地,自定义,交易所编号
		/// </summary>
		/// <returns></returns>
		public override string ToString()
		{
			return $"{_OrderID}, {_InstrumentID},{_Direction},{_Offset},{_LimitPrice},{_Volume},{_InsertTime},{_AvgPrice},{_VolumeLeft},{_TradeTime},{_Status},{_StatusMsg},{_IsLocal},{_Custom},{_SysID}";
		}
	}
}
