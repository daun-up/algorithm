def solution(a, b):
    print(zip(a,b))
    
    # zip(): 동일한 인덱스끼리 묶어 튜플로 만들어 반환
    return sum([x*y for x,y in zip(a,b)])

    # answer = [0]*len(a)
    # answer = []
    # for i in range(len(a)):
    #     answer.append(a[i] * b[i])
    #     # 만약 
    # return sum(answer)