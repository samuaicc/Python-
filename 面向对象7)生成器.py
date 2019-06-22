#-*-coding:utf-8-*-
#yield 定义的函数是生成器，可以生成一个值序列用于迭代，使用一个再生成一个，节约内存
#生成器的运行机制:
'''
生成器是一个函数，而且函数的参数都可以保留
当迭代到下一次调用时，所使用的参数都是第一次保留的。
也就是说，在整个函数调用中的参数都是第一次调用时所保留的，而不是新建的
'''
#使用yield函数
def fib(max):
    a,b = 1,1
    while a < max:
        yield a
        a,b = b,a+b
if __name__ == '__main__':
    for n in fib(15):
        print(n)

#创建生成器
#演示生成器的运行机制
def shengchengqi(n):
    while n > 0:
        print('开始生成...')
        yield n
        print('完成一次...')
        n -= 1
if __name__ == '__main__':
    for i in shengchengqi(5):
        print('遍历得到的值：',i)
    print()
    shengcheng = shengchengqi(4)
    print('已经实例化生成器对象')
    shengcheng.__next__()
    print('第二次调用__next__()方法:')
    shengcheng.__next__()     #以手动方式获取序列值
#调用一个生成器
def shengyield(n):
    while n > 0:
        rcv = yield n
        n -= 1
        if rcv is not None:
            n = rcv
if __name__ == '__main__':
    sheng_yield = shengyield(2)
    print(sheng_yield.__next__())
    print(sheng_yield.__next__())
    print('传给生成器一个值，重新初始化生成器。')
    print(sheng_yield.send(11))  ######传给生成器一个新值
    print(sheng_yield.__next__())
#使用协程重置生成器序列
def xie():
    print('等待接受处理任务...')
    while True:
        data = (yield)
        print('收到任务:',data)
def producer():
    c = xie()
    c.__next__()
    for i in range(3):
        print('发送一个任务...','任务%d' % i)
        c.send('任务%d' % i)  #协程,配合的是yield的停止特性
if __name__ == '__main__':
    producer()
