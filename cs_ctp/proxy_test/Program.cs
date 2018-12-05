using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
	class Program
	{
		static void Main(string[] args)
		{
			// investor, pwd, instrument, price for buy
			TestTrade tt = null;
			string investor = "008107", pwd = "1", inst = "rb1905";
			double price_for_buy = 3400;
			if (args.Length == 4)
			{
				investor = args[0];
				pwd = args[1];
				inst = args[2];
				price_for_buy = double.Parse(args[3]);
			}

			tt = new TestTrade(investor, pwd, inst, price_for_buy);
			tt.Run();
			Console.WriteLine("Press any key to continue . . . ");
			Console.ReadKey(true);

			TestQuote tq = new TestQuote(investor, pwd, inst);
			tq.Run();
			Console.WriteLine("Press any key to continue . . . ");
			Console.ReadKey(true);

			tt.Release();
			tq.Release();
			Console.ReadKey(true);
        }
	}
}
