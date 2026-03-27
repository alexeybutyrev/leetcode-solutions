# Problem: All Paths from Source Lead to Destination
# Language: python3
# Runtime: 268 ms
# Memory: 21 MB

class Solution:
    def leadsToDestination(self, N: int, edges: List[List[int]], source: int, destination: int) -> bool:
        color = defaultdict(lambda: 1)
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
        
        def dfs(u):
            if color[u] == 2:
                return False
            
            if u == destination and not graph[u]:
                return True
            
            if not graph[u]:
                return False
            
            color[u] = 2
            for v in graph[u]:
                if not dfs(v):
                    return False    
            color[u] = 3
            return True
        
        return  dfs(source)
        
        