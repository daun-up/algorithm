# 1516 게임 개발
# 위상 정렬
from collections import deque

import sys
input = sys.stdin.readline

def sort(n, graph, indegree, time):
    result = time[:]
    q = deque()
    
    # 시작 노드 즉 진입 차수 0인 노드 
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            # 선행 건물 중 가장 오래 시간 걸린 경우 저장
            result[nxt] = max(result[nxt], result[cur] + time[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)
                
    return result

# 입력
n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1) # 각 노드 진입 차수
time = [0] * (n + 1) # 각 건물 짓는 데 걸리는 시간

for i in range(1, n + 1):
    data = list(map(int,input().split()))
    time[i] = data[0] # 해당 건물 짓는데 걸리는 시간
    
    for j in data[1:-1]:
        # j 번에서 i 번으로 가는 간선
        graph[j].append(i)
        indegree[i] += 1
    
result = sort(n, graph, indegree ,time)
# result 는 1-based
print('\n'.join(map(str, result[1:])))