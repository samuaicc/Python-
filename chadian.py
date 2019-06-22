#-*-coding:utf-8-*-
from car import Car
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
        self.battery = Battery()
