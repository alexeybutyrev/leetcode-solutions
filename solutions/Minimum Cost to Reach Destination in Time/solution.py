# Problem: Minimum Cost to Reach Destination in Time
# Language: python3
# Runtime: 8908 ms
# Memory: 41 MB

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], F: List[int]) -> int:
        n=len(F)
        dp = [ [inf] * (maxTime+1) for i in range(n) ]
        
        dp[0][0] = F[0]
        
        
        graph = defaultdict(list)
        d = defaultdict(lambda: inf)
        for u,v,c in edges:
            graph[u].append(v)
            graph[v].append(u)
            d[(u,v)] = d[(v,u)] = min(c, d[(u,v)] )
        
        q = []
        heappush(q, (F[0],0,0))
        while q:
            #print(q)
            cost, time, u = heappop(q)
            if u == n - 1:
                return cost
            for v in graph[u]:
                #print(time,v)
                t = time + d[(u,v)]
                if t <= maxTime and dp[v][t] >  cost + F[v] :
                    dp[v][t] =  cost + F[v]
                    heappush(q,(dp[v][t],t, v))
        
        #print(dp[-1])
        ans = min(dp[-1])
        return -1 if ans == inf else ans
        