def solution(n):
    ans = 0
    # Top-down
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        # 내가 지금 4에 있다면 2에서 순간이동해서 왔구나 알 수 있으니까
        else:
            n -= 1
            ans += 1 # 비용이 들음

    return ans

# [점프] 한 번에 K 칸 
# [순간이동] (현재까지 온 거리) * 2 

# 그리디?