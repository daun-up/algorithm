import sys

input = sys.stdin.readline

n = int(input())
max_n = []

for _ in range(n) :
    nums = list(map(int,input().split()))
    max_n = sorted(max_n + nums, reverse=True)[:n]
print(max_n[n-1])
    