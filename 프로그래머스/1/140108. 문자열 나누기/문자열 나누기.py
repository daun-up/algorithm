def solution(s):
    answer = 0
    same = 0
    different = 0
    
    for ch in s:
        # 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
        if same == different:
            answer += 1
            x = ch
        
        if ch == x:
            same += 1
        else:
            different += 1

    return answer