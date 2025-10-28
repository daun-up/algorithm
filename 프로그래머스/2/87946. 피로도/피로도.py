def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(hp, cnt):
        nonlocal answer  # 외부 변수 answer 수정하기 위해
        answer = max(answer, cnt)  # 최댓값 갱신
        
        for i in range(len(dungeons)):
            need, consume = dungeons[i]  # 최소 필요 피로도, 소모 피로도
            
            # 조건: 필요 피로도 충족 & 아직 방문 안 함
            if hp >= need and not visited[i]:
                visited[i] = True
                dfs(hp - consume, cnt + 1)  # 피로도 소모하고 던전 수 +1
                visited[i] = False  # 백트래킹: 다른 경로 탐색 위해 복구
        
    dfs(k, 0)
    return answer