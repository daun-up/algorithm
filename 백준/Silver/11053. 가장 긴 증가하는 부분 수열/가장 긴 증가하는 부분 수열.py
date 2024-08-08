n = int(input())

list = list(map(int,input().split()))
# result = []
result = [1] * n


# result.append(list[0])

# for i in range(1,n) :
#     if list[i-1] < list[i] :
#         result.append(list[i])
#     elif list[i] in result :
#         continue

for i in range(1,n) :
    for j in range(i) :
        if list[i] > list[j] :
            result[i] = max(result[i], result[j]+1)
print(max(result))
