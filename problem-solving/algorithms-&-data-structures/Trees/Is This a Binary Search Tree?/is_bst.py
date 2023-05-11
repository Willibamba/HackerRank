""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

# The function uses inorder traversal to check if Binary Tree is a Binary Search Tree (BST) or not
def check_binary_search_tree_(root, array = []):
    
    if root.left:
        check_binary_search_tree_(root.left, array)
        
    array.append(root.data)
    
    if root.right:
        check_binary_search_tree_(root.right, array)
    # The condition to check if there is duplicates or not sorted 
    if len(array) > len(set(array)) or array != sorted(array):
        return False
    
    return True