# list 만들기
# 비내림차순으로 정렬
n = int(input()) 
A = list(map(int,input().split()))
sorted_A = sorted(A) # 정렬

result = [0] * n 

for i in range(n):
  idx = sorted_A.index(A[i])
  result[i] = idx
  sorted_A[idx] = -1

print(*result)