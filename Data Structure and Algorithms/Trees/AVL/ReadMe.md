
## AVL Trees 

Self balancing binary search trees. In breif, difference in height of left sub-tree and right sub-tree must be <b> 1 or less </b>.
<br>This property solves the problem of the worst case complexities of unbalanced Binary Search Trees. 

Examples of  a valid AVL Tree and a invalid AVL Treee

                10 h(2,1)     
               / \     
       h(1,1) 5   13 h(0,0)    AVL Tree    
             / \       
            3   6
            
            
                10 h(3,1)      
               / \     
      X h(2,0)5   13 h(0,0)   Not a AVL Tree    
             /        
      h(1,0)4
           /
          3
          
#### Advantages of AVL Trees 
<ul>
    <li> All BST operations like search, max, min, insert, delete take O(height of BST time). Keeping the height bounded makes sure that the height remains logn 
    </li>
</ul>




#### Insertion 

Find the place for insertion simillar to that of BST. Insert the new node and then balance the tree, so that the diff in height remains under 1. 

<b> There are 4 possible arrangements </b>

##### 1.Left Left

          15                                      10 
         /  \                                   /    \
        10   17       Left Left                7      15
       / \          - - - - - - - - ->        / \    /   \ 
      7   12          Rotate at 15           6   9   12   17
     / \
    6   9

The first unbalanced node is 15 h(3,1) [from left side] next at 10 h(2,1) [from left side] --> <b> Left Left Case </b> 

##### 2.Left Right 

           15                                 15                                    10
          /  \                               /  \                                 /    \ 
         8   17    Left Rotate (8)          10   17     Right Rotate(15)         8       15
        / \       - - - - - - - - ->       / \           - - - - - - ->         / \     /  \
       7   10                             8   12                               7   9  12    17 
          /  \                           / \                                  
         9   12                         7   9 
         


##### 2.Right Right 

           8                                  10
         /   \                              /    \ 
        7     10      Left Rotate(8)       8      15
             /  \    - - - - - - - ->     / \     / \
            9    15                      7   9   12  17
                /  \
               12  17 
               
               
##### 2.Right Left

           5                                  5                                     9
         /   \                              /   \                                 /   \
        4     15      Right Rotate(15)     4     9      Left Rotate(5)           5     15 
             /  \    - - - - - - - ->           / \     - - - - - - - ->        / \    / \
            9    17                            8   15                          4   8  10  17
           / \                                     / \
          8  10                                   10  17

                                                                    


### Implementation 

Node that forms a AVL Tree is simillar to that of BST with an additional member to height(saves time). 




```python
class AVLTree:
        """ Building block of AVL Tree """
        def __init__(self,data= None):
            """ Constructor for creating new node"""
            self.data = data
            self.left = None
            self.right = None
            self.height = 0        
    
```


```python
def inorder(root):
    """Utility function to print the tree traversal in sorted order to visualize BST """
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
```


```python
def diff_height(root):
    """ Difference in heights of left sub-trees and right sub-trees  """
    return root.left.height - root.right.height
```


```python
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
```


```python
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
```

### Insert a Node

Use binary search to find the location for insertion after insertion the tree has to be balanced. 
There 4 cases of balancing are:

1. When  `height of left sub-tree - height of right sub-tree > 1 and  new key is in left side of the tree.` <br>
      Do a `right rotation`. 

2. When  `height of left sub-tree - height of right sub-tree < -1 and  new key is in right side of the tree.`<br>
      Do a `left rotation`. 
    
3. When  `height of left sub-tree - height of right sub-tree > 1 and  new key is in right side of the tree.` <br>
      Do a `right rotation followed by left rotation`. 

4. When  `height of left sub-tree - height of right sub-tree < -1 and  new key is in left side of the tree.` <br>
      Do a `left rotation followed by right rotation`. 
    


```python
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
```


```python

```
