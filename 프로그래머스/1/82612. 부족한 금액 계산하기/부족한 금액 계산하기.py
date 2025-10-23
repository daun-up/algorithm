def solution(price, money, count):
    tmp = 0
    for i in range(count+1):
        tmp += price*i
    if tmp < money:
        return 0
    return tmp - money