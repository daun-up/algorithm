def solution(want, number, discount):
    answer = 0
    dict = {w:n for w,n in zip(want,number)}
    
    for i in range(len(discount) - 9) : 
        # 길이 10짜리 윈도우(연속 구간)를 discount 안에서 모두 확인하기 위한 범위
        count = {}
        
        for item in discount[i:i+10] :
            count[item] = count.get(item, 0) + 1
        if count == dict: # 모든 키와 값 쌍이 동일하면
            answer += 1
            
            
    return answer # 회원 등록을 할 수 있는 총 날짜