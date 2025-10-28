def solution(diffs, times, limit):
    answer = 0
    
    def calculate_time(level):
        total_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1] if i > 0 else 0
            
            if diff <= level:
                total_time += time_cur
            else:
                total_time += (diff-level)*(time_cur) + (diff-level)*(time_prev) + time_cur
        return total_time
    
    lo, hi = 1, max(diffs)
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if calculate_time(mid) <= limit:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    return answer