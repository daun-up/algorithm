n = int(input())

# for i in range(n) :
#     data = list(map(int,input().split()))

data = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)] # 0 으로 dp 초기화
dp[0] = data[0]

for i in range(1, n) :
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0] # 빨간색 0
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1] # 초록색 1
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2] # 파란색 2

print(min(dp[-1]))