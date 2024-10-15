import sys
input = sys.stdin.readline
def bfs (start,end) :
    # 큐, visited 배열, 필요 변수 생성
    q = []
    v = [0] * 200001
    
    # 초기 데이터 삽입 및 visited 초기화
    
    q.append(start)
    v[start] = 1
    
    while q :
        current = q.pop(0)
        for next in (current - 1, current + 1, current * 2) :
            if 0 <= next <= 200000 and v[next] == 0 :
                q.append(next)
                v[next] = v[current] + 1
        if current == end :
            return v[end] - 1
    # 이곳에 도달할 리는 없지만 
    return -1
                
    
n, k = map(int,input().split())
answer = bfs(n, k)
print(answer)

    