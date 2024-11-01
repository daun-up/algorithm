n = int(input())
k = int(input())
if k >= n:
    print(0)
else:
    sensors = list(map(int, input().split()))
    sensors.sort()

    distances = [sensors[i+1] - sensors[i] for i in range(n - 1)]
    distances.sort(reverse=True)

    # 가장 큰 (k-1)개의 거리를 제외한 합이 최소 거리
    print(sum(distances[k-1:]))