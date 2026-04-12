print('🏆欢迎来到：答题闯关挑战赛（输入q可随时推出）\n')

# 题目与答案
ques1, ans1 = 'Python中用于输出的函数是？', 'print'
ques2, ans2 = 'Python中用于表达逻辑"并且"的关键字是？', 'and'
ques3, ans4 = 'Python属于编译型还是解释型？', '解释型'


# 最多可尝试次数
max_tries = 3
# 总关卡数
total_levels =3
# 是否处于可游戏状态
is_playing = True

# 根据题目数量开始循环
for level in range(1, total_levels + 1):
    #打印当前是第几关
    print(f'************⏳第{level}关***************')
    # 取出当前关卡所对应的题目和答案
    if level == 1:
        question, answer = ques1, ans1
    elif level == 2:
        question, answer = ques2, ans2
    else:
        question, answer = ques3, ans3
    # 向用户提问
    user_input = input('📍'+question)
    # 根据用户输入，来决定做什么
    if user_input == answer:
        print('✅回答正确！\n')
    elif user_input == '':
        print('')