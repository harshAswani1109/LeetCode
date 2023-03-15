import math
for i in range (int(input())):
    x,y=map(float,input().split())
    
    z1=(y*y-x*x)**.5
    z2=(x*x+y*y)**.5
    print(round(z1,4),round(z2,4))