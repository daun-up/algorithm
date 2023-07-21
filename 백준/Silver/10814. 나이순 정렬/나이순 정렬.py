n = int(input())
list = []

for i in range(n):
    age, name = map(str,input().split())
    age = int(age) # 형 변환
    list.append((age, name))

list.sort(key= lambda x:x[0])

for i in list :
    print(i[0], i[1])