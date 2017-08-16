class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def getCount(self):
        count=0
        curr = self.head 
        while(curr):
            curr = curr.next
            count+=1

        return count

    def getCountRec(self,head):
        if head==None:
            return 0

        return 1+ self.getCountRec(head.next)

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
            print(curr.data,end=' --> ')
            curr = curr.next 
        print('\n')
        
    def insertAfter(self,old_node,new_data):
        if old_node == None:
            print("Nothing is present")
        else:
            new_node  = Node(new_data) 
            old_node.next  = new_node 

    def insertFront(self,data):
        new_head = Node(data)
        new_head.next = self.head
        self.head  = new_head 

    def deleteKey(self,key):
        curr = self.head
        prev = curr 
        if curr and curr.data == key:
            self.head = curr.next 
            curr = None
            return 

        while(curr):
            if curr.data ==key:
                break 
            prev = curr 
            curr  = curr.next 
        
        if(curr):
            prev.next = curr.next
            curr = None  
        else:
            return 






if __name__=='__main__':
    myList = LinkedList()
    myList.head = Node(2)
    second = Node(13)
    myList.head.next = second 
    myList.insert(24)
    myList.insert(4)
    myList.insertFront(1)

    myList.printList() 
    i = 4
    print("\nDeleting {}....".format(str(i)))
    myList.deleteKey(i)
    myList.printList() 
    
    print("\n",myList.getCountRec(myList.head))


