# Problem: Maximal Network Rank
# Language: python3
# Runtime: 308 ms
# Memory: 18.2 MB

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = 0
        for u in range(n):
            for v in range(u+1,n):
                ans = max(ans, len(graph[u]) + len(graph[v])-  int(u in graph[v])  )
        
        return ans