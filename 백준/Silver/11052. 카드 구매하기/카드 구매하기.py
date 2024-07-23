n = int(input())
li = list(map(int,input().split()))

card = li[:]
for i in range(n):
    for j in range(i):
        card[i] = max(card[i], card[i-j-1] + li[j])
print(card[n-1])