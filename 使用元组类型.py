#-*-coding:utf-8-*-
'''
使用元组
元祖可以看做一种特殊的列表，
唯一与列表不同的是元组内的数据元素不能发生改变
不仅不能改变其中的数据项还不能添加和删除数据项
当开发者需要创建一组不可改变的数据时
通常会把这些数据放在一个元组中
元组也可以嵌套
'''
tup1 = ('google','huawei',1991,1120)
tup2 = (1,2,3,4,5,6,7,8)
print(tup1[0])
print(tup2[1:5])   #截取元祖
for elements in tup1:  #for循环遍历元组
    print(elements)
'''
python 中的元组与字符串相同
元组之间可以用'+''*'进行运算
这就意味着可以对元组进行组合和复制
运算后会生成一个新元组
len()                 计算元素个数、元组长度
() + ()               连接
() * int num          复制
element in ()         判断元素是否存在
for x in (): print()  迭代
'''
tup3 = tup1 + tup2
print(tup3)
print((tup2)*2)
#元组的解包，两边个数必须一致
a,b,c,d = tup1
print(a,b,c,d)
#修改元组变量值，重新给储存元组的变量赋值，达到修改元祖的目的
tup1 = (1,11,111,1111)
print(tup1)
#不能删除元组中的一个元素但可以使用del语句删除整个元组
del tup3  #删除tup3
#将元组转化列表
print(list(tup1))
list1 = [1,2,22,222]
print(tuple(list1))
#元组索引和截取，上面已经提到
#使用内置方法操作元组
print(max(tup1))  #返回最大值
print(min(tup1))  #返回最小值
print(len(tup1))

