from heapq import *
def solution(n, k, enemy):
    if len(enemy)<=k:
        return len(enemy)
    q = []
    for i in range(len(enemy)):
        heappush(q, enemy[i])
        if len(q) > k:
            attack = heappop(q)
            if attack > n:
                return i
            n -= attack       
    return len(enemy)