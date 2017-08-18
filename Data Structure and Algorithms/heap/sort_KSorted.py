"""
Sort a nearly sorted (or K sorted) array
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
""" 

from minHeap import MinHeap 

def ksort(inputlist, k ):
    indx =1
    heap = MinHeap()
    res = []
    heap.insertKey(inputlist[0])
    while len(heap.heap)>0:
        for i in range(k+1):
            if indx < len(inputlist):
                heap.insertKey(inputlist[indx])
                indx+=1
        minValue = heap.extractMin()
        res.append(minValue)
           
    return res 

inputlist= [2, 6, 3, 12, 56, 8]
print(ksort(inputlist,k=3))


