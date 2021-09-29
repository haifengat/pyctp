using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace HaiFeng
{

	/// <summary>
	/// 
	/// </summary>
	[AttributeUsage(AttributeTargets.Enum | AttributeTargets.Field, AllowMultiple = false)]
	public sealed class EnumDescriptionAttribute : Attribute
	{
		private string description;
		/// <summary>
		/// 
		/// </summary>
		public string Description
		{
			get
			{
				return this.description;
			}
		}
		/// <summary>
		/// 
		/// </summary>
		/// <param name="description"></param>
		public EnumDescriptionAttribute(string description)
			: base()
		{
			this.description = description;
		}
	}
	/// <summary>
	/// 
	/// </summary>
	public static class EnumHelper
	{
		#region GetDescription
		/// <summary>
		/// Gets the <see cref="DescriptionAttribute"/> of an <see cref="Enum"/> type value.
		/// </summary>
		/// <param name="value">The <see cref="Enum"/> type value.</param>
		/// <returns>A string containing the text of the <see cref="DescriptionAttribute"/>.</returns>
		public static string GetDescription(this Enum value)
		{
			if (value == null)
			{
				throw new ArgumentNullException("value");
			}

			string description = value.ToString();
			FieldInfo fieldInfo = value.GetType().GetField(description);
			EnumDescriptionAttribute[] attributes = (EnumDescriptionAttribute[])fieldInfo.GetCustomAttributes(typeof(EnumDescriptionAttribute), false);

			if (attributes != null && attributes.Length > 0)
			{
				description = attributes[0].Description;
			}
			return description;
		}
		#endregion

		#region ToExtendedList
		/// <summary>
		///  Converts the <see cref="Enum"/> type to an <see cref="IList"/> compatible object.
		/// </summary>
		/// <param name="type">The <see cref="Enum"/> type.</param>
		/// <returns>An <see cref="IList"/> containing the enumerated type value and description.</returns>
		[SuppressMessage("Microsoft.Design", "CA1004:GenericMethodsShouldProvideTypeParameter",
			Justification = "This is a more advanced use of the ToList function; providing a type parameter has no semantic meaning for this function and would actually make the calling syntax more complicated.")]
		[EditorBrowsable(EditorBrowsableState.Advanced)]
		public static IList ToExtendedList<T>(this Type type)
		{
			if (type == null)
			{
				throw new ArgumentNullException("type");
			}

			if (!type.IsEnum)
			{
				//throw new ArgumentException(Properties.Resources.ArgumentExceptionMustBeEnum, "type");
			}

			ArrayList list = new ArrayList();
			Array enumValues = Enum.GetValues(type);

			foreach (Enum value in enumValues)
			{
				list.Add(new KeyValueTriplet<Enum, T, string>(value, (T)Convert.ChangeType(value, typeof(T), CultureInfo.InvariantCulture), GetDescription(value)));
			}

			return list;
		}
		#endregion
	}
	#region struct KeyValueTriplet
	/// <summary>
	/// Defines a key/numeric key/value triplet that can be set or retrieved.
	/// </summary>
	/// <typeparam name="TKey"></typeparam>
	/// <typeparam name="TNumericKey"></typeparam>
	/// <typeparam name="TValue"></typeparam>
	[Serializable, StructLayout(LayoutKind.Sequential)]
	[SuppressMessage("Microsoft.Design", "CA1005:AvoidExcessiveParametersOnGenericTypes")]
	[SuppressMessage("Microsoft.Performance", "CA1815:OverrideEqualsAndOperatorEqualsOnValueTypes")]
	public struct KeyValueTriplet<TKey, TNumericKey, TValue>
	{
		#region class-wide fields
		private TKey key;
		private TValue value;
		private TNumericKey numericKey;
		#endregion

		#region Key
		/// <summary>
		/// Gets the key in the key/numeric key/value triplet.
		/// </summary>
		/// <value>A <typeparamref name="TKey"/> that is the key of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>.</value>
		public TKey Key
		{
			get
			{
				return this.key;
			}
		}
		#endregion

		#region NumericKey
		/// <summary>
		/// Gets the numeric representation of the <see cref="Key"/> in the key/numeric key/value triplet.
		/// </summary>
		/// <value>A <typeparamref name="TNumericKey"/> that is the numeric key of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>.</value>
		public TNumericKey NumericKey
		{
			get
			{
				return this.numericKey;
			}
		}
		#endregion

		#region Value
		/// <summary>
		/// Gets the value in the key/numeric key/value triplet.
		/// </summary>
		/// <value>A <typeparamref name="TValue"/> that is the value of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>.</value>
		public TValue Value
		{
			get
			{
				return this.value;
			}
		}
		#endregion

		#region constructor
		/// <summary>
		/// Inititalizes a new instance of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>
		/// structure with the specified key, numeric key, and value.
		/// </summary>
		/// <param name="key">The object defined in each key/numeric key/value triplet.</param>
		/// <param name="numericKey">The numeric representation of each <paramref name="key"/> 
		/// defined in each key/numeric key/value triplet.</param>
		/// <param name="value">The definition associate with <paramref name="key"/>.</param>
		public KeyValueTriplet(TKey key, TNumericKey numericKey, TValue value)
		{
			this.key = key;
			this.value = value;
			this.numericKey = numericKey;
		}
		#endregion

		#region ToString
		/// <summary>
		/// Returns a string representation of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>,
		/// using the string representations of the key, numeric key, and value.
		/// </summary>
		/// <returns>A string representation of the <see cref="KeyValueTriplet{TKey, TNumericKey, TValue}"/>,
		/// which includes the string representations of the key, numeric key, and value.</returns>
		public override string ToString()
		{
			StringBuilder builder = new StringBuilder();
			builder.Append('[');
			if (this.Key != null)
			{
				builder.Append(this.Key.ToString());
			}
			builder.Append(", ");
			if (this.NumericKey != null)
			{
				builder.Append(this.NumericKey.ToString());
			}
			builder.Append(", ");
			if (this.Value != null)
			{
				builder.Append(this.Value.ToString());
			}
			builder.Append(']');
			return builder.ToString();
		}
		#endregion
	}
	#endregion
}
