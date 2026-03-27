# Problem: Minimum Cost Path with Edge Reversals
# Language: python3
# Runtime: 1313 ms
# Memory: 102.8 MB

class Solution:
    def minCost(self, N: int, E: List[List[int]]) -> int:
        graph = defaultdict(lambda: inf)
        g = defaultdict(set)
        for u,v,w in E:
            graph[(u,v)] = min(graph[(u,v)],w)
            graph[(v,u)] = min(graph[(v,u)],2 * w)
            g[u].add(v)
            g[v].add(u)
        
        C = [inf] * N
        C[0] = 0

        q = []
        heappush(q, (C[0],0))

        while q:
            c, u = heappop(q)
            
            for v in g[u]:
                if C[v] > C[u] + graph[(u,v)]:
                    C[v] = C[u] + graph[(u,v)]
                    heappush(q,(C[v], v))
        
        return -1 if C[N-1] == inf else C[N-1]
        