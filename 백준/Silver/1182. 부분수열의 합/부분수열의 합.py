# 크기가 양수인 부분 수열
# 수열의 원소를 다 더한 값이 S 가 되는 경우의 수

def dfs (n, sum, cnt) :
    global answer # 함수 외부에 있는 변수를 함수 내에서 수정하려면 전역 변수임을 명시해줘야 함
    if n == N : # 종료
        if (sum == S and cnt > 0) :
            answer += 1
        return
    # 하부 함수 호출
    # 포함하는 경우
    dfs(n + 1, sum + data[n], cnt + 1)
    # 포함하지 않는 경우
    dfs(n + 1, sum, cnt)

N,S = map(int,input().split())


data = list(map(int,input().split()))


answer = 0

dfs(0, 0, 0)
print(answer)
    
# print(dfs(0, 0, 0))