N = int(input())

dic = {}
for _ in range(N):
    
    num = int(input())
    
    if dic.get(num, 0):
        dic[num] += 1
    else:
        dic[num] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(dic[0][0])