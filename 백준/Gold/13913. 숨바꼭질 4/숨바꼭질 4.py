from collections import deque

N, K = map(int,input().split())
cnt = 0
ans = []

def bfs(s,e) :
    v = [0] * 200001
    q = deque()
    q.append(s)
    v[s] = 1
    path = {} # 경로 추적용 딕셔너리
    while q :
        c = q.popleft() # 큐에서 현재 위치를 꺼내서 확인
        if c == e : # 목표 위치에 도착 -> 경로 복원
            route = []
            while c != s :
                route.append(c)
                c = path[c] # path[c] 를 따라 거슬러 올라가며 경로를 복원함
            route.append(s)
            route.reverse() # 출발점 -> 도착점 순서로 변경
            return v[e] - 1, route
        
        for n in (c-1, c+1, c*2) :
            if 0 <= n <= 200000 and v[n] == 0 :
                q.append(n)
                v[n] = v[c] + 1
                path[n] = c  # 경로 저장
ans = bfs(N,K)
# print(cnt)
# 이동 횟수 출력
print(ans[0])

# 최단 경로 출력
print(*ans[1])