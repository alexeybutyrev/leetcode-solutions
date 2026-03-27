# Problem: Cheapest Flights Within K Stops
# Language: python3
# Runtime: 241 ms
# Memory: 15.2 MB

class Solution:
    def findCheapestPrice(self, N: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[v].append((u,w))
        
        C = [inf] * N
        C[src] = 0
        
        for _ in range(K+1):
            copy = C[:]
            for u in range(N):
                for (v,w) in graph[u]:
                    copy[u] = min(copy[u], C[v] + w)
            C = copy

        return -1 if C[dst] == inf else C[dst]