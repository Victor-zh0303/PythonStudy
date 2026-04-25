# 递归的应用举例：使用递归求一个书的阶乘

def factorial(num):
    if num == 0:  # 递归终止条件（必须有！否则无限递归）
        return 1  # 0! 规定等于 1
    else:
        # 递归：num × 上一个数的阶乘
        return num * factorial(num-1)

result = factorial(5)
print(result)  # 输出 120