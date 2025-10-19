def solution(n):
    # 리스트로 만들어서 첫 번째 요소를 꺼냄
    return [x for x in range(1, n) if n % x == 1][0]

#     answer = 0
#     i = 0
#     for i in range(1,n):
#         if n % i == 1:
#             answer = i
#             break
        
        
#     return answer

