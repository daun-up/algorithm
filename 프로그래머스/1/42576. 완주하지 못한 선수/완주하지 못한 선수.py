def solution(participant, completion):
    tmp = 0
    dic = {}
    
    for p in participant:
        dic[hash(p)] = p # 이름 값을 hash 로 저장
        tmp += hash(p) # 참가자들의 hash 값을 더함
        
    for c in completion:
        tmp -= hash(c)
    
    return dic[tmp] # 남은 해시 값 = 완주하지 못한 사람의 해시

#     answer = ''
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]