k = int(input())
num_list = [int(input()) for _ in range(k)]
stack = []

for i in range(k) :
    
    if num_list[i] == 0 :
        stack.pop()
    else :
        stack.append(num_list[i])
    

print(sum(stack))