def solution(numbers, target):
    answer = 0
    bfs = [0]
    
    for n in numbers:
        tmp = []
        for b in bfs:
            tmp.append(b + n)
            tmp.append(b - n)
        bfs = tmp
        
    for b in bfs:
        if b == target:
            answer += 1
            
    return answer