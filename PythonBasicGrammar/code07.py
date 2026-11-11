# 输入1表示认真学习，输入2表示摆烂，输入其他的违法输入。

choice = input("输入 1 表示认真学习, 输入 2 表示躺平摆烂: ")
if choice == "1":
    print("认真学习,找到好工作")
elif choice == "2":
    print("摆烂躺平")
else:
    print("违法输入!")