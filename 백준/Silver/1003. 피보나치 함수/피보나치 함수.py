# t = int(input())

# for i in range(t) :
#     n = int(input())
#     a, b = 1, 0 # 0 과 1 이 출력된 횟수
#     for i in range(n) :
#         # 0 은 1 이 호출된 횟수만큼, 1 은 0 과 1 이 호출된 합만큼 출력됨
#         a,b = b, a+b
#     print(a,b)

# 0 과 1 의 호출 횟수를 저장하는 배열을 만들어준다.

t = int(input()) # 테스트 케이스
for _ in range(t):
    n = int(input())

    # 0과 1의 호출 횟수(N은 40보다 작거나 같은 자연수 또는 0)
    zero = [0] * (41)
    one = [0] * (41)
    
    zero[0], one[0] = 1, 0 # f(0)
    zero[1], one[1] = 0, 1 # f(1)

    for i in range(2, n+1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    print(zero[n], one[n])

