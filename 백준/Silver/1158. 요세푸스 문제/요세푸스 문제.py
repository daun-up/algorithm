import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split()) # 인원 수, k 번째 사람 제거
people = deque()
result = []

for i in range(1, n+1) :
    people.append(i)

while people :
    for _ in range(k-1) : # 여기가 이해 안 감
        # k-1개 빼놓고 다시 뒤에 붙이고, k번째를 pop()
        people.append(people.popleft())
    
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))

    