import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

list = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        list[stack.pop()] = A[i]
    stack.append(i)


print(*list)