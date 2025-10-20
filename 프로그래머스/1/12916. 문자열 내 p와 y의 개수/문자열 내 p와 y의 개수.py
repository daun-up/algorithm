def solution(s):
    # answer = True
    
    return s.lower().count('p') == s.lower().count('y')

    # 먼저 대문자 혹은 소문자로 통일
#     s = s.lower()
#     p = 0
#     y = 0
    
#     for i in s:
#         if i == 'p':
#             p += 1
#         elif i == 'y':
#             y += 1
    
#     if p == y:
#         return True
#     else:
#         return False