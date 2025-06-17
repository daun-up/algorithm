# 가장 큰 수와 가장 작은 수를 구해서 곱하면 됨
n = int(input())

data = list(map(int,input().split()))

max_tmp = max(data)
min_tmp = min(data)

print(max_tmp * min_tmp)