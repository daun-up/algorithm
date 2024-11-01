n = int(input())
dasom = int(input())
data = [] 

for _ in range(n - 1):
    data.append(int(input()))

count = 0  

while data and max(data) >= dasom:
    max_data = max(data)
    max_index = data.index(max_data) 
    data[max_index] -= 1 
    dasom += 1  
    count += 1  

print(count)