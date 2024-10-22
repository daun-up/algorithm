score = input().strip().upper()  # 공백 제거 및 대문자로 변환

if score == 'A+':
    print(f"{4.3:.1f}")
elif score == 'A0':
    print(f"{4.0:.1f}")
elif score == 'A-':
    print(f"{3.7:.1f}")
elif score == 'B+':
    print(f"{3.3:.1f}")
elif score == 'B0':
    print(f"{3.0:.1f}")
elif score == 'B-':
    print(f"{2.7:.1f}")
elif score == 'C+':
    print(f"{2.3:.1f}")
elif score == 'C0':
    print(f"{2.0:.1f}")
elif score == 'C-':
    print(f"{1.7:.1f}")
elif score == 'D+':
    print(f"{1.3:.1f}")
elif score == 'D0':
    print(f"{1.0:.1f}")
elif score == 'D-':
    print(f"{0.7:.1f}")
elif score == 'F':
    print(f"{0.0:.1f}")
else:
    print("Invalid score input.")