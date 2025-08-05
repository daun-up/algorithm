import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for i in range(n) :
    x = int(input())
    if x != 0 :
        heapq.heappush(heap,(abs(x),x)) # 절댓값만 저장하면 원래 어떤 수였는지 알 수 없기 때문에 tuple 로 저장
    else :
        if heap :
            print(heapq.heappop(heap)[1])  # 실제값 출력
        else :
            print(0)

