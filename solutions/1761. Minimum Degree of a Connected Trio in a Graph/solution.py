# Problem: Minimum Degree of a Connected Trio in a Graph
# Language: python3
# Runtime: 8744 ms
# Memory: 39.6 MB

from collections import defaultdict
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = inf
        for u in range(1,n+1):
            for v in range(u+1, n+1):
                for w in range(v+1, n+1):
                    if v in graph[u] and w in graph[u] and v in graph[w]:
                        d = len(graph[u]) + len(graph[v]) + len(graph[w]) - 6
                        if d < ans:
                            ans = d
        
        return -1 if ans == inf else ans
                        
                    
            