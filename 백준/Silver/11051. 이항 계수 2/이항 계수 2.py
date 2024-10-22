n, k = map(int,input().split())

dp = [1 for _ in range(n + 1)] # 팩토리얼 값을 저장하기 위한 리스트


if n == k and k == 0 :
    print(dp[1])
else :
    for i in range(2, n + 1) :
        dp[i] = dp[i-1] * i
    print(dp[n] // (dp[k] * dp[n-k]) % 10007 ) # n C r 공식