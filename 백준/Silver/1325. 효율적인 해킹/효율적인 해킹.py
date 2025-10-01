from collections import deque

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    q = deque()
    # q.append([x])
    q.append(start)
    
    cnt = 0
    visited = [0] * (n+1)
    visited[start] = 1
    
    while(q):
        node = q.popleft()
        
        for next in graph[node]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)
                cnt += 1
    return cnt

tmp = []

for i in range(1, n+1):
    tmp.append(bfs(i)) # 컴퓨터에 매겨진 번호는 n 

for i in range(n):
    if tmp[i] == max(tmp):
        print(i+1, end=' ')