# import sys
# input = sys.stdin.readline

n = int(input())

list = list(map(int,input().split()))

dp = [1] * n
result = []

for i in range(n) :
    for j in range(i) :
        if list[i] > list[j] :
            dp[i] = max(dp[i] ,dp[j]+1) # i 에서의 최적의 해를 갱신해준다.
            
max_length = max(dp) # 가장 긴 증가하는 부분의 길이
m = max_length
for i in range(n-1, -1, -1):
    if dp[i] == m :
        result.append(list[i])
        m -= 1
result.reverse()
print(max_length)
print(" ".join(map(str, result)))

