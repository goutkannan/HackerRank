"""
Function to check if a singly linked list is palindrome
"""
from linkedlist import LinkedList, Node
left = None

def isPalindrome(right):
    if right is None:
        return True

    f = isPalindrome(right.next)
    if f is False:
        return False
    
    global left 
    flag= (left.data == right.data) 

    left = left.next
    return flag

    

llist1 = LinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(7)
llist1.insert(4)
llist1.insert(2)
llist1.printList()

left = llist1.head 
print(isPalindrome(llist1.head) )






