n = int(input())

tree = list(map(int,input().split()))

remove_node = int(input())

def dfs(remove_node) :
    tree[remove_node] = -10
    for i in range(n) :
        if remove_node == tree[i] :
            dfs(i)
dfs(remove_node)

count = 0

for i in range(n) :
    if tree[i] != -10 and i not in tree :
        count += 1
print(count)