n = list(input()) # 문자열로 입력 받아야 함!, 파이썬은 문자열 숫자도 정렬

n.sort(reverse=True)

print(''.join(n))