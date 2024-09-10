# 중복을 허용하면서 모든 가능한 조합을 출력하려면, 방문 여부를 확인할 필요 없이 그냥 모든 숫자를 사용할 수 있도록 설정해야 함. 따라서 방문 여부를 체크하는 visited 리스트를 없애고, 단순히 모든 경우의 수를 탐색하도록 수정

n, m = map(int, input().split())

numList = [i for i in range(1, n+1)]

def backtracking(result):
    # 개수에 맞게 꽉 찼다면 결과 출력
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        result.append(numList[i-1])
        # 재귀로 백트래킹 실행
        backtracking(result)
        # 재귀 끝난 후 빠져나와서 바로 직전에 담았던 것 제거
        result.pop()

backtracking([])