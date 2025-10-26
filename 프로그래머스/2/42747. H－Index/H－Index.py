def solution(citations):
    answer = 0
    # h 번 이상 인용된 논문이 h 편 이상이고 나머지 논문이 h 번 이하
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        if i + 1 <= c:
            answer = i + 1
    
    return answer