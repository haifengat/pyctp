# hf_ctp_py_proxy

上期技术期货交易 api 之 python 封装，实现接口调用。支持 windows linux.

## 环境需求

- VS2017
- python 3.6+

## 使用说明

- 运行 `pyton generate\\run.py` 生成所有文件
- C++编译
  - Windows
    - 环境要求 `vs2017`
    - 设置项目为 x64,否则会提示找不到 windows.h
    - 打开 ctp_c\\ctp.sln
    - 编译 ctp_quote 和 ctp_trade 项目
    - 编译后生成的 dll 放在 `py_ctp/lib64` 目录下
  - Linux
    - 设置系统语言为：zh_CN.UTF-8
    - 执行以下指令, -Wl,rpath=指定 so 路径(需要与 setup.py 中的 data_files 配合使用)
      - export VERSION=**v6.5.1**
        1. 代码生成
           ```bash
           pip3 uninstall py-ctp -y && python generate/run.py $VERSION
           ```
        2. 编译 so
           ```bash
           cd py_ctp/lib64 && \
           \cp ../../$VERSION/lnx/*.so . \
           && g++ -shared -fPIC -Wl,-rpath . -o ./ctp_trade.so ../../ctp_c/trade.cpp thosttraderapi_se.so \
           && g++ -shared -fPIC -Wl,-rpath . -o ./ctp_quote.so ../../ctp_c/quote.cpp  thostmduserapi_se.so \
           && cd ../..
           ```
        3. 测试
           ```bash
           sed -i "s#version=.*#version='$VERSION.`date '+%Y%m%d'`',#g" setup.py && \
           python setup.py install && python test_trade.py
           ```
        4. 上传
           ```bash
           pip install wheel twine setuptool setuptools_rust
           python setup.py sdist && twine upload -u haifengat dist/*$VERSION.`date '+%Y%m%d'`*.gz && \
           python setup.py bdist_wheel && twine upload -u haifengat dist/*$VERSION.`date '+%Y%m%d'`*.whl
           ```

## 更新

### 20201104

更新:接口更新到 6.3.15;不再支持 32 位; 解决 lnx 下 so 路径问题;解决合约过多导致的 bug;

### 20210115

更新：接口更新到 6.5.1;大商所非交易合约数量庞大导致的问题。

### 20220504

更新: 重新编译封装的 C 接口, trade 登录不再需要 productInfo
