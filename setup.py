from setuptools import setup
from os import path as os_path
import shutil

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        desc = f.read()
    return desc


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


if not os_path.exists('py_ctp/lib'):
    shutil.copytree('dll', 'py_ctp/lib')

long_description = read_file('README.md')
long_description_content_type = "text/markdown",  # 指定包文档格式为markdown

setup(
    name='py_ctp',  # 包名
    python_requires='>=3.4.0',  # python环境
    version='1.1.7',  # 包的版本
    description="Python CTP futures api",  # 包简介，显示在PyPI上
    long_description=long_description,  # 读取的Readme文档内容
    long_description_content_type=long_description_content_type,  # 指定包文档格式为markdown
    author="HaiFeng",  # 作者相关信息
    author_email='haifengat@vip.qq.com',
    url='https://github.com/haifengat/hf_ctp_py_proxy',
    # 指定包信息，还可以用find_packages()函数
    # packages=find_packages(),
    packages=['py_ctp'],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT License",
    platforms="any",
    data_files=['README.md'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
