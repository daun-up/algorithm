n = int(input())

list = [list(map(int, input().split())) for _ in range(n)]

def recur(i) :
    if i >= n :
        return 0
    money = 0
    if i + list[i][0] <= n :
        money = recur(i + list[i][0]) + list[i][1]
    money = max(money, recur(i+1))
    return money
print(recur(0))
    