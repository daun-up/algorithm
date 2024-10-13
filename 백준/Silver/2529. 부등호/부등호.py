def check(i, j, oper):
    if oper == "<":
        return i < j  # 부등호가 <일 때, i < j 인지 확인
    else:
        return i > j  # 부등호가 >일 때, i > j 인지 확인
    
def backtracking(idx, num):
    if idx == k + 1:  # 숫자 k+1개를 모두 선택한 경우
        answer.append(num)  # 정답 리스트에 숫자 저장
        return
    for i in range(10):  # 0부터 9까지 숫자 시도
        if not used[i]:  # 해당 숫자가 아직 사용되지 않았으면
            if idx == 0 or check(num[idx-1], str(i), oper[idx-1]):  # 부등호 조건을 만족하면
                used[i] = True  # 해당 숫자를 사용 중으로 표시
                backtracking(idx + 1, num + str(i))  # 다음 자리로 이동하여 재귀 호출
                used[i] = False  # 해당 숫자 사용 완료 후 다시 미사용 상태로 되돌림
    
k = int(input())  # 부등호의 개수 입력
oper = list(input().split())  # 부등호 리스트 입력

used = [False] * 10  # 숫자의 사용 여부를 기록하는 리스트
answer = []  # 정답을 저장할 리스트
backtracking(0, '')  # 백트래킹 시작

answer.sort()  # 정답 리스트 정렬
print(answer[-1])  # 가장 큰 숫자 출력
print(answer[0])  # 가장 작은 숫자 출력