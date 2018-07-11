using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 帐户权益
	/// </summary>
	public class TradingAccount : BindableBase
	{
		/// <summary>
		/// 上次结算准备金
		/// </summary>
		[DisplayName("静态权益")]
		public double PreBalance { get { return _PreBalance; } set { SetProperty(ref _PreBalance, value); } }
		private double _PreBalance;

		/// <summary>
		/// 持仓盈亏
		/// </summary>
		[DisplayName("持仓盈亏")]
		public double PositionProfit { get { return _PositionProfit; } set { SetProperty(ref _PositionProfit, value); } }
		private double _PositionProfit;

		/// <summary>
		/// 平仓盈亏
		/// </summary>
		[DisplayName("平仓盈亏")]
		public double CloseProfit { get { return _CloseProfit; } set { SetProperty(ref _CloseProfit, value); } }
		private double _CloseProfit;

		/// <summary>
		/// 手续费
		/// </summary>
		[DisplayName("手续费")]
		public double Commission { get { return _Commission; } set { SetProperty(ref _Commission, value); } }
		private double _Commission;

		/// <summary>
		/// 当前保证金总额
		/// </summary>
		[DisplayName("当前保证金")]
		public double CurrMargin { get { return _CurrMargin; } set { SetProperty(ref _CurrMargin, value); } }
		private double _CurrMargin;

		/// <summary>
		/// 冻结的资金
		/// </summary>
		[DisplayName("冻结资金")]
		public double FrozenCash { get { return _FrozenCash; } set { SetProperty(ref _FrozenCash, value); } }
		private double _FrozenCash;

		/// <summary>
		/// 可用资金
		/// </summary>
		[DisplayName("可用资金")]
		public double Available { get { return _Available; } set { SetProperty(ref _Available, value); } }
		private double _Available;

		/// <summary>
		/// 动态权益
		/// </summary>
		[DisplayName("动态权益")]
		public double Fund { get { return _Fund; } set { SetProperty(ref _Fund, value); } }
		private double _Fund;

		/// <summary>
		/// 风险度
		/// </summary>
		[DisplayName("风险度")]
		public double Risk { get { return _Risk; } set { SetProperty(ref _Risk, value); } }
		private double _Risk;

		/// <summary>
		/// 返回:静态权益,持仓盈亏,平仓盈亏,保证金占用,冻结资金,可用资金,动态权益
		/// </summary>
		/// <returns></returns>
		public override string ToString()
		{
			return $"{_PreBalance},{_PositionProfit},{_CloseProfit},{_CurrMargin},{_FrozenCash},{_Available},{_Fund},{_Risk}";
		}
	}
}
