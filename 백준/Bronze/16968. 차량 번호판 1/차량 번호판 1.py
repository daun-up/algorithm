data = input()
count = 1


for i in range(len(data)):
    if data[i] == "c":
        if i > 0 and data[i] == data[i - 1]:  # 첫 번째 인덱스는 비교하지 않음
            count *= 25
        else:
            count *= 26
    elif data[i] == "d":
        if i > 0 and data[i] == data[i - 1]:  # 첫 번째 인덱스는 비교하지 않음
            count *= 9
        else:
            count *= 10

print(count)