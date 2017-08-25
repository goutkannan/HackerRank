# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:03:05 2017

@author: Goutham
"""
from collections import defaultdict
import copy

class Node:
    def __init__(self,data):
        self.left  = None
        self.right = None
        self.data = data
        
def inorder(root):
    if root :
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def nthLargest(root,n,count):
    if root: 
        nthLargest(root.right,n,count)
        
        print(root.data)
        if n == count:
            return 
        else:
            count[0]+=1

        nthLargest(root.left,n,count)



def pre_order(root):
    if root :
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root :
        
        post_order(root.left)
        post_order(root.right)
        print(root.data)
        

        
def level_order(root):
    """ BFS Using Queues"""
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        curr= queue.pop()
        print(curr.data)
        
        if curr.left is not None and curr.left not in queue:
            queue.append(curr.left)
        if curr.right is not None and curr.right not in queue:
            queue.append(curr.right)
            
def height(root):
    if root is None:
        return 0
    else:
        return 1+max(height(root.left),height(root.right))


def LCA(curr,l,r):
    if curr is None:
        return None
    if curr.data == l.data or curr.data == r.data:
        return curr

    left = LCA(curr.left,l,r)
    right = LCA(curr.right,l,r) 

    if left is not None and right is not None:
        return curr
    
    if left is None:
        return right
    else:
        return left


def diagonal_sum(root,curr_diag,sum):
    if root:
        diagonal_sum(root.left,curr_diag+1,sum)
        if curr_diag in sum.keys():
            sum[curr_diag]+=root.data
        else:
            sum[curr_diag]=root.data

        diagonal_sum(root.right, curr_diag,sum)


        
def lca(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root

def reverse(root):
    if root is None:
        return None

    reverse(root.left)
    reverse(root.right)

    root.left,root.right =root.right,root.left


def printnthLevel(root, n):
    assert isinstance(n,int), 'Level must be integer'
    if root is None:
        return 
    if n==1:
        print(root.data)
    elif n>1:
        printnthLevel(root.left,n-1)
        printnthLevel(root.right,n-1)

def diameter(root):
    if root is None:
        return 0 
    lheight = height(root.left)
    rheight = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(lheight+ rheight +1,max(ld,rd))


def printAncestors(root,target):
    if root is None:
        return False
    if root.data == target:
        return True

    if printAncestors(root.left,target) or printAncestors(root.right, target):
        print(root.data)
        return True
    return False

def MorrisTraversal(root):
     
    # Set current to root of binary tree
    current = root 
     
    while(current is not None):
         
        if current.left is None:
            print(current.data,end=' ')
            current = current.right
        else:
            #Find the inorder predecessor of current
            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right
  
            # Make current as right child of its inorder predecessor
            if(pre.right is None):
                pre.right = current
                current = current.left
                 
            # Revert the changes made in if part to restore the 
            # original tree i.e., fix the right child of predecssor
            else:
                pre.right = None
                print(current.data,end=' ')
                current = current.right

def isBST(root):
    if root:
        

        left = isBST(root.left)
        if not left:
            return False
      
        if isBST.prev is not None and root.data <= isBST.prev.data:
            return False

        isBST.prev = root 
        

        return isBST(root.right)
    
    return True

def size(root):
    """count of left subtrees + right subtrees + 1"""

    if root is None:
        return 0

    return size(root.left) + size(root.right) + 1

def largestBST(root):
    """ compute the max number of nodes that form a BST in a given binary tree"""
    isBST.prev = None
    if isBST(root):
        return size(root)
    else:
        return max(largestBST(root.left), largestBST(root.right)) 

def make_bst_util(root):
    """ Given a tree 2 nodes are out of place preventing it becoming a BST
    Utility function that computes the elements to be swapped. 
    """
    if root is None:
        return 

    make_bst_util(root.left)

    if make_bst_util.prev and make_bst_util.prev.data >= root.data:
        if not make_bst_util.first:
            make_bst_util.first= copy.deepcopy(make_bst_util.prev)
            make_bst_util.middle = copy.deepcopy(root)
        else:
            make_bst_util.last = copy.deepcopy(root)
    
    make_bst_util.prev= copy.deepcopy(root)
    make_bst_util(root.right) 

def swap(root, a , b):
    if root:
        if root.data == a.data:
            root.data = b.data 
            
        elif root.data == b.data:
            root.data = a.data

        
        swap(root.left, a, b)
        swap(root.right, a, b)   

def make_bst(root):
    """ Given a tree 2 nodes are out of place preventing it becoming a BST """
    if root:
        make_bst_util.first = None
        make_bst_util.last = None
        make_bst_util.middle = None
        make_bst_util.prev = None

        make_bst_util(root)
        if  make_bst_util.first and make_bst_util.last:
            swap(root,make_bst_util.first,make_bst_util.last)
        elif make_bst_util.first and make_bst_util.middle:
            swap(root,make_bst_util.first,make_bst_util.middle)


if __name__ == "__main__":
    root = Node(5)
    root.left  = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.left.right.right = Node(4.5)
    root.right.left = Node(6)
    root.right.right = Node(8)
    root.right.right.right = Node(21)
    root.right.right.right.left  = Node(19)

    #printnthLevel(root,4)
    print(diameter(root))
    #    printAncestors(root,19)
    root1 = Node(5)
    root1.left  = Node(3)
    root1.right = Node(4)
    root1.left.left = Node(2)
    root1.left.right = Node(3.5)
    MorrisTraversal(root1)
    isBST.prev = None
    print("")
    # print("Size of larget BST is ", largestBST(root1))
    make_bst(root1)
    inorder(root1)

