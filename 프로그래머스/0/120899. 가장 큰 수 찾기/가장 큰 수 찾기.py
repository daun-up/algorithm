def solution(array):
    answer = []
    # for i in range(1,len(array)) :
    #     if array[i-1] < array[i] :
    #         answer.append(array[i])
    #         answer.append(i)
    tmp = max(array)
    answer.append(tmp)
    answer.append(array.index(tmp))
            
    return answer