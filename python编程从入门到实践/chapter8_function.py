'''
函数
1、定义函数
def greet_user():
...
向函数传递信息 传递任意数量的实参 函数(*index)  任意数量的关键字实参 函数(**index)
def greet_user(username):
...
2、返回值
返回简单值 return ...
返回字典 return dictionary
3、函数导入模块
(1)import .py
(2)from pizza import make_pizza   from pizza import * 导入pizza的所有函数
4、使用as给模块指定别名 import pizza as p
'''
# import chapter7_while
# chapter7_while.make_pizza(16, 'mushrooms')

# from chapter7_while import make_pizza
# make_pizza(16,'mushrooms')

import chapter7_while as pizza
from chapter9_class import Car
pizza.make_pizza(16,'mushrooms')
my_new_car = Car('Q', 'medium', '17')
print(my_new_car.get_descriptive_name())