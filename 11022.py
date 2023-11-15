#11022

x=int(input())
list=[]
listA=[]
listB=[]
n=1
while x>0:
    A,B=map(int, input().split())
    C=A+B
    list.append(C)
    listA.append(A)
    listB.append(B)
    x-=1
for i in list:
    print('Case #{}: {} + {} = {}'.format(n,listA[n-1],listB[n-1],i))
    n+=1
