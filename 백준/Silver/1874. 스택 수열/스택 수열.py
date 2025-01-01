# 스택에 "push" 하는 순서가 오름차순이다.
# 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 나중에 들어간 자료가 가장 먼저 나오는 특징을 가지고 있다.

n = int(input())

stack = [] # 여기에 추가
answer = [] # 수열을 저장
cnt = 1
flag = True

for _ in range(n) :
    num = int(input())
    
    # num 이하 숫자까지 stack 에 넣기
    while cnt <= num :
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    
    # num 이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num :
        stack.pop()
        answer.append('-')
    else :
        # print('NO')
        # break 반복문만 종료됨
        # sys.exit() 라이브러리를 사용해야 함
        
        flag = False
        break
        

if flag :
    for i in answer :
        print(i)
else :
    print("NO")