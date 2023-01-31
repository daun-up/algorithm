import sys
n = int(sys.stdin.readline())
list = []
for _ in range(n) :
    a,b,c = map(int,input().split())
    if a == b == c :
        list.append(10000 + (a*1000))
    elif a == b and a != c:
        list.append(1000 + (a*100))
    elif a != b and a == c:
        list.append(1000 + (a*100))
    elif a != b and b == c:
        list.append(1000 + (b*100))
    else :
        list.append(max(a,b,c)*100)
print(max(list))
    