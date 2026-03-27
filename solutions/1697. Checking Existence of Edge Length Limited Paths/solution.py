# Problem: Checking Existence of Edge Length Limited Paths
# Language: python3
# Runtime: 2343 ms
# Memory: 60.3 MB

from itertools import product
class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges.sort(key = lambda x: x[2])
        queries = [(l,i,p,q) for i,(p,q,l) in enumerate(queries)]
        queries.sort()
        
        
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        
        for i in range(n):
            union(i,i)
        
        NQ = len(queries)
        ans = [False] * NQ
        NE = len(edges)
        j = 0
        for l,i,p,q in queries:
            while j < NE and edges[j][2] < l:
                union(edges[j][0],edges[j][1])
                j += 1
            
            ans[i] = find(p) == find(q)
        
        return ans