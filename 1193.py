#1193

n=int(input())
k=0
start=1
while n>=start:
    k+=1
    start+=k
start=start-k
if k%2==0:
    print('%d/%d'%(n-start+1,k-n+start))
else:
    print('%d/%d'%(k-n+start,n-start+1))
