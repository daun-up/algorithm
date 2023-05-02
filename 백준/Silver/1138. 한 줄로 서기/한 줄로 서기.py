import sys
input = sys.stdin.readline

n = int(input()) # 몇 명인지
list = list(map(int,input().split()))
result = [0]*n # 크기가 n 이고 모두 0 인 배열

for i in range(n) :
    cnt = 0

    for j in range(n):
        if cnt == list[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt += 1

print(*result)






