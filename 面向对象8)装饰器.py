#-*-coding:utf-8-*-
'''
装饰器可以给函数或类增强功能
可以快速的给不同的函数或类插入相同的功能
绝对意义上讲装饰器是一种代码实现方式
@装饰器名称 ---创建装饰器
'''
#使用装饰器装饰函数
def zz(fun):  #定义一个装饰器函数
    def wrapper(*args,**bian):  #定义一个包装器函数
        print('开始运行....')
        fun(*args,**bian)   #使用被装饰函数
        print('运行结束....')
    return wrapper
@zz #使用装饰器装饰函数
def bianli(x):
    l = []
    for i in range(x):
        l.append(i)
    print(l)
@zz  #使用装饰器装饰函数
def hello(name):
    print('Hello',name)
if __name__ == '__main__':
    bianli(10)
    print('*********')
    hello('Samu')
#使用装饰器装饰带参函数
'''
当对带参数的函数进行装饰时
内嵌包装函数的形参和返回值与原函数相同
装饰函数返回内嵌包装函数对象
'''
def deco(func):
    def _deco(a,b):
        print('在函数myfunc()之前被调用。')
        ret = func(a,b)
        print('在函数myfunc()之后被调用,结果是:%s'%ret)
        return ret
    return _deco
@deco
def myfunc(a,b):
    print('函数myfunc(%s,%s)被调用！'%(a,b))
    return a + b
if __name__ == '__main__':
    myfunc(1,2)
    myfunc(3,4)
#使用装饰器装饰类（首先定义内嵌类中的函数然后返回新类）
def zzb(myclass):
    class InnerClass:
        def __init__(self,z=0):
            self.z = z
            self.wrapper = myclass() #实例化被装饰的类
        def position(self):
            self.wrapper.position()
            print('z轴坐标：',self.z)
    return InnerClass  #返回新定义的类
@zzb
class Coordination:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def position(self):
        print('x轴坐标：',self.x)
        print('y轴坐标：',self.y)
if __name__ == '__main__':
    coor = Coordination()
    coor.position()
