money = int(input())
prices = list(map(int,input().split()))


# 준현 : 무조건 살 수 있는 만큼 매일 매수
def junhyeon(money, prices) :
    stock = 0
    for price in prices :
        if money >= price :
            stock += money // price
            money %= price
    return money + stock * prices[-1]

# 성민
def sungmin(money, prices) :
    stock = 0
    for i in range(3, len(prices)) :
        if prices[i - 3] > prices[i - 2] > prices[i - 1] :
            if money >= prices[i] :
                stock += money // prices[i]
                money %= prices[i]
        elif prices[i - 3] < prices[i - 2] < prices[i - 1]:
            money += stock * prices[i]
            stock = 0
    return money + stock * prices[-1]


junhyeon_total = junhyeon(money, prices)
sungmin_total = sungmin(money,prices)

if junhyeon_total > sungmin_total :
    print("BNP")
elif junhyeon_total < sungmin_total :
    print("TIMING")
else : 
    print("SAMESAME")