n = int(input())

list = list(map(int,input().split()))

dp = [1] * n
result = []


for i in range(n) :
    for j in range(i) :
        if list[i] < list[j] :
            dp[i] = max(dp[i], dp[j] +1)
print(max(dp))
