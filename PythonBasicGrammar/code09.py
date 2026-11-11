# #打印 1-10 的整数
# num = 1
# while num <= 10 :
#     print(num)
#     num += 1

# 计算 1-100 的和
# num = 1
# sum = 0
# while num <= 100 :
#     sum += num
#     num += 1
# print(sum)

#计算 5 的阶乘
# num = 1
# result = 1
# while num <= 5 :
#    result *= num
#    num += 1
# print(result)

#求 1! + 2! + 3! + 4! + 5!
num = 1
sum = 0
while num <= 5:
    factorResult = 1
    i = 1
    while i <= num:
        factorResult *= i
        i += 1
    sum += factorResult
    num += 1
print(sum)