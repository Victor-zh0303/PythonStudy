# 使用str()将指定数据转换为字符串
# result1 = str(19)
# result2 = str(75.6)
# result3 = str(1.5e3)
# result4 = str(12_000)
# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)

# <class 'str'> 19
# <class 'str'> 75.6
# <class 'str'> 1500.0
# <class 'str'> 12000

# 把指定数据转为整型：int（）
# result1 = int(15.6)
# result2 = int('79')
# result3 = int('    79   ')
# result4 = int(46)
# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)
# <class 'int'> 15
# <class 'int'> 79
# <class 'int'> 79
# <class 'int'> 46


# 把指定数据转为浮点型：float（）
result1 = float(19)
result2 = float('15.6')
result3 = float('    5.7   ')
result4 = float(14.8)
result5 = float('48')


print(type(result1), result1)
print(type(result2), result2)
print(type(result3), result3)
print(type(result4), result4)
print(type(result5), result5)

# <class 'float'> 19.0
# <class 'float'> 15.6
# <class 'float'> 5.7
# <class 'float'> 14.8
# <class 'float'> 48.0