import getpass
import random
me=timi=0
while True:
    r=random.randint(1,2)
    
    me_input=int(getpass.getpass('black is 1,white is 2,your:'))
    if me_input != 1 and me_input !=2:
        print('no,again')
        continue

    timi_input=int(getpass.getpass('black is 1,white is 2,your:'))
    if timi_input != 1 and timi_input !=2:
        print('no,again')
        continue
    
    if me_input==timi_input==r==1 or me_input==timi_input==r==2: # we are tied
        x='your are lucky!'
        
    elif me_input==timi_input==1 and r==2: # robot is lost
        x='robot is lost'
        
    elif me_input==timi_input==2 and r==1: # robot is lost
        x='robot is lost'
        
    elif me_input==r==1 and timi_input==2: # timi is lost
        x='timi is lost'
        
    elif me_input==r==2 and timi_input==1: # timi is lost
        x='timi is lost'
        
    elif timi_input==r==1 and me_input==2: # I am lost
        print('zao is lost')
        
    elif timi_input==r==2 and me_input==1: # I am lost
        print('zao is lost')
        
    else:
        print('Error')
        continue
    print(x)