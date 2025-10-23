def solution(s):
    answer = ''
    s = list(s)
    tmp = len(s) // 2

    if len(s) % 2 == 0:
        answer += s[tmp-1]
        answer += s[tmp]
    else:
        answer += s[tmp]
    return answer