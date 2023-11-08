#2563

n=int(input())
arr=[[0 for _ in range(100)] for _ in range(100)]
lst=[]
cnt=0
for _ in range(n):
    row=list(map(int, input().split(' ')))
    lst.append(row)
for i in range(n):
    for j in range(10):
        for k in range(10):
            arr[lst[i][0]-1+j][lst[i][1]-1+k]=1
for p in range(100):
    cnt+=arr[p].count(1)
print(cnt)

# 겹치는 부분 빼는 것보다 처음 배열에서 0>1으로 바꿔 마지막에 1을 세는 것이 쉬움.
