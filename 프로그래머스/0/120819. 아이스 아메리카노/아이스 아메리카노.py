def solution(money):
    answer = []
    if money == 5500 :
        answer.append(1)
        answer.append(0)
    elif money > 5500 :
        answer.append(money//5500)
        answer.append(money%5500)
    elif money < 5500 :
        answer.append(0)
        answer.append(money)
    return answer