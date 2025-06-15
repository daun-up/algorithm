# 서로 다른 두 개의 수를 뽑아 더해서 만들 수 있는 경우 (조합)
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)
