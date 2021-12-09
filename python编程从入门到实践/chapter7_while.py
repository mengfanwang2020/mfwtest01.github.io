'''
用户输入和while循环
1、input()函数 int()函数
2、求模运算符 % 两数相除返回余数
3、while循环
使用标志 active = True
while active:
...
break退出while循环 立即退出while循环 不再执行循环余下代码
continue退出while循环 返回到循环开头
'''
def make_pizza(size, *toppings):
    print(size)
    for topping in toppings:
        print(topping)