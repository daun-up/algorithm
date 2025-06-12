# 3 개 수를 더해서 0 이 되는 조합을 찾는 것
def solution(number):
    answer = 0
    n = len(number)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer