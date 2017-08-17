from linkedlist import LinkedList,Node

class CircularLinkedList(LinkedList):
    def printList(self):
        current = self.head
        if current is not None:
            while(True):
                print(current.data,end=' ')
                current = current.next 
                if(current.data == self.head.data):
                    break
        
llist1 = CircularLinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(7)
llist1.insert(4)
llist1.insert(2)
llist1.printList()