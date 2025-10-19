def solution(n):
    
    # num / 2 의 수들만 검사하면 성능 약 2배 향상
    return n + sum([i for i in range(1,(n//2) + 1) if n % i == 0])

#     answer = 0
#     tmp = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             tmp.append(i)
    
#     return sum(tmp)