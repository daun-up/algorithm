n = int(input())
A = list(map(int,input().split()))

result = [-1] * n
stack = []

for i in range(n) :
    # while stack and A[i-1] < A[i] :
    while stack and A[stack[-1]] < A[i] :
        result[stack.pop()] = A[i] 
    stack.append(i)

print(*result)
