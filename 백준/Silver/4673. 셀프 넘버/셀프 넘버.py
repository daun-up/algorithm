# 생성자를 생성하는 함수
def make_generated(n):
    result = n
    for ch in str(n): # 문자열로 바꿔 각 자리 더하기
        result += int(ch)
    return result

generated = set() # 생성자

for i in range(1, 10001):
    g = make_generated(i) # 생성자를 생성
    if g <= 10000: # 생성자가 범위 안일 때만 추가
        generated.add(g)

for i in range(1, 10001):
    if i not in generated: # 생성자가 없는 수 (셀프 넘버)
        print(i)
