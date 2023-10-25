x=int(input())
m=list(map(int,input().split()))
n=list(map(int,input().split()))

result=0
n.remove(n[-1])

mi=n.index(min(n))
for i in range(len(m)-mi):
    result+=n[mi]*m[mi+i]

while mi>0:
    mii=n.index(min(n[0:mi]))
    for i in range(mi-mii):
        result+=n[mii]*m[mii+i]
    if mii==0:
        break
    mi=mii

print(result)
