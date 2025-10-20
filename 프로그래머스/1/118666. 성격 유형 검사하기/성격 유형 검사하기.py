def solution(survey, choices):
    answer = ''
    # survey[i][0] 비동의 선택 시 받는 성격 유형
    # survey[i][1] 동의 선택 시 받는 성격 유형
    
    score = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    
    for i in range(len(survey)):
        left, right = survey[i]
        if choices[i] > 4:
            score[left] += 4 - choices[i]
        elif choices[i] < 4:
            score[right] += choices[i] - 4
    
    for a,b in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]: # 이거 잘 알아두기...
        # 각 지표에서 더 점수가 높은 성격 유형!
        if score[a] >= score[b]:
        # 문제에서 처음 부터 사전순으로 정렬해서 줌
            answer += a
        else:
            answer += b
            
    return answer