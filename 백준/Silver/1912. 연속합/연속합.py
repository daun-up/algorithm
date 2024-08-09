n = int(input())
list = list(map(int,input().split()))

dp = [0] * n

for i in range(n) :
    dp[i] = max(list[i], dp[i-1] + list[i])
    
print(max(dp))