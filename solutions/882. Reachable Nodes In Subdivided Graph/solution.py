# Problem: Reachable Nodes In Subdivided Graph
# Language: python3
# Runtime: 730 ms
# Memory: 21.8 MB

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        
        for u,v,w in edges:
            graph[u][v] = graph[v][u] = w
        
        dist = {0:0}
        ans = 0
        h = []
        heappush(h,(0,0))
        used = {}
        while h:
            d,node = heappop(h)
            if d > dist[node]:
                continue
                
            ans += 1
            for nei,w in graph[node].items():
                v = min(w, maxMoves - d)
                used[(node, nei)] = v
                
                d2 = d + w + 1
                if d2 < dist.get(nei,maxMoves+1):
                    heappush(h,(d2,nei))
                    dist[nei] = d2
        
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))
            
        return ans