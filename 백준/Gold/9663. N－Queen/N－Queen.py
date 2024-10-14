import sys
input = sys.stdin.readline
n = int(input())

visited = [0] * n # 각 인덱스는 행(row) 그 값은 열(col) 의미
cnt = 0 # 퀸을 배치할 수 있는 경우의 수


def check(now_row) :
    for row in range(now_row) : # now_row 에서 퀸을 배치하려고 할 때 그 이전에 배치된 퀸들과 충돌하지 않는지 확인하는 함수
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]) :
            # 가로 (같은 열) 충돌 확인, 두 퀸의 열 차이와 행 차이가 같다면 대각선에 위치해 있음을 확인
            return False # 충돌이 있으면
    return True # 충돌이 없으면

def backtracking(row) : # row : 현재 퀸을 배치하려는 행
    global cnt
    
    if row == n : # 퀸을 모두 배치한 경우
        cnt += 1
    
    else : # 현재 행 row 에서 가능한 모든 열에 퀸을 배치해보는 시도
        for col in range(n) :
            visited[row] = col
            if check(row) : # 배치가 유효한지 확인
                backtracking(row + 1) # 유효하면 다음 행에 대해 (row +1) 호출하고 재귀적으로 퀸 배치
                
backtracking(0) # 첫 번째 행부터 퀸을 배치하기 시작
print(cnt)