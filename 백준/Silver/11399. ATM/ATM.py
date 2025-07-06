n = int(input())
people = list(map(int,input().split()))

people.sort()

result = 0
tmp = 0

for time in people :
    tmp += time
    result += tmp

print(result)