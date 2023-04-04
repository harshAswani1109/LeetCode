for i in range (int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 1
    for i in range(n) :
        cnt = cnt * arr[i]
    if(cnt>=0):
        print("0")
    else:
        print("1")
        