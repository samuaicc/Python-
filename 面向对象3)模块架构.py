#-*-coding:utf-8-*-
#最基本的模块调用
import math #调用math模块 
from math import sqrt #调用math模块中的sqrt函数 
import math as sx  #调用math模块并重命名为sx

print('调用math.sqrt:',sx.sqrt(1))
print('直接调用sqrt:',sqrt(4))
print('调用sx.sqrt:',sx.sqrt(9))
#外部模块需要和引用程序在同一目录下
#练习导入我自己的lianximokuai中的make函数
from lianximokuai import make
make(12,'黄油','奶酪','牛肉')
'''
模块在运行后会在同目录文件夹中生成__pycache__文件
此文件是python在使用模块后自动生成的模块编译文件
有时可以发布此文件而不发布源文件，起到对源文件的保护
#编译指定的文件 将文件编译为字节码的形式，保护源文件
import py_compile  #调用系统内置模块
py_compile.compile('?.py','?.pyc')  #调用模块中的compile函数编译文件如果括号内没有第二个参数则会在目录中新建一个__pycache__的字节码文件
#除此之外还可以使用命令选项实现脚本编译
-O 编译后脚本以'pyo'的扩展名保存，对脚本的优化程度不大
-OO 对脚本的优化程度比较大，可以使脚本变的更小，但可能会导致运行出错
通过如下命令调用
python -O -m py_compile file.name
-m相当于import
'''
#使用__name__属性

