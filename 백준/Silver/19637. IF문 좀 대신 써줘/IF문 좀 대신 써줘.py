# n, m = map(int, input().split())

# tmp = []
# for _ in range(n):
#     name, num = input().split()
#     tmp.append([name, int(num)])

# level = [int(input()) for _ in range(m)]

# for d in level:
#     for i in range(n):
#         if d <= tmp[i][1]:
#             print(tmp[i][0])
#             break  # 조건 만족 시 즉시 종료


# 시간 초과로 인해 이진 탐색으로 재풀이
import sys
input = sys.stdin.readline

# from bisect import bisect_left

n, m = map(int, input().split())

level = []

for _ in range(n):
    name, limit = list(input().split())
    level.append((name, int(limit)))

def binary_search(x):
    left = 0
    right = n
    
    while left < right:
        mid = (left + right) // 2
    
        if x > level[mid][1]: # 전투력이 현재 상한보다 크면
            left = mid + 1 # 오른쪽 구간 탐색
        else: 
            right = mid # 조건을 만족하므로 왼쪽 구간을 줄임
    
    return level[left][0] # 칭호를 반환


for _ in range(m):
    x = int(input())
    
    print(binary_search(x))    
