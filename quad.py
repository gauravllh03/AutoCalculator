import math 
def findRoots( a, b, c): 
    if a == 0: 
        print("Invalid") 
        return -1
    d = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(d)) 
    if d > 0: 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
    elif d == 0: 
        print(-b / (2*a)) 
        print(-b / (2*a)) 
    else: #d<0 
        print(- b / (2*a) , " + i", sqrt_val/(2*a)) 
        print(- b / (2*a) , " - i", sqrt_val/(2*a)) 
  

si=list(input())
sa=0
sb=0
sc=0
if(si[0]=='-'):
        sa=1
f=1 
for i in range(1,len(si)):
    if si[i]=='+':
        si[i]='#'
        if f==1:
            f=2
        elif f==2:
            break
    elif si[i]=='-':
        si[i]='#'
        if f==1:
            f=2
            sb=1 
        elif f==2:
            sc=1 
            break
s=""
for i in si:
    s+=i
data=s.split("#")
#print(sc)
b=0
a=0
c=0
l=""
if len(data)==1:
    a=1
elif len(data)==2:
    if s[-1]!='x':
        c=int(data[1])
        if sb==1:
            c=-1*c
        for i in data[0]:
            if(i=='x'):
                break
            elif i=='-':
                continue
            else:
                l+=i
        if l=='':
            l=1
        a=int(l)
        if sa==1 :
            a=a*-1
    else :
        for i in data[1]:
            if(i=='x'):
                break
            else:
                l+=i
        if l=='':
            l=1
        b=int(l)
        if sb==1 :
            b=-1*b
        l=""
        for i in data[0]:
            if(i=='x'):
                break
            elif i=='-':
                continue
            else:
                l+=i
        if l=='':
            l=1
        a=int(l)
        if sa==1 :
            a=a*-1
else:       
    c=int(data[2])
    if sc==1:
        c=-1*c
    
    l=""
    for i in data[1]:
        if(i=='x'):
            break
        else:
            l+=i
    if l=='':
        l=1
    b=int(l)
    if sb==1 :
        b=-1*b
    l=""
    for i in data[0]:
        if(i=='x'):
            break
        else:
            l+=i
    if l=='':
        l=1
    a=int(l)
    if sa==1 :
        a=a*-1
findRoots(a, b, c)
