# 新增操作
# 方式一：调用列表的append方法
# nums = [10, 20, 30, 40]
# nums.append(50)
# print(nums)

# 方式二：调用列表的insert方法
# nums = [10, 20, 30, 40]
# nums.insert(2, 666)
# print(nums)

# 方式三：可迭代对象中的内容一次取出，追加到列表尾部，调用列表extend方法
# nums = [10, 20, 30, 40]
# nums.extend('你好')
# nums.extend(range(1, 4))
# nums.extend([70, 80 ,90])
# print(nums)

# 删除操作
# 方式一：删除指定位置的元素，并将删除的元素返回，列表.pop(下标）
# nums = [10, 20, 30, 40]
# result = nums.pop(1)
# print(nums)
# print(result)

# 方式二：删除列表中第一次出现的指定值，列表.remove(值）
# nums = [10, 20, 30, 40]
# nums.remove(10)
# print(nums)

# 方式三：删除列表中的所有元素（变成一个空列表），列表.clear(）
# nums = [10, 20, 30, 40]
# nums.clear()
# print(nums)

# 方式四：删除指定位置的元素，del 列表[下标]
# nums = [10, 20, 30, 40]
# del nums[0]
# print(nums)

# 修改操作
nums = [10, 20, 30, 40]
nums[2] = 66
print(nums)

# 查询操作
nums = [10, 20, 30, 40]
print(nums[3])