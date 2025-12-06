t = int(input())

for _ in range(t):
    p = ''
    r, s = input().split()
    for c in s:
        p += c*int(r)
    print(p)