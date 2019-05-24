#-*-coding:utf-8-*-
#while循环依次输出1——50
num = 0
while (num < 51):
    print("The number is:",num)
    num += 1
print("Over!!!")
print("=========这是一条华丽的分割线=========")
#while嵌套循环输出素数
list = []
i = 2
while (i < 100):
    j = 2
    while (j <=( i / j )):
        if (i % j == 0):break
        j += 1
    if (j > (i / j)):      #此处不能用else语句，因为上面有break
        list.append(i)
    i = i + 1
print("100以前的素数为:",list)
    
