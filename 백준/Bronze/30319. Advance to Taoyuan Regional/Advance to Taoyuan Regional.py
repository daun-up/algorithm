from datetime import datetime, timedelta

# 입력 받기
string = input().strip()

# 입력된 날짜 문자열을 datetime 객체로 변환
date = datetime.strptime(string, '%Y-%m-%d')

# 2023년 10월 21일로부터 35일 이전 날짜 계산
deadline = datetime(2023, 10, 21) - timedelta(days=35)

# 날짜 비교
if date > deadline:
    print("TOO LATE")
else:
    print("GOOD")
