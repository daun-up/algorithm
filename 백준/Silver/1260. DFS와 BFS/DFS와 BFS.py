def dfs(c):  # 현재 노드 : current
    ans_dfs.append(c)  # 방문 노드 추가
    v[c] = 1  # 방문 표시
    
    for n in adj[c]:
        if not v[n]:  # 방문하지 않은 노드이면 DFS 수행
            dfs(n)

def bfs(s):  # 현재 노드 : start
    q = []  # 큐 초기화
    q.append(s)  # Q 에 초기 데이터 삽입
    ans_bfs.append(s)  # 방문 노드 추가
    v[s] = 1  # 방문 표시
    
    while q:
        c = q.pop(0)  # 큐에서 노드 꺼내기
        for n in adj[c]:
            if not v[n]:  # 방문하지 않은 노드이면 큐에 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N, M, V = map(int, input().split())  # 노드 수, 간선 수, 시작 노드
adj = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)  # 양방향 그래프이므로 반대 방향도 추가

# [1] 오름차순 정렬 (문제에서 작은 번호부터 방문해야 하는 경우)
for i in range(1, N + 1):
    adj[i].sort()

# DFS 실행
v = [0] * (N + 1)  # 방문 리스트 초기화
ans_dfs = []
dfs(V)  # 시작 노드로 DFS 실행

# BFS 실행
v = [0] * (N + 1)  # 방문 리스트 초기화
ans_bfs = []
bfs(V)  # 시작 노드로 BFS 실행

print(*ans_dfs)
print(*ans_bfs)