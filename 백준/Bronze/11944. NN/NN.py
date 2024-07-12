n, m = map(int,input().split())

if len(str(n) * n) > m :
    print((str(n)*n)[:m])
else :
    print(str(n)*n)