def solution(s):
    answer = True
    s = [i for i in s]
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            else:
                stack.pop()
                
        # elif s[i] == ")":
        #     if stack:
        #         stack.pop(-1)
        #     else:
        #         answer = False
        #         break
            
    if stack:
        return False
    

    
    return True