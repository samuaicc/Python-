#-*-coding:utf-8-*-
#定义多个类
class Car():
    def __init__(self,manufacturer,model,year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.licheng_reading = 0
    def get_car_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    def read_licheng(self):
        print('当前已经行驶了' + str(self.licheng_reading) + '千米!')
    def update_licheng(self,mileage):
        if mileage >= self.licheng_reading:
            self.licheng_reading = mileage
        else:
            print('这不是插电动力！')
    def increment_licheng(self,miles):
        self.licheng_reading += miles
class Battery():
    def __init__(self,battery_size=60):
        self.battery_size = battery_size
    def describe_battery(self):
        print('全新锂电池容量:' + str(self.battery_size) + '千瓦时！')
    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
        message = '注意,当前电量够行驶' + str(range) + '千米!'
        print(message)
class ChadianCar(Car):
    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)
        self.battery = Battery(85)
        
        
