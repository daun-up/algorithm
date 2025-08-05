t = int(input())

for _ in range(t) :
    n, m = map(int,input().split())
    
    data = list(map(int,input().split()))
    
    result = 1 # 인쇄 순서 (최소 1번부터 시작)
    
    while data :
        if data[0] < max(data) :
            data.append(data.pop(0)) # 맨 앞 문서를 꺼내서 뒤로 붙임
        else :
            if m == 0 : break # 내가 찾던 문서가 인쇄됨 -> 바로 종료
            
            data.pop(0) # 아니라면 
            result += 1
        
        # 위치 업데이트 (문서의 위치가 계속 바뀌므로 찾고 있던 문서의 위치 이동)
        if m > 0 : # 아직 뒤에 있으므로 그냥 한 칸 앞으로 이동
            m = m - 1
        else : # 맨 앞에 있었기 때문에 맨 뒤로 이동했으므로 길이 줄이기
            m = len(data) - 1
    print(result)