from collections import deque

# 입력 받기 (가로 M, 세로 N)
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 큐 초기화: 익은 토마토(1)의 위치를 모두 넣음
queue = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue.append((i, j))

# 방향 설정: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 시작
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] # 다음 좌표는 현재 좌표 + 상하좌우 
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0: # grid 내에 존재하고 안 익은 토마토일 때
            grid[nx][ny] = grid[x][y] + 1 # 다음 좌표는 현재 좌표 숫자 day + 1
            queue.append((nx, ny))


max_days = 0

for row in grid:
    for cell in row:
        if cell == 0:
            print(-1)  # 익지 못한 토마토 있음
            exit(0)
    max_days = max(max_days, max(row))

# 최소 일수 = 최댓값 - 1 (처음 시작이 1이었으므로)
print(max_days - 1)