n = int(input())
group = 0

for _ in range(n):
    error = 0
    word = input()
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            if word[index] in word [index+1:]:
                error += 1
    if error == 0 :
        group += 1
print(group)
