data = list(input().strip())

visited = [0] * len(data)

order = 'quack'
ducks = 0
max_ducks = 0

result = 0

for i in range(len(data)) :
    if data[i] == 'q' and not visited[i]:
            ducks += 1 # 새로운 오리 울음 시작
            max_ducks = max(max_ducks, ducks)

            idx = 0 # q 부터 매칭 시작
            
            for j in range(i, len(data)):
                if not visited[j] and data[j] == order[idx] :
                    visited[j] = 1
                    idx += 1
                    if idx == 5:
                        # ducks -= 1
                        idx = 0
            if idx != 0:
                result = -1

if result != -1:
    if not all(visited):
        result = -1
    else :
        result = max_ducks

print(result)
                    