n=int(input())
arr=[]
cnt=0

for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x: (x[1], x[0]))
now=[0,0]
for i in arr:
    if now[1]<=i[0]:
        cnt+=1
        now=i
print(cnt)

# sort(key=lambda x: (x[1],x[0])) : x[1]로 먼저 오름차순, x[0]으로 오름차순. 앞에 - 붙이면 내림차순
