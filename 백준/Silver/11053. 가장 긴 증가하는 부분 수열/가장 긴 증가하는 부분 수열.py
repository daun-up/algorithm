n = int(input())
a = list(map(int, input().split()))

length = [1] * n

for i in range(n) :
    for j in range(i) :
        if a[j] < a[i] :
            length[i] = max(length[i], length[j] + 1)

print(max(length))
