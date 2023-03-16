for i in range (int(input())):
    n,x = list(map(int,input().split()))
    print(min(x,n-x))