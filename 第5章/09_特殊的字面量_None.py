# None表示空值 / 无值 / 无意义，是一个特殊的字面量
msg = None
# None它的类型是 NoneType，且整个 Python 中只有一个 None 实例
print(type(msg))

# None转换为布尔值时为 False
print(bool(msg))
# None不能参与数学运算，也不能直接和字符串拼接
if msg:
    print('你好')

# result1 = msg + 1
# result2 = msg + 'Hello'