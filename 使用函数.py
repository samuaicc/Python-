#-*-coding:utf-8-*-
#函数基础
'''
在使用函数前应声明函数，然后才能调用
在使用函数时只需要按照函数定义的形式向函数传递必要的参数就可以调用函数完成相应的
功能或者获得函数返回的结果
关键字def可以定义一个函数
'''
#定义函数
def name() :   #定义一个函数name()的作用是输出'Samu'
    print('Samu')
name()
#调用函数
def sum( T ):      #定义一个函数sum()
    result = 0   
    for i in T:
        result += i  #函数语句:计算T中各个数据的和
    return result    #定义返回的是计算后的result
print(sum((1,2,3,4,5))) #T是一个参数，所以要计算多个数字就要用元组
#函数的参数
#形参和实参
#在上面的例子代码中T就是形参而下面的（1,2,3,4）就是实参
#形参表示函数完成一项工作所需的一项信息,实参是调用函数是传递给函数的信息
#正式实参类型--必须参数  也称为位置实参，在调用函数时，必须以正确的顺序传入参数，参数的数量必须与声明时一样
def print1(str):
    print(str)
    return
print1('lll')     #如果没有参数运行时就会报错因为参数的数量没有与声明时一样
#正式实参形式--关键字参数  在调用函数时，不必要以正确的顺序传入参数，因为解释器会根据参数名匹配参数值
def print2(name,age):
    print('名字:',name)
    print('年龄:',age)
    return
print2(age=18,name='samu')
#正式实参形式--默认参数   在调用函数时如果没有传递参数则会使用默认参数（也称为默认值参数）
def print2(name,age=18):
    print('名字:',name)
    print('年龄:',age)
    return
print2(name='aicc',age=20)
print2(name='samu')       #因为没有传递age所以就使用默认参数
#如果在声明一函数的参数是既有包含默认值的参数又有不包含默认值的参数就要先声明不包含默认值的参数
#正式实参形式--不定长参数  带有一个*号的参数是可变数量参数
def printinfo(arg1,*vartuple):
    print('输出:')
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(20,30,40,50)  #先单个输出的20，然后将30,40,50列在一个元组中进行for语句循环输出
#按值传递参数和按引用传递参数
def changeme(mylist):
    mylist.append([1,2,3,4])
    print('函数内取值:',mylist)
    return
list = [5,6,7,8]
changeme(list)
print('函数外取值:',list)    #调用函数的实参发生了改变，即使没有套用函数
#函数的返回值
#返回一个简单值
def get_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()   #定义返回值为full_name并使字符首字母大写
name = get_name('li','samu')   #调用函数
print(name)   
#可选实参
def get_name(first_name,last_name,middle_name=''):    #定义一个中间名为空字符串,如果有中间名就会输出，否则作为空字符串输出
    full_name = first_name + ' ' + middle_name + last_name
    return full_name.title()   #定义返回值为full_name并使字符首字母大写
name = get_name('li','aicc','samu')   #调用函数
print(name)
#返回一个字典,return可以返回任意类型的值
def person(first_name,last_name,age=''):
    person = {"first_name":first_name,"last_name":last_name}
    if age:          #python中空字符串解读为true
        person['age'] = age
    return person   
persondict = person('li','samu',age=18)   
print(persondict) 
#变量的作用域
def myfun():
    a = 0     #声明变量名a
    a += 1
    print('函数内a:')
a = 'samu'      #函数外给a赋值
print('全局作用变量a:',a)   #显示函数外赋值的a
myfun()                     #显示函数内赋值的a
print('全局作用变量a:',a)   #再次显示函数外赋值的a,与函数内的a互不影响,但要是将函数外的a作为参数引入函数就会改变
#global调用函数外变量到函数中
def myfun():
    global a   #global使函数内的变量a变为全局变量a的值
    a = 0     #声明变量名a
    a += 1
    print('函数内a:',a)
a = 'samu'      #函数外给a赋值
print('全局作用变量a:',a)   #显示函数外赋值的a
myfun()                     #显示函数内赋值的a
print('全局作用变量a:',a)   #此时函数外a就发生了变化,变为了函数内的a
#使用函数传递列表
def users(names):
    for name in names:
        message = 'hello,' + name.title() + '!'
        print(message)
username = ['sa mu','ai cc','xiu er']
users(username)
#在函数中修改列表
def copy(list1,list2):       #list1是被复制的列表,list2是接受复制的列表
    while list1:
        name = list1.pop()
        print('复制好友:',name)
        list2.append(name)
def copylist(list2):
    print('以下好友已经成功被复制到list2')
    for names in list2:
        print(names)
list1 = ['ji er','xiu er','ca ji']
list2 = []
copy(list1,list2)
copylist(list2)
#使用lambdac创建匿名函数
sum1 = lambda arg1,arg2: arg1 + arg2  
print(sum1(1,2))
print(sum1(10,25))

