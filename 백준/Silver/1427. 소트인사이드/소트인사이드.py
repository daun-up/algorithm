n = int(input())
array = list(map(int,str(n)))
array.sort(reverse=True)
for i in array :
    print(i, end = '')
