def solution(food):
    # 칼로리가 낮은 음식 순으로
    # 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 함
    # 중앙에는 물을 배치 -> 물을 먼저 먹는 선수가 승리
    left = ""
    for i in range(1, len(food)):
        # 각 음식 개수 절반만큼 배치
        left += str(i) * (food[i] // 2)
    # 좌측 + 0 + 우측(좌측 뒤집기)
    return left + "0" + left[::-1]
