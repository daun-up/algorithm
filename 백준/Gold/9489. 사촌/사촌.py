# 사촌

# k 의 부모와 다르고, 부모의 부모가 일치하면 카운트

while True:
    n, k = map(int,input().split())
    
    if n == 0 and k == 0: # 종료 조건
        break
    
    nodes = list(map(int,input().split()))
    
    parent = [-1] * n # 각 노드의 부모 노드의 인덱스를 저장할 배열

    
    cur_parent_idx = -1 # 현재 부모의 인덱스
    # cur_parent_idx = 0

    # parent[0] = -1
    
    for i in range(1, n): # 모든 노드에 부모 만들어주기
        if nodes[i] == nodes[i-1] + 1: # 값이 연속인가? (같은 부모라는 뜻)
            # 같은 부모의 자식들은 값이 연속된 증가로 주어짐
            parent[i] = cur_parent_idx
        else: # 부모가 달라짐
            cur_parent_idx += 1
            parent[i] = cur_parent_idx
    
    k_idx = nodes.index(k)
    k_parent_idx = parent[k_idx]
    
    ans = 0

    # k의 부모가 존재하고, 그 부모의 부모(조부모)도 존재해야 사촌이 가능
    if k_parent_idx != -1 and parent[k_parent_idx] != -1:
        k_grandparent_idx = parent[k_parent_idx] # 부모의 부모
        for i in range(1,n):
            if parent[i] != k_parent_idx and parent[parent[i]] == k_grandparent_idx:
                ans += 1
    else:
        ans = 0

    print(ans)