def solution(brown, yellow):
    answer = []
    w, h = 0,0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow // i
            h = i
            if (2*w + 2*h + 4) == brown:
                answer.append(w+2)
                answer.append(h+2)
                break
                
                
    answer.sort(reverse=True)
    
    
    return answer