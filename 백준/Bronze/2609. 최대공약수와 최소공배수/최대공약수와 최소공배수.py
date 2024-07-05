n, m = map(int, input().split())

# 반복문
def gcd(a,b) :
    while b != 0 :
        a, b = b, a % b
    return a

# 재귀 함수
# def gcd (a,b) :
#     if b == 0 :
#         return a
#     return gcd(b, a % b)
    
 
def lcm(a,b) :
    return a * b // gcd(a,b)
    
print(gcd(n,m))
print(lcm(n,m))
