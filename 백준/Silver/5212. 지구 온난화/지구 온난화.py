r, c = map(int,input().split())

# map = [list(input().split()) for _ in range(r)]
board = [input().strip() for _ in range(r)]
new_board = [['.'] * c for _ in range(r)]  # 기본은 바다로 두고, 살아남는 X만 찍기

# 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다

dx = [0,0,-1,1]
dy = [-1,1,0,0]


for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            sea = 0
             
            for k in range(4):
                nx,ny = i + dx[k], j + dy[k]
                if not(0 <= nx < r  and 0 <= ny < c): # 경계 밖은 = 바다
                    sea += 1
                elif board[nx][ny] == '.':
                    sea += 1
            if sea < 3: # 살아남는 조건
                new_board[i][j] = 'X'

# 최소 직사각형 출력

min_r, max_r = r, -1
min_c, max_c = c, -1

for i in range(r):
    for j in range(c):
        if new_board[i][j] == 'X':
            min_r = min(min_r, i)
            max_r = max(max_r, i)
            min_c = min(min_c, j)
            max_c = max(max_c, j)

if max_r == -1:
    print('.')
else:
    for i in range(min_r,max_r+1):
        print(''.join(new_board[i][min_c:max_c + 1]))
