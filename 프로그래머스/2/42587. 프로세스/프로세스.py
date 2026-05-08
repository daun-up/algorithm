from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for process, priority in enumerate(priorities):
        q.append((process, priority))
    
    
    while q:
        cur, p = q.popleft()
        
        flag = False
        
        for item in q:
            process, priority = item
            
            if p < priority:
                flag = True
                q.append((cur, p))
                break
            
        if flag == False:
            answer += 1
            if cur == location:
                return answer

    return answer