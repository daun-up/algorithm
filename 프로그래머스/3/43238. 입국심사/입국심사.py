def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n # 최악의 경우
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid // time
        
        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer