samustr1 = "I love you!"
print("显示原始字符串：",samustr1)
print("将字符串中的第一个首字母大写:\t",samustr1.capitalize())
print("获取字符串中某一子字符串的数目\t",samustr1.count('o'))
print("获得字符串中某一子字符串的起始位置\t",samustr1.find('I')) #无则返回-1
print("检测字符串中是否仅包含0~9、A~Z、a~z\t",samustr1.isalnum())
print("连接字符串",' '.join("abcde"))
print("将字符串全部变为小写",samustr1.lower())
print("将字符串全部变为大写",samustr1.upper())
print("将字符串中的大写字母变小写，小写字母变大写",samustr1.swapcase())
print("将字符串中的单词首字母大写",samustr1.title())
print("分割字符串",samustr1.split(' ')) #' '表示以空格分隔
print("获取字符串长度",len(samustr1))
samustr = "My name is samu,I am 19 years old"
print(samustr.center(60,'*'))   #规定一个字符串的长度，并用自定的字符在两边自动补齐
print(samustr.endswith('old'))  #可以用来判断字符串是不是以('输入判断的字符')结尾
print("姓名：{name},年龄：{age}".format(name="samu", age="19")) #格式化字符串
print(samustr.rjust (60,'0'))    #规定一个字符串的长度，不足用'0'从左边补齐
print(samustr.ljust (60,'$'))    #规定一个字符串的长度，不足用'$'从右边补齐
print("abcabcbacbac\n   ")
print("abcabcbacbac\n   ".rstrip())  #默认去掉右边的空格或回车
print("\n   abcabcbacbac".lstrip())
print("abca\n   bcbacbac".strip())   #删除字符串开头或结尾的空格或换行符。只能删除开头或是结尾的字符，不能删除中间部分的字符
#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
str1 = "-"
seq = ("a", "b", "c") # 字符串序列
print (str1.join( seq ))
print (samustr.zfill(60))        #规定字符串长度不够全部由0补充
print (samustr.rfind('a'))      #找到某一字符在字符串中最右边的位置
print (samustr.find('a'))       #找到某一字符在字符串中的起始位置，没有返回-1
print (samustr.replace('a','*')) #替换字符
#创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标.两个字符串的长度必须相同，为一一对应的关系。
samu = 'abcdefghijklmnop'
aicc = '0123456789~!@#$%'
str = 'i love you girl!'
jia_mi = str.maketrans(samu,aicc)
print (str.translate(jia_mi))

