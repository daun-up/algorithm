def check(board) :
    max_cnt = 1
    
    # 가로에서 가장 긴 연속 개수를 판단
    for i in range(n) :
        row_cnt = 1
        for j in range(1,n) :
            if board[i][j] == board[i][j-1] :
                row_cnt += 1
                max_cnt = max(max_cnt, row_cnt)
            else :
                row_cnt = 1
                
    # 세로
    for j in range(n) :
        col_cnt = 1
        for i in range(1,n) :
            if board[i][j] == board[i-1][j] :
                col_cnt += 1
                max_cnt = max(max_cnt, col_cnt)
            else :
                col_cnt = 1
                
    return max_cnt
            

n = int(input())
result = 0
# 사탕을 어떻게 바꿔보지?

board = [list(input()) for _ in range(n)]


for i in range(n) :
    for j in range(n) :
        # 오른쪽 사탕과 교환
        if j+1 < n :
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            result = max(result, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        # 아래쪽 사탕과 교환
        
        if i+1 < n :
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            result = max(result, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(result)
        
        