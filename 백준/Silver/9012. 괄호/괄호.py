t = int(input())

for _ in range(t) :
    stack = []
    data = input()
    for i in data :
        if i == '(' :
            stack.append(i)
        elif i == ')' :
            if stack :
                stack.pop()
            else :
                print("NO")
                break
    else :
        if len(stack) == 0 :
            print("YES")
        else :
            print("NO")