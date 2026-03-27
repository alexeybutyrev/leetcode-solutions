# Problem: Cheapest Flights Within K Stops
# Language: python3
# Runtime: 108 ms
# Memory: 14.7 MB

from math import inf
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        
        adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for s, d, w in flights:
            adj_matrix[s][d] = w
        
        distances     = [inf for _ in range(n)]
        current_stops = [inf for _ in range(n)]
        distances[src], current_stops[src] = 0, 0
        
        h = [(0, 0, src)]
        
        while h:
            cost, stops, node = heapq.heappop(h)
            
            if node == dst:
                return cost
            if stops == K + 1:
                continue
                
            for nb in range(n):
                if adj_matrix[node][nb] > 0:
                    dU, dV, wUV = cost, distances[nb], adj_matrix[node][nb]
                    
                    if dU + wUV < dV:
                        distances[nb] = dU + wUV
                        heapq.heappush(h, (dU + wUV, stops + 1, nb))
                    elif stops < current_stops[nb]:
                        current_stops[nb] = stops
                        heapq.heappush(h, (dU + wUV, stops + 1, nb))
                
        return -1 if distances[dst] == inf else distances[dst]