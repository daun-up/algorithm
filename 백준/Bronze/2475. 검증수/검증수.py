data = map(int,input().split())
sum = 0

for i in data :
    sum += i*i
    
answer = sum%10
    
print(answer)