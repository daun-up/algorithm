from collections import deque
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

def bfs(node):
    visited = [0] * n
    
    q = deque()
    q.append(node)
    
    
    while q:
        u = q.popleft()
        for v in range(n):
            if graph[u][v] == 1 and not visited[v]:
                visited[v] = 1
                q.append(v)
    return visited

for i in range(n):
    print(*bfs(i))