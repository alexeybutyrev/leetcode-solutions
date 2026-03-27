# Problem: Optimize Water Distribution in a Village
# Language: python3
# Runtime: 500 ms
# Memory: 22.4 MB

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        h = []
        
        for i, x in enumerate(wells):
            heappush(h, (x,i+1))
        
        graph = defaultdict(set)
        for x,y,c in pipes:
            graph[x].add((c,y))
            graph[y].add((c,x))
        
        seen = {0}
        ans = 0
        while len(seen) < n + 1:
            c, x = heappop(h)
            if x not in seen:
                seen.add(x)
                ans += c
                
                for c, node in graph[x]:
                    if node not in seen:
                        heappush(h, (c,node))
        
        return ans