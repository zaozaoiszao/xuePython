import random
chance = 5
a=random.randint(1,100)
while True:
    print('猜数字游戏开始')
    inp = int(input('请输入一个数字:'))
    if inp == a:
        print('恭喜你猜对了')
        break
    else:
        print('猜错了')
        chance -= 1
        if inp > a:
            print('猜大了')
        else:
            print('猜小了')

    if chance == 0:
        print('游戏结束,正确答案是:%s' % a)
        break