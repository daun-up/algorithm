n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

dp[0] = 1

for coin in coins :
    for i in range(coin, k+1) : # coin 보다 작은 수의 경우의 수는 변화가 없음
        dp[i] += dp[i-coin] # dp[i] 는 금액 i 를 만드는 방법의 수!
print(dp[k])