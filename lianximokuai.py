#-*-coding:utf-8-*-
def make(size,*toppings):
    print('制作一个{0}寸的披萨要用到的配料:'.format(size))
    for topping in toppings:
        print('-',topping)
def printinfo(arg1,*arg2):
    print('依次输出:')
    print(arg1)
    for value in arg2:
        print(value)
    return
        
