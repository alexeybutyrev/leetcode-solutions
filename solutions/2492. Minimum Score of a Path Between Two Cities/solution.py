# Problem: Minimum Score of a Path Between Two Cities
# Language: python3
# Runtime: 1724 ms
# Memory: 58.8 MB

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]


        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)


        for u, v, w in roads:
            union(u,v)
        
        ans = inf
        for u,v,w in roads:
            if find(u) == find(1):
                ans = min(ans, w)
        return ans