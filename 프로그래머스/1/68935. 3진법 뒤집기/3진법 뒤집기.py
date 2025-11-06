def solution(n):
    answer = 0
    tmp = ''
    while n > 0 :
        tmp += str(n % 3)
        n = n // 3
    
    return int(tmp, 3)