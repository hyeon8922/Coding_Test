N, K = map(int, input().split())
lst = list(map(int, input().split()))
x = []
for i in range(N):
    for j in range(N):
        a, b = lst[i], lst[j]
        x.append((a, b))
x.sort()
print(x)
