import sys
from collections import defaultdict 
goal = 5
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def DFS_Until(self,v,visited): 
  
        visited[v]= True
        print (v, ' ')
        if (v == goal):
            sys.exit()

        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFS_Until(i, visited) 
  
  
    def DFS(self,v): 

        visited = [False]*(len(self.graph)*2)
        self.DFS_Until(v,visited) 
  
  
if __name__ == "__main__":
    g = Graph() 
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 6)
    g.addEdge(6, 5) 
      
    print ("Following is DFS from (starting from vertex 2)")
    g.DFS(1) 
