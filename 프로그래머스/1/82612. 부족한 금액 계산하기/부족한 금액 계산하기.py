def solution(price, money, count):
    pay = 0
    for i in range(count+1):
        pay += price*i
        
    if pay < money:
        return 0
    else:
        return pay - money