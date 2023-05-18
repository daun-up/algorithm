import sys
input = sys.stdin.readline

N,L = map(int,input().rstrip().split()) # 물이 새는 개수, 테이프의 길이
cnt = 0
complete = 0

p_list = list(map(int,input().split())) # 물이 새는 위치
p_list.sort()

# 테이프로 막은 부분 표시 

for i in (p_list):
    if i > complete :
        complete = i + L - 1 # p_list 의 고칠 위치 값 + 테이프 길이 - 1
        cnt += 1

print(cnt)



