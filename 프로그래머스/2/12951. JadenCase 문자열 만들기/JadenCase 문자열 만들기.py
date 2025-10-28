def solution(s):
    answer = ''
    s = list(s)
    
    for i in range(len(s)):
        if s[i-1] == ' ' or i == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
            
    answer = ''.join(s)
    
    return answer