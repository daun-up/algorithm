from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque([(i,p) for i,p in enumerate(priorities)])
    
    while queue:
        item = queue.popleft()
        
        if any(item[1] < q[1] for q in queue):
            queue.append(item)
        else:
            answer += 1
            if item[0] == location:
                break
        
    
    return answer