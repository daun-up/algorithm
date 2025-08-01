exp = input()
stack = []
result = ""

for char in exp:
    if char.isalpha() :
        result += char

    elif char == "(" : # 여는 괄호는 그냥 스택에 저장
        stack.append(char)
    elif char == ")" :
        while stack and stack[-1] != "(" :
            result += stack.pop() # 스택에서 ( 가 나올 때까지 모든 연산자를 꺼내 출력
        stack.pop()
        
    else : # 연산자일 경우
        while stack and stack[-1] != "(" :
            top = stack[-1]
            
            if (char in '+-' and top in '+-*/') or (char in '*/' and top in '*/') :
                result += stack.pop()
            else :
                break
            
        stack.append(char)
        
        
# 남은 연산자 출력
while stack :
    result += stack.pop()


print(result)