import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    coin = map(int,input().split())
    m = int(input())

    dp = [0] * 10001
    dp[0] = 1

    for i in coin :
        for j in range(1, m+1) :
            if j - i >= 0 :
                dp[j] += dp[j - i]
    print(dp[m])