def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    # s가 "1"이 될 때까지 계속해서
    while s != '1':
        zero_cnt += s.count('0') # 0 의 개수 세기
        
        s = s.replace('0','') # replace
        
        s = bin(len(s))[2:] # 이진수 만들기
        
        cnt += 1
    
    answer.append(cnt)
    answer.append(zero_cnt)
    
    return answer