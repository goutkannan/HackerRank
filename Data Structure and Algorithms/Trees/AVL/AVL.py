"""
Implementation of AVL Trees with search, insert functionalities  
"""

class AVLTree(object):
    """ Building block of AVL Tree """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

def diff_height(root):
    """ Difference in heights of left sub-trees and right sub-trees  """
    return root.left.height - root.right.height

def right_rotate(root):
    """
     The left child of the root becomes the new root, 
     save the prev right child and make it the left child of the old root
                old_root                                  new_root
       new_root           right      =========>      cleft        old_root   
    cleft    cright                                           cright    right  
    """

    y = root.left 
    temp_x = y.right

    y.right = root
    root.left = temp_x

    root.height = max(root.left.height, root.right.height) + 1
    y.height = max(y.left.height, y.right.height) + 1

    return y

def left_rotate(root):
    """
    The right child of the current root becomes the new root and
    its left child becomes the right child of the old root. 
            old_root                                new_root
        cleft     new_root        ====>     old_root        ccright
                ccleft  ccright          cleft     ccleft

    """
    y = root.right
    temp_x = y.left  

    root.right = temp_x
    y.left = root

    root.height = max(root.left.height, root.right.height) + 1
    y.height = max(y.left.height, y.right.height) + 1

    return y 


def insert(root,value):
    """ Do a binary search and insert the new node """ 
    if root is None:
        root = AVLTree(value)
    if root.data > value:
        root.left = insert(root.left,value)
    else:
        root.left = insert(root.right,value)

    root.height =  1 + max(root.left,root.right)
    difference = diff_height(root)

    if difference > 1 and value < root.left.data:
        return right_rotate(root)

    if difference < -1 and value > root.right.data:
        return left_rotate(root)

    if difference > 1 and value > root.left.data: 
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if difference < -1 and value < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root 












def inorder(root):
    """ Visualizing the tree in the sorted form """
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)



