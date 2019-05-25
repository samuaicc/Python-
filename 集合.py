#-*-coding:utf-8-*-
#集合的基本功能是进行成员关系运算并删除重复元素
#创建集合
jianli = {'name','age','job'}
print(jianli)
a = ['a','b','c','d']
b = set(a)
print(b)
#创建空集合
e = set()  #{}不能用来创建空集合
print(e)
#添加删除元素和清空集合
#添加add()
b.add('e')
print(b)
b.add('a')   #集合是元素不可重复的因此'a'添加不到b中
print(b)
#删除remove()
jianli.remove('job')
print(jianli)
#clear()清空集合
jianli.clear()
print(jianli)
#进行成员关系运算
if 'a' in b:
    print("'a'在集合b中")
else:
    print("'a'不在集合b中")
#集合的并集，交集，差集等运算
c = set('abcdef')
print(c - b)  #c和b的差集c.difference(b)
print(c & b)  #c和b的交集c.intersection(b)
print(c | b)  #c和b的并集c.union(b)
print(c ^ b)  #c和b的不同时存在的元素
