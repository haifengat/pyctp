#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2016/9/17'
"""

from ctp_data_type import typedefDict
import os
# /// <summary>
# ///资金账户基本准备金
# /// </summary>
# [StructLayout(LayoutKind.Sequential)]
# public struct CThostFtdcTradingAccountReserveField
# {
# 	/// <summary>
# 	///经纪公司代码
# 	/// </summary>
# 	[MarshalAs(UnmanagedType.ByValTStr, SizeConst = 11)]
# 	public string BrokerID;
#
# 	/// <summary>
# 	///投资者帐号
# 	/// </summary>
# 	[MarshalAs(UnmanagedType.ByValTStr, SizeConst = 13)]
# 	public string AccountID;
#
# 	/// <summary>
# 	///基本准备金
# 	/// </summary>
# 	public double Reserve;
#
# 	/// <summary>
# 	///币种代码
# 	/// </summary>
# 	[MarshalAs(UnmanagedType.ByValTStr, SizeConst = 4)]
# 	public string CurrencyID;
# }


class Generate:
    def __init__(self, dir, out_path):
        self.ctp_dir = dir
        self.out_path = out_path

    def run(self):
        """主函数"""
        fcpp = open(os.path.join(os.path.abspath(self.ctp_dir), 'ThostFtdcUserApiStruct.h'), 'r')
        fpy = open(os.path.join(self.out_path, 'ctp_struct.cs'), 'w', encoding='utf-8')

        fpy.write('\n')
        fpy.write('using System.Runtime.InteropServices;\n')
        fpy.write('\n')

        py_str = ''
        py_str_idx = 0
        py_str_format = ''

        for no, line in enumerate(fcpp):

            # 结构体申明注释
            if '///' in line and '\t' not in line:
                remark = line[3:-1]
                continue

            # 结构体变量注释
            elif '\t///' in line:
                remark = line[4:-1]
                continue

            # 结构体申明
            elif 'struct ' in line:
                content = line.split(' ')
                name = content[1].replace('\n', '')

                # struct begin
                py_line = """
/// <summary>
/// {1}
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct {0}
{{""".format(name, remark)

            # 结构体变量
            elif '\t' in line and '///' not in line:
                content = line.split('\t')
                if line.find('short') >= 0:
                    content = content
                typedef = content[1]
                type_ = typedefDict[typedef]
                variable = content[2].replace(';\n', "")
                # fields
                py_line = """
 	/// <summary>
 	/// {0}
 	/// </summary>""".format(remark)
                if type_ == 'c_int32':
                    py_line += '\n\tpublic int {0};'.format(variable)
                elif type_ == 'c_double':
                    py_line += '\n\tpublic double {0};'.format(variable)
                elif type_.find('short') >= 0:
                    py_line += '\n\tpublic short {0};'.format(variable)
                elif type_.find('c_char*') >= 0:
                    py_line += """
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst={1})]
	public string {0};""".format(variable, type_.split('*')[1])
                elif type_.find('c_char') >= 0:
                    py_line += '\n\tpublic {0} {1};'.format(typedef, variable)
                else:
                    py_str_format += "self.{0}, ".format(variable)
                    py_str += "{0}={{{1}}}, ".format(variable, py_str_idx)

                py_str_idx += 1
                # py_str += '{0}={{self.{0}}}, '.format(variable)

            # 结构体结束
            elif '}' in line:
                # struct end
                py_line = '\n}\n\n'

            # 结构体开始
            elif '{' in line:
                py_line = ''
                py_str = ''
                py_str_idx = 0
                py_str_format = ''

            # 其他
            else:
                py_line = '\n'
                continue

            fpy.write(py_line)


if __name__ == '__main__':
    import generate_cs as g
    for out_path in g.out_paths:
        Generate(g.ctp_path, out_path).run()
