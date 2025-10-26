from itertools import permutations

def isPrime(x):
    x = int(x)
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    tmp = set()
    
    for i in range(1,len(numbers)+1):
        for num in permutations(numbers,i):
            # tmp.add(''.join(num))
            tmp.add(int(''.join(num))) 

    for t in tmp:
        if isPrime(t):
            answer += 1
    
    return answer