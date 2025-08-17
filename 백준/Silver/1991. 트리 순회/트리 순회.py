n = int(input())

tree = {}

for _ in range(n) :
    root, left, right = input().split()
    tree[root] = [left, right] # dictionary 에 값 추가하기
    
# root -> left -> right
def preorder(root) :
    if root != '.' :
        print(root, end = '')
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right
 
# left -> root -> right   
def inorder(root) :
    if root != '.' :
        inorder(tree[root][0]) # left
        print(root, end = '')
        inorder(tree[root][1]) # right


# left -> right -> root 순서
def postorder(root) :
    if root != '.' :
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end = '')

# 항상 A가 루트 노드

preorder('A')
print()
inorder('A')
print()
postorder('A')