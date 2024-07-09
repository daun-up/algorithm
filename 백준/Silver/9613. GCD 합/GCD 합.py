t = int(input())
answer = 0

def gcd(a,b) :
    while b != 0 :
        a, b = b, a % b
    return a

for _ in range(t):
    nums = list(map(int,input().split()))
    answer = 0
    for i in range(1, len(nums)):
        for j in range(i+1, len(nums)) :
            answer += gcd(nums[j], nums[i])
            
    print(answer)
    
    