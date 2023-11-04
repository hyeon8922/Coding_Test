#1978
n=int(input()) 
arr=list(map(int,input().split())) 
lst=[] 
if 1 in arr: 
    arr.remove(1) 
for i in arr: 
    cnt=0 
    for j in range(2,i): 
        if i%j==0: 
            cnt+=1 
    if cnt==0: 
        lst.append(i) 
print(len(lst))
