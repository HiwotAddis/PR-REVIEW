import math
t=int(input())
for _ in range(t):
    x,n,m=map(int,input().split())
    min_=max_=x
    for _ in range(n+m):
        min_//=2
        max_=math.ceil(max_/2)
    print(min_,max_)
