# 나이 순, 나이가 같으면 가입한 순
n = int(input())

members = []

for i in range(n) :
    age, name = input().split()
    
    members.append((int(age), i, name))
    
members.sort(key=lambda x:(x[0], x[1]))
# x[0] 은 나이
# x[1] 은 입력 순서
# 정렬 기준을 (나이, 입력순서) 튜플로 한다는 뜻

for age, _, name in members :
    print(age, name)

