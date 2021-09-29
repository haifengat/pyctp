using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 投资者持仓明细
	/// </summary>
	public class PositionField : BindableBase
	{
		/// <summary>
		/// 合约代码
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
		/// 持仓均价
		/// </summary>
		[DisplayName("持仓均价")]
		public double Price { get { return _Price; } set { SetProperty(ref _Price, value); } }
		private double _Price;

		/// <summary>
		/// 持仓总量
		/// </summary>
		[DisplayName("总持仓")]
		public int Position { get { return _Position; } set { SetProperty(ref _Position, value); } }
		private int _Position;

		/// <summary>
		/// 昨仓
		/// </summary>
		[DisplayName("昨仓")]
		public int YdPosition { get { return _YdPosition; } set { SetProperty(ref _YdPosition, value); } }
		private int _YdPosition;

		/// <summary>
		/// 今仓
		/// </summary>
		[DisplayName("今仓")]
		public int TdPosition { get { return _TdPosition; } set { SetProperty(ref _TdPosition, value); } }
		private int _TdPosition;

		///// <summary>
		///// 可平量
		///// </summary>
		//public int PositionClose;

		/// <summary>
		/// 占用保证金
		/// </summary>
		//public double Margin; //无此项便不再用查询

		/// <summary>
		/// 投机套保标志
		/// </summary>
		[DisplayName("投保")]
		public HedgeType Hedge { get { return _Hedge; } set { SetProperty(ref _Hedge, value); } }
		private HedgeType _Hedge;

		/// <summary>
		/// 平仓盈亏
		/// </summary>
		[DisplayName("平仓盈亏")]
		public double CloseProfit { get { return _CloseProfit; } set { SetProperty(ref _CloseProfit, value); } }
		private double _CloseProfit;

		/// <summary>
		/// 持仓盈亏
		/// </summary>
		[DisplayName("持仓盈亏")]
		public double PositionProfit { get { return _PositionProfit; } set { SetProperty(ref _PositionProfit, value); } }
		private double _PositionProfit;

		/// <summary>
		/// 手续费
		/// </summary>
		[DisplayName("手续费")]
		public double Commission { get { return _Commission; } set { SetProperty(ref _Commission, value); } }
		private double _Commission;

		/// <summary>
		/// 保证金
		/// </summary>
		[DisplayName("保证金")]
		public double Margin { get { return _Margin; } set { SetProperty(ref _Margin, value); } }
		private double _Margin;

		/// <summary>
		/// 返回:合约,多空,持仓均价,总持仓,今仓,昨仓,平仓盈亏,持仓盈亏,手续费
		/// </summary>
		/// <returns></returns>
		public override string ToString()
		{
			return $"{_InstrumentID},{_Direction},{_Price},{_Position},{_TdPosition},{_YdPosition},{_CloseProfit},{_PositionProfit},{_Commission},{_Margin}";
		}
	}
}
