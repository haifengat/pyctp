#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/22'
"""

import threading
import itertools
import time
import os
import platform

from .enums import OrderType, InstrumentStatus
from .structs import DirectType, InfoField, InstrumentField, OffsetType, OrderField, OrderStatus, PositionField, TradeField, TradingAccount
from .ctp_trade import Trade
from .ctp_struct import CThostFtdcInputOrderActionField, CThostFtdcInputOrderField, CThostFtdcInstrumentField, CThostFtdcInstrumentStatusField, CThostFtdcInvestorPositionField, CThostFtdcOrderField, CThostFtdcRspInfoField, CThostFtdcRspUserLoginField, CThostFtdcSettlementInfoConfirmField, CThostFtdcTradingAccountField
from .ctp_enum import ActionFlagType, ContingentConditionType, DirectionType, OffsetFlagType, ForceCloseReasonType, HedgeFlagType, OrderPriceTypeType, PosiDirectionType, TimeConditionType, VolumeConditionType, OrderStatusType, InstrumentStatusType


class CtpTrade():
    """"""

    def __init__(self):
        self.front_address = ''
        self.investor = ''
        self.password = ''
        self.broker = ''
        self.logined = False
        self.tradingday = ''

        self.instruments = {}
        self.orders = {}
        self.trades = {}
        self.account: TradingAccount = None
        self.positions = {}
        self.instrument_status = {}

        self._req = 0
        self._session = ''
        self._orderid_sysid = {}
        self._posi = []

        self.t = Trade(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib', 'ctp_trade.' + ('dll' if 'Windows' in platform.system() else 'so')))

    def _OnFrontConnected(self):
        threading.Thread(target=self.OnConnected, args=(self,)).start()

    def _OnFrontDisconnected(self, nReason):
        self.logined = False
        print(nReason)
        # 下午收盘后会不停断开再连接 4097错误
        if nReason == 4097 or nReason == 4098:
            threading.Thread(target=self._reconnect).start()
        else:
            threading.Thread(target=self.OnDisConnected, args=(self, nReason)).start()

    def _reconnect(self):
        if sum([1 if stat == 'Continous' else 0 for exc, stat in self.instrument_status.items()]) == 0:
            print(time.strftime('%Y%m%d %H:%M:%S', time.localtime()))
            self.t.Release()
            time.sleep(600)
            self.ReqConnect(self.front_address)

    # def _OnRspUserLogout(self, pUserLogout: CThostFtdcUserLogoutField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
    #     pass

    def _OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField(), pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if pRspInfo.getErrorID() == 0:
            self.session = pRspUserLogin.getSessionID()
            self.tradingday = pRspUserLogin.getTradingDay()
            self.t.ReqSettlementInfoConfirm(self.broker, self.investor)
        elif self.logined:
            threading.Thread(target=self._relogin).start()
        else:
            info = InfoField()
            info.ErrorID = pRspInfo.getErrorID()
            info.ErrorMsg = pRspInfo.getErrorMsg()
            threading.Thread(target=self.OnUserLogin, args=(self, info)).start()

    def _relogin(self):
        # 隔夜重连=>处理'初始化'错误
        time.sleep(60 * 10)
        self.t.ReqUserLogin(
            BrokerID=self.broker,
            UserID=self.investor,
            Password=self.password,
            UserProductInfo='@haifeng')

    def _OnRspSettlementInfoConfirm(
            self,
            pSettlementInfoConfirm: CThostFtdcSettlementInfoConfirmField,
            pRspInfo: CThostFtdcRspInfoField,
            nRequestID: int,
            bIsLast: bool):
        if not self.logined:
            time.sleep(0.5)
            """查询合约/持仓/权益"""
            threading.Thread(target=self._qry).start()  # 开启查询

    def _qry(self):
        """查询帐号相关信息"""
        # restart 模式, 待rtnorder 处理完毕后再进行查询,否则会造成position混乱
        ord_cnt = 0
        trd_cnt = 0
        while True:
            time.sleep(0.5)
            if len(self.orders) == ord_cnt and len(self.trades) == trd_cnt:
                break
            ord_cnt = len(self.orders)
            trd_cnt = len(self.trades)
        self.t.ReqQryInstrument()
        time.sleep(1.1)
        self.t.ReqQryInvestorPosition(self.broker, self.investor)
        time.sleep(1.1)
        self.t.ReqQryTradingAccount(self.broker, self.investor)
        time.sleep(1.1)

        self.logined = True
        info = InfoField()
        info.ErrorID = 0
        info.ErrorMsg = '正确'
        threading.Thread(target=self.OnUserLogin, args=(self, info)).start()
        # 调用Release后程序异常退出,但不报错误:接口断开了仍然调用了查询指令
        while self.logined:
            """查询持仓与权益"""
            self.t.ReqQryInvestorPosition(self.broker, self.investor)
            time.sleep(1.1)
            if not self.logined:
                return
            self.t.ReqQryTradingAccount(self.broker, self.investor)
            time.sleep(1.1)

    def _OnRtnInstrumentStatus(self, pInstrumentStatus: CThostFtdcInstrumentStatusField):
        if pInstrumentStatus.getInstrumentID() == '':
            return
        status = InstrumentStatus.Continous
        if pInstrumentStatus.getInstrumentStatus() == InstrumentStatusType.Continous:
            status = InstrumentStatus.Continous
        elif pInstrumentStatus.getInstrumentStatus() == InstrumentStatusType.Closed:
            status = InstrumentStatus.Closed
        elif str(pInstrumentStatus.getInstrumentStatus()).startswith('Auction'):
            status = InstrumentStatus.Auction
        else:
            status = InstrumentStatus.NoTrading
        self.instrument_status[pInstrumentStatus.getInstrumentID()] = status
        self.OnInstrumentStatus(self, pInstrumentStatus.getInstrumentID(), status)

    def _OnRspQryInstrument(self, pInstrument: CThostFtdcInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        inst = InstrumentField()
        inst.InstrumentID = pInstrument.getInstrumentID()
        inst.ProductID = pInstrument.getProductID()
        inst.ExchangeID = pInstrument.getExchangeID()
        inst.VolumeMultiple = pInstrument.getVolumeMultiple()
        inst.PriceTick = pInstrument.getPriceTick()
        inst.MaxOrderVolume = pInstrument.getMaxLimitOrderVolume()
        inst.ProductType = pInstrument.getProductClass().name  # ProductClassType.Futures -> Futures
        self.instruments[inst.InstrumentID] = inst

    def _OnRspQryPosition(self, pInvestorPosition: CThostFtdcInvestorPositionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if pInvestorPosition.getInstrumentID() != '':  # 偶尔出现NULL的数据导致数据转换错误
            self._posi.append(pInvestorPosition)  # Struct(**f.__dict__)) #dict -> object

        if bIsLast:
            # 先排序再group才有效
            self._posi = sorted(self._posi, key=lambda c: '{0}_{1}'.format(c.getInstrumentID(), DirectType.Buy if c.getPosiDirection() == PosiDirectionType.Long else DirectType.Sell))
            # direction需从posidiction转换为dictiontype
            for key, group in itertools.groupby(self._posi, lambda c: '{0}_{1}'.format(c.getInstrumentID(), 'Buy' if c.getPosiDirection() == PosiDirectionType.Long else 'Sell')):
                pf = self.positions.get(key)
                if not pf:
                    pf = PositionField()
                    self.positions[key] = pf
                pf.Position = 0
                pf.TdPosition = 0
                pf.YdPosition = 0
                pf.CloseProfit = 0
                pf.PositionProfit = 0
                pf.Commission = 0
                pf.Margin = 0
                pf.Price = 0
                cost = 0.0
                for g in group:
                    if not pf.InstrumentID:
                        pf.InstrumentID = g.getInstrumentID()
                        pf.Direction = DirectType.Buy if g.getPosiDirection() == PosiDirectionType.Long else DirectType.Sell
                    pf.Position += g.getPosition()
                    pf.TdPosition += g.getTodayPosition()
                    pf.YdPosition = pf.Position - pf.TdPosition
                    pf.CloseProfit += g.getCloseProfit()
                    pf.PositionProfit += g.getPositionProfit()
                    pf.Commission += g.getCommission()
                    pf.Margin += g.getUseMargin()
                    cost += g.OpenCost
                # pf.Position <= 0 ? 0 : (g.Sum(n => n.PositionCost) / DicInstrumentField[pf.InstrumentID].VolumeMultiple / pf.Position);
                vm = self.instruments[pf.InstrumentID].VolumeMultiple
                pf.Price = 0 if pf.Position <= 0 else cost / vm / pf.Position
            self._posi.clear()

    def _OnRspQryAccount(self, pTradingAccount: CThostFtdcTradingAccountField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        if not self.account:
            self.account = TradingAccount()
        self.account.Available = pTradingAccount.getAvailable()
        self.account.CloseProfit = pTradingAccount.getCloseProfit()
        self.account.Commission = pTradingAccount.getCommission()
        self.account.CurrMargin = pTradingAccount.getCurrMargin()
        self.account.FrozenCash = pTradingAccount.getFrozenCash()
        self.account.PositionProfit = pTradingAccount.getPositionProfit()
        self.account.PreBalance = pTradingAccount.getPreBalance() + pTradingAccount.getDeposit() + pTradingAccount.getWithdraw()
        self.account.Fund = self.account.PreBalance + pTradingAccount.getCloseProfit() + pTradingAccount.getPositionProfit() - pTradingAccount.getCommission()
        self.account.Risk = 0 if self.account.Fund == 0 else self.account.CurrMargin / self.account.Fund

    def _OnRtnOrder(self, pOrder: CThostFtdcOrderField):
        """"""
        id = '{0}|{1}|{2}'.format(pOrder.getSessionID(), pOrder.getFrontID(), pOrder.getOrderRef())
        of = self.orders.get(id)
        if not of:
            of = OrderField()
            if pOrder.getOrderRef().isdigit():
                of.Custom = int(pOrder.getOrderRef()) % 1000000
            of.InstrumentID = pOrder.getInstrumentID()
            of.InsertTime = pOrder.getInsertTime()
            of.Direction = DirectType.Buy if DirectionType(
                pOrder.getDirection()
            ) == DirectionType.Buy else DirectType.Sell
            ot = OffsetFlagType(ord(pOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == OffsetFlagType.Open else (
                OffsetType.CloseToday
                if ot == OffsetFlagType.CloseToday else OffsetType.Close)
            of.Status = OrderStatus.Normal
            of.StatusMsg = pOrder.getStatusMsg()
            of.IsLocal = pOrder.getSessionID() == self.session
            of.LimitPrice = pOrder.getLimitPrice()
            of.OrderID = id
            of.Volume = pOrder.getVolumeTotalOriginal()
            of.VolumeLeft = of.Volume
            self.orders[id] = of
            threading.Thread(target=self.OnOrder, args=(self, of)).start()
        elif pOrder.getOrderStatus() == OrderStatusType.Canceled:
            of.Status = OrderStatus.Canceled
            of.StatusMsg = pOrder.getStatusMsg()

            if of.StatusMsg.find('被拒绝') >= 0:
                info = InfoField()
                info.ErrorID = -1
                info.ErrorMsg = of.StatusMsg
                threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()
            else:
                threading.Thread(target=self.OnCancel, args=(self, of)).start()
        else:
            if pOrder.getOrderSysID():
                of.SysID = pOrder.getOrderSysID()
                self._orderid_sysid[pOrder.getOrderSysID()] = id  # 记录sysid与orderid关联,方便Trade时查找处理

    def _OnRtnTrade(self, f):
        """"""
        tf = TradeField()
        tf.Direction = DirectType.Buy if f.getDirection() == DirectionType.Buy else DirectType.Sell
        tf.ExchangeID = f.getExchangeID()
        tf.InstrumentID = f.getInstrumentID()
        tf.Offset = OffsetType.Open if f.getOffsetFlag() == OffsetFlagType.Open else OffsetType.Close if f.getOffsetFlag(
        ) == OffsetFlagType.Close else OffsetType.CloseToday
        tf.Price = f.getPrice()
        tf.SysID = f.getOrderSysID()
        tf.TradeID = f.getTradeID()
        tf.TradeTime = f.getTradeTime()
        tf.TradingDay = f.getTradingDay()
        tf.Volume = f.getVolume()

        self.trades[tf.TradeID] = tf

        id = self._orderid_sysid[tf.SysID]
        of = self.orders[id]
        tf.OrderID = id  # tradeid 与 orderid 关联
        of.TradeTime = tf.TradeTime
        of.AvgPrice = (of.AvgPrice * (of.Volume - of.VolumeLeft) + tf.Price *
                       tf.Volume) / (of.Volume - of.VolumeLeft + tf.Volume)
        of.TradeVolume = tf.Volume
        of.VolumeLeft -= tf.Volume
        if of.VolumeLeft == 0:
            of.Status = OrderStatus.Filled
            of.StatusMsg = '全部成交'
        else:
            of.Status = OrderStatus.Partial
            of.StatusMsg = '部分成交'
        # 更新持仓 *****
        if tf.Offset == OffsetType.Open:
            key = '{0}_{1}'.format(tf.InstrumentID, 'Buy' if tf.Direction == DirectType.Buy else 'Sell')
            pf = self.positions.get(key)
            if not pf:
                pf = PositionField()
                self.positions[key] = pf
            pf.InstrumentID = tf.InstrumentID
            pf.Direction = tf.Direction
            pf.Price = (pf.Price * pf.Position + tf.Price * tf.Volume) / (pf.Position + tf.Volume)
            pf.TdPosition += tf.Volume
            pf.Position += tf.Volume
        else:
            key = '{0}_{1}'.format(tf.InstrumentID, DirectType.Sell if tf.Direction == DirectType.Buy else DirectType.Buy)
            pf = self.positions.get(key)
            if pf:  # 有可能出现无持仓的情况
                if tf.Offset == OffsetType.CloseToday:
                    pf.TdPosition -= tf.Volume
                else:
                    tdclose = min(pf.TdPosition, tf.Volume)
                    if pf.TdPosition > 0:
                        pf.TdPosition -= tdclose
                    pf.YdPosition -= max(0, tf.Volume - tdclose)
                pf.Position -= tf.Volume
        threading.Thread(target=self._onRtn, args=(of, tf)).start()

    def _onRtn(self, of, tf):
        self.OnOrder(self, of)
        self.OnTrade(self, tf)

    def _OnRspOrder(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        id = '{0}|{1}|{2}'.format(self.session, '0', pInputOrder.getOrderRef())
        of = self.orders.get(id)
        if not of:
            of = OrderField()
            l = int(pInputOrder.getOrderRef())
            of.Custom = l % 1000000
            of.InstrumentID = pInputOrder.getInstrumentID()
            of.InsertTime = time.strftime('%H:%M:%S', time.localtime())
            # 对direction需特别处理（具体见ctp_struct）
            of.Direction = DirectType.Buy if DirectionType(pInputOrder.getDirection()) == DirectionType.Buy else DirectType.Sell
            ot = OffsetFlagType(ord(pInputOrder.getCombOffsetFlag()[0]))
            of.Offset = OffsetType.Open if ot == OffsetFlagType.Open else (OffsetType.CloseToday if ot == OffsetFlagType.CloseToday else OffsetType.Close)
            # of.Status = OrderStatus.Normal
            # of.StatusMsg = f.getStatusMsg()
            of.IsLocal = True
            of.LimitPrice = pInputOrder.getLimitPrice()
            of.OrderID = id
            of.Volume = pInputOrder.getVolumeTotalOriginal()
            of.VolumeLeft = of.Volume
            self.orders[id] = of

        of.Status = OrderStatus.Error
        of.StatusMsg = '{0}:{1}'.format(info.ErrorID, info.ErrorMsg)
        threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()

    def _OnErrOrder(self, pInputOrder: CThostFtdcInputOrderField, pRspInfo: CThostFtdcRspInfoField):
        """"""
        id = '{0}|{1}|{2}'.format(self.session, '0', pInputOrder.getOrderRef())
        of = self.orders.get(id)

        info = InfoField()
        info.ErrorID = pRspInfo.getErrorID()
        info.ErrorMsg = pRspInfo.getErrorMsg()

        if of and of.IsLocal:
            of.Status = OrderStatus.Error
            of.StatusMsg = '{0}:{1}'.format(pRspInfo.getErrorID(), pRspInfo.getErrorMsg())
            threading.Thread(target=self.OnErrOrder, args=(self, of, info)).start()

    def _OnRspOrderAction(self, pInputOrderAction: CThostFtdcInputOrderActionField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        id = "{0}|{1}|{2}".format(pInputOrderAction.getSessionID(), pInputOrderAction.getFrontID(), pInputOrderAction.getOrderRef())
        if self.logined and id in self.orders:
            info = InfoField()
            info.ErrorID = pRspInfo.ErrorID
            info.ErrorMsg = pRspInfo.ErrorMsg
            threading.Thread(target=self.OnErrCancel, args=(self, self.orders[id], info)).start()

    def ReqConnect(self, front: str):
        """
        连接交易前置
            :param self:
            :param front:str:
        """
        self.t.CreateApi()
        spi = self.t.CreateSpi()
        self.t.RegisterSpi(spi)

        self.t.OnFrontConnected = self._OnFrontConnected
        self.t.OnRspUserLogin = self._OnRspUserLogin
        self.t.OnFrontDisconnected = self._OnFrontDisconnected
        # self.t.OnRspUserLogout = self._OnRspUserLogout
        self.t.OnRspSettlementInfoConfirm = self._OnRspSettlementInfoConfirm
        self.t.OnRtnOrder = self._OnRtnOrder
        self.t.OnRtnTrade = self._OnRtnTrade
        self.t.OnRspOrderInsert = self._OnRspOrder
        self.t.OnErrRtnOrderInsert = self._OnErrOrder
        self.t.OnRspOrderAction = self._OnRspOrderAction
        self.t.OnRtnInstrumentStatus = self._OnRtnInstrumentStatus
        self.t.OnRspQryInstrument = self._OnRspQryInstrument
        self.t.OnRspQryTradingAccount = self._OnRspQryAccount
        self.t.OnRspQryInvestorPosition = self._OnRspQryPosition

        self.front_address = front
        self.t.RegCB()
        self.t.RegisterFront(front)
        self.t.SubscribePrivateTopic(0)  # restart 同步处理order trade
        self.t.SubscribePublicTopic(0)
        self.t.Init()
        # self.t.Join()

    def ReqUserLogin(self, user: str, pwd: str, broker: str):
        """
        登录
            :param self:
            :param user:str:
            :param pwd:str:
            :param broker:str:
        """
        self.broker = broker
        self.investor = user
        self.password = pwd
        self.t.ReqUserLogin(BrokerID=broker, UserID=user, Password=pwd)

    def ReqOrderInsert(self, pInstrument: str, pDirection: DirectType, pOffset: OffsetType, pPrice: float = 0.0, pVolume: int = 1, pType: OrderType = OrderType.Limit, pCustom: int = 0):
        """
        委托
            :param self:
            :param pInstrument:str:
            :param pDirection:DirectType:
            :param pOffset:OffsetType:
            :param pPrice:float=0.0:
            :param pVolume:int=1:
            :param pType:OrderType=OrderType.Limit:
        """
        OrderPriceType = OrderPriceTypeType.AnyPrice
        TimeCondition = TimeConditionType.IOC
        LimitPrice = 0.0
        VolumeCondition = VolumeConditionType.AV

        if pType == OrderType.Market:  # 市价
            OrderPriceType = OrderPriceTypeType.AnyPrice
            TimeCondition = TimeConditionType.IOC
            LimitPrice = 0.0
            VolumeCondition = VolumeConditionType.AV
        elif pType == OrderType.Limit:  # 限价
            OrderPriceType = OrderPriceTypeType.LimitPrice
            TimeCondition = TimeConditionType.GFD
            LimitPrice = pPrice
            VolumeCondition = VolumeConditionType.AV
        elif pType == OrderType.FAK:  # FAK
            OrderPriceType = OrderPriceTypeType.LimitPrice
            TimeCondition = TimeConditionType.IOC
            LimitPrice = pPrice
            VolumeCondition = VolumeConditionType.AV
        elif pType == OrderType.FOK:  # FOK
            OrderPriceType = OrderPriceTypeType.LimitPrice
            TimeCondition = TimeConditionType.IOC
            LimitPrice = pPrice
            VolumeCondition = VolumeConditionType.CV  # 全部数量

        self._req += 1
        self.t.ReqOrderInsert(
            BrokerID=self.broker,
            InvestorID=self.investor,
            InstrumentID=pInstrument,
            OrderRef="%06d%06d" % (self._req, pCustom % 1000000),
            UserID=self.investor,
            # 此处ctp_enum与at_struct名称冲突
            Direction=DirectionType.Buy
            if pDirection == DirectType.Buy else DirectionType.Sell,
            CombOffsetFlag=chr(OffsetFlagType.Open if pOffset == OffsetType.Open else (OffsetFlagType.CloseToday if pOffset == OffsetType.CloseToday else OffsetFlagType.Close)),
            CombHedgeFlag=HedgeFlagType.Speculation.__char__(),
            IsAutoSuspend=0,
            ForceCloseReason=ForceCloseReasonType.NotForceClose,
            IsSwapOrder=0,
            ContingentCondition=ContingentConditionType.Immediately,
            VolumeCondition=VolumeCondition,
            MinVolume=1,
            VolumeTotalOriginal=pVolume,
            OrderPriceType=OrderPriceType,
            TimeCondition=TimeCondition,
            LimitPrice=LimitPrice,
        )

    def ReqOrderAction(self, OrderID: str):
        """
        撤单
            :param self:
            :param OrderID:str:
        """
        of = self.orders[OrderID]

        if not of:
            return -1
        else:
            pOrderId = of.OrderID
            return self.t.ReqOrderAction(
                self.broker,
                self.investor,
                OrderRef=pOrderId.split('|')[2],
                FrontID=int(pOrderId.split('|')[1]),
                SessionID=int(pOrderId.split('|')[0]),
                InstrumentID=of.InstrumentID,
                ActionFlag=ActionFlagType.Delete)

    def ReqUserLogout(self):
        """
        退出接口
            :param self:
        """
        self.logined = False
        time.sleep(3)
        self.t.ReqUserLogout(BrokerID=self.broker, UserID=self.investor)
        self.t.RegisterSpi(None)
        self.t.Release()
        threading.Thread(target=self.OnDisConnected, args=(self, 0)).start()

    def OnConnected(self, obj):
        """
        接口连接
            :param self:
            :param obj:
        """
        print('=== OnConnected ==='.format(''))

    def OnDisConnected(self, obj, reason: int):
        """
        接口断开
            :param self:
            :param obj:
            :param reason:int:
        """
        print('=== OnDisConnected === \n{0}'.format(reason))

    def OnUserLogin(self, obj, info: InfoField):
        """
        登录响应
            :param self:
            :param obj:
            :param info:InfoField:
        """
        print('=== OnUserLogin === \n{0}'.format(info))

    def OnOrder(self, obj, f: OrderField):
        """
        委托响应
            :param self:
            :param obj:
            :param f:OrderField:
        """
        print('=== OnOrder === \n{0}'.format(f.__dict__))

    def OnTrade(self, obj, f: TradeField):
        """
        成交响应
            :param self:
            :param obj:
            :param f:TradeField:
        """
        print('=== OnTrade === \n{0}'.format(f.__dict__))

    def OnCancel(self, obj, f: OrderField):
        """
        撤单响应
            :param self:
            :param obj:
            :param f:OrderField:
        """
        print('=== OnCancel === \n{0}'.format(f.__dict__))

    def OnErrCancel(self, obj, f: OrderField, info: InfoField):
        """
        撤单失败
            :param self:
            :param obj:
            :param f:OrderField:
            :param info:InfoField:
        """
        print('=== OnErrCancel ===\n{0}'.format(f.__dict__))
        print(info)

    def OnErrOrder(self, obj, f: OrderField, info: InfoField):
        """
        委托错误
            :param self:
            :param obj:
            :param f:OrderField:
            :param info:InfoField:
        """
        print('=== OnErrOrder ===\n{0}'.format(f.__dict__))
        print(info)

    def OnInstrumentStatus(self, obj, inst: str, status: InstrumentStatus):
        """
        交易状态
            :param self:
            :param obj:
            :param inst:str:
            :param status:InstrumentStatus:
        """
        print('{}:{}'.format(inst, str(status).strip().split('.')[1]))
