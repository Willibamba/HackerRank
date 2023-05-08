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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# The function is to return the lowest common ancestor of v1 and v2 in the Binary Search Tree (BST), 
# Given pointer to the root of the BST

def lca(root, v1, v2):
    #Enter your code here

    # Enque root to the queue
    queue = [root]

    # While queue is not empty, dequeue the first item in queue as an ancestor
    while len(queue) > 0:
        ancestor = queue.pop(0)

        # If ancestor is not Null and meet one of the conditions in second If statement then
        # Return the ancestor as Lower Common Ancestor
        if ancestor:
            if (ancestor.info >= v1 and ancestor.info <= v2) or (ancestor.info <= v1 and ancestor.info >= v2):
                return ancestor
            
        # If the left and/or right child is not Null, append in enqueue to the queue        
        if ancestor.left:
            queue.append(ancestor.left)
        if ancestor.right:
            queue.append(ancestor.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
