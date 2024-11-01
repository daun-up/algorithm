import sys
input = sys.stdin.readline

n = int(input().strip())
straws = [int(input().strip()) for _ in range(n)]

straws.sort(reverse=True)
answer = -1

for i in range(n - 2):
    if straws[i] < straws[i + 1] + straws[i + 2]:
        answer = straws[i] + straws[i + 1] + straws[i + 2]
        break
    
print(answer)