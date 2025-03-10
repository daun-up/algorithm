def solution(n, t):
    answer = 0
    answer += n
    for _ in range(0,t) :
        answer += n
        n = 2*n
    return answer