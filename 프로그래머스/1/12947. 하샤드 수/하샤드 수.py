def solution(x):
    answer = True
    ls = [int(i) for i in str(x)]
    s = sum(ls)
    
    if (x % s) == 0:
        answer = True
    else:
        answer = False
    return answer