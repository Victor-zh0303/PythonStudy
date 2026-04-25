# 使用递归打印n次“你好啊”（从大到小）
# def welcome(n):
#     print(f'你好啊{n}')
#     if n > 1:
#         welcome(n - 1)
#
#
# welcome(5)

# 按从小到大顺序打印

def welcome(n):
    if n > 1:
        welcome(n - 1)
    print(f'你好啊{n}')


welcome(5)
