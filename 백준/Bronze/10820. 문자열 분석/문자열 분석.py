# import sys
# input = sys.stdin.readline


while True:
    try:
        words = list(input())
        # result = [0]*4
        upper, lower, number, space = 0,0,0,0
        for i in range(len(words)):
            # 공백일 때
            if words[i] == ' ':
                space += 1
            # 숫자일 때
            elif 48 <= ord(words[i]) <= 57 :
                number += 1
            # 소문자일 때
            elif 97 <= ord(words[i]) <= 122 :
                lower += 1
            # 대문자일 때
            elif 65 <= ord(words[i]) <= 90 :
                upper += 1
        print(lower, upper, number, space) 
    except EOFError:
        break
    

         
