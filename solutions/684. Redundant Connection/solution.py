# Problem: Redundant Connection
# Language: python3
# Runtime: 52 ms
# Memory: 15.1 MB

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        seen = set()
        def dfs(u,v):
            if u == v:
                return True
            for n in graph[u]:
                if n not in seen:
                    seen.add(n)
                    if dfs(n,v):
                        return True
            return False
        
        graph = defaultdict(set)
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)
        return []
                    