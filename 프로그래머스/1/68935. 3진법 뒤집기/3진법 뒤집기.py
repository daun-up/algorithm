def solution(n):
    answer = 0
    tmp = ''
    while n > 0 :
        tmp += str(n % 3)
        n = n // 3
    
    return int(tmp, 3) # int(숫자로 이루어진 문자열, 진법) -> 해당 진법으로 변환이 됨