t = int(input())

for i in range(t) :
    stack = []
    
    data = input()
    
    for j in data :
        if j == '(' :
            stack.append(j)
        elif j == ')' :
            if len(stack) != 0 :
                stack.pop()
            else :
                print("NO")
                break
    else :
        if not stack :
            print("YES")
        else :
            print("NO")
