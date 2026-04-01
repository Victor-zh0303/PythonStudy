print('请输入你的年龄')
age = input()
# print(type(age)) # input的都是字符串
print(f'你今年的年龄是{age}岁')
# input的都是字符串所以，用input的数值运算要先转成int
print(f'你明年的年龄是{int(age)+1}岁')

# 更优雅的方式
name = input('请输入你的姓名：')
age = input('请输入你的年龄：')
# print(type(age)) # input的都是字符串
print(f'{name}，你今年的年龄是{age}岁')
# input的都是字符串所以，用input的数值运算要先转成int
print(f'{name}，你明年的年龄是{int(age)+1}岁')