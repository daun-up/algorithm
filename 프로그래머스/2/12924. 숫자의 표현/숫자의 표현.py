def solution(n):
    answer = 0
    for i in range(1,n+1): # 시작 숫자
        sum = 0
        for j in range(i,n+1): # 연속 합
            sum += j
            
            if sum == n: # 정확히 n 이 되면
                answer += 1
                break # 안쪽 for 문
            elif sum > n: # n 을 초과하면 멈춤
                break # 안쪽 for 문
    return answer