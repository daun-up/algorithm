def solution(t, p):
    answer = 0
    tmp = ''
    # 슬라이딩 윈도우
    for i in range(len(t)- len(p) + 1):
        tmp = t[i:i+len(p)]
        print(tmp)
        if tmp <= p:
            answer += 1
    return answer