# # 测试continue
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     continue
#     print('睡觉')

# 第2天不睡觉
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     if day == 2:
#         continue
#     print('睡觉')

# 第2天不打印
# for day in range(1, 5):
#     if day == 2:
#         continue
#     print(f'************第{day}天************')
#     print('吃饭')
#     print('睡觉')

# 在嵌套循环中使用
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 每天不要牛奶2
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if item == 2:
#             continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 不要第4天的牛奶2
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 测试break
# for day in range(1, 5):
#     print(f'************第{day}天************')
#     print('吃饭')
#     if day == 2:
#         break
#     print('睡觉')

# 第2天停止
# for day in range(1, 5):
#     if day == 2:
#         break
#     print(f'************第{day}天************')
#     print('吃饭')
#     print('睡觉')

for day in range(1, 5):
    print(f'************第{day}天************')
    print('吃饭')
    for item in range(1, 3):
        print(f'面包{item}')
        if day == 4 and item == 2:
            break
        print(f'牛奶{item}')
    print('睡觉')