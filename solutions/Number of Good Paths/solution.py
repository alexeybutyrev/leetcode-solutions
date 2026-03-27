# Problem: Number of Good Paths
# Language: python3
# Runtime: 3015 ms
# Memory: 42.8 MB

class Solution:
    def numberOfGoodPaths(self, V: List[int], edges: List[List[int]]) -> int:
        N = len(V)
        F = list(range(N))
        count = [] 
        for i in range(N):
            count.append(Counter({V[i]:1}))
        
        def find(x):
            if x != F[x]:
                F[x] = find(F[x])
            return F[x]
        
        E = sorted( (max(V[u],V[v]),u,v) for u,v in edges)
        
        ans = N
        for x,u,v in E:
            fu, fv = find(u), find(v)
            cu, cv = count[fu][x], count[fv][x]
            ans += cu * cv
            F[fv] = fu
            count[fu] = Counter({x:cu + cv})
        return ans
                   
    
        