n,m=map(int,input().split())
lst=[]
cnt,i=0,-1
for i in range(n):
    lst.append(int(input()))
while m>0:
    cnt+=m//lst[i]
    m%=lst[i]
    i-=1
print(cnt)
