import math

t = int(input())

for i in range(t) :
    n, m = map(int,input().split())

    if n == m :
        print ("1")
    elif n == 1:
        print(m)
    else :
        print (math.factorial(m)//(math.factorial(n) * math.factorial(m-n)))

