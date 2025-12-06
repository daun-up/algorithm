# 마지막 줄에는 0 0 0 이 입력됨

while True:
    a,b,c = map(int,input().split())
    
    # 종료 조건
    if a == b == c == 0:
        break
    
    if c**2 == (a**2 + b**2) or b**2 == (a**2 + c**2) or a**2 == (b**2 + c**2):
        print("right")
    else:
        print("wrong")
    