#!/usr/bin/env python
# coding:utf-8
"""
  Author:  HaiFeng
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
    def __init__(self, dir, out_path):
        self.ctp_dir = dir
        # C++和python类型的映射字典
        self.type_dict = {'int': 'c_int32', 'char': 'c_char', 'double': 'c_double', 'short': 'c_short', 'string': 'c_char_p'}

        self.define = []
        self.fenum = open(os.path.join(out_path, 'ctp_enum.cs'), 'w', encoding='utf-8')  # 增加utf-8解决乱码问题
        self.f_data_type = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ctp_data_type.py'), 'w', encoding='utf-8')  # 增加utf-8解决乱码问题
        self.enum_comment = {}
        self.tmp_comment = ''

        self.fenum.write("""
public enum THOST_TE_RESUME_TYPE
{
	THOST_TERT_RESTART = 0,
	THOST_TERT_RESUME,
	THOST_TERT_QUICK
}
		""")
        self.f_data_type.write("""#!/usr/bin/env python
# coding:utf-8
\"\"\"
  Author:  HaiFeng
  Purpose:
  Created: 2016/7/5
\"\"\"

typedefDict = {}
defineDict = {}

""")

    def process_line(self, idx, line):
        """处理每行"""
        if '///' in line:  # 注释
            py_line = '#' + line[3:]

            # /// [T去掉ftdc前的内容，方便后面比对]FtdcInvestorRangeType是一个投资者范围类型 ==>
            # /// <summary>
            # /// 投资者范围类型
            # /// </summary>"""
            if py_line.find('是一个') > 0:
                self.enum_comment[py_line[py_line.find('Ftdc'):py_line.find('是一个')]] = '/// <summary>\n/// %s\n///</summary>' % py_line[py_line.find('是一个') + 3:-1]
            else:
                self.tmp_comment = '/// <summary>\n\t/// {0}\n\t///</summary>\n\t'.format(line[3:-1])  # -1去掉尾换行

        elif '#define' in line:  # 定义常量
            # define THOST_FTDC_IR_All '1' ==> defineDict["THOST_FTDC_IR_All"] = '1'
            content = line.split(' ')
            constant = content[1]
            if len(content) > 2:
                value = content[-1][:-1]  # value带行尾的\n
                py_line = 'defineDict["%s"] = %s\n' % (constant, value)
            else:
                py_line = ''

            # enum relate define
            if py_line:  # 命名保持一致，不再精简
                if len(value) > 3:  # 处理理'x' x长度>1的情况，如102001
                    self.define.append("{2}{0} = {1},".format(constant, value[1:-1], self.tmp_comment))
                else:
                    self.define.append("{2}{0} = (byte){1},".format(constant, value, self.tmp_comment))

        elif 'typedef' in line:  # 类型申明
            # typedef char TThostFtdcInvestorRangeType; ==> typedefDict["TThostFtdcInvestorRangeType"] = "c_char"
            py_line = self.process_typedef(line)
            # public enum TThostFtdcInvestorRangeType : byte
            # {
            # 	/// <summary>
            # 	///所有
            # 	/// </summary>
            # 	THOST_FTDC_IR_All = (byte)'1',
            # 	/// <summary>
            # 	///投资者组
            # 	/// </summary>
            # 	THOST_FTDC_IR_Group = (byte)'2',
            # 	/// <summary>
            # 	///单一投资者
            # 	/// </summary>
            # 	THOST_FTDC_IR_Single = (byte)'3'
            # }

            if line.find(' char ') > 0 and line.find('[') < 0:
                key = line.split(' ')[2][6:-2]  # TThostFtdcInvestorRangeType=>FtdcInvestorRangeType(去掉首个T)
                enum_line = self.enum_comment[key]
                enum_line += '\npublic enum TThost%s : byte\n{\n' % key
                for l in self.define:
                    enum_line += '\t%s\n' % l
                enum_line += '}\n\n'
                # 处理形如 102001此类值
                if enum_line.find("(byte)") < 0:
                    enum_line = enum_line.replace(': byte', ': int')

                self.fenum.write(enum_line)
            self.define.clear()

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
        # try:
        self.fenum.write('\n')

        self.fcpp = open(os.path.join(os.path.abspath(self.ctp_dir), 'ThostFtdcUserApiDataType.h'), 'r')
        for idx, line in enumerate(self.fcpp):
            l = self.process_line(idx, line)
            self.f_data_type.write(l)

        self.fcpp.close()
        self.f_data_type.close()
        self.fenum.close()

        print('ctp_data_type.py生成过程完成')
    # except:
    # print('data_type.py生成过程出错')


if __name__ == '__main__':
    import generate_cs as g
    for out_path in g.out_paths:
        Generate(g.ctp_path, out_path).run()
