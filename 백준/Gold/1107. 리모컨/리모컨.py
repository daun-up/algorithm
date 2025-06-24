import sys
input = sys.stdin.readline
n = int(input().strip()) # 이동하려고 하는 채널
m = int(input().strip()) # 고장난 버튼의 개수
broken = list(map(int,input().strip().split())) # 고장난 버튼

result = abs(n - 100)

for i in range(1000000) :
    for j in str(i) :
        if int(j) in broken : # 무조건 int 씌워줘야함
            break 
    else :
        result = min(result, len(str(i)) + abs(i - n))
print(result)