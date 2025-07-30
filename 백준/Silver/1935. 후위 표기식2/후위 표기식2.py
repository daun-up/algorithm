n = int(input())
exp = input()
values = [int(input()) for _ in range(n)]
stack = []

for char in exp :
    if char.isalpha() :
        value = values[ord(char) - ord('A')]
        stack.append(value)
    else :
        b = stack.pop()
        a = stack.pop()
        if char == '+' :
            stack.append(a+b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b)

print(f"{stack[0]:.2f}")
    