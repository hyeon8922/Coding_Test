def solution(n):
    answer = 0
    cnt = 0
    lst = []
    for i in range(n//2+1):
        cnt+=i
        if cnt < n:
            lst.append(cnt)
        else:
            break
    print(lst)
    for j in range(len(lst)):
        if ((n - lst[j]) % (j+1)) == 0:
            answer+=1
    return answer


#6n + 15
#5n + 10
#n, n+1, n+2, n+3 = 4n + 6
#n, n+1, n+2 = 3n+3
#n, n+1 = n+1
#n = n