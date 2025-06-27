import sys
sys.setrecursionlimit(10000) 

n, m = map(int, input().split())  # 정점, 간선 개수

graph = [[] for _ in range(n + 1)] 

count = 0
# visited = [[0] * m for _ in range(n)]
visited = [False] * (n + 1)  # 방문 여부

# 그래프 입력 받기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 함수 정의
def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

# 연결 요소 개수 세기
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)