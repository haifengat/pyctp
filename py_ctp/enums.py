#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/10/30'
"""

from enum import Enum


class TradeTypeType(Enum):
    """成交类型类型"""
    SplitCombinatio = 110
    """组合持仓拆分为单一持仓,初始化不应包含该类型的持仓"""
    Common = 48
    """普通成交"""
    OptionsExecution = 49
    """期权执行"""
    OTC = 50
    """OTC成交"""
    EFPDerived = 51
    """期转现衍生成交"""
    CombinationDerived = 52
    """组合衍生成交"""


class HedgeType(Enum):
    """投保"""
    Speculation = 0
    '''投机'''
    Arbitrage = 1
    '''套利'''
    Hedge = 2
    '''套保'''
    MarketMaker = 3
    '''做市商'''

    def __int__(self):
        """Enum"""
        return self.value


class DirectType(Enum):
    """买卖"""
    Buy = 0
    '''买'''
    Sell = 1
    '''卖'''

    def __int__(self):
        return self.value


class OffsetType(Enum):
    """开平(今)"""
    Open = 0
    '''开仓'''
    Close = 1
    '''平仓'''
    CloseToday = 2
    '''平今
    上期所独有'''

    def __int__(self):
        return self.value


class OrderType(Enum):
    """委托类型"""
    Limit = 0
    '''限价单'''
    Market = 1
    '''市价单'''
    FAK = 2
    '''部成立撤'''
    FOK = 3
    '''全成立撤'''

    def __int__(self):
        return self.value


class OrderStatus(Enum):
    """委托状态"""
    Normal = 0
    '''正常'''
    Partial = 1
    '''部分成交'''
    Filled = 2
    '''全部成交'''
    Canceled = 3
    '''撤单'''
    Error = 4
    '''错单'''

    def __int__(self):
        return self.value


class InstrumentStatus(Enum):
    """交易状态"""
    Continous = 0
    '''交易'''
    Auction = 1
    '''竞价'''
    NoTrading = 2
    '''非交易'''
    Closed = 3
    '''收盘'''

    def __int__(self):
        return self.value
