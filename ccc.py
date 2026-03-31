import math
A=int(input())
B=int(input())
k=int(input())
T=int(input())

Staring_Distance=A-B
d=abs(A-B)
Steps=0


if d <= k/2:
    Steps=Staring_Distance
else:
    if not (d/k*2)%2 == 1:
        Steps+=abs(round((d/k)))
        d-=abs((round((d/k))*k))
        Steps+=abs(d)
    else:
        Steps+=abs(math.floor((d/k)))
        d-=abs((math.floor((d/k))*k))
        Steps+=abs(d)
    

if T==1:
    print(Steps)

if T==2:
    if d%k==k/2:
        print(Steps+1)
    elif k%2==0 and d%k==k/2+1:
        print(Steps+1)
    else:
        print(Steps+2)
