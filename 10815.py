m=int(input())
lst1=list(map(int,input().split()))
n=int(input())
lst2=list(map(int,input().split()))
result=[]
for i in lst2:
    if i in lst1:
        result.append(1)
    else:
        result.append(0)
print(*result)
