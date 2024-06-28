from collections import deque

# 입력
s = input().strip()

# 결과를 저장할 문자열
result = ''
# 단어를 저장할 스택
stack = deque()
# 괄호 안인지 아닌지 구분하는 플래그
flag = False

for i in s:
    if i == '<':
        # 스택에 남아있는 단어를 결과에 추가
        while stack:
            result += stack.pop()
        # 태그 시작
        flag = True
        result += i
    elif i == '>':
        # 태그 끝
        flag = False
        result += i
    elif flag:
        # 태그 내부 문자
        result += i
    else:
        if i == ' ':
            # 단어 끝
            while stack:
                result += stack.pop()
            result += i
        else:
            # 단어의 문자
            stack.append(i)

while stack:
    result += stack.pop()

print(result)
