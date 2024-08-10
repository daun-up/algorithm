list = []
result = []
find_result = False
sum = 0


for i in range(9) :
    tmp = int(input())
    list.append(tmp)
    sum += tmp
    
for i in range(9) :
    for j in range(i+1, 9) :
        tmp_sum = sum - list[i] - list[j]
        if tmp_sum == 100 :
            result.extend([list[i], list[j]])
            find_result = True
            break
    if find_result : break

list.sort()
for ele in list :
    if ele not in result : print(ele)