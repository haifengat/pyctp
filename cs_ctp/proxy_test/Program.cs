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
            string addr = "tcp://180.168.146.187:10101", broker = "9999", investor = "008107", pwd = "1", inst = "rb2101", app = "simnow_client_test", code = "0000000000000000", proc = "";
            string qaddr = "tcp://180.168.146.187:10111";
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
            //if(tt.IsLogin)
            //    tt.ReqOrderInsert("rb2101", DirectionType.Buy, OffsetType.Open, 4000, 2, 100000);
            //Console.WriteLine("Press any key to continue . . . ");
            //Console.ReadKey(true);

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
