# Problem: Graph Valid Tree
# Language: python3
# Runtime: 104 ms
# Memory: 15.5 MB

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(y)] = find(x)
        
        for i in range(n):
            union(i,i)
            
        for u,v in edges:
            if find(u) == find(v):
                return False
            union(u,v)
        
        return len( {find(u) for u in range(n)}) == 1