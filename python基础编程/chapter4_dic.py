'''
字典由键及其相应的值组成，这种键值对称为项（item）。在前面的示例中，键为名字，而
值为电话号码。每个键与其值之间都用冒号（:）分隔，项之间用逗号分隔，而整个字典放在花
括号内。空字典（没有任何项）用两个花括号表示，类似于下面这样：{}
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
'''

phonebook = {'Alice': 2341, 'Beth': '9102', 'Cecil': '3258'}

'''
相比于检查列表是否包含指定的值，检查字典是否包含指定的键的效率更高。数据结构
越大，效率差距就越大。
前述第一点（键可以是任何不可变的类型）是字典的主要优点。第二点也很重要，下面的示
例说明了这种差别：
>>> x = [] 
>>> x[42] = 'Foobar' 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
IndexError: list assignment index out of range 
>>> x = {} 
>>> x[42] = 'Foobar' 
>>> x 
{42: 'Foobar'} 
'''

people = {
 'Alice': {'phone': '2341', 'addr': 'Foo drive 23'},
 'Beth': {'phone': '9102', 'addr': 'Bar street 42'},
 'Cecil': {'phone': '3158', 'addr': 'Baz avenue 90'}
}

# 电话号码和地址的描述性标签，供打印输出时使用
labels = {'phone': 'phone number', 'addr': 'address'}

name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')

# 使用正确的键：
if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'
# 仅当名字是字典包含的键时才打印信息：
if name in people:
    print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

'''
第3章介绍过，可使用字符串格式设置功能来设置值的格式，这些值是作为命名或非命名参
数提供给方法format的。在有些情况下，通过在字典中存储一系列命名的值，可让格式设置更容
易些。例如，可在字典中包含各种信息，这样只需在格式字符串中提取所需的信息即可。为此，
必须使用format_map来指出你将通过一个映射来提供所需的信息。
>>> phonebook 
{'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'} 
>>> "Cecil's phone number is {Cecil}.".format_map(phonebook) 
"Cecil's phone number is 3258." 
'''
print("Cecil's phone number is {Cecil}.".format_map(phonebook))
