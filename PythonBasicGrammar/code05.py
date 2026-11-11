"控制台输入输出"
# 输出
print("hello world")


# 输出
num = 0
num = input("请输入一个数字: ")
print(f"你输入的数字是: {num}")

a = input("请输入第一个整数: ")
b = input("请输入第二个整数: ")
a = int(a)
b = int(b)

print(f"a + b = {a+b}")

#输入 4 个小数, 求 4 个小数的平均值.
a = input("请输入第一个小数: ")
b = input("请输入第二个小数: ")
c = input("请输入第三个小数: ")
d = input("请输入第四个小数: ")
a = float(a)
b = float(b)
c = float(c)
d = float(d)
avg = (a + b + c + d) / 4
print(f"4 个小数的平均值是: {avg}")


