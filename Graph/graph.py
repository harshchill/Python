class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for x in range(vertex)]
        self.size=vertex

    def add_edge(self,src,dest):
        if ( 0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("this is an invalid edge")
            return None
        
    def print(self):
        for row in self.mat:
            print(" ".join(map(str,row)))


G = Graph(3)
G.add_edge(1,0)
G.add_edge(1,2)
G.add_edge(2,0)

G.print()