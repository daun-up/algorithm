n,k = map(int,input().split())
coins = []

for i in range(n) :
    coins.append(int(input()))

count = 0
coins.sort(reverse=True)
for coin in coins :
    count += k // coin
    k %= coin

print(count)