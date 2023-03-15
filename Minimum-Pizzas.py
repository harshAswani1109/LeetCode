import math
for i in range (int(input())):
    n,x=map(int,input().split())
    print(math.ceil(n*x/4))