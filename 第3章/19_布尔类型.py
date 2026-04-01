# 自己定义的布尔值
a = True
b = False
# 靠程序执行得到的布尔值
c = 6 > 3
d = 7 < 2
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
print(int(True))
print(int(False))
# <class 'bool'> True
# <class 'bool'> False
# <class 'bool'> True
# <class 'bool'> False

print(4 + True)
print(8 - False)

print(True + True)
print(True - False)


print(4 > True)
print(8 <= False)

#使用bool()将指定内容转为布尔类型
print(bool(1))
print(bool(0))

#Python中除0以外的任何数，转为布尔值后都为True
print(bool(300))
#Python中除空字符串以外的任何字符串，转为布尔值都是True
print(bool('hello'))
print(bool(''))
print(bool('18.5'))
print(bool('-9'))