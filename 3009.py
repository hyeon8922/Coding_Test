x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=list(map(int,input().split()))
a=[x[0],y[0],z[0]]
b=[x[1],y[1],z[1]]
for i in a:
    if a.count(i)==1:
        x1=i
for i in b:
    if b.count(i)==1:
        y1=i      
print(x1,y1)  
