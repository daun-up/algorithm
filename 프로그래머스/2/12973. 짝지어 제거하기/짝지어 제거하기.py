def solution(s):
    # answer = -1
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
        
        
    if len(stack) == 0:
        return 1
    else:
        return 0
