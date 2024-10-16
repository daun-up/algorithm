def num(m, n, x, y):
    while x <= m * n: # 최대 범위
        if (x-y) % n == 0: # 나머지로 확인 x에서 y를 뺐을 때 그 값이 N으로 나누어떨어져야 y 주기를 만족하는 해
            return x
        x += m 
    return -1


t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    # <M:N> 이 마지막 해
    # <x:y> 는 몇 번째 해일까?
    # N 만큼 한 번 돌면 하나
    print(num(m, n, x, y))
    
    
# y는 N년을 주기로 반복됩니다. x - y가 N으로 나누어떨어질 때, y는 다시 1로 초기화되며 다음 주기를 시작하게 됩니다. 따라서, x에서 y를 뺀 값이 N의 배수여야 두 주기가 맞아떨어져서 동일한 해를 나타냅니다.