n = int(input())

w = [[] for _ in range(n)]

for i in range(n):
    costs = list(map(int,input().split()))
    
    for j in range(n):
        # if costs[i] != 0:
        if costs[j] != 0:
            w[i].append((j,costs[j]))

min_cost = float('inf')

visited = [False] * n

def dfs(start, now, total_cost, depth):
    global min_cost
    
    # 종료 조건
    if depth == n:
        for nxt, cost in w[now]:
            if nxt == start:
                min_cost = min(min_cost, total_cost + cost)
        return
    
    visited[now] = True
    
    for nxt, cost in w[now]:
        if not visited[nxt]:
            if total_cost + cost <= min_cost:
                dfs(start, nxt, total_cost + cost, depth+1)
                # start 는 출발한 도시로, 갱신되지 않음
    
    visited[now] = False

for i in range(n):
    dfs(i,i,0,1)
    
print(min_cost)