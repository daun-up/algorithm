n, s = map(int,input().split())
data = list(map(int,input().split()))

count = 0

def dfs (index, total) :
    global count
    if index == n :
        if total == s :
            count += 1
        return
    
    # 현재 원소를 포함할 때
    dfs (index + 1, total + data[index])
    
    # 현재 원소를 포함하지 않을 때
    dfs (index + 1, total)

if s == 0 :
    count -= 1
    
dfs(0,0)
print(count)