def solution(arr):
    answer = []
    arr.remove(min(arr))
    if arr :
        answer = arr
    else :
        answer.append(-1)
    return answer