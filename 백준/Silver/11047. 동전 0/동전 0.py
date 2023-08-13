n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

result = 0

for coin in coins :
    if k // coin > 0 :
        result += k // coin
    k %= coin

print(result)


