# cook your dish here
for i in range (int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    cnt = 0
    for i in d:
        if i>999:
            cnt+=1
    print(cnt)