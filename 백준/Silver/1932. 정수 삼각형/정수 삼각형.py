n = int(input())
tree = []

for _ in range(n):
    tree.append(list(map(int, input().split())))

# DP 테이블 생성 (tree와 동일한 크기)
dp = [[0] * (i + 1) for i in range(n)]

# DP 테이블의 첫 번째 값은 삼각형의 꼭대기 값과 같음
dp[0][0] = tree[0][0]

# 동적 계획법으로 DP 테이블을 채움
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tree[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + tree[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tree[i][j]

print(max(dp[n - 1]))