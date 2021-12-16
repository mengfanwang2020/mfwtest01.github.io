# path = 'D:\githubcode\mfwtest01.github.io\python编程从入门到实践\pi_digits'
# with open(path) as file_object:
#     contents = file_object.readlines()
# pi_string = ''
# for content in contents:
#     pi_string += content.strip()
# print(pi_string[:])
# line = '1582'
# print(line in pi_string)
'''
逐行读取 使用for循环
for line in file_object:
    print(line.rstrip())
读取文本文件时，Python将其中的所有文本读取为字符串，若读取数值作为值用 int() 转换 float() 转换
'''
#创建一个包含文件各行内容的列表
#line = file_object.readlines()
#为了删除左右的空格 可使用.strip()
# with open(path, 'a') as file_object:
#     file_object.write("我爱编程")
'''
调用open时 提供两个实参 一个是path 一个是'r'读取模式 'w'写入模式 'a'附加模式
'r+'读取+写入模式   'w'模式打开文件若文件已经存在，则先清空文件后打开
'''
# try:
#     print(5/0)
# except Exception:
#         print("no zero")
'''
处理FileNotFoundError 找不到文件异常
try:
...
except FileNotFoundError:
...
else:
...
如果有异常一声不吭 使用pass
'''

'''
导入模块json 文件数据存储的格式为JSON
使用函数json.dump()将数字列表存储到文件number.json中
重构：每个函数执行单一而清晰的任务 代码划分为一系列完成具体工作的函数
'''
import json

number = [2, 3, 4, 5, 7]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

filename2 = 'number.json'
with open(filename2) as f_obj:
    #使用函数.load()加载存储在number.json中的信息
    numbers = json.load(f_obj)

print(numbers)