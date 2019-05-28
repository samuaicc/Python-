#-*-coding:utf-8-*-
#导入整个模块文件
'''
要想让函数变成可导入的
要先创建一个模块
模块是扩展名为'.py'的格式文件
在里面包含了要导入到程序中的代码
'''
#导入先前存的lainximokuai模块
import lianximokuai
lianximokuai.make(16,'黄油','芝士','虾')
lianximokuai.make(10,'黄油','牛肉')
#lianximokuai是模块名，make是模块中的函数名,更改函数名可以调用模块中的不同函数
#导入模块文件中的指定模块，如果多个模块就用逗号隔开不同模块名称,'*'可以导入所有函数名，但最好少用，防止函数覆盖或变量函数混淆
from lianximokuai import printinfo
printinfo(1,2,3,4,5)
printinfo(555,666,777)
#使用as制定函数别名
from lianximokuai import printinfo as samu
samu(1,11,111,1111)
samu(2,22,222,2222)
#使用as制定模块别名
import lianximokuai as lian
lian.printinfo(3,33,333,3333)
 
