from linkedlist import LinkedList,Node

class LinkedList(LinkedList):
    #Nth node from the last 
    def printNthNode(self,n):
        runner = self.head
        current = self.head

        while(n>=0):
            runner = runner.next 
            n-=1

        while(runner is not None):
            runner = runner.next
            current = current.next 

        return current.data

llist1 = LinkedList()
llist1.head = Node(2)

llist1.insert(4)
llist1.insert(7)
llist1.insert(8)
llist1.insert(12)
llist1.insert(20)
llist1.printList()
print(llist1.printNthNode(3))



        


