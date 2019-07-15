using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace HaiFeng
{
    public class TestQuote : CTPQuote
    {
        string _inst;

        public TestQuote(string instrument)
        {
            _inst = instrument;

            this.OnFrontConnected += _q_OnFrontConnected;
            this.OnRspUserLogin += _q_OnRspUserLogin;
            this.OnRspUserLogout += _q_OnRspUserLogout;
            this.OnRtnTick += _q_OnRtnTick;
            this.OnRtnError += _q_OnRtnError;
        }

        public void Release()
        {
            this.ReqUserLogout();
        }

        public void Run()
        {
            this.ReqConnect();
        }

        void Log(string pMsg)
        {
            Console.WriteLine(DateTime.Now.TimeOfDay + "\t" + pMsg);
        }

        private void _q_OnFrontConnected(object sender, EventArgs e)
        {
            Log("connected");
            this.ReqUserLogin();
        }

        private void _q_OnRspUserLogin(object sender, IntEventArgs e)
        {
            if (e.Value == 0)
            {
                Log($"登录成功:{this.Investor}");
                this.ReqSubscribeMarketData(_inst);
            }
            else
            {
                //this.OnFrontConnected -= _q_OnFrontConnected;    //解决登录错误后不断重连导致再不断登录的错误
                Log($"登录错误：{e.Value}");
                this.ReqUserLogout();
            }
        }

        private void _q_OnRtnTick(object sender, TickEventArgs e)
        {
            Log($"{e.Tick.InstrumentID}\t{e.Tick.LastPrice}");
        }

        private void _q_OnRspUserLogout(object sender, IntEventArgs e)
        {
            Log($"quote logout: {e.Value}");
        }

        private void _q_OnRtnError(object sender, ErrorEventArgs e)
        {
            Log(e.ErrorMsg);
        }
    }

    class TestTrade : CTPTrade
    {
        string _inst;
        double _price;


        public TestTrade(string pInstrument, double pPrice)
        {
            _inst = pInstrument;
            _price = pPrice;
        }

        public void Release()
        {
            this.ReqUserLogout();
        }

        void Log(string pMsg)
        {
            Console.WriteLine(DateTime.Now.TimeOfDay + "\t" + pMsg);
        }

        public void Run()
        {
            this.OnFrontConnected += _t_OnFrontConnected;
            this.OnRspUserLogout += _t_OnRspUserLogout;
            this.OnRspUserLogin += _t_OnRspUserLogin;
            this.OnRtnExchangeStatus += _t_OnRtnExchangeStatus;

            this.OnRtnOrder += _t_OnRtnOrder;
            this.OnRtnTrade += _t_OnRtnTrade;
            this.OnRtnCancel += _t_OnRtnCancel;
            this.OnRtnNotice += _t_OnRtnNotice;
            Console.WriteLine(this.Version);
            this.Investor = Investor;
            this.Broker = Broker;
            this.ReqConnect();
            //this.ReqConnect("tcp://218.202.237.33:10002");
            //this.ReqConnect("tcp://172.20.28.57:41205");
        }

        private void _t_OnRtnExchangeStatus(object sender, StatusEventArgs e)
        {
            Log($"{e.Exchange}:{e.Status}");
        }

        private void _t_OnFrontConnected(object sender, EventArgs e)
        {
            this.ReqUserLogin();
        }


        private void _t_OnRspUserLogin(object sender, ErrorEventArgs e)
        {
            if (e.ErrorID == 0)
            {
                
                Log("登录成功");
                foreach (var v in this.DicPositionField.Values)
                {
                    Log($"posi:{v.InstrumentID}\t{v.Direction}\t{v.Price}\t{v.Position}");
                }
                foreach(var v in this.DicExcStatus)
                {
                    Log($"{v.Key}:{v.Value}");
                }
                //            new Thread(() =>
                //{
                //	// 需要另启线程,在onrsp中处理,会导致线程被阻塞,后续的查询无法返回.
                //	Thread.Sleep(3000);
                //	foreach (var v in this.DicPositionField.Values)
                //	{
                //		Log($"posi:{v.InstrumentID}\t{v.Direction}\t{v.Price}\t{v.Position}");
                //	}
                //}).Start();
                //this.ReqOrderInsert(_inst, DirectionType.Buy, OffsetType.Open, _price, 1, 1000);
            }
            else
            {
                Log($"登录错误：{e.ErrorID}={e.ErrorMsg}");
            }
        }

        private void _t_OnRtnNotice(object sender, StringEventArgs e)
        {
            Console.WriteLine(e.Value);
        }

        private void _t_OnRtnCancel(object sender, OrderArgs e)
        {
            Log($"cancel:{e.Value.StatusMsg}\t{e.Value.InstrumentID}\t{e.Value.Direction}\t{e.Value.Offset}\t{e.Value.LimitPrice}\t{e.Value.Volume}\t{e.Value.StatusMsg}");
        }

        private void _t_OnRtnTrade(object sender, TradeArgs e)
        {
            Log($"trade:{e.Value.InstrumentID}\t{e.Value.Direction}\t{e.Value.Offset}\t{e.Value.Price}\t{e.Value.Volume}");
            foreach (var v in this.DicPositionField.Values)
            {
                Log($"posi:{v.InstrumentID}\t{v.Direction}\t{v.Price}\t{v.Position}");
            }
        }

        private void _t_OnRtnOrder(object sender, OrderArgs e)
        {
            Log($"order:{e.Value.InstrumentID}\t{e.Value.Direction}\t{e.Value.Offset}\t{e.Value.LimitPrice}\t{e.Value.Volume}");

            if (e.Value.IsLocal)
                this.ReqOrderAction(e.Value.OrderID);
        }


        private void _t_OnRspUserLogout(object sender, IntEventArgs e)
        {
            Log("t: logout:" + e.Value);
        }
    }

}
