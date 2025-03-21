def dfs(c) :
    global ans
    v[c] = 1 # 단위 작업
    ans += 1 # 단위 작업
    
    for n in adj[c] : # C 와 연결된 노드를 방문 (다음 노드 next)
        if not v[n] : # 만약에 방문한 노드가 아니먄
            dfs(n) # dfs 로 해당되는 노드를 방문

# 여기까지 하고 함수 만들기
N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)  # 양방향 그래프이므로 반대 방향도 추가
    
ans = 0
v = [0] * (N+1)
dfs(1)

print(ans-1)