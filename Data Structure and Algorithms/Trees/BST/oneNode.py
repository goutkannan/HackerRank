"""
Check if each internal node of a BST has exactly one child
Given Preorder traversal of a BST, check if each non-leaf node has only one child. Assume that the BST contains unique entries.

Examples

Input: pre[] = {20, 10, 11, 13, 12}
Output: Yes
The give array represents following BST. In the following BST, every internal
node has exactly 1 child. Therefor, the output is true.
        20
       /
      10
       \
        11
          \
           13
           /
         12
"""

def if_bst_has_one_node(data):
    """Given Preorder traversal of a BST, check if each non-leaf node has only one child.
    Assume that the BST contains unique entries."""
    n = len(data)
    if n>2:
        _min,_max =  [data[n-1], data[n-2]] if data[n-1] < data[n-2] else [data[n-2],data[n-1]]
        for i in range(n-2,0,-1):
            i-=1
            if data[i] < _min:
                _min = data[i]
            elif  data[i] > _max:
                _max = data[i]
            else:
                return False
    return True

arr = [20, 10, 11, 13, 12]
print(if_bst_has_one_node(arr))