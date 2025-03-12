def solution(n):
    answer = 0
    tmp = n ** 0.5
    if tmp % 1 == 0 :
        answer = 1
    else :
        answer = 2
    return answer