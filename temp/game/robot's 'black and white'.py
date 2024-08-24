import random
a1=a2=a3=v=x=0
while True:
    # 生成三个随机数r1、r2、r3，分别代表三个判断结果
    r1=random.randint(1,2)
    r2=random.randint(1,2)
    r3=random.randint(1,2)
    
    # 判断是否平局
    if r2==r3==r1==1 or r2==r3==r1==2:
        x+=1  # 平局次数累计
        
    # 判断机器人失败的情况
    elif r2==r3==1 and r1==2:
        a1+=1  # 机器人失败次数累计
        
    elif r2==r3==2 and r1==1:
        a1+=1
        
    # 判断机器人以外的其他参与者失败的情况
    elif r2==r1==1 and r3==2:
        a3+=1  # 参与者r3失败次数累计
        
    elif r2==r1==2 and r3==1:
        a3+=1
        
    elif r3==r1==1 and r2==2:
        a2+=1  # 参与者r2失败次数累计
        
    elif r3==r1==2 and r2==1:
        a2+=1        
    else:
        print('Error')  # 发生无法识别的结果
        continue
    v+=1  # 比较次数累计
    if v==100:
        break  # 达到预设比较次数，结束循环
print((a1+a2+a3)-v)  # 输出参与者们的平均失败次数