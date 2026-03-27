# Problem: Shortest Path Visiting All Nodes
# Language: python3
# Runtime: 668 ms
# Memory: 41.4 MB

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        T = (1 << N) - 1
        
        hm = {}
        def dp(node,mask):
            state = (node, mask)
            if state in hm:
                return hm[state]
            
            if mask & (mask - 1) == 0: return 0
            
            hm[state] = inf
            for nb in graph[node]:
                if mask & (1<<nb):
                    c1 = 1 + dp(nb, mask)
                    c2 = 1 + dp(nb, mask ^ (1<<node))
                    hm[state] = min(hm[state],c1,c2)
            return hm[state]
        

        return min(dp(node,T) for node in range(N))