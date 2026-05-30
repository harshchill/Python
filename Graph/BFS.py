class graph :
    def  __init__(self,vector):
        self.mat = [[0]*vector for x in range(vector)]
        self.size = vector

    def add_edge(self,src,dest):

        if 0<= src <self.size  and 0 <= dest < self.size:

            self.mat[src][dest] = 1
            self.mat[dest] [src] = 1
        else :
            print("invalid edge")

    def bfs(self,src):
        visited = [False]*self.size
        Queue = [src]

        

        while Queue:
         
         vec = Queue.pop(0)

         if visited[vec] == False:
            visited[vec] = True
            print(vec ,end="--->")

         for i in range(self.size):
            if  self.mat[vec][i] == 1 and visited[i] == 0:
                Queue.append(i)

        


g = graph(6)

g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,5)
g.add_edge(3,4)
g.add_edge(4,5)

g.bfs(0)


