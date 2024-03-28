from collections import deque
def solution(s):
    answer = True
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if len(q) == 0:
                q.append(-1)
                break
            else:
                q.pop()
    if q:
        return False
    return True