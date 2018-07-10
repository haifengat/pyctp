#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""

import os


class Generate:

    def __init__(self, dir, apiName):
        self.cbNames = []
        self.cbArgs_dict = {}

        self.fcNames = []
        self.fcArgs_dict = {}
        self.ctp_dir = dir

        self.ClassName = 'Quote'
        self.ApiName = 'CThostFtdcMdApi'
        self.SpiName = 'CThostFtdcMdSpi'
        self.HFile = 'ThostFtdcMdApi'
        self.LibFile = 'thostmduserapi'

        if apiName.upper() == 'TRADE':
            self.ClassName = 'Trade'
            self.ApiName = 'CThostFtdcTraderApi'
            self.SpiName = 'CThostFtdcTraderSpi'
            self.HFile = 'ThostFtdcTraderApi'
            self.LibFile = 'thosttraderapi'

        self.fcpp = open(os.path.join(self.ctp_dir, self.HFile + '.h'), 'r')

        self.f_head = open(os.path.join('..\ctp_c', '{0}.h'.format(apiName)), 'w', encoding='utf8')

        self.f_cpp = open(os.path.join('..\ctp_c', '{0}.cpp'.format(apiName)), 'w', encoding='utf8')

    def processCallBack(self, line):
        line = line.replace('\tvirtual void ', '')  # 删除行首的无效内容
        line = line.replace('{};\n', '')  # 删除行尾的无效内容

        content = line.split('(')
        cbName = content[0]  # 回调函数名称*Onxxxx

        self.cbNames.append(cbName)

        cbArgs = content[1]  # 回调函数参数
        if cbArgs[-1] == ' ':
            cbArgs = cbArgs.replace(') ', '')
        else:
            cbArgs = cbArgs.replace(')', '')
        self.cbArgs_dict[cbName] = cbArgs

    def processFunction(self, line):

        # line = line.replace('\tvirtual int ', '')  # 删除行首的无效内容
        line = line.replace(') = 0;\n', '')  # 删除行尾的无效内容
        content = line.split('(')
        fcName = content[0].split(' ')[-1].replace('*', '')  # 回调函数名称

        self.fcNames.append(fcName)

        fcArgs = content[1]  # 回调函数参数
        fcArgs = fcArgs.replace(')', '')

        self.fcArgs_dict[fcName] = fcArgs

    def WriteH(self):

        self.f_head.write('')
        self.f_head.write("""
#pragma once
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
#define WINAPI      __stdcall
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#include "{4}/{0}.h"
#pragma comment(lib, "{4}/{1}.lib")
#else
#define WINAPI
#include "{4}/{0}.h"
#endif

#include <string.h>

class {2}: {3}
{{
public:
	{2}(void);
	~{2}(void);
	//针对收到空反馈的处理
	CThostFtdcRspInfoField rif;
	CThostFtdcRspInfoField* repare(CThostFtdcRspInfoField *pRspInfo)
	{{
		if (pRspInfo == NULL)
		{{
			memset(&rif, 0, sizeof(rif));
			return &rif;
		}}
		else
			return pRspInfo;
	}}
""".format(self.HFile, self.LibFile, self.ClassName, self.SpiName, self.ctp_dir))

        vars = ''
        typedef = ''
        virtual = ''
        for cbName in self.cbNames:  # 使用[]保证多次生成的顺序一致 self.cbArgs_dict:
            cbArgs = self.cbArgs_dict[cbName]
            cbArgsList = cbArgs.split(', ')  # 将每个参数转化为列表

            cbArgsTypeList = []
            cbArgsValueList = []

            for arg in cbArgsList:  # 开始处理参数
                content = arg.split(' ')
                if len(content) > 1:
                    cbArgsTypeList.append(content[0])  # 参数类型列表
                    cbArgsValueList.append(content[1].replace('*', ''))  # 参数数据列表

            cb = cbName[2:]

            # 生成.h文件中的on部分
            if 'OnRspError' in cbName:
                on_line = """
	virtual void onRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
	{
		if (_RspError)
		{
			((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
		}
	}\n"""
            elif 'OnRsp' in cbName:
                cnt = """
		if (_{0})
		{{
			if ({2})
				(({0})_{0})({2}, repare(pRspInfo), nRequestID, bIsLast);
			else
			{{
				{1} f; memset(&f, 0, sizeof(f));
				(({0})_{0})(&f, repare(pRspInfo), nRequestID, bIsLast);
			}}
		}}""".format(cb, cbArgsTypeList[0], cbArgsValueList[0])

                on_line = '\tvirtual void {0} ({1})\n\t{{{2}\n\t}}\n'.format(cbName, cbArgs, cnt)
            elif 'OnRtn' in cbName:
                cnt = """if (_{0}) (({0})_{0})({1});""".format(cb, cbArgsValueList[0])
                on_line = '\tvirtual void {0} ({1})\n\t{{\n\t\t{2}\n\t}}\n'.format(cbName, cbArgs, cnt)
            elif 'OnErrRtn' in cbName:
                params = ''
                for args in cbArgsValueList:
                    params += args if params == '' else (', ' + args)
                cnt = """if (_{0}) (({0})_{0})({1});""".format(cb, params)
                on_line = '\tvirtual void {0} ({1})\n\t{{\n\t\t{2}\n\t}}\n'.format(cbName, cbArgs, cnt)
            else:
                cnt = """if (_{0}) (({0})_{0})({1});""".format(cb, '' if len(cbArgsValueList) == 0 else cbArgsValueList[0])
                on_line = '\tvirtual void {0} ({1}) {{{2}}}\n'.format(cbName, cbArgs, cnt)

            if on_line != '':
                # typedef int (WINAPI *RspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
                typedef += '\ttypedef int (WINAPI *{0})({1});\n'.format(cb, cbArgs)

                # void* _FrontConnected;
                vars += '\tvoid *_{0};\n'.format(cb)

                # virtual void OnFrontConnected(){ if (_FrontConnected) ((FrontConnected)_FrontConnected)(); }
                virtual += on_line

        self.f_head.write(typedef)
        self.f_head.write('\n')
        self.f_head.write(vars)
        self.f_head.write('\n')
        self.f_head.write(virtual)
        self.f_head.write('\n')
        self.f_head.write('};\n')

    def WriteCpp(self):

        initCb = ''
        # SetFunction(api, func){spi.xxx = xxx
        setf = ''
        for cbName in self.cbNames:
            cb = cbName[2:]
            # set
            setf += 'DLL_EXPORT_C_DECL void WINAPI Set{0}({2}* spi, void* func){{spi->_{1} = func;}}\n'.format(cbName, cb, self.ClassName)
            initCb += '\t_{0} = NULL;\n'.format(cb)

        self.f_cpp.write('')
        self.f_cpp.write("""

#include "{2}.h"
#include <string.h>
int nReq;

{1}::{1}(void)
{{
{0}
}}
""".format(initCb, self.ClassName, self.ClassName.lower()))

        self.f_cpp.write(setf)

        self.f_cpp.write("""
DLL_EXPORT_C_DECL void* WINAPI CreateApi(){{return {1}("./log/");}}

DLL_EXPORT_C_DECL void* WINAPI CreateSpi(){{return new {0}();}}

""".format(self.ClassName, 'CThostFtdcTraderApi::CreateFtdcTraderApi' if self.ClassName == 'Trade' else 'CThostFtdcMdApi::CreateFtdcMdApi'))

        for fcName in self.fcNames:  # 使用[]保证多次生成的顺序一致 self.fcArgs_dict:
            fcArgs = self.fcArgs_dict[fcName]
            fcArgsList = fcArgs.split(', ')  # 将每个参数转化为列表

            fcArgsTypeList = []
            fcArgsValueList = []

            for arg in fcArgsList:  # 开始处理参数
                content = arg.replace('*', '').split(' ', 1)
                if len(content) > 1:
                    fcArgsTypeList.append(content[0])  # 参数类型列表
                    fcArgsValueList.append(content[1].replace(' ', ''))  # 参数数据列表
            params = ''
            for p in fcArgsValueList:
                p = p.replace('[', '').replace(']', '')
                params += p if params == '' else ',' + p

            # if line.find(' int ') >= 0:
            #     self.Voids += 'void* WINAPI {0}({1} *api {2}){{return (void *)api->{0}({3});}}\n'.format(fcName, self.ApiName, '' if fcArgs == '' else ',' + fcArgs, params)
            # else:
            self.f_cpp.write('DLL_EXPORT_C_DECL void* WINAPI {0}({1} *api {2}){{api->{0}({3}); return 0;}}\n'.format(fcName, self.ApiName, '' if fcArgs == '' else ',' + fcArgs, params))

    def run(self):
        for line in self.fcpp.readlines():
            if "\tvirtual void On" in line:
                self.processCallBack(line)
            # elif "\tvirtual int" in line:
            elif '= 0;' in line:
                # virtual void RegisterFront(char *pszFrontAddress) = 0;
                # ==>
                # DllExport void* WINAPI
                self.processFunction(line)
        self.WriteH()
        self.WriteCpp()


if __name__ == '__main__':
    # 构建quote  cb, func
    g = Generate('../ctp_20160628', 'trade')
    g.run()
    g = Generate('../ctp_20160628', 'quote')
    g.run()

    # 运行generate_struct.py 和 generate_enum.py即可

    # 下面的enum 和 struc 只需要运行一次
    # e = GenerateEnum()
    # e.main()

    # from generate_struct import GenerateStruct
    # s = GenerateStruct()
    # s.main()
