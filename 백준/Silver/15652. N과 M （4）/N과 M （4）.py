n, m = map(int, input().split())

numList = [i for i in range(1, n+1)]

def backtracking(result, start) :
    if(len(result) == m) :
        print(*result)
        return
    for i in range(start, n+1) :
        result.append(i)
        backtracking(result, i)
        result.pop()
        
backtracking([], 1)
