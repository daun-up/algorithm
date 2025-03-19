def solution(n, m):
    answer = []
    # 유클리드 호제법 : 최대 공약수 구하기
    answer.append(gcd(n, m))
    answer.append(lcm(n, m, gcd(n, m)))
    return answer

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # a는 b로, b는 a % b로 갱신
    return a  # b가 0일 때 a가 최대공약수

def lcm(a, b, gcd):
    return (a * b) // gcd  # 최소 공배수는 (a * b) / gcd로 계산하고, 정수로 반환