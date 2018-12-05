using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HaiFeng
{
    class Program
    {
        static ctp_quote q = null;
        static ctp_trade t = null;
        static void Main(string[] args)
        {
            q = new ctp_quote(new FileInfo("../../../dll/ctp_quote.dll").FullName);
            t = new ctp_trade(new FileInfo("../../../dll/ctp_trade.dll").FullName);

            t.SetOnFrontConnected(t_connected);
            t.SetOnRspUserLogin(t_login);
            t.SetOnRtnTradingNotice(t_notice);

            q.SetOnFrontConnected(connected);
            q.SetOnRspUserLogin(login);

            t.RegisterFront("tcp://180.168.146.187:10000");
            q.RegisterFront("tcp://180.168.146.187:10010");

            t.Init();
            q.Init();
            Console.ReadLine();
        }

        private static void t_notice(ref CThostFtdcTradingNoticeInfoField pTradingNoticeInfo)
        {
            Console.WriteLine(pTradingNoticeInfo.SendTime + pTradingNoticeInfo.FieldContent);
        }

        private static void t_login(ref CThostFtdcRspUserLoginField pRspUserLogin, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            Console.WriteLine("t:" + pRspInfo.ErrorMsg);
        }

        private static void t_connected()
        {
            Console.WriteLine("t:connected");
            t.ReqUserLogin(BrokerID: "9999", UserID: "008107", Password: "1");
        }

        private static void login(ref CThostFtdcRspUserLoginField pRspUserLogin, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            Console.WriteLine(pRspInfo.ErrorMsg);
        }

        private static void connected()
        {
            Console.WriteLine("connected");
            q.ReqUserLogin(BrokerID: "9999", UserID: "008105", Password: "1");
        }
    }
}
