#25304

X=int(input())
N=int(input())
last=0
while N>0:
    a,b=map(int, input().split())
    last+=a*b
    N-=1
if X==last:
    print('Yes')
else:
    print('No')

 
