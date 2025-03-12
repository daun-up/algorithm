def solution(my_string, alp):
    answer = ''
    for i in range(len(my_string)) :
        if my_string[i] == alp :
            my_string = my_string.replace(my_string[i], alp.upper())
        answer = my_string
    return answer