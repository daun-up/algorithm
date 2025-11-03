def solution(d, budget):
    answer = 0
    # 최대 지원 가능한 부서 수
    tmp = budget
    d.sort()

    for i in d:
        if  tmp >= i:
            tmp -= i
            answer += 1
        else :
            break
            
    return answer