import sys
from collections import deque

stack = []
result = []

n = int(sys.stdin.readline().strip())
num = 1

for i in range(n) :
    value = int(sys.stdin.readline().strip())
    while (num <= value) :
        stack.append(num)
        result.append("+")
        num += 1
        
    if stack[-1] == value :
        stack.pop()
        result.append("-")
    else:
        result.clear()
        result.append('NO')
        break	

for k in result :
    print(k)