t = int(input())

for _ in range(t) :
    data = list(input().split())
    for i in data :
        print(i[::-1], end=' ')