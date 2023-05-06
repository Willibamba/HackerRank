class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        #Set the root as the parent node
        parent = self.root
        if parent == None:
            self.root = Node(val)
            return
        
        # While the parent is not null, keep iterating for insertion position
        while parent:
            # If true, insert to the left-child else left-child is the parent
            if parent.info > val:
                if parent.left == None:
                    parent.left = Node(val)
                    return
                parent = parent.left
            # If true, insert to the right-child else right-child is the parent   
            elif parent.info < val:
                if parent.right == None:
                    parent.right = Node(val)
                    return    
                parent = parent.right
        

        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
