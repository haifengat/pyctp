#!/usr/bin/env python
# coding:utf-8
"""
  Author:  HaiFeng --<galaxy>
  Purpose:
  Created: 2016/7/5
"""
import os
# /////////////////////////////////////////////////////////////////////////
# ///TFtdcInvestorRangeType是一个投资者范围类型
# /////////////////////////////////////////////////////////////////////////
# ///所有
# #define THOST_FTDC_IR_All '1'
# ///投资者组
# #define THOST_FTDC_IR_Group '2'
# ///单一投资者
# #define THOST_FTDC_IR_Single '3'
#
# typedef char TThostFtdcInvestorRangeType;


class Generate():

    def __init__(self, dir):
        self.ctp_dir = dir
        # C++和python类型的映射字典
        self.type_dict = {'int': 'c_int32', 'char': 'c_char', 'double': 'c_double', 'short': 'c_int32', 'string': 'c_char_p'}

        self.defline = []
        self.fenum = open(os.path.join(os.path.abspath('..\py_ctp'), 'ctp_enum.py'), 'w', encoding='utf-8')  # 增加utf-8解决乱码问题
        self.enum_comment = {}

    def process_line(self, line):
        """处理每行"""
        if '///' in line:  # 注释
            py_line = '#' + line[3:]

            # /// TFtdcInvestorRangeType是一个投资者范围类型 ==> """投资者范围类型"""
            if py_line.find('是一个') > 0:
                self.enum_comment[py_line[py_line.find('Ftdc') + 4:py_line.find('是一个')]] = '    """%s"""\n' % py_line[py_line.find('是一个') + 3:-1]

        elif 'typedef' in line:  # 类型申明
            # typedef char TThostFtdcInvestorRangeType; ==> typedefDict["TThostFtdcInvestorRangeType"] = "c_char"
            py_line = self.process_typedef(line)

            # class InvestorRangeType(Enum):
            # 	"""投资者范围类型"""
            # 	All = 49
            # 	Group = 50
            # 	Single = 51
            if line.find(' char ') > 0 and line.find('[') < 0:
                key = line.split(' ')[2][:-2]
                key = key[key.find('Ftdc') + 4:]
                enum_line = 'class %s(Enum):\n' % key
                enum_line += self.enum_comment[key]
                for l in self.defline:
                    enum_line += '    %s\n' % l
                enum_line += '\n    #----------------------------------------------------------------------\n'
                enum_line += '    def __int__(self):\n'
                enum_line += '        """return int value"""\n'
                enum_line += '        return self.value\n\n'
                enum_line += '    #----------------------------------------------------------------------\n'
                enum_line += '    def __char__(self):\n'
                enum_line += '        """return char value"""\n'
                enum_line += '        return chr(self.value)\n\n'

                self.fenum.write(enum_line)
            self.defline.clear()

        elif '#define' in line:  # 定义常量
            # define THOST_FTDC_IR_All '1' ==> defineDict["THOST_FTDC_IR_All"] = '1'
            content = line.split(' ')
            constant = content[1]
            if len(content) > 2:
                value = content[-1]
                py_line = 'defineDict["%s"] = %s' % (constant, value)
            else:
                py_line = ''

            # enum relate define
            if py_line:  # split 3 ==> 分成4段最后一段,以解决新的h文件中类似Limit_FOK  Market_FOK的情况
                key = py_line[py_line.find('[') + 2:py_line.find(']') - 1].split('_', 3)[-1]
                if key[0].isdigit():
                    key = key[1:] + key[0:1]
                elif key == 'None':
                    key = 'Zero'
                if len(value) > 4:
                    value = value[1:-2]
                else:
                    value = ord(value[1])
                self.defline.append('{0} = {1}'.format(key, value))

        elif line == '\n':  # 空行
            py_line = line
        else:
            py_line = ''

        return py_line

    def process_typedef(self, line):
        """处理类型申明"""
        content = line.split(' ')
        type_ = self.type_dict[content[1]]

        if type_ == 'c_char' and '[' in line:
            # type_ = 'string'
            type_ = '%s*%s' % (type_, line[line.index('[') + 1:line.index(']')])

        keyword = content[2]
        if '[' in keyword:
            i = keyword.index('[')
            keyword = keyword[:i]
        else:
            keyword = keyword.replace(';\n', '')  # 删除行末分号

        py_line = 'typedefDict["%s"] = "%s"\n' % (keyword, type_)

        return py_line

    def run(self):
        """主函数"""
        try:
            fcpp = open(os.path.join(os.path.abspath(self.ctp_dir), 'ThostFtdcUserApiDataType.h'), 'r')
            fpy = open('ctp_data_type.py', 'w', encoding='utf-8')  # 增加utf-8解决乱码问题

            fpy.write('#!/usr/bin/env python\n')
            fpy.write('#coding:utf-8\n')
            fpy.write('\n')
            fpy.write('defineDict = {}\n')
            fpy.write('typedefDict = {}\n')
            fpy.write('\n')

            self.fenum.write('#!/usr/bin/env python\n')
            self.fenum.write('#coding:utf-8\n')
            self.fenum.write('''
from ctypes import *
from enum import Enum\n''')

            for no, line in enumerate(fcpp):
                py_line = self.process_line(line)
                if py_line:
                    fpy.write(py_line)
                # print(py_line)

            fcpp.close()
            fpy.close()
            self.fenum.close()

            print('data_type.py生成过程完成')
        except Exception as ex:
            print('data_type.py生成过程出错:' + str(ex))


if __name__ == '__main__':
    dir = '../ctp_20180109'
    Generate(dir).run()
