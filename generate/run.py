#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/1/17'
"""

import os

# 切换到 generate 目录下
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# src_dir = '../ctp_20180109_x86'
src_dir = '../ctp_20190220_se_x64'   # 看穿式监管
data_type_file_name = 'ThostFtdcUserApiDataType'

import g_enum
g_enum.src_dir = src_dir
g_enum.data_type_file_name = 'ThostFtdcUserApiDataType'
g_enum.run()

import g_struct
g_struct.src_dir = src_dir
g_struct.struct_file_name = 'ThostFtdcUserApiStruct'
g_struct.run()

import g_c_py
g_c_py.src_dir = src_dir
g_c_py.spi_class_name = 'trade'
g_c_py.file_src = 'ThostFtdcTraderApi'
# g_c_py.lib_name = 'thosttraderapi'
g_c_py.lib_name = 'thosttraderapi_se'   # 看穿式监管
g_c_py.api_class_name = 'CThostFtdcTraderApi'
g_c_py.info_struct_name = 'CThostFtdcRspInfoField'
g_c_py.create_api = 'CThostFtdcTraderApi::CreateFtdcTraderApi'
g_c_py.run(True, True) # 生成c+  py
# g_c_py.run(False, True)
g_c_py.spi_class_name = 'quote'
g_c_py.file_src = 'ThostFtdcMdApi'
# g_c_py.lib_name = 'thostmduserapi'
g_c_py.lib_name = 'thostmduserapi_se'   # 看穿式监管
g_c_py.api_class_name = 'CThostFtdcMdApi'
g_c_py.info_struct_name = 'CThostFtdcRspInfoField'
g_c_py.create_api = 'CThostFtdcMdApi::CreateFtdcMdApi'
g_c_py.run(True, True)
# g_c_py.run(False, True)

# 手动修改
# ctp_trade.cs
#
#         [UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
#         public delegate IntPtr DeleGetSystemInfo();
#         [UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
#         public delegate IntPtr DeleGetVersion();
#         public string GetVersion()
#         {
#             return Marshal.PtrToStringAnsi((Invoke(_handle, "GetVersion", typeof(DeleGetVersion)) as DeleGetVersion)());
#         }
#         public IntPtr GetSystemInfo()
#         {
#             return (Invoke(_handle, "GetSystemInfo", typeof(DeleGetSystemInfo)) as DeleGetSystemInfo)();
#         }
#
# trade.h
#
# #include "../ctp_20190220_se_x64/DataCollect.h"
# #pragma comment(lib, "../ctp_20190220_se_x64/WinDataCollect.lib")
#
#
# trade.cpp
#
# ///获取AES加密和RSA加密的终端信息
# ///@pSystemInfo 出参 空间需要调用者自己分配 至少270个字节
# ///@nLen 出参 获取到的采集信息的长度
# ///采集信息内可能含有‘\0’ 建议调用者使用内存复制
# DLL_EXPORT_C_DECL int WINAPI GetSystemInfo()
# {
# 	char pinfo[344];
# 	int nLen;
# 	return CTP_GetSystemInfo(pinfo, nLen);
# }
#
# DLL_EXPORT_C_DECL void* WINAPI GetVersion() { return (void *)CThostFtdcTraderApi::GetApiVersion(); }
