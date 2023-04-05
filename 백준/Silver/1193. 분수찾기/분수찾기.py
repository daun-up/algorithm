import sys
input = sys.stdin.readline

x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    top = x
    under = line - x + 1
else :
    top = line - x + 1
    under = x

print(f'{top}/{under}')