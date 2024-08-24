a,b=1,1
print('1\n1')
while a+b<1000:
    a,b=b,a+b
    print(b,end=",")