n, s = map(int,input().split())
data = list(map(int,input().split()))

count = 0

# depth : 현재 몇 번째 원소까지 탐색했는지를 나타내는 인덱스
# total : 지금까지 선택한 원소들의 합
def dfs (depth, total) : 
    global count
    if depth == n :
        if total == s :
            count += 1
        return # 깊이가 n 이면 이미 다 돌아본 것이기 때문에 종료
    
    # 현재 원소를 포함하는 경우
    dfs(depth + 1, total + data[depth])
    
    # 현재 원소를 포함하지 않는 경우
    dfs(depth + 1, total)



dfs(0,0)

# 공집합도 total == 0으로 포함되므로, s == 0일 때는 1개 빼줌
if s == 0:
    count -= 1

print(count)