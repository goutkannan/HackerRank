"""
Sorted order printing of a given array that represents a BST
Given an array that stores a complete Binary Search Tree, write a function that efficiently prints the given array in ascending order.

For example, given an array [4, 2, 5, 1, 3], the function should print 1, 2, 3, 4, 5
"""


def inorderPrint(array,start,end):
    if start > end:
        return

    inorderPrint(array,2*start+1,end)
    print(array[start],end=' ')
    inorderPrint(array,2*start+2,end)



if __name__=="__main__":
    arr = [4,2,5,1,3,4.5,6,-1 ]
    inorderPrint(arr,0,len(arr)-1)


