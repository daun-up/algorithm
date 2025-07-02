import sys
sys.setrecursionlimit(10**6)

# 8방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1,  0,  1, 1, 1,  0, -1, -1]


def dfs (y, x) :
    if y < 0 or y >= h or x < 0 or x >= w or grid[y][x] != 1 :
        return
    grid[y][x] = 0
    for i in range(8) :
        ny = y + dy[i]
        nx = x + dx[i]
        dfs(ny, nx)


while True :
    w, h = map(int,input().split())
    # 입력 종료 조건
    if w == 0 and h == 0:
        break
    grid = [list(map(int,input().split())) for _ in range(h)]
    count = 0
    
    for y in range(h) :
        for x in range(w) :
            if grid[y][x] == 1 :
                dfs(y, x)
                count += 1
    print(count)