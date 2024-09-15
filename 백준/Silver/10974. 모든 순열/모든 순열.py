import sys
input = sys.stdin.readline

n = int(input())
result = []

def backtracking():
    if len(result) == n:	#종료조건
        print(*result)
        return

    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            backtracking()
            result.pop()

backtracking()