import heapq
import sys
# input = sys.stdin.readline() <- 문자열이 되어버림
input = sys.stdin.readline # 함수 참조만


n = int(input())

heap = []

for _ in range(n) :
    x = int(input())
    
    if x > 0 :
        heapq.heappush(heap, -x)
    elif x == 0 :
        if heap :
            print(-heapq.heappop(heap))
        else : print(0)