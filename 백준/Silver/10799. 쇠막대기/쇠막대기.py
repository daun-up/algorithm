exp = input()

stack = []
cnt = 0

for i in range(len(exp)) :
    if exp[i] == "(" :
        stack.append("(")
    else : # exp[i] 가 ) 일 떄
        stack.pop()
        if exp[i-1] == "(" : # 레이저인 경우
            cnt += len(stack)
        else :
            cnt += 1
print(cnt)