from collections import deque
def solution(operations):
    q = []
    
    for i in operations:
        a, b = i.split()
        if a == 'I':
            q.append(int(b))
            q.sort()
        else:
            if len(q) == 0:
                continue
            elif int(b) == 1:
                q.pop(-1)              
            else:
                q.pop(0)
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [q[-1], q[0]]
    return answer
