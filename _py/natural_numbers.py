

def NatNum(x):
 sum=1
 for b in range(1,x+1):
   sum=sum*b
 return sum

 print(NatNum(1,250))


def NatNum(x,y):
    if x==1:
        print('')
        x += 1
    for a in range(x, y+1):
        for b in range(2, a+1):
            if a % b == 0:          
                break              
        if b == a:                  
            print(a,end=" ")
    print('')
NatNum(1,1000)