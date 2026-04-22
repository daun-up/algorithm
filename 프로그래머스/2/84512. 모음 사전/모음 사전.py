from itertools import product
def solution(word):
    answer = 0
    data = ['A', 'E', 'I', 'O', 'U']
    prod = [] # 중복 순열
    
    for i in range(1, 6):
        for p in product(data, repeat=i):
            prod.append(''.join(p))
    # 사전 순 정렬
    prod.sort()
    
    for i in range(len(prod)):
        if prod[i] == word:
            answer = i + 1
    
    return answer