def solution(a, b):
    answer = 1234567890
    tmp = 0
    for i in range(len(a)) :
        tmp += a[i]*b[i]
    answer = tmp
    return answer