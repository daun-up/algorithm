from collections import deque

n, m, t = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

knife = None
# 그람의 위치 표시해두기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            knife = (i,j)
            break
    if knife:
        break

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(sx,sy):
    dist = [[-1]*m for _ in range(n)] # ??
    q = deque([(sx,sy)]) # 튜플로 넣기
    dist[sx][sy] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 + 벽 + 방문 체크
            
            # if knife:
            #     dist[nx][ny] = dist[knife[0]][knife[1]] + 
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist
    
    # for x,y in q:
    #     if 0 <= nx < n and 0 <= ny < m:
    #         graph[nx][ny] = dist[x][y] + 1
    #         q.append((nx,ny))
    
dist = bfs(0,0)

# 후보 1: 직행
tmp = [] # 후보 경로들을 저장함

# dist[i][j] 는 시작점에서 해당 칸 (i,j) 까지 가는 데 걸린 최단 시간을 저장한 2차원 배열
end = dist[n-1][m-1]
if end != -1:
    # dist 배열의 초기값은 -1 로 설정 -> 즉, 아직 방문하지 못한 칸은 -1
    # 따라서 end 가 -1 이면 공주님한테 갈 수 없었단 뜻 (벽 때문에 막혀 있다는 뜻)
    tmp.append(end) # 공주님께 갈 수 있었따면 저장

# 후보 2: 그람 경유
if knife:
    gx, gy = knife
    to_knife = dist[gx][gy] # 그람 까지 가는 데 걸린 거리
    
    # 가는 중에 그람이 있는 칸을 만나면 그 이후로는 벽을 무시하고 이동할 수 있음
    
    if to_knife != -1:
        # 그람을 집은 후 단순 맨해튼 거리로 계산 가능
        via_knife = to_knife + abs((n-1) - gx) + abs((m-1) - gy)
        tmp.append(via_knife)

if not tmp:
    print("Fail")
else:
    ans = min(tmp)
    print(ans if ans <= t else "Fail")