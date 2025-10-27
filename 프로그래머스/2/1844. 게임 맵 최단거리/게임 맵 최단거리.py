from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    dist = [[0]*m for _ in range(n)]
    
    # 시작 칸이 벽이면 바로 불가능
    if maps[0][0] == 0:
        return -1
    
    q = deque()
    q.append((0,0))
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    dist[0][0] = 1
    
    while q:
        x, y = q.popleft() # 현재 요소
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return dist[n-1][m-1] if dist[n-1][m-1] != 0 else -1