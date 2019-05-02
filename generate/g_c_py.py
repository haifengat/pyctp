#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/8
# @desc    : generate cpp and h
""" 32位与64位区别
#ifdef WIN32
#define WINAPI      __cdecl
#else
#define WINAPI      __stdcall
#endif
"""

import os
import re

cur_dir = os.path.dirname(os.path.abspath(__file__))
type_dict = {'int': 'c_int32', 'char': 'c_char', 'double': 'c_double', 'short': 'c_short', 'string': 'c_char_p', 'bool': 'c_bool'}
src_dir = ''
'''接口文档目录'''
file_src = ''
'''api头文件'''
lib_name = ''

spi_class_name = 'trade'
'''生成trade/quote小写'''
api_class_name = ''

info_struct_name = ''
'''api类名'''
create_api = ''
'''生成api的命令'''


def run(generate_c: bool, generate_py: bool, generate_cs: bool = True):
    f_src = open(os.path.join(cur_dir, src_dir, f'{file_src}.h'), 'r', encoding='gbk')

    if generate_c:
        f_c_h = open(os.path.join(cur_dir, '..', 'ctp_c', f'{spi_class_name}.h'), 'w', encoding='utf-8')
        f_c_cpp = open(os.path.join(cur_dir, '..', 'ctp_c', f'{spi_class_name}.cpp'), 'w', encoding='utf-8')
        # f_c_def = open(os.path.join(cur_dir, '..', 'ctp_c', 'function.def'), 'w', encoding='utf-8')
    if generate_py:
        f_py = open(os.path.join(cur_dir, '..', 'py_ctp', f'ctp_{spi_class_name}.py'), 'w', encoding='utf-8')
    if generate_cs:
        f_cs = open(os.path.join(cur_dir, '..', 'cs_ctp', 'proxy', f'ctp_{spi_class_name}.cs'), 'w', encoding='utf-8')

    lines = f_src.read()
    lines = re.sub(r'\n\s*([iC])', '\g<1>', lines)  # 多行参数变为一行
    lines = lines.split('\n')
    no = -1
    lines_on = []  # 响应函数
    cpp_set = []  # set
    cpp_null = []  # 声明为NULL
    cpp_req = []  # Req函数
    def_req = []  # define使用的函数名
    def_on = []  # define

    py_req_type_def = []  # req声明
    py_req_def_body = []  # req函数定义
    py_on_def__ = []  # 生成def __Onxxx
    py_on_def = []  # 生成def Onxxx
    py_on_reg = []

    cs_req_type_def = []  # req声明
    cs_req_def_body = []  # req函数定义
    cs_on_set = []  # 生成def Onxxx
    cs_on_dele = []

    import sys
    import inspect
    sys.path.append('..')
    ctp_struct = getattr(__import__('py_ctp.ctp_struct'), 'ctp_struct')

    for line in lines:
        no += 1
        g = re.search(r'class\s*(\w*Spi)', line)
        if g is not None:
            spi_parent = g.group(1)
            if generate_c:
                f_c_h.write(f'''#pragma once
#ifdef _WINDOWS  //64位系统没有预定义 WIN32
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT_DECL __declspec(dllexport)
#endif
#else
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C"
#else
#define DLL_EXPORT_DECL extern
#endif
#endif

#ifdef _WINDOWS
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WINAPI      __cdecl
#include "{src_dir}/{file_src}.h"
#pragma comment(lib, "{src_dir}/{lib_name}.lib")
#include "{src_dir}/DataCollect.h"
#pragma comment(lib, "{src_dir}/WinDataCollect.lib")
#else
#define WINAPI      __stdcall
#include "{src_dir}/{file_src}.h"
#pragma comment(lib, "{src_dir}/{lib_name}.lib")
#include "{src_dir}/DataCollect.h"
#pragma comment(lib, "{src_dir}/WinDataCollect.lib")
#endif
#else
#define WINAPI
#include "{src_dir}/{file_src}.h"
#include "{src_dir}/DataCollect.h"
#endif

#include <string.h>

class {spi_class_name.title()}: {spi_parent}
{{
public:
    {spi_class_name.title()}(void);
    //针对收到空反馈的处理
    {info_struct_name} rif;
    {info_struct_name}* repare({info_struct_name} *pRspInfo)
    {{
        if (pRspInfo == NULL)
        {{
            memset(&rif, 0, sizeof(rif));
            return &rif;
        }}
        else
            return pRspInfo;
    }}\n\n''')
                f_c_cpp.write(f'''#include "{spi_class_name.title()}.h"
#include <string.h>
int nReq;

{spi_class_name.title()}::{spi_class_name.title()}(void)
{{	
''')
            if generate_py:
                f_py.write(f'''#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/10


import os
import sys
import platform
import ctypes
import copy
from .ctp_struct import *


class {spi_class_name.title()}:

    def __init__(self):

        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"lib{{'64' if sys.maxsize > 2**32 else '32'}}")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_{spi_class_name}.' + ('dll' if 'Windows' in platform.system() else 'so'))
        if not os.path.exists(absolute_dllfile_path):
            print('缺少DLL接口文件')
            return

        # make log dir for api log
        logdir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(logdir):
            os.mkdir(logdir)

        dlldir = os.path.split(absolute_dllfile_path)[0]
        # change work directory
        cur_path = os.getcwd()
        os.chdir(dlldir)

        self.h = CDLL(absolute_dllfile_path)

        self.h.CreateApi.argtypes = []
        self.h.CreateApi.restype = c_void_p

        self.h.CreateSpi.argtypes = []
        self.h.CreateSpi.restype = c_void_p

        self.api = None
        self.spi = None
        self.nRequestID = 0''')

            if generate_cs:
                f_cs.write(f'''using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;

namespace HaiFeng
{{
	public class ctp_{spi_class_name}
	{{
		#region Dll Load /UnLoad
		/// <summary>
		/// 原型是 :HMODULE LoadLibrary(LPCTSTR lpFileName);
		/// </summary>
		/// <param name="lpFileName"> DLL 文件名 </param>
		/// <returns> 函数库模块的句柄 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr LoadLibrary(string lpFileName);

		/// <summary>
		/// 原型是 : FARPROC GetProcAddress(HMODULE hModule, LPCWSTR lpProcName);
		/// </summary>
		/// <param name="hModule"> 包含需调用函数的函数库模块的句柄 </param>
		/// <param name="lpProcName"> 调用函数的名称 </param>
		/// <returns> 函数指针 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);

		/// <summary>
		/// 原型是 : BOOL FreeLibrary(HMODULE hModule);
		/// </summary>
		/// <param name="hModule"> 需释放的函数库模块的句柄 </param>
		/// <returns> 是否已释放指定的 Dll </returns>
		[DllImport("kernel32", EntryPoint = "FreeLibrary", SetLastError = true)]
		private static extern bool FreeLibrary(IntPtr hModule);

		/// <summary>
		///
		/// </summary>
		/// <param name="pHModule"></param>
		/// <param name="lpProcName"></param>
		/// <param name="t"></param>
		/// <returns></returns>
		/// <exception cref="Exception"></exception>
		private static Delegate Invoke(IntPtr pHModule, string lpProcName, Type t)
		{{
			// 若函数库模块的句柄为空，则抛出异常
			if (pHModule == IntPtr.Zero)
			{{
				throw (new Exception(" 函数库模块的句柄为空 , 请确保已进行 LoadDll 操作 !"));
			}}
			// 取得函数指针
			IntPtr farProc = GetProcAddress(pHModule, lpProcName);
			// 若函数指针，则抛出异常
			if (farProc == IntPtr.Zero)
			{{
				throw (new Exception(" 没有找到 :" + lpProcName + " 这个函数的入口点 "));
			}}
			return Marshal.GetDelegateForFunctionPointer(farProc, t);
		}}
		#endregion

		IntPtr _handle = IntPtr.Zero, _api = IntPtr.Zero, _spi = IntPtr.Zero;
		private int nRequestID = 0;
		delegate IntPtr Create();
		
		public ctp_{spi_class_name}()
		{{
			string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(this.GetType().Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            dll_path = Path.Combine(dll_path, "lib" + (Environment.Is64BitProcess ? "64" : "32"));
            if (!Directory.Exists(dll_path))
            {{
                File.WriteAllBytes("lib.zip", Properties.Resources.lib);
                ZipFile.ExtractToDirectory("lib.zip", ".");
                File.Delete("lib.zip");
            }}
			Environment.CurrentDirectory = dll_path;
			_handle = LoadLibrary(Path.Combine(dll_path, "ctp_{spi_class_name}.dll"));
			if (_handle == IntPtr.Zero)
			{{
				throw (new Exception(String.Format("没有找到:", dll_path)));
			}}
			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");

			_api = (Invoke(_handle, "CreateApi", typeof(Create)) as Create)();
			_spi = (Invoke(_handle, "CreateSpi", typeof(Create)) as Create)();
			this.RegisterSpi(_spi);
		}}
''')
                if spi_class_name.lower().endswith('trade'):
                    f_cs.write('''
        #region SE版本增加
        [UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
        public delegate IntPtr DeleGetVersion();
        public string GetVersion()
        {
            return Marshal.PtrToStringAnsi((Invoke(_handle, "GetVersion", typeof(DeleGetVersion)) as DeleGetVersion)());
        }
        #endregion\n''')
        else:
            g_on = re.search(r'virtual void\s*On(\w+)[(](.*)[)]', line)  # virtual void RegisterFront(char *pszFrontAddress) = 0;
            if g_on is not None:
                # 写入注释
                lines_comment = []
                for i in range(no, 0, -1):
                    g_comment = re.search(r'///(.*)$', lines[i - 1])
                    if g_comment is None:
                        break
                    lines_comment.insert(0, '\t' + g_comment.group())
                lines_comment = '\n\t'.join(lines_comment)
                lines_on.append(lines_comment)
                on_name = g_on.group(1)

                cpp_null.append(f'\t_{on_name} = NULL;')  # _FrontConnected = NULL;
                # DLL_EXPORT_C_DECL void WINAPI SetOnFrontConnected(Trade* spi, void* func){spi->_FrontConnected = func;}
                cpp_set.append(f'DLL_EXPORT_C_DECL void WINAPI SetOn{on_name}({spi_class_name.title()}* spi, void* func){{spi->_{on_name} = func;}}')
                def_on.append(f'SetOn{on_name}')

                on_param = '' if len(g_on.regs) == 2 else g_on.group(2)
                on_param_name = ''
                params_0 = []  # 首个参数
                params_name = []
                params_type = []
                if on_param != '':
                    params = re.findall(r'(\w+\s+[*]*)\s*(\w+)', on_param)
                    for p in params:
                        params_name.append(p[1])
                        params_type.append(p[0].strip())
                    on_param_name = ', '.join(params_name)
                    on_param_name = on_param_name.replace('pRspInfo', 'repare(pRspInfo)')
                    if '*' in params[0][0]:
                        params_0 = params[0]
                lines_on.append(f"\ttypedef int (WINAPI *{on_name})({on_param});")  # typedef int (WINAPI *FrontConnected)();
                lines_on.append(f'\tvoid *_{on_name};')  # void *_FrontConnected;
                if len(params_0) == 0:  # 首个参数不为struct
                    # if (_RtnTradeParam) ((RtnTradeParam)_RtnTradeParam)(pTradeParam);
                    lines_on.append(f'\tvirtual void On{on_name}({on_param}){{if (_{on_name}) (({on_name})_{on_name})({on_param_name});}}\n')
                else:  # 返回的Struct为NULL的处理
                    lines_on.append(f'''\tvirtual void On{on_name}({on_param})
    {{
        if (_{on_name})
        {{
            if ({params_0[1]})
                (({on_name})_{on_name})({on_param_name});
            else
            {{
                {params_0[0].replace('*','').strip()} f = {{}};
                (({on_name})_{on_name})({on_param_name.replace(params_0[1], '&f')});
            }}
        }}
    }}\n''')

                # py
                py_params_type = ''
                py_params_name = []
                py_params_def = []  # xxx:int=''
                for i, t in enumerate(params_type):
                    n = params_name[i]
                    if '*' in t:
                        py_params_type += f", POINTER({t.replace('*','').strip()})"
                        py_params_name.append(f"copy.deepcopy(POINTER({t.replace('*','').strip()}).from_param({n}).contents)")
                    else:
                        py_params_type += f', {type_dict[t]}'
                        py_params_name.append(n)
                    py_params_def.append(f"{n}: {t.replace('*','').strip()}")

                py_on_reg.append(f'''
        self.h.SetOn{on_name}.argtypes = [c_void_p, c_void_p]
        self.h.SetOn{on_name}.restype = None
        self.evOn{on_name} = CFUNCTYPE(None{py_params_type})(self.__On{on_name})
        self.h.SetOn{on_name}(self.spi, self.evOn{on_name})''')

                py_on_def__.append(f'''
    def __On{on_name}(self{(', ' + ', '.join(params_name)) if len(params_name)>0 else ''}):
        self.On{on_name}({', '.join(py_params_name)})''')

                py_on_def.append(f'''
    def On{on_name}(self, {', '.join(py_params_def)}):
        print('===On{on_name}===: {', '.join(py_params_def)}')''')

                # C#
                cs_params = []
                for i, t in enumerate(params_type):
                    n = params_name[i]
                    if '*' in t:
                        cs_params.append(f"ref {t.replace('*','').strip()} {n}")
                    else:
                        cs_params.append(f"{type_dict[t].replace('c_', '').replace('32','')} {n}")
                # 处理32位调用
                cs_on_dele.append(f'[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]')
                cs_on_dele.append(f"public delegate void DeleOn{on_name}({','.join(cs_params)});")
                cs_on_set.append(f'public void SetOn{on_name}(DeleOn{on_name} func) {{(Invoke(_handle, "SetOn{on_name}", typeof(DeleSet)) as DeleSet)(_spi, func);}}')
            else:  # req
                g_req = re.search(r'virtual\s+(\w+)\s+(\w+)[(](.*)[)].*0;', line)
                if g_req is not None and '//' not in line:  # 过滤一个之前有但现在不支持的函数
                    req_type = g_req.group(1)
                    req_name = g_req.group(2)
                    req_params = g_req.group(3)
                    req_params_name = ''
                    argtypes = ''
                    py_params = ''
                    py_params_name = ''
                    py_params_stru = []  # 有struct则转换为各字段为参数

                    cs_argtypes = '' # 定义delegate使用
                    cs_params = [] # 定义函数时使用public IntPtr Reqxxx(cs_params)
                    cs_params_name = '' # 调用底层时使用 return (Invoke(_handle, "ReqUserLogin", typeof(DeleReqUserLogin)) as DeleReqUserLogin)(_api, struc, this.nRequestID++);
                    cs_params_stru = []  # 有struct则转换为各字段为参数

                    if req_params != '':
                        req_params = ', ' + req_params  # CShfeFtdcQryStatField *pQryStat, int nRequestID

                        params_name = []
                        params_type = []
                        for p in re.findall(r'(\w+\s+[*]*)\s*([\w\[\]]+)', req_params): # 参数名包含[]
                            params_name.append(p[1])  # 'pQryStat' **不**能去掉订阅合约时参数后面的[]
                            params_type.append(p[0].strip())  # CShfeFtdcQryStatField *
                        req_params_name = ', '.join(params_name).replace('[', '').replace(']', '')

                        # pQryStat: CShfeFtdcQryStatField
                        for i, t in enumerate(params_type):
                            n = params_name[i]
                            py_params_name += ', '
                            cs_params_name += ', '
                            # RegisterSpi函数特别处理
                            if n == 'pSpi':
                                py_params += f', {n}'
                                py_params_name += n

                                cs_argtypes += f', IntPtr {n}'
                                cs_params.append(f'IntPtr {n}')
                                cs_params_name += n
                                continue

                            if 'char *' in t:  # char *=>str
                                if '[]' in n:  # char * 数组
                                    _n = n.split('[')[0]
                                    py_params += f", {_n}: str"
                                    py_params_stru.append("ca1 = (ctypes.c_char_p * 1)()")
                                    py_params_stru.append(f"ca1[0] = bytes({_n}, encoding='ascii')")
                                    py_params_name += 'ca1'

                                    cs_argtypes += f', IntPtr {_n}'
                                    cs_params.append(f'IntPtr {_n}')
                                    cs_params_name += _n
                                else:
                                    py_params += f", {n}: str"
                                    # byref(pQryStat), nRequestID
                                    py_params_name += f"bytes({n}, encoding='ascii')" if 'char *' in t else (n if t in type_dict else f'byref({n})')

                                    cs_argtypes += f', string {n}'
                                    cs_params.append(f'string {n}')
                                    cs_params_name += n
                            elif '*' in t:  # struct按字段赋值 CShfeFtdcSubMarketDataField*
                                # 取struct所有字段
                                stru_name = t.replace('*', '').strip()
                                stru = getattr(ctp_struct, stru_name)()
                                lst = getattr(stru, '_fields_')
                                py_params_stru.append(f"{n} = {stru_name}()")

                                cs_params_stru.append(f'{stru_name} {n} = new {stru_name}')
                                cs_params_stru.append('{')
                                cs_argtypes += f', ref {stru_name} {n}'
                                for l in lst:
                                    # 多个Struc参数时,字段可能重复
                                    if f' {l[0]}:' in py_params:
                                        continue
                                    cs_params_stru.append(f'\t{l[0]} = {l[0]},')
                                    type_name = l[1].__name__
                                    if 'c_char_Array_' in type_name:
                                        py_params += f", {l[0]}: str = ''"
                                        py_params_stru.append(f"{n}.{l[0]} = bytes({l[0]}, encoding='ascii')")
                                        cs_params.append(f'string {l[0]} = ""')
                                    elif 'char' in type_name:  # 枚举
                                        # 利用读取源码取得枚举类型
                                        _t_name = re.search(r'return\s+(\w*)', inspect.getsourcelines(getattr(stru, f'get{l[0]}'))[0][-1]).group(1)
                                        py_params += f", {l[0]}: {_t_name} = list({_t_name})[0]"
                                        py_params_stru.append(f"{n}.{l[0]} = {l[0]}.value")
                                        cs_params.append(f'{_t_name} {l[0]} = {_t_name}.{getattr(stru, "get"+l[0])().name}')
                                    elif 'long' in type_name:
                                        py_params += f", {l[0]}: int = 0"  # c_long => int 默认值由1改为0,原因TThostFtdcBoolType为int型,默认为1会导致按true处理,在reqorderinsert中userforceclose被置为true则表示为"强平单"
                                        py_params_stru.append(f"{n}.{l[0]} = {l[0]}")
                                        cs_params.append(f'int {l[0]} = 1')
                                    elif 'bool' in type_name:
                                        py_params += f", {l[0]}: bool = False"
                                        py_params_stru.append(f"{n}.{l[0]} = {l[0]}")
                                        cs_params.append(f'bool {l[0]} = False')
                                    elif 'double' in type_name:
                                        py_params += f", {l[0]}: float = .0"
                                        py_params_stru.append(f"{n}.{l[0]} = {l[0]}")
                                        cs_params.append(f'double {l[0]} = 0.0')
                                    else:
                                        raise Exception(f'no type: {type_name}')
                                        # py_params += f"{l[0]}: {[k for k, v in type_dict.items() if v == type_name][0]}" # c_bool => bool
                                py_params_name += f'byref({n})'
                                cs_params_name += f'ref {n}'
                                cs_params_stru.append('};')
                            elif 'nRequestID' in n:
                                py_params_stru.append('self.nRequestID += 1')
                                py_params_name += 'self.nRequestID'
                                cs_params_name += 'this.nRequestID++'
                                cs_argtypes += ', int nRequestID'
                            else:
                                py_params += f", {n}: {t.strip()} = 1"
                                # byref(pQryStat), nRequestID
                                py_params_name += n
                                if 'int' in t:
                                    cs_params.append(f'{t.strip()} {n} = 1')
                                else:
                                    cs_params.append(f'{t.strip()} {n}')
                                cs_params_name += n
                                cs_argtypes += f', {t.strip()} {n}'
                        # 转换参数类型为c_xxxx
                        argtypes = ', ' + ', '.join([type_dict[t] if t in type_dict else 'c_void_p' for t in params_type])
                    # 处理32位
                    cs_req_type_def.append('\t\t[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]')
                    cs_req_type_def.append(f'\t\tpublic delegate IntPtr Dele{req_name}(IntPtr api{cs_argtypes});')
                    cs_params_stru = ('\n\t\t\t' + '\n\t\t\t'.join(cs_params_stru)) if len(py_params_stru) > 0 else ''
                    cs_req_def_body.append(f'''
        public IntPtr {req_name}({','.join(cs_params)})
        {{{cs_params_stru}
            return (Invoke(_handle, "{req_name}", typeof(Dele{req_name})) as Dele{req_name})(_api{cs_params_name});
        }}
                    ''')

                    # self.h.ReqQryTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]     self.h.ReqQryTradingAccount.restype = c_void_p
                    py_req_type_def.append(f"\n{' '*8}self.h.{req_name}.argtypes = [c_void_p{argtypes}]\n{' '*8}self.h.{req_name}.restype = c_void_p")
                    # py_req_def_body.append(f"{' '*4}def {req_name}(self{py_params}):\n{' '*8}self.h.{req_name}(self.api{py_params_name})")
                    py_params_stru = (f"\n{' '*8}" + f"\n{' '*8}".join(py_params_stru)) if len(py_params_stru) > 0 else ''
                    py_req_def_body.append(f'''
    def {req_name}(self{py_params}):{py_params_stru}
        self.h.{req_name}(self.api{py_params_name})''')

                    if not req_name.endswith('UserSystemInfo'):
                        cpp_req.append(f'DLL_EXPORT_C_DECL void* WINAPI {req_name}({api_class_name} *api{req_params}){{api->{req_name}({req_params_name}); return 0;}}')
                    def_req.append(req_name)

    if generate_c:
        f_c_h.write('\n'.join(lines_on))
        f_c_h.write('};\n')

        f_c_cpp.write('\n'.join(cpp_null))
        f_c_cpp.write('\n}\n\n')

        f_c_cpp.write('\n'.join(cpp_set))
        f_c_cpp.write(f'''\n\nDLL_EXPORT_C_DECL void* WINAPI CreateApi(){{return {create_api}("./log/");}}\nDLL_EXPORT_C_DECL void* WINAPI CreateSpi(){{return new {spi_class_name.title()}();}}\n''')
        f_c_cpp.write('\n'.join(cpp_req))
        if spi_class_name.lower().endswith('trade'):
            f_c_cpp.write('''\n// SE版本
DLL_EXPORT_C_DECL void* WINAPI GetVersion() { return (void *)CThostFtdcTraderApi::GetApiVersion(); }

DLL_EXPORT_C_DECL void* WINAPI RegisterUserSystemInfo(CThostFtdcTraderApi* api, CThostFtdcUserSystemInfoField* pUserSystemInfo)
{
	char pinfo[344];
	int nLen;
	CTP_GetSystemInfo(pinfo, nLen);
	memcpy(pUserSystemInfo->ClientSystemInfo, pinfo, nLen);
	api->RegisterUserSystemInfo(pUserSystemInfo);
	return 0;
}
DLL_EXPORT_C_DECL void* WINAPI SubmitUserSystemInfo(CThostFtdcTraderApi* api, CThostFtdcUserSystemInfoField* pUserSystemInfo)
{
	char pinfo[344];
	int nLen;
	CTP_GetSystemInfo(pinfo, nLen);
	memcpy(pUserSystemInfo->ClientSystemInfo, pinfo, nLen);
	api->SubmitUserSystemInfo(pUserSystemInfo);
	return 0;
}''')
        # f_c_def.write('LIBRARY ctp_trade\nEXPORTS\nCreateApi\nCreateSpi\n')
        # f_c_def.write('\n'.join(def_req))
        # f_c_def.write('\n')
        # f_c_def.write('\n'.join(def_on))

    if generate_py:
        f_py.write('\n'.join(py_req_type_def))
        f_py.write(f"\n{' '*8}os.chdir(cur_path)")
        f_py.write('\n\n')
        f_py.write('''
    def CreateApi(self):
        self.api = self.h.CreateApi()
        return self.api
        
    def CreateSpi(self):
        self.spi = self.h.CreateSpi()
        return self.spi\n\n''')
        f_py.write('\n'.join(py_req_def_body))
        f_py.write(f"\n\n{' '*4}def RegCB(self):")
        f_py.write('\n'.join(py_on_reg))
        f_py.write('\n')
        f_py.write('\n'.join(py_on_def__))
        f_py.write('\n')
        f_py.write('\n'.join(py_on_def))

    if generate_cs:
        f_cs.write('\n'.join(cs_req_type_def))
        f_cs.write('\n'.join(cs_req_def_body))
        f_cs.write('\n\t\t[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]')
        f_cs.write('\n\t\tdelegate void DeleSet(IntPtr spi, Delegate func);')
        f_cs.write('\n\t\t')
        f_cs.write('\n\t\t'.join(cs_on_dele))
        f_cs.write('\n\t\t')
        f_cs.write('\n\t\t'.join(cs_on_set))

        f_cs.write('\n\t}\n}')

if __name__ == '__main__':
    src_dir = '../ctp_20180109_x86'
    spi_class_name = 'trade'
    file_src = 'ThostFtdcTraderApi'
    lib_name = 'thosttraderapi'
    api_class_name = 'CThostFtdcTraderApi'
    info_struct_name = 'CThostFtdcRspInfoField'
    create_api = 'CThostFtdcTraderApi::CreateFtdcTraderApi'
    run(True, True)
    # run(False, True)
    spi_class_name = 'quote'
    file_src = 'ThostFtdcMdApi'
    lib_name = 'thostmduserapi'
    api_class_name = 'CThostFtdcMdApi'
    info_struct_name = 'CThostFtdcRspInfoField'
    create_api = 'CThostFtdcMdApi::CreateFtdcMdApi'
    run(True, True)
    # run(False, True)
