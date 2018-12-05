#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/13'
"""

import os


class Generate:

    def __init__(self, dir, apiName, out_path):
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
        self.f_py = open(os.path.join(out_path, 'ctp_{0}.cs'.format(apiName)), 'w', encoding='utf-8')

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

        self.fcNames.append(fcName.strip())

        fcArgs = content[1]  # 回调函数参数
        fcArgs = fcArgs.replace(')', '')

        self.fcArgs_dict[fcName] = fcArgs

    def WritePyCtp_xx(self):
        # structs and fields
        fstruct = open('..\py_ctp\ctp_struct.py', 'r', encoding='utf-8').readlines()
        fenum_cs = open(out_path + '\ctp_enum.cs', 'r', encoding='utf-8').readlines()
        struct_dict = {}  # 需要用到python的 ctp_struct.py文件
        struct_init_dict = {}
        deles = ''
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
            """

using System;
using System.IO;
using System.Runtime.InteropServices;

namespace HaiFeng
{{
	public class ctp_{0}
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
		delegate IntPtr Create();
		delegate IntPtr DeleRegisterSpi(IntPtr api, IntPtr pSpi);
		public ctp_{0}(string pAbsoluteFilePath)
		{{
			string curPath = Environment.CurrentDirectory;
			Environment.CurrentDirectory = new FileInfo(pAbsoluteFilePath).DirectoryName;
			_handle = LoadLibrary(pAbsoluteFilePath);
			if (_handle == IntPtr.Zero)
			{{
				throw (new Exception(String.Format("没有找到:", pAbsoluteFilePath)));
			}}
			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");

			_api = (Invoke(_handle, "CreateApi", typeof(Create)) as Create)();
			_spi = (Invoke(_handle, "CreateSpi", typeof(Create)) as Create)();
			(Invoke(_handle, "RegisterSpi", typeof(DeleRegisterSpi)) as DeleRegisterSpi)(_api, _spi);
		}}
""".format(self.ClassName.lower()))
        deles = ''
        funcs = []
    # 	funcs.append("""
    # public IntPtr {0}()
    # {{
    # 	return (Invoke(_handle, "{0}", typeof(Create)) as Create)();
    # }}\n""".format("CreateApi",""))
    # 	funcs.append("""
    # public IntPtr {0}()
    # {{
    # 	return (Invoke(_handle, "{0}", typeof(Create)) as Create)();
    # }}\n""".format("CreateSpi",""))

        type_dict = {'CThostFtdcTraderSpi': 'IntPtr', 'CThostFtdcMdSpi': 'IntPtr', 'c_int32': 'int', 'char*': 'string', 'c_double': 'double', 'c_short': 'short', 'string': 'string', 'c_bool': 'bool', 'c_long': 'int'}

        for fcName in self.fcNames:  # 使用[]保证多次生成的顺序一致 self.fcArgs_dict:
            if fcName == 'RegisterSpi':  # 封装在构造函数中
                continue
            fcArgs = self.fcArgs_dict[fcName]
            fcArgsList = fcArgs.split(', ')  # 将每个参数转化为列表

            fcArgsTypeList = []
            fcArgsValueList = []

            for arg in fcArgsList:  # 开始处理参数
                content = arg.replace('*', '').split(' ', 1)
                if len(content) > 1:
                    # 处理char *xx
                    if arg.find('char *') >= 0:
                        fcArgsTypeList.append('char*')  # 参数类型列表
                        fcArgsValueList.append(content[1].replace(' ', ''))  # 参数数据列表
                    else:
                        fcArgsTypeList.append(content[0])  # 参数类型列表
                        fcArgsValueList.append(content[1].replace(' ', ''))  # 参数数据列表

            # 对合约订阅与要的特别处理
            if self.ClassName.lower() == 'quote' and (fcName.find('Subscribe') == 0 or fcName.find('Subscribe') == 2):
                deles += '\t\tpublic delegate IntPtr Dele{0}(IntPtr api, IntPtr pInstruments, int pCount);\n'.format(fcName)
                func = '''
		public IntPtr {0}(IntPtr pInstruments, int pCount)
		{{
			return (Invoke(_handle, "{0}", typeof(Dele{0})) as Dele{0})(_api, pInstruments, pCount);
		}}\n'''.format(fcName)
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
                    # CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID =>,CThostFtdcReqUserLoginField pReqUserLoginField, int nRequestID
                    type = fcArgsTypeList[i]
                    args = fcArgsValueList[i].replace('[', '').replace(']', '')
                    if type in type_dict.keys():
                        types += ', {0} {1}'.format(type_dict[type], args)  # IntPtr nResumeType
                        if type == 'char':
                            values += ', ' + "bytes({0}, encoding='ascii')".format(args)
                        else:
                            values += ', ' + args
                        if args != 'nRequestID':  # 调用参数中不包含
                            params += ', {0} {1}'.format(type_dict[type], args)
                    else:  # 非基础类型的参数
                        if type in struct_dict.keys():
                            struct_init = '\n\t\t\t{0} struc = new {0}\n\t\t\t{{'.format(type)
                            for field in struct_dict[type]:
                                tt = str(field[1]).split('.')[-1].split('\'')[0]
                                # 对于c_char的参数需要有默认值,以防止调用时不赋值报错
                                # 合成structure bytes('9999', encoding='ascii')
                                if tt.find('c_char') >= 0:
                                    if tt.find('Array') > 0:
                                        params += ', string {0} = ""'.format(field[0])
                                        struct_init += "\n\t\t\t\t{0} = {0},".format(field[0])
                                    else:  # 处理enum类型
                                        # 找到field对应的类型
                                        idx = fstruct.index('class {0}(Structure):\n'.format(type))
                                        enum_type = None
                                        for i in range(idx + 1, len(fstruct)):
                                            if fstruct[i].find('get{0}(self):'.format(field[0])) >= 0:
                                                enum_type = fstruct[i + 1].split('(')[0].split(' ')[-1]
                                                break
                                        # 从ctp_enum.cs中找到类型的第一个值
                                        first = None
                                        idx = fenum_cs.index('public enum TThostFtdc{0} : byte\n'.format(enum_type))
                                        for i in range(idx + 1, len(fenum_cs)):
                                            if fenum_cs[i].find('THOST_FTDC_') >= 0:
                                                first = fenum_cs[i].split('=')[0].replace('\t', '').strip()
                                                break
                                        params += ", TThostFtdc{0} {1} = TThostFtdc{0}.{2}".format(enum_type, field[0], first)
                                        struct_init += "\n\t\t\t\t{0} = {0},".format(field[0])
                                else:
                                    params += ', {1} {0} = 0'.format(field[0], type_dict[tt])
                                    struct_init += "\t\t\t\t{0} = {0},\n".format(field[0])
                            struct_init += '\n\t\t\t};'
                            # 构造struct的语句
                            struct_init_dict[fcName] = struct_init
                            values += '{0}'.format('struc')
                        else:
                            values += ', {0}'.format(args)
                            if args != 'nRequestID':  # 调用参数中不包含
                                params += ', {0} {1}'.format(type, args)
                        types += ', {0} {1}'.format(type, args)

                # 声明主调函数类型 public delegate IntPtr SubscribePublicTopic (IntPtr ptr, IntPtr nResumeType);
                line = '''\t\tpublic delegate IntPtr Dele{0}(IntPtr api{1});\n'''.format(fcName, types)
                deles += line

                # 去掉首','
                params = params[2:] if params[0:1] == ',' else params
                params = params.strip()
                # 处理参数为Structure的情况:加入structu构造,去掉reqid
                if fcName in struct_init_dict.keys():
                    func = '''
		public IntPtr {0}({1})
		{{{3}
			return (Invoke(_handle, "{0}", typeof(Dele{0})) as Dele{0})(_api, {2});
		}}\n'''.format(fcName, params.replace(', nRequestID', ''), values.replace(', nRequestID', ', this.nRequestID++'), struct_init_dict[fcName])
                else:
                    func = '''
		public IntPtr {0}({1})
		{{
			return (Invoke(_handle, "{0}", typeof(Dele{0})) as Dele{0})(_api{2});
		}}\n'''.format(fcName, params, values)

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
                paramtype += ', {0} {1}'.format(('ref {0}'.format(t) if 'CThostFtdc' in t else t), cbArgsValueList[cbArgsTypeList.index(t)])
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
		public delegate void Dele{0}({1});
		public void Set{0}(Dele{0} func) {{ (Invoke(_handle, "Set{0}", typeof(DeleSet)) as DeleSet)(_spi, func); }}""".format(cbName, paramtype[2:])
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
                    cbFuncs.append("\t\tprint({0})\n".format(param))

        self.f_py.write('''
''')
        # 以上为__init__函数内容

        self.f_py.write("""
		#region 声明REQ函数类型\n""")
        self.f_py.write(deles)
        self.f_py.write("""
		#endregion""")

        self.f_py.write("""
		#region REQ函数\n
		private int nRequestID = 0;\n""")
        for func in funcs:
            self.f_py.write(func)
        self.f_py.write("""
		#endregion""")

        self.f_py.write('''
		delegate void DeleSet(IntPtr spi, Delegate func);
''')
        for reg in cbRegs:
            self.f_py.write(reg)

        # 回调函数
        # for func in cb__Funcs:
        # 	self.f_py.write(func)
        # for func in cbFuncs:
        # 	self.f_py.write(func)
        self.f_py.write('\n\t}\n}')

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

ctp_path = '../ctp_20180109'
# 生成两份文件用于测试
out_paths = ['../cs_ctp/proxy', '../cs_ctp/ctp_test']

if __name__ == '__main__':
    # 构建quote  cb, func
    for out_path in out_paths:
        g = Generate(ctp_path, 'trade', out_path)
        g.run()
        g = Generate(ctp_path, 'quote', out_path)
        g.run()

    # 运行generate_struct.py 和 generate_enum.py即可

    # 下面的enum 和 struc 只需要运行一次
    # e = GenerateEnum()
    # e.main()

    # from generate_struct import GenerateStruct
    # s = GenerateStruct()
    # s.main()
