# 1. sorted（数据容器，reverse=布尔值）对容器排序（从小到大，不会改变原容器）reverse用于控制排序方式返回值：经过排序的新容器
# 1.1若容器中的元素：都是数字，则按照数字的大小顺序进行排序
nums = [23, 11, 32, 33, 14]
result = sorted(nums, reverse=True)
print(result)
print(nums)

# 1.2若容器中的元素：既有数字又有字符串，则报错
# nums = [23, 11, 32, 33, 14, '你好']
# sorted(nums, reverse=True)

# 1.2若容器中的元素：都是字符串，则按照字符串的Unicode编码大小进行排序
msg_list = ['北京', '上海', '江苏']
result = sorted(msg_list)
print(result)
print(msg_list)
print(ord('你'))
print(ord('北'))
print(ord('上'))


# len（数据容器）获取容器中元素的个数返回值：元素个数
#
# max（数据容器）返回容器中或多个值中的最大值返回值：最大值
#
# min（数据容器）返回容器中或多个值中的最小值返回值：最小值
#
# sum（数据容器）  ！！！不能使用在字符串上对容器中所有元素求和（只能是数值类型）返回值：所有元素的和
