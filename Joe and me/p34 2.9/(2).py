import random
a=random.randint(1,100)
while True:
    b=random.randint(1,100)
    if b==a:
        b=random.randint(1,100)
    if not b==a:
        break
print(a,b)