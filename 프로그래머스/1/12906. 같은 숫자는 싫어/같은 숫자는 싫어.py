def solution(arr):
    answer = []
    
    for i in arr:
        if len(answer) == 0 or i != answer[-1]:
            answer.append(i)

    # for i in range(len(arr)):
    #     if i == 0 or arr[i-1] != arr[i]:
    #         answer.append(arr[i])
    return answer