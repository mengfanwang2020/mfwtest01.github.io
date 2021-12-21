'''
5.4.1 比较运算符
x == y x 等于y
x < y x小于y
x > y x大于y
x >= y x大于或等于y
x <= y x小于或等于y
x != y x不等于y
x is y x和y是同一个对象
x is not y x和y是不同的对象
x in y x是容器（如序列）y的成员
x not in y x不是容器（如序列）y的成员

is检查两个对象是否相同（而不是相等）。变量x和y指向同一个列表，而z指向另一个列表
（其中包含的值以及这些值的排列顺序都与前一个列表相同）。这两个列表虽然相等，但并
非同一个对象，总之，==用来检查两个对象是否相等，而is用来检查两个对象是否相同
（是同一个对象）。
'''