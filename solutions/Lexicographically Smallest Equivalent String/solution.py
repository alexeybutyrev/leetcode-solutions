# Problem: Lexicographically Smallest Equivalent String
# Language: python3
# Runtime: 40 ms
# Memory: 14 MB

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
            
        
        for l1,l2 in zip(s1,s2):
            union(l1,l2)
        
        d = defaultdict(set)
        for l in set(s1) | set(s2):
            d[find(l)].add(l)
        
        min_map = {}
        for k,v in d.items():
            m = min(k,min(v))
            for l in {k} | v:
                min_map[l] = m
        
        ans = ""
        for l in baseStr:
            if l in min_map:
                ans += min_map[l]
            else:
                ans += l
        return ans