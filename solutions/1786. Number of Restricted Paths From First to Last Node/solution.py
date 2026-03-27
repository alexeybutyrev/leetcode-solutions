# Problem: Number of Restricted Paths From First to Last Node
# Language: python3
# Runtime: 3631 ms
# Memory: 43.6 MB

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10** 9 + 7
        graph = defaultdict(list)
        G = defaultdict(set)
        for u,v,w in edges:
            graph[(u,v)] = w
            graph[(v,u)] = w
            G[u].add(v)
            G[v].add(u)
        
        dist = defaultdict(lambda: inf)
        dist[n] = 0
        pq = [[0, n]]
        
        count = 0
        while pq:
            d, node = heappop(pq)
            if d > dist[node]:
                continue
            for nei in G[node]:
                w = graph[(node,nei)]
                d2 = w + d
                if d2 < dist[nei]:
                    dist[nei] = d2
                    heappush(pq, [d2,nei])
        

        # dp
        dp = defaultdict(int)
        dp[1] = 1
        for node in list(sorted(dist, key=dist.__getitem__, reverse = True)):
            for nb in G[node]:
                if dist[nb] < dist[node]:
                    dp[nb] += dp[node]
                    dp[nb] %= MOD
        
        return dp[n]