from itertools import permutations

n = int(input())
questions = [list(map(int,input().split())) for _ in range(n)]

# baseballs = list(permutations())
tmp = [''.join(p) for p in permutations('123456789', 3)]

def check(q, t):
    num, s, b = q # 숫자, 스트라이크, 볼
    num = str(num)
    
    strike = sum(1 for i in range(3) if num[i]==t[i]) # 만약 
    ball = sum(1 for i in range(3) if num[i] in t and num[i] != t[i])
    
    return strike == s and ball == b

cnt = 0

for t in tmp:
    if all(check(q,t) for q in questions):
        cnt += 1

print(cnt)