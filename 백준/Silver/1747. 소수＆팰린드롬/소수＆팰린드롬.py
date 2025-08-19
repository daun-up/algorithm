n = int(input())

# 1. n 보다 크거나 같고
# 2. 소수이면서
# 3. 팰린드롬인 수 (숫자 순서를 뒤집은 수가 일치하는 수)

def is_prime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def is_palindrome(n) :
    n = str(n)
    if n == n[::-1] :
        return True
    else :
        return False

while True :
    if is_prime(n) and is_palindrome(n) :
        print(n)
        break
    n += 1