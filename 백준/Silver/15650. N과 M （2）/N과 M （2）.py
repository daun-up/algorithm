n, m = map(int,input().split())

numList = [i for i in range(0, n+1)]

index = 0 
visited = [False]*(len(numList)+1) # 이미 쓴 숫자인지 판별하기 위해

def backtracking(result) :
    # 개수에 맞게 꽉 찼다면 결과 출력
    if len(result) == m :
        print(*result)
        return
    
    for i in range(1, n+1) :
        # 쓴 것이 아니고 담아놓은 결과가 비어있는 경우 담기
        # 쓴 것이 아니고 담아놓은 결과가 담을 것보다 작으면 담기 (오름차순)
        if (visited[i]== False) and (len(result) == 0 or i > result[-1]) :
            visited[i] = True
            result.append(numList[i])
            # 재귀로 백트래킹 실행
            backtracking(result)
            # 재귀 끝난 후 빠져나와서 바로 직전에 담았던 것 제거
            visited[i] = False
            result.pop()

backtracking([])