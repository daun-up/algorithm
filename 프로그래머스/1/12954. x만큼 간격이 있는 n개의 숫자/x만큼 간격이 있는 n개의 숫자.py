def solution(x, n):
    answer = []
    tmp = x
    while n > 0:
        n -= 1
        answer.append(tmp)
        tmp += x
    return answer