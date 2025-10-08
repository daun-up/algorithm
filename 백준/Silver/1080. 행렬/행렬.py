n, m = map(int,input().split())


# a = [list(map(int,input().split())) for _ in range(n)]
# b = [list(map(int,input().split())) for _ in range(n)]

# 공백 없이 붙은 0/1 문자열 → 각 문자(int)로 변환
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

def flip(a, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] ^= 1 # 0 -> 1, 1 -> 0

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnt += 1
            flip(a,i,j)
            
print(cnt if a == b else -1)

