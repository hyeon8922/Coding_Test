#4344

c=int(input())
lst=[]
for t in range(c):
    n=list(map(int, input().split()))
    av=sum(n[1:])/n[0]
    cnt=0
    for k in range(n[0]):
        if n[k+1]>av:
            cnt+=1
    lst.append(cnt/n[0]*100)
for j in lst:
    print(f'{j:.3f}%')
