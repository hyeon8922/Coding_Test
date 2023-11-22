import sys
n = int(input())
present = list(map(int, sys.stdin.readline().split()))

cnt = 1
ans = cnt
while cnt <= min(present):
    t=0
    for i in present:
        t+=1
        if (i % cnt) == 0: 
            if t == n:
                ans = cnt
        else:
            break
        
    cnt+=1
    
print(ans)
