import sys
input = sys.stdin.readline

n = int(input()) #전체 사람의 수
info = []
rank = []

for _ in range(n):
    x,y = map(int,input().split())
    info.append((x,y))

for i in info:
    rank = 1
    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    
    print(rank,end=' ')







    


 