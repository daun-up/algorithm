def solution(absolutes, signs):
    # answer = 123456789
    answer = 0
    for a,s in zip(absolutes,signs):
        if s == False:
            answer -= a
        elif s == True:
            answer += a
    return answer