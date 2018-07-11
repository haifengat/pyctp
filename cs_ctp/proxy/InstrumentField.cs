using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{

	/// <summary>
	/// 合约信息
	/// </summary>
	public class InstrumentField : BindableBase
	{
		/// <summary>
		/// 合约代码
		/// </summary>
		[DisplayName("合约")]
		public string InstrumentID { get { return _InstrumentID; } set { SetProperty(ref _InstrumentID, value); } }
		private string _InstrumentID;

		/// <summary>
		/// 品种代码
		/// </summary>
		[DisplayName("品种代码")]
		public string ProductID { get { return _ProductID; } set { SetProperty(ref _ProductID, value); } }
		private string _ProductID;

		/// <summary>
		/// 交易所代码
		/// </summary>
		[DisplayName("交易所")]
		public Exchange ExchangeID { get { return _ExchangeID; } set { SetProperty(ref _ExchangeID, value); } }
		private Exchange _ExchangeID = Exchange.SHFE;

		/// <summary>
		/// 合约数量乘数
		/// </summary>
		[DisplayName("合约乘数")]
		public int VolumeMultiple { get { return _VolumeMultiple; } set { SetProperty(ref _VolumeMultiple, value); } }
		private int _VolumeMultiple;

		/// <summary>
		/// 最小变动价位
		/// </summary>
		[DisplayName("最小变动")]
		public double PriceTick { get { return _PriceTick; } set { SetProperty(ref _PriceTick, value); } }
		private double _PriceTick;

		/// <summary>
		/// 品种类型
		/// </summary>
		[DisplayName("品种类型")]
		public ProductClassType ProductClass { get { return _ProductClass; } set { SetProperty(ref _ProductClass, value); } }
		private ProductClassType _ProductClass;

		/// <summary>
		/// 最大委托量[限价]
		/// </summary>
		[DisplayName("最大委托量")]
		public int MaxOrderVolume { get { return _MaxOrderVolume; } set { SetProperty(ref _MaxOrderVolume, value); } }
		private int _MaxOrderVolume;
	}
}
