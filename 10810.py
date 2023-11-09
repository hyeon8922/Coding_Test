#10810

n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(0)
for k in range(m):
    i,j,k=map(int, input().split())
    for t in range(i,j+1):
        lst[t-1]=k
for l in lst:
    print(l)
