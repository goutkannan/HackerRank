"""
Implementation of Dijkstra's algo.
"""
from collections import defaultdict
from minHeap import MinHeap


class Graph:
    """
    Basic Graph datastrucutre
    """
    num_of_nodes = 0
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, edge_from, edge_to, weight): # pylint: disable=invalid-name
        """ Adding edges to Graph"""
        self.graph[edge_from].append([edge_to, weight])


def Dijkstra(graph, start):# pylint: disable=invalid-name
    """ Main implementation using Priority Queue"""
    priorityqueue = MinHeap()
    priorityqueue.insertKey(start)

    distance = [-1 for i in range(graph.num_of_nodes)]
    path = [-1 for i in range(graph.num_of_nodes)]
    while not priorityqueue.empty():
        v = priorityqueue.extractMin() # pylint: disable=invalid-name
        print(graph.graph.items(),"...",v)
        for adj, weight in graph.graph.get(v):
            d = distance[v] + weight # pylint: disable=invalid-name
            if distance[adj] == -1:
                distance[adj] = d
                priorityqueue.insertKey(adj)
                priorityqueue.decreaseKey(adj, d)
            elif distance[adj] > d:
                distance[adj] = d
                priorityqueue.decreaseKey(adj, d)
            
            path[adj] = v

    return distance, path

G = Graph()
G.addEdge(0, 1, 12)
G.addEdge(1, 2, 23)
G.addEdge(0, 2, 2)
G.addEdge(1, 3, 26)
G.addEdge(3, 2, 12)
G.addEdge(2, 3, 7)
G.num_of_nodes = 4

Dijkstra(G, 0)

