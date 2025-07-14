n,x = map(int,input().split())

arr = list(map(int,input().split()))

curr_sum = sum(arr[:x]) # 처음 x 개 합
max_sum = curr_sum
count = 1

for i in range(x, n) : # 두 번째 윈도우부터 하나씩 오른쪽으로 슬라이드
    curr_sum += arr[i] - arr[i - x]
    
    if curr_sum > max_sum:
        max_sum = curr_sum
        count = 1
    elif curr_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)