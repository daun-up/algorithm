def solution(n):
    answer = 0
    # tmp = [i for i in str(n)]
    # tmp.sort(reverse=True)
    # answer = int(''.join(tmp))
    # return answer
    ls = list(str(n))
    ls.sort(reverse=True)
    return int(''.join(ls))
    