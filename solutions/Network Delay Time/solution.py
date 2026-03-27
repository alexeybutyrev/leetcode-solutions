# Problem: Network Delay Time
# Language: python3
# Runtime: 448 ms
# Memory: 16.3 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        T = [inf] * n
        k-=1
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u-1].append((w,v-1))
        
        T[k] = 0
        
        h = []
        
        heappush(h,(0,k))
        while h:

            d, u = heappop(h)
            for w,v in graph[u]:
                if w + d < T[v]:
                    heappush(h,(w+d,v))
                    T[v] = w + d
        
        s = max(T)
        return -1 if s == inf else s