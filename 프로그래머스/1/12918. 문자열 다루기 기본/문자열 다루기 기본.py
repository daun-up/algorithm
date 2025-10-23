def solution(s):
    return s.isdigit() and len(s) in [4,6]
#     answer = True
#     if len(s) == 4 or len(s) == 6:
#         for i in s:
#             if i.isdigit():
#                 answer = True
#             else:
#                 answer = False
#                 break
#     else:
#         answer = False
        
#     return answer