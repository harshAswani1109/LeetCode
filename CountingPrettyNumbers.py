for i in range (int(input())):
    l,r = map(int,input().split())
    cnt = 0
    for j in range(l,r+1):
        k = j%10
        if k==2 or k==3 or k==9 :
            cnt = cnt + 1
 
    print(cnt)   
