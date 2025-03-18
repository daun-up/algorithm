def solution(s):
    answer = ''
    tmp = s.split()
    center = int(len(s) / 2)
    for i in range(len(s)) :
        if len(s) % 2 == 0 :
            if i == center :
                answer += s[i-1]
                answer += s[i]
        else :
            if i == center :
                answer += s[i]
    return answer