class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def topView(root):
    #Write your code here
    if root == None:
        return
    # Create dictionay to store the root info and an array to deque and enque
    view = {}
    roots = []
    # Enque root, start the root level to 0
    roots.append(root)
    level = 0
    root.level = level
    
    while len(roots):
        root = roots[0]
        level = root.level
        # If the condition is true
        # add level index and root value to view dictionay
        if level not in view:
            view[level] = root.info
        # if the condition is true, decrement the index and enque left root    
        if root.left:
            root.left.level = level - 1
            roots.append(root.left)
        # if the condition is true, increment the index and enque right root
        if root.right:
            root.right.level = level + 1
            roots.append(root.right)
        # Deque the 0 index     
        roots.pop(0)
    # Loop through and sorted view dictionary
    # print the values on a single line separated by space     
    for value in sorted(view):        
        print(view[value], end=" ")   
        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)