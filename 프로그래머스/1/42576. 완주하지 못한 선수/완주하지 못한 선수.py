from collections import defaultdict
def solution(participant, completion):
    answer = ''
    people = defaultdict(int)
    
    for name in participant:
        people[name] += 1
    
    for name in completion:
        people[name] -= 1
    
    # print(people)
    # print(list(people.items()))
    # print(dict(people))
    
    for k, v in people.items():
        if v >= 1:
            answer = k
    
    return answer