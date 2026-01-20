INF = 10**18

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())

    # 가중치 그래프로 입력 받기
    # u, v, d   

    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        u, v, d = map(int,input().split())
        graph[u].append((v,d))
        graph[v].append((u,d))

    # print(graph)

    # 트리를 만들었은 (1 번 섬을 root 로)

    # root = 1
    # parent = [0] * (n + 1)
    # pw = [0] * (n + 1) # 간선 가중치
    # depth = [0] * (n + 1) # 루트로부터 깊이
    # dist = [0] * (n + 1) # 루트로부터 가중치 합

    # stack = [root]
    # parent[root] = -1

    # while stack:
    #     u = stack.pop()
    #     for v, d in graph[u]:
    #         if v == parent[u]:
    #             continue
    #         parent[v] = u
    #         pw[v] = d
    #         depth[v] = depth[u] + 1
    #         dist[v] = dist[u] + d
    #         stack.append(v)
    
    # dist (가중치 합) 음음음음ㅇ믕ㅁ음
    # 루트(1)에서 각 리프(자식이 없는 노드)까지의 거리(dist) 중 최솟값
    # 이면 안 되는 게 중간에서 띨롱 끊어버릴 수도 있음... depth 별로 말단 노드라고 치고

    # 깊이 별 최소 비용

    # 몰라

    def dfs(u, parent_node):
        answer = 0

        is_leaf = True
        
        for v, d in graph[u]:
            if v == parent_node:
                continue

            is_leaf = False
            sub = dfs(v, u)
            answer += min(sub, d) # 서브트리에서 막기 vs 간선에서 막기

        if is_leaf:
            return INF
        
        return answer
    
    if n == 1:
        print(0)
    else:
        print(dfs(1,0)) # 1 번 섬에서 시작하니까? 아닌 거 같은데...

    
    # for v in range(1, n+1):
    #     # print(parent[v])  
    #     print(f"{v} : {parent[v]} ({pw[v]})")  
    
