class UnDirGraph:
    def __init__(self,numn):
        self.V = numn
        self.G = []

    def addEdge(self,edgefrom,edgeto,edgeweight):
        self.G.append([edgefrom,edgeto,edgeweight])

    def find(self,i,parent):

        if(parent[i]==i):
            return i
        return self.find(parent[i],parent)

    def union(self,x,y,parent,rank):
        xfind = self.find(x,parent)
        yfind = self.find(y,parent)

        if rank[xfind] > rank[yfind]:
            parent[yfind] = xfind
        elif rank[yfind] > rank[xfind]:
            parent[xfind]=yfind
        else:
            parent[yfind] = xfind
            rank[xfind]+=1

    def Kruskal_MST(self):
        res =[]
        parent= [i for i in range(self.V)]
        rank =[0]*self.V
        count =0
        idx=0

        self.G = sorted(self.G,key=lambda item:item[2])
        while count < self.V -1:

            src,dest,weight = self.G[idx]

            idx+=1
            x= self.find(src,parent)
            print(src,">",dest)
            y= self.find(dest,parent)

            if x!=y:
                count+=1
                res.append([src,dest,weight])

                self.union(x,y,parent,rank)
            else:
                print(src,dest,"Forms cycle")
        return res


g = UnDirGraph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print(g.Kruskal_MST())





