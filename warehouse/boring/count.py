try:
    def jiafa(a):

        jia=a.index('+')
        jia1=a[:jia]
        jia2=a[jia+1:]

        return int(jia1)+int(jia2)

    def jianfa(b):

        jian=b.index('-')
        jian1=b[:jian]
        jian2=b[jian+1:]

        return int(jian1)-int(jian2)

    def chengfa(c):

        cheng=c.index('*')
        cheng1=c[:cheng]
        cheng2=c[cheng+1:]

        return int(cheng1)*int(cheng2)

    def chufa(c):
        #c=input('input:')
        chu=c.index('/')
        chu1=c[:chu]
        chu2=c[chu+1:]

        #print(int(chu1)/int(chu2))
        return int(chu1)/int(chu2)

    while True:
        try:
            inp=input('请输入算式：')
            if '+' in inp:
                print(jiafa(inp))
            elif '-' in inp: 
                print(jianfa(inp))
            elif '*' in inp:  
                print(chengfa(inp))  
            elif '/' in inp:  
                print(chufa(inp))  
        except:
            print("Error")
except: 
    print("Error")