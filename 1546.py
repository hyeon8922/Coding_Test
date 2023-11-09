#1546

n=int(input())
lst=list(map(int,input().split()))
m=max(lst)
last=0
for i in lst:
    last+=(i/m*100)
print(last/len(lst))
