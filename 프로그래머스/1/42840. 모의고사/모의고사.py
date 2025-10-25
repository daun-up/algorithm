def solution(answers):
    answer = []
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            scores[0] += 1
        if answers[i] == second[i % 8]:
            scores[1] += 1
        if answers[i] == third[i % 10]:
            scores[2] += 1
    
    for idx, num in enumerate(scores): # (인덱스, 점수) 형태
        if num == max(scores):
            answer.append(idx+1)
            
    return answer