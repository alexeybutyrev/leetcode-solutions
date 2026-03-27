# Problem: Satisfiability of Equality Equations
# Language: python3
# Runtime: 60 ms
# Memory: 14.6 MB

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
            
        for e in equations:
            a = e[0]
            b = e[3]
            union(a,a)
            union(b,b)
            if e[1:3] == "==":
                union(a,b)
        
        for e in equations:
            a = e[0]
            b = e[3]
            if e[1:3] == "!=" and find(a) == find(b):
                return False
        
        return True
                