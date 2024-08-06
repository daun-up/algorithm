n = int(input())

if n == 1 :
    print(1)
else :
    dp = [0] * n
    dp[0] = 1 # 한 자리 수는 1 한 개
    dp[1] = 1 # 두 자리는 10 한 개 ( 11 은 안 되므로 )
    for i in range(2, n) :
        dp[i] = dp[i-2] + dp[i-1] # '101' 로 시작하는 경우 + '100' 으로 시작하는 경우
    print(dp[n-1])
        