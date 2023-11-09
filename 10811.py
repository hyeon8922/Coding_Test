#10811

n,m=map(int, input().split())
lst=[i+1 for i in range(n)]
lst_new=lst.copy()
for i in range(m):
    i,j=map(int, input().split())
    for k in range(j-i+1):
        lst_new[k+i-1]=lst[j-k-1]
    lst=lst_new.copy()
for t in lst:
    print(t,end=' ')

# 같은 주소로 대입하면 같이 바뀌어 버리므로 copy하는게 >>매우중요<< 같이 안 바뀜.

# lst2=lst1[:]

# lst2=list[lst1]

# lst2=lst1.copy()
