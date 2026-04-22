from itertools import permutations

def isPrime(x):
    # 1과 자기 자신으로만 나누어떨어지는 수
    if x < 2:
        return False
        
    for i in range(2, int(x ** 0.5) + 1):
        # 모두 확인하면 비효율적이니까 제곱근까지만 확인해도 됨
        if x % i == 0:
            return False
        
    return True
    
def solution(numbers):
    answer = 0
    nums = set()
    
    # for i in range(1, len(numbers) + 1):
    #     nums.add(int(''.join(permutations(numbers, i))))
    
    for i in range(1, len(numbers) + 1):
        # print(list(permutations(numbers, i)))
        for p in permutations(numbers, i):
            # print(p)
            nums.add(int(''.join(p)))
    
    for num in nums:
        # print(num)
        if isPrime(num):
            answer += 1
            
    return answer