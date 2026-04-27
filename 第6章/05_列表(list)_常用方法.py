# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
fruits = ["apple", "banana", "cherry", "apple"]
result = fruits.index("apple")
print(result)
# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
nums = [1, 2, 3, 4, 5, 2]
result = nums.count(2)
print(result)
# 3.使用 reverse 方法，对列表进行反转（会改变原列表）。
nums = [1, 2, 3, 4, 5, 2]
nums.reverse()
print(nums)
# 4.使用 sort 方法，对列表排序（默认从小到大），若想从大到小，可以将 reverse 参数设为True
# 4.1 若列表中的元素都是数字，咱找数字大小排序
nums = [1, 2, 3, 4, 5, 2]
nums.sort(reverse=True)
print(nums)

# 4.2 若列表中的元素既有数字又有字符串，会报错
# nums = [1, 2, 3, 4, 5, '你好']
# nums.sort(reverse=True)
# print(nums)

# 4.3 若列表中的元素都是字符串，会按照字符串Unicode编码大小进行排序
msg_list = ['北京', '上海', '江西']
msg_list.sort()
print(msg_list)
print(ord('北'), ord('上'), ord('江'))