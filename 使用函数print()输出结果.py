#coding=utf8
print('a','b','c')             #正常打印输出，输出后逗号用空格代替并分开数据,结束后添加了一个换行符
print('a','b','c',sep=',')     #将分隔符改为“,”
print('a','b','c',sep=';')     #将分隔符改为“;”
print('a','b','c',end=';')     #在输出结束后添加了一个分号，所以下一行输出结果将会与这行放在同一行
print('a','b','c')             #正常输出，但是输出结果会与上一行并列
