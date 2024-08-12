import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def backtracking():
    if len(res) == m:	#종료조건
        print(' '.join(map(str, res)))

    for i in range(1, n+1):
        if i not in res:
            res.append(i)
            backtracking()
            res.pop()

backtracking()