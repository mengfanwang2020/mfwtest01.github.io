'''
1.9
编写简单示例时，print语句很有用，因为几乎在任何地方都可使用它。如果你要尝试提供更有趣的输出，
应考虑使用模块turtle，它实现了海龟绘图法。from turtle import *
可尝试在网上搜索海龟绘图法（turtle graphic）。学习更多的概念后，你可能
想用海龟绘图法替换平淡的print语句。

1.10.4
原始字符串可派上用场，因为它们根本不会对反斜杠做特殊处理，而是让字符串包含的每个字符都保持
原样print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
要获悉字符的Unicode码点和名称，可在网上使用有关该字符的描述进行搜索，也可参阅特
定的网站，如http://unicode-table.com。
'''

print('Let\'s go')
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
print( "This is a cat: \N{Cat}")