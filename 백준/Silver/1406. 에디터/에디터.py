# import sys
# input = sys.stdin.readline

# n = list(input().strip())
# m = int(input())
# cursor = len(n) # 커서는 인덱스인데, 처음에 문자열의 맨 뒤에 위치해있다고 하니까 입력된 문자열의 길이로 초기화한다.
# # stack = []

# for _ in range(m) :
#     command = list(input().split())
    
#     if command[0] == "P" :
#         n.insert(cursor, command[1])
#         cursor += 1
#     elif command[0] == "L" :
#         if cursor > 0 :
#             cursor -= 1
#     elif command[0] == "D" :
#         if cursor == len(n) :
#             cursor += 1
#     else :
#         if cursor > 0 and n:
#             # n.remove(n[cursor-1])
#             n.pop(cursor - 1)
#             cursor -= 1 # 이걸 꼭 해줘야함!!

# print(''.join(n))
        
# # -> 런타임 에러 stack 을 사용하여 푸는 방법이 있을까?
# # 리스트를 직접 다루는 방식 (insert, remove) 등은 중간 삽입과 삭제 시 비용이 크다.

# # 큐로 풀면 되나??

# # n = list(input().split())
# # m = int(input())



import sys
input = sys.stdin.readline

n = list(input().strip())  # 초기 문자열
m = int(input().strip())  # 명령어 개수
left = n  # 초기 문자열을 왼쪽 스택으로 설정
right = []  # 오른쪽 스택은 빈 리스트로 시작

for _ in range(m):
    command = input().strip().split()  # 명령어 입력

    if command[0] == "P":  # 문자 삽입
        left.append(command[1])
    elif command[0] == "L":  # 커서를 왼쪽으로 이동
        if left:  # 왼쪽 스택이 비어있지 않을 때
            right.append(left.pop())
    elif command[0] == "D":  # 커서를 오른쪽으로 이동
        if right:  # 오른쪽 스택이 비어있지 않을 때
            left.append(right.pop())
    elif command[0] == "B":  # 커서 왼쪽 문자 삭제
        if left:  # 왼쪽 스택이 비어있지 않을 때
            left.pop()

# 결과 출력: 왼쪽 스택 + 오른쪽 스택의 반전
print(''.join(left + right[::-1]))

# https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-1406-%EC%97%90%EB%94%94%ED%84%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC