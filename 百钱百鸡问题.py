#-*-coding:utf-8-*-
#百钱百鸡问题：公鸡五文钱一只，母鸡三文钱一只，小鸡一文钱三只，拿一百文钱买一百只鸡，公鸡，母鸡，小鸡都要有，问各要几只？
for x in range(1,20):
    for y in range(1,33):
        for z in range(3,300,3):
            if 5*x + 3*y + z/3 == 100 and x + y + z == 100:
                print("公鸡:%d,母鸡:%d,小鸡:%d"%(x,y,z))
