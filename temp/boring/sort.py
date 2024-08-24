a=[]
while True:
    me_input=input('input:')
    if me_input=='':
        break
    else:
        me_input=int(me_input)
        a.append(me_input)
a2=[]
u=len(a)
o=0
while True:
    a2.append(min(a))
    a.remove(min(a))
    o+=1
    if o==u:
        break
print(a2)