#9063

n=int(input())
x=[0 for _ in range(n)]
y=[0 for _ in range(n)]
for i in range(n):
    x[i],y[i]=map(int,input().split())
print((max(x)-min(x))*(max(y)-min(y)))
