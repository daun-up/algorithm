n = int(input())
m = int(input())
nums = sorted(map(int, input().split()))

cnt = 0
l, r = 0, n - 1

while l < r:
    s = nums[l] + nums[r]
    if s == m:
        cnt += 1
        l += 1
        r -= 1
    elif s < m:
        l += 1
    else:
        r -= 1

print(cnt)