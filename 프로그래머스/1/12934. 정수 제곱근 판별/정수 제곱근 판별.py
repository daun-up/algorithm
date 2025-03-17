def solution(n):
    answer = 0
    tmp = int(n ** 0.5)
    if n == tmp ** 2 :
        answer = (tmp+1)**2
    else :
        answer = -1
    return answer

# x값이 실수가 되는 케이스가 있기에 n의 제곱근을 정수화 시키는 것이 핵심
# 정수화 하지 않으면 x 값이 실수가 되는 케이스가 있고, return 값도 실수가 나오므로 오답이 됨