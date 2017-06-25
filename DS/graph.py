__author__ = 'Goutham'
import itertools

from collections import defaultdict

NODE =0
COLOR =1
"""
Uni-directional Graphs 
"""

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,edge_from,edge_to,weight):

        self.graph[edge_from].append([edge_to,weight])

    def test(self):
        for i in (self.graph[0]):
            if i[0] == 1:
                self.graph[0][0][1]="black"

        for k,v in self.graph.items():
            print(k,v)

    """
    CLRS Implementation of DFS 

    """
    def dfs_visit(self, u, color, found_cycle):
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

    """
    Using the DFS Visit to find if there is vertex that is already visited 
    Note: Not a great way of finding cycles. Union - Find is better 
    
    """
    def cycle_exists(self):                     # - G is a directed graph
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



g = Graph()

#addEdge(from,to,weight)
g.addEdge(0, 1,5)
g.addEdge(0, 2,0)
g.addEdge(1, 3,0)
g.addEdge(2, 4,0)
g.addEdge(3, 2,0)

print (g.cycle_exists())
