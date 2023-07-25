import sys
input = sys.stdin.readline
n, game = input().split()
people = []
n = int(n)

for _ in range(n) :
    name = input()
    people.append(name)

result = set(people)

if game == "Y" :
    print(len(result))
elif game == "F" :
    print(len(result) // 2)
elif game == "O" :
    print(len(result) // 3)