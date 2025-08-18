n = int(input())
a = list(map(int,input().split()))
x = int(input())

# 수열 a 에서 x 와 서로소인 수들의 평균을 출력
# 서로소 판단해야함 <- 약수... gcd 함수 구현

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

avg = 0
cnt = 0

for i in range(n) :
    if gcd(a[i], x) == 1 :
        avg += a[i]
        cnt += 1
        
if cnt > 0:
    print(avg / cnt)
else:
    print(0) 