# Problem: Network Delay Time
# Language: python3
# Runtime: 587 ms
# Memory: 17 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = Counter()
        graph = defaultdict(list)
        
        for u,v,w in times:
            graph[u].append(v)
            time[(u,v)] = w
        
        seen = {k}
        
        q = []
        heappush(q, (0,k))
            
        D = defaultdict(lambda : inf)
        
        D[k] = 0
        ans = -1
        while q:
            t, u = heappop(q)
            for v in graph[u]:
                t0 = t + time[(u,v)]
                if v not in D or D[v] > t0:
                    D[v] = t0
                    heappush(q,(t0,v))
        
        return max(D.values()) if len(D) == n else -1
            