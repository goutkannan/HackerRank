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
    inorder(root.left)
   
    inorder(root.right)
    

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
    if root is not None:
        while(root.left):
            root = root.left


        return root.data
    
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










