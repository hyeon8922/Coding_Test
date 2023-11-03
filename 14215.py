#14215

x=list(map(int,input().split()))
if sum(x)-max(x)<=max(x):
    print((sum(x)-max(x))*2-1)
else:
    print(sum(x))
