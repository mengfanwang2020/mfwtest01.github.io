#列表
'''
1、
[]表示列表 逗号分隔
bicycles = ['trek', 'redline', 'cannondale']
最后一个元素的索引为 -1 以此类推
'''
bicycles = ['trek', 'redline', 'cannondale']

'''
2、
修改元素、添加元素、插入元素、删除元素
.append() .insert(index, '')  del bicycles[1] / .pop(index) 删除元素 可以继续使用/ .remove() 名称
'''
bicycles.insert(0,'suzuki')

'''
3、
组织列表
.sort() 永久性排序 index: reverse = True 相反顺序
函数sorted() 临时排序 index同上
倒着打印列表 .reverse()
列表长度 len(index)
'''
print(len(bicycles))