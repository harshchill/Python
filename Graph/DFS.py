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
        
    def dfs(self,src):
        visited = [False] * self.size
        stack = [src]

        while stack :
            node = stack.pop()

            if visited[node] == False:
                visited[node] = True
                print(node , end="-->")
            
            for i in range(self.size):
                if self.mat[node][i] == 1 and visited[i] == False:
                    stack.append(i)


g = Graph(6)

g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,5)
g.add_edge(3,4)
g.add_edge(4,5)

g.dfs(0)
        

