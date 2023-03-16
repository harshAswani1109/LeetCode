for _ in range (int(input())):
    a,b,c = map(int,input().split())
    min3=min(b,c)
    p = b - min3
    q = c - min3
    sum = p+q
    if a!=0 and a>sum:
        print("Yes")
    else :
        print('No')