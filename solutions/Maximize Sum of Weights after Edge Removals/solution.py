# Problem: Maximize Sum of Weights after Edge Removals
# Language: python3
# Runtime: 4295 ms
# Memory: 259.9 MB

from sortedcontainers import SortedList
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], K: int) -> int:
        N = len(edges)
        graph = defaultdict(list)
        c = defaultdict(SortedList)
        E = {}
        ans = 0
        for u,v,w in edges:
            graph[u].append(v)
            c[u].add((w, v))

            graph[v].append(u)
            c[v].add((w, u))

            E[(u,v)] = w
            E[(v,u)] = w

        
        @cache
        def dp(u, hp, p):
            h = []
            
            for v in graph[u]:
                if v == p: continue
                pick = E[(u,v)] + dp(v,1,u)
                nopick = dp(v,0,u)
                h.append((pick - nopick, v))
            
            h.sort(key = lambda t : t[0], reverse=True)
            cnt = 0
            ans = 0
            for c,v in h:
                
                if c > 0 and cnt < K - hp:
                    ans += E[(u,v)] + dp(v,1,u)
                    cnt += 1
                else:
                    ans += dp(v,0,u)
            return ans
        return dp(0,0,-1)
                    
                    
        
                
            
            