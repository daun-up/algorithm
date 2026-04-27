from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        current_word, cnt = q.popleft()
        
        if current_word == target:
            return cnt

        
        for word in words:
            if word not in visited:
                diff = 0
                for a, b in zip(current_word, word):
                    if a != b:
                        diff += 1
                if diff == 1:
                    q.append((word, cnt + 1))
                    visited.add(word)
    
    return 0
                    
    