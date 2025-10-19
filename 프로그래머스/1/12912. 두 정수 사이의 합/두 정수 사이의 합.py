def solution(a, b):
    if a > b:
        a,b = b,a
    return sum(range(a, b + 1)) # 와 이런 거도 된다고...?
    # return sum([i for i in range(a,b+1)])

    # answer = 0
    # if a < b:
    #     for i in range(a,b+1):
    #         answer += i
    # else:
    #     for i in range(b,a+1):
    #         answer += i
    # return answer