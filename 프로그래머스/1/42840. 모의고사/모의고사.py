def solution(answers):
    answer = []
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if(answers[i] == case1[i % len(case1)]):
            scores[0] += 1
        if (answers[i] == case2[i % len(case2)]):
            scores[1] += 1
        if (answers[i] == case3[i % len(case3)]):
            scores[2] += 1
    max_score = max(scores)
    
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer