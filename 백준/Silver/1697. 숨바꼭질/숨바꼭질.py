def bfs (s,e) :
    # 큐, v[], 필요 변수 생성
    v = [0] * 200001
    q = []
    # 초기데이터 삽입, v[] 초기화
    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if c == e :
            return v[e] - 1
        # 3 방향, 범위내 (0~200000), 미방문
        for n in (c-1, c+1, c*2) :
            if 0 <= n <= 200000 and v[n] == 0 :
                q.append(n)
                v[n] = v[c] + 1
    # 이곳에 도달할 리는 없겠지만
    return -1
        


N, K = map(int,input().split())
ans = bfs(N, K)
print(ans)
