n = int(input())
costs = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

dp[0] = costs[0] # 첫 행은 비용 그대로

for i in range(1,n) :
    # r,g,b = map(int,input().split())
    
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    # i 번째 집을 빨강 (0) 으로 칠한다고하면, 이전 집은 초록(1)이나 파랑(2)만 가능
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

result = min(dp[n-1]) # 모든 집 (n개) 를 다 칠했을 때 최소 비용은 마지막 집을 어떤 색으로 칠했는지에 따라 달라짐

print(result)