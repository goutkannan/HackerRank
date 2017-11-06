from heapq import heappush, heappop, heapify 


class MinHeap:
     
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
 
    def empty(self):
        return True if not self.heap else False

    def parent(self, i):
        return (i-1)/2
     
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           
 
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    """def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])"""
    
    def decreaseKey(self, i ,new_val):
        self.heap.insert(i, new_val) 
        heapify(self.heap)

    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
 
    
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
 
    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


if __name__=='__main__':
    heap = MinHeap()
    heap.insertKey(2)
    heap.insertKey(3)
    heap.insertKey(7)
    heap.insertKey(1)
    heap.insertKey(9)
    heap.insertKey(4)
    heap.insertKey(20)
    heap.insertKey(12)
    heap.deleteKey(0)

    print(heap.extractMin()) 
    print(heap.getMin())
    heap.decreaseKey(2,1)
    print(heap.getMin())
