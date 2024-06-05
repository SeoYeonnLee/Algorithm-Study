import sys

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    data, left, right = sys.stdin.readline().split()
    tree[data] = [left, right]

def preOrder(root):
    if root == '.':
        return
    
    print(root, end='')
    preOrder(tree[root][0])
    preOrder(tree[root][1])

def inOrder(root):
    if root == '.':
        return
    
    inOrder(tree[root][0])
    print(root, end='')
    inOrder(tree[root][1])

def postOrder(root):
    if root == '.':
        return
    
    postOrder(tree[root][0])
    postOrder(tree[root][1])
    print(root, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')