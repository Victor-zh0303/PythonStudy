# 定义函数
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}，二者相加是：{n1 + n2}')
    print(f'add函数执行完毕！')
    return n1 + n2


# 调用函数
result = add(100, 200)
print(result)

# print函数没有返回值
res = print('Hello World')
print(res)