def solution(elements):
    n = len(elements)
    answer = set()
    arr = elements * 2 # 원형이므로 길이 두 배
    
    for length in range(n):
        for start in range(n):
            answer.add(sum(arr[start:start+length]))
        
    return len(answer)