def solution(price):
    if price >= 500000:
        price *= 0.80
    elif price >= 300000:
        price *= 0.90
    elif price >= 100000:
        price *= 0.95
    
    return int(price)  # 정수형 변환