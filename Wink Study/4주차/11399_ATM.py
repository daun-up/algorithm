import sys
input = sys.stdin.readline

n = int(input())
p_list = list(map(int,input().split()))
p_list.sort() # 최솟값을 찾기 위함
sum = 0

for i in range(n):
    for j in range(i+1):
        sum += p_list[j]

print(sum)