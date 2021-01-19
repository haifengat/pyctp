using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using HaiFeng.Properties;
using static HaiFeng.ctp_trade;

namespace HaiFeng
{
    public abstract class CTPTrade : Trade
    {
        ctp_trade _t = null;
        private int _session = 0;
        private int _front = 0;
        private Thread _tIsLogin = null;
        private DateTime _rtnOrderTime = DateTime.MinValue, _excTime = DateTime.MinValue;
        private readonly List<CThostFtdcInvestorPositionField> _listPosi = new List<CThostFtdcInvestorPositionField>();
        private readonly ConcurrentDictionary<string, string> _dicSysidSfrId = new ConcurrentDictionary<string, string>();
        //用来处理成交先返回的情况:在order中重新调用onrtntrade
        private readonly ConcurrentDictionary<string, List<CThostFtdcTradeField>> _sysidTrade = new ConcurrentDictionary<string, List<CThostFtdcTradeField>>();
        private readonly Stopwatch _sw = new Stopwatch();
        private readonly List<Delegate> _listDele = new List<Delegate>();
        private int _ref = 0;

        /// <summary>
        /// 
        /// </summary>
		public CTPTrade()
        {
            _t = new ctp_trade();
            this.SetCallBack();
        }

        /// <summary>
        /// 前置地址端口
        /// </summary>
        public override string FrontAddr { get; set; }

        /// <summary>
        /// 帐号
        /// </summary>
        public override string Investor { get; set; }

        /// <summary>
        /// 密码
        /// </summary>
        public override string Password { get; set; }

        /// <summary>
        /// 经纪商代码
        /// </summary>
        public override string Broker { get; set; }

        /// <summary>
        /// 
        /// </summary>
        public string ProductInfo { get; set; }

        /// <summary>
        /// 
        /// </summary>
        public string AppID { get; set; }

        /// <summary>
        /// 
        /// </summary>
        public string AuthCode { get; set; }

        /// <summary>
        /// 直接方式不需要
        /// </summary>
        public string IP { get; set; }

        /// <summary>
        /// 直接方式不需要
        /// </summary>
        public int Port { get; set; }

        Delegate AddDele(Delegate d) { _listDele.Add(d); return d; }

        /// <summary>
        /// 接口版本
        /// </summary>
        public string Version => _t.GetVersion();

        //响应注册
        void SetCallBack()
        {
            _t.SetOnFrontConnected((DeleOnFrontConnected)AddDele(new DeleOnFrontConnected(CTPOnFrontConnected)));
            _t.SetOnRspUserLogin((DeleOnRspUserLogin)AddDele(new DeleOnRspUserLogin(CTPOnRspUserLogin)));
            _t.SetOnRspSettlementInfoConfirm((DeleOnRspSettlementInfoConfirm)AddDele(new DeleOnRspSettlementInfoConfirm(CTPOnRspSettlementInfoConfirm)));
            _t.SetOnFrontDisconnected((DeleOnFrontDisconnected)AddDele(new DeleOnFrontDisconnected(CTPOnFrontDisconnected)));
            _t.SetOnRspQryInstrument((DeleOnRspQryInstrument)AddDele(new DeleOnRspQryInstrument(CTPOnRspQryInstrument)));
            _t.SetOnRspQryClassifiedInstrument((DeleOnRspQryClassifiedInstrument)AddDele(new DeleOnRspQryClassifiedInstrument(CTPOnRspQryClassifiedInstrument)));
            _t.SetOnRspQryInvestorPosition((DeleOnRspQryInvestorPosition)AddDele(new DeleOnRspQryInvestorPosition(CTPOnRspQryInvestorPosition)));
            _t.SetOnRspQryTradingAccount((DeleOnRspQryTradingAccount)AddDele(new DeleOnRspQryTradingAccount(CTPOnRspQryTradingAccount)));
            _t.SetOnRspOrderInsert((DeleOnRspOrderInsert)AddDele(new DeleOnRspOrderInsert(CTPOnRspOrderInsert)));
            _t.SetOnErrRtnOrderInsert((DeleOnErrRtnOrderInsert)AddDele(new DeleOnErrRtnOrderInsert(CTPOnErrRtnOrderInsert)));
            _t.SetOnErrRtnOrderAction((DeleOnErrRtnOrderAction)AddDele(new DeleOnErrRtnOrderAction(CTPOnErrRtnOrderAction)));
            _t.SetOnRspOrderAction((DeleOnRspOrderAction)AddDele(new DeleOnRspOrderAction(CTPOnRspOrderAction)));
            _t.SetOnRtnOrder((DeleOnRtnOrder)AddDele(new DeleOnRtnOrder(CTPOnRtnOrder)));
            _t.SetOnRtnTrade((DeleOnRtnTrade)AddDele(new DeleOnRtnTrade(CTPOnRtnTrade)));
            _t.SetOnRtnInstrumentStatus((DeleOnRtnInstrumentStatus)AddDele(new DeleOnRtnInstrumentStatus(CTPOnRtnInstrumentStatus)));
            _t.SetOnRtnTradingNotice((DeleOnRtnTradingNotice)AddDele(new DeleOnRtnTradingNotice(CTPOnRtnTradingNotice)));
            _t.SetOnRspUserPasswordUpdate((DeleOnRspUserPasswordUpdate)AddDele(new DeleOnRspUserPasswordUpdate(CTPOnRspUserPasswordUpdate)));
            _t.SetOnRspError((DeleOnRspError)AddDele(new DeleOnRspError(CTPOnRspError)));
            _t.SetOnRspAuthenticate((DeleOnRspAuthenticate)AddDele(new DeleOnRspAuthenticate(CTPOnRspAuth)));
        }

        private void CTPOnRspAuth(ref CThostFtdcRspAuthenticateField pRspAuthenticateField, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (pRspInfo.ErrorID == 0)
            {
                switch (pRspAuthenticateField.AppType)
                {
                    // 多对多
                    case TThostFtdcAppTypeType.THOST_FTDC_APP_TYPE_InvestorRelay:
                        _t.RegisterUserSystemInfo(this.Broker, this.Investor, 1, "", this.IP, this.Port, DateTime.Now.ToString("HH:mm:ss"), this.AppID);
                        break;
                    case TThostFtdcAppTypeType.THOST_FTDC_APP_TYPE_OperatorRelay:
                        _t.SubmitUserSystemInfo(this.Broker, this.Investor, 1, "", this.IP, this.Port, DateTime.Now.ToString("HH:mm:ss"), this.AppID);
                        break;
                    default:
                        break;
                }
                _t.ReqUserLogin(BrokerID: this.Broker, UserID: this.Investor, Password: this.Password, UserProductInfo: this.ProductInfo);
            }
            else
            {
                _OnRspUserLogin?.Invoke(this, new ErrorEventArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = $"认证错误:{pRspInfo.ErrorMsg}" });
            }
        }

        private void CTPOnFrontConnected()
        {
            _OnFrontConnected?.Invoke(this, new EventArgs());
        }

        private void CTPOnFrontDisconnected(int nReason)
        {
            this.IsLogin = false;
            _OnRspUserLogout?.Invoke(this, new IntEventArgs { Value = nReason });
            SetCallBack();
        }

        private void CTPOnRspUserLogin(ref CThostFtdcRspUserLoginField pRspUserLogin, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            //避免登录错误后不断重连
            if (pRspInfo.ErrorID != 0)
                _t.SetOnFrontDisconnected(null);
            //else //正常登录时注册连接事件(后续自动重连时可自行登录)
            //_t.SetOnFrontConnected(CTPOnFrontConnected);

            if (pRspInfo.ErrorID == 0)
            {
                //IsLogin = true; //position中完成
                this.TradingDay = pRspUserLogin.TradingDay; // Marshal.PtrToStringAnsi(_t.GetTradingDay());
                _session = pRspUserLogin.SessionID;
                _front = pRspUserLogin.FrontID;
                //_orderref = pRspUserLogin.MaxOrderRef;

                _t.ReqSettlementInfoConfirm(this.Broker, this.Investor);
            }
            else
            {
                _OnRspUserLogin?.Invoke(this, new ErrorEventArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg });
            }
        }

        private void CTPOnRspSettlementInfoConfirm(ref CThostFtdcSettlementInfoConfirmField pSettlementInfoConfirm, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (this.Broker == "9999")
                _t.ReqQryInstrument();
            else
                _t.ReqQryClassifiedInstrument(TradingType: TThostFtdcTradingTypeType.THOST_FTDC_TD_TRADE, ClassType: TThostFtdcClassTypeType.THOST_FTDC_INS_ALL);
        }

        private void CTPOnRtnInstrumentStatus(ref CThostFtdcInstrumentStatusField pInstrumentStatus)
        {
            ExchangeStatusType status = ExchangeStatusType.BeforeTrading;
            switch (pInstrumentStatus.InstrumentStatus)
            {
                case TThostFtdcInstrumentStatusType.THOST_FTDC_IS_Continous:
                    status = ExchangeStatusType.Trading;
                    break;
                case TThostFtdcInstrumentStatusType.THOST_FTDC_IS_Closed:
                    status = ExchangeStatusType.Closed;
                    break;
                case TThostFtdcInstrumentStatusType.THOST_FTDC_IS_NoTrading:
                    status = ExchangeStatusType.NoTrading;
                    break;
            }
            DicExcStatus[pInstrumentStatus.InstrumentID] = status;
            if (IsLogin)
            {
                _OnRtnExchangeStatus?.Invoke(this, new StatusEventArgs { Exchange = pInstrumentStatus.InstrumentID, Status = status });
            }
        }

        private void CTPOnRspQryClassifiedInstrument(ref CThostFtdcInstrumentField pInstrument, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            CTPOnRspQryInstrument(ref pInstrument,ref pRspInfo, nRequestID, bIsLast);
        }

        private void CTPOnRspQryInstrument(ref CThostFtdcInstrumentField pInstrument, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            var field = new InstrumentField
            {
                //ExchangeID = pInstrument.ExchangeID,
                InstrumentID = pInstrument.InstrumentID,
                PriceTick = pInstrument.PriceTick,
                ProductClass = pInstrument.ProductClass == TThostFtdcProductClassType.THOST_FTDC_PC_Futures ? ProductClassType.Futures :
                       pInstrument.ProductClass == TThostFtdcProductClassType.THOST_FTDC_PC_Options ? ProductClassType.Options :
                       pInstrument.ProductClass == TThostFtdcProductClassType.THOST_FTDC_PC_Combination ? ProductClassType.Combination :
                       pInstrument.ProductClass == TThostFtdcProductClassType.THOST_FTDC_PC_SpotOption ? ProductClassType.SpotOption : ProductClassType.Futures,
                ProductID = pInstrument.ProductID,
                VolumeMultiple = pInstrument.VolumeMultiple,
                MaxOrderVolume = pInstrument.MaxLimitOrderVolume,
            };
            Exchange exc;
            if (Enum.TryParse(pInstrument.ExchangeID, out exc))
                field.ExchangeID = exc;
            DicInstrumentField.TryAdd(pInstrument.InstrumentID, field);
            if (bIsLast)
            {
                //查询流控
                _tIsLogin = new Thread(qryPosiAccount);
                _tIsLogin.Start();
                //Thread.Sleep(1100);
                //_t.ReqQryTradingAccount(_broker, _investor);
            }
        }

        private void CTPOnRspQryTradingAccount(ref CThostFtdcTradingAccountField pTradingAccount, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (!string.IsNullOrEmpty(pTradingAccount.AccountID))
            {
                TradingAccount.Available = pTradingAccount.Available;
                //this.TradingAccount.CashIn = pTradingAccount.CashIn; //资金查额
                TradingAccount.CloseProfit = pTradingAccount.CloseProfit;
                TradingAccount.Commission = pTradingAccount.Commission;
                TradingAccount.CurrMargin = pTradingAccount.CurrMargin;
                //this.TradingAccount.DeliveryMargin = pTradingAccount.DeliveryMargin;
                TradingAccount.FrozenCash = pTradingAccount.FrozenCash;
                TradingAccount.PositionProfit = pTradingAccount.PositionProfit;
                TradingAccount.PreBalance = pTradingAccount.PreBalance + pTradingAccount.Deposit - pTradingAccount.Withdraw;
                //this.TradingAccount.Reserve = pTradingAccount.Reserve;
                //this.TradingAccount.WithdrawQuota = pTradingAccount.WithdrawQuota;//可取
                TradingAccount.Fund = TradingAccount.PreBalance //静态权益									  
                    + pTradingAccount.CloseProfit + pTradingAccount.PositionProfit - pTradingAccount.Commission; //动态权益
                TradingAccount.Risk = TradingAccount.CurrMargin / TradingAccount.Fund;
            }
            if (bIsLast)
            {
                //首次查询后启动循环查询
                if (!IsLogin)
                {
                }
            }
        }

        private void CTPOnRspQryInvestorPosition(ref CThostFtdcInvestorPositionField pInvestorPosition, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (!string.IsNullOrEmpty(pInvestorPosition.InstrumentID))
            {
                // 排队交易所大额单边时所生成的非交易合约
                if (this.DicInstrumentField.ContainsKey(pInvestorPosition.InstrumentID))
                {
                    var f = pInvestorPosition;
                    _listPosi.Add(f);
                }
            }

            if (bIsLast)
            {
                foreach (var g in _listPosi.GroupBy(p => p.InstrumentID + "_" + p.PosiDirection))
                {
                    var id = g.First();
                    //整理持仓数据
                    HedgeType hedge = HedgeType.Speculation;
                    switch (id.HedgeFlag)
                    {
                        case TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation:
                            hedge = HedgeType.Speculation;
                            break;
                        case TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage:
                            hedge = HedgeType.Arbitrage;
                            break;
                        case TThostFtdcHedgeFlagType.THOST_FTDC_HF_Hedge:
                            hedge = HedgeType.Hedge;
                            break;
                    }

                    DirectionType dire = DirectionType.Buy;
                    if (g.First().PosiDirection == TThostFtdcPosiDirectionType.THOST_FTDC_PD_Short)
                        dire = DirectionType.Sell;
                    var key = id.InstrumentID + "_" + dire;
                    var pf = DicPositionField.GetOrAdd(key, new PositionField
                    {
                        InstrumentID = id.InstrumentID,
                        Direction = dire,
                        Hedge = hedge,
                    });

                    //if (pInvestorPosition.PositionDate == TThostFtdcPositionDateType.THOST_FTDC_PSD_Today)
                    //{
                    //	pf.TdPosition = pInvestorPosition.Position;
                    //	pf.TdCost = pf.TdPosition == 0 ? 0 : (pInvestorPosition.PositionCost  /*pInvestorPosition.TodayPosition * pf.TdPosition*/);
                    //}
                    //if (pInvestorPosition.PositionDate == TThostFtdcPositionDateType.THOST_FTDC_PSD_History)
                    //{
                    //	pf.YdPosition = pInvestorPosition.Position;
                    //	pf.YdCost = pInvestorPosition.PreSettlementPrice * pf.YdPosition * DicInstrumentField[pf.InstrumentID].VolumeMultiple;
                    //	//pf.YdCost = pInvestorPosition.PositionCost / pInvestorPosition.YdPosition * pf.YdPosition;
                    //}
                    pf.Position = g.Sum(n => n.Position);// pf.TdPosition + pf.YdPosition;
                    pf.TdPosition = g.Sum(n => n.TodayPosition);
                    pf.YdPosition = pf.Position - pf.TdPosition;// g.Sum(n => n.YdPosition);
                    // 交易合约可能不存在(如交易所合约的SP合约)
                    if (DicInstrumentField.ContainsKey(pf.InstrumentID))
                        pf.Price = pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
                    else
                        pf.Price = pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID.Split('&')[1]].VolumeMultiple / pf.Position);
                    pf.CloseProfit = g.Sum(n => n.CloseProfit);
                    pf.PositionProfit = g.Sum(n => n.PositionProfit);
                    pf.Commission = g.Sum(n => n.Commission);
                    pf.Margin = g.Sum(n => n.UseMargin);
                }

                TradingAccount.CloseProfit = _listPosi.Sum(n => n.CloseProfit);
                TradingAccount.PositionProfit = _listPosi.Sum(n => n.PositionProfit);
                TradingAccount.Commission = _listPosi.Sum(n => n.Commission);
                TradingAccount.Fund = TradingAccount.PreBalance + TradingAccount.CloseProfit + TradingAccount.PositionProfit - TradingAccount.Commission;

                TradingAccount.FrozenCash = _listPosi.Sum(n => n.FrozenCash);
                //由查帐户资金函数处理,原因:保证金有单边收的情况无法用持仓统计
                //TradingAccount.CurrMargin = _listPosi.Sum(n => n.UseMargin);
                //TradingAccount.Available = TradingAccount.Fund - TradingAccount.CurrMargin - TradingAccount.FrozenCash;
                //TradingAccount.Risk = TradingAccount.CurrMargin / TradingAccount.Fund;

                _listPosi.Clear();//清除,以便得到结果是重新添加
            }
        }

        void qryPosiAccount()
        {
            _rtnOrderTime = DateTime.Now;
            //当rtnorder数量过大时,需等待n秒响应时间.避免在旧的rtnorder未响应完成时进行接口操作导致未知错误.
            do
            {
                Thread.Sleep(1100);
            } while ((DateTime.Now - _rtnOrderTime).TotalSeconds <= 1);//  cnt < DicOrderField.Count); //等待rtn响应完成

            //20170113 _excTime = DateTime.MinValue;  //用于取交易所时间

            _t.ReqQryInvestorPosition();

            //权益查询:解决锁仓/套利只收单边保证金的问题
            Thread.Sleep(1100);
            if (IsLogin)
                _t.ReqQryTradingAccount();
            Thread.Sleep(1100);
            IsLogin = true;
            _OnRspUserLogin?.Invoke(this, new ErrorEventArgs { ErrorID = 0, ErrorMsg = "正确" });

            while (IsLogin)
            {
                _t.ReqQryInvestorPosition();

                //权益查询:解决锁仓/套利只收单边保证金的问题
                Thread.Sleep(1100);
                if (IsLogin)
                    _t.ReqQryTradingAccount();
                Thread.Sleep(1100);
            }

        }

        private void CTPOnRtnOrder(ref CThostFtdcOrderField pOrder)
        {
            TimeSpan ts;
            if (!IsLogin)
                _rtnOrderTime = DateTime.Now;   //登录前接收所有旧的 order

            if (string.IsNullOrEmpty(pOrder.InstrumentID)) return;

            string id = string.Format("{0}|{1}|{2}", pOrder.SessionID, pOrder.FrontID, pOrder.OrderRef);
            //_dicLocalidSfrId.TryAdd(pOrder.OrderLocalID, id);//防止因此项未赋值,导致成交响应里无法更新

            long tmp;
            if (DicOrderField.TryAdd(id, new OrderField
            {
                Custom = (int)(long.TryParse(pOrder.OrderRef, out tmp) ? tmp % 1000000 : 0),
                //修复: 值为null会导致界面显示错误
                InsertTime = string.IsNullOrEmpty(pOrder.InsertTime) ? DateTime.Now.ToString("HH:mm:ss") : pOrder.InsertTime,
                InstrumentID = pOrder.InstrumentID,
                //SysID = string.Empty,        //为null会导致界面显示错误
                //TradeTime = string.Empty,

                IsLocal = pOrder.SessionID == _session,
                LimitPrice = pOrder.LimitPrice,
                OrderID = id,
                Volume = pOrder.VolumeTotalOriginal,
                VolumeLeft = pOrder.VolumeTotalOriginal, // pOrder->VolumeTotal;
                                                         //f->VolumeLeft = pOrder->VolumeTotal; //由ontrade处理
                Status = OrderStatus.Normal,
                StatusMsg = pOrder.StatusMsg,
                Direction = pOrder.Direction == TThostFtdcDirectionType.THOST_FTDC_D_Buy ? DirectionType.Buy : DirectionType.Sell,
                Hedge = (TThostFtdcHedgeFlagType)pOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation ? HedgeType.Speculation : (TThostFtdcHedgeFlagType)pOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage ? HedgeType.Arbitrage : HedgeType.Hedge,
                Offset = (TThostFtdcOffsetFlagType)pOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open ? OffsetType.Open : (TThostFtdcOffsetFlagType)pOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday ? OffsetType.CloseToday : OffsetType.Close,
            })) //首次响应
            {
                //if (pOrder.OrderLocalID.Length > 0) //成交响应时用
                if (IsLogin)
                {
                    _OnRtnOrder?.Invoke(this, new OrderArgs { Value = DicOrderField[id] });
                }
            }
            else
            {
                OrderField f = DicOrderField[id];
                //修复: 值为null会导致界面显示错误
                f.InsertTime = string.IsNullOrEmpty(pOrder.InsertTime) ? DateTime.Now.ToString("HH:mm:ss") : pOrder.InsertTime;

                if (IsLogin && _excTime == DateTime.MinValue && TimeSpan.TryParse(f.InsertTime, out ts)) //首次的onrtnorder时间有问题,故放在此处更新_exctime
                {
                    _excTime = DateTime.Today.Add(ts);
                    _sw.Restart();
                }

                if (TThostFtdcOrderStatusType.THOST_FTDC_OST_Canceled == pOrder.OrderStatus)
                {
                    f.Status = OrderStatus.Canceled;
                    f.StatusMsg = pOrder.StatusMsg;
                    if (!string.IsNullOrEmpty(pOrder.CancelTime))
                        f.TradeTime = pOrder.CancelTime;
                    else if (IsLogin)//成撤时间:此处为撤单时间
                        f.TradeTime = DateTime.Now.ToString("HH:mm:ss");

                    if (IsLogin)
                    {
                        //委托被拒绝的撤单按错误处理
                        if (pOrder.StatusMsg.IndexOf(@"被拒绝") >= 0)
                        {
                            _OnRtnErrOrder?.Invoke(this, new ErrOrderArgs { ErrorID = -1, ErrorMsg = pOrder.StatusMsg, Value = f });
                        }
                        else
                            _OnRtnCancel?.Invoke(this, new OrderArgs { Value = f, });
                    }
                    //撤单次数等规则由业务层处理
                    //_dicCancelTimes.AddOrUpdate(f.InstrumentID, 1, (k, v) => v + 1);
                    //if (_dicCancelTimes[f.InstrumentID] >= 450 && _dicCancelTimes[f.InstrumentID] % 10 == 0)
                    //{
                    //	if (IsLogin && _caller._OnRtnErrCancel != null)
                    //		_caller._OnRtnErrOrder(_caller, new ErrOrderArgs
                    //		{
                    //			ErrorID = -1,
                    //			ErrorMsg = string.Format("撤单次数将要达到上限500次[{0}]", _dicCancelTimes[f.InstrumentID]),
                    //			Value = f,
                    //		});
                    //}
                }
            }

            //委托到交易所
            if (!string.IsNullOrEmpty(pOrder.OrderSysID))
            {
                DicOrderField[id].SysID = pOrder.OrderSysID;

                if (_dicSysidSfrId.TryAdd(pOrder.OrderSysID, id))
                {
                    List<CThostFtdcTradeField> list;
                    //成交先至,则在此处再调成交
                    if (_sysidTrade.TryGetValue(pOrder.OrderSysID, out list))
                    {
                        foreach (CThostFtdcTradeField t1 in list)
                        {
                            var t = t1;
                            //再调用rtntrade: 成交响应在rtntrade中完成
                            CTPOnRtnTrade(ref t);
                        }
                        list.Clear();
                    }
                }
            }
        }

        private void CTPOnRtnTrade(ref CThostFtdcTradeField pTrade)
        {
            if (!IsLogin)
                _rtnOrderTime = DateTime.Now;

            string id;
            OrderField of = null;
            if (!(_dicSysidSfrId.TryGetValue(pTrade.OrderSysID, out id) && DicOrderField.TryGetValue(id, out of)))
            {
                CThostFtdcTradeField fReTrade = pTrade;
                var list = _sysidTrade.GetOrAdd(pTrade.OrderSysID, new List<CThostFtdcTradeField>());
                list.Add(fReTrade);
                return;
            }

            TradeField f = new TradeField
            {
                Hedge = pTrade.HedgeFlag == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation ? HedgeType.Speculation
                    : pTrade.HedgeFlag == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage ? HedgeType.Arbitrage : HedgeType.Hedge,
                Direction = pTrade.Direction == TThostFtdcDirectionType.THOST_FTDC_D_Buy ? DirectionType.Buy : DirectionType.Sell,

                //ExchangeID = pTrade.ExchangeID,
                InstrumentID = pTrade.InstrumentID,
                Offset = pTrade.OffsetFlag == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open ? OffsetType.Open
                    : pTrade.OffsetFlag == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday ? OffsetType.CloseToday : OffsetType.Close,
                Price = pTrade.Price,
                TradeID = pTrade.TradeID + (char)pTrade.Direction,
                TradeTime = pTrade.TradeTime,
                TradingDay = pTrade.TradingDay,
                Volume = pTrade.Volume,
                SysID = pTrade.OrderSysID,
            };
            Exchange exc;
            if (Enum.TryParse(pTrade.ExchangeID, out exc))
                f.ExchangeID = exc;
            // if (DicTradeField.TryAdd(f.TradeID, f))
            if (DicTradeField.TryAdd(string.Format("{0}_{1}", f.TradeID, f.Direction == DirectionType.Buy ? 0 : 1), f))
            {
                f.OrderID = id; //更新成交对应的委托ID
                of.TradeTime = pTrade.TradeTime;
                of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + pTrade.Price * pTrade.Volume) / (of.Volume - of.VolumeLeft + pTrade.Volume);
                of.TradeVolume = pTrade.Volume;
                of.VolumeLeft -= of.TradeVolume;
                if (of.VolumeLeft == 0)
                {
                    of.Status = OrderStatus.Filled;
                    of.StatusMsg = "全部成交";
                }
                else
                {
                    of.Status = OrderStatus.Partial;
                    of.StatusMsg = "部分成交";
                }

                if (IsLogin)
                {
                    #region 更新持仓
                    PositionField pf;
                    //处理持仓
                    if (f.Offset == OffsetType.Open)
                    {
                        pf = DicPositionField.GetOrAdd(f.InstrumentID + "_" + f.Direction, new PositionField());
                        pf.InstrumentID = f.InstrumentID;
                        pf.Direction = f.Direction;
                        pf.Hedge = f.Hedge;
                        pf.Price = (pf.Price * pf.Position + f.Price * f.Volume) / (pf.Position + f.Volume);
                        pf.TdPosition += f.Volume;
                        pf.Position += f.Volume;
                    }
                    else
                    {
                        pf = this.DicPositionField.GetOrAdd(f.InstrumentID + "_" + (f.Direction == DirectionType.Buy ? "Sell" : "Buy"), new PositionField());
                        if (f.Offset == OffsetType.CloseToday)
                        {
                            pf.TdPosition -= f.Volume;
                        }
                        else
                        {
                            int tdClose = Math.Min(pf.TdPosition, f.Volume);
                            if (pf.TdPosition > 0)
                                pf.TdPosition -= tdClose;
                            pf.YdPosition -= Math.Max(0, f.Volume - tdClose);
                        }
                        pf.Position -= f.Volume;
                    }
                    #endregion

                    //委托响应
                    _OnRtnOrder?.Invoke(this, new OrderArgs { Value = of });
                    //成交响应
                    _OnRtnTrade?.Invoke(this, new TradeArgs { Value = f });
                }
            }
        }

        /// <summary>
        /// 处理错单: CTP平台返回
        /// </summary>
        /// <param name="pInputOrder"></param>
        /// <param name="pRspInfo"></param>
        /// <param name="nRequestID"></param>
        /// <param name="bIsLast"></param>
        private void CTPOnRspOrderInsert(ref CThostFtdcInputOrderField pInputOrder, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            //ref重复::重发
            //if (pRspInfo.ErrorID == 22)
            //{
            //	if (!IsLogin) return;

            //	CThostFtdcInputOrderField f = pInputOrder;
            //	//Thread.Sleep(50);
            //	f.OrderRef = string.Format("{0:000000}{1}", ++_req, f.OrderRef.Length >= 6 ? f.OrderRef.Substring(f.OrderRef.Length - 6) : (new string('0', 6 - f.OrderRef.Length) + f.OrderRef));
            //	_t.ReqOrderInsert()
            //	this._import.ReqCommand(EnumReq.ReqOrderInsert, f);
            //}
            //else
            {
                string id = string.Format("{0}|{1}|{2}", _session, _front, pInputOrder.OrderRef);

                int tmp;
                if (DicOrderField.TryAdd(id, new OrderField
                {
                    Custom = int.TryParse(pInputOrder.OrderRef, out tmp) ? tmp % 1000000 : 0,// pOrder.OrderRef.Length <= 6 ? string.Empty : pOrder.OrderRef.Substring(pOrder.OrderRef.Length - 6),
                                                                                             //InsertTime = DicOrderField.Max(n => n.Value.InsertTime) ?? DateTime.Now.ToString("HH:mm:ss"),
                    InstrumentID = pInputOrder.InstrumentID,
                    InsertTime = DateTime.Now.ToString("HH:mm:ss"), //为null会导致界面显示错误
                                                                    //SysID = string.Empty,        //为null会导致界面显示错误
                    TradeTime = string.Empty,
                    IsLocal = true,
                    LimitPrice = pInputOrder.LimitPrice,
                    OrderID = id,
                    Volume = pInputOrder.VolumeTotalOriginal,
                    VolumeLeft = pInputOrder.VolumeTotalOriginal, // pOrder->VolumeTotal;
                                                                  //f->VolumeLeft = pOrder->VolumeTotal; //由ontrade处理
                                                                  //Status = OrderStatus.Normal,
                                                                  //Status = OrderStatus.Canceled,
                    Status = OrderStatus.Error,
                    StatusMsg = pRspInfo.ErrorID + "|" + pRspInfo.ErrorMsg,
                    Direction = pInputOrder.Direction == TThostFtdcDirectionType.THOST_FTDC_D_Buy ? DirectionType.Buy : DirectionType.Sell,
                    Hedge = (TThostFtdcHedgeFlagType)pInputOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation ? HedgeType.Speculation :
                        (TThostFtdcHedgeFlagType)pInputOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage ? HedgeType.Arbitrage : HedgeType.Hedge,
                    Offset = (TThostFtdcOffsetFlagType)pInputOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open ? OffsetType.Open :
                        (TThostFtdcOffsetFlagType)pInputOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday ? OffsetType.CloseToday : OffsetType.Close,
                }))
                {
                    string it = DicOrderField.Max(n => n.Value.InsertTime);
                    if (string.IsNullOrEmpty(it))
                        it = DateTime.Now.ToString("HH:mm:ss");
                    else
                        it = TimeSpan.Parse(it).Add(TimeSpan.FromMilliseconds(1)).ToString(@"hh\:mm\:ss"); //加1秒
                    DicOrderField[id].InsertTime = it;
                    if (IsLogin)
                    {
                        _OnRtnErrOrder?.Invoke(this, new ErrOrderArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg, Value = DicOrderField[id] });
                    }
                }
            }
        }

        /// <summary>
        /// 处理错单: 交易所返回
        /// </summary>
        /// <param name="pInputOrder"></param>
        /// <param name="pRspInfo"></param>
        private void CTPOnErrRtnOrderInsert(ref CThostFtdcInputOrderField pInputOrder, ref CThostFtdcRspInfoField pRspInfo)
        {
            string id = string.Format("{0}|{1}|{2}", _session, _front, pInputOrder.OrderRef);
            OrderField of = new OrderField();
            if (IsLogin)// && DicOrderField.TryGetValue(id, out of))// && of.Status != OrderStatus.Canceled && of.IsLocal)
            {
                var pOrder = pInputOrder;
                int tmp;
                of = new OrderField
                {
                    Custom = int.TryParse(pOrder.OrderRef, out tmp) ? tmp % 1000000 : 0,
                    InstrumentID = pOrder.InstrumentID,
                    InsertTime = DateTime.Now.ToString("HH:mm:ss"), //为null会导致界面显示错误
                                                                    //SysID = string.Empty,        //为null会导致界面显示错误
                    TradeTime = string.Empty,
                    IsLocal = true,
                    LimitPrice = pOrder.LimitPrice,
                    OrderID = id,
                    Volume = pOrder.VolumeTotalOriginal,
                    VolumeLeft = pOrder.VolumeTotalOriginal, // pOrder->VolumeTotal;
                                                             //f->VolumeLeft = pOrder->VolumeTotal; //由ontrade处理
                                                             //Status = OrderStatus.Normal,
                                                             //Status = OrderStatus.Canceled,
                    Status = OrderStatus.Error,
                    StatusMsg = pRspInfo.ErrorID + "|" + pRspInfo.ErrorMsg,
                    Direction = pOrder.Direction == TThostFtdcDirectionType.THOST_FTDC_D_Buy ? DirectionType.Buy : DirectionType.Sell,
                    Hedge = (TThostFtdcHedgeFlagType)pOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation ? HedgeType.Speculation :
                        (TThostFtdcHedgeFlagType)pOrder.CombHedgeFlag[0] == TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage ? HedgeType.Arbitrage : HedgeType.Hedge,
                    Offset = (TThostFtdcOffsetFlagType)pOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open ? OffsetType.Open :
                        (TThostFtdcOffsetFlagType)pOrder.CombOffsetFlag[0] == TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday ? OffsetType.CloseToday : OffsetType.Close,
                };
                of.Status = OrderStatus.Error;
                of.StatusMsg = string.Format("[RtnErrorID:{0}]{1}", pRspInfo.ErrorID, pRspInfo.ErrorMsg);

                _OnRtnErrOrder?.Invoke(this, new ErrOrderArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg, Value = of });
            }
        }

        private void CTPOnRspOrderAction(ref CThostFtdcInputOrderActionField pInputOrderAction, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (pRspInfo.ErrorID == 0) return;

            string id = string.Format("{0}|{1}|{2}", pInputOrderAction.SessionID, pInputOrderAction.FrontID, pInputOrderAction.OrderRef);
            OrderField of;
            if (IsLogin && DicOrderField.TryGetValue(id, out of))
            {
                _OnRtnErrCancel?.Invoke(this, new ErrOrderArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg, Value = of });
            }
        }

        private void CTPOnErrRtnOrderAction(ref CThostFtdcOrderActionField pOrderAction, ref CThostFtdcRspInfoField pRspInfo)
        {
            if (pRspInfo.ErrorID == 0) return;

            string id = string.Format("{0}|{1}|{2}", pOrderAction.SessionID, pOrderAction.FrontID, pOrderAction.OrderRef);
            OrderField of;
            if (IsLogin && DicOrderField.TryGetValue(id, out of))
            {
                _OnRtnErrCancel?.Invoke(this, new ErrOrderArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg, Value = of });
            }
        }

        private void CTPOnRspUserPasswordUpdate(ref CThostFtdcUserPasswordUpdateField pUserPasswordUpdate, ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (IsLogin)
            {
                _OnRtnPasswordUpdate?.Invoke(this, new ErrorEventArgs { ErrorID = pRspInfo.ErrorID, ErrorMsg = pRspInfo.ErrorMsg });
            }
        }

        private void CTPOnRspError(ref CThostFtdcRspInfoField pRspInfo, int nRequestID, bool bIsLast)
        {
            if (IsLogin)
                _OnRtnError?.Invoke(this, new ErrorEventArgs
                {
                    ErrorID = pRspInfo.ErrorID,
                    ErrorMsg = string.Format("OnRspError:[ErrorID:{0}][ErrorMsg:{1}]", pRspInfo.ErrorID, pRspInfo.ErrorMsg),
                });
        }

        private void CTPOnRtnTradingNotice(ref CThostFtdcTradingNoticeInfoField pTradingNoticeInfo)
        {
            _OnRtnNotice?.Invoke(this, new StringEventArgs { Value = pTradingNoticeInfo.SendTime + ":\r\n" + pTradingNoticeInfo.FieldContent });
        }

        public override bool IsLogin { get; protected set; }

        public override string TradingDay { get; protected set; }

        public override TimeSpan GetExchangeTime()
        {
            return _excTime == DateTime.MinValue ? DateTime.Now.TimeOfDay : _excTime.Add(_sw.Elapsed).TimeOfDay;
        }

        public override ExchangeStatusType GetInstrumentStatus(string pExc)
        {
            var instField = DicInstrumentField[pExc];
            ExchangeStatusType excStatus = default(ExchangeStatusType);
            if (DicExcStatus.TryGetValue(instField.ProductID, out excStatus) || DicExcStatus.TryGetValue(instField.ExchangeID.ToString(), out excStatus) || DicExcStatus.TryGetValue(instField.InstrumentID, out excStatus))
                return excStatus;
            return ExchangeStatusType.Closed;
        }


        /// <summary>
        /// 采用restart模式
        /// </summary>
        /// <returns></returns>
        public override int ReqConnect()
        {
            _t.RegisterFront(this.FrontAddr);
            _t.SubscribePrivateTopic(THOST_TE_RESUME_TYPE.THOST_TERT_RESTART);
            _t.SubscribePublicTopic(THOST_TE_RESUME_TYPE.THOST_TERT_RESTART);
            return (int)_t.Init();
        }

        public override int ReqUserLogin()
        {
            return (int)_t.ReqAuthenticate(this.Broker, this.Investor, this.ProductInfo, this.AuthCode, this.AppID);
        }

        public override void ReqUserLogout()
        {
            this.IsLogin = false;
            //上面的disconnect注销掉,需要主动调用此回调函数
            _OnRspUserLogout?.Invoke(this, new IntEventArgs { Value = 0 });
            //取消连接响应,避免重连后的再登录.（release中已处理）
            //_t.SetOnFrontDisconnected(null);
            //_t.SetOnFrontConnected(null);
            _t.Release();
        }

        public override int ReqOrderAction(string pOrderId)
        {
            OrderField of;
            if (!DicOrderField.TryGetValue(pOrderId, out of))
            {
                _OnRtnError?.Invoke(this, new ErrorEventArgs
                {
                    ErrorID = -1,
                    ErrorMsg = string.Format("OrderActionError:[OrderID:{0}][ErrorMsg:no orderid.]", pOrderId),
                });
                return -1;
            }

            return (int)_t.ReqOrderAction(this.Broker, this.Investor, InstrumentID: of.InstrumentID,
                OrderRef: pOrderId.Split('|')[2],
                FrontID: int.Parse(pOrderId.Split('|')[1]),
                SessionID: int.Parse(pOrderId.Split('|')[0]),
                ActionFlag: TThostFtdcActionFlagType.THOST_FTDC_AF_Delete);
        }

        public override int ReqOrderInsert(string pInstrument, DirectionType pDirection, OffsetType pOffset, double pPrice, int pVolume, int pCustom, OrderType pType = OrderType.Limit, HedgeType pHedge = HedgeType.Speculation)
        {
            //限价
            var OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice;
            var TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_GFD;
            var VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_AV;
            if (pType == OrderType.Market) //市价
            {
                OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_AnyPrice;
                TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC;
                //max = instField.MaxMarketOrderVolume;
                pPrice = 0;
            }
            else if (pType == OrderType.FAK) //FAK
            {
                OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice;
                TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC;
            }
            else if (pType == OrderType.FOK) //FOK
            {
                OrderPriceType = TThostFtdcOrderPriceTypeType.THOST_FTDC_OPT_LimitPrice;
                TimeCondition = TThostFtdcTimeConditionType.THOST_FTDC_TC_IOC;
                VolumeCondition = TThostFtdcVolumeConditionType.THOST_FTDC_VC_CV; //全部数量
            }

            return (int)_t.ReqOrderInsert(this.Broker, this.Investor, InstrumentID: pInstrument,
                OrderRef: string.Format("{0:000000}{1:000000}", _ref++, pCustom % 1000000),
                CombHedgeFlag: new string((char)(pHedge == HedgeType.Speculation ? TThostFtdcHedgeFlagType.THOST_FTDC_HF_Speculation : pHedge == HedgeType.Arbitrage ? TThostFtdcHedgeFlagType.THOST_FTDC_HF_Arbitrage : TThostFtdcHedgeFlagType.THOST_FTDC_HF_Hedge), 1),
                CombOffsetFlag: new String((char)(pOffset == OffsetType.Open ? TThostFtdcOffsetFlagType.THOST_FTDC_OF_Open : pOffset == OffsetType.Close ? TThostFtdcOffsetFlagType.THOST_FTDC_OF_Close : TThostFtdcOffsetFlagType.THOST_FTDC_OF_CloseToday), 1),
                ExchangeID: this.DicInstrumentField[pInstrument].ExchangeID.ToString(),
                Direction: pDirection == DirectionType.Buy ? TThostFtdcDirectionType.THOST_FTDC_D_Buy : TThostFtdcDirectionType.THOST_FTDC_D_Sell,
                VolumeTotalOriginal: pVolume,
                ForceCloseReason: TThostFtdcForceCloseReasonType.THOST_FTDC_FCC_NotForceClose,
                ContingentCondition: TThostFtdcContingentConditionType.THOST_FTDC_CC_Immediately,
                VolumeCondition: VolumeCondition,
                LimitPrice: pPrice,
                IsSwapOrder: 0,
                MinVolume: 1,
                UserForceClose: 0,
                TimeCondition: TimeCondition,
                OrderPriceType: OrderPriceType);
        }

        public override int ReqUserPasswordUpdate(string pOldPassword, string pNewPassword)
        {
            return (int)_t.ReqUserPasswordUpdate(this.Broker, this.Investor, pOldPassword, pNewPassword);
        }
    }
}
