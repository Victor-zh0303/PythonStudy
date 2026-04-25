# 嵌套调用：在一个函数的执行过程中，去调用了另外一个函数
# 函数嵌套调用测试1
# def speak(msg):
#     print(f'-' * 40)
#     print(msg)
#     print('-' * 40)
#
#
# def greet(name, msg):
#     print(f'我叫 {name}, 我想说的话在下面：')
#     speak(msg)
#     print('嗯，我想说的结束了')
#
#
# greet('张三', '你好啊！')

# 函数嵌套调用测试2
# def greet(name, msg):
#     print(f'我叫 {name}, 我想说的话在下面：')
#     speak(msg)
#     print('嗯，我想说的结束了')
#
#
# def speak(msg):
#     print(f'-' * 40)
#     print(msg)
#     print('-' * 40)
#
#
# greet('张三', '你好啊！')


# 测试三
def test1():
    print('进入 test1 函数')
    test2()
    print('退出 test1 函数')


def test2():
    print('进入 test2 函数')
    test3()
    print('退出 test2 函数')


def test3():
    print('进入 test3 函数')
    print('***正在执行 test3 函数***')
    print('退出 test3 函数')


test1()
