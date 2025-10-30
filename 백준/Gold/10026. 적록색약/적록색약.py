import sys
sys.setrecursionlimit(1_000_000) 

n = int(input())

# arr = [list(i for i in input()) for _ in range(n)]
arr = [list(input()) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    stack = []
    stack.append((x,y))
    visited[x][y] = True
    
    while stack:
        x,y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n):
                if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
            # 겉으로 붙어 있는(4방향) 같은 색만 재귀로 이어라
            # dfs(nx,ny)

            


normal = 0
# 새로운 색 덩어리를 발견할 때마다 DFS로 모두 방문 표시
for i in range(n): # 전체 행 순회
    for j in range(n): # 전체 열 순회
        if not visited[i][j]: # 아직 방문 안 한 칸이면
            dfs(i,j) # 그 칸을 시작점으로 DFS 실행
            normal += 1 

# 빨간색과 초록색의 차이를 느끼지 못하므로, 빨강 초롱 모두 빨강으로 그래프를 바꿈 
# arr = [[('R' if c in ('R', 'G') else 'B') for c in row] for row in arr]
arr = [[('R' if color in ('R', 'G') else 'B') for color in row] for row in arr]


visited = [[False] * n for _ in range(n)]

weak = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            weak += 1
print(normal, weak)