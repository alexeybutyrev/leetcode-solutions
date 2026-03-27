# Problem: Minimum Weighted Subgraph With the Required Paths
# Language: python3
# Runtime: 2962 ms
# Memory: 89.2 MB

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
        def dra(adj,node,n):
            dist = [inf] * n
            h = []
            heappush(h, (0,node))
            dist[node] = 0
            while h:
                d,u = heappop(h)
                if d > dist[u]: continue
                for v,w in adj[u]:
                    dv = d + w
                    if dv < dist[v]:
                        dist[v] = dv
                        heappush(h,(dv, v))
            
            return dist
        
        adj = defaultdict(list)
        adj_reversed = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj_reversed[v].append((u,w))
        
        
        a = dra(adj,src1,n)
        b = dra(adj,src2,n)
        c = dra(adj_reversed,dest,n)

        ans = min(a[i] + b[i] + c[i] for i in range(n))
        
        return -1 if ans == inf else ans
    
        
        
            
            