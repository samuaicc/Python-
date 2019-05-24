#截取字符
var1 = 'abcdefghijklmnopqrstuvwxyz'
print("I_want_tell_you:",var1[8],var1[11],var1[14],var1[21],var1[4],var1[24],var1[14],var1[20])
print(var1[0:1])      #输入var1中位置0开始到位置1以前的字符
print(var1[2:8])      #输入var1中位置2开始到位置8以前的字符
num = 166             #定义num是整数18
str1 = '00000' + str(num)       #通过str()函数将num改变为字符串的类型
print(str1[-5:])       #输出字符串str右五位
print(str1[-5:-1])       #输出字符串倒数第五位和倒数第一位之前的字符
print(str1[::-1])        #创造一个与原字符串相反的字符串
print(str1[:])           #截取全部字符
print(str1[-5:])         #截取倒数第五位到最后的字符
print(str1[:-3])         #截取从头开始到倒数第三位之前的字符


