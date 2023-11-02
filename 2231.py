#1)
n=int(input())
cnt=0
for i in range(n//2,n):
    t=list(map(int,str(i)))
    if sum(t)+i==n:
        print(i)
        cnt=1
        break
if cnt==0:
    print(0)

#2)
n=input()
arr=[]
cnt=0
for i in n:
    arr.append(int(i))
n=int(n)
for j in range(n//2,n):
    result=j
    for k in range(len(arr)):
        result+=((j%(10**(k+1)))-(j%(10**k)))/(10**k)
    if n==result:
        print(j)
        cnt=1
        break
if cnt==0:
    print(0)
