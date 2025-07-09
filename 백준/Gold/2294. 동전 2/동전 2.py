# 동전 1 처럼 경우의 수가 아니라 동전의 최소 개수 구하기
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

INF = int(1e9)
dp = [INF] * (k+1)
dp[0] = 0

for coin in coins :
    for i in range(coin,k+1) :
        dp[i] = min(dp[i-coin] + 1, dp[i])
        
print(dp[k] if dp[k] != INF else -1)