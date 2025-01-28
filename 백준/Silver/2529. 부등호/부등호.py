k = int(input())

data = list(input().split())

# 문자열의 index 와 부등호의 index 가 존재
visited = [0] * 10
answer = []

def check (a, b, op) :
    if op == "<" :
        if a > b : return False
    if op == ">" :
        if a < b : return False
    return True

def dfs (idx, num) :
    
    if idx == k + 1 :
        answer.append(num)
        return
    
    for i in range(10) :
        if not visited[i] :
            if idx == 0 or check(num[idx-1], str(i), data[idx-1]) :
                visited[i] = True
                dfs(idx + 1, num + str(i))
                visited[i] = False
    
    # 브루트포스
    # 0~9 까지의 숫자를 부등호 사이사이에 넣을 수 있으므로 숫자를 하나씩 넣어본다
    # 이때, 선택된 숫자는 모두 달라야 하므로 visited 배열을 만들어 이미 사용된 숫자인지를 체크한다. 
    # 만약 사용되지 않은 숫자라면 부등호를 만족하는지 확인한다.
    # 이때 index 가 0 이라면 비교할 필요가 없으므로 그냥 문자열에 넣는다.
 
 
dfs(0, '')
answer.sort()

print(answer[-1])
print(answer[0])
