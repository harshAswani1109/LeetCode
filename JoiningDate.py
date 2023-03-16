t = int(input())
for i in range (t):
    n,k = map(int,input().split())
    if(k%5==0 and n%5!=0):
        print(n//5-k//5+1)
    elif(k%5!=0 and n%5==0):
        print(n//5-k//5-1)
    else :
        print(n//5-k//5)
    