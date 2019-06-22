#-*-coding:utf-8-*-
#使用for循环遍历迭代器
list = [0,1,2,3,4]
it = iter(list)   #创建迭代对象
for i in it:      #遍历迭代器中的对象
    print(i,end = '\n')  #显示迭代结果
#创建迭代器
class Use:
    def __init__(self,x=2,max=50): 
        self.__mul,self.__x = x,x
        self.__max = max
    def __iter__(self):      #定义迭代器的协议方法
        return self          #返回类的自身
    def __next__(self):
        if self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__max:
                return self.__mul            
            else:
                raise StopIteration
        else:
            raise StopIteration

my = Use(2,100)    #该迭代器的作用是返回x在一定范围内的n次方
for i in my:
    print('迭代的数据元素为:',i)
'''
使用内置迭代器函数iter()的两种方法
iter(iterable)  iterable为可迭代的类型，也可以是各种序列类型
iter(callable,sentinel)   callable表示可调用类型，一般为函数，sentinel为标记，是指引发函数结束的条件
'''
#演示第二种iter()函数方法
class Counter:
    def __init__(self,x = 0):
        self.x = x
counter = Counter()
def used_iter():
    counter.x += 2
    return counter.x
for i in iter(used_iter,12):
    print('遍历当前的数值',i)
#使用其他内置迭代器方法
#主要包括两大迭代器方法，分别是无限迭代和处理输入序列迭代器
#使用groupby()遍历数据
from itertools import *    #导入itertools中的所有模块
def height_class(h):
    if h > 182:
        return 'tall'
    elif h < 160:
        return 'short'
    else:
        return 'middle'
friends = [191,158,166,170,183,182,167,190]
friends = sorted(friends, key = height_class)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(tuple(n))
