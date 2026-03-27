# Problem: Minimum Time to Visit Disappearing Nodes
# Language: python3
# Runtime: 1524 ms
# Memory: 70.6 MB

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], D: List[int]) -> List[int]:
        graph = defaultdict(list)
        T = defaultdict(lambda: inf)
        
        for u,v,t in edges:
            graph[u].append((t,v))
            graph[v].append((t,u))
        h = []
        ans = [-1] * n
        
        ans[0] = 0
        for t,x in graph[0]:
            heappush(h,(t,x))
        
        heappush(h,(0,0))
        while h:
            t,u = heappop(h)
            if D[u] <= t or ans[u] !=-1:
                continue
            
            ans[u] = t
            
            for x,v in graph[u]:
                heappush(h,(t + x,v))
                    
        
        
        
        return ans