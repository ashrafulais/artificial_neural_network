'''
1{2, 3}
2{5}
3{4, 6}
4{}
5{6}
'''

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    #BFS starts
    def BFS(self, s, g): 
  
        visited = [False] * (len(self.graph)*2) 
        queue = []
  
        queue.append(s) 
        visited[s] = True
  
        while queue: 
            s = queue.pop(0) 
            print (s, " ")
            if(s == g):
                break
  
            for i in self.graph[s]:
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True


#main_funciton
if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 6)
    g.addEdge(6, 5)

    print("BFS starting from vertex 1 to 5:\n")
    g.BFS(1, 5)
