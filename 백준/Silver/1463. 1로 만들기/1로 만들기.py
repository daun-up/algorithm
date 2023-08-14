x = int(input())
dp = [0]*(x+1) # dp = 각 인덱스의 숫자가 1 이 되는데 필요한 연산의 최솟값
# 크기가 (x+1) 인 배열로 선언 / 동적 계획법을 이용하여 배열의 값을 갱신하며 숫자를 1 로 만드는데 필요한 최소 연산 횟수를 계산해 나갈 것

for i in range(2, x+1) :
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i // 3] + 1)


print(dp[x])
