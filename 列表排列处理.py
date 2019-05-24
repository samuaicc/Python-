#-*-coding:utf-8-*-
#列表排列处理
car = ['benchi','baoma','aodi','falali']
print('原列表:',car)
#sort()对列表进行永久性排列，默认字母顺序从a到z
car.sort()    
print('将列表元素按字母升序排列:',car)
car.sort(reverse=True)   #’reverse=True‘参数对列表进行字母顺序从z到a
print('将列表元素按字母降序排列:',car)
#sorted()对列表临时性排序,不会改变原来的列表顺序
print('将列表临时按字母升序排序:',sorted(car))  #按照字母升序输出列表
print('将列表临时按字母降序排序:',sorted(car,reverse=True))  #’reverse=True‘参数对列表进行字母顺序从z到a的临时输出
#reverse()将列表按倒序输出，也是永久性改变列表，但可以再次调用来恢复
car.reverse()
print('将列表按倒序输出:',car)
#len()可以获取列表长度
print('该列表的长度是:',len(car))
