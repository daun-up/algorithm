tmp = 0
tmp_list = []
for i in range(4):
    a,b = map(int,input().split())
    tmp -= a
    tmp += b
    tmp_list.append(tmp)
print(max(tmp_list))
