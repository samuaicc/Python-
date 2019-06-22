#-*-coding:utf-8-*-
#使用包
'''
包就是一个文件夹或目录
里面存放的是许多个模块
但包内必须包含一个名为__init__的文件，此文件可以为空文件
此外还可以使用包的嵌套
'''
#创建并使用包
#创建包的最简单方法为放一个空的__init__文件，这个文件中也可以包含一些初始代码或为变量__all__赋值
#我创建的是pckage包，用来练习使用,已放在同目录的pckage文件夹中
import pckage
import pckage.tt
print('输出包pckage中的全局变量:',pckage.name)
print('调用包pckage中的函数：',end = '\n')
pckage.pck_test_fun()
pckage.tt.tt()
