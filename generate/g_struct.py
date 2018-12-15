#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/10
# @desc    : generate structs

import os
import re

from data_type import typedefDict

cur_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = ''
struct_file_name = ''

def run():
    f_src = open(os.path.join(cur_dir, src_dir, f'{struct_file_name}.h'), 'r', encoding='gbk')
    f_py_struct = open(os.path.join(cur_dir, '..', 'py_ctp', 'ctp_struct.py'), 'w', encoding='utf-8')  # 增加utf-8解决乱码问题

    f_py_struct.write('''#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2018/12/10'


from ctypes import *
from .ctp_enum import *
''')

    line = f_src.read()
    ss = re.findall(r'///(.*)\s*\n\s*struct([^}]*)', line)  # 找到
    for s in ss:
        remark = s[0]
        s_name = s[1].split('\n')[0]
        fields = re.findall(r'///(.*)\s*\n\s*(\w+)\s+(\w+);', s[1])
        fields_str = []
        fields_get = []
        fields_dic = []
        for f in fields:
            # 注释 类型 变量名
            remaek = f[0]
            f_type = f[1]
            f_name = f[2]
            type_name = typedefDict[f_type] if f_type in typedefDict else 'c_char'
            fields_str.append(f'{" "*8}("{f_name}", {type_name}),')  # ('SequenceSeries', c_short),
            if type_name == 'c_char': # 枚举
                get_value = f"{f_type}(ord(self.{f_name})) if self.{f_name} in list({f_type}) else list({f_type})[0]"
            else:
                get_value = f"str(self.{f_name}, 'GBK')" if 'char*' in type_name else f"self.{f_name}"
            fields_get.append(f"""
    def get{f_name}(self):
        '''{remaek}'''
        return {get_value}""")

            fields_dic.append(f"'{f[2]}': self.get{f[2]}()")
        fields_str = '\n'.join(fields_str)
        fields_get = '\n'.join(fields_get)
        fields_dic = ', '.join(fields_dic)
        f_py_struct.write(f'''
class {s_name}(Structure):
    """{remark}"""
    _fields_ = [
{fields_str}
    ]
{fields_get}

    def __str__(self): # 可以直接print
        return f"{fields_dic.replace(': ','={').replace(',','},')}}}"\n\n''')

if __name__ == '__main__':
    src_dir = '../ctp_20180109_x86'
    struct_file_name = 'ThostFtdcUserApiStruct'
    run()
