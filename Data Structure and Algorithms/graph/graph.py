__author__ = 'Goutham'
import itertools
import Queue

from collections import defaultdict

NODE =0
COLOR =1
"""
Uni-directional Graphs
"""
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex = None

    def addEdge_weight(self,edge_from,edge_to,weight):
        self.graph[edge_from].append((edge_to,weight))

    def addEdge(self,edge_from,edge_to):
        self.graph[edge_from].append(edge_to)

    def numVertex(self):
        if not self.vertex:
            self.vertex = max(self.graph.keys()) +1
        return self.vertex

    def test(self):
        for i in (self.graph[0]):
            if i[0] == 1:
                self.graph[0][0][1]="black"

        for k,v in self.graph.items():
            print(k,v)

    def dfs_visit(self, u, color, found_cycle):
        """
        CLRS Implementation of DFS """
        if found_cycle[0]:                          # - Stop dfs if cycle is found.
            return
        color[u] = "gray"                           # - Gray nodes are in the current path

        for v in self.graph[u]:                              # - Check neighbors, where G[u] is the adjacency list of u.
            print(">>>v :",v[0])
            if color[v[0]] == "gray":                  # - Case where a loop in the current path is present.
                found_cycle[0] = True
                return
            if color[v[0]] == "white":                 # - Call dfs_visit recursively.
                self.dfs_visit( v[0], color, found_cycle)
        color[u] = "black"

        print (">>",color.items())

    def nodes(self):
        l=[]
        for k in list(self.graph):
            l.append(k)
            for v in self.graph[k]:
                l.append(v[0])
        return list(set(l))

    def cycle_exists(self):                     # - G is a directed graph
        """
        Using the DFS Visit to find if there is vertex that is already visited
        Note: Not a great way of finding cycles. Union - Find is better """
        color = { u : "white" for u in self.nodes()  }  # - All nodes are initially white
        found_cycle = [False]                # - Define found_cycle as a list so we can change
                                             # its value per reference, see:
                                             # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
        for u in list(self.graph):                          # - Visit all nodes.

            if color[u] == "white":
                self.dfs_visit( u, color, found_cycle)
            if found_cycle[0]:
                break
       # print(".......")
       # print(color.items())
        return found_cycle[0]

    def bfs(self, u=0):
        """ print vertices breath wise """
        visited = [False]*self.numVertex()
        _queue = Queue.Queue()
        _queue.put(u)
        visited[u] = True
        while not _queue.empty():
            v = _queue.get()
            print("Node {}".format(str(v)))
            for child in self.graph[v]:
                if visited[child] == False:
                    _queue.put(child)
                    visited[child] = True

    def DFSUtil(self, node, visited):
        visited[node] = True:
            for child in self.graph[node]:
                if visited[child] == False:
                    self.DFSUtil(child, visited)

    def mother_vertex(self):
        visited = [False] * self.numVertex
        result = None
        for nodes in self.graph:
            if visited[node] == False:
                self.DFSUtil(node, visited)
                result = node

        visited = [False] * self.numVertex
        self.DFSUtil(node, visited)
        return node if all(visited) else -1


g = Graph()

#addEdge(from,to,weight)
g.addEdge(0, 1)
g.addEdge(1, 0)

g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(1, 3)
g.addEdge(3, 1)
g.addEdge(2, 4)
g.addEdge(4, 2)
g.addEdge(10,2)
g.addEdge(2,10)
g.addEdge(3, 4)
g.addEdge(4,3)
g.bfs()
#print (g.cycle_exists())
