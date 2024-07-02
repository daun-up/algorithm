import sys
input = sys.stdin.readline

S = input().strip()
list = [0]*26
# print(list)
# print(S)
for i in S:
    list[ord(i)-97] += 1
    # print(ord(i)-97)
print(*list)