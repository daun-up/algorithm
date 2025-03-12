def solution(my_string):
    answer = ''
    for i in my_string :
        if i.islower() :
            i = i.upper()
            answer += i
        elif i.isupper() :
            i = i.lower()
            answer += i
    return answer