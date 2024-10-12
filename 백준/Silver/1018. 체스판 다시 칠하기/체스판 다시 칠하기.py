n, m = map(int,input().split())
board = []
result = []

for _ in range(n) :
    board.append(input())

for i in range(n-7) : # 칠할 체스는 8X8 크기로 정해져 있음
    for j in range(m-7) : # i, j 는 체스판의 칠할 부분을 찾는 시작점
        draw1 = 0 # 시작점이 하얀색일 경우
        draw2 = 0 # 시작점이 검은색일 경우
        
        for a in range(i, i+8) : # 시작점 i,j 부터 8 을 더한 범위
            for b in range(j, j+8) :
                if (a + b) % 2 == 0 : # board[a][b] 지점을 2 로 나눈 나머지가 0 일 때 draw1 (검은색이 아님)
                    if board[a][b] != 'B' :
                        draw1 += 1
                    if board[a][b] != 'W' :
                        draw2 += 1
                else :
                    if board[a][b] != 'W' :
                        draw1 += 1
                    if board[a][b] != 'B' :
                        draw2 += 1
        result.append(min(draw1, draw2))
print(min(result))  