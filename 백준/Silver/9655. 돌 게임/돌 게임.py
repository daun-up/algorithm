n = int(input())

# 턴을 번갈아가면서 돌 가져감
# 1 개 또는 3 개 가져갈 수 있음 <- 이거 식을 어떻게 세우지?
# 마지막 돌 가져간 사람 WIN
# 상근이가 먼저 시작

# dp = [0 for i in range(n+1)]

# dp[1] = 1
# dp[2] = 2
# dp[3] = 1

# for i in range(4, n+1) :
#     dp[n] = min(dp[n-1], dp[n-3]) + 1
    
# if dp[n] % 2 == 1 :
#     print('SK')
# else :
#     print('CY')

if n % 2 == 1 :
    print('SK')
else :
    print('CY')