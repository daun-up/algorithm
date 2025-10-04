n = int(input())

arr = []

for _ in range(n) :
    s, e = map(int,input().split())
    arr.append((s,e))
    
# max_day = max(arr[1])
max_day = max(e for _, e in arr)
diff = [0]*(max_day + 2)

# 연속된 날짜 구간별로 최대 동시 이벤트 수를 찾아 구간 길이 × 최대 높이를 더하는 방식이 해법의 핵심

for s,e in arr:
    diff[s] += 1
    diff[e+1] -= 1
    # diff = [0, 1, 0, 0, -1, 0]
 
    
# 누적합 계산
count = [0]*(max_day + 2)
cur = 0
for d in range(1, max_day+1):
    cur += diff[d]
    count[d] = cur

area = 0
width = 0 # 연속 구간의 수
max_height = 0 # 

for d in range(1, max_day+1):
    if count[d] > 0: # 이 날짜에 일정이 있으면
        width += 1 # 구간 길이 1 추가하고
        if count[d] > max_height:
            max_height = count[d]
    else: # 일정이 없으면 (연속 구간이 끊겼으면)
        if width > 0: 
            area += width*max_height
            width = 0
            max_height = 0

if width > 0:
    area += width*max_height
print(area)