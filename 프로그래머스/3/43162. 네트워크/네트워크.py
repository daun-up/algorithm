def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(cur):
        visited[cur] = True
        
        for next in range(n):
            if computers[cur][next] == 1 and not visited[next]:
                dfs(next)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer