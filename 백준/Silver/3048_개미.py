import sys
input = sys.stdin.readline
n1, n2 = map(int,input().split())
ant1 = list(map(str,input().rstrip("\n")))
ant2 = list(map(str,input().rstrip("\n")))
t = int(input())

ant1.reverse()
result = ant1 + ant2

for _ in range(t) :
    for i in range(len(result) - 1) :
        if result[i] in ant1 and result[i + 1] in ant2 :
            result[i], result[i + 1] = result[i + 1], result[i]

            # 위치를 바꾼 개미가 선두 개미라면
            if result[i + 1] == ant1[-1] :
                break

print("".join(result))