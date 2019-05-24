#-*-coding:utf-8-*-
#方法1.python中没有switch语句但可以通过elif来实现
num = int(input("输如一个0到20的数字:"))
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print("输入的正合我心意")
else:
    print("输入的有点不合我心意")
print("---------华丽的分割线---------")
#方法2.实用字典实现
#定义一个字典（由键组对组成的集合），调用字典中的get()方法获取相应的表达式
x = int(input("输入x的值:"))
y = int(input("输入y的值:"))
operator = "*"       #设置operator(运算符)的初始值为"*"
result = {
    "+":x + y,     #当字典值为"+"是求x + y
    "-":x - y,
    "*":x * y,
    "/":x / y
}
print("x * y = %d"%result.get(operator))    #计算x*y的值

