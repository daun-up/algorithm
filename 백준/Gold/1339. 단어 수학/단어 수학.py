n = int(input())

data = []
answer = 0
dic = {}
# 가장 큰 숫자부터 차례대로 곱해서 더함
max_number = 9

for i in range(n):
    data.append(list(input()))  # 입력 문자열을 리스트로 변환하여 저장
    for j in range(len(data[i])):
        # 자릿수에 따라 해당 알파벳에 10의 제곱을 더함
        if data[i][j] in dic:
            dic[data[i][j]] += 10 ** (len(data[i]) - j - 1) # 중복된 알파벳!
        else:
            dic[data[i][j]] = 10 ** (len(data[i]) - j - 1)

# 딕셔너리의 값을 리스트로 변환한 후 내림차순으로 정렬
total = list(dic.values())
total.sort(reverse=True)

for i in total:
    answer += i * max_number
    max_number -= 1

print(answer)