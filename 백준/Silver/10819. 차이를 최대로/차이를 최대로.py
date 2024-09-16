n = int(input())
list = list(map(int,input().split()))
arr = [0] * n # 정답을 저장
visited = [0] * n # 각 숫자가 순열에 포함되었는지 여부
answer = -99999 # 가능한 최댓값을 저장하는 변수 나중에 max 로 갱신되도록 가장 작은 수로 설정

def recur(cur) :
    global answer
    
    # arr 가 완성되었을 때
    if cur == n :
        total = 0
        # 문제에서 주어진 식 실행
        for i in range(1,n) :
            total += abs(arr[i] - arr[i-1])
            
        # 최댓값으로 정답 갱신
        answer = max(answer, total)
        return
    
    for i in range(n) :
        if visited[i] :
            continue
        
        arr[cur] = list[i]
        visited[i] = 1
        recur(cur + 1)
        visited[i] = 0
                
recur(0)
print(answer)
        