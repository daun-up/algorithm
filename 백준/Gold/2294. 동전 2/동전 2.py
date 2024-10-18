n, k = map(int,input().split())

sset = set() # 중복 제거

for _ in range(n) :
    sset.add(int(input()))
    
INF = k + 1
dp = [INF]*(k+1)
dp[0] = 0

for coin in sset :
    for j in range(1, k + 1) :
        if (j - coin) >= 0 :
            dp[j] = min(dp[j], dp[j-coin]+1)

answer = dp[k] 
if answer == INF :
    answer = -1

print(answer)