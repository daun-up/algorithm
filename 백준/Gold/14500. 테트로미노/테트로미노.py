def dfs (depth, sum, tmp) : # backtracking
    global answer
    if depth == 4 :
        answer = max(answer, sum)
        return
    
    for ci, cj in tmp : # ci, cj -> 현재 위치 도형의 모든 위치에서 네 방향
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) : # 상하좌우
            ni, nj = ci + di, cj + dj # 다음 위치는 현재 위치 + 다음 방향
            # 범위 내 미방문이면 다음 단계로
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 :
                visited[ni][nj] = 1
                dfs (depth + 1, sum + arr[ni][nj], tmp + [(ni, nj)])
                visited[ni][nj] = 0



n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 행열
answer = 0

for i in range(n) :
    for j in range(m) : # 가능한 모든 위치에서 dfs 탐색
        visited[i][j] = 1 # 현재 위치니까 방문한 위치지!
        dfs(1, arr[i][j], [(i,j)])
print(answer)
    