#-*-coding:utf-8-*-
'''
命名空间，就是一个字典，键就是变量，值就是变量的值。
命名空间是一个容器，这个容器中可以装许多标识符，不同容器中，同名标识符互不冲突。、
命名空间用来记录变量的轨迹
'''
#locals()函数可以获取当前作用域的命名空间。
s = 1
str = 'sdsdd'
dict1 = {'name':'samu','age':18}
def sum(a,b):
    c = 0
    d = a + b + c
    #locals()获取局部命名空间
    scope = locals()
    #全局不能窥探内部的命名空间，但是内部可以使用globals()获取全局命名空间
    globals_scope = globals()
    #命名空间就是一个字典，甚至可以使用添加key-value的方式添加变量到作用域，但一般不建议这样做
    scope['e'] = 'sa'  #通过locals()添加的函数是只读的不能实际使用和修改，而globals()添加的函数不是只读的
    print(scope)
    print(globals_scope)
    return d
print(sum(1,2))
#locals()获取全局命名空间
print(locals())
print(globals())

