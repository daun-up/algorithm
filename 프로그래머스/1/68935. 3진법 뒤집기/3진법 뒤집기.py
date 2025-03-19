def solution(n):
    answer = 0
    tmp = []
    while n > 0 :
        tmp.append(n % 3) # 3 진법의 자릿수가 낮은 자리부터 높은 자리 순으로 저장
        n = n // 3
    # 3진법: 1200 (뒤집힌 순서로 저장됨: [0, 0, 2, 1])
        
    for i in range(len(tmp)) :
        # tmp 의 각 자릿수에 3 의 거듭제곱을 곱해서 10 진수로 변환
        # 가장 높은 자리(왼쪽)는 큰 가중치(3의 높은 제곱수)를 가져야 함
        # 근데 뒤집혀 있으니까 len(tmp) -1 -i 를 사용
        answer += tmp[i] * (3 ** (len(tmp) -1 -i))
    return answer