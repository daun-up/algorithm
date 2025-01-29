n = int(input())

list = [list(map(int,input().split())) for _ in range(n)] 

def solution(i) :
    if i >= n : # i 는 날짜
        return 0 # 종료 조건 : 날짜가 제시된 n 보다 크거나 같으면 종료
    money = 0
    if i + list[i][0] <= n : # 현재 날짜에서 상담에 필요한 날짜를 더했을 때 n 보다 작거나 같아야함
        money = solution(i + list[i][0]) + list[i][1] # 현재 상담을 끝낸 후 가능한 최댓값 + 현재 상담을 선택했을 때 벌 수 있는 돈을 더함
    money = max(money, solution(i+1)) # 현재 상담을 건너뛰고 다음 날(i+1)로 이동하는 경우와 현재 상담을 진행하는 경우를 비교하여 최대값을 선택
    return money
print(solution(0))