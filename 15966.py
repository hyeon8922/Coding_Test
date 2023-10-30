n=int(input())
arr=list(map(int,input().split()))
lst=[[] for i in range(len(arr))]
j,t=0,1
for i in range(len(arr)):
    a=arr[i]
    lst[j].append(a)
    t=i+1
    while t<len(arr):
        if a+1==arr[t]:
            lst[j].append(arr[t])
            a=arr[t]
        t+=1
    j+=1
max=0
for k in lst:
    if len(k)>=max:
        max=len(k)
print(max)
