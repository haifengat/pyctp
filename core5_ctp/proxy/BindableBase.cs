using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{

	/// <summary>
	/// {get;set;} = >  { get { return _Status; } set { SetProperty(ref ^1, value); } } }
	/// </summary>
	public abstract class BindableBase : INotifyPropertyChanged
	{
		/// <summary>
		/// 
		/// </summary>
		public event PropertyChangedEventHandler PropertyChanged;

		/// <summary>
		/// 
		/// </summary>
		/// <typeparam name="T"></typeparam>
		/// <param name="storage"></param>
		/// <param name="value"></param>
		/// <param name="propertyName"></param>
		/// <returns></returns>
		protected bool SetProperty<T>(ref T storage, T value, [System.Runtime.CompilerServices.CallerMemberName] String propertyName = null)
		{
			if (string.IsNullOrEmpty(propertyName)) return false;
			if (object.Equals(storage, value)) return false;
			try
			{
				storage = value;
				//ThreadPool.QueueUserWorkItem(new WaitCallback(NotifyPropertyChanged), propertyName);

				if (PropertyChanged != null)
				{
					PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
				}
				return true;
			}
			catch
			{
				return false;
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param name="propertyName"></param>
		protected void NotifyPropertyChanged(object propertyName)
		{
			if (PropertyChanged != null)
			{
				PropertyChanged(this, new PropertyChangedEventArgs((string)propertyName));
			}
		}
	}
}
