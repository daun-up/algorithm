n = int(input())
stack = []
answer = []

for _ in range(n) :
    command = input().split()
    if len(command) == 2 :
        if command[0] == "push" :
            stack.append(command[1])
    else :
        if command[0] == "pop" :
            if stack :
                answer.append(stack.pop())
            else :
                answer.append(-1)
        elif command[0] == "size" :
            answer.append(len(stack))
        elif command[0] == "empty" :
            if stack :
                answer.append(0)
            else :
                answer.append(1)
        elif command[0] == "top" :
            if stack :
                answer.append(stack[-1])
            else :
                answer.append(-1)
        
# print(''.join(answer))
for i in answer :
    print(i)
    