# Problem: Erect the Fence
# Language: python3
# Runtime: 467 ms
# Memory: 15 MB

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) < 1:
            return points
        
        
        def cross(o, a, b):
            return (o[0] - a[0]) * (o[1] - b[1]) - (o[1] - a[1]) * (o[0] - b[0])
        
        points.sort()
        low_hull = []
        for p in points:
            while len(low_hull) >= 2 and cross(low_hull[-2],low_hull[-1], p) < 0:
                low_hull.pop()
            low_hull.append(p)
        
        high_hull = []
        for p in reversed(points):
            while len(high_hull) >= 2 and cross(high_hull[-2],high_hull[-1], p) < 0:
                high_hull.pop()
            high_hull.append(p)
        
        ans = set()
        for a,b in low_hull:
            ans.add((a,b))
        
        for a,b in high_hull:
            ans.add((a,b))
        
        return list(ans)
        