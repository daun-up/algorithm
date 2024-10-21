n = int(input())

meetings = []

for _ in range(n) :
    start, end, people = map(int, input().split())
    # 각 회의는 이미 시간 순서대로 주어짐
    meetings.append((start, end, people))
    
dp = [0] * n
dp[0] = meetings[0][2]

for i in range(1,n) :
    # i 번째 회의까지 선택했을 떄의 최대 인원
    
    # 이전 회의를 선택하는 경우 : i 번째 회의를 택하지 않고 이전까지의 최대 인원을 가져옴
    # 현재 회의를 선택하는 경우 : i 번째 회의를 선택할 경우, 그 이전의 겹치지 않는 회의를 찾아서 그 회의까지의 최대 인원에 현재 회의의 인원을 더함
    dp[i] = max(dp[i-1], dp[i-2] + meetings[i][2])
    
    # 이 문제에서 i 번째 회의를 선택할 때 겹치지 않는 회의는 i-2 번째 회의임 (i 와 i-1 회의는 무조건 겹침)
    
print(dp[n-1])