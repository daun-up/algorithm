from collections import defaultdict

def solution(participant, completion):
    answer = ''
    d = defaultdict(int)
    
    for name in participant:
        d[name] += 1
    for name in completion:
        d[name] -= 1
    
    for key, value in d.items():
        if value >= 1:
            answer = key
    
    return answer