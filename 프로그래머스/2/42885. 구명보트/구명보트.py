def solution(people, limit):
    answer = 0
    # 한 번에 두 명
    people.sort()
    l, r = 0, len(people) - 1
    
    # while l < r: <- 두 명 이상이 남았을 때만 처리 (마지막 1명은 처리 안 됨)
    while l <= r: # <- 한 명 남았을 때까지 처리 (마지막 1명도 보트 태움!)
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        answer += 1
    
    return answer