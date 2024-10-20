n = int(input())

arr = list(map(int,input().split()))
possible_sums = set()

def dfs(idx, current_sum) :
    if idx == n :
        possible_sums.add(current_sum)
        return
    # 현재 수를 포함하는 경우
    dfs(idx + 1, current_sum)
    # 현재 수를 포함하지 않는 경우
    dfs(idx + 1, current_sum + arr[idx])
    
dfs(0, 0)

result = 0
while result in possible_sums :
    result += 1
print(result)