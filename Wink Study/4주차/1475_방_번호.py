import sys
input = sys.stdin.readline

n = input().rstrip()
list = [0]*10 # 위치 리스트 생성

for i in range(len(n)):
    num = int(n[i]) # int 변환
    if num == 6 or num == 9 : # 만약 6 이나 9 일 때
        if list[6] <= list[9]: 
            list[6] += 1
        else :
            list[9] += 1
    else :
        list[num] += 1
print(max(list))
        






