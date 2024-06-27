# import sys
# input = sys.stdin.readline()

N, K = map(int,input().split()) 
array = [i for i in range(1, N+1)] # 처음에 원에 앉아 있는 사람들

answer = []
idx = 0 # 제거되는 사람의 인덱스

for i in range(N) :
    idx += K - 1
    if (idx >= len(array)):
        idx = idx % len(array)
    answer.append(str(array.pop(idx)))
# answer = list(map(int,answer))
    
print("<", ", ".join(answer),">", sep="")