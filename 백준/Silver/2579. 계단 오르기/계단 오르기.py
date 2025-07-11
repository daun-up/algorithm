n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * n # dp[i]는 i번째 계단까지 왔을 때 얻을 수 있는 최대 점수

if n <= 2 :
    print(sum(arr))
else :
    # 첫 번째 계단까지의 최대 점수는 arr[0] (0번 인덱스)
    dp[0] = arr[0]
    # 두 번째 계단까지의 최대 점수는 arr[0] + arr[1] (연속 두 칸 밟기 가능)
    dp[1] = arr[0] + arr[1]
    # 세 번째 계단부터는 연속 세 칸을 밟을 수 없으므로 두 가지 경우 중 최대값 선택
    # 1. 첫 번째 계단 → 세 번째 계단 (arr[0] + arr[2])
    # 2. 두 번째 계단 → 세 번째 계단 (arr[1] + arr[2])
    # 단, 위 조건이 성립하려면 그 이전 계단을 건너뛴 구조여야 함
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    
    
    # 경우 1: i-2 → i
    # → i-1을 밟지 않고 두 칸 점프
    
    # 경우 2: i-3 → i-1 → i
    # → i-2는 쉬고, i-1과 i를 연속으로 밟음
    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
        
    # 마지막 계단(n-1)을 반드시 밟아야 하므로, dp[n-1]이 정답
    print(dp[n-1])