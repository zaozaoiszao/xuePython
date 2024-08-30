while True:
    #bigboxlook=0
    smallboxlook=0
    bigbox=input('a$')
    smallbox=input('b$')
    if smallbox in bigbox:
        print('yes')
    elif smallbox not in bigbox:
        while True:
            #用while循环来判断，把smallbox里的字符串一个一个的取出来，和bigbox里的字符串进行比较，如果对比到了就退出循环并打印出yes
            if smallbox[smallboxlook] in bigbox[smallboxlook:]:
                #
                smallboxlook+=1
                if smallboxlook==len(smallbox):
                    print('yes')
                    break
            else:
                print('no')
                break