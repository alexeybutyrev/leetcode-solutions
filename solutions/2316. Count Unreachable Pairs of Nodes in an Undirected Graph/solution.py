# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph
# Language: python3
# Runtime: 2423 ms
# Memory: 108.9 MB

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for u in range(n):
            union(u,u)
        
        for u,v in edges:
            union(u,v)
        
        c = Counter()
        for u in range(n):
            c[find(u)] += 1
        A = list(c.values())

        p = 0
        for v in c.values():
            p += v * (n - v)
            n -= v
        return p
        
        