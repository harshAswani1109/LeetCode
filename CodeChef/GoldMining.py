for i in range (int(input())):
        n,x,y = map(int,input().split())
        if x <= (n+1)*y :
            print("Yes")
        else :
            print("No")