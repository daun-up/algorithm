n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

p = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        p[i+1][j+1] = (p[i][j+1] + p[i+1][j] - p[i][j] + data[i][j])
        # data의 (0,0)부터 (a-1, b-1)까지 전부 더한 값

def rect_sum(r1, c1, r2, c2):
    return p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]

# print(*p)

answer = 0

# 마지막 행/열은 i+1, j+1이 없으니 제외

# 꼭짓점 경우의 수 돌기

# ↘ 케이스

# i, j 는 두 네모가 만나는 모서리 점
for i in range(n-1):
    for j in range(n-1):
        cnt = {}
        
        # 왼쪽 위 땅
        for r1 in range(i+1):
            for c1 in range(j+1):
                s = rect_sum(r1, c1, i, j)
                cnt[s] = cnt.get(s,0) + 1 # 이 합이 몇 번 나왔는지 기억하도록 함
        
        # 오른쪽 아래 땅
        for r2 in range(i+1, n):
            for c2 in range(j+1, n):
                s = rect_sum(i+1, j+1, r2, c2)
                # cnt[s] = cnt.get(s,0) + 1
                answer += cnt.get(s, 0) # 합이 s 인 cnt 값을 answer 에 추가함
        
        
# # ↙ 케이스
for i in range(n-1):
    for j in range(n-1):
        cnt = {}
        
        # NE (오른쪽 위): (r1, j+1) ~ (i, c2)
        for r1 in range(i+1):
            for c2 in range(j+1, n):
                s = rect_sum(r1, j+1, i, c2)
                cnt[s] = cnt.get(s,0) + 1
                
        # SW (왼쪽 아래): (i+1, c1) ~ (r2, j)
        for r2 in range(i+1, n):
            for c1 in range(j+1):
                s = rect_sum(i+1, c1, r2, j)
                answer += cnt.get(s,0)

print(answer)