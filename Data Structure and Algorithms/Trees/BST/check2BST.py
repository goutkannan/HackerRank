"""
Given two arrays which represent a sequence of keys. Imagine we make a Binary Search Tree (BST) from each array. We need to tell whether two BSTs will be identical or not without actually constructing the tree.

Examples
For example, the input arrays are {2, 4, 3, 1} and {2, 1, 4, 3} will construct the same tree

 Let the input arrays be a[] and b[]

Example 1:
a[] = {2, 4, 1, 3} will construct following tree.
   2
 /  \
1    4
    /
   3
b[] = {2, 4, 3, 1} will also also construct the same tree.
   2
 /  \
1    4
    /
   3 
So the output is "True"

Example 2:
a[] = {8, 3, 6, 1, 4, 7, 10, 14, 13}
b[] = {8, 10, 14, 3, 6, 4, 1, 7, 13}

They both construct the same following BST, so output is "True"
            8
         /    \
       3       10
     /  \        \
    1     6       14
        /   \     /
       4     7   13  
"""

def check(a,b):
    n1 = len(a)-1
    n2 = len(b)-1   
    if n1 != n2:
        return False

    i = 0 
    j = 0
    idx=-1
    temp=[]
    while(i<n1 and j<n2):
        if a[i]==b[j]:
            i+=1
            j+=1
        elif len(temp)==0:
            temp.append(b[j])
            j+=1
        else:
          

a = [8, 3, 6, 1, 4, 7, 10, 14, 13]
b = [8, 10, 14, 3, 6, 4, 1, 7, 13]

