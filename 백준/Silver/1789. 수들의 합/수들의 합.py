s = int(input())

total = 0
count = 0

n = 1

while total + n <= s :
    total += n
    count += 1
    n += 1
    
print(count)