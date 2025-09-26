def solution(n, arr1, arr2):
    answer = []
    arr1_bin = [bin(i)[2:].zfill(n) for i in arr1]
    arr2_bin = [bin(i)[2:].zfill(n) for i in arr2]
    
    for a,b in zip(arr1_bin, arr2_bin):
        tmp = ''
        for x,y in zip(a,b):
            if x == '1' or y == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    
    return answer