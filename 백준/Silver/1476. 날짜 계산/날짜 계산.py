e, s, m = map(int, input().split())

year = 1
while True :
    if (year - 1) % 15 + 1 == e and (year - 1) % 28 + 1 == s and (year - 1) % 19 + 1 == m :
        print(year)
        break
    year += 1