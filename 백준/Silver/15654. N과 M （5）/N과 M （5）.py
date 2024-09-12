n, m = map(int, input().split())

numList = list(map(int, input().split()))
numList.sort()

def backtracking(result) :
    if len(result) == m :
        print(*result)
        return
    for i in numList : 
        if i not in result :
            result.append(i)
            backtracking(result)
            result.pop()
        
backtracking([])