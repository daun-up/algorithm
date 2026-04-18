# 플로이드
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# 인접 행렬
INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게로 가는 비용 0
for i in range(1, n + 1):
    graph[i][i] = 0
    
for _ in range(m):
    a, b, c = map(int,input().split())
    # 최소 비용만 저장
    graph[a][b] = min(graph[a][b], c)

# 시작 도시 a, 도착 도시 b, 비용 c
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for row in graph:
#     print(' '.join(map(lambda x : '0' if x == INF else str(x))))

for i in range(1, n + 1):
    print(' '.join(map(lambda x: '0' if x == INF else str(x), graph[i][1:])))