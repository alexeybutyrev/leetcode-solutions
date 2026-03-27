# Problem: Design Graph With Shortest Path Calculator
# Language: python3
# Runtime: 1515 ms
# Memory: 19.9 MB

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.d = defaultdict(lambda : inf)
        for u,v,w in edges:
            self.addEdge([u,v,w])

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        self.graph[u].append(v)
        self.d[(u,u)] = 0
        self.d[(v,v)] = 0
        if self.d[(u,v)] > w:
            self.d[(u,v)] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        #print(self.d)
        q = []
        heappush(q, (0,node1))
        while q:
            c, node = heappop(q)
            if node == node2: return c
            for nb in self.graph[node]:
                if self.d[(node1, nb)] >= c + self.d[(node, nb)]:
                    self.d[(node1, nb)] = c + self.d[(node, nb)]
                    heappush(q,(self.d[(node1, nb)],nb))
        
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)