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
        self.ctp_dir = dir
        self.cbNames = []
        self.cbArgs_dict = {}

        self.fcNames = []
        self.fcArgs_dict = {}

        if apiName.upper() == 'TRADE':
            self.ClassName = 'Trade'
            self.ApiName = 'CThostFtdcTraderApi'
            self.SpiName = 'CThostFtdcTraderSpi'
            self.HFile = 'ThostFtdcTraderApi'
            self.LibFile = 'thosttraderapi'
        else:
            self.ClassName = 'Quote'
            self.ApiName = 'CThostFtdcMdApi'
            self.SpiName = 'CThostFtdcMdSpi'
            self.HFile = 'ThostFtdcMdApi'
            self.LibFile = 'thostmduserapi'

        self.fcpp = open(os.path.join(self.ctp_dir, self.HFile + '.h'), 'r')

        self.f_py = open(os.path.join('..\py_ctp', '{0}.py'.format(apiName)), 'w', encoding='utf-8')

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

    def WritePyCtp_xx(self):
        # structs and fields
        fstruct = open('..\py_ctp\ctp_struct.py', 'r', encoding='utf-8')
        struct_dict = {}
        struct_init_dict = {}
        import sys
        sys.path.append('..')
        m = __import__('py_ctp.ctp_struct')
        for line in fstruct:
            if line.find('Structure') >= 0:
                key = line.split(' ')[1].split('(')[0]
                c = getattr(getattr(m, 'ctp_struct'), key)
                o = c()
                struct_dict[key] = o._fields_

        self.f_py.write(
            """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py_ctp.ctp_struct import *
import os
import sys
import platform


def isWindowsSystem():
    return 'Windows' in platform.system()


class {0}:

    def __init__(self, absolute_dllfile_path: str):

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

        if isWindowsSystem():
            self.h = CDLL(absolute_dllfile_path)
        else:
            self.h = cdll.LoadLibrary(absolute_dllfile_path)

        self.h.CreateApi.argtypes = []
        self.h.CreateApi.restype = c_void_p

        self.h.CreateSpi.argtypes = []
        self.h.CreateSpi.restype = c_void_p

        self.api = None
        self.spi = None
        self.nRequestID = 0
""".format(self.ClassName, self.ClassName.lower()))
        funcs = []
        funcs.append("""
    def {0}(self{1}):
        self.api = self.h.{0}({1})
        return self.api\n""".format("CreateApi", ""))
        funcs.append("""
    def {0}(self{1}):
        self.spi = self.h.{0}({1})
        return self.spi\n""".format("CreateSpi", ""))

        type_dict = {'int': 'c_int32', 'char': 'c_char_p', 'double': 'c_double', 'short': 'c_int32', 'string': 'c_char_p', 'bool': 'c_bool'}

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

            # 对合约订阅与要的特别处理
            if self.ClassName.lower() == 'quote' and (fcName.find('Subscribe') == 0 or fcName.find('Subscribe') == 2):
                func = '''
    def {0}(self, pInstrumentID):
        self.h.{0}.argtypes = [c_void_p , c_char_p*1, c_int32]
        self.h.{0}.restype = c_void_p
        self.h.{0}(self.api, (c_char_p*1)(bytes(pInstrumentID, encoding = 'ascii')), 1)\n'''.format(fcName)
            else:
                # 类型声明时的argtypes用
                types = ''
                # def同行参数
                params = ''
                # 调用时的参数名
                values = ''
                struct_init = ''
                # for type in fcArgsTypeList:
                for i in range(len(fcArgsTypeList)):
                    type = fcArgsTypeList[i]
                    args = fcArgsValueList[i].replace('[', '').replace(']', '')
                    if type in type_dict.keys():
                        types += ' , ' + type_dict[type]

# CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID =>,pReqUserLoginField,nRequestID
                        if type == 'char':
                            values += ', ' + "bytes({0}, encoding='ascii')".format(args)
                        else:
                            values += ', ' + args
                        params += ', ' + args
                    else:  # 非基础类型的参数
                        if type in struct_dict.keys():
                            struct_init = '\n        struc = {0}()\n'.format(type)
                            for field in struct_dict[type]:
                                tt = str(field[1]).split('.')[-1].split('\'')[0]
                                # 对于c_char的参数需要有默认值,以防止调用时不赋值报错
                                # 合成structure bytes('9999', encoding='ascii')
                                if tt.find('c_char') >= 0:
                                    if tt.find('Array') > 0:
                                        params += ", {0} = ''".format(field[0])
                                        struct_init += "        struc.{0} = bytes({0}, encoding='ascii')\n".format(field[0])
                                    else:  # 处理enum类型
                                        params += ", {0} = ''".format(field[0])
                                        struct_init += "        struc.{0} = list({0}Type)[0].value if {0}=='' else {0}.value\n".format(field[0])
                                else:
                                    params += ', {0} = 0'.format(field[0])
                                    struct_init += "        struc.{0} = {0}\n".format(field[0])
                            # 构造struct的语句
                            struct_init_dict[fcName] = struct_init
                            values += ', byref({0})'.format('struc')
                        else:
                            values += ', {0}'.format(args)
                            params += ', ' + args
                        types += ' , c_void_p'

                line = '''        self.h.{0}.argtypes = [c_void_p{1}]
        self.h.{0}.restype = c_void_p\n'''.format(fcName, types)
                self.f_py.write(line)

                # 处理参数为Structure的情况:加入structu构造,去掉reqid
                if fcName in struct_init_dict.keys():
                    func = '''
    def {0}(self{1}):{3}
        self.nRequestID += 1
        self.h.{0}(self.api{2}, self.nRequestID)
            '''.format(fcName, params.replace(', nRequestID', ''), values.replace(', nRequestID', ''), struct_init_dict[fcName])
                else:
                    func = '''
    def {0}(self{1}):
        self.h.{0}(self.api{2})
            '''.format(fcName, params, values)

            funcs.append(func)

        cbRegs = []
        cb__Funcs = []
        cbFuncs = []
        # 响应函数
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

            paramtype = ''
            params = ''
            params__ = ''
            param_trans = ''

            for t in cbArgsTypeList:
                paramtype += ', ' + (type_dict[t] if t in type_dict.keys() else 'POINTER({0})'.format(t))
                # 在响应参数中加入参数的类型,方便之后的调用(可查类型)
                param = cbArgsValueList[cbArgsTypeList.index(t)]
                params__ += ', ' + param
                # if params == '':
                #     params += '{0} = {1}'.format(param, t)
                # else:
                params += ', {0} = {1}'.format(param, t)
# def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
# self.OnRspSubMarketData(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents, POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents, nRequestID, bIsLast)
                ref = param
                if t not in type_dict:
                    ref = 'POINTER({0}).from_param({1}).contents.clone()'.format(t, param)
                param_trans += ref if param_trans == '' else (', ' + ref)

            line = """
        self.h.Set{0}.argtypes = [c_void_p, c_void_p]
        self.h.Set{0}.restype = c_void_p
        self.ev{0} = CFUNCTYPE(c_void_p{1})(self.__{0})
        self.h.Set{0}(self.spi, self.ev{0})
""".format(cbName, paramtype)
            cbRegs.append(line)

            cb__Funcs.append("""
    def __{0}(self{1}):
        self.{0}({2})
    """.format(cbName, params__, param_trans))

            cbFuncs.append("""
    def {0}(self{1}):
        print('{0}:{1}')\n""".format(cbName, params))
            for param in params__.replace(' ', '').split(','):
                if param != '':
                    cbFuncs.append("        print({0})\n".format(param))

        self.f_py.write('''
        # restore work directory
        os.chdir(cur_path)

''')
        # 以上为__init__函数内容

        # 事件注册函数
        self.f_py.write('''
    def RegCB(self):
        """在createapi, createspi后调用"""
''')

        for reg in cbRegs:
            self.f_py.write(reg)

        # 回调函数
        for func in cb__Funcs:
            self.f_py.write(func)
        for func in cbFuncs:
            self.f_py.write(func)

        # 主调函数
        for func in funcs:
            self.f_py.write(func)

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

        self.WritePyCtp_xx()


if __name__ == '__main__':
    # 构建quote  cb, func
    os.chdir('./generate')
    dir = '../ctp_20180109'
    # 构建quote  cb, func
    g = Generate(dir, 'trade')
    g.run()
    g = Generate(dir, 'quote')
    g.run()

    # 运行generate_struct.py 和 generate_enum.py即可

    # 下面的enum 和 struc 只需要运行一次
    # e = GenerateEnum()
    # e.main()

    # from generate_struct import GenerateStruct
    # s = GenerateStruct()
    # s.main()
