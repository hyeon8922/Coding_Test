#10813

n,m=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(i+1)
for k in range(m):
    i,j=map(int, input().split())
    lst[i-1],lst[j-1]=lst[j-1],lst[i-1]
for t in lst:
    print(t,end=' ')

# list 한 줄에 변경하면 교환으로 가능(=swap). 나눠서하면 차레로 변경돼서 교환이 되지 않음.
