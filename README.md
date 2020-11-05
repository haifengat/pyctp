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
        * 编译后生成的dll放在 `py_ctp\lib32|lib64` 目录下
    * Linux
        * 设置系统语言为：zh_CN.UTF-8
        * 复制 ctp_20180109\\*.so到 `py_ctp/lib64` 目录下
        * 进入 `py_ctp/lib64` 目录，执行以下指令, -Wl,rpath=指定so路径(需要与setup.py中的data_files配合使用)
            * cd py_ctp/lib64/ && \cp ../../v6.3.15_20190220/*.so . && g++ -shared -fPIC -Wl,-rpath /usr/lib/py_ctp -o ./ctp_trade.so ../../ctp_c/trade.cpp thosttraderapi_se.so && g++ -shared -fPIC -Wl,-rpath /usr/lib/py_ctp -o ./ctp_quote.so ../../ctp_c/quote.cpp  thostmduserapi_se.so
* 测试
    * Python
        * 安装 
        ```python
        pip install --no-binary :all: py-ctp==6.3.15
        pip install --no-binary :all: py-ctp==6.3.16
        ```
        * 测试代码 https://pypi.org/project/py-ctp/
    * C#
        * `copy cs_ctp\*.cs cs_ctp\ctp_test\`
        * 打开cs_ctp\ctp_test 项目进行调试
        * 打开cs_ctp\proxytest 项目测试.net封装

* 代码管理
    ```bash
    eval `ssh-agent`
    ssh-add /home/code/gitee_rsa
    git push gitee
    ```
## 更新
### 20201104
更新:接口更新到6.3.16;不再支持32位; 解决lnx下so路径问题;解决合约过多导致的bug;
连接simnow，须用官方6.3.15的文件覆盖lib64下同名文件
## 安装
pip install --no-binary :all: py-ctp
