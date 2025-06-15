# dictionary
def solution(s):
    answer = []
    dict = {}
    for i in range(len(s)) :
        char = s[i]
        if char in dict :
            answer.append(i - dict[char])
        else :
            answer.append(-1)
        dict[char] = i
    return answer