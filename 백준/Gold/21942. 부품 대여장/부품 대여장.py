from datetime import datetime, timedelta

n, l, f = input().split()

n = int(n) # 부품 대여장에 작성된 정보의 개수
rental_period_str = l # 대여 기간 DDD/hh:mm 일/시간:분
fine_per_minute = int(f) # 벌금

# 대여 기간 문자열을 실제 시간으로 변환
# "DDD/hh:mm" 형식을 / 와 : 기준으로 분리
days_str, time_str = rental_period_str.split('/')
hours_str, minutes_str = time_str.split(':')

# 대여 기간을 timedelta 객체로 만들어 계산에 용이하게 함
rental_period = timedelta(days=int(days_str), hours=int(hours_str), minutes=int(minutes_str))

# 대여 기록을 저장할 딕셔너리
rentals = {}
# 회원별 벌금을 저장할 딕셔너리
fines = {}

for _ in range(1, n+1) :
    log = input().split()
    
    # 날짜와 시간 문자열을 datetime 객체로 변환
    date_str, time_str, part_name, member_name = log[0], log[1], log[2], log[3]
    
    # 두 문자열을 합치고, strptime을 이용해 datetime 객체로 변환
    # 'strptime'은 문자열을 파싱(parsing)해서 datetime 객체를 만든다는 의미
    timestamp = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    
    # 처리할 대여 기록의 키
    rental_key = (part_name, member_name)

    # 이 회원의 벌금 기록이 없으면 0으로 초기화
    if member_name not in fines:
        fines[member_name] = 0
    # '대여' 처리: rentals 딕셔너리에 키가 없는 경우
    if rental_key not in rentals:
        rentals[rental_key] = timestamp  # (부품, 회원)을 키로, 대여 시간을 값으로 저장
    
    # '반납' 처리: rentals 딕셔너리에 키가 이미 있는 경우
    else:
        # 대여 시작 시간 가져오기
        rental_start_time = rentals[rental_key]
        # 총 대여 시간 계산
        total_rental_time = timestamp - rental_start_time
        
        # 허용된 대여 기간을 초과했는지 확인
        if total_rental_time > rental_period:
            # 연체 시간(분 단위) 계산
            overdue_time = total_rental_time - rental_period
            overdue_minutes = int(overdue_time.total_seconds() / 60)
            
            # 벌금 계산 후 해당 회원의 벌금에 누적
            fines[member_name] += overdue_minutes * fine_per_minute
            
        # 반납 처리 완료했으므로, 대여 기록에서 삭제
        del rentals[rental_key]

# 모든 로그 처리 후 결과 출력
# 벌금이 있는 회원만 이름순으로 정렬하여 출력
sorted_fines = sorted(fines.items())

found_fine = False # 벌금을 내는 사람의 존재 여부

for member, fine in sorted_fines:
    if fine > 0:
        print(member, fine)
        found_fine = True

if not found_fine: # 벌금을 내야 하는 사람이 없는 경우
    print(-1) 

    
    
    