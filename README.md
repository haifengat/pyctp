# hf_ctp_py_proxy
上期技术期货交易api之python封装，实现接口调用。支持windows linux.

## 使用说明
* 设置系统语言为：zh_CN.UTF-8
* 把源码中的文件复制到目标计算机上
* 进入py_ctp/dll目录，执行以下指令
    * `g++ -shared -fPIC ../../ctp_c/trade.cpp -o ./ctp_trade.so ./thosttraderapi.so`
	* `g++ -shared -fPIC ../../ctp_c/quote.cpp -o ./ctp_quote.so ./thostmduserapi.so`
* 进入py_ctp目录，运行 `python test_api.py`

* Linux以下代码可存入 xxx.sh，再`chmod 777 xxx.sh`，直接执行xxx.sh 实现编译
``` c
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
cd "$DIR/dll"
pwd
g++ -shared -fPIC ../../ctp_trade/trade.cpp -o ./ctp_trade.so ./thosttraderapi.so
g++ -shared -fPIC ../../ctp_quote/quote.cpp -o ./ctp_quote.so ./thostmduserapi.so
```
