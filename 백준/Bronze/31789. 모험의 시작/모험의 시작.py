n = int(input())
x, s = map(int,input().split())
flag = False
for i in range (n) :
    c,p = map(int,input().split())
    
    if c <= x and p > s :
        flag = True
        break

if flag :
    print('YES')
else :
    print("NO")