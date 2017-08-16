"""
Merge two sorted linked lists such that merged list is in reverse order
Given two linked lists sorted in increasing order. Merge them such a way that the result list is in decreasing order (reverse order).

Examples:

Input:  a: 5->10->15->40
        b: 2->3->20 
Output: res: 40->20->15->10->5->3->2

Input:  a: NULL
        b: 2->3->20 
Output: res: 20->3->2
""" 
from linkedlist import LinkedList,Node

def merge_n_reverse(llist1,llist2):
    curr1 = llist1.head
    curr2 = llist2.head
    myList = LinkedList()
    while(curr1 and curr2):
        if curr1.data > curr2.data:
            myList.insertFront(curr2.data)
            curr2 = curr2.next
        else:
            myList.insertFront(curr1.data)
            curr1 = curr1.next

    #Left overs in either list
    while(curr1):
        myList.insertFront(curr1.data)
        curr1 = curr1.next
    
    while(curr2):
        myList.insertFront(curr2.data)
        curr2 = curr2.next

    return myList

llist1 = LinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(8)
llist1.insert(12)
llist1.insert(20)

llist2 = LinkedList()
llist2.head = Node(1)
llist2.insert(14)
llist2.insert(27)
llist2.insert(38)

print("Befor Merge Sort")
llist1.printList()
print("....")
llist2.printList()
print("....")

Finallist = LinkedList()
Finallist = merge_n_reverse(llist1,llist2)
Finallist.printList()


#Beautiful - Gok 

