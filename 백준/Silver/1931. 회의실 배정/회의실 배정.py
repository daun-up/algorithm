n = int(input())
meetings = []

for _ in range(n) :
    start, end = map(int,input().split())
    meetings.append((start,end))
    

# 회의를 끝나는 시간 기준으로 오름차순 정렬
# 끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0 # 가능한 최대 회의 개수
last_end_time = 0 # 마지막으로 선택한 회의의 끝나는 시간

for start, end in meetings :
    if start >= last_end_time : # 현재 회의의 시작 시간이 이전 회의의 끝나는 시간보다 늦거나 같으면 선택
        count += 1
        last_end_time = end
        
print(count)