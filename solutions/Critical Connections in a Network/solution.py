# Problem: Critical Connections in a Network
# Language: python3
# Runtime: 2484 ms
# Memory: 114.3 MB

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(set)

        for i, (u,v) in enumerate(connections):
            graph[u].add(v)
            graph[v].add(u)
            
        low = {}
        seen = set()
        ans = []
        def dfs(id, prev, node):
            seen.add(node)
            low[node] = id
            for n in graph[node]:
                if n == prev:
                    continue
                
                if n not in seen:
                    dfs(id+1, node, n)
                
                low[node] = min(low[node], low[n])
                if id < low[n]:
                    ans.append([node, n])

        dfs(0, -1, 0)
        return ans
        
        
        
        