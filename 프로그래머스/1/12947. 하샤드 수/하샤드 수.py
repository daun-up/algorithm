def solution(x):
    answer = True
    tmp = sum(map(int,str(x)))
    
    if (x % tmp) == 0 :
        answer = True
    else :
        answer = False
    return answer