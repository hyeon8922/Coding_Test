from collections import deque
def solution(n, edge):
    answer = 0
    edge.sort()
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for (a, b) in edge:
        graph[a] += [b]
        graph[b] += [a]
        
    visited[1] = 1
    q = deque([1])
    while q:
        c = q.popleft()
        for nx in graph[c]:
            if visited[nx] == 0:
                q.append(nx)
                visited[nx] = visited[c] +1
                
    print(visited)
    answer = visited.count(max(visited))
    return answer