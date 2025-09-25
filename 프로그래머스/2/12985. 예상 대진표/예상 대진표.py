def solution(n,a,b):
    answer = 0
    # 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지
    # A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정
    # 이기면 -1 됨 (순번이)
    while a!= b :
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer