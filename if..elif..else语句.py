#-*-coding:utf-8-*-
#用来判断多条件
x = input("输入你的成绩:")
x = float(x)
if x >= 90:
    print("你的成绩为优")
elif x >= 80:
    print("你的成绩为良")
elif x >= 70:
    print("你的成绩为中")
elif x >= 60:
    print("你的成绩为合格")
else:
    print("你的成绩不合格，继续努力！")
