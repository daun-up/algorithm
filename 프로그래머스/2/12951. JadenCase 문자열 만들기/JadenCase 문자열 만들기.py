def solution(s):
    answer = ''
    # s = list(s) # str 타입은 불변 객체라서 문자열의 한 글자를 직접 바꾸는 건 불가능
    
    for i in range(len(s)):
        if s[i-1] == ' ' or i == 0:
            # s[i] = s[i].upper()
            answer += s[i].upper()
        else:
            # s[i] = s[i].lower()
            answer += s[i].lower()
    
    
            
    # answer = ''.join(s)
    
    return answer