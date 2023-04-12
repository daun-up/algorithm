import sys
input = sys.stdin.readline

n = int(input().rstrip()) 
words = [] # 배열 만들어주기

for i in range(n):
    word = input().rstrip() # n 만큼 input 입력을 받고
    words.append(word) # words 배열에 추가해줌

result = list(set(words)) # 중복 제거
result.sort() # 같은 길이일 때 알파벳 정렬
result.sort(key = len) # 길이로 정렬

for j in result:
    print(j)