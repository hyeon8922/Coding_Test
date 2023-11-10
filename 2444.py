#2444

t=int(input())
for k in range(t):
    print(' '*((t-1)-k)+'*'*(k*2+1))
for i in range(t-1):
    print(' '*(i+1)+'*'*((t*2-3)-i*2))

 
