#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/7
# @desc    : generate enums

import os
import re

type_dict = {'int': 'c_int32', 'char': 'c_char', 'double': 'c_double', 'short': 'c_short', 'string': 'c_char_p', 'bool': 'c_bool'}

cur_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = ''
data_type_file_name = ''


def run():
    f_src = open(os.path.join(cur_dir, src_dir, f'{data_type_file_name}.h'), 'r', encoding='gbk')
    f_py_enum = open(os.path.join(cur_dir, '..', 'py_ctp', 'ctp_enum.py'), 'w', encoding='utf-8')
    f_cs_enum = open(os.path.join(cur_dir, '..', 'cs_ctp', 'proxy', 'ctp_enum.cs'), 'w', encoding='utf-8')
    f_py_type = open(os.path.join(cur_dir, 'data_type.py'), 'w', encoding='utf-8')

    f_py_type.write(r'''#!/usr/bin/env python
# -*- coding: utf-8 -*-

typedefDict = {}
''')

    f_py_enum.write('''#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum\n\n
class THOST_TE_RESUME_TYPE(Enum):
	TERT_RESTART = 0
	TERT_RESUME = 1
	TERT_QUICK = 2\n\n
''')

    f_cs_enum.write('''
/// <summary>
/// 
/// </summary>
public enum THOST_TE_RESUME_TYPE
{
    /// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESTART = 0,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESUME,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_QUICK
}\n\n''')

    line: str = ''
    lines = [l.strip() for l in f_src.readlines()]
    no = -1
    for line in lines:
        no += 1

        g_type = re.search(r'typedef\s*(\w*)\s*(\w*)(.*)$', line)
        if g_type is not None:
            src_type = g_type.group(1)
            tar_type = g_type.group(2)
            param = g_type.group(3)
            if src_type == 'char' and param == ';':  # char TShfeFtdcInvestorRangeType;
                py_lines = []
                cs_lines = []
                for i in range(no, 0, -1):
                    g = re.search(r'是一个(.*)$', lines[i])
                    if g is not None:  # enum 注释
                        py_lines.append(f'"""{g.group(1)}"""')
                        cs_lines.insert(0, f"public enum {g_type.group(2)} : byte\n{{")
                        cs_lines.insert(0, f'/// <summary>\n/// {g.group(1)}\n///</summary>')
                        break
                    # 枚举值
                    g = re.search(r'#define\s*(\S*).*(\w+)', lines[i])  # #define SHFE_FTDC_ISPI_BillDeposit '9'
                    if g is not None:  # 枚举值注释
                        g1 = re.search(r'///(.*)$', lines[i - 1])
                        if g1 is not None:
                            py_lines.append(f'"""{g1.group(1)}"""') # """收盘"""
                            cs_lines.append(f'\t/// <summary>\n\t/// {g1.group(1)}\n\t///</summary>')
                        py_lines.append(f"{g.group(1)} = {ord(g.group(2))}") # THOST_FTDC_IS_Closed = 54
                        cs_lines.append(f"\t{g.group(1)} = (byte)'{g.group(2)}',")

                py_lines.reverse()
                py_lines = '\n    '.join(py_lines)
                f_py_enum.write(f"class {g_type.group(2)}(Enum):\n    {py_lines}\n")
                f_py_enum.write('\n\n')

                # cs_lines.reverse()
                cs_lines = '\n'.join(cs_lines)
                f_cs_enum.write(f"{cs_lines}\n}}\n\n")
            else:
                g_n = re.search(r'\[(\d+)\]', param)
                if g_n is not None:  # char TShfeFtdcTraderIDType[21];
                    f_py_type.write(f"typedefDict['{tar_type}'] = 'c_char*{g_n.group(1)}'\n")
                else:  # int double short
                    f_py_type.write(f"typedefDict['{tar_type}'] = '{type_dict[src_type]}'\n")
                g_comment = re.search(r'是一个(.*)$', lines[no - 2])
                if g_comment is not None:  # 注释
                    f_py_type.write(f'"""{g_comment.group(1)}"""\n')


if __name__ == '__main__':
    src_dir = '../ctp_20180109_x86'
    data_type_file_name = 'ThostFtdcUserApiDataType'
    run()
