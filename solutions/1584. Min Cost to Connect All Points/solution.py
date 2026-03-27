# Problem: Min Cost to Connect All Points
# Language: python3
# Runtime: 735 ms
# Memory: 83.3 MB

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        dist = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        N = len(points)
        if N <= 1:
            return 0
        E = []
        for i in range(N):
            union(i,i)
            for j in range(i+1,N):
                heappush(E,(dist(points[i],points[j]),i,j))
        
        seen = set()
        cost = 0
        count = 0
        while count != N -1:
            d, x, y = heappop(E)
            if find(x) == find(y):
                continue
            union(x,y)
            count += 1
            seen.add(x)
            seen.add(y)
            cost += d

        return cost