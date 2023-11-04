#2581
n=int(input()) 
m=int(input()) 
lst=[] 
for i in range(n,m+1): 
    if i == 1: 
        cnt=1 
        continue 
    cnt=0 
    for j in range(2,i): 
        if i%j==0: 
            cnt+=1 
            break 
    if cnt==0: 
        lst.append(i) 
if len(lst)==0: 
    print(-1) 
else: 
    print(sum(lst),min(lst),sep='\n')
