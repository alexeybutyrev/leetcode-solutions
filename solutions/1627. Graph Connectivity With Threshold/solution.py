# Problem: Graph Connectivity With Threshold
# Language: python3
# Runtime: 996 ms
# Memory: 49.5 MB

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold == 0:
            return [True] * len(queries)
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        graph = defaultdict(list)
        for i in range(1,n+1):
            union(i,i)
            
        for z in range(threshold+1, n//2 +1):
            for j in range(z,n+1,z):
                union(z,j)
        
        
            
        
        seen = {}
        ans = []
        for x,y in queries:
            if (x,y) not in seen:
                seen[(x,y)] = find(x) == find(y)
            ans.append(seen[(x,y)])
        return ans
                    