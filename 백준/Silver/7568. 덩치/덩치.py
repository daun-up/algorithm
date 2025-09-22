n = int(input())

peoples = []

for _ in range(n) :
    x, y = map(int,input().split())
    peoples.append((x,y))
    
for i in peoples :
    rank = 1
    for j in peoples :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end=" ")