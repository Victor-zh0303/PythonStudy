# message1和message2是不能直接换行，在PyCharm中换行会自动变成如下，加上圆括号
message1 = 'Hello World'
message2 = "Hello World"
# 三个单引号可以直接换行，并且可以作为多行注释使用。print后结果也是换行的。（回车也打印了）
message3 = '''Hello World'''
# 三个双引号，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用
message4 = """Hello World"""
print(message1)
print(message2)
print(message3)
print(message4)
