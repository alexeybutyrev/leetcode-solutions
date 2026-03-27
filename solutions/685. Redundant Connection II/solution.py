# Problem: Redundant Connection II
# Language: python3
# Runtime: 1930 ms
# Memory: 16.2 MB

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        c = Counter() 
        nodes = set()
        for u,v in edges:
            graph[u].add(v)
            nodes.add(u)
            nodes.add(v)
            c[v] += 1
        
        
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            
            for nb in graph[node]:
                if not dfs(nb):
                    return False
            return True
        
        N = len(nodes)
        ans = []
        for u,v in edges:
            graph[u].remove(v)
            
            c[v]-=1
            if c[v] == 0:
                root = v
            for root in nodes:
                seen = set()
                if not c[root] and dfs(root) and len(seen) == N:
                    ans = [u,v]
            c[v] += 1
            graph[u].add(v)
        
        return ans