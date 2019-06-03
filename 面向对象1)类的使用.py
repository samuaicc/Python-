#-*-coding:utf-8-*-
#定义并使用类
#在面向对象的编程语言中，具有相同属性的模型是使用类进行定义和表示的
#定义类'class Classname'
#类的基本用法，类必须实例化才能使用，类似于调用函数
class MyClass:            #定义类
    '这是一个类。'
myclass = MyClass()       #实例化类
print('输出类的说明:')
print(myclass.__doc__)    #显示类属性
print('显示类帮助信息:')
help(myclass)
#类对象
class Myclass:
    i = 123456     #定义变量i的初始值
    def f(self):   #定义类方法f()
        return 'hello world'
x = Myclass()
print('类Myclass中的属性i为:',x.i)
print('类Myclass中的方法f输出为:',x.f())
#类方法
class Smplclass:
    def info(self):
        print('This is my class')
    def mycacl(self,x,y):
        return x + y
sa = Smplclass()
sa.info()  #调用实例对象中的info()类方法
print(sa.mycacl(55,12))    #调用实例对象中的mycacl()类方法
#__init__方法
class Complex:
    def __init__(self,part1,part2):
        self.p1 = part1
        self.p2 = part2
x = Complex(3,-1)
print(x.p1,x.p2)
#类方法调用 类中的方法既可以调用自身的方法也可以调用全局函数来实现相关功能
def diao(x,y):
    return (abs(x),abs(y))   #abs() 返回一个数的绝对值
class Ant():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.d_point()     #调用内部方法d_point() 
    def yi(self,x,y):
        x,y = diao(x,y)    #调用全局diao()
        self.e_point(x,y)  #调用内部方法e_point()
        self.d_point()     #调用内部方法d_point()
    def e_point(self,x,y):
        self.x += x
        self.y += y
    def d_point(self):
        print('\n当前位置是({0},{1})'.format(self.x,self.y))
ant_a = Ant() 
ant_a.yi(2,7)
ant_a.yi(-5,6)
#创建多个实例
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def wang(self):
        print(self.name.title() + '  ' + '汪汪')
    def shen(self):
        print(self.name.title() + '  ' + '伸舌头')
my_dog = Dog('小财',6)
you_dog = Dog('大旺',3)
print('\n我的爱犬的名字是:' + my_dog.name.title())
print('我的爱犬' + str(my_dog.age) + '岁了')
my_dog.wang()
my_dog.shen()
print('\n你的爱犬的名字是:' + you_dog.name.title())
print('你的爱犬' + str(you_dog.age) + '岁了')
you_dog.wang()
you_dog.shen()
#使用私有方法   '__'加上名称表私有方法
class Site:
    def __init__(self,name,email):
        self.name = name
        self.__email = email
    def who(self):
        print('name:' + '  ' + self.name)
        print('email:' + '  ' + self.__email)
    def __foo(self):
        print('这是私有方法')
    def foo(self):
        print('这是公共方法')
        self.__foo()
x = Site('仨木','samuaicc999@gmail.com')
x.who()
x.foo()
#x.__foo() 为内部方法，外部不可调用，否则会报错
#析构方法__del__()
class NewClass():
    num_count = 0
    def __init__(self,name):
        self.name = name
        NewClass.num_count += 1
        print(self.name,'  ',NewClass.num_count)
    def __del__(self):
        NewClass.num_count -= 1
        print('del',' ',self.name,NewClass.num_count)
    def test():
        print('aa')
aa = NewClass('samu')
bb = NewClass('nihao')
cc = NewClass('aicc')
del aa
del bb
del cc
print('over')
#静态方法和类方法
class Jing():
    def __init__(self,x = 0):
        self.x = x    #定义类属性
    @staticmethod     #使用静态方法装饰器d()
    def static_method():
        print('此处调用了静态方法!')
    @classmethod      #使用类方法装饰器
    def class_method(cls):  #定义类方法，默认参数是cls
        print('此处调用了类方法!')
Jing.static_method()  #没有实例化类通过类名调用静态方法
Jing.class_method()   #没有实例化类通过类名调用类方法
dm = Jing()           #实例化类
dm.static_method()    #通过类实例调用静态方法
dm.class_method()     #通过类实例调用类方法
#类的专有方法
#详见书本P130
#类属性    属性就是指的类中定义的变量
#类属性和实例属性
class X_property():
    class_name = 'x_property'   #设置类属性   
    def __init__(self,x = 0):
        self.x = x              #设置实例属性
    def class_info(self):
        print('类变量值:',X_property.class_name)
        print('实例变量值:',self.x)
    def change(self,x):
        self.x = x                     #修改实例属性
    def change_cn(self,name):
        X_property.class_name = name   #修改类属性
aaa = X_property()   #实例化类
bbb = X_property()
print('初始化两个实例')
aaa.class_info()
bbb.class_info()
print('修改实例变量')
print('修改aaa实例变量')
aaa.change(3)
aaa.class_info()
bbb.class_info()
print('修改bbb实例变量')
bbb.change(10)
aaa.class_info()
bbb.class_info()
print('修改类变量')
print('修改aaa类变量')
aaa.change_cn('xiuer')
aaa.class_info()
bbb.class_info()
print('修改bbb类变量')
bbb.change_cn('samu')
aaa.class_info()
bbb.class_info()
'''
对于实例属性来说，两个实例相互之间并不联系，可以各自独立修改为不同的值。
而对于类属性来说，无论哪个实例修改了它，都会导致所有实例的类属性值发生变化。
是例属性就类似于局部变量，而类属性类似于全局变量。
'''
#设置属性的默认值
class Car():
    def __init__(self,manufacturer,model,year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print('本车的行驶里程为:',str(self.odometer_reading),'千米!')
my_car = Car('TOYOTA','LandCruiser','2018')
print(my_car.get_descriptive_name())
my_car.read_odometer()
#修改属性的值
my_car.odometer_reading = 15   #直接通过实例修改
my_car.read_odometer()
#自定义方法修改属性的值
class Car1():
    def __init__(self,manufacturer,model,year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    def up_odometer(self,mileage):      #自定义方法修改属性的值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('这是一个不合理的数据！')
    def read_odometer(self):
        print('本车的行驶里程为:',str(self.odometer_reading),'千米!')
my_car1 = Car1('Benz','G500','2018')
print(my_car1.get_descriptive_name())
my_car1.up_odometer(-1)
my_car1.read_odometer()
#通过递增修改属性，在自定义方法中设置递增，然后逐步调用方法修改属性，与上一个类似
#使用私有属性，与私有方法类似，也是使用”__+属性名“定义私有属性,只供类内部调用
class Person():
    def __init__(self,name,age):
        self.__name = name   #定义私有属性
        self.age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.age
person = Person('samu',18)
print('姓名:',person.get_name())
print('年龄:',person.get_age())

