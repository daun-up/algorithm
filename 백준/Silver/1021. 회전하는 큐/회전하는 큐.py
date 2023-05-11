import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().rstrip().split()) # 큐의 크기 n, 뽑아내려고 하는 수 개수 m
idx = deque(map(int, input().rstrip().split())) # 위치 저장
q = deque(range(1,n+1)) # 큐 만들기

cnt = 0 # 2,3 번 연산 수행하면 ++

for i in idx: # 뽑아내려는 위치 반복문 돌리기
    while True: # 뽑을 때까지
        if q[0] == i: # 1 번 연산 -> 첫 번째 원소를 뽑아낸다 무조건 첫 번째
            q.popleft() # 왼쪽으로 ㄱ
            break
        else:
            if q.index(i) < len(q)/2 : # 큐의 길이를 2 로 나눈 것보다 원소 위치가 작으면
                 while q[0] != i:
                        q.append(q.popleft()) # 왼쪽에서 지운 값을 추가
                        cnt += 1
                         
            else :
                 while q[0] != i:
                        q.appendleft(q.pop()) 
                        cnt += 1
                        
print(cnt)








        


