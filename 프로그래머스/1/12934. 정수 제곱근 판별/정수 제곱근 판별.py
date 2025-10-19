def solution(n):
    # 제곱 판별 어떻게 하더라
    tmp = int(n)**(1/2)
    
    if tmp == int(tmp): # 정수 x 일 때
        return (tmp+1)**2
    else:
        return -1