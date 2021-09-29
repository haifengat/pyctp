using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 委托类型
	/// </summary>
	public enum OrderType
	{
		/// <summary>
		/// 限价
		/// </summary>
		[EnumDescription("限价")]
		Limit,
		/// <summary>
		/// 市价
		/// </summary>
		[EnumDescription("市价")]
		Market,
		/// <summary>
		/// 部成即撤
		/// </summary>
		[EnumDescription("部成即撤")]
		FAK,
		/// <summary>
		/// 全成全撤
		/// </summary>
		[EnumDescription("全成全撤")]
		FOK,
	};

	/// <summary>
	/// 买卖方向
	/// </summary>
	public enum DirectionType
	{
		/// <summary>
		/// 买
		/// </summary>
		[EnumDescription("买")]
		Buy,

		/// <summary>
		/// 卖
		/// </summary>
		[EnumDescription("卖")]
		Sell
	}

	/// <summary>
	/// 开平
	/// </summary>
	public enum OffsetType
	{
		/// <summary>
		/// 开仓
		/// </summary>
		[EnumDescription("开仓")]
		Open,
		/// <summary>
		/// 平仓
		/// </summary>
		[EnumDescription("平仓")]
		Close,
		/// <summary>
		/// 平今
		/// </summary>
		[EnumDescription("平今")]
		CloseToday,
		/// <summary>
		/// 期权行权
		/// </summary>
		//Excute,
	}
	/// <summary>
	/// 委托状态
	/// </summary>
	public enum OrderStatus
	{
		/// <summary>
		/// 委托
		/// </summary>
		[EnumDescription("委托")]
		Normal,
		/// <summary>
		/// 部成
		/// </summary>
		[EnumDescription("部成")]
		Partial,
		/// <summary>
		/// 全成
		/// </summary>
		[EnumDescription("全成")]
		Filled,
		/// <summary>
		/// 撤单[某些"被拒绝"的委托也会触发此状态]
		/// </summary>
		[EnumDescription("撤单")]
		Canceled,
		/// <summary>
		/// 错误
		/// </summary>
		[EnumDescription("错误")]
		Error,
	}

	/// <summary>
	/// 交易所
	/// </summary>
	public enum Exchange
	{
		/// <summary>
		/// 大商所
		/// </summary>
		[EnumDescription("大商所")]
		DCE,
		/// <summary>
		/// 郑商所
		/// </summary>
		[EnumDescription("郑商所")]
		CZCE,
		/// <summary>
		/// 上期所
		/// </summary>
		[EnumDescription("上期所")]
		SHFE,
		/// <summary>
		/// 中金所
		/// </summary>
		[EnumDescription("中金所")]
		CFFEX,
		/// <summary>
		/// 上海国际能源交易中心股份有限公司
		/// </summary>
		[EnumDescription("能源交易中心")]
		INE,
	}

	/// <summary>
	/// 交易所状态
	/// </summary>
	public enum ExchangeStatusType
	{
		/// <summary>
		/// 开盘前
		/// </summary>
		[EnumDescription("开盘前")]
		BeforeTrading,
		/// <summary>
		/// 非交易
		/// </summary>
		[EnumDescription("非交易")]
		NoTrading,
		/// <summary>
		/// 交易中
		/// </summary>
		[EnumDescription("交易中")]
		Trading,
		/// <summary>
		/// 收盘
		/// </summary>
		[EnumDescription("收盘")]
		Closed,
	}

	/// <summary>
	/// 投机套保标志
	/// </summary>
	public enum HedgeType
	{
		/// <summary>
		/// 投机
		/// </summary>
		[EnumDescription("投机")]
		Speculation,

		/// <summary>
		/// 套利
		/// </summary>
		[EnumDescription("套利")]
		Arbitrage,

		/// <summary>
		/// 套保
		/// </summary>
		[EnumDescription("套保")]
		Hedge,
	}

	/// <summary>
	/// 品种类型
	/// </summary>
	public enum ProductClassType
	{
		/// <summary>
		/// 期货
		/// </summary>
		[EnumDescription("期货")]
		Futures,
		/// <summary>
		/// 期货期权
		/// </summary>
		[EnumDescription("期货期权")]
		Options,
		/// <summary>
		/// 组合
		/// </summary>
		[EnumDescription("组合")]
		Combination,
		/// <summary>
		/// 现货期权
		/// </summary>
		[EnumDescription("现货期权")]
		SpotOption,
	};
}
