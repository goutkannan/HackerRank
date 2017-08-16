from linkedlist import LinkedList,Node
class LinkedList(LinkedList):
    def deleteIndex(self,indx):
        curr = self.head
        if indx ==0:
            self.head = curr.next 
        else:
            for i in range(0,indx-1):
                if curr:
                    curr = curr.next 
                else:
                    print("Index Out of Range")
                    return

            if curr is not None  and curr.next is not None:
                curr.next = curr.next.next 
            
        


myList = LinkedList() 
myList.head = Node(1)
myList.insert(2)
myList.insert(4)
myList.insert(5)
myList.insert(12)
myList.insert(7)
myList.insert(6)
myList.printList()
myList.deleteIndex(11)
print("\n")
myList.printList()

