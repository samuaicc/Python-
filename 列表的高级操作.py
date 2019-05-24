#-*-coding:utf-8-*-
#列表可以使用'+','*'运算符，'+'用于组合列表，'*'用于重复输出列表
print('*********列表中的运算符*********')
list = [1,2,3]
list1 = [4,5,6]
print(list + list1)   #'+'用来合并列表
print(list * 4)       #'*'用来重复输出列表
print(3 in list)      #判断3是否在列表中
for x in list:        #用于循环
    print(x)
print("*********列表的截取和拼接功能*********")
list3 = [0,1,2,3,4,5,6]
print(list3[2])
print(list3[1:])
print(list3[-2])          #显示指定的元素
print(list3 + [7,8,9])    #拼接列表
print('*********使用列表嵌套*********')
list4 = [list,list1]
print(list4)
print(list4[0])     #输出list4中位置为0的元素
print(list4[1][2])  #输出list4中位置为1的列表中位置为2的元素
print('*********获取列表中元素的最大值和最小值*********')
list5 = ['a','b','c','d','e']
print(max(list))
print(min(list))
print(max(list5))
print(min(list5))
print('*********追加其他列表中的值*********')
list.extend(list1)   #使用list.extend(sep)追加其他列表中的元素到list,会永久改变list
print(list)
print('*********统计列表中元素出现的次数*********')
list6 = [1,1,1,12,3,6,4,1,3]
print(list6)
print('列表中1出现的次数:',list6.count(1))
print('列表中3出现的次数:',list6.count(3))   #list.count(obj)用来统计元素出现的次数
print('*********清空列表的元素*********')
print('原list6列表:',list6)
list6.clear()      #clear()清空列表
print('将list6清空:',list6)
print('*********复制列表中的元素*********')
list7 = list3.copy()
print('复制list3到list7中:',list7)
print('*********获取列表中的某个元素的索引*********')
#使用index()获取列表中某个元素的索引位置，只能找出元素第一次出现的位置，如果没有找到元素就会抛异常
print('list7中元素3的位置:',list7.index(3))

