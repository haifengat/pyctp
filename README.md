# hf_ctp_py_proxy
上期技术期货交易api之python封装，实现接口调用。支持windows linux.

## 使用说明
* 运行generate\run.py生成所有文件
* C++编译
    * Windows
        * 设置项目为x64,否则会提示找不到windows.h
        * 编译后生成的dll放在dll目录下
    * Linux
        * 设置系统语言为：zh_CN.UTF-8
        * 复制文件到linux ctp_c\*.h *.cpp 到ctp_c目录下
        * 复制 ctp_20180109\*.so到dll目录下
        * 复制 py_ctp\*.py到py_ctp目录下
        * 进入dll目录，执行以下指令
            * g++ -shared -fPIC ../ctp_c/trade.cpp -o ./ctp_trade.so ./thosttraderapi.so
            * g++ -shared -fPIC ../ctp_c/quote.cpp -o ./ctp_quote.so ./thostmduserapi.so
        * 进入py_ctp目录，运行 `python test_api.py`

