a,b,q=0,0,0
import random
while True:
    x=random.randint(1,2)
    if x==1:
        a+=1
    elif x==2:
        b+=1
    q+=1
    if q==100000:
        break
print(a/q,b/q,a/q+b/q)