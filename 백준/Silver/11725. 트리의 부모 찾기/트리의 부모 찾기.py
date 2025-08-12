import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1) : # n 개의 노드를 가질 때 항상 n-1 개의 간선(연결선) 을 가짐
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(curr) :
    visited[curr] = True
    for next in tree[curr] :
        if not visited[next] :
            parent[next] = curr
            dfs(next)
            
dfs(1)

for i in range(2, len(parent)):
    print(parent[i])