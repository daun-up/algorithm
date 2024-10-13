def backtracking(lotto, s, start):
    if len(lotto) == 6:
        print(*lotto)
        return

    for i in range(start, len(s)):
        backtracking(lotto + [s[i]], s, i + 1)


while True:
    data = list(map(int, input().split()))
    k = data[0]  
    s = data[1:]  

    if k == 0:
        break

    backtracking([], s, 0)  # 빈 리스트에서 시작하여 백트래킹
    print()