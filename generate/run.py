#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/1/17'
"""

import os

# 切换到 generate 目录下
os.chdir('./generate')
dir = '../ctp_20180109'

from generate_enum_py import Generate as e_py
e_py(dir).run()
print('e_py')

from generate_struct_py import Generate as s_py
s_py(dir).run()
print('s_py')

from generate_c import Generate as g_c
g_c(dir, 'trade').run()
g_c(dir, 'quote').run()
print('g_c')

from generate_py import Generate as g_py
g_py(dir, 'trade').run()
g_py(dir, 'quote').run()
print('g_py')

from generate_enum_cs import Generate as e_cs
e_cs(dir).run()
print('e_cs')

from generate_struct_cs import Generate as s_cs
s_cs(dir).run()
print('s_cs')

from generate_cs import Generate as g_cs
g_cs(dir, 'trade').run()
g_cs(dir, 'quote').run()
print('g_cs')
