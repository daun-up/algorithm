def solution(array, commands):
    answer = []
    # commands = [i,j,k]
    for command in commands:
        # print(command)
        i,j,k = command
        # sliced = array[i-1:j]
        # sliced.sort()
        # answer.append(sliced[k-1])
        answer.append(list(sorted(array[i-1:j]))[k-1])
            
    return answer

# 파이썬에서 슬라이싱을 할 때는 첫 번째 인덱스는 포함하고 끝 인덱스는 포함하지 않음
# k번째 수(1-based) -> 0-based -> k-1
# i번째 수(1-based) -> 0-based -> i-1
