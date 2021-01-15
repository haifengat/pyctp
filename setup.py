from setuptools import setup
import os
from os import path as os_path

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    desc = ''
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        desc = f.read()
    return desc


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

# 删除无用文件
path = f'./py_ctp/lib64'
for f in os.listdir(path):
    if os.path.isdir(f):
        continue
    if os.path.splitext(f)[1] not in ['.dll', '.so']:
        os.remove(f'./py_ctp/lib64/{f}')

long_description = read_file('setup.md')

# 生成requirements.txt pipreqs --encoding=utf8 --force py_ctp
# rm dist -rf && python setup.py sdist && twine upload dist/*         //.tar.gz
# pip install --upgrade setuptools wheel keyring
# python setup.py bdist_wheel && twine upload dist/*   //.whl
setup(
    name='py_ctp',  # 包名
    python_requires='>=3.6.0',  # python环境
    version='v6.5.1.0115',
    description="Python CTP futures api",  # 包简介，显示在PyPI上
    long_description=long_description,  # 读取的Readme文档内容
    long_description_content_type = "text/markdown",  # 指定包文档格式为markdown
    author="HaiFeng",  # 作者相关信息
    author_email='haifengat@vip.qq.com',
    url='https://github.com/haifengat/hf_ctp_py_proxy',
    # library_dirs = ['/usr/lib'],
    # extra_link_args.append（'-Wl，-rpath，'+ lib_path）
    # 指定包信息，还可以用find_packages()函数
    # packages=find_packages(),
    packages=['py_ctp'],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT License",
    platforms="any",
    # data_files=['README.md', ('/usr/lib/py_ctp', ['py_ctp/lib64/thostmduserapi_se.so', 'py_ctp/lib64/thosttraderapi_se.so'])],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
