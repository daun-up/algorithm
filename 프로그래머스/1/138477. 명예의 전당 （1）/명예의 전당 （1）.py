def solution(k, score):
    answer = []
    tmp = []
    
    for i in range(len(score)):
        tmp.append(score[i])
        tmp.sort(reverse=True)
        tmp = tmp[:k]
        answer.append(tmp[-1])
        
    return answer