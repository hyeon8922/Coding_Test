#2292

n=int(input())
i=1
cnt=1
while n>1:
    n=n-(6*i)
    i+=1
    cnt+=1
print(cnt)
