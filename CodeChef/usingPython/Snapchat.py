for i in range (int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c =0; m=0
    for i in range(n):
        if a[i]!=0 and b[i]!=0:
             c = c + 1 ; m = max(m,c)
        else : 
            c=0
    print(m)