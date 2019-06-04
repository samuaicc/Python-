#-*-coding:utf-8-*-
#定义子类
class Car():    #定义一个基类(父类)
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
class BMW(Car):  #定义子类(派生类)
    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)       #关联父类和子类，调用父类的方法super()
        self.battery_size = ''    #定义子类中的新属性
    def motor(self):        #定义子类中的新方法
        print('该车的发动机是:' + str(self.battery_size))
BMWtest = BMW('BMW','7x',2017)
print(BMWtest.get_descriptive_name())
BMWtest.motor()
#子类可以继续派生新类
class BMW1(Car):  #定义新子类(派生类)
    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)
        self.Motor = Motor()
class Motor(BMW1):   #基于新子类定义一个子类
    def __init__(self,Motor_size = 60):  #设置形参默认为60
        self.Motor_size = Motor_size
    def print_motor(self):
        print('这款汽车的发动机参数是:' + str(self.Motor_size) + '  ' + '6缸 3.0T 225kw')
BMW1test = BMW1('BMW','5x',2015)
print(BMW1test.get_descriptive_name())
BMW1test.Motor = Motor(90)    #修改形参值，否则默认为60
BMW1test.Motor.print_motor()
#私有属性和私有方法
'''
当子类继承了父类之后，虽然子类可以具有父类的属性和方法，但是父类中的私有属性和方法不能继承，
在子类中还可以使用(重写)的方法来修改父类的方法，以实现与父类不同的行为表现或能力
class A:
    def __init__(self):
        self.__name = 'samu'
        self.age = 18
class B(A):
    def sayName(self):
        print(self.__name)
b = B()
b.sayName()  #会报错，因为B调用不了A中的私有属性self.__name
'''
#多重继承  一个子类可以继承多个父类，父类在（）内使用逗号隔开
class PrntOne:
    namea = 'PrntOne'
    def set_value(self,a):
        self.a = a
    def set_namea(self,namea):
        PrntOne.namea = namea
    def info(self):
        print('PrntOne:%s,%s'%(PrntOne.namea,self.a))
class PrntSecond:
    nameb = 'PrntSecond'
    def set_nameb(self,nameb):
        PrntSecond.nameb = nameb
    def info(self):
        print('PrntSecond:%s'%(PrntSecond.nameb,))
class Sub(PrntOne,PrntSecond):
    pass
class Sub2(PrntSecond,PrntOne):
    pass
class Sub3(PrntOne,PrntSecond):
    def info(self):
        PrntOne.info(self)
        PrntSecond.info(self)
print('使用第一个子类：')
sub = Sub()
sub.set_value('11111')
sub.info()
sub.set_nameb('22222')
sub.info()
print('使用第二个子类：')
sub2 = Sub2()
sub2.set_value('33333')
sub2.info()
sub2.set_nameb('44444')
sub2.info()
print('使用第三个子类：')
sub3 = Sub3()
sub3.set_value('55555')
sub3.info()
sub3.set_nameb('66666')
sub3.info()
#方法重写
class Wai:
    def __init__(self,x = 0,y = 0,color = 'black'):
        self.x = x
        self.y = y
        self.color = color
    def haijun(self,x,y):
        self.x = x
        self.y = y
        print('鱼雷就绪!')
        self.info()
    def info(self):
        print('定位(%d,%d)'%(self.x,self.y))
    def gongji(self):
        print('发射导弹!')
class FlyWai(Wai):
    def gongji(self):    #在子类中重写方法gongji()
        print('飞船拦截!')
    def fly(self,x,y):
        print('火箭军...')
        self.x = x
        self.y = y
        self.info()
flyWai = FlyWai(color='red')
flyWai.haijun(100,220)
flyWai.fly(12,15)
flyWai.gongji()  #会调用在子类中重写的方法gongji()
