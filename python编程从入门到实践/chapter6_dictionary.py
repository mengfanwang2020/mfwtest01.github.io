'''
1、字典
alien_0 = {'color':'green', 'point':5}
字典用放在 花括号 中的一系列 键-值 表示
访问字典中的值 alien_0['color'] 修改字典中的值
添加 键-值 对  alien_0['x_position'] = 0   删除 del alien_0['color'] 彻底删除 键-值 对
可以先形成一个空字典 alien_0 = {}

2、遍历字典
.items() 键-值对  .keys() 键  .values() 值

3、嵌套
字典列表 alien_0 = {} alien_1 = {}   aliens = [alien_0,alien_1]
'''
alien_0 = {'color':'green', 'point':5}
for key in alien_0.keys():
    print(key)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein'
    }
}
for key,value in users.items():
    print(key)
    for key0,value0 in value.items():
        print(key0 + " " + value0)