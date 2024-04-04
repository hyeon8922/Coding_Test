from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        cnt = 0
        c = q.popleft()
        for i in q:
            cnt+=1
            if c > i:
                break
        answer.append(cnt)
    return answer