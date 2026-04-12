# # 前序知识
# print('你好')
# print('HELLO')
#
# print('你好', end='!')
# print('HELLO', end='@')
#
# print('你好', end='')
# print('HELLO', end='')

# for循环实现九九乘法表
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={item * row}', end='\t')
    print()
