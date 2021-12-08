'''
1、遍历整个列表
bicycles = ['trek', 'redline', 'cannondale']
for _ in _: for循环
在for循环中 一定要注意  缩进 不要遗漏冒号
2、避免缩进错误 PE8中规定每级缩进四个空格
忘记缩进、忘记缩进额外的代码行、不必要的缩进
'''
bicycles = ['trek', 'redline', 'cannondale']
for bicycle in bicycles:
    print(bicycle)

'''
3、创建数字列表
使用.range()函数创建 左闭右开+步长
list(range(2,11,2)) 使用list()函数
min() max() sum()
列表解析  squares = [value**2 for value in range(1,11,2)]
4、使用列表的一部分 切片
bicycles[0:2] bicycles[:2] bicycles[0:] bicycles[-2:]
复制列表 copy_bicycles = bicycles[:]
5、元组 不可变的列表称为元组 
使用圆括号来标识 而不是方括号 dimensions = (200,50)  dimensions[0] = 200 
'''
for value in range(1,5,2):
    print(value)

squares = [value ** 2 for value in range(1, 11, 2)]
print(squares)
