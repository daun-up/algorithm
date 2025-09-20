n = int(input())

str_n = str(n)

# 등차수열 판별 공식
def is_hansu(n):
    if n < 100:
        return 1
    else:
        a = n // 100
        b = (n // 10) % 10
        c = n % 10
        if a - b == b - c:
            return 1
        else:
            return 0

# n 보다 작거나 같은 한수의 '개수' 의 누적합을 출력
tmp = 0
for i in range(1, n+1):
    tmp += is_hansu(i)

print(tmp)
    