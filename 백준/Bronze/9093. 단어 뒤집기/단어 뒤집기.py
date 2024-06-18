import sys

N = int(sys.stdin.readline())

for _ in range(N):
    word = list(sys.stdin.readline().split())
    
    for j in word :
        print(j[::-1], end=' ')