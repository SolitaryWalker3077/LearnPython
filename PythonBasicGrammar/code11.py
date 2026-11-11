import random
import sys
import time

# 人生重开模拟器
"""
在游戏中我们设定四个属性.
颜值 (face)
体质 (strong)
智力 (iq)
家境 (home)
我们约定每个属性的范围为 [1, 10], 并且总和不能超过 20.
"""
print("+--------------------------------------------------------------------+")
print("|                                                                    |")
print("|                    花有重开日, 人无再少年                              |")
print("|                                                                    |")
print("|                    欢迎来到, 人生重开模拟器                            |")
print("|                                                                    |")
print("+--------------------------------------------------------------------+")
# 设置初始属性
while True:
    print("请设定初始属性(可用总点数 20)")
    face = int(input("设定 颜值(1-10):"))
    strong = int(input("设定 体质(1-10)"))
    iq = int(input("设定 智商(1-10)"))
    home = int(input("设定 家境(1-10)"))

    #初始值合法判断
    if face < 1 and face > 10:
        print("颜值设置有误!")
        continue
    if strong < 1 and strong > 10:
        print("体质设置有误!")
        continue
    if iq < 1 and iq > 10:
        print("智商设置有误")
        continue
    if home < 1 and home > 10:
        print("家境设置有误")
        continue
    if face + strong + iq + home > 20 :
        print("总点数超过了 20!")
        continue
    print("初始属性设定完成!")
    break

# 设置性别
point = random.randint(1, 6) # 掷色子
if point % 2 == 1:
    gender = "boy"
    print("你是一个男孩")
else :
    gender = "girl"
    print("你是一个女孩")

# 设置出生点
"""
首先按照家境(home), 分成四个档位. 
10 是第一档. 加成最高
[7, 9] 是第二档. 也有一些加成
[4, 6] 是第三档. 加成较少
[1, 3] 是第四档. 会扣掉属性. 
再扔一次色子, 生成 [1, 3] 的随机数, 用来表示每一种细分情况.
"""
point = random.randint(1, 3) # 掷色子
if home == 10:
    print('你出生在帝都, 你的父母是高官政要')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    if point == 1:
        print('你出生在大城市, 你的父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大城市, 你的父母是大企业高管')
        home += 2
    else:
        print('你出生在大城市, 你的父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    if point == 1:
        print('你出生在三线城市, 你的父母是教师')
        iq += 1
    elif point == 2:
        print('你出生在镇上, 你的父母是医生')
        strong += 1
    else:
        print("你出生在镇上, 你的父母是个体户")
        home += 1
else:
    if 1 <= point <= 2:
        print('你出生在村里, 你的父母是辛苦劳作的农民')
        strong += 1
        face -= 2
    elif 3 <= point <= 4:
        print('你出生在穷乡僻壤, 你的父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上, 你父母感情不和')
        strong -= 1

"""
针对每一岁, 生成人生经历
按照年龄, 把人生经历分成四个阶段:
幼年阶段 [1, 10]
青年阶段 [11, 20]
壮年阶段 [20, 50]
老年阶段 50 岁以上
"""

for age in range(1, 11):
    info = f'你今年{age}岁'
    point = random.randint(1, 3)
    # 性别触发事件
    if gender == "girl" and home <= 3 and point == 1:
        info += '你家里人重男轻女思想非常严重, 你被遗弃了!'
        print(info)
        print("游戏结束")
        sys.exit(0)
    # 体质触发事件
    elif strong < 6 and point != 1:
        info += "你生了一场病"
        if home >= 5:
            info += '在父母的精心照料下恢复了健康'
            strong += 1
            home -= 1
        else:
            info += "你的父母没精力管你, 你的身体状况更糟糕了"
            strong -= 1
    # 颜值触发的事件
    elif face < 6 and age > 7:
        info += '你因为长的太丑, 别的小朋友不喜欢你, '
        if iq > 5:
            info += '你决定用学习填充自己'
            iq += 1
        else:
            if gender == "boy":
                info += '你和别的小朋友经常打架'
                iq -= 1
                strong += 1
            else:
                info += '你经常被别的小朋友欺负'
                strong -= 1
    # 智商触发的事件
    elif iq < 5:
        info += '你看起来傻傻的, '
        if home >= 8 and age >= 6:
            info += '你的父母给你送到更好的学校学习'
        elif 4 <= home <= 7:
            if gender == 'boy':
                info += '你的父母鼓励你多运动, 加强身体素质'
                strong += 1
            else:
                info += '你的父母鼓励你多打扮自己'
                face += 1
        else:
            info += '你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
    # 健康成长
    else:
        info += '你健康成长, '
        if point == 1:
            info += '看起来更聪明了'
            iq += 1
        elif point == 2:
            info += '看起来更好看了'
            face += 1
        else:
            info += '看起来更结实了'
            strong += 1

    print('-------------------------------------------')
    print(info)
    print(f'strong={strong}, face={face}, iq={iq}, home={home}')
    time.sleep(1)