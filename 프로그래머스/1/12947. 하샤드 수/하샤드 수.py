def solution(x):
    return x % sum(int(x) for x in str(x)) == 0

#     answer = True
#     ls = [int(i) for i in str(x)]
#     s = sum(ls)
    
#     if (x % s) == 0:
#         answer = True
#     else:
#         answer = False
#     return answer