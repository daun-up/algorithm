data = []
for _ in range(9) :
    data.append(int(input()))
sum_data = sum(data)
found = False
    
for i in range(9) :
    for j in range(i + 1, 9) :
        if sum_data - (data[i] + data[j]) == 100 :
            tmp1, tmp2 = data[i], data[j]
            found = True
            break
        if found == True :
            break
            
while len(data) > 7 :
    data.remove(tmp1)
    data.remove(tmp2)
    
data.sort()

for k in data :
    print(k)
        