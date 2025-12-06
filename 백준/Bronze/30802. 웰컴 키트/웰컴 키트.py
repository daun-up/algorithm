n = int(input())
# s,m,l,xl,xxl,xxxl = map(int,input().split())
sizes = map(int,input().split())
t, p = map(int,input().split()) # 티셔츠와 펜의 묶음 수

t_cnt = 0


for size in sizes:
    if size == 0:
        continue
    elif size <= t:
        t_cnt += 1
    elif size % t > 0:
        t_cnt += (size//t) + 1
    else:
        t_cnt += (size//t)

print(t_cnt)
print((n // p), (n % p))