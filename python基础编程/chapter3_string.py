import math
import string

print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))


fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))


tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))


'''
下述三个标志（s、r和a）指定分别使用str、repr和ascii进行转换。函数str通常创建外观
普通的字符串版本（这里没有对输入字符串做任何处理）。函数repr尝试创建给定值的Python表
示（这里是一个字符串字面量）。函数ascii创建只包含ASCII字符的表示，类似于Python 2中的repr
'''
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))


'''
虽然字符串方法完全盖住了模块string的风头，但这个模块包含一些字符串没有的常量
和函数。下面就是模块string中几个很有用的常量①。
 string.digits：包含数字0～9的字符串。
 string.ascii_letters：包含所有ASCII字母（大写和小写）的字符串。
 string.ascii_lowercase：包含所有小写ASCII字母的字符串。
 string.printable：包含所有可打印的ASCII字符的字符串。
 string.punctuation：包含所有ASCII标点字符的字符串。
 string.ascii_uppercase：包含所有大写ASCII字母的字符串。
虽然说的是ASCII字符，但值实际上是未解码的Unicode字符串
'''
print(string.digits, string.ascii_letters)