import random
while True:
    a=random.randint(1,3)
    t=int(input())

    if (t==1 and a==3) or (t==2 and a==1) or (t==3 and a==2):
        x='win!'
    elif t==a:
        x='lucky!'
    else:
        x='lost!'
    print('I\'m',a,',your are '+x)