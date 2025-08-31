n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

max_weight = 0

for i in range(n):
    weight = ropes[i] * (n - i) # i 번째 로프를 포함하면 총 n-1 개의 로프를 사용할 수 있음
    max_weight = max(max_weight, weight)

print(max_weight)
