n = int(input())

array = list(map(int,input().split()))

for i in range(n-1, 0, -1) : # 역순을 탐색하는 반복문
    if array[i] > array[i-1] :
        for j in range(n-1, 0, -1) : # 교환할 값을 찾는 반복문
            if array[i-1] < array[j] :
                array[i-1], array[j] = array[j], array[i-1]
                array = array[:i] + sorted(array[i:])
                print(*array)
                exit()
print(-1)