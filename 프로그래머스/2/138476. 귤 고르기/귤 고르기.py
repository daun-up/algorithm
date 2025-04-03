def solution(k, tangerine):
    dic = {}

    # 각 종류별 개수 세기
    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1

    # 등장 횟수만 추출해서 정렬 (내림차순)
    counts = sorted(dic.values(), reverse=True)

    total = 0
    answer = 0

    # 가장 많이 나온 것부터 더하다가 k 이상이면 종료
    for c in counts:
        total += c
        answer += 1
        if total >= k:
            break

    return answer
