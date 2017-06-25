# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:03:05 2017

@author: Goutham
"""
from collections import defaultdict

class Node:
    def __init__(self,data):
        self.left  = None
        self.right = None
        self.data = data
        
def inorder(root):
    if root :
        inorder(root.left)
        print(root.data)
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
        
""" BFS Using Queues"""
        
def level_order(root):
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

        diagonal_sum(root.right,curr_diag,sum)


        
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

root = Node(5)
root.left  = Node(3)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.right = Node(4.5)
root.right.left = Node(6)
root.right.right = Node(8)
lhs = Node(4.5)
rhs = Node(3)

"""
     5
  3     7
 3 4    6 8
   4.5



"""



inorder(root)
print("reverse")
reverse(root)

inorder(root)


#inorder(root)
#print("Level Order")
#level_order(root)
"""
l=lca(root,3,4.5)

if l is not None:
    print (l.data)

lca_1 = LCA(root,lhs,rhs)
print (lca_1.data)
count=[0]
print("Height %d" % height(root))
print(nthLargest(root,2,count))

d_sum = defaultdict()
diagonal_sum(root,0,d_sum)
max_diag,max_sum = max(d_sum.items(), key=lambda  x: x[1])
print(max_diag,max_sum)   """