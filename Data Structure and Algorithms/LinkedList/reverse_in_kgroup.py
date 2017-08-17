"""Reverse a Linked List in groups of given size | Set 1
Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
Output:  3->2->1->6->5->4->8->7->NULL. 

Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL. """

from linkedlist import LinkedList,Node

class LinkedList(LinkedList):
    
   # cool implementation of reverse with 
    def reverse(self, head, k):
        current = head
        nextNode = None
        prev = None
        count =0 
        while current is not None and count<k:
            nextNode = current.next 
            current.next = prev 
            prev = current            
            current = nextNode 
            count+=1

        if nextNode is not None:
            head.next = self.reverse(nextNode,k)
        
        return prev        

llist1 = LinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(8)
llist1.insert(12)
llist1.insert(20)
llist1.printList()

llist1.head = llist1.reverse(llist1.head,3)
llist1.printList()