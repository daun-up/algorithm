def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    
    # s가 "1"이 될 때까지 계속해서
    while s != '1':
        zero_cnt += s.count('0') # 0 의 개수 세기
        # 문자열에서 요소의 개수 세는 함수
        
        s = s.replace('0','') # replace
        
        s = bin(len(s))[2:] # 이진수 만들기
        # 0b 는 2 진수임을 의미하는 접두어이기 때문에 [2:] 로 잘라서 씀
        
        cnt += 1
    
    answer.append(cnt)
    answer.append(zero_cnt)
    
    return answer