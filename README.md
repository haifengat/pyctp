# hf_ctp_py_proxy
上期技术期货交易api之python封装，实现接口调用。支持windows linux.

## 使用说明
* 运行generate\run.py生成所有文件
* C++编译
    * Windows
        * 环境要求 `vs2017` `64位`
        * 设置项目为x64,否则会提示找不到windows.h
        * 打开ctp.sln
        * 编译ctp_quote 和 ctp_trade项目
        * 编译后生成的dll放在dll目录下
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
        * 运行 `python py_ctp\test_api.py`
    * C#
        * 复制 ctp_20180109\\*.dll 到dll目录下
        * 复制cs_ctp\\*.cs 到目录 cs_ctp\test_ctp  cs_ctp\proxy
        * 打开cs_ctp\test_ctp 项目进行调试
        * 打开cs_ctp\proxy 编译.net封装
        * 打开cs_ctp\proxy_test 测试.net封装

