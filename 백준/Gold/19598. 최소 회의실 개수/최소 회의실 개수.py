import heapq

n = int(input())
meetings = []
for _ in range(n) :
    start, end = map(int,input().split())
    meetings.append((start,end))

meetings.sort(key=lambda start: start[0]) # start 기준으로 정렬

heap = []
for start,end in meetings :
    if heap and heap[0] <= start :
        heapq.heappop(heap)
    heapq.heappush(heap,end)

print(len(heap))