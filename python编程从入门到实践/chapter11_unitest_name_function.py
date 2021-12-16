'''
Python标准库中的模块unittest提供了代码测试工具
'''
def get_formatted_name(first, last, middle = ''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
