import sys
input = sys.stdin.readline

n = input().strip()
result = 0

# i가 1부터 len(n)-1까지 반복
for i in range(1, len(n)) :
    result += 9 * 10 ** (i-1) * i
    # 1자리 숫자: 1부터 9까지 9개 (1자리의 수: 9 * 10^0 * 1)
    # 2자리 숫자: 10부터 99까지 90개 (2자리의 수: 9 * 10^1 * 2)
    # 3자리 숫자: 100부터 999까지 900개 (3자리의 수: 9 * 10^2 * 3)
result += (int(n)-10 ** (len(n)-1) +1)*len(n)
# (int(n) - 10 ** (len(n)-1) + 1)는 n이 속한 자리수의 숫자 개수를 계산
print(result)