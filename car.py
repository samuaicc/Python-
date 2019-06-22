#-*-coding:utf-8-*-
#此类用于{面向对象5)导入类}程序文件进行导入演示
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
