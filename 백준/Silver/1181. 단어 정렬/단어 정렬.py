n = int(input())

words = [input() for _ in range(n)]

words = list(set(words)) # 중복된 단어는 제거

words.sort() # 사전 순으로 정렬
words.sort(key=len) # 길이 순으로 정렬

for i in words:
    print(i)