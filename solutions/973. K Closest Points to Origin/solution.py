# Problem: K Closest Points to Origin
# Language: python3
# Runtime: 5528 ms
# Memory: 19.1 MB

from operator import itemgetter
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda x: x[0]*x[0] + x[1]*x[1]
        
        d = list(map(dist, points))
        
        inds = sorted(range(len(d)), key=lambda k: d[k])[0:K]
        
        res = []
        
        for i in range(len(d)):
            if i in inds:
                res.append(points[i])
        return res
        