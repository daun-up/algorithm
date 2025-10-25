def solution(sizes):
    answer = 0
    # 각 명함의 긴 변은 w, 짧은 변은 h로 정렬
    for i in range(len(sizes)):
        w,h = sizes[i]
        # 가로 기준으로 정렬
        if w < h:
            sizes[i] = [h,w]
    
    max_w = max(s[0] for s in sizes)
    max_h = max(s[1] for s in sizes)
    
    answer = max_w * max_h
    
    return answer