n = int(input())
answer = 0

for i in range(1, n + 1):
    answer += i * (n // i)
    # i 가 약수로서 등장한 횟수 * i 값 = 모든 약수의 총합

print(answer)