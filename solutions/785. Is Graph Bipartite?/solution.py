# Problem: Is Graph Bipartite?
# Language: python3
# Runtime: 164 ms
# Memory: 14.7 MB

from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = {}
        
        for n in range(len(graph)):
            if n not in color:
                color[n] = 0
                
                q = [n]
                while q:
                    node = q.pop()
                    for nb in graph[node]:
                        if nb not in color:
                            q.append(nb)
                            color[nb] = color[node] ^1
                        elif color[nb] == color[node]:
                            return False
        return True 