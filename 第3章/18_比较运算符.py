a = 5
b = 5
c = '5'
# 使用==判断左右两侧是否相等
print(a == b)
# 使用==判断左右两侧是否相等
print(a != c)

# 使用>判断左侧是否大于右侧
a = 5
b = 7
c = '5'
result = a > b
print(result)
# result = a > c
# print(result)  # 报错

# 使用<判断左侧是否小于右侧
a = 3
b = 7
c = '5'
result = a < b
print(result)

# 使用>=判断左侧是否大于等于右侧
a = 7
b = 7
C = '5'
result = a >= b
print(result)

# 使用<=判断左侧是否大于等于右侧
a = 7
b = 7
C = '5'
result = a <= b
print(result)

# 以上这些比较运算符，同样适用于字符串
msg1 = '你好啊'
msg2 = '你好啊666'
print(msg1 == msg2)

msg1 = '你好啊'
msg2 = '你好啊666'
print(msg1 != msg2)

# Python中字符串进行比较时，是依次比较每个字符的Unicode编码。
msg1 = 'abc'
msg2 = 'xyz'
msg3 = '我爱你'
msg4 = '中国'
msg5 = 'abc'
msg6 = 'abcde'
print(msg1 > msg2)
print(msg3 > msg4)
print(msg5 > msg6)

#使用ord()查看指定字符的unicode编码
print(ord('a'))
print(ord('我'))

#使用chr()将unicode编码转为字符
print(chr(97))
print(chr(25105))