n, m = map(int,input().split())

def factorial(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2,n+1) :
        dp[i] = dp[i-1] * i
    return dp[i]

print(factorial(n)//(factorial(m)*factorial(n-m)))
