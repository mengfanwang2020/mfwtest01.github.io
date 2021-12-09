'''
类 class
方法中有self
'''
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + "蹲下")
#
# my_dog = Dog("1", 12)
# print(my_dog.name)
# my_dog.sit()

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return str(self.year) + " " + self.make + " " + self.model

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super.__init__(make, model, year)
        self.battery_size
'''
导入类 如上
from car import Car, ElectricCar
导入整个模块   
import car
导入模块中所有类 
from model_name import *
'''
