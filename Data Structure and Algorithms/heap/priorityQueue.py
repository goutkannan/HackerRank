"""
Priority queue usage using inbuild module
"""
from queue import PriorityQueue

q = PriorityQueue()

q.put((0,10))
q.put((10,0))
q.put((12,20))
q.put((2,20))


while not q.empty():
    next_item = q.get()
    print(next_item)