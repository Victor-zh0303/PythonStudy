# 定义函数（接收位置参数）
def greet(name, gender, age, height):
    print(f'我叫{name}，性别{gender}，年龄是{age}，身高是{height}cm')
    print(f'我的身高是{height}，我的年龄是{age}，我叫{name}')


# 调用函数（使用关键字参数）
greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age=18, gender='男', name='张三')
greet('张三', '男', height=172, age=18)

# 错误示例
# greet(age=18, height=172, '张三', '男')
# greet(name='张三', '男', 18, 172)
# greet(name='张三', '男', age=18, 172)
# greet(name='张三', gender='男', age=18, height=172, age=19)
# greet(name='张三', gender='男', age=18, height=172, tall=19)
