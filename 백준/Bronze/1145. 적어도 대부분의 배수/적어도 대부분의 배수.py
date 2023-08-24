list = list(map(int, input().split()))
min = min(list) # 최솟값
while True:
    cnt = 0
    for i in list:
        if min % i == 0: 
            cnt += 1
    if cnt > 2: 
        break
    min += 1   
print(min)