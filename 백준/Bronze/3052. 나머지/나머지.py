tmp = []

for _ in range(10):
    a = int(input())
    b = a % 42
    
    tmp.append(b)

print(len(set(tmp)))