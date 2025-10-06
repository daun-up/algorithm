from collections import deque
n = int(input())

move = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)] # 가로, 세로, 대각선

# 비트마스크로 변환
masks = []
for mv in move:
    mask = 0
    for idx in mv:
        mask |= (1 << idx)
    masks.append(mask)

# 입력
boards = []
for _ in range(n):
    board = []
    
    for _ in range(3):
        row = input().split()
        board.append(''.join(['1' if c=='H' else '0' for c in row]))
    boards.append(board)


# bfs 및 XOR

def bfs(coins):
    start = int(coins, 2)
    
    if start == 0 or start == 511:
        return 0
    # 만약 이미 모든 동전이 같은 면이라면 (전부 0 또는 전부 1) 바로 0 반환

    visited = [0]*512
    q = deque([(start, 0)])
    visited[start] = 1
    
    
    while q:
        cur, d = q.popleft()
        
        for mask in masks:
            nxt = cur ^ mask
            
            if not visited[nxt]:
                if nxt == 0 or nxt == 511:
                    return d + 1
                visited[nxt] = 1
                q.append((nxt, d+1))
    return -1

for board in boards:
    coins9 = ''.join(board)
    print(bfs(coins9)) # 9자리 문자열(1차원)으로 만들어서 bfs 돌림

