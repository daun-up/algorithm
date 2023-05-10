import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    n, m = map(int,input().split())
    queue = deque(map(int, input().split())) # 큐 만들기
    idx = deque(range(0,n))


    cnt = 0

    while queue:
        if (queue[0] == max(queue)):
            cnt += 1
            queue.popleft()

            if (idx.popleft() == m):
                print(cnt)
                break
        else :
            queue.append(queue.popleft())
            idx.append(idx.popleft())



        


