# Problem: Connecting Cities With Minimum Cost
# Language: python3
# Runtime: 728 ms
# Memory: 22.6 MB

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        A = [(cost,u,v) for u,v,cost in connections]
        
        A.sort()
        for u in range(1,n+1):
            union(u,u)
        
        ans = 0
        for c,u,v in A:
            if find(u) != find(v):
                ans += c
                union(u,v)
        
        
        return ans if len({find(u) for u in range(1,n+1)})==1 else -1
        