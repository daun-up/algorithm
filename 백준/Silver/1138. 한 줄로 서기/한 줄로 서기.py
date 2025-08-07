n = int(input())

# 각 사람이 기억하는 '왼쪽에 있던 키 큰 사람의 수'를 리스트로 입력받음
data = list(map(int,input().split()))

# 최종 줄 순서를 저장할 리스트를 0으로 초기화
answer = [0] * n


# 1번부터 n번 사람까지 차례대로 자리를 배치
for i in range(n) :
    # 각 사람을 배치할 때마다 빈칸 카운트를 초기화
    count = 0 
    for j in range(n) :
        # 만약 (지나온 빈칸 수 == 기억하는 수) 이고 (현재 자리가 비어있다면)
        if count == data[i] and answer[j] == 0 :
            # 바로 그 자리에 현재 사람(i+1)을 배치
            answer[j] = i + 1
            # 현재 사람 배치가 끝났으므로 안쪽 루프 탈출
            break
        # 만약 현재 자리가 비어있다면 (아직 내 자리는 아님)
        elif answer[j] == 0 :
            # 나보다 키 큰 사람이 설 자리로 간주하고 빈칸 카운트 1 증가
            count += 1

print(*answer)
