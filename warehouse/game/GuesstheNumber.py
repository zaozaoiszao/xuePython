import random
opportunities=5
#机会只有5次
print('欢迎来到猜数字游戏！')

#使用random模块随机生成一个1到100的整数
num=random.randint(1,100)
#使用while循环，当输入的数字与随机生成的数字不相等时，继续循环
while True:
    inp=input('请猜一个1到100之间的整数：')
    
    #作弊码
    if inp=='give me the key':
        print('你发现了作弊码！')
        print('目标数字是'+str(num)+'。游戏结束！')
        break
    
    elif inp=='give me some opportunities':
        print('你发现了作弊码！,机会多了5次！')
        opportunities+=5
        continue
        
    else:
        #判断输入的数字是否为整数
        try:
            inp=int(inp)
        except:
            print('输入的数字格式有误，请重新输入！')
            continue
        

    if num==inp:
        print('恭喜你，猜对了！游戏结束！')
        break
    
    elif num>inp:
        print('猜的数字偏小了！')
        opportunities-=1
        
    else:
        print('猜的数字偏大了！')
        opportunities-=1

    if opportunities==0:
        print('很遗憾，你没有在5次机会内猜中数字。目标数字是'+str(num)+'。游戏结束！')
        break
    elif opportunities>0:
        print('你还有'+str(opportunities)+'次机会！')