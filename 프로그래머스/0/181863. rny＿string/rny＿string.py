def solution(rny_string):
    answer = ''
    for i in range(len(rny_string)) :
        if rny_string[i] == 'm' :
            rny_string = rny_string.replace(rny_string[i],'rn')
            
    answer = rny_string
    return answer