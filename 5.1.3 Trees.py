class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
        
root = Node('A')
root.left = Node('B')
root.right = Node('C')

root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.left.right.right = Node('K')
root.right.left.left = Node('L')
root.right.left.right = Node('M')
root.right.right.left = Node('N')
root.right.right.right = Node('O')
`
def traverse(node, height):
    if node is None:
        return
    elif height==1:
        print(node.val)
    else:
        traverse(node.left, height-1)
        traverse(node.right, height-1)
for i in range(4):    
    traverse(root, i+1)
    