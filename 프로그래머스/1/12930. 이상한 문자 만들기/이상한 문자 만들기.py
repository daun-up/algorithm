# def solution(s):
#     answer = ''
#     s_arr = s.split()
#     for s in s_arr:
#         for i in range(len(s)):
#             if i % 2 == 0:
#                 # s[i] = s[i].upper()
#                 s = s.replace(s[i], s[i].upper())
#             else:
#                 s = s.replace(s[i], s[i].lower())
#         answer += s
#     return answer

def solution(s):
    answer = []
    for word in s.split(' '):  # 공백 포함 split
        new_word = ''
        for i, ch in enumerate(word):
            if i % 2 == 0:
                new_word += ch.upper()
            else:
                new_word += ch.lower()
        answer.append(new_word)
    return ' '.join(answer)

# split(' ') → join(' ') 구조를 쓰면 원래의 공백 구조가 1:1로 복원
