n = int(input()) # 스위치의 개수
status = list(map(int,input().split())) # 스위치의 상태
students_num = int(input()) # 학생 수

students = [tuple(map(int,input().split())) for _ in range(students_num)] # 성별, 학생이 받은 스위치 수 (남학생 1 여학생 2)


for gender, num in students :
    if gender == 1 : # s남
        for i in range(num - 1, len(status), num) :
            status[i] = 1 - status[i]
    else : # 여학생
        idx = num - 1
        status[idx] = 1 - status[idx]
        
        d = 1
        
        while idx - d >= 0 and idx + d < len(status) :
            if status[idx - d] == status[idx + d] :
                status[idx - d] = 1 - status[idx - d]
                status[idx + d] = 1 - status[idx + d]
                d += 1
            else :
                break

for i in range(len(status)) :
    print(status[i], end=' ')
    
    if (i + 1) % 20 == 0 :
        print()