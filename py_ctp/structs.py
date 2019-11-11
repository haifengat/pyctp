#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/21'
"""

from .enums import DirectType, OffsetType, OrderStatus, HedgeType, TradeTypeType


class InfoField:
    """返回信息"""

    def __init__(self):
        """Constructor"""
        '''错误号'''
        self.ErrorID = 0
        '''错误号'''
        '''错误描述'''
        self.ErrorMsg = '正确'
        '''错误描述'''

    def __str__(self):
        # return 'ErrorID:{0}, ErrorMsg:{1}'.format(self.ErrorID, self.ErrorMsg)
        return '{{"ErrorID":{self.ErrorID}, "ErrorMsg":"{self.ErrorMsg}"}}'.format(
            self=self)

    @property
    def __dict__(self):
        return {'ErrorID': self.ErrorID, 'ErrorMsg': str(self.ErrorMsg, 'GB2312')}


class OrderField:
    """报单响应"""

    def __init__(self):
        """initionalize"""
        '''委托标识'''
        self.OrderID = ""
        '''委托标识'''
        '''合约'''
        self.InstrumentID = ""
        '''合约'''
        '''交易所'''
        self.ExchangeID = ""
        '''交易所'''
        '''买卖'''
        self.Direction = DirectType.Buy
        '''买卖'''
        '''开平'''
        self.Offset = OffsetType.Open
        '''开平'''
        '''限价单价格'''
        self.LimitPrice = 0.0
        '''限价单价格'''
        '''报单均价'''
        self.AvgPrice = 0.0
        '''报单均价'''
        '''委托时间'''
        self.InsertTime = ""
        '''委托时间'''
        '''成交时间'''
        self.TradeTime = ""
        '''成交时间'''
        '''成交数量(本次)'''
        self.TradeVolume = 0
        '''成交数量(本次)'''
        '''委托数量'''
        self.Volume = 0
        '''委托数量'''
        '''未成交数量'''
        self.VolumeLeft = 0
        '''未成交数量'''
        '''委托状态'''
        self.Status = OrderStatus.Normal
        '''委托状态'''
        '''状态描述'''
        self.StatusMsg = ""
        '''状态描述'''
        '''是否本地委托'''
        self.IsLocal = False
        '''是否本地委托'''
        '''委托自定义标识'''
        self.Custom = 0
        '''委托自定义标识'''
        '''系统(交易所)ID'''
        self.SysID = ""
        '''系统(交易所)ID'''

    def __str__(self):
        """"""
        return '{self.OrderID}, {self.InstrumentID}, {self.ExchangeID}, {self.Direction}, {self.Offset}, {self.LimitPrice}, {self.AvgPrice}, {self.InsertTime}, {self.TradeTime}, {self.TradeVolume}, {self.Volume}, {self.VolumeLeft}, {self.Status}, {self.StatusMsg}, {self.IsLocal}, {self.Custom}, {self.SysID}'.format(
            self=self)

    @property
    def __dict__(self):  # 如何控制dict的字段次序?:交由客户端处理
        return {
            'OrderID': self.OrderID,
            'InstrumentID': self.InstrumentID,
            'ExchangeID': self.ExchangeID,
            'Direction': self.Direction.name,
            'Offset': self.Offset.name,
            'LimitPrice': self.LimitPrice,
            'AvgPrice': self.AvgPrice,
            'InsertTime': self.InsertTime,
            'TradeTime': self.TradeTime,
            'TradeVolume': self.TradeVolume,
            'Volume': self.Volume,
            'VolumeLeft': self.VolumeLeft,
            'Status': self.Status.name,
            'StatusMsg': self.StatusMsg,
            'IsLocal': self.IsLocal,
            'Custom': self.Custom,
            'SysID': self.SysID
        }


class TradeField:
    """成交响应"""

    def __init__(self):
        """Constructor"""
        '''成交标识'''
        self.TradeID = ''
        '''成交标识'''
        '''合约'''
        self.InstrumentID = ''
        '''合约'''
        '''交易所'''
        self.ExchangeID = ''
        '''交易所'''
        '''买卖'''
        self.Direction = DirectType.Buy
        '''买卖'''
        '''开平'''
        self.Offset = OffsetType.Open
        '''开平'''
        '''成交价'''
        self.Price = 0.0
        '''成交价'''
        '''成交数量'''
        self.Volume = 0
        '''成交数量'''
        '''成交时间'''
        self.TradeTime = ''
        '''成交时间'''
        '''交易日'''
        self.TradingDay = ''
        '''交易日'''
        ''''对应的委托标识'''
        self.OrderID = ''
        ''''对应的委托标识'''
        '''对应的系统(交易所)ID'''
        self.SysID = ''
        '''对应的系统(交易所)ID'''

    def __str__(self):
        """"""
        return '{self.TradeID}, {self.InstrumentID}, {self.ExchangeID}, {self.Direction}, {self.Offset}, {self.Price}, {self.Volume}, {self.TradeTime}, {self.TradingDay}, {self.OrderID}, {self.SysID}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'TradeID': self.TradeID,
            'InstrumentID': self.InstrumentID,
            'ExchangeID': self.ExchangeID,
            'Direction': self.Direction.name,
            'Offset': self.Offset.name,
            'Price': self.Price,
            'Volume': self.Volume,
            'TradeTime': self.TradeTime,
            'TradingDay': self.TradingDay,
            'OrderID': self.OrderID,
            'SysID': self.SysID
        }


class InstrumentField:
    """合约"""

    def __init__(self):
        """Constructor"""
        '''合约'''
        self.InstrumentID = ''
        '''合约'''
        '''名称'''
        self.InstrumentName = ''
        '''名称'''
        '''品种'''
        self.ProductID = ''
        '''品种'''
        '''交易所'''
        self.ExchangeID = ''
        '''交易所'''
        '''合约乘数'''
        self.VolumeMultiple = ''
        '''合约乘数'''
        '''每跳价格变动'''
        self.PriceTick = 0.0
        '''每跳价格变动'''
        '''最大单笔下单量'''
        self.MaxOrderVolume = 9999
        '''最大单笔下单量'''
        '''类型 Futures/Options/Combination/Spot/EFP/SpotOption'''
        self.ProductType = 'Future'
        '''类型 Futures/Options/Combination/Spot/EFP/SpotOption'''

    def __str__(self):
        """"""
        return '{self.InstrumentID}, {self.ProductID}, {self.ExchangeID}, {self.VolumeMultiple}, {self.PriceTick}, {self.MaxOrderVolume}, {self.ProductType}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'InstrumentID': self.InstrumentID,
            'ProductID': self.ProductID,
            'ExchangeID': self.ExchangeID,
            'VolumeMultiple': self.VolumeMultiple,
            'PriceTick': self.PriceTick,
            'MaxOrderVolume': self.MaxOrderVolume,
            'ProductType': self.ProductType
        }


class TradingAccount:
    """交易帐户"""

    def __init__(self):
        """Constructor"""
        '''昨日结算'''
        self.PreBalance = 0.0
        '''昨日结算'''
        '''持仓盈亏'''
        self.PositionProfit = 0.0
        '''持仓盈亏'''
        '''平仓盈亏'''
        self.CloseProfit = 0.0
        '''平仓盈亏'''
        '''手续费'''
        self.Commission = 0.0
        '''手续费'''
        '''保证金'''
        self.CurrMargin = 0.0
        '''保证金'''
        '''冻结'''
        self.FrozenCash = 0.0
        '''冻结'''
        '''可用'''
        self.Available = 0.0
        '''可用'''
        '''动态权益'''
        self.Fund = 0.0
        '''动态权益'''
        '''风险度'''
        self.Risk = 0.0
        '''风险度'''

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return '{self.PreBalance}, {self.PositionProfit}, {self.CloseProfit}, {self.Commission}, {self.CurrMargin}, {self.FrozenCash}, {self.Available}, {self.Fund}, {self.Risk}'.format(
            self=self)

    @property
    def __dict__(self):
        return {
            'PreBalance': self.PreBalance,
            'PositionProfit': self.PositionProfit,
            'CloseProfit': self.CloseProfit,
            'Commission': self.Commission,
            'CurrMargin': self.CurrMargin,
            'FrozenCash': self.FrozenCash,
            'Available': self.Available,
            'Fund': self.Fund,
            'Risk': self.Risk
        }


########################################################################
class PositionField:
    """持仓"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        '''合约'''
        self.InstrumentID = ''
        '''合约'''
        self.Direction = DirectType.Buy
        '''多空'''
        '''持仓价格'''
        self.Price = 0.0
        '''持仓价格'''
        '''持仓量'''
        self.Position = 0
        '''持仓量'''
        '''昨持仓'''
        self.YdPosition = 0
        '''昨持仓'''
        '''今持仓'''
        self.TdPosition = 0
        '''今持仓'''
        '''平仓盈亏'''
        self.CloseProfit = 0.0
        '''平仓盈亏'''
        '''持仓盈亏'''
        self.PositionProfit = 0.0
        '''持仓盈亏'''
        '''手续费'''
        self.Commission = 0.0
        '''手续费'''
        '''保证金'''
        self.Margin = 0.0
        '''保证金'''

    # ----------------------------------------------------------------------
    def __str__(self):
        """"""
        return (
            '{self.InstrumentID}, {self.Direction}, {self.Price}, {self.Position}, {self.TdPosition}, {self.YdPosition}, {self.CloseProfit}, {self.PositionProfit}, {self.Commission}, {self.Margin}'
        ).format(self=self)

    @property
    def __dict__(self):
        return {
            'InstrumentID': self.InstrumentID,
            'Direction': self.Direction.name,
            'Price': self.Price,
            'Position': self.Position,
            'TdPosition': self.TdPosition,
            'YdPosition': self.YdPosition,
            'CloseProfit': self.CloseProfit,
            'PositionProfit': self.PositionProfit,
            'Commission': self.Commission,
            'Margin': self.Margin
        }


class PositionDetail:
    """持仓明细"""

    def __init__(self):
        """"""
        self.Instrument = ''
        """合约"""
        self.HedgeFlag = HedgeType.Speculation
        """投保"""
        self.Direction = DirectType.Buy
        """持仓方向"""
        self.TradeID = ''
        """交易ID"""
        self.Volume = 0
        """持仓量"""
        self.OpenPrice = .0
        """平仓价格"""
        self.OpenDate = ''
        """开仓日期"""
        self.TradeType = TradeTypeType.Common
        """交易类型"""
        self.PositionProfit = .0
        """盯市持仓盈亏"""
        self.CloseProfit = .0
        """盯市平仓盈亏"""


class Tick:
    """分笔数据"""

    def __init__(self):
        """初始化"""
        '''合约'''
        self.Instrument = ''
        '''合约'''
        '''最新价'''
        self.LastPrice = 0.0
        '''最新价'''
        '''挂卖价'''
        self.AskPrice = 0.0
        '''挂卖价'''
        '''挂买价'''
        self.BidPrice = 0.0
        '''挂买价'''
        '''挂卖量'''
        self.AskVolume = 1
        '''挂卖量'''
        '''挂买量'''
        self.BidVolume = 1
        '''挂买量'''
        '''时间'''
        self.UpdateTime = ''
        '''时间'''
        '''毫秒'''
        self.UpdateMillisec = 0
        '''毫秒'''
        '''成交量'''
        self.Volume = 1
        '''成交量'''
        '''持仓量'''
        self.OpenInterest = 1.0
        '''持仓量'''
        '''均价'''
        self.AveragePrice = 0.0
        '''均价'''
        '''涨板价'''
        self.UpperLimitPrice = 0.0
        '''涨板价'''
        '''跌板价'''
        self.LowerLimitPrice = 0.0
        '''跌板价'''
        '''昨结算价'''
        self.PreOpenInterest = 0.0

    def __str__(self):
        """"""
        return '{self.Instrument}, {self.LastPrice}, {self.AskPrice}, {self.AskVolume}, {self.BidPrice}, {self.BidVolume}, {self.UpdateTime}, {self.Volume}, {self.OpenInterest}, {self.AveragePrice}, {self.UpperLimitPrice}, {self.LowerLimitPrice}, {self.PreOpenInterest}'.format(self=self)

    # @property
    # def __dict__(self):
    #     return {
    #         'Instrument': self.Instrument,
    #         'LastPrice': self.LastPrice,
    #         'AskPrice': self.AskPrice,
    #         'AskVolume': self.AskVolume,
    #         'BidPrice': self.BidPrice,
    #         'BidVolume': self.BidVolume,
    #         'UpdateTime': self.UpdateTime,
    #         'Volume': self.Volume,
    #         'OpenInterest': self.OpenInterest,
    #         'AveragePrice': self.AveragePrice
    #     }
