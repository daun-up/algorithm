def solution(x) :
    global answer
    if len(data) == 2 :
        answer = max(x, answer)
        return
    
    for i in range(1, len(data) - 1) :
        target = data[i-1] * data[i+1]
        
        tmp = data.pop(i)
        solution(x + target)
        data.insert(i, tmp)
        
n = int(input())
data = list(map(int,input().split()))

answer = 0
        
solution(0)
print(answer)
        
        
    