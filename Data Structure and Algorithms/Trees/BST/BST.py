class BinarySearchTree(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def preOrder(root):
    if root is None:
        return
    
    print(root.data, end=' ')
    preOrder(root.left)
   
    preOrder(root.right)
    

def search(root,value):
    if root is None:
        print("Not Found")
        return -1

    if root.data > value:
        search(root.left,value)
    elif root.data == value:
        print("Found")
         
    else:
        search(root.right,value)

    return

def extractMin(root):
    """ Find that smallest element in a BST which is the left most element """
    if root is not None:
        while root.left:
            root = root.left


        return root.data

def isBST(root):
    """ Given a Binary Tree check if it is a BST or not 
    Checking for validity while doing the inorder traversal
    """
    if root:

        left = isBST(root.left)
        if not left:
            return False

        if isBST.prev is not None and root.data <= isBST.prev.data:
            return False

        isBST.prev = root 

        return isBST(root.right)
    
    return True

def kthsmallest(root):
    """ printing the kth smallest element in a BST """
    if root is None or kthsmallest.k<1:
        return

    kthsmallest(root.left)
    kthsmallest.k-=1
    if kthsmallest.k==0:
        print(root.data)

    kthsmallest(root.right)


def add_greater_values(root):
    """Add all greater values to every node in a given BST"""
    if root is None:
        return

    add_greater_values(root.right)
    add_greater_values.cumulative += root.data
    root.data = add_greater_values.cumulative
    add_greater_values(root.left)


def merge_bst(root1, root2):
    """ Given 2 unbalanced BSTs, print the inorder traversal of the merged resultant tree 
    Algo: Iterative inorder traversal
    DS: One stack per tree  
    """
    if root1 is None:
        inorder(root2)
        return
    elif  root2 is None:
        inorder(root1)
        return 
    current1 = root1 
    current2 = root2 

    stack1 = []
    stack2 = []

    while(len(stack1)!=0 or len(stack2)!=0 or current1 is not None or current2 is not None):
        if current1 is not None:
            stack1.append(current1)
            current1 = current1.left

        if current2 is not None:
            stack2.append(current2)
            current2 = current2.left
        
        if len(stack1) == 0:
            while len(stack2) > 0:
                current2 = stack2.pop()
                current2.left = None
                inorder(current2)
            return 
        if len(stack2)==0:
            while len(stack1)>0:
                current1 = stack1.pop()
                current1.left = None
                inorder(current1)
            return


        current1 = stack1.pop()
        current2 = stack2.pop()

        if current1.data < current2.data:
            print(current1.data)
            current1 = current1.next
            stack2.append(current2)
            current2 = None 
        else:
            print(current2.data)
            current2 = current2.next
            stack1.append(current1)
            current1 = None

def pair_sum_exists(root, value):
    """Returns true if a pair with target sum exists in BST, otherwise false"""
    


if __name__ == "__main__":
    myTree = BinarySearchTree(6)
    insert(myTree,3)
    insert(myTree,5)
    insert(myTree,13)
    insert(myTree,8)
    insert(myTree,9)
    insert(myTree,1)
    insert(myTree,4)
    inorder(myTree)
    print("")
    kthsmallest.k = 3
    kthsmallest(myTree)
    add_greater_values.cumulative = 0 
    add_greater_values(myTree)
    inorder(myTree)
    print("")

"""    print("")
    searchKey = 13
    print("chaecking for "+str(searchKey)+"...")
    search(myTree,searchKey)
    searchKey = 11
    print("chaecking for "+str(searchKey)+"...")
    search(myTree,searchKey)
    print("Finding Min")
    print(extractMin(myTree))
    insert(myTree,-1)
    inorder(myTree)
"""









