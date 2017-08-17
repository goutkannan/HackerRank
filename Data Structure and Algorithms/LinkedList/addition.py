"""
Add two numbers represented by linked lists | Set 1
Given two numbers represented by two lists, write a function that returns sum list. The sum list is list representation of addition of two input numbers.

Example 1

Input:
  First List: 5->6->3  // represents number 365
  Second List: 8->4->2 //  represents number 248
Output
  Resultant list: 3->1->6  // represents number 613
Example 2

Input:
  First List: 7->5->9->4->6  // represents number 64957
  Second List: 8->4 //  represents number 48
Output
  Resultant list: 5->0->0->5->6  // represents number 65005

  Assumption : Making an assumption that input list contains all
  elements that is less than 10. 

"""
from linkedlist import LinkedList,Node

def addition(llist1,llist2):
    curr1 = llist1.head
    curr2 = llist2.head
    myList = LinkedList()
    carry = 0 
    temp = None 

    while(curr1 is not None or curr2 is not None):
        lvalue= curr1.data if curr1 else 0
        rvalue= curr2.data if curr2 else 0 

        val = lvalue + rvalue + carry
        carry = 1 if  val >10 else 0
        val = val % 10 

        newNode = Node(val)
        if myList.head is None:
            myList.head = newNode
            temp = myList.head
        else:
            temp.next = newNode
            temp = temp.next  
        
        if curr1 is not None:
            curr1 = curr1.next
        if curr2 is not None:
            curr2 = curr2.next 

    if carry>0:
        temp.next = Node(carry) 
    
    return myList

llist1 = LinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(8)
llist1.insert(2)
llist1.insert(5)

llist2 = LinkedList()
llist2.head = Node(1)
llist2.insert(4)
llist2.insert(7)
llist2.insert(8)
llist2.insert(8)
llist2.insert(8)

print("Befor Merge Sort")
llist1.printList()
print("....")
llist2.printList()
print("....")

Finallist = LinkedList()
Finallist = addition(llist1,llist2)
Finallist.printList()
