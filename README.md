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
    * Linux
        * 设置系统语言为：zh_CN.UTF-8
        * 复制文件到linux ctp_c\\*.h *.cpp 到ctp_c目录下
        * 复制 ctp_20180109\\*.so到dll目录下
        * 复制 py_ctp\\*.py到py_ctp目录下
        * 进入dll目录，执行以下指令
            * g++ -shared -fPIC ./trade.cpp -o ./ctp_trade.so ./thosttraderapi_se.so ./LinuxDataCollect.so
            * g++ -shared -fPIC ./quote.cpp -o ./ctp_quote.so ./thostmduserapi_se.so
* 测试
    * Python
        * 安装 `pip install py_ctp`
        * 测试代码 https://pypi.org/project/py-ctp/
    * C#
        * `copy cs_ctp\*.cs cs_ctp\ctp_test\`
        * 打开cs_ctp\ctp_test 项目进行调试
        * 打开cs_ctp\proxytest 项目测试.net封装

