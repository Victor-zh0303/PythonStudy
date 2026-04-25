a = 100
b = 200


def test():
    c = '你好啊'
    d = 'Hello World'
    print(a)
    print(b)
    print(c)
    print(d)


test()
print(a)
print(b)
# print(c)报错
# print(d)报错

print(f'+' * 50)


# 局部作用域和局部变量，会在函数调用时创建，在函数执行结束后销毁
def test2():
    m = 100
    m += 1
    print(f'我是test2函数中打印的m:{m}')


test2()
test2()

# 全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
n = 100


def test3():
    global n
    n = n + 1
    print(n)


test3()
test3()
print(n)
