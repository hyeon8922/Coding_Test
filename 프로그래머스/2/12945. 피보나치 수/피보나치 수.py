def solution(n):
    f = [0, 1]
    for i in range(1, n+1):
        f.append(f[i-1] + f[i])
    return f[n]%1234567