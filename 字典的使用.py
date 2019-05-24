#-*-coding:utf-8-*-
#字典是无序性的
dict1 = {'name':'samu','age':18,'job':'student'}
#调用,访问字典的值
print(dict1['name'])
print(dict1['age'])
print(dict1['job'])
print(dict1.get('name'))
print(dict1.get('high'))
print(dict1.get('high','不存在'))  #get()方法若访问元素没有在字典中会输出None，还可以自定义返回
print(dict1.items())  #返回所有键值对
print(dict1.keys())   #返回所有键
print(dict1.values()) #返回所有值
#向字典中添加数据
dict2 = {'height':170,'salary':30000}
dict1['weight'] = 130
dict1['grade'] = 'dayi'
dict1.update(dict2)  #update()将另一个字典全部添加到旧字典中
print(dict1)
#修改字典的值，类似于添加数据
dict1['age'] = 19
dict1['grade'] = 'daer'
print(dict1)
#删除字典的元素
#del语句,pop(),clear()
del dict1['height']
b = dict1.pop('weight')  #pop()删除后可以保留值
dict2.clear()  #清空字典
print(dict1)
print(b)
print(dict2)
#popitem()可以随机删除删除并返回一个键值对
#创建空字典
dict3 = {}
dict4 = dict()
print(dict3,dict4)
#创建值为空的字典
dict5 = dict.fromkeys(['name','age','sex'])
print(dict5)
#创建值为相同的字典
dict6 = dict.fromkeys(['name','age','sex'],10)
print(dict6)
#和字典有关的内置函数
print('dict1的键对个数;',len(dict1))
print('输出字典dict1并以可打印的字符串表示:',str(dict1))
print('dict1的变量类型是;',type(dict1))
#遍历字典
for key1,value1 in dict1.items():  #遍历所有键和值
    print('key:',key1)
    print('value:',value1)
for key2 in dict1.keys():
    print('key:',key2)            #遍历所有键
for value2 in dict1.values():
    print('value:',value2)
#使用sorted()获得按特定顺序排列的键列表的副本并按序遍历所有键
for key3 in sorted(dict1.keys()):
    print('key:',key3.title())
#字典嵌套
#字典列表
stu = {'语文':100,'数学':98,'英语':100}
stu1 = {'语文':98,'数学':95,'英语':90}
stu2 = {'语文':96,'数学':91,'英语':80}
stus = [stu,stu1,stu2]
for name in stus:   #通过for遍历列表stus 
    print(name)
for i in range(len(stus)):
    print(stus[i].get('语文'))  #输出所有语文成绩
#字典中存储字典
users = {'仨木':{'初级密码':'666666',
               '中级密码':'888888',
               '电话':'123456789'},
         '小李':{'初级密码':'111111',
               '中级密码':'222222',
               '电话':'12345222001'},
         }
for username,message in users.items():
    print('用户名:'+username)
    password = message['初级密码'] + ' ' + message['中级密码']
    pnum = message['电话']
    print('组合密码:',password.title())
    print('电话:',pnum.title())
#在字典中存储列表
#面馆点餐系统
menu = {}
list = []
mian = str(input('你吃什么面?:'))
i = 0
while i == 0:
    yaoqiu = str(input("你有什么附加要求？没有按'N':"))
    if yaoqiu == 'N':
        break
    else:
        list.append(yaoqiu)
menu['面条种类'] = mian
menu['附加条件'] = list
print('你点了一份:',menu['面条种类'],'你提出了如下要求:')
for topping in menu['附加条件']:
    print('\t',topping)
#使用其他内置方法
#copy()复制
dict7 = dict1.copy()
print(dict7)
#setdefault()获取指定键值,与get()类似如果键不在字典中则会添加键并把值设为默认'None'
print(dict1.setdefault('name',None))
print(dict1.setdefault('sex',None))  #因为现dict1字典中没有sex，所以返回None,并会在原字典中添加'sex':'None'键值对
print(dict1)

