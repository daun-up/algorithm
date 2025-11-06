def solution(s):
    answer = []
    dic = {} # 각 문자별 마지막 등장 위치
    
    for i, ch in enumerate(s):
        if ch in dic:
            answer.append(i - dic[ch]) # 현재 인덱스 빼기 마지막 등장 인덱스
        else:
            answer.append(-1)
        dic[ch] = i # 마지막 위치 갱신
            
            
    return answer