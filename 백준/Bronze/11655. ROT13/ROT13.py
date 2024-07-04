s = list(input())
# answer = []

for i in range(len(s)):
    # 공백일 때
    if 97 <= ord(s[i]) <= 109 or 65 <= ord(s[i]) <= 77 :
        s[i] = chr(ord(s[i]) + 13)
    elif 78 <= ord(s[i]) <= 90 or 110 <= ord(s[i]) <= 122 :
        s[i] = chr(ord(s[i]) - 13)
    elif 48 <= ord(s[i]) <= 57 or s[i] == ' ':
        s[i] = s[i]
    # else:
        # s[i] += s[i]
# print(answer)
print(''.join(s))

# 1. 공백 없이 결과 출력하기 O n r x w | | {   \ { y v { r   W  q t r

# 특정 아스키 코드 범위 넘어갈 때 예외 처리