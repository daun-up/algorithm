# 재귀를 사용하여 번호 조합을 만들어냄
def lotto(arr, s, idx, cnt) : # 선택한 번호를 저장할 배열, 입력 받은 숫자 리스트, 다음 반복문의 시작 위치, 지금까지 선택한 번호의 수
    if cnt == 6 :
        print(*arr)
        return
    for i in range(idx, len(s)) :
        arr[cnt] = s[i]
        # 선택한 번호를 바탕으로 다음 조합 만들기 (백트래킹)
        lotto(arr, s, i + 1, cnt + 1)
        
while True :
    s = list(map(int,input().split()))
    if s[0] == 0 : # 리스트 첫 번째 숫자가 0 이면 종료
        break
    arr = [0] * 6 # 6 개의 번호를 저장할 배열
    lotto(arr, s[1:], 0, 0) # 리스트의 첫 번째 값(숫자 개수)은 제외하고 나머지 숫자들만 넘김
    print()