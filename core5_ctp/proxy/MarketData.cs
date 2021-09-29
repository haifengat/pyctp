using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	/// <summary>
	/// 
	/// </summary>
	public class MarketData : BindableBase
	{
		/// <summary>
		/// 合约代码SetProperty(ref _InstrumentID, value);
		/// </summary>
		[DisplayName("合约")]
		public string InstrumentID { get { return _InstrumentID; } set { SetProperty(ref _InstrumentID, value); } }
		private string _InstrumentID;
		/// <summary>
		/// 最新价
		/// </summary>
		[DisplayName("最新价")]
		public double LastPrice { get { return _LastPrice; } set { SetProperty(ref _LastPrice, value); } }
		private double _LastPrice;
		/// <summary>
		///申买价一
		/// </summary>
		[DisplayName("申买价")]
		public double BidPrice { get { return _BidPrice; } set { SetProperty(ref _BidPrice, value); } }
		private double _BidPrice;
		/// <summary>
		/// 申买量一
		/// </summary>
		[DisplayName("申买量")]
		public int BidVolume { get { return _BidVolume; } set { SetProperty(ref _BidVolume, value); } }
		private int _BidVolume;
		/// <summary>
		///申卖价一
		/// </summary>
		[DisplayName("申卖价")]
		public double AskPrice { get { return _AskPrice; } set { SetProperty(ref _AskPrice, value); } }
		private double _AskPrice;
		/// <summary>
		///申卖量一
		/// </summary>
		[DisplayName("申卖量")]
		public int AskVolume { get { return _AskVolume; } set { SetProperty(ref _AskVolume, value); } }
		private int _AskVolume;
		/// <summary>
		///当日均价
		/// </summary>
		[DisplayName("当日均价")]
		public double AveragePrice { get { return _AveragePrice; } set { SetProperty(ref _AveragePrice, value); } }
		private double _AveragePrice;
		/// <summary>
		///数量
		/// </summary>
		[DisplayName("数量")]
		public int Volume { get { return _Volume; } set { SetProperty(ref _Volume, value); } }
		private int _Volume;
		/// <summary>
		///持仓量
		/// </summary>
		[DisplayName("持仓量")]
		public double OpenInterest { get { return _OpenInterest; } set { SetProperty(ref _OpenInterest, value); } }
		private double _OpenInterest;
		/// <summary>
		///最后修改时间:yyyyMMdd HH:mm:ss(20141114:日期由主程序处理,因大商所取到的actionday==tradingday)
		/// </summary>
		[DisplayName("时间")]
		public string UpdateTime { get { return _UpdateTime; } set { SetProperty(ref _UpdateTime, value); } }
		private string _UpdateTime;
		/// <summary>
		///最后修改毫秒
		/// </summary>
		[DisplayName("毫秒")]
		public int UpdateMillisec { get { return _UpdateMillisec; } set { SetProperty(ref _UpdateMillisec, value); } }
		private int _UpdateMillisec;
		/// <summary>
		///涨停板价
		/// </summary>
		[DisplayName("涨板")]
		public double UpperLimitPrice { get { return _UpperLimitPrice; } set { SetProperty(ref _UpperLimitPrice, value); } }
		private double _UpperLimitPrice;
		/// <summary>
		///跌停板价
		/// </summary>
		[DisplayName("跌板")]
		public double LowerLimitPrice { get { return _LowerLimitPrice; } set { SetProperty(ref _LowerLimitPrice, value); } }
		private double _LowerLimitPrice;
		//int IComparable.CompareTo(object obj)
		//{
		//	MarketData y = (MarketData)obj;
		//	return DateTime.ParseExact(UpdateTime, "yyyyMMdd HH:mm:ss", null).AddMilliseconds(UpdateMillisec).CompareTo(DateTime.ParseExact(y.UpdateTime, "yyyyMMdd HH:mm:ss", null).AddMilliseconds(y.UpdateMillisec));
		//}
	}
}
