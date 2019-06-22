#-*-coding:utf-8-*-
#Python中为了使程序文件更简洁，会将类单独放在一个模块中，在其他程序中导入使用
#在同目录中创建类来进行导入引用
#我创建car.py,duo.py,chadian.py
#只导入一个类
from car import Car
my_new_car = Car('TOYOTA','Land cruiser',2018)
print(my_new_car.get_car_name())
my_new_car.licheng_reading = 15
my_new_car.increment_licheng(19)
my_new_car.read_licheng()
#导入指定模块
from duo import ChadianCar
my_new_diancar = ChadianCar('Tesla','Modle',2019)
print(my_new_diancar.get_car_name())
my_new_diancar.battery.describe_battery()
my_new_diancar.battery.get_range()
#导入多个类
from duo import Car,ChadianCar
my_car = Car('Benz','G500',2017)
print(my_car.get_car_name())
my_battery = ChadianCar('BYD','唐',2018)
print(my_battery.get_car_name())
#导入整个模块
import duo
my_car = duo.Car('Benz','E300L',2017)
print(my_car.get_car_name())
my_battery = duo.ChadianCar('BYD','元',2019)
print(my_battery.get_car_name())
#在一个模块中导入另一个模块
from car import Car
from chadian import ChadianCar
my_car = Car('Benz','G500',2017)
print(my_car.get_car_name())
my_battery = ChadianCar('BYD','唐',2018)
print(my_battery.get_car_name())
