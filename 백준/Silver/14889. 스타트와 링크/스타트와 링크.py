n = int(input())

peoples = [list(map(int,input().split())) for _ in range(n)]

min_gap = float('inf') # 최소 값 갱신
visited = [False] * n

def dfs(depth, idx):
    global min_gap
    
    if depth == n//2:
        # 팀 결성이 끝나면
        
        start, link = 0,0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += peoples[i][j]
                elif not visited[i] and not visited[j]:
                    link += peoples[i][j]
        min_gap = min(min_gap, abs(start - link))
        return
    
    for i in range(idx, n): # 이전 단계에서 선택한 사람 이후(i+1)부터만 탐색
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False
dfs(0, 0)
print(min_gap)