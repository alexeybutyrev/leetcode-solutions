# Problem: Path with Maximum Probability
# Language: python3
# Runtime: 1064 ms
# Memory: 25.1 MB

from collections import defaultdict
from copy import deepcopy
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        
        
        graph = defaultdict(dict)
        for i, (u,v) in enumerate(edges):
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
        
        q = [(start,1)]
        possibility = [0] * n
        possibility[start] = 1
        
        while q:
            u, pos = q.pop(0)
            if u == end: continue
            for v,p in graph[u].items():
                if p * pos > possibility[v]:
                    q.append((v,p*pos))
                    possibility[v] = p * pos
                
        
        
        return possibility[end]
