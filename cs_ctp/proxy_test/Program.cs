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
            string addr = "tcp://180.168.146.187:13030", broker = "9999", investor = "", pwd = "", inst = "rb1909", app = "", code = "", proc = "";
            string qaddr = "tcp://180.168.146.187:13040";
            double price_for_buy = 3900;

            tt = new TestTrade(inst, price_for_buy)
            {
                FrontAddr = addr,
                Broker = broker,
                Investor = investor,
                Password = pwd,
                AppID = app,
                AuthCode = code,
                ProductInfo = app,
            };

            tt.Run();
            Console.WriteLine("Press any key to continue . . . ");
            Console.ReadKey(true);

            TestQuote tq = new TestQuote(inst)
            {
                FrontAddr = qaddr,
                Broker = broker,
            };
            tq.Run();
            Console.WriteLine("Press any key to continue . . . ");
            Console.ReadKey(true);

            tt.Release();
            tq.Release();
            Console.ReadKey(true);
        }
    }
}
