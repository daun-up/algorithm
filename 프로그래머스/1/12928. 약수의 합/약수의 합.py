def solution(n):
    answer = 0
    tmp = []
    for i in range(1,n+1):
        if n % i == 0:
            tmp.append(i)
    
    return sum(tmp)