def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    
    return answer if answer else [-1]
    
    # answer = []
    # for i in arr:
    #     if i % divisor == 0: # 나누어 떨어질 때
    #         answer.append(i)
    # if answer:
    #     answer.sort() # 걍 이렇게 해야 하는 거임?
    # else:
    #     answer.append(-1)
    # return answer