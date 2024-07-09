n = int(input())
result = ''

# 이진수 나누기가 
if n == 0 :
    print(0)
    exit
    
# 10 진수 -> 2진수
while n!=0 :
    if n % (-2) : # 나머지가 있을 때
        n = n // -2 + 1
        result += '1'
    else : 
        n = n // -2 # 몫
        result += '0'
    
print(''.join(reversed(result)))