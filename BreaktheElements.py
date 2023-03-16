for i in range(int(input())):
    n = int (input())
    a = list (map(int,input().split()))
    e=o=0
    for i in a:
        if i%2==0: e= e +1
        else: o = o + 1
    if e ==0 or o == 0 :print(0)
    else: print(e)