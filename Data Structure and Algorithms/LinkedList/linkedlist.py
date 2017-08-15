class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self,data):
        newNode = Node(data)
        curr = self.head
        if curr == None:
            curr = Node(data)
            return

        while(curr.next):
            curr = curr.next 
        
        
        curr.next = newNode 


    def printList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next 


if __name__=='__main__':
    myList = LinkedList()
    myList.head = Node(2)
    second = Node(13)
    myList.head.next = second 
    myList.insert(24)
    myList.insert(4)
    myList.printList() 
