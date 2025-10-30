from collections import deque

n, k = map(int,input().split())
MAX = 100000

def bfs(start):
    dist = [-1] * (MAX + 1)
    
    q = deque()
    q.append(start)
    
    dist[start] = 0 # 시작점은 방문하고 시작하느 거니까
    
    while q:
        cur = q.popleft()
        
        if cur == k:
            return dist[cur]
        
        for nxt in (cur + 1, cur - 1, cur * 2):
            if 0 <= nxt <= MAX and dist[nxt] == -1:
                # nxt 가 범위 안에 있는지를 먼저 생각해야함
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return -1

print(bfs(n))
        
    