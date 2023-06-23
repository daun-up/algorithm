n = int(input())
answer = "int"
for _ in range(n//4):
    answer = "long " + answer
print(answer)
