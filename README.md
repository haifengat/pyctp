# hf_ctp_py_proxy
上期技术期货交易api之python封装，实现接口调用。支持windows linux.

## 环境需求
* VS2017
* python 3.6+

## 使用说明
* 运行 `pyton generate\\run.py` 生成所有文件
* C++编译
    * Windows
	
        * 环境要求 `vs2017`
        * 设置项目为x64,否则会提示找不到windows.h
        * 打开ctp_c\\ctp.sln
        * 编译ctp_quote 和 ctp_trade项目
        * 编译后生成的dll放在<red>py_ctp\lib32|lib64</red>目录下
		
		
vs2017编译如果提示:
error C1041: 无法打开程序数据库“xxx\vc141.pdb”(或者其他版本的vc)；如果要将多个 CL.EXE 写入同一个 .PDB 文件
请在项目ctp_quote点击右键，属性，设置：
1. “C/C++” --> "常规” -->”调试信息格式” 设置为 “C7 兼容(/Z7)”
2. “C/C++” --> "代码生成” -->”启用字符串池” 设置为 “是(/GF)”
3. “链接器” --> "调试” -->”生成调试信息” 设置为 “是(/DEBUG)”

如果编译提示找不到"windows.h"
请在项目ctp_quote点击右键，属性，设置：
常规->windows SDK版本->选择你已安装的windows_sdk版本，win 10的用win 10 sdk，win 8的用win 8 sdk，没有安装sdk的话，就去vs安装程序里安装

如果提示缺少vc141_xp.pdb云云，
请在项目ctp_quote点击右键，属性，设置：
常规->平台工具集，选择你有的工具集

ctp_trade项目，如上法同样设置

    * Linux
        * 设置系统语言为：zh_CN.UTF-8
        * 复制文件到linux ctp_c\\*.h *.cpp 到ctp_c目录下
        * 复制 ctp_20180109\\*.so到dll目录下
        * 复制 py_ctp\\*.py到py_ctp目录下
        * 进入dll目录，执行以下指令
            * g++ -shared -fPIC ../ctp_c/trade.cpp -o ./ctp_trade.so ./thosttraderapi.so
            * g++ -shared -fPIC ../ctp_c/quote.cpp -o ./ctp_quote.so ./thostmduserapi.so
* 测试
    * Python
        * 安装 `pip install py_ctp`
        * 运行 `python py_ctp\test_api.py`
    * C#
        * `copy cs_ctp\*.cs cs_ctp\ctp_test\`
        * 打开cs_ctp\ctp_test 项目进行调试
        * 打开cs_ctp\proxytest 项目测试.net封装

