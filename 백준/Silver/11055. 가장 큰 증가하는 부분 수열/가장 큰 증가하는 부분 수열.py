n = int(input())
a_list = list(map(int,input().split()))

dp = [0] * n

dp[0] = a_list[0]

for i in range(n) :
        for j in range(i) :
            if a_list[i] > a_list[j] :
                dp[i] = max(dp[i], dp[j] + a_list[i])
            else :
                dp[i] = max(dp[i], a_list[i])
                
print(max(dp))