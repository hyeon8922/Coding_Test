#10818

n=int(input())
lst=list(map(int, input().split()))
print(min(lst),end=' ')
print(max(lst))

#함수 사용

 

n=int(input())
lst=list(map(int, input().split()))
min=lst[0]
max=lst[0]
for i in range(n):
    if lst[i]>max:
        max=lst[i]
for i in range(n):
    if lst[i]<=min:
        min=lst[i]
print(min,max)

#반복문 사용
