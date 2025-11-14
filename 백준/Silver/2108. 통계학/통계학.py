import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())

arr = [int(input()) for _ in range(n)]

# 평균
print(round(sum(arr) / n)) # 반올림
# // 은 버림 나눗셈임

# 중앙값
arr.sort()
print(arr[n//2])

# 최빈값
cnt = Counter(arr)
freq = cnt.most_common()

max_freq = freq[0][1] # 최빈값의 값
modes = [x for x, f in freq if f == max_freq] # 최빈값의 값과 값이 같을 때의 숫자 값 배열
modes.sort()

if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(max(arr) - min(arr))