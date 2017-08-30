class SplayTree(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def search(root,value):
    if root is None or root.data = value:
        return root

    if root.data > value: # left side
        if root.left is None:
            return root
        # Zig-Zig 
        if root.left.left.data > value:
            root.left.left = search(root.left.left, value)
            root = right_rotate(root)
        # Zig-Zag    
        elif root.left.left.data < value:
            root.left.right = search(root.left.right, value)

            if root.left.right:
                root.left = left_rotate(root.left)
        
        if root.left:
            return right_rotate(root)
        else:
            return root
    else:
        if not root.right :
            return root

        if root.right.key > value:
            root.right.left = search(root.right.left, key)

            if root.right.left:
                root.right = right_rotate(root.right)
        
        elif root.right.key < value:
            root.right.right = search(root.right.right, value)
            root = left_rotate(root)

        if root.right:
            return left_rotate(root)
        else:
            return root



def insert(root,value):
    if root is None:
        root = BinarySearchTree(value)
    if root.data > value:
        if root.left is None:
            root.left  = BinarySearchTree(value)
        else:
            insert(root.left,value)
    else:
        if root.right is None:
            root.right  = BinarySearchTree(value)
        else:
            insert(root.right,value)

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

    return y 

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)