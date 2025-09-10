from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    queue = deque()
    queue.append((x, y))
    
    while queue :
        x, y = queue.popleft()
        
        # 상하좌우 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # graph 를 삐져나갈 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            # 0 일 때는 못 가
            if graph[nx][ny] == 0 :
                continue
            
            if graph[nx][ny] == 1:  # 아직 방문하지 않은 길
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1] # 

print(bfs(0,0)) # 0,0 에서 시작하니까