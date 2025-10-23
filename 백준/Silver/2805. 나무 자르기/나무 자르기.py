import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# 적어도 m 미터의 나무를 가져가야 함

trees = list(map(int,input().split()))

# 가장 짧은 길이 1 을 lo 로
# 나무 중 가장 긴 길이를 hi 로 둔다

lo, hi = 1, max(trees)

while lo <= hi:
    mid = (lo + hi) // 2 # 현재 시도 중인 절단기 높이
    
    tmp = 0 # 벌목된 나무 총합
    
    for tree in trees:
        if tree >= mid:
            tmp += tree - mid
        
    if tmp >= m:
        lo = mid + 1 # 더 높이 잘라도 조건 만족 -> 높이 올려보기
    else:
        hi = mid - 1 # 조건 미달, 더 낮게 자르기

print(hi)