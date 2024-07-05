# m과 n을 입력받습니다.
m, n = map(int, input().split())

# 소수인지 판별하는 함수입니다.
def is_prime_number(x):
    if x < 2:  # 2보다 작은 숫자는 소수가 아닙니다.
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# m에서 n까지의 숫자 중 소수를 찾아 출력합니다.
for i in range(m, n + 1):
    if is_prime_number(i):
        print(i)
