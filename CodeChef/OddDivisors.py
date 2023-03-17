for i in range(int(input())):
    l,r = map(int,input().split())
    sum1=0; sum2=0
    for i in range(1,r+1,2):
        sum1 = sum1 + i*(r//i)
        
    for i in range (1,l,2):
        sum2=sum2+i*((l-1)//i)
    print(sum1-sum2)